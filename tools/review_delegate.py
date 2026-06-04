#!/usr/bin/env python3
"""Run an application-review prompt through Kiro first, with Claude fallback."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


def read_prompt(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text)


def run_command(command: list[str], prompt: str, timeout: int) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.setdefault("NO_COLOR", "1")
    env.setdefault("TERM", "dumb")
    return subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        timeout=timeout,
        env=env,
        check=False,
    )


def backend_command(name: str, args: argparse.Namespace) -> list[str]:
    if name == "kiro":
        executable = shutil.which(args.kiro_executable)
        if executable is None:
            raise FileNotFoundError(args.kiro_executable)

        command = [
            executable,
            "chat",
            "--no-interactive",
            "--wrap",
            "never",
            "--model",
            args.kiro_model,
        ]
        if args.kiro_agent:
            command.extend(["--agent", args.kiro_agent])
        if args.kiro_trust_all_tools:
            command.append("--trust-all-tools")
        return command

    if name == "claude":
        executable = shutil.which(args.claude_executable)
        if executable is None:
            raise FileNotFoundError(args.claude_executable)

        return [
            executable,
            "-p",
            "--model",
            args.claude_model,
        ]

    raise ValueError(f"Unsupported backend: {name}")


def try_backend(name: str, prompt: str, args: argparse.Namespace) -> tuple[bool, str]:
    try:
        command = backend_command(name, args)
    except FileNotFoundError as exc:
        return False, f"{name}: executable not found: {exc}"

    print(f"review_delegate: running {name} backend", file=sys.stderr)
    try:
        result = run_command(command, prompt, args.timeout)
    except subprocess.TimeoutExpired:
        return False, f"{name}: timed out after {args.timeout}s"

    stdout = strip_ansi(result.stdout) if args.strip_ansi else result.stdout
    stderr = strip_ansi(result.stderr) if args.strip_ansi else result.stderr

    if result.returncode == 0 and stdout.strip():
        sys.stdout.write(stdout)
        if not stdout.endswith("\n"):
            sys.stdout.write("\n")
        return True, ""

    details = stderr.strip() or stdout.strip() or "no output"
    return False, f"{name}: exited {result.returncode}: {details}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a job-application reviewer prompt with Kiro CLI and optional Claude fallback."
    )
    parser.add_argument("prompt_file", nargs="?", default="-", help="Prompt file path, or '-' for stdin")
    parser.add_argument(
        "--backend",
        choices=["auto", "kiro", "claude"],
        default=os.environ.get("REVIEW_AGENT_BACKEND", "auto"),
        help="Review backend. auto tries Kiro first, then Claude.",
    )
    parser.add_argument("--timeout", type=int, default=900, help="Per-backend timeout in seconds")
    parser.add_argument("--kiro-executable", default=os.environ.get("KIRO_CLI", "kiro-cli"))
    parser.add_argument("--kiro-agent", default=os.environ.get("KIRO_AGENT", "job-application-reviewer"))
    parser.add_argument("--kiro-model", default=os.environ.get("KIRO_MODEL", "auto"))
    parser.add_argument(
        "--kiro-trust-all-tools",
        action="store_true",
        help="Allow Kiro to use all tools. Use only in trusted workspaces.",
    )
    parser.add_argument("--claude-executable", default=os.environ.get("CLAUDE_CLI", "claude"))
    parser.add_argument("--claude-model", default=os.environ.get("CLAUDE_MODEL", "sonnet"))
    parser.add_argument("--strip-ansi", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prompt = read_prompt(args.prompt_file)
    if not prompt.strip():
        print("review_delegate: prompt is empty", file=sys.stderr)
        return 2

    backends = ["kiro", "claude"] if args.backend == "auto" else [args.backend]
    failures: list[str] = []
    for backend in backends:
        ok, message = try_backend(backend, prompt, args)
        if ok:
            return 0
        failures.append(message)
        print(f"review_delegate: {message}", file=sys.stderr)

    print("review_delegate: all backends failed", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

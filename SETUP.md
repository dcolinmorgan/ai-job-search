# Setup Guide

Step-by-step instructions for getting the AI Job Search framework running.

## 1. Prerequisites

### Assistant CLI

Install at least one assistant CLI. The original command workflow uses Claude Code:

```bash
npm install -g @anthropic-ai/claude-code
```

You'll need an Anthropic API key or a Claude Pro/Team subscription. See the [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code) for details.

Kiro CLI is optional but recommended for the reviewer delegate:

```bash
kiro-cli chat --help
```

The repo's review runner uses Kiro first and falls back to Claude:

```bash
python tools/review_delegate.py --help
```

### Python

Python 3.10+ is required for the salary lookup tool. Check with:

```bash
python --version
```

### Bun (for Danish job search tools)

The Danish job portal CLIs are written in TypeScript and run with Bun. US and Sweden searches use WebSearch/site-query patterns and do not require Bun unless you also use the Danish CLIs.

```bash
curl -fsSL https://bun.sh/install | bash
```

### LaTeX (for compiling CVs and cover letters)

Install a LaTeX distribution to compile the generated `.tex` files to PDF:

- **Windows:** [MiKTeX](https://miktex.org/download)
- **macOS:** [MacTeX](https://tug.org/mactex/)
- **Linux:** `sudo apt install texlive-full` or `sudo dnf install texlive-scheme-full`

The CV compiles with `lualatex` (pdflatex often fails on modern MiKTeX installs with `fontawesome5` font-expansion errors). The cover letter compiles with `xelatex` because `cover.cls` requires `fontspec` for its custom Lato/Raleway fonts.

## 2. Fork and clone

```bash
gh repo fork MadsLorentzen/ai-job-search --clone
cd ai-job-search
```

Or manually: fork on GitHub, then clone your fork.

## 3. Install job search CLI dependencies

This step is required for the Danish portal CLIs. You can skip it if you only use US/Sweden WebSearch-based searches.

```bash
for tool in jobbank-search jobdanmark-search jobindex-search jobnet-search; do
  cd .agents/skills/$tool/cli && bun install && cd ../../../..
done
```

## 4. Run the setup interview

Start Claude Code in the repository:

```bash
claude
```

Then run the onboarding:

```
/setup
```

The assistant will offer two paths:

- **Path A (recommended):** Share your existing CV (mention the file with `@` or paste the text). The assistant extracts your information and asks follow-up questions for anything missing.
- **Path B:** Answer structured interview questions section by section.

Both paths produce the same result: fully populated profile files.

### What gets populated

| File | Content |
|------|---------|
| `CLAUDE.md` | Your full candidate profile |
| `01-candidate-profile.md` | Structured education, experience, skills |
| `02-behavioral-profile.md` | Behavioral assessment |
| `04-job-evaluation.md` | Personalized skill match areas and career goals |
| `05-cv-templates.md` | Profile statement templates for your background |
| `07-interview-prep.md` | STAR examples from your experience |
| `08-market-localization.md` | US, Sweden, Denmark document/search conventions |
| `cv/main_example.tex` | Your LaTeX CV with actual details |
| `search-queries.md` | Job search queries for `/scrape` |

### Re-running setup

You can update specific sections later:

```
/setup --section skills
/setup --section experience
/setup --section search
```

The `--section search` option is especially useful as your priorities evolve. It re-runs the search configuration interview, asks which target markets to search (`us`, `sweden`, `denmark`, or custom), and suggests role/title variants you may not have considered based on your full profile.

## 5. Optional: Set up salary benchmarking

If you have salary data (from a union, salary survey, Glassdoor, Levels.fyi, Swedish salary statistics, or personal research):

1. **Option A:** Create `salary_data.json` manually in the repo root (see `tools/README_SALARY_TOOL.md` for the format)
2. **Option B:** Convert from Excel:
   ```bash
   pip install openpyxl
   python tools/convert_salary_excel.py path/to/salary-data.xlsx --source "My Salary Data 2025"
   ```

This creates `salary_data.json` which the `/apply` workflow uses for salary benchmarking. If you skip this step, salary lookup is simply omitted.

## 6. Test the workflow

Find a job posting you're interested in, then:

```
/apply https://jobindex.dk/job/1234567
```

For US or Swedish roles, use any URL or paste the job text:

```
/apply https://www.usajobs.gov/job/123456789
/apply [paste a Swedish posting from Platsbanken, LinkedIn, or a company career page]
```

Or paste the job description directly:

```
/apply [paste job posting text here]
```

The assistant will:
1. Evaluate the fit against your profile
2. Ask if you want to proceed
3. Draft a tailored CV and cover letter
4. Have `tools/review_delegate.py` critique the drafts with Kiro CLI first and Claude fallback
5. Revise and present the final output

## 7. Compile your documents

After `/apply` creates the LaTeX files:

```bash
# Compile CV
cd cv && lualatex main_<company>.tex && cd ..

# Compile cover letter
cd cover_letters && xelatex cover_<company>_<role>.tex && cd ..
```

## Troubleshooting

### "salary_data.json not found"
This is expected if you haven't set up salary benchmarking. The `/apply` workflow skips this step automatically.

### Job search CLI tools not working
Make sure Bun is installed and you ran `bun install` in each CLI directory. These tools are Denmark-specific. US and Sweden searches should still work through the configured WebSearch/site-query blocks even if the Danish CLIs are not installed.

### Kiro reviewer not working
Run:

```bash
kiro-cli whoami
python tools/review_delegate.py --backend claude --help
```

If Kiro is unavailable, the default `--backend auto` path falls back to Claude. To force Claude, use `--backend claude`; to require Kiro, use `--backend kiro`.

### LaTeX compilation errors
- CV: uses `lualatex` (pdflatex often fails on modern MiKTeX with `fontawesome5` font-expansion errors; lualatex handles the same sources cleanly)
- Cover letter: uses `xelatex` (for custom fonts in `OpenFonts/fonts/`)
- Make sure your LaTeX distribution includes the `moderncv` package

### Fonts not found in cover letter
The cover letter template expects fonts in `cover_letters/OpenFonts/fonts/`. Make sure this directory exists and contains the Lato and Raleway font files.

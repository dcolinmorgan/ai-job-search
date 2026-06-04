# Job Scraper

**name:** job-scraper
**description:** Searches configured job markets for new positions matching your profile. Supports Denmark, United States, Sweden, and custom site-query markets. Deduplicates across runs. Triggers on: job scrape, find jobs, search jobs, new jobs, job search, scrape jobs, /scrape
**allowed-tools:** Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, Agent, AskUserQuestion

---

## How It Works

This skill searches configured job markets using targeted queries based on your profile, deduplicates against previously seen jobs and the application tracker, and presents new matches with a quick fit assessment. The legacy Danish portal CLIs are still available for Denmark; US and Sweden searches use WebSearch/site-query patterns unless local portal integrations are added.

## Invocation

The user triggers this skill by saying things like:
- "Find new jobs"
- "Scrape for jobs"
- "Any new positions?"
- "/scrape"

Optional arguments:
- A focus area, e.g. "/scrape data science" or "/scrape geophysics"
- "broad" to run all search categories, e.g. "/scrape broad"

---

## Execution Steps

### Step 0: Load State

1. Read `job_scraper/seen_jobs.json` (create if missing - start with `{"seen": {}}`)
2. Read `job_search_tracker.csv` to extract already-applied companies+roles
3. Read `search-queries.md` (this directory) for the search strategy
4. Read `.claude/skills/job-application-assistant/08-market-localization.md` for market-specific source lists, terminology, and logistics filters

### Step 1: Search

Run **WebSearch** queries from `search-queries.md`. By default, run the top 3 priority categories for each configured target market. If the user said "broad", run all categories.

If the user specified a focus area (e.g. "data science"), prioritize queries from that category.

For each search:
- Use `WebSearch` with site-specific queries from the configured market blocks:
  - Denmark: Jobindex, Jobnet, Akademikernes Jobbank, Jobdanmark, LinkedIn, IDA/Karriere
  - United States: LinkedIn, Indeed, company ATS domains, USAJOBS for federal roles, and role-specific boards
  - Sweden: Arbetsformedlingen/Platsbanken, LinkedIn, Indeed Sweden, The Hub, and sector-specific boards
- Target the configured geographic area, state/region, remote constraints, and work-authorization constraints
- Look for postings from the last 14 days

### Step 2: Fetch & Parse

For each promising result from Step 1:
- Use `WebFetch` to retrieve the job posting page
- Extract: **job title**, **company**, **location**, **posting date** (or "recent"), **URL**, **key requirements** (brief), **application deadline** (if listed)
- Extract: **market** (`us`, `sweden`, `denmark`, or `other`) and note any language, work authorization, clearance, onsite, timezone, or commute requirement
- Skip if the URL or company+title combo already exists in `seen_jobs.json`
- Skip if the company+role already appears in `job_search_tracker.csv`

### Step 3: Quick Fit Assessment

For each new job, do a rapid fit check (NOT the full evaluation from `04-job-evaluation.md` - just a quick signal):

- **High match**: Role directly involves your core skills
- **Medium match**: Role is adjacent to your experience
- **Low match**: Role requires significant skills you lack
- **Market/logistics risk**: Flag country-specific work authorization, Swedish language requirements, US security clearance, state-only remote eligibility, or commute/onsite conflicts

### Step 4: Deduplicate & Store

1. Add ALL fetched jobs (new and skipped) to `seen_jobs.json` with structure:
```json
{
  "seen": {
    "<url_or_company_title_key>": {
      "title": "...",
      "company": "...",
        "url": "...",
        "market": "us/sweden/denmark/other",
        "first_seen": "YYYY-MM-DD",
        "fit": "high/medium/low",
        "status": "new/skipped/evaluated"
    }
  }
}
```
2. Only present jobs NOT already in the seen list or tracker.

### Step 5: Present Results

Present new jobs in a table sorted by fit (high first):

```
## New Job Matches - YYYY-MM-DD

Found X new positions (Y high, Z medium, W low match).

| # | Fit | Market | Title | Company | Location | Deadline | URL |
|---|-----|--------|-------|---------|----------|----------|-----|
| 1 | High | ... | ... | ... | ... | [Link](...) |

### High-Match Highlights
For each high-match job, add 2-3 bullet points:
- Why it matches your profile
- Key requirements to check
- Any red flags
```

After presenting, ask:
> "Want me to evaluate any of these in detail? Just give me the number(s)."

If the user picks a number, invoke the **job-application-assistant** skill workflow (fit evaluation first, then CV + cover letter if approved).

### Step 6: Update Tracker (Optional)

If the user decides to apply to any job, add a row to `job_search_tracker.csv`.

---

## Important Rules

1. **Never fabricate job postings.** Only present jobs found via actual WebSearch/WebFetch results.
2. **Respect deduplication.** Always check seen_jobs.json AND job_search_tracker.csv before presenting.
3. **Focus on configured geographic area.** Skip jobs that require relocation or are clearly outside commute range.
4. **Respect market constraints.** Do not present roles that require work authorization, language fluency, clearance, state residency, or onsite availability the profile does not support unless you mark the risk clearly.
5. **Only open positions.** Skip postings with expired deadlines or those marked as closed.
6. **Be efficient with WebFetch.** Don't fetch every search result - use titles and snippets to pre-filter before fetching.
7. **Parallel searches.** Use the Agent tool or parallel WebSearch calls to speed up the search phase.

# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, markets, and location -->

## Target Markets

Priority order:
1. `[PRIMARY_MARKET: us | sweden | denmark | other]`
2. `[SECONDARY_MARKET_OPTIONAL]`

Supported market guidance lives in `.claude/skills/job-application-assistant/08-market-localization.md`.

## Candidate Search Inputs

- **Primary role type:** `[YOUR_PRIMARY_ROLE_TYPE]`
- **Primary job titles:** `[YOUR_PRIMARY_JOB_TITLE_1]`, `[YOUR_PRIMARY_JOB_TITLE_2]`
- **Adjacent titles:** `[YOUR_ADJACENT_TITLE_1]`, `[YOUR_ADJACENT_TITLE_2]`
- **Key skills:** `[YOUR_KEY_SKILL_1]`, `[YOUR_KEY_SKILL_2]`, `[YOUR_KEY_SKILL_3]`
- **Domain keywords:** `[YOUR_DOMAIN_KEYWORD_1]`, `[YOUR_DOMAIN_KEYWORD_2]`
- **Target companies:** `[TARGET_COMPANY_1]`, `[TARGET_COMPANY_2]`

## Market: United States (`us`)

Use these when US is a target market. Combine city/state/remote terms where relevant.

### Sites

- LinkedIn Jobs
- Indeed
- Google Jobs / direct company career pages
- Built In, Dice, Wellfound, or other role-specific boards
- USAJOBS for federal roles
- Greenhouse, Lever, Workday, Ashby, and other ATS domains for direct postings

### Priority 1: Core Role

```text
site:linkedin.com/jobs "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_CITY]" "[YOUR_STATE]"
site:indeed.com "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_KEY_SKILL_1]" "[YOUR_CITY]"
site:greenhouse.io "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_KEY_SKILL_1]" "[YOUR_STATE]"
site:lever.co "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_DOMAIN_KEYWORD_1]" remote
```

### Priority 2: Domain / Sector

```text
site:linkedin.com/jobs "[YOUR_DOMAIN_KEYWORD_1]" "[YOUR_KEY_SKILL_1]" "United States"
site:indeed.com "[YOUR_DOMAIN_KEYWORD_2]" "[YOUR_PRIMARY_JOB_TITLE_2]" "[YOUR_STATE]"
site:ashbyhq.com "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_DOMAIN_KEYWORD_1]"
```

### Priority 3: Adjacent Roles

```text
site:linkedin.com/jobs "[YOUR_ADJACENT_TITLE_1]" "[YOUR_KEY_SKILL_1]" "[YOUR_CITY]"
site:indeed.com "[YOUR_ADJACENT_TITLE_2]" "[YOUR_KEY_SKILL_2]" remote
site:wellfound.com/jobs "[YOUR_ADJACENT_TITLE_1]" "[YOUR_KEY_SKILL_1]" remote
```

### Public Sector / Regulated Roles

```text
site:usajobs.gov "[YOUR_PRIMARY_JOB_TITLE_1]" "[YOUR_KEY_SKILL_1]"
site:usajobs.gov "[YOUR_DOMAIN_KEYWORD_1]" "[YOUR_STATE]"
```

## Market: Sweden (`sweden`)

Use these when Sweden is a target market. Include both English and Swedish title variants when useful.

### Sites

- Arbetsformedlingen / Platsbanken
- LinkedIn Jobs
- Indeed Sweden
- The Hub for Nordic startup roles
- Academic Work, Jobbsafari, Ingenjorsjobb, or sector-specific boards
- Direct company career pages

### Priority 1: Core Role

```text
site:arbetsformedlingen.se/platsbanken "[YOUR_PRIMARY_JOB_TITLE_SWEDISH]" "[YOUR_CITY]"
site:linkedin.com/jobs "[YOUR_PRIMARY_JOB_TITLE_ENGLISH]" Sweden "[YOUR_CITY]"
site:se.indeed.com "[YOUR_PRIMARY_JOB_TITLE_ENGLISH]" "[YOUR_KEY_SKILL_1]" "[YOUR_CITY]"
site:thehub.io/jobs "[YOUR_PRIMARY_JOB_TITLE_ENGLISH]" Sweden
```

### Priority 2: Domain / Sector

```text
site:arbetsformedlingen.se/platsbanken "[YOUR_DOMAIN_KEYWORD_1]" "[YOUR_CITY]" 
site:linkedin.com/jobs "[YOUR_DOMAIN_KEYWORD_1]" "[YOUR_KEY_SKILL_1]" Sweden
site:se.indeed.com "[YOUR_DOMAIN_KEYWORD_2]" "[YOUR_PRIMARY_JOB_TITLE_SWEDISH]"
```

### Priority 3: Adjacent Roles

```text
site:linkedin.com/jobs "[YOUR_ADJACENT_TITLE_1]" "[YOUR_KEY_SKILL_1]" Sweden
site:arbetsformedlingen.se/platsbanken "[YOUR_ADJACENT_TITLE_2_SWEDISH]" "[YOUR_CITY]"
site:thehub.io/jobs "[YOUR_ADJACENT_TITLE_1]" "[YOUR_KEY_SKILL_2]" Sweden
```

## Market: Denmark (`denmark`)

Use these when Denmark is a target market or when preserving the original workflow.

### Sites

- Jobindex
- Jobnet
- Akademikernes Jobbank
- Jobdanmark
- LinkedIn Jobs
- IDA / Karriere and sector-specific boards

### Priority 1: Core Role

```text
site:jobindex.dk "[YOUR_PRIMARY_JOB_TITLE]" [YOUR_CITY]
site:jobindex.dk "[YOUR_KEY_SKILL_1]" [YOUR_CITY]
site:linkedin.com/jobs "[YOUR_PRIMARY_JOB_TITLE]" Denmark [YOUR_CITY]
```

### Priority 2: Domain / Sector

```text
site:jobindex.dk [YOUR_DOMAIN_KEYWORD_1] [YOUR_CITY] OR [YOUR_REGION]
site:jobindex.dk [YOUR_DOMAIN_KEYWORD_2] Denmark
site:linkedin.com/jobs [YOUR_DOMAIN_KEYWORD_1] [YOUR_CITY] Denmark
```

### Priority 3: Adjacent Roles

```text
site:jobindex.dk "[YOUR_ADJACENT_TITLE_1]" [YOUR_KEY_SKILL_1] [YOUR_CITY]
site:jobindex.dk "[YOUR_ADJACENT_TITLE_2]" [YOUR_KEY_SKILL_2] [YOUR_CITY]
```

## Custom Company / ATS Searches

Use these for any market when target companies are known:

```text
site:[TARGET_COMPANY_DOMAIN] careers "[YOUR_PRIMARY_JOB_TITLE_1]"
site:greenhouse.io "[TARGET_COMPANY_1]" "[YOUR_PRIMARY_JOB_TITLE_1]"
site:lever.co "[TARGET_COMPANY_1]" "[YOUR_PRIMARY_JOB_TITLE_1]"
site:workdayjobs.com "[TARGET_COMPANY_1]" "[YOUR_KEY_SKILL_1]"
```

## Location Filter

When evaluating results, verify the job location is within reasonable commute distance and compatible with work authorization or remote constraints.

- **Ideal:** `[YOUR_CITY]`, `[YOUR_STATE_OR_REGION]`, remote roles explicitly open to `[YOUR_MARKET]`
- **Acceptable:** `[ACCEPTABLE_AREA_1]`, `[ACCEPTABLE_AREA_2]`
- **Borderline:** `[BORDERLINE_AREA]` (borderline - ~X min by transit or timezone friction)
- **Too far:** `[TOO_FAR_AREA]` (too far, relocation required, or remote not available in the candidate's market)

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and generate 2-3 custom queries for that focus.

Examples:
- `/scrape data science us` -> US core role + US domain queries
- `/scrape sweden` -> Sweden market queries with Swedish/English title variants
- `/scrape broad` -> all configured market blocks

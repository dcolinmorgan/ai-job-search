# Market Localization Guide

Use this file whenever a job posting, search query, CV, resume, or cover letter targets a specific hiring market. The default supported markets are:

- `us` - United States
- `sweden` - Sweden
- `denmark` - Denmark / legacy default
- `other` - infer from the posting and ask the user only when the choice affects the document

## Market Detection

Infer the market from the strongest available signal:

1. The posting location or required work authorization
2. The job-board domain or company career site locale
3. The candidate's configured target markets in `search-queries.md`
4. The language of the posting

If a posting is remote but the employer requires a country-specific payroll location, use that country as the market. If the posting is remote globally and no legal market is specified, use the candidate's target market.

## Shared Rules

- Match the cover-letter language to the posting unless the user requests otherwise.
- Do not invent work authorization, citizenship, visa status, security clearance, or language fluency.
- Keep salary and compensation comparisons in the market's currency and cadence when the data supports it.
- Use local document conventions, but do not add sensitive personal details unless the user explicitly wants them included.
- Keep company-specific claims out of the documents unless verified independently by web search or official company sources.

## United States (`us`)

### Search Sources

Use a mix of broad boards, professional networks, specialist boards, and direct company searches:

- LinkedIn Jobs
- Indeed
- Google Jobs / company career pages
- Built In, Dice, Wellfound, or other role-specific boards when relevant
- USAJOBS for federal roles
- State, city, university, hospital, national lab, and contractor career pages when relevant

### Search Query Patterns

Combine role, skill, location, and remote terms:

```text
site:linkedin.com/jobs "[ROLE_TITLE]" "[CITY]" "[STATE]"
site:indeed.com "[ROLE_TITLE]" "[KEY_SKILL]" "[CITY]"
site:wellfound.com/jobs "[ROLE_TITLE]" "[KEY_SKILL]" remote
site:usajobs.gov "[ROLE_TITLE]" "[KEY_SKILL]"
site:greenhouse.io "[ROLE_TITLE]" "[TARGET_COMPANY_OR_DOMAIN]"
site:lever.co "[ROLE_TITLE]" "[TARGET_COMPANY_OR_DOMAIN]"
```

### Resume / CV Conventions

- Refer to the document as a resume in user-facing notes, even if the repo path remains `cv/`.
- Use US English.
- Prefer `letterpaper` for newly generated US resume PDFs.
- Keep the resume to 1-2 pages. The repo's default workflow still enforces exactly 2 pages unless the user changes that rule.
- Omit photo, age, date of birth, marital status, nationality, full street address, and references.
- Include city/state, email, phone, LinkedIn, GitHub/portfolio if relevant.
- Lead with impact, metrics, tools, and scope. US resumes reward concise achievement bullets.

### Cover Letter Conventions

- Use "Dear Hiring Manager," or "Dear [Company] hiring team," when no named contact is available.
- Use "Sincerely," or "Best regards," as the closing.
- Keep it direct, evidence-led, and one page.
- Avoid over-explaining personal motivation. Tie motivation to the company's product, team, mission, or problem space.

### Evaluation Notes

- Check remote eligibility by state, time zone expectations, work authorization, sponsorship, clearance, travel, and onsite cadence.
- For compensation, distinguish base salary, bonus, equity, and benefits when the data supports it.
- For public-sector roles, check USAJOBS-style requirements carefully: eligibility, questionnaire language, transcripts, and specialized experience.

## Sweden (`sweden`)

### Search Sources

Use Swedish and international sources:

- Arbetsformedlingen / Platsbanken
- LinkedIn Jobs
- Indeed Sweden
- The Hub for Nordic startup roles
- Academic Work, Jobbsafari, Ingenjorsjobb, or sector-specific boards when relevant
- Direct company career pages, especially for large employers and consultancies

### Search Query Patterns

Combine Swedish and English job titles where useful:

```text
site:arbetsformedlingen.se/platsbanken "[ROLE_TITLE_SWEDISH]" "[CITY]"
site:linkedin.com/jobs "[ROLE_TITLE_ENGLISH]" Sweden "[CITY]"
site:se.indeed.com "[ROLE_TITLE]" "[KEY_SKILL]" "[CITY]"
site:thehub.io/jobs "[ROLE_TITLE]" Sweden
site:career*.com "[TARGET_COMPANY]" "[ROLE_TITLE]" Sweden
```

### CV Conventions

- "CV" is standard. English CVs are common for international and technical roles; Swedish CVs fit Swedish-language postings.
- Keep it concise, usually 1-2 pages. The repo's default workflow still enforces exactly 2 pages unless the user changes that rule.
- Do not include Swedish personal identity number, marital status, age, or photo by default.
- Include language proficiency, work authorization only if true and strategically relevant, and location/relocation constraints.
- Swedish hiring often values collaborative tone, practical ownership, and fit with the team, not only individual achievement.

### Cover Letter Conventions

- For Swedish-language postings, use Swedish unless the user asks for English.
- Acceptable salutations include "Hej [Name]," or "Hej [Company/team],".
- Acceptable closings include "Vanliga halsningar," or "Med vanliga halsningar,". Use Swedish diacritics if the document already uses them.
- Keep the tone warm, concrete, and modestly confident. Avoid US-style exaggeration.

### Evaluation Notes

- Check Swedish language requirements carefully. "Swedish required" is often a real filter, not a nice-to-have.
- Check hybrid/onsite expectations by city and commute, especially Stockholm, Gothenburg, Malmo/Lund, Uppsala, and remote Nordic roles.
- For compensation, use SEK monthly or annual consistently based on the source data.
- If the candidate has non-Swedish education or experience, make equivalence and relevance easy to understand without overstating.

## Denmark (`denmark`)

### Search Sources

Use the existing Danish job-search pattern:

- Jobindex
- Jobnet
- Akademikernes Jobbank
- Jobdanmark
- LinkedIn Jobs
- IDA / Karriere and sector-specific boards when relevant

### Document Conventions

- English CVs are acceptable for many technical roles. Use Danish cover letters for Danish-language postings.
- "Med venlig hilsen," is the standard Danish closing.
- Include language proficiency and commute/work authorization constraints only when accurate and relevant.

## Other Markets

When the market is outside the supported set:

1. Follow the posting language and document instructions.
2. Use country-specific government or major job boards if known.
3. Ask one short clarifying question if document norms conflict with the repo defaults.
4. Keep sensitive personal details out unless the local market clearly requires them and the user confirms.

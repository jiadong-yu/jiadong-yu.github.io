# Jiadong Yu

Personal academic homepage built with Jekyll and al-folio.

Deployment URL: https://jiadong-yu.github.io/

## GitHub Pages deployment

Repository: https://github.com/jiadong-yu/jiadong-yu.github.io

The site is published at the root URL with an empty `baseurl`. The deployment
workflow explicitly builds for the root. Settings → Pages uses `gh-pages` (root).
After repository or URL changes, run Deploy site to regenerate navigation,
canonical URLs, course links, and asset paths before serving the new address.

## Group synchronization

The Group page links to https://extend-lab.com/ and renders People data from
`_data/lab_people.json`, excluding Jiadong Yu. Each deployment fetches the public
https://extend-lab.com/people/ page and extracts names, photos, roles, and alumni.
Deployments run on pushes, manually, and every six hours (GitHub schedules may be delayed).
The generated data is deployed directly; scheduled runs do not commit to main.
If fetching or parsing fails, deployment fails and the previously published site remains available.

To refresh the checked-in snapshot locally:

```bash
python -m pip install beautifulsoup4==4.15.0
python scripts/sync_people.py
```

## Grants and Publications synchronization

The Grants page keeps its card layout and reads project titles, funders, amounts,
and dates from https://extend-lab.com/projects/ in source order. Known PI/Co-PI and
location details remain in `_data/grant_details.json`; projects without those
local details omit those fields. New projects are included automatically.

The Publications page reads the complete archive linked by Research → Publications
→ Find More at https://extend-lab.com/publications/, including both journal and
conference lists. It preserves the existing J/C labels, journal italics, and
J. Yu author emphasis. Source corrections, additions, and removals are reflected
on the next deployment. `_bibliography/papers.bib` is not used by this page.

Both pages refresh during the same six-hour deployment schedule as Group.
Snapshots are in `_data/lab_projects.json` and `_data/lab_publications.json`.
To refresh them locally after installing Beautiful Soup:

```bash
python scripts/sync_research.py
```

## Local development

```bash
docker compose up --build
```

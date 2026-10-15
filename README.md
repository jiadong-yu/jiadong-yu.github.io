# Jiadong Yu

Personal academic homepage built with Jekyll and al-folio.

Deployment URL: https://jiadong-yu.github.io/

## Root URL migration

Rename the GitHub repository from `Bio` to `jiadong-yu.github.io` in Settings → General.
Keep Settings → Pages configured to deploy from `gh-pages` (root), then run the
Deploy site workflow. The configuration already uses an empty `baseurl`. During the transition, the workflow
uses `/Bio` while the repository is named `Bio`, and switches to the root automatically
after renaming.
Update the local remote after renaming:

```bash
git remote set-url origin git@github-jiadongyu:jiadong-yu/jiadong-yu.github.io.git
```

GitHub does not redirect old project Pages URLs automatically. External links to
`https://jiadong-yu.github.io/Bio/` should be updated, including the link on EXTEND Lab People.

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

## Local development

```bash
docker compose up --build
```

"""Generate group data from the public EXTEND Lab People page."""

import json
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://extend-lab.com/people/"


def extract_people(html):
    soup = BeautifulSoup(html, "html.parser")
    base = urljoin(SOURCE, soup.base["href"]) if soup.base else SOURCE
    sections = []
    for section in soup.select("main .page-section"):
        heading = section.select_one("h2")
        if not heading:
            continue
        members = []
        for card in section.select(".person-card"):
            name = card.select_one("h3").get_text(" ", strip=True)
            if name.casefold() == "jiadong yu":
                continue
            photo = card.select_one("img")
            role = card.select_one(".person-body p")
            members.append({
                "name": name,
                "photo": urljoin(base, photo["src"]) if photo else "",
                "role": role.get_text(" · ", strip=True) if role else "",
            })
        table = section.select_one("table")
        rows = [[cell.get_text(" ", strip=True) for cell in row.select("th, td")]
                for row in table.select("tr")] if table else []
        rows = [row for row in rows if not any(cell.casefold() == "jiadong yu" for cell in row)]
        if members or rows:
            sections.append({"title": heading.get_text(" ", strip=True), "members": members, "rows": rows})
    if not any(section["members"] for section in sections):
        raise ValueError("No recognized members; refusing to replace saved data")
    return sections


if __name__ == "__main__":
    with urlopen(SOURCE, timeout=30) as response:
        sections = extract_people(response.read())
    (ROOT / "_data" / "lab_people.json").write_text(json.dumps(sections, ensure_ascii=False, indent=2) + "\n")
    print(f"Synced {sum(len(section['members']) for section in sections)} members from {SOURCE}")

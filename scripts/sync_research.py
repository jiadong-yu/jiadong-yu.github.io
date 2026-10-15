"""Sync lab project summaries and the complete Research publication archive."""

import html
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = "https://extend-lab.com/projects/"
PUBLICATIONS = "https://extend-lab.com/publications/"


def extract_projects(source):
    soup = BeautifulSoup(source, "html.parser")
    projects = []
    for row in soup.select("main .project-table .project-summary-row"):
        cells = row.find_all("td", recursive=False)
        if len(cells) != 5:
            raise ValueError("Unexpected project columns")
        title, funder, amount, start, end = [cell.get_text(" ", strip=True) for cell in cells]
        if not all((title, funder, amount, start, end)):
            raise ValueError("Incomplete project")
        # Store real dates for Jekyll's date filter; the source provides year-month.
        dates = [datetime.strptime(value, "%Y-%m").strftime("%Y-%m-%d") for value in (start, end)]
        projects.append(dict(title=title, funder=funder, amount=amount, start=dates[0], end=dates[1]))
    if not projects:
        raise ValueError("No recognized projects; refusing to replace saved data")
    return projects


def citation_html(node):
    """Keep citation typography and safe links, without importing source UI/code."""
    if isinstance(node, NavigableString):
        text = html.escape(str(node))
        return re.sub(r"\bJ\.\s+Yu\*?(?!\w)", lambda match: f"<strong>{match[0]}</strong>", text)
    if node.name in ("script", "style", "iframe"):
        return ""
    content = "".join(citation_html(child) for child in node.children)
    if node.name in ("em", "i", "sub", "sup"):
        return f"<{node.name}>{content}</{node.name}>"
    if node.name in ("strong", "b"):
        return f"<strong>{content}</strong>"
    if node.name == "a":
        url = urljoin(PUBLICATIONS, node.get("href", ""))
        if urlparse(url).scheme in ("http", "https"):
            return f'<a href="{html.escape(url, quote=True)}">{content}</a>'
    return content


def extract_publications(source):
    soup = BeautifulSoup(source, "html.parser")
    sections = []
    for section_id, title, prefix in (
        ("journal-articles", "Journal Papers", "J"),
        ("conference-papers", "Conference Papers", "C"),
    ):
        listing = soup.select_one(f"main #{section_id} ol.publication-list")
        if listing is None:
            raise ValueError(f"Missing publication section: {section_id}")
        entries = listing.find_all("li", recursive=False)
        if not entries:
            raise ValueError(f"Empty publication section: {section_id}")
        reverse = listing.has_attr("reversed")
        number = int(listing.get("start", len(entries) if reverse else 1))
        papers = []
        for entry in entries:
            number = int(entry.get("value", number))
            if not entry.get_text(strip=True):
                raise ValueError("Empty citation")
            papers.append({"label": f"{prefix}{number}", "html": citation_html(entry).strip()})
            number += -1 if reverse else 1
        sections.append({"title": title, "papers": papers})
    return sections


if __name__ == "__main__":
    # Validate both sources before writing either snapshot.
    with urlopen(PROJECTS, timeout=30) as response:
        projects = extract_projects(response.read())
    with urlopen(PUBLICATIONS, timeout=30) as response:
        publications = extract_publications(response.read())
    for name, data in (("lab_projects", projects), ("lab_publications", publications)):
        (ROOT / "_data" / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"Synced {len(projects)} projects and {sum(len(section['papers']) for section in publications)} publications")

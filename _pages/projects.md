---
layout: page
title: Grants
permalink: /grants/
description: Grants and funded research from EXTEND Lab Projects.
nav: true
nav_order: 2
---

<p class="jd-page-intro">Grants and funded research, automatically updated from <a href="https://extend-lab.com/projects/">EXTEND Lab Projects</a>.</p>

<div class="jd-section-divider"><span>Selected Grants</span></div>

<div class="jd-card-grid">
{% for grant in site.data.lab_projects %}
  {% assign details = site.data.grant_details[grant.title] %}
  <div class="jd-card">
    <h3 class="jd-card-title">{{ grant.title | escape }}</h3>
    <div class="jd-meta-tags">
      {% if details.role %}<span class="jd-meta-tag role">{{ details.role | escape }}</span>{% endif %}
      <span class="jd-meta-tag amount">{{ grant.amount | escape }}</span>
    </div>
    <p class="jd-card-meta"><em>{{ grant.funder | escape }}</em></p>
    {% if details.location %}<p class="jd-card-meta">{{ details.location | escape }}</p>{% endif %}
    <p class="jd-card-meta">{{ grant.start | date: '%b. %Y' }} - {{ grant.end | date: '%b. %Y' }}</p>
  </div>
{% endfor %}
</div>

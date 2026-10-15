---
layout: page
permalink: /group/
title: Group
description: Students and collaborators at EXTEND Lab.
nav: true
nav_order: 4
---

<p class="jd-page-intro">Our research group is <a href="https://extend-lab.com/">EXTEND Lab</a>.</p>
<p class="jd-page-intro">Students, collaborators, and alumni, automatically updated from <a href="https://extend-lab.com/people/">EXTEND Lab People</a>.</p>

{% for section in site.data.lab_people %}

<div class="jd-section-divider"><span>{{ section.title | escape }}</span></div>
{% if section.members.size > 0 %}
<div class="jd-person-grid">
{% for person in section.members %}
  <div class="jd-person-card">
    {% if person.photo != '' %}<img class="jd-person-photo" src="{{ person.photo | escape }}" alt="{{ person.name | escape }}" loading="lazy" />{% endif %}
    <div class="jd-person-body">
      <h3 class="jd-person-name">{{ person.name | escape }}</h3>
      <p class="jd-person-role">{{ person.role | escape }}</p>
    </div>
  </div>
{% endfor %}
</div>
{% endif %}
{% if section.rows.size > 0 %}
<div class="table-responsive">
<table class="table">
  <thead><tr>{% for cell in section.rows.first %}<th scope="col">{{ cell | escape }}</th>{% endfor %}</tr></thead>
  <tbody>{% for row in section.rows offset:1 %}<tr>{% for cell in row %}<td>{{ cell | escape }}</td>{% endfor %}</tr>{% endfor %}</tbody>
</table>
</div>
{% endif %}
{% endfor %}

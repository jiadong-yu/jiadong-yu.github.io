---
layout: page
permalink: /publications/
title: Publications
description: Journal and conference papers by Jiadong Yu.
nav: true
nav_order: 5
---

<style>
  .pub-intro {
    margin-bottom: 1.2rem;
    color: var(--global-text-color-light);
    line-height: 1.8;
  }

  .pub-list {
    list-style: none;
    padding-left: 0;
    margin-top: 1rem;
  }

  .pub-list li {
    margin-bottom: 1rem;
    line-height: 1.7;
  }

  .pub-label {
    display: inline-block;
    min-width: 3.2rem;
    font-weight: 700;
    color: var(--global-theme-color);
  }

  .pub-section {
    margin-top: 2rem;
  }
</style>

<p class="pub-intro">
  For a complete citation profile, please visit my
  <a href="https://scholar.google.com/citations?user=lsj5Wv4AAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar</a>.
  This list is automatically updated from <a href="https://extend-lab.com/publications/">EXTEND Lab Publications</a>.
</p>

{% for section in site.data.lab_publications %}

<div class="pub-section">
  <h2>{{ section.title | escape }}</h2>
  <ul class="pub-list">
    {% for paper in section.papers %}
    <li><span class="pub-label">[{{ paper.label | escape }}]</span> {{ paper.html }}</li>
    {% endfor %}
  </ul>
</div>
{% endfor %}

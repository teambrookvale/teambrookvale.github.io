---
title: Software Development and System Integration services
permalink: /landings/locations
leadtext: We develop software products and provide digital platform engineering services in across Australia, New Zeland and Asia
layout: landing_list
---
{% comment %}
    {{ page.content }} is similar to a CSV file where the line end would be a semi-colon e.g.:
    Auckland,/landings/locations/auckland;
    Sydney,/landings/locations/sydney;
{% endcomment %}

{% for item in site.landing_locations %}
    {% assign url = page.url | append: "/" | append: item.slug %}
    {% assign text = item.name %}
    {{ text }},{{ url }};
{% endfor %}

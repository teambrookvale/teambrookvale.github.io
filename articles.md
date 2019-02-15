---
layout: default
title: Articles - Team Brookvale 
permalink: /articles
description: "We develop software products and provide digital platform engineering services on the Northern Beaches of Sydney"
---

<div class="articlespage">
    <div class="pagehero">
        <div class="inner flex sb">
            <div>
                <h1>Articles</h1>
                <p style="margin-bottom: 50px">We develop software products and provide digital platform engineering services on the Northern Beaches of Sydney</p>
                <img src="/assets/images/arrowdown.png">
            </div>
            <div class="pageheropic">
                <img src="/assets/images/abstract-architectural-design-architecture.webp" />
            </div>
        </div>
    </div>
    <div class="collection clearfix">
        {% assign sortedarticles = site.articles | sort: 'date' | reverse %}
        {% assign articles = sortedarticles %}
        {% for article in articles %}
            <div>
                <a href="{{ article.url }}">
                 {% if article.image %}
                <div class="img block">
                        <img src="{{article.image}}" />
                </div>
                {% else %}
                <div class="block {{article.boxclassname | downcase }}">
                </div>
                {% endif %}
                <div class="text">
                    <div class="small hovu">
                        {{ article.topic }}
                    </div>
                    <p class="clamp3">
                        {{ article.title }}
                    </p>
                </div>
                </a>
            </div>
        {% endfor %}
    </div>
    <div class="projects">
        <hr>
        <div class="flex sb">
            <div>
                <h2>{{ site.data.text.home.doyouliketitle }}</h2>
                <p class="gray">{{ site.data.text.home.doyoulikedescription }}</p>
            </div>
            <div>
                <button onclick="top.location.href = '/contact'">{{ site.data.text.home.letsmakebuttontext}}</button>
            </div>
        </div>
    </div>
</div>
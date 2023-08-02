---
layout: default
title: Articles - Team Brookvale 
permalink: /more-articles
description: "We develop software products and provide digital platform engineering services in Sydney, Gold Coast and Brisbane"
---

<div class="articlespage">
    <div class="pagehero">
        <div class="inner flex sb">
            <div>
                <h1>Articles</h1>
                <p style="margin-bottom: 50px">We develop software products and provide digital platform engineering services in Sydney, Gold Coast and Brisbane</p>
                <img src="/assets/images/arrowdown.png">
            </div>
            <div class="pageheropic">
                <img src="/assets/images/abstract-architectural-design-architecture.webp" />
            </div>
        </div>
    </div>
    <div class="inner flex sb">
        <ul>
            {% assign sortedarticles = site.articles
                | where_exp: "item", "item.aigenerated == true"
                | sort: 'date'
                | reverse
            %}
            {% assign articles = sortedarticles %}
            {% for article in articles %}
                <div>
                    <a href="{{ article.url }}">
                    <div class="text">
                        <div class="small hovu">
                            {{ article.title }}
                        </div>
                    </div>
                    </a>
                </div>
            {% endfor %}
        </ul>
    </div>
    {% include contact.html %}
</div>
---
layout: article
permalink: /articles/overview-of-the-mqtt-protocol
boxclassname: black
author: "Thomas Saunders"
topic: "Business Apps"
title: "Learn how a 17 year old IBM invention is powering the IoT devices – An overview of the MQTT protocol"
leadhead: "What is MQTT?"
leadtext: "Internet of Things structures are getting complex and the large number of interconnected device systems are growing fast. For example a modern car has about 100 electronic controllers. As the number of systems are rapidly growing CPU and power usage have to be optimised."
image: /assets/images/articles/xhand-laptop-notebook-typing.webp
date: '2019-02-03 00:00:00'
---

<div class="arttext">
<img src="/assets/images/articles/xhand-laptop-notebook-typing.webp" alt="laptop" />
    <p>The MQTT protocol was invented in 1999 by IBM and Arcom. It is a free, open-source protocol. </p>
<p>MQTT is a machine-to-machine (M2M)/&#8221;Internet of Things&#8221; connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium. For example, it has been used in sensors communicating to a broker via satellite link, over occasional dial-up connections with healthcare providers, and in a range of home automation and small device scenarios. It is also ideal for mobile applications because of its small size, low power usage, minimised data packets, and efficient distribution of information to one or many receivers. (source: http://mqtt.org/ )<br/></p>
<img src="/assets/images/articles/MQTT-architecture.webp" alt="architecture" />
<p>MQTT-SN Architecture<br/>(source: http://mqtt.org/)</p>
<h2>How MQTT is different from HTTP?</h2>
<p>For specific tasks such as M2M communication, MQTT is superior compared to HTTP. MQTT can receive almost 100 times more packages and send almost 10 times more packages than traditional HTTPS at the same time.</p>
<p>See comparison table below:<br/>
(Source: http://stephendnicholas.com/archives/1217).</p>
<p>
<img src="/assets/images/articles/MQTT-speed-table.webp" alt="table" />
</p>
<p>It is clear then, that the MQTT protocol is significantly more efficient. The footprint of the packets can be as small as 2 bytes. 2 bytes are very small, it’s exactly to characters in text file for example “AB”. Further to this it was designed to be simple and reliable. </p>
<p>The Internet of Things combines all web, mobile and machine-to-machine (M2M) devices. Distributing packets in huge volumes is only available using MQTT in an efficient manner. Since its introduction in 1999 almost every industry adopted the technology and while the IoT hits the consumer market we will see systems that are getting complex and efficient at the same time.</p>
</div>
---
permalink: /landings/system-integrations/amazon-cloudfront/amazon-sqs
author: Edward Saunders
title: "Integrating Amazon CloudFront and Amazon SQS"
topic: System Integration
leadhead: "The integration of Amazon CloudFront and Amazon SQS is a powerful solution for delivering high-quality web content and improving the performance and scalability of distributed applications and microservices"
leadtext: "It provides organizations with a reliable, scalable, and cost-effective solution for deploying and managing their content delivery network and message queueing systems."
image: /assets/images/articles/people-sitting-near-table.webp
---
<div class="arttext">	<header>
		<h1>Integrating Amazon CloudFront and Amazon SQS</h1>
	</header>
	<main>
		<h2>Amazon CloudFront</h2>
		<p>Amazon CloudFront is a content delivery network (CDN) service that helps organizations deliver static and dynamic web content, video streams, and APIs around the world by caching data in edge locations close to the end-users.</p>

		<h2>Amazon SQS</h2>
		<p>Amazon Simple Queue Service (SQS) is a fully-managed message queuing service that enables decoupling of distributed software components and microservices by sending, storing, and processing messages between them without requiring them to be connected with each other all the time.</p>

		<h2>Integration of the two through API or SDK</h2>
		<p>Amazon CloudFront uses Amazon SNS (Simple Notification Service) to send notifications to Amazon SQS whenever a new invalidation request or a cache usage report is generated. This integration can be set up through the Amazon CloudFront console or programmatically using the AWS SDK.</p>

		<h2>Problems their integration solves</h2>
		<p>The integration of Amazon CloudFront and Amazon SQS provides several benefits for organizations:</p>
		<ul>
			<li>Reduced latency and improved performance by serving content from edge locations closer to end-users and minimizing the travel distance of messages between microservices.</li>
			<li>Improved scalability and reliability by distributing the workload across multiple edge locations and processing messages asynchronously and independently without affecting the overall system performance.</li>
			<li>Enhanced monitoring and analysis by collecting and storing real-time data about cache usage, invalidation requests, and message traffic in Amazon CloudFront and Amazon SQS logs for further analysis and optimization.</li>
		</ul>

		<h2>Conclusion</h2>
		<p>The integration of Amazon CloudFront and Amazon SQS is a powerful solution for delivering high-quality web content and improving the performance and scalability of distributed applications and microservices. It provides organizations with a reliable, scalable, and cost-effective solution for deploying and managing their content delivery network and message queueing systems. </p>
	</main>
	<footer>
		<p>Copyright © 2021. All rights reserved.</p>
	</footer>
</div>
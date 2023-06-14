---
permalink: /landings/system-integrations/amazon-sqs/aws-lambda
author: Edward Saunders
title: "Integrating Amazon SQS and AWS Lambda"
topic: System Integration
leadhead: "Amazon SQS and AWS Lambda are two of the most powerful services offered by AWS"
leadtext: "By integrating these services, we can design a highly scalable, resilient, and cost-efficient application architecture. We can achieve this by decoupling our application components and handling the surges in traffic and load effortlessly. The integration process is straightforward and can be done in a few simple steps."
image: /assets/images/articles/people-sitting-near-table.webp
---
<div class="arttext">	<header>
		<h1>Integrating Amazon SQS and AWS Lambda</h1>
	</header>
	<main>
		<section>
			<h2>What is Amazon SQS?</h2>
			<p>Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.</p>
		</section>
		<section>
			<h2>What is AWS Lambda?</h2>
			<p>AWS Lambda is a serverless computing service that lets you run code without provisioning or managing servers. You can run code for virtually any type of application or backend service, all with zero administration.</p>
		</section>
		<section>
			<h2>Integration of the two through API or SDK</h2>
			<p>The integration of Amazon SQS and AWS Lambda is done through API or SDK. With the help of AWS Lambda function, we can directly connect with the Amazon SQS and get access to send and receive messages from it. We can connect these services using the following steps:</p>
			<ol>
				<li>Create an Amazon SQS queue</li>
				<li>Create an AWS Lambda function</li>
				<li>Create an event source mapping between the two</li>
			</ol>
		</section>
		<section>
			<h2>Problems their integration solves</h2>
			<p>By integrating Amazon SQS and AWS Lambda, we can solve several problems:</p>
			<ul>
				<li>Decoupling: We can decouple our application architecture and make it more resilient to failure. With the help of Amazon SQS, we can buffer messages and handle any surge in traffic or load.</li>
				<li>Scalability: AWS Lambda scales automatically based on demand, which means it can dynamically respond to the number of messages coming in from Amazon SQS. This results in faster processing times and more efficient resource utilization.</li>
				<li>Cost optimization: With the help of serverless architecture, the cost of running the application is significantly reduced. We can pay only for the used compute time without worrying about provisioning and managing servers.</li>
			</ul>
		</section>
	</main>
	<footer>
		<h3>Conclusion</h3>
		<p>Amazon SQS and AWS Lambda are two of the most powerful services offered by AWS. By integrating these services, we can design a highly scalable, resilient, and cost-efficient application architecture. We can achieve this by decoupling our application components and handling the surges in traffic and load effortlessly. The integration process is straightforward and can be done in a few simple steps.</p>
	</footer>
</div>
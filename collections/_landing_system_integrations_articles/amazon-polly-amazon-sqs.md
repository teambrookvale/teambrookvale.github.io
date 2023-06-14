---
permalink: /landings/system-integrations/amazon-polly/amazon-sqs
author: Edward Saunders
title: "Integrating Amazon Polly and Amazon SQS"
leadhead: "Integrating Amazon Polly and Amazon SQS provides a powerful solution to speech processing challenges that are commonly encountered in building speech-enabled applications"
leadtext: "It enables you to decouple and scale components of your application to be more efficient and optimize resource utilization to reduce cloud computing costs."
image: /assets/images/articles/people-sitting-near-table.webp
---
<div class="arttext">	<h1>Integrating Amazon Polly and Amazon SQS</h1>

	<p>Amazon Polly is a text-to-speech service that uses advanced deep learning technologies to synthesize speech that sounds like a human voice. Amazon SQS, on the other hand, is a fully managed message queuing service that enables decoupling and scaling of distributed microservices. These two AWS services can be integrated through their APIs or SDKs to solve various problems.</p>

	<h2>Integrating Amazon Polly and Amazon SQS through API or SDK</h2>

	<p>To integrate Amazon Polly and Amazon SQS, you need to follow these steps:</p>

	<ol>
		<li>Set up an Amazon Polly account</li>
		<li>Create a message queue in Amazon SQS</li>
		<li>Configure Amazon Polly to push generated speech to Amazon SQS</li>
		<li>Read speech messages from Amazon SQS in your application</li>
	</ol>

	<p>You can use either the Amazon Polly API or SDK to push speech messages to Amazon SQS. The API is a low-level interface while the SDK provides a higher-level and more user-friendly interface for integration.</p>

	<h2>Problems their integration solves</h2>

	<p>The integration of Amazon Polly and Amazon SQS solves various problems encountered in speech processing, particularly in building speech-enabled applications. Some of these problems include:</p>
	<ul>
		<li>Scalability issues: When building speech-enabled applications, the volume of speech generated can be overwhelming, making it challenging to scale and manage. Integrating Amazon Polly and Amazon SQS enables you to decouple and scale components of your speech-enabled application to be more efficient.</li>
		<li>Resource utilization issues: Generating speech can be a resource-intensive task, and integrating Amazon Polly and Amazon SQS enables you to optimize resource utilization by leveraging Polly's text-to-speech abilities and SQS's messaging capabilities.</li>
		<li>Costs: Speech processing can be expensive, especially when dealing with large amounts of data. Through their integration, Amazon Polly and Amazon SQS help you optimize resource allocation and reduce cloud computing costs.</li>
	</ul>

	<h2>Conclusion</h2>

	<p>Integrating Amazon Polly and Amazon SQS provides a powerful solution to speech processing challenges that are commonly encountered in building speech-enabled applications. It enables you to decouple and scale components of your application to be more efficient and optimize resource utilization to reduce cloud computing costs. </p>
</div>
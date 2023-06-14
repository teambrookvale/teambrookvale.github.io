---
permalink: /landings/system-integrations/amazon-ses/amazon-sns
author: Edward Saunders
title: "Integrating Amazon SES and Amazon SNS for Better Email Delivery"
topic: System Integration
leadhead: "Integrating Amazon SES and SNS is a powerful way to improve your email delivery system"
leadtext: "By combining these two services, businesses can improve delivery rates, reduce the risk of messages being marked as spam, and gain valuable insights into user behavior. Whether you're sending transactional emails or marketing campaigns, SES and SNS provide a scalable and cost-effective solution for reliably sending messages to your customers."
image: /assets/images/articles/people-sitting-near-table.webp
---
<div class="arttext">    <h1>Integrating Amazon SES and Amazon SNS for Better Email Delivery</h1>
    <p>When it comes to email delivery, Amazon Web Services (AWS) offers a variety of powerful tools to help businesses send messages to customers efficiently and reliably. Two of these tools, Amazon Simple Email Service (SES) and Amazon Simple Notification Service (SNS), can be combined to create a robust email delivery system that solves many common problems. In this post, we'll explore how these two services work together and what benefits this integration provides.</p>
    
    <h2>Amazon SES</h2>
    <p>Amazon SES is a cloud-based service that enables businesses to send emails to their customers. It provides a scalable and cost-effective solution for sending transactional and marketing emails. Amazon SES is designed to integrate with other AWS services and can be easily integrated into applications using the AWS SDKs.</p>
    
    <h2>Amazon SNS</h2>
    <p>Amazon SNS is a messaging service that allows applications to send notifications to a variety of endpoints. It supports multiple protocols, including email, SMS, and push notifications. Amazon SNS can be used for a variety of use cases, including sending alerts, notifications, and updates.</p>
    
    <h2>Integration of SES and SNS</h2>
    <p>Integrating Amazon SES and SNS is a straightforward process that involves creating an SNS topic and subscribing SES to that topic. Once subscribed, SES can send bounce, complaint, and delivery notifications to the SNS topic, which can then be forwarded to other endpoints as needed.</p>
    <p>Another way to integrate SES and SNS is through the use of AWS Lambda. When an email is sent through SES, a Lambda function can be triggered to perform additional processing, such as analytics or personalization. The Lambda function can then use SNS to send a notification to another endpoint, such as Slack or a database.</p>
    
    <h2>Problems their integration solves</h2>
    <p>Integrating Amazon SES and SNS can solve a variety of problems related to email delivery. By using SES to send emails and SNS to handle notifications, businesses can:</p>
    <ul>
      <li>Receive instant notifications of email bounces and complaints</li>
      <li>Track email delivery and engagement metrics</li>
      <li>Perform real-time analytics on email campaigns</li>
      <li>Personalize messages based on user behavior and demographics</li>
      <li>Reduce the risk of emails being marked as spam or blocked by email providers</li>
    </ul>
    
    <h2>Conclusion</h2>
    <p>Integrating Amazon SES and SNS is a powerful way to improve your email delivery system. By combining these two services, businesses can improve delivery rates, reduce the risk of messages being marked as spam, and gain valuable insights into user behavior. Whether you're sending transactional emails or marketing campaigns, SES and SNS provide a scalable and cost-effective solution for reliably sending messages to your customers.</p>
</div>
---
layout: default
title: Contact - Team Brookvale
permalink: /contact
description: "We develop software products and provide digital platform engineering services on the Northern Beaches of Sydney"
---
 <script type="text/javascript" src="https://cdn.emailjs.com/sdk/2.2.4/email.min.js"></script>
 <script type="text/javascript">
  (function(){
            emailjs.init("user_knG2BzWL3cFIviNKOkKF5");
        })();
  </script>
<script type="text/javascript">
    function getIp(json){
        window.ipAddress = json.ip;
    }

    function sendEmail(event) {
        var button = document.getElementById("submit-button");
        var service_id = 'gmail-longbtomi';
        var template_id = 'contact_form';
        var form = document.forms['contactForm'];
        var templateParams = {
            name: form["name"].value,
            from_email: form["from_email"].value,
            phone: form["phone"].value,
            message: form["message"].value,
            ip: window.ipAddress != null && window.ipAddress != undefined ? window.ipAddress : "N/A"
        }; 

        if(form["additional_field"].value != ""){
            return;
        }

        button.innerHTML = '<span><i class="fas fa-spinner fa-spin"></i> Sending...</span>';
        button.disabled = true;

         emailjs.send(service_id, template_id, templateParams)
            .then(function(response) {
                button.innerHTML = '<span><i class="fas fa-check"></i> Message sent!</span>';
            }, function(error) {
                button.disabled = false;
                button.innerHTML = 'Send message';
                alert("We are terribly sorry, but we have not been able to send your message. Please try again, and if that fails, contact us directly via e-mail. Thank you!")
            });        
    }  
</script>
<script type="text/javascript" src="https://api.ipify.org?format=jsonp&callback=getIp"></script>
<div class="contactpage">
    <div class="pagehero">
        <div class="inner flex sb">
            <div>
                <h1>Contact</h1>
                <p style="margin-bottom: 50px">We develop software products and provide digital platform engineering services on the Northern Beaches of Sydney</p>
                <img src="/assets/images/arrowdown.png">
            </div>
            <div>
                <img  class="pageheropic jumptop" src="/assets/images/xlifestyle-working-brookvale.webp">
            </div>
        </div>
    </div>
    <div class="inner flex sb">
        <div style="width: 659px">
            <h2>Sign up for your free 45 minute Project Discovery Workshop</h2>
            <div class="mid gray">
                Team Brookvale helps you to improving business efficiency through implementing mobile technologies. From iOS business apps through games and IoT solutions Team Brookvale provides a full consulting and development service. Take advantage of working with a local development team!
            </div>
            <div class="contact semibold" style="margin: 30px 0 40px 0">
                <div class="floleft" style="width: 150px">Phone:</div><div class="bluetext">{{ site.data.text.footer.phone }}</div>
                <div class="floleft" style="width: 150px">Email:</div><div class="bluetext">{{ site.data.text.footer.email }}</div>
            </div>
            <div>
                <a href="https://www.facebook.com/teambrookvale" class="socialmedia fb"><i class="fab fa-facebook-f"></i></a>
                <a href="http://twitter.com/teambrookvale" class="socialmedia tw"><i class="fab fa-twitter"></i></a>
                <!--<a href="https://www.youtube.com/channel/UCpFdJdlijg9qK7p3su-9J_Q" class="socialmedia yt"><i class="fab fa-youtube"></i></a>
                <a href="http://teambrookvale.tumblr.com" class="socialmedia tm"><i class="fab fa-tumblr"></i></a>-->
            </div>
            <div class="map-holder">
                <div>
                     <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3316.758445082223!2d151.26014485137583!3d-33.76690738058974!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12aa46876df29f%3A0x9fd196ca7df78eff!2s117+Old+Pittwater+Rd%2C+Brookvale+NSW+2100!5e0!3m2!1sen!2sau!4v1459312995857" width="100%" height="100%" frameborder="0" style="border:0" allowfullscreen=""></iframe>
                </div>
            </div>
        </div>
        <div style="width: 460px">
            <form id="contactForm" style="margin-bottom: 80px" onsubmit="sendEmail();return false">
                <input class="d-none" name="additional_field" type="text" />
                <div class="row">
                    <label>Name</label>
                    <input type="text" required name="name" placeholder="Name">
                </div>
                <div class="flex sb">
                    <div style="width: 48%">
                        <div class="row">
                            <label>Email</label>
                            <input type="email" required name="from_email" placeholder="Email">
                        </div>
                    </div>
                    <div style="width: 48%">
                        <div class="row">
                            <label>Phone number</label>
                            <input type="text" required name="phone" placeholder="Phone number">
                        </div>
                    </div>
                </div>
                <div class="row">
                    <label>Message</label>
                    <textarea name="message" required placeholder="Your message here..."></textarea>
                </div>
                <div class="row buttons">
                    <button id="submit-button" type="submit">Send message</button>
                </div>
            </form>
        </div>
    </div>
</div>
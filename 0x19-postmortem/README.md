<h1>Postmortem : Payment website experience outage</h1>

<h2>Issue Summary:</h2>

On the 25th of December 2022, at around 12:02am, our website experienced very huge spikes in traffic. This traffic continued to grow exponentially until we were effectively knocked off the internet. The issue impacted all users and companies that rely on our services, with 100% of our user base being affected. Users were unable to access the website, and error messages were reported.

<h2>Root Cause:</h2>

After investigations were carried out, it was discovered to be a distributed denial of service(DDos) attack by the Lazarus Group, an advanced persistent threat actor (formerly called APT38). This attack was executed using the Kraken botnet. The overwhelming amount of traffic directed towards ours servers was used to render the site unusable.

<h2>Timeline:</h2>

- 12:02 AM - Our monitoring system detected a significant increase in server errors and latency on our payment site.

- 12:04 AM - Engineers on site received alerts and started investigating the issue.

- 12:10 AM - The Engineers noticed an exponential growth in the amount of incoming traffic, resulting in the servers being overloaded and was eventually taken offline.

- 12:40 AM - An attempted was made by the engineers to bring the site online, but after a few minutes the servers were bombarded with traffic which rendered it unusable.

- 12:50 AM - The issue was escalated by engineers onsite to the senior engineering team, as well as an incident response team. Investigation began immediately.

- 05:30 AM - The team was able to identify the cause, as well as pinpoint the source of the attack. Problems were fixed and the site was brought back online.

<h2>Resolution:</h2>

The incident response team investigated the entire system and ensure that there was no persistent connection planted in our system or data stolen by the threat actor. Our engineering team then implemented efficient and robust measures to tackle future problems.

<h2>Corrective and Preventative Measures:</h2>

To prevent similar issues in the future, we will be implementing the following corrective and preventative measures:

- In addition to our inhouse DDos mitigation systems, our engineering team opted for the services of  a robust third party DDos mitigation company (Cloudflare).

- Implemented a robust disaster recovery plan to quickly recover from future outages in record time.

- Installed more robust monitoring system to detect anomalies and potential issues on time. 

- Carrying out regular Pen-tests to identify potential issues and ensure we have the necessary resources to handle them in an efficient manner.

<h2>In summary</h2>
The attack on the 25th of December 2022 was caused by a distributed denial of service (DDos) by a state actor, which led to the site being taken offline. The issue was resolved by integrating a robust DDos mitigation service to our system. Going forward, we will be implementing several preventative and corrective measures to handle issues that may arise.  All these are done improve our overall web stack reliability and to provide top notch service to our beloved customers.

To our wonderful and loverly customers, don't you f*ck**ng take us to court. :raised_eyebrow:

Abeg, na Beg!!! :rofl:  :joy:



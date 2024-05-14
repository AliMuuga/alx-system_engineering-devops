Postmortem: Web Stack Debugging Outage

Issue Summary:
- Duration: The outage was on 29th Feburary 2024 from 14:00 hours to 15:00 hours CAT.
- Impact: It was a complete service outage for every user of the website, with 100% downtime during the affected period.
- Root Cause: The outages were identified to have been caused by a badly configured Apache server that would crash periodically.

Timeline:
- 14:00 AM: Monitoring alerts reported this issue, indicating the server was unresponsive.
- 14:05 AM: The engineers trying to access the website noticed the failure.
- 14:10 AM: Preliminary investigation was aimed at health metrics of servers and analysis of logs.
- 14:15 AM: Took the assumed root cause to be a traffic spike that was overwhelming the server's resources.
- 14:20 AM: Misled by the assumption, scaled up the server capacity, but it didn't solve the problem.
- 14:25 AM: Incident escalated to senior engineering team to dig deeper.
- 14:30 AM: Verbose log examination has shown that the Apache server crashes coincide with high traffic.
- 14:35 AM: Misconfiguration detected in the Apache settings; resulting in increased memory consumption.
- 14:40 AM: Modified Apache server configuration to reduce memory consumption and avoid crashing.
- 14:50 AM: Server restarted with new configuration.
- 15:00 AM: Website service was restored, and users were able to access the site.

Root Cause and Resolution:
Root Cause: Misconfigured Apache server settings—resulting in memory exhaustion and servers going down at peak traffic.
Resolution: Adjusted Apache server configuration to ensure efficient usage of memory so as not to crash. Set up more vigilant monitoring to pick up spikes in resource utilization early.

Corrective and Preventative Measures:
Enhanced monitoring: The monitoring system should be improved in order to detect and alert on spikes in resource utilization in a timely manner.
Configuration Management: Use version-controlled configuration management to avoid accidental misconfigurations.
- Automated testing: Allow the server configurations to be automatically testable, so any change made can be validated before deployment.
Regular audit: There needs to be a regular audit of server configurations done to identify and proactively remediate potential issues.
• Incident response training: Train engineering teams on incident responses for faster and effective response at the time of outages.

Tasks to Address the Issue:
1. Patch Apache server configuration in order to have memory usage optimized.

2. Apply more rigorous monitoring thresholds for resource consumption. 3. Use version-controlled configuration management for all server settings. 4. Develop automated tests that verify the server configuration. 5. Regularly audit configurations on servers to ensure they are in compliance with best practices. This postmortem underlines a proactive monitoring role, a strict configuration management, and continuous improvement in order to reduce the impact of the outage and increase reliability.

For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails.md)
.

You can require all new accounts to be verified by email. This prevents malicious admins from registering accounts without email verification.

Prerequisites[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails#prerequisites)

-------------------------------------------------------------------------------------------------------------

*   SMTP must be set up and n8n must be able to send emails.
    

How to restrict account registration[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails#how-to-restrict-account-registration)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Set the environment variable `N8N_INVITE_LINKS_EMAIL_ONLY` to `true`. This locks down your instance so that only users with verified email addresses can register.

For more details on configuring SMTP, see [Set up SMTP](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management#step-one-smtp)
.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    

[PreviousHarden task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners)
[NextEnable SSRF protection](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection)

Last updated 10 days ago

Was this helpful?
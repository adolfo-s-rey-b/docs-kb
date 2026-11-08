For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/send-email/outlook.md)
.

**Feature availability**

Microsoft deprecated Basic Authentication and app passwords for SMTP in Exchange Online and Outlook.com. As a result, the Send Email node **cannot connect to Outlook.com or Microsoft 365 accounts** using username/password or app password authentication.

**To send email from your Outlook.com or Microsoft 365 account, use the** [**Microsoft Outlook node**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook)
**, which uses OAuth 2.0 as required by Microsoft.**

Refer to [Microsoft's deprecation notice](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)
 for more information.

[PreviousGmail](https://docs.n8n.io/integrations/builtin/credentials/send-email/gmail)
[NextYahoo](https://docs.n8n.io/integrations/builtin/credentials/send-email/yahoo)

Last updated 10 days ago

Was this helpful?
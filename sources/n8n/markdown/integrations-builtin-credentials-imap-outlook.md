For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/imap/outlook.md)
.

**Feature availability**

Microsoft deprecated Basic Authentication for IMAP in Exchange Online and Outlook.com from October 1, 2022. As a result, the IMAP node **can't connect to Outlook.com or Microsoft 365 accounts**. App passwords are not a workaround for this restriction.

**Use the** [**Microsoft Outlook node**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook)
 **instead.** It uses OAuth 2.0, which Microsoft now requires for mail access.

Refer to [Microsoft's deprecation notice](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)
 for more information.

Outlook.com IMAP credentials[](https://docs.n8n.io/integrations/builtin/credentials/imap/outlook#outlookcom-imap-credentials)

------------------------------------------------------------------------------------------------------------------------------

IMAP access for Outlook.com and Microsoft 365 accounts is no longer supported in n8n due to Microsoft's deprecation of Basic Authentication for Exchange Online and Outlook.com from October 1, 2022. You can't use IMAP (with a regular password or app password) to connect to Outlook.com or Microsoft 365 accounts.

To replace IMAP triggers for incoming email, use the [Microsoft Outlook Trigger node](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger)
, which supports the Message Received event.

For general Microsoft Outlook automation, use the [Microsoft Outlook node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook)
, which uses OAuth 2.0 as required by Microsoft.

For more information, refer to [Microsoft's deprecation notice](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)
.

[PreviousGmail](https://docs.n8n.io/integrations/builtin/credentials/imap/gmail)
[NextYahoo](https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo)

Last updated 10 days ago

Was this helpful?
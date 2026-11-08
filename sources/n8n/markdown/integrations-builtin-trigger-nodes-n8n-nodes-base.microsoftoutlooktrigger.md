For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)
.

Use the Microsoft Outlook Trigger node to respond to events in [Microsoft Outlook](https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook)
 and integrate Microsoft Outlook with other applications.

On this page, you'll find a list of events the Microsoft Outlook Trigger node can respond to, and links to more resources.

**Credentials**

This node's **Authentication** dropdown offers three options:

*   **Outlook OAuth2**: the Microsoft Outlook-specific OAuth2 credential (default).
    
*   **Microsoft OAuth2 (Graph)**: a generic Microsoft Graph credential that you can reuse across other Microsoft nodes. When you select this option, make sure you grant the credential the scopes this node needs (for example, `Mail.ReadWrite`).
    
*   **Microsoft Entra Service Principal (App-Only)**: app-only access through a Microsoft Entra app registration, with no signed-in user. Refer to [Microsoft Entra Service Principal credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
     for setup and required application permissions.
    

Refer to the [Microsoft credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/microsoft)
 for authentication information for this node.

**Government Cloud Support**

If you're using a government cloud tenant (US Government, US Government DOD, or China), make sure to select the appropriate **Microsoft Graph API Base URL** in your Microsoft credentials configuration.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Microsoft Outlook integrations](https://n8n.io/integrations/microsoft-outlook-trigger/)
 page.

Events[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger#events)

---------------------------------------------------------------------------------------------------------------

*   Message Received
    

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

n8n provides an app node for Microsoft Outlook. Refer to the [Microsoft Outlook node documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook)
 for more information.

View [example workflows and related content](https://n8n.io/integrations/microsoft-outlook-trigger/)
 on n8n's website.

[PreviousMicrosoft OneDrive Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger)
[NextMicrosoft SharePoint Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/raindrop.md)
.

You can use these credentials to authenticate the following nodes:

*   [Raindrop](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.raindrop)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/raindrop#prerequisites)

---------------------------------------------------------------------------------------------

Create a [Raindrop](https://raindrop.io/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/raindrop#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/raindrop#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Raindrop's API documentation](https://developer.raindrop.io/)
 for more information about the service.

Using OAuth[](https://docs.n8n.io/integrations/builtin/credentials/raindrop#using-oauth)

-----------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**
    
*   A **Client Secret**
    

Generate both by creating a Raindrop app.

To create an app, go to **Settings >** [**Integrations**](https://app.raindrop.io/settings/integrations)
 and select **\+ Create new app** in the **For Developers** section.

Use these settings for your app:

*   Copy the **OAuth Redirect URL** from n8n and add it as a **Redirect URI** in your app.
    
*   Copy the **Client ID** and **Client Secret** from the Raindrop app and enter them in your n8n credential.
    

[PreviousRabbitMQ credentials](https://docs.n8n.io/integrations/builtin/credentials/rabbitmq)
[NextRapid7 InsightVM credentials](https://docs.n8n.io/integrations/builtin/credentials/rapid7insightvm)

Last updated 10 days ago

Was this helpful?
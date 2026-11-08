For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/xero.md)
.

You can use these credentials to authenticate the following nodes:

*   [Xero](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.xero)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/xero#prerequisites)

-----------------------------------------------------------------------------------------

Create a [Xero](https://www.xero.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/xero#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/xero#related-resources)

-------------------------------------------------------------------------------------------------

Refer to [Zero's API documentation](https://developer.xero.com/documentation/api/accounting/overview)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/xero#using-oauth2)

---------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated when you create a new app for a custom connection.
    
*   A **Client Secret**: Generated when you create a new app for a custom connection.
    

To generate your Client ID and Client Secret, [create an OAuth2 custom connection app](https://developer.xero.com/documentation/guides/oauth2/custom-connections/)
 in your Xero developer portal [**My Apps**](https://developer.xero.com/app/manage)
.

Use these settings for your app:

**Xero App Name**

Xero doesn't support app instances within the Xero Developer Centre that contain `n8n` in their name.

*   Select **Web app** as the **Integration Type**.
    
*   For the **Company or Application URL**, enter the URL of your n8n server or reverse proxy address. For cloud users, for example, this is: `https://your-username.app.n8n.cloud/`.
    
*   Copy the **OAuth Redirect URL** from n8n and add it as an **OAuth 2.0 redirect URI** in your app.
    
*   Select appropriate **scopes** for your app. Refer to [OAuth2 Scopes](https://developer.xero.com/documentation/guides/oauth2/scopes/)
     for more information.
    
    *   To use all functionality in the [Xero](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.xero)
         node, add the `accounting.contacts` and `accounting.transactions` scopes.
        
    

Refer to Xero's [OAuth Custom Connections](https://developer.xero.com/documentation/guides/oauth2/custom-connections)
 documentation for more information.

[PreviousXata credentials](https://docs.n8n.io/integrations/builtin/credentials/xata)
[NextYourls credentials](https://docs.n8n.io/integrations/builtin/credentials/yourls)

Last updated 10 days ago

Was this helpful?
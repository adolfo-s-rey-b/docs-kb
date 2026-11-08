For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/webflow.md)
.

You can use these credentials to authenticate the following nodes:

*   [Webflow](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.webflow)
    
*   [Webflow Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/webflow#prerequisites)

--------------------------------------------------------------------------------------------

*   Create a [Webflow](https://webflow.com/)
     account.
    
*   [Create a site](https://developers.webflow.com/data/reference/structure-1#sites)
    : Required for API access token authentication only.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/webflow#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   API access token
    
*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/webflow#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Webflow's API documentation](https://developers.webflow.com/data/reference/rest-introduction)
 for more information about the service.

Using API access token[](https://docs.n8n.io/integrations/builtin/credentials/webflow#using-api-access-token)

--------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A Site **Access Token**: Access tokens are site-specific. Go to your site's **Site Settings > Apps & integrations > API access** and select **Generate API token**. Refer to [Get a Site Token](https://developers.webflow.com/data/v1.0.0/docs/get-a-site-token)
     for more information.
    

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/webflow#using-oauth2)

------------------------------------------------------------------------------------------

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you need to configure OAuth2 from scratch, [register an application](https://developers.webflow.com/data/docs/register-an-app)
 in your workspace.

Use these settings for your application:

*   Copy the **OAuth callback URL** from n8n and add it as a **Redirect URI** in your application.
    
*   Once you've created your application, copy the **Client ID** and **Client Secret** and enter them in your n8n credential.
    
*   The Webflow Data API V1 is deprecated. If you're using it, enable the **Legacy** toggle. Otherwise, leave this inactive.
    

Refer to [OAuth](https://developers.webflow.com/data/reference/oauth-app)
 for more information on Webflow's OAuth web flow.

[PreviousWebex by Cisco credentials](https://docs.n8n.io/integrations/builtin/credentials/ciscowebex)
[NextWebhook credentials](https://docs.n8n.io/integrations/builtin/credentials/webhook)

Last updated 10 days ago

Was this helpful?
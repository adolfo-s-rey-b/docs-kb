For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/strava.md)
.

You can use these credentials to authenticate the following nodes:

*   [Strava](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.strava)
    
*   [Strava Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/strava#prerequisites)

-------------------------------------------------------------------------------------------

*   Create a [Strava](https://strava.com/)
     account.
    
*   Create a Strava application in [**Settings > API**](https://www.strava.com/settings/api)
    . Refer to [Using OAuth2](https://docs.n8n.io/integrations/builtin/credentials/strava#using-oauth2)
     for more information.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/strava#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/strava#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Strava's API documentation](https://developers.strava.com/docs/reference/)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/strava#using-oauth2)

-----------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated when you [create a Strava app](https://developers.strava.com/docs/getting-started/#account)
    .
    
*   A **Client Secret**: Generated when you [create a Strava app](https://developers.strava.com/docs/getting-started/#account)
    .
    

Use these settings for your Strava app:

*   In n8n, copy the **OAuth Callback URL**. Paste this URL into your Strava app's **Authorization Callback Domain**.
    
*   Remove the protocol (`https://` or `http://`) and the relative URL (`/oauth2/callback` or `/rest/oauth2-credential/callback`) from the **Authorization Callback Domain**. For example, if the OAuth Redirect URL was originally `https://oauth.n8n.cloud/oauth2/callback`, the **Authorization Callback Domain** would be `oauth.n8n.cloud`.
    
*   Copy the **Client ID** and **Client Secret** from your app and add them to your n8n credential.
    

Refer to [Authentication](https://developers.strava.com/docs/authentication/)
 for more information about Strava's OAuth flow.

[PreviousStrapi credentials](https://docs.n8n.io/integrations/builtin/credentials/strapi)
[NextStripe credentials](https://docs.n8n.io/integrations/builtin/credentials/stripe)

Last updated 10 days ago

Was this helpful?
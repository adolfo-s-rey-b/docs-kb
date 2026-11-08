For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/sentryio.md)
.

You can use these credentials to authenticate the following nodes:

*   [Sentry.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#prerequisites)

---------------------------------------------------------------------------------------------

Create a [Sentry.io](https://sentry.io/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   API token
    
*   OAuth2
    
*   Server API token: Use for [self-hosted Sentry](https://develop.sentry.dev/self-hosted/)
    .
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Sentry.io's API documentation](https://docs.sentry.io/api/)
 for more information about the service.

Using API token[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#using-api-token)

-------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An API **Token**: Generate a [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)
     in **Account > Settings > User Auth Tokens**. Refer to [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)
     for more information.
    

Using OAuth[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#using-oauth)

-----------------------------------------------------------------------------------------

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you need to configure OAuth2 from scratch, [create an integration](https://docs.sentry.io/organization/integrations/integration-platform/#creating-an-integration)
 with these settings:

*   Copy the n8n **OAuth Callback URL** and add it as an **Authorized Redirect URI**.
    
*   Copy the **Client ID** and **Client Secret** and add them to your n8n credential.
    

Refer to [Public integrations](https://docs.sentry.io/organization/integrations/integration-platform/public-integration/)
 for more information on creating the integration.

Using Server API token[](https://docs.n8n.io/integrations/builtin/credentials/sentryio#using-server-api-token)

---------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An API **Token**: Generate a [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)
     in **Account > Settings > User Auth Tokens**. Refer to [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)
     for more information.
    
*   The **URL** of your self-hosted Sentry instance.
    

[PreviousSendy credentials](https://docs.n8n.io/integrations/builtin/credentials/sendy)
[NextSerp credentials](https://docs.n8n.io/integrations/builtin/credentials/serp)

Last updated 10 days ago

Was this helpful?
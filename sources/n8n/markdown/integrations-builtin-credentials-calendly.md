For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/calendly.md)
.

You can use these credentials to authenticate the following nodes:

*   [Calendly Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger)
    

**Supported Calendly plans**

The Calendly Trigger node relies on Calendly webhooks. Calendly only offers access to webhooks in their paid plans.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/calendly#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   Personal Access Token
    
*   OAuth2
    

Required scopes[](https://docs.n8n.io/integrations/builtin/credentials/calendly#required-scopes)

-------------------------------------------------------------------------------------------------

To use Calendly nodes and triggers in n8n, your credentials must have the following scopes:

*   `users:read`: Read user information
    
*   `webhooks:read`: Read webhook subscriptions
    
*   `webhooks:write`: Create and manage webhook subscriptions
    
*   `scheduled_events:read`: Read scheduled event information
    

Personal Access Tokens also require the same scopes. When creating a Personal Access Token in Calendly, select the same scopes listed above.

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/calendly#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Calendly's API documentation](https://developer.calendly.com/getting-started)
 for more information about the service.

Using Personal Access Token[](https://docs.n8n.io/integrations/builtin/credentials/calendly#using-personal-access-token)

-------------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Calendly](https://www.calendly.com/)
 account and:

*   A **Personal Access Token**
    

To get your access token:

1.  Go to the Calendly [**Integrations & apps**](https://calendly.com/integrations)
     page.
    
2.  Select [**API & Webhooks**](https://calendly.com/integrations/api_webhooks)
    .
    
3.  In **Your Personal Access Tokens**, select **Generate new token**.
    
4.  Enter a **Name** for your access token, like `n8n integration`.
    
5.  Select **Create token**.
    
6.  Select **Copy token** and enter it in your n8n credential.
    

Refer to [Calendly's API authentication documentation](https://developer.calendly.com/docs/authentication/how-to-authenticate-with-personal-access-tokens)
 for more information.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/calendly#using-oauth2)

-------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Calendly developer](https://developer.calendly.com/)
 account and:

*   A **Client ID**
    
*   A **Client Secret**
    

To get both, create a new OAuth app in Calendly:

1.  Log in to Calendly's developer portal and go to [**My apps**](https://developer.calendly.com/console/apps)
    .
    
2.  Select **Create new app**.
    
3.  Enter a **Name of app**, like `n8n integration`.
    
4.  In **Kind of app**, select **Web**.
    
5.  In **Environment type**, select the environment that corresponds to your usage, either **Sandbox** or **Production**.
    
    *   Calendly recommends starting with **Sandbox** for development and creating a second application for **Production** when you're ready to go live.
        
    
6.  Copy the **OAuth Redirect URL** from n8n and enter it as a **Redirect URI** in the OAuth app.
    
7.  In the **Scopes** section, add the following required scopes:
    
    *   `users:read`
        
    *   `webhooks:read`
        
    *   `webhooks:write`
        
    *   `scheduled_events:read`
        
    
8.  Select **Save & Continue**. The app details display.
    
9.  Copy the **Client ID** and enter this as your n8n **Client ID**.
    
10.  Copy the **Client secret** and enter this as your n8n **Client Secret**.
    
11.  Select **Connect my account** in n8n and follow the on-screen prompts to finish authorizing the credential.
    

Refer to [Registering your application with Calendly](https://developer.calendly.com/docs/authentication/creating-an-oauth-app)
 for more information.

**Local OAuth2 testing**

When testing OAuth2 with a tunnel (such as ngrok or Cloudflare Tunnel), open n8n through the same public URL you used as the **OAuth Redirect URL**. Otherwise, the OAuth callback may fail because the n8n session cookie belongs to a different host.

[PreviousCal.com credentials](https://docs.n8n.io/integrations/builtin/credentials/cal)
[NextCarbon Black credentials](https://docs.n8n.io/integrations/builtin/credentials/carbonblack)

Last updated 10 days ago

Was this helpful?
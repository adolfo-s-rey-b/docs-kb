For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/twist.md)
.

You can use these credentials to authenticate the following nodes:

*   [Twist](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/twist#prerequisites)

------------------------------------------------------------------------------------------

*   Create a [Twist](https://twist.com/)
     account.
    
*   [Create a general integration](https://twist.com/app_console/create_app)
     and configure a valid OAuth Redirect URL. Refer to [Using OAuth2](https://docs.n8n.io/integrations/builtin/credentials/twist#using-oauth2)
     for more information.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/twist#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/twist#related-resources)

--------------------------------------------------------------------------------------------------

Refer to [Twist's API documentation](https://developer.twist.com/v3/#authorization)
 for more information about authenticating with the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/twist#using-oauth2)

----------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated once you create a general integration.
    
*   A **Client Secret**: Generated once you create a general integration.
    

To generate your Client ID and Client Secret, [create a general integration](https://twist.com/app_console/create_app)
.

Use these settings for your integration's **OAuth Authentication**:

*   Copy the **OAuth Redirect URL** from n8n and enter it as the **OAuth 2 redirect URL** in Twist.
    
    **OAuth Redirect URL for self-hosted n8n**
    
    Twist doesn't accept a `localhost` Redirect URL. The Redirect URL should be a URL in your domain, for example: `https://mytemplatemaker.example.com/gr_callback`. If your n8n **OAuth Redirect URL** contains localhost, refer below to [Local environment redirect URL](https://docs.n8n.io/integrations/builtin/credentials/twist#local-environment-redirect-url)
     for generating a URL that Twist will allow.
    
*   Select **Update OAuth settings** to save those changes.
    
*   Copy the **Client ID** and **Client Secret** from Twist and enter them in the appropriate fields in n8n.
    

### Local environment redirect URL[](https://docs.n8n.io/integrations/builtin/credentials/twist#local-environment-redirect-url)

Twist doesn't accept a localhost callback URL. These steps should allow you to configure the OAuth credentials for the local environment:

1.  Use [ngrok](https://ngrok.com/)
     to expose the local server running on port `5678` to the internet. In your terminal, run the following command:
    

Copy

    ngrok http 5678

1.  Run the following command in a new terminal. Replace `<YOUR-NGROK-URL>` with the URL that you get from the previous step. `N8N_WEBHOOK_URL` is available from n8n 2.30.0; on earlier versions, use `WEBHOOK_URL`.
    

Copy

    export N8N_WEBHOOK_URL=<YOUR-NGROK-URL>

1.  Use the generated URL as your **OAuth 2 redirect URL** in Twist.
    

[PreviousTwilio credentials](https://docs.n8n.io/integrations/builtin/credentials/twilio)
[NextTypeform credentials](https://docs.n8n.io/integrations/builtin/credentials/typeform)

Last updated 10 days ago

Was this helpful?
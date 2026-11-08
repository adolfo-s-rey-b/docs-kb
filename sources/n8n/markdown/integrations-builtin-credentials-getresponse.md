For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/getresponse.md)
.

You can use these credentials to authenticate the following nodes:

*   [GetResponse](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.getresponse)
    
*   [GetResponse Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#prerequisites)

------------------------------------------------------------------------------------------------

Create a [GetResponse](https://www.getresponse.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------------

*   API key
    
*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#related-resources)

--------------------------------------------------------------------------------------------------------

Refer to [GetResponse's API documentation](https://apidocs.getresponse.com/v3)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#using-api-key)

------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: To view or generate an API key, go to **Integrations and API > API**. Refer to the [GetResponse Help Center](https://www.getresponse.com/help/where-do-i-find-the-api-key.html)
     for more detailed instructions.
    

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#using-oauth2)

----------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated when you [register your application](https://apidocs.getresponse.com/v3/authentication/oauth2)
    .
    
*   A **Client Secret**: Generated when you [register your application](https://apidocs.getresponse.com/v3/authentication/oauth2)
     as the **Client Secret Key**.
    

When you register your application, copy the **OAuth Redirect URL** from n8n and add it as the **Redirect URL** in GetResponse.

**Redirect URL with localhost**

The Redirect URL should be a URL in your domain, for example: `https://mytemplatemaker.example.com/gr_callback`. GetResponse doesn't accept a localhost callback URL. Refer to the [FAQs](https://docs.n8n.io/integrations/builtin/credentials/getresponse#configure-oauth2-credentials-for-a-local-environment)
 to configure the credentials for the local environment.

Configure OAuth2 credentials for a local environment[](https://docs.n8n.io/integrations/builtin/credentials/getresponse#configure-oauth2-credentials-for-a-local-environment)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GetResponse doesn't accept the localhost callback URL. Follow the steps below to configure the OAuth credentials for a local environment:

1.  Use [ngrok](https://ngrok.com/)
     to expose the local server running on port `5678` to the internet. In your terminal, run the following command:
    

Copy

    ngrok http 5678

1.  Run the following command in a new terminal. Replace `<YOUR-NGROK-URL>` with the URL that you got from the previous step. `N8N_WEBHOOK_URL` is available from n8n 2.30.0; on earlier versions, use `WEBHOOK_URL`.
    

Copy

    export N8N_WEBHOOK_URL=<YOUR-NGROK-URL>

1.  Follow the [Using OAuth2](https://docs.n8n.io/integrations/builtin/credentials/getresponse#using-oauth2)
     instructions to configure your credentials, using this URL as your **Redirect URL**.
    

[PreviousFTP credentials](https://docs.n8n.io/integrations/builtin/credentials/ftp)
[NextGhost credentials](https://docs.n8n.io/integrations/builtin/credentials/ghost)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/linear.md)
.

You can use these credentials to authenticate the following nodes:

*   [Linear Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger)
    
*   [Linear](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linear)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/linear#prerequisites)

-------------------------------------------------------------------------------------------

Create a [Linear](https://linear.app/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/linear#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API key
    
*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/linear#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Linear's API documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/linear#using-api-key)

-------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A personal **API Key**: Create a dedicated personal API key in your [**Settings** > **Security & access**](https://linear.app/n8n/settings/account/security)
    . Refer to the [Linear Personal API keys documentation](https://linear.app/developers/graphql#personal-api-keys)
     for more information.
    

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/linear#using-oauth2)

-----------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Client ID**: Generated when you create a new OAuth2 application.
    
*   A **Client Secret**: Generated when you create a new OAuth2 application.
    
*   Select the **Actor**: The actor defines how the OAuth2 application should create issues, comments and other changes. Options include:
    
    *   **User** (Linear's default): The application creates resources as the authorizing user. Use this option if you want each user to do their own authentication.
        
    *   **Application**: The application creates resources as itself. Use this option if you have only one user (like an admin) authorizing the application.
        
    
*   To use this credential with the [Linear Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger)
     node, you must enable the **Include Admin Scope** toggle.
    

Refer to the [Linear OAuth2 Authentication documentation](https://developers.linear.app/docs/oauth/authentication)
 for more detailed instructions and explanations. Use the n8n **OAuth Redirect URL** as the **Redirect callback URL** in your Linear OAuth2 application.

[PreviousLine credentials](https://docs.n8n.io/integrations/builtin/credentials/line)
[NextLingvaNex credentials](https://docs.n8n.io/integrations/builtin/credentials/lingvanex)

Last updated 10 days ago

Was this helpful?
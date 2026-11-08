For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter.md)
.

You can use these credentials to authenticate the following nodes:

*   [Venafi TLS Protect Datacenter node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter#prerequisites)

---------------------------------------------------------------------------------------------------------------

*   Create a Venafi [TLS Protect Datacenter](https://venafi.com/)
     account.
    
*   Set the expiration and refresh time for tokens. Refer to [Setting up token authentication](https://docs.venafi.com/Docs/current/TopNav/Content/SDK/AuthSDK/t-SDKa-Setup-OAuth.php)
     for more information.
    
*   Create an [API integration](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/c-APIAppIntegrations-about.php)
     in **API > Integrations**. Refer to [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php)
     for detailed instructions.
    
    *   Take note of the Client ID for your integration.
        
    *   Choose the scopes needed for the operations you want to perform within n8n. Refer to the scopes table in [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php)
         for more details on available scopes.
        
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------------------------

*   API integration
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter#related-resources)

-----------------------------------------------------------------------------------------------------------------------

Refer to [Venafi's API integration documentation](https://docs.venafi.com/Docs/currentSDK/TopNav/Content/SDK/WebSDK/c-sdk-AboutThisGuide.php)
 for more information about the service.

Using API integration[](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter#using-api-integration)

-------------------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Domain**: Enter your Venafi TLS Protect Datacenter domain.
    
*   A **Client ID**: Enter the **Client ID** from your API integration. Refer to the information and links in [Prerequisites](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter#prerequisites)
     for more information on creating an API integration.
    
*   A **Username**: Enter your username.
    
*   A **Password**: Enter your password.
    
*   **Allow Self-Signed Certificates**: If turned on, the credential will allow self-signed certificates.
    

[PreviousVenafi TLS Protect Cloud credentials](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud)
[NextVercel AI Gateway credentials](https://docs.n8n.io/integrations/builtin/credentials/vercel)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/zoho.md)
.

You can use these credentials to authenticate the following nodes:

*   [Zoho CRM](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/zoho#prerequisites)

-----------------------------------------------------------------------------------------

Create a [Zoho](https://www.zoho.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/zoho#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/zoho#related-resources)

-------------------------------------------------------------------------------------------------

Refer to [Zoho's CRM API documentation](https://www.zoho.com/crm/developer/docs/api/v3/)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/zoho#using-oauth2)

---------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **Access Token URL**: Zoho provides region-specific access token URLs. Select the region that best fits your Zoho data center:
    
    *   **AU**: Select this option for Australia data center.
        
    *   **CN**: Select this option for Canada data center.
        
    *   **EU**: Select this option for the European Union data center.
        
    *   **IN**: Select this option for the India data center.
        
    *   **US**: Select this option for the United States data center.
        
    

Refer to [Multi DC](https://www.zoho.com/crm/developer/docs/api/v3/multi-dc.html)
 for more information about selecting a data center.

**Note for n8n Cloud users**

Cloud users don't need to provide connection details. Select **Connect my account** to connect through your browser.

If you need to configure OAuth2 from scratch, [register an application](https://www.zoho.com/accounts/protocol/oauth-setup.html)
 with Zoho.

Use these settings for your application:

*   Select **Server-based Applications** as the **Client Type**.
    
*   Copy the **OAuth Callback URL** from n8n and enter it in the Zoho **Authorized Redirect URIs** field.
    
*   Copy the **Client ID** and **Client Secret** from the application and enter them in your n8n credential.
    

[PreviousZep credentials](https://docs.n8n.io/integrations/builtin/credentials/zep)
[NextZoom credentials](https://docs.n8n.io/integrations/builtin/credentials/zoom)

Last updated 10 days ago

Was this helpful?
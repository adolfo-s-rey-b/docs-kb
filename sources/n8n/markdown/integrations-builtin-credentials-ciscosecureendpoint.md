For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint#prerequisites)

--------------------------------------------------------------------------------------------------------

*   Create a [Cisco DevNet developer account](https://developer.cisco.com/)
    .
    
*   Access to a [Cisco Secure Endpoint license](https://www.cisco.com/site/us/en/products/security/endpoint-security/secure-endpoint/index.html)
    .
    

Authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint#authentication-methods)

--------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to [Cisco Secure Endpoint's documentation](https://developer.cisco.com/docs/secure-endpoint/introduction/)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/cisco-secure-endpoint/)
 on n8n's website.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint#using-oauth2)

------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   The **Region** for your Cisco Secure Endpoint. Options are:
    
    *   Asia Pacific, Japan, and China
        
    *   Europe
        
    *   North America
        
    
*   A **Client ID**: Provided when you register a SecureX API Client
    
*   A **Client Secret**: Provided when you register a SecureX API Client
    

To get a Client ID and Client Secret, you'll need to Register a SecureX API Client. Refer to [Cisco Secure Endpoint's authentication documentation](https://developer.cisco.com/docs/secure-endpoint/authentication/#authentication)
 for detailed instructions. Use the SecureX **Client Password** as the **Client Secret** within the n8n credential.

[PreviousCisco Meraki credentials](https://docs.n8n.io/integrations/builtin/credentials/ciscomeraki)
[NextCisco Umbrella credentials](https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella)

Last updated 10 days ago

Was this helpful?
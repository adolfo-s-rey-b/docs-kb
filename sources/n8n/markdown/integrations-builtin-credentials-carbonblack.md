For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/carbonblack.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/carbonblack#prerequisites)

------------------------------------------------------------------------------------------------

*   Create a [Carbon Black subscription](https://www.broadcom.com/products/carbon-black/threat-prevention/carbon-black-cloud)
    .
    
*   Create a [Carbon Black developer account](https://developer.carbonblack.com/)
    .
    

Authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/carbonblack#authentication-methods)

------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/carbonblack#related-resources)

--------------------------------------------------------------------------------------------------------

Refer to [Carbon Black's documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/carbon-black/)
 on n8n's website.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/carbonblack#using-api-key)

------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **URL**: This URL is determined by the environment/product URL you use. You can find it by looking at the web address of your Carbon Black Cloud console. Refer to [Carbon Black's URL Parts documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#the-url-parts)
     for more information.
    
*   An **Access Token**: Refer to the [Carbon Black Create an API key documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#carbon-black-cloud-manages-identities-and-roles)
     to create an API key. Add the **API Secret Key** as the **Access Token** in n8n.
    

[PreviousCalendly credentials](https://docs.n8n.io/integrations/builtin/credentials/calendly)
[NextChargebee credentials](https://docs.n8n.io/integrations/builtin/credentials/chargebee)

Last updated 10 days ago

Was this helpful?
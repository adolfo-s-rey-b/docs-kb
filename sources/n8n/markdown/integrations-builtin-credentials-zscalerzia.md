For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia#prerequisites)

-----------------------------------------------------------------------------------------------

Create an admin account on a [Zscaler Internet Access (ZIA)](https://www.zscaler.com/products/zscaler-internet-access)
 cloud instance.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------------

*   Basic auth and API key combo
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia#related-resources)

-------------------------------------------------------------------------------------------------------

Refer to [Zscaler ZIA's documentation](https://help.zscaler.com/zia/getting-started-zia-api)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/zscaler-zia/)
 on n8n's website.

Using basic auth and API key combo[](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia#using-basic-auth-and-api-key-combo)

-----------------------------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Base URL**: Enter the base URL of your Zscaler ZIA cloud name. To get your base URL, log in to the ZIA Admin Portal and go to **Administration > Cloud Service API Security**. The base URL is displayed in both the **Cloud Service API Key** tab and the **OAuth 2.0 Authorization Servers** tab.
    
*   A **Username**: Enter your ZIA admin username.
    
*   A **Password**: Enter your ZIA admin password.
    
*   An **Api Key**: Get an API key by creating one from **Administration > Cloud Service API Security > Cloud Service API Key**.
    

Refer to [About Cloud Service API Key](https://help.zscaler.com/zia/about-cloud-service-api-key)
 for more detailed instructions.

[PreviousZoom credentials](https://docs.n8n.io/integrations/builtin/credentials/zoom)
[NextZulip credentials](https://docs.n8n.io/integrations/builtin/credentials/zulip)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/trellixepo.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/trellixepo#prerequisites)

-----------------------------------------------------------------------------------------------

Create a [Trellix ePolicy Orchestrator](https://www.trellix.com/products/epo/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/trellixepo#supported-authentication-methods)

-------------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/trellixepo#related-resources)

-------------------------------------------------------------------------------------------------------

Refer to [Trellix ePO's documentation](https://docs.trellix.com/docs/trellix-epolicy-orchestrator-on-prem-web-api-scripting-reference-guide)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/trellix-epo/)
 on n8n's website.

Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/trellixepo#using-basic-auth)

-----------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Username** to connect as.
    
*   A **Password** for that user account.
    

n8n uses these fields to build the `-u` parameter in the format of `-u username:pw`. Refer to [Web API basics](https://docs.trellix.com/docs/web-api-basics)
 for more information.

[PreviousTravis CI credentials](https://docs.n8n.io/integrations/builtin/credentials/travisci)
[NextTrello credentials](https://docs.n8n.io/integrations/builtin/credentials/trello)

Last updated 10 days ago

Was this helpful?
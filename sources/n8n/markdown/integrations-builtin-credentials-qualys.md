For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/qualys.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/qualys#prerequisites)

-------------------------------------------------------------------------------------------

Create a [Qualys](https://www.qualys.com/)
 user account with any user role except Contact.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/qualys#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/qualys#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Qualys's documentation](https://qualysguard.qg2.apps.qualys.com/qwebhelp/fo_portal/api_doc/index.htm)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/qualys/)
 on n8n's website.

Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/qualys#using-basic-auth)

-------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Username**
    
*   A **Password**
    
*   A **Requested With** string: Enter a user description, like a user agent, or keep the default `n8n application`. This sets the required `X-Requested-With` header.
    

[PreviousQdrant credentials](https://docs.n8n.io/integrations/builtin/credentials/qdrant)
[NextQuestDB credentials](https://docs.n8n.io/integrations/builtin/credentials/questdb)

Last updated 10 days ago

Was this helpful?
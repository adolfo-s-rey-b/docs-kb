For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/kibana.md)
.

You can use these credentials to authenticate when using the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to make a [Custom API call](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/kibana#prerequisites)

-------------------------------------------------------------------------------------------

*   Create an [Elasticsearch](https://www.elastic.co/)
     account.
    
*   If you're creating a new account to test with, load some sample data into Kibana. Refer to the [Kibana quick start](https://www.elastic.co/guide/en/kibana/current/get-started.html)
     for more information.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/kibana#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/kibana#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Kibana's API documentation](https://www.elastic.co/guide/en/kibana/current/api.html)
 for more information about the service.

This is a credential-only node. Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 to learn more. View [example workflows and related content](https://n8n.io/integrations/kibana/)
 on n8n's website.

Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/kibana#using-basic-auth)

-------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   The **URL** you use to access Kibana, for example `http://localhost:5601`
    
*   A **Username**: Use the same username that you use to log in to Elastic.
    
*   A **Password**: Use the same password that you use to log in to Elastic.
    

[PreviousKeap credentials](https://docs.n8n.io/integrations/builtin/credentials/keap)
[NextKitemaker credentials](https://docs.n8n.io/integrations/builtin/credentials/kitemaker)

Last updated 10 days ago

Was this helpful?
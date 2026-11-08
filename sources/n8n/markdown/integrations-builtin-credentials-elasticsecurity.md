For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity.md)
.

You can use these credentials to authenticate the following nodes:

*   [Elastic Security](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity#prerequisites)

----------------------------------------------------------------------------------------------------

*   Create an [Elastic Security](https://www.elastic.co/security)
     account.
    
*   [Deploy](https://www.elastic.co/guide/en/cloud/current/ec-create-deployment.html)
     an application.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    
*   API Key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity#related-resources)

------------------------------------------------------------------------------------------------------------

Refer to [Elastic Security's documentation](https://www.elastic.co/guide/en/security/current/es-overview.html)
 for more information about the service.

Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity#using-basic-auth)

----------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   A **Username**: For the user account you log into Elasticsearch with.
    
*   A **Password**: For the user account you log into Elasticsearch with.
    
*   Your Elasticsearch application's **Base URL** (also known as the Elasticsearch application endpoint):
    
    1.  In Elasticsearch, select the option to **Manage this deployment**.
        
    2.  In the **Applications** section, copy the endpoint of the **Elasticsearch** application.
        
    3.  Add this in n8n as the **Base URL**.
        
    

**Custom endpoint aliases**

If you add a [custom endpoint alias](https://www.elastic.co/guide/en/cloud/current/ec-regional-deployment-aliases.html)
 to a deployment, update your n8n credential **Base URL** with the new endpoint.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity#using-api-key)

----------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: For the user account you log into Elasticsearch with. Refer to Elasticsearch's [Create API key documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html)
     for more information.
    
*   Your Elasticsearch application's **Base URL** (also known as the Elasticsearch application endpoint):
    
    1.  In Elasticsearch, select the option to **Manage this deployment**.
        
    2.  In the **Applications** section, copy the endpoint of the **Elasticsearch** application.
        
    3.  Add this in n8n as the **Base URL**.
        
    

[PreviousElasticsearch credentials](https://docs.n8n.io/integrations/builtin/credentials/elasticsearch)
[NextEmelia credentials](https://docs.n8n.io/integrations/builtin/credentials/emelia)

Last updated 10 days ago

Was this helpful?
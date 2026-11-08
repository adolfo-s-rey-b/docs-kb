For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/thehive5.md)
.

You can use these credentials to authenticate the following nodes with TheHive 5.

*   [TheHive 5](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5)
    

**TheHive and TheHive 5**

n8n provides two nodes for TheHive. Use these credentials with TheHive 5 node. If you're using TheHive node for TheHive 3 or TheHive 4, use [TheHive credentials](https://docs.n8n.io/integrations/builtin/credentials/thehive)
.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/thehive5#prerequisites)

---------------------------------------------------------------------------------------------

Install [TheHive 5](https://docs.strangebee.com/thehive/download/)
 on your server.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/thehive5#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/thehive5#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [TheHive's API documentation](https://docs.strangebee.com/thehive/api-docs/)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/thehive5#using-api-key)

---------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: Users with `orgAdmin` and `superAdmin` accounts can generate API keys:
    
    *   `orgAdmin` account: Go to **Organization > Create API Key** for the user you wish to generate a key for.
        
    *   `superAdmin` account: Go to **Users > Create API Key** for the user you wish to generate a key for.
        
    *   Refer to [API Authentication](https://docs.strangebee.com/cortex/api/api-guide/?h=api+key#authentication)
         for more information.
        
    
*   A **URL**: The URL of your TheHive server.
    
*   **Ignore SSL Issues**: When turned on, n8n will connect even if SSL certificate validation fails.
    

[PreviousTheHive credentials](https://docs.n8n.io/integrations/builtin/credentials/thehive)
[NextTimescaleDB credentials](https://docs.n8n.io/integrations/builtin/credentials/timescaledb)

Last updated 10 days ago

Was this helpful?
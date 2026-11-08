For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/jotform.md)
.

You can use these credentials to authenticate the following nodes:

*   [Jotform Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/jotform#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/jotform#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Jotform's API documentation](https://api.jotform.com/docs/)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/jotform#using-api-key)

--------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Jotform](https://www.jotform.com/)
 account and:

*   An **API Key**
    
*   The **API Domain**
    

To set it up:

1.  Go to **Settings >** [**API**](https://www.jotform.com/myaccount/api)
    .
    
2.  Select **Create New Key**.
    
3.  Select the **Name** in Jotform to update the API key name to something meaningful, like `n8n integration`.
    
4.  Copy the **API Key** and enter it in your n8n credential.
    
5.  In n8n, select the **API Domain** that applies to you based on the forms you're using:
    
    *   **api.jotform.com**: Use this unless the other form types apply to you.
        
    *   **eu-api.jotform.com**: Select this if you're using Jotform [EU Safe Forms](https://www.jotform.com/eu-safe-forms/)
        .
        
    *   **hipaa-api.jotform.com**: Select this if you're using Jotform [HIPAA forms](https://www.jotform.com/hipaa/)
        .
        
    

Refer to the [Jotform API documentation](https://api.jotform.com/docs/)
 for more information on creating keys and API domains.

[PreviousJira credentials](https://docs.n8n.io/integrations/builtin/credentials/jira)
[NextJWT credentials](https://docs.n8n.io/integrations/builtin/credentials/jwt)

Last updated 10 days ago

Was this helpful?
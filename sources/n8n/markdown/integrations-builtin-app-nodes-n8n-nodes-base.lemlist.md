For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md)
.

Use the Lemlist node to automate work in Lemlist, and integrate Lemlist with other applications. n8n has built-in support for a wide range of Lemlist features, including getting activities, teams and campaigns, as well as creating, updating, and deleting leads.

On this page, you'll find a list of operations the Lemlist node supports and links to more resources.

**Credentials**

Refer to [Lemlist credentials](https://docs.n8n.io/integrations/builtin/credentials/lemlist)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist#operations)

---------------------------------------------------------------------------------------------------

*   Activity
    
    *   Get Many: Get many activities
        
    
*   Campaign
    
    *   Get Many: Get many campaigns
        
    *   Get Stats: Get campaign stats
        
    
*   Enrichment
    
    *   Get: Fetches a previously completed enrichment
        
    *   Enrich Lead: Enrich a lead using an email or LinkedIn URL
        
    *   Enrich Person: Enrich a person using an email or LinkedIn URL
        
    
*   Lead
    
    *   Create: Create a new lead
        
    *   Delete: Delete an existing lead
        
    *   Get: Get an existing lead
        
    *   Unsubscribe: Unsubscribe an existing lead
        
    
*   Team
    
    *   Get: Get an existing team
        
    *   Get Credits: Get an existing team's credits
        
    
*   Unsubscribe
    
    *   Add: Add an email to an unsubscribe list
        
    *   Delete: Delete an email from an unsubscribe list
        
    *   Get Many: Get many unsubscribed emails
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse Lemlist node documentation integration templates](https://n8n.io/integrations/lemlist)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousKoboToolbox](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox)
[NextLine](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line)

Last updated 10 days ago

Was this helpful?
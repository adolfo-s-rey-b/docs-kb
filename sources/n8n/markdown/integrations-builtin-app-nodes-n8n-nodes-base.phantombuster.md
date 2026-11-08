For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster.md)
.

Use the PhantomBuster node to automate work in PhantomBuster, and integrate PhantomBuster with other applications. n8n has built-in support for a wide range of PhantomBuster features, including adding, deleting, and getting agents.

On this page, you'll find a list of operations the PhantomBuster node supports and links to more resources.

**Credentials**

Refer to [PhantomBuster credentials](https://docs.n8n.io/integrations/builtin/credentials/phantombuster)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster#operations)

---------------------------------------------------------------------------------------------------------

*   Agent
    
    *   Delete an agent by ID.
        
    *   Get an agent by ID.
        
    *   Get all agents of the current user's organization.
        
    *   Get the output of the most recent container of an agent.
        
    *   Add an agent to the launch queue.
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------

[Browse PhantomBuster node documentation integration templates](https://n8n.io/integrations/phantombuster)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousPerplexity](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.perplexity)
[NextPhilips Hue](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.philipshue)

Last updated 10 days ago

Was this helpful?
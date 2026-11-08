For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp.md)
.

Use the MISP node to automate work in MISP, and integrate MISP with other applications. n8n has built-in support for a wide range of MISP features, including creating, updating, deleting and getting events, feeds, and organizations.

On this page, you'll find a list of operations the MISP node supports and links to more resources.

**Credentials**

Refer to [MISP credentials](https://docs.n8n.io/integrations/builtin/credentials/misp)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp#operations)

------------------------------------------------------------------------------------------------

*   Attribute
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Search
        
    *   Update
        
    
*   Event
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Publish
        
    *   Search
        
    *   Unpublish
        
    *   Update
        
    
*   Event Tag
    
    *   Add
        
    *   Remove
        
    
*   Feed
    
    *   Create
        
    *   Disable
        
    *   Enable
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Galaxy
    
    *   Delete
        
    *   Get
        
    *   Get All
        
    
*   Noticelist
    
    *   Get
        
    *   Get All
        
    
*   Object
    
    *   Search
        
    
*   Organisation
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Tag
    
    *   Create
        
    *   Delete
        
    *   Get All
        
    *   Update
        
    
*   User
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Warninglist
    
    *   Get
        
    *   Get All
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------

[Browse MISP node documentation integration templates](https://n8n.io/integrations/misp)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousMindee](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mindee)
[NextMistral AI](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai)

Last updated 10 days ago

Was this helpful?
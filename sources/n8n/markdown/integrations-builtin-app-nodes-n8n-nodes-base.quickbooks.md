For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks.md)
.

Use the QuickBooks node to automate work in QuickBooks, and integrate QuickBooks with other applications. n8n has built-in support for a wide range of QuickBooks features, including creating, updating, deleting, and getting bills, customers, employees, estimates, and invoices.

On this page, you'll find a list of operations the QuickBooks node supports and links to more resources.

**Credentials**

Refer to [QuickBooks credentials](https://docs.n8n.io/integrations/builtin/credentials/quickbooks)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks#operations)

------------------------------------------------------------------------------------------------------

*   Bill
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Customer
    
    *   Create
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Employee
    
    *   Create
        
    *   Get
        
    *   Get All
        
    *   Update
        
    
*   Estimate
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Send
        
    *   Update
        
    
*   Invoice
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Send
        
    *   Update
        
    *   Void
        
    
*   Item
    
    *   Get
        
    *   Get All
        
    
*   Payment
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get All
        
    *   Send
        
    *   Update
        
    *   Void
        
    
*   Purchase
    
    *   Get
        
    *   Get All
        
    
*   Transaction
    
    *   Get Report
        
    
*   Vendor
    
    *   Create
        
    *   Get
        
    *   Get All
        
    *   Update
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse QuickBooks Online node documentation integration templates](https://n8n.io/integrations/quickbooks-online)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousQuick Base](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbase)
[NextQuickChart](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickchart)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin.md)
.

PostBin is a service that helps you test API clients and webhooks. Use the PostBin node to automate work in PostBin, and integrate PostBin with other applications. n8n has built-in support for a wide range of PostBin features, including creating and deleting bins, and getting and sending requests.

On this page, you'll find a list of operations the PostBin node supports, and links to more resources.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin#operations)

---------------------------------------------------------------------------------------------------

*   Bin
    
    *   Create
        
    *   Get
        
    *   Delete
        
    
*   Request
    
    *   Get
        
    *   Remove First
        
    *   Send
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse PostBin node documentation integration templates](https://n8n.io/integrations/postbin)
 or [search all templates](https://n8n.io/workflows/)

Send requests[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin#send-requests)

---------------------------------------------------------------------------------------------------------

To send requests to a PostBin bin:

1.  Go to [PostBin](https://www.toptal.com/developers/postbin/)
     and follow the steps to generate a new bin. PostBin gives you a unique URL, including a bin ID.
    
2.  In the PostBin node, select the **Request** resource.
    
3.  Choose the type of **Operation** you want to perform.
    
4.  Enter your bin ID in **Bin ID**.
    

Create and manage bins[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin#create-and-manage-bins)

---------------------------------------------------------------------------------------------------------------------------

You can create and manage PostBin bins using the PostBin node.

1.  In **Resource**, select **Bin**.
    
2.  Choose an **Operation**. You can create, delete, or get a bin.
    

[PreviousPlivo](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.plivo)
[NextPostgres](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres)

Last updated 10 days ago

Was this helpful?
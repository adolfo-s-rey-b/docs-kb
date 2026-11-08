For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md)
.

Use the monday.com node to automate work in monday.com, and integrate monday.com with other applications. n8n has built-in support for a wide range of monday.com features, including creating a new board, and adding, deleting, and getting items on the board.

On this page, you'll find a list of operations the monday.com node supports and links to more resources.

**Feature availability**

The monday.com node is available from n8n 1.22.6.

**Credentials**

Refer to [monday.com credentials](https://docs.n8n.io/integrations/builtin/credentials/mondaycom)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom#operations)

-----------------------------------------------------------------------------------------------------

*   Board
    
    *   Archive a board
        
    *   Create a new board
        
    *   Get a board
        
    *   Get all boards
        
    
*   Board Column
    
    *   Create a new column
        
    *   Get all columns
        
    
*   Board Group
    
    *   Delete a group in a board
        
    *   Create a group in a board
        
    *   Get list of groups in a board
        
    
*   Board Item
    
    *   Add an update to an item.
        
    *   Change a column value for a board item
        
    *   Change multiple column values for a board item
        
    *   Create an item in a board's group
        
    *   Delete an item
        
    *   Get an item
        
    *   Get all items
        
    *   Get items by column value
        
    *   Move item to group
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------

[Browse monday.com node documentation integration templates](https://n8n.io/integrations/mondaycom)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousMocean](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mocean)
[NextMongoDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mongodb)

Last updated 10 days ago

Was this helpful?
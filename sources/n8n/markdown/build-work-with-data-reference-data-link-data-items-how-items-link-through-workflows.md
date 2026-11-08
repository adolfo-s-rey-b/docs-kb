For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md)
.

Each output item created by a node includes metadata that links them to the input item (or items) that the node used to generate them. This creates a chain of items that you can work back along to access previous items. This can be complicated to understand, especially if the node splits or merges data. You need to understand item linking when building your own programmatic nodes, or in some scenarios using the Code node.

This document provides a conceptual overview of this feature. For usage details, refer to:

*   [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    , for details on how to handle item linking when building a node.
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    , to learn how to handle item linking in the Code node.
    
*   [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    , to understand the errors you may encounter in the editor UI.
    

n8n's automatic item linking[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows#n8ns-automatic-item-linking)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

If a node doesn't control how to link input items to output items, n8n tries to guess how to link the items automatically:

*   Single input, single output: the output links to the input.
    
*   Single input, multiple outputs: all outputs link to that input.
    
*   Multiple inputs and outputs:
    
    *   If you keep the input items, but change the order (or remove some but keep others), n8n can automatically add the correct linked item information.
        
    *   If the number of inputs and outputs is equal, n8n links the items in order. This means that output-1 links to input-1, output-2 to input-2, and so on.
        
    *   If the number isn't equal, or you create completely new items, n8n can't automatically link items.
        
    

If n8n can't link items automatically, and the node doesn't handle the item linking, n8n displays an error. Refer to [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
 for more information.

Item linking example[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows#item-linking-example)

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-2d525e117f61517ea8851cf1270a9599ce561988%252Fitem-linking-multiple-lines.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=db1ba550dfb242c3b17945d1f3269332&sv=3)

A diagram showing the threads linking multiple items back through a workflow

In this example, it's possible for n8n to link an item in one node back several steps, despite the item order changing. This means the node that sorts movies alphabetically can access information about the linked item in the node that gets famous movie actors.

The methods for accessing linked items are different depending on whether you're using the UI, expressions, or the code node. Explore the following resources:

*   [Mapping in the UI](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    
*   [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------

*   [Link data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    
*   [Accessing linked items in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node)
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    
*   [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    
*   [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    

[PreviousLink data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
[NextAccessing linked items in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node)

Last updated 10 days ago

Was this helpful?
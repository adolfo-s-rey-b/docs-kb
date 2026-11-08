For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items.md)
.

An item is a single piece of data. Nodes receive one or more items, operate on them, and output new items. Each item links back to the items in the previous nodes that generated it.

Usually this just works. You need to understand this behavior in detail if you're:

*   Using the Code node for complex behaviors with input and output data.
    
*   Building a programmatic-style node.
    

This section provides:

*   A conceptual overview of [Item linking concepts](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
    .
    
*   Information on [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    .
    
*   Support for end users who need to [work with the data path](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
     to retrieve item data from previous nodes and link items when using the Code node.
    
*   Guidance on troubleshooting [errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    .
    

In this section[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items#in-this-section)

-----------------------------------------------------------------------------------------------------------

*   [How items link through workflows](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
    : a conceptual overview of item linking.
    
*   [Accessing linked items in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node)
    : use `itemMatching()` to retrieve linked item data.
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    : keep item links intact when you write custom code.
    
*   [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    : troubleshoot common item linking errors.
    
*   [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    : what node creators need to know about item linking.
    

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items#related-resources)

---------------------------------------------------------------------------------------------------------------

*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    
*   [Use the UI mapper](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)
    
*   [Reference previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
    

[PreviousReference previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
[NextHow items link through workflows](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)

Last updated 10 days ago

Was this helpful?
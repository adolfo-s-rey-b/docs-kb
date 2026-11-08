For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors.md)
.

In n8n you can reference data from any previous node. This doesn't have to be the node just before: it can be any previous node in the chain. When referencing nodes further back, you use the expression syntax `$(node_name).item`.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-2d525e117f61517ea8851cf1270a9599ce561988%252Fitem-linking-multiple-lines.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=db1ba550dfb242c3b17945d1f3269332&sv=3)

Diagram of threads for different items. Due to the item linking, you can get the actor for each movie using \`$('Get famous movie actors').item\`.

Since the previous node can have multiple items in it, n8n needs to know which one to use. When using `.item`, n8n figures this out for you behind the scenes. Refer to [Item linking concepts](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
 for detailed information on how this works.

`.item` fails if information is missing. To figure out which item to use, n8n maintains a thread back through the workflow's nodes for each item. For a given item, this thread tells n8n which items in previous nodes generated it. To find the matching item in a given previous node, n8n follows this thread back until it reaches the node in question.

When using `.item`, n8n displays an error when:

*   The thread is broken
    
*   The thread points to more than one item in the previous node (as it's unclear which one to use)
    
*   The node you reference is on a different branch from the current item
    

To solve these errors, you can either avoid using `.item`, or fix the root cause.

You can avoid `.item` by using `.first()`, `.last()` or `.all()[index]` instead. They require you to know the position of the item that you're targeting within the target node's output items. Refer to [Referencing previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
 for more detail on these methods.

The fix for the root cause depends on the exact error.

### Fix for 'Info for expressions missing from previous node'[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors#fix-for-info-for-expressions-missing-from-previous-node)

If you see this error message:

> ERROR: Info for expression missing from previous node

There's a node in the chain that doesn't return pairing information. The solution here depends on the type of the previous node:

*   Code nodes: make sure you return which input items the node used to produce each output item. Refer to [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
     for more information.
    
*   Custom or community nodes: the node creator needs to update the node to return which input items it uses to produce each output item. Refer to [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
     for more information.
    

### Fix for 'Multiple matching items for expression'[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors#fix-for-multiple-matching-items-for-expression)

This is the error message:

> ERROR: Multiple matching items for expression

Sometimes n8n uses multiple items to create a single item. Examples include the Summarize, Aggregate, and Merge nodes. These nodes can combine information from multiple items.

When you use `.item` and there are multiple possible matches, n8n doesn't know which one to use. To solve this you can either:

*   Use `.first()`, `.last()` or `.all()[index]` instead. Refer to [Referencing previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
     for more detail on these methods.
    
*   Reference a different node that contains the same information, but doesn't have multiple matching items.
    

### Fix for 'Node is on another branch'[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors#fix-for-node-is-on-another-branch)

This is the error message:

> `ERROR: '<node-name>' is on another branch`

The node you reference with `.item` is upstream of the current node, but the current item didn't come from it, so n8n can't match the current item to an item in that node. This happens when two branches come back together but their items stay separate.

For example, a **Merge** node in **Append** mode outputs the items from **Input 1** first, then the items from **Input 2**. Each output item still links back to only one input. If **Input 2** comes from a node called **Get orders**, then `{{ $('Get orders').item.json.total }}` resolves for items that came from **Input 2** and fails for items that came from **Input 1**.

The expression resolves to `null` and the node still succeeds, so the execution doesn't stop. n8n shows the error in the expression preview in the editor.

To solve this, you can either:

*   Use `.first()`, `.last()` or `.all()[index]` instead of `.item`. Refer to [Referencing previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
     for more detail on these methods.
    
*   If a **Merge** node brought the branches together, set it to **Combine** mode, so that each output item contains data from both branches.
    

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------

*   [Link data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    
*   [How items link through workflows](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
    
*   [Accessing linked items in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node)
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    
*   [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    

[PreviousPreserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
[NextItem linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)

Last updated 10 days ago

Was this helpful?
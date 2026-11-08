For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data.md)
.

Filtering in n8n can mean different things depending on what you want to accomplish. This guide covers both visual filtering in the UI and data filtering during workflow execution.

Filter data visually in the UI[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-data-visually-in-the-ui)

-----------------------------------------------------------------------------------------------------------------------------------

**Feature availability**

Filtering data in the node **INPUT** and **OUTPUT** panels is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** All editions
    

Search and filter data in the node **INPUT** and **OUTPUT** panels. Use this to check your node's data and find specific items.

To search:

1.  In a node, select **Search** ![Search icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-0c4a30a1cf6c3de522204819914621f894f09001%252Fsearch.png%3Falt%3Dmedia&width=40&dpr=3&quality=100&sign=ed1d89ec7b9dc5ce0d738a6458b92602&sv=3) in the **INPUT** or **OUTPUT** panel.
    
2.  Enter your search term.
    

n8n filters as you type, displaying the objects or rows containing the term.

Filtering is purely visual: n8n doesn't change or delete data. The filter resets when you close and reopen the node.

Filter data during workflow execution[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-data-during-workflow-execution)

-------------------------------------------------------------------------------------------------------------------------------------------------

To actually remove or filter data in your workflow, use these approaches:

### Filter out items[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-out-items)

To remove entire items from your workflow based on conditions, use the [Filter node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter)
. This node evaluates conditions and only passes through items that meet your criteria.

### Filter out fields[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-out-fields)

To remove specific fields from an item or object while keeping the item itself, use the [Edit Fields (Set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
. Configure it to remove the fields you don't need.

### Filter array elements[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-array-elements)

To filter elements within an array inside an item, use the `.filter()` method in an expression or Code node. For example:

Copy

    {{ $json.myArray.filter(item => item.value > 10) }}

This removes array elements that don't match your condition while preserving the item structure.

### Filter out duplicate items from previous executions[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#filter-out-duplicate-items-from-previous-executions)

To remove items that have been seen in previous executions of a workflow, use the [Remove Duplicates](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates)
 node. Use this when an event fires multiple times but you only want to process the first occurrence.

Related resources[](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data#related-resources)

---------------------------------------------------------------------------------------------------------

*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Understand n8n's data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    
*   [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    
*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    
*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Pin and mock data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
    
*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
    

[PreviousWorkflowdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata)
[NextPin and mock data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)

Last updated 10 days ago

Was this helpful?
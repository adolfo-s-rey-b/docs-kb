For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data.md)
.

In n8n, data flows through your workflow from node to node. Each node receives data, processes it, and passes the results to the next node. Understanding how data moves and transforms in your workflows is essential for building effective workflows.

How data works in n8n[](https://docs.n8n.io/build/work-with-data#how-data-works-in-n8n)

----------------------------------------------------------------------------------------

**Data flows through nodes**: When you connect nodes, data automatically passes from one to the next. Each node processes the incoming data and outputs results based on its configuration.

**View data at every stage**: You can inspect data at any point in your workflow:

*   **Node details view**: Double-click any node to see its input and output data. Choose between **Schema**, **Table** and **JSON** views. Schema view shows a simplified structure from the first item only, Table and JSON display the full dataset.
    
*   **Execution logs**: Review past workflow runs to see the data that passed through each node.
    

**Reference previous data**: Use [data mapping](https://docs.n8n.io/build/work-with-data/reference-data)
 to reference data from earlier nodes in your workflow. You can:

*   Select values from previous nodes using the UI
    
*   Write [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
     to dynamically access and combine data
    
*   Reference specific nodes by name to get their output
    

**Transform data**: n8n provides multiple ways to modify data:

*   Use dedicated transformation nodes (Aggregate, Split Out, Sort, and more)
    
*   Write [expressions](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)
     directly in node parameters
    
*   Use the [Code node](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#code-node)
     for custom JavaScript or Python logic
    
*   Apply the [AI Transform node](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#ai-transform-node)
     for AI-assisted transformations
    

**Understand the data structure**: n8n uses a [consistent data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
 across all nodes, making it predictable how data flows and transforms throughout your workflows.

In this section[](https://docs.n8n.io/build/work-with-data#in-this-section)

----------------------------------------------------------------------------

*   [Understand n8n's data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    : how n8n structures and passes data between nodes.
    
*   [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    : compare expressions, the Code node, the AI Transform node, and data transformation nodes.
    
*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    : reference data from earlier nodes in your workflow.
    
*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    : modify, restructure, or enrich data as it moves through your workflow.
    
*   [Filter out unwanted data](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data)
    : filter data visually in the UI or during workflow execution.
    
*   [Pin and mock data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
    : pin and mock data in your workflow during development.
    
*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    : work with binary files, dates and times, and nested JSON.
    
*   [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
    : store and manage structured tabular data within project boundaries.
    

Related resources[](https://docs.n8n.io/build/work-with-data#related-resources)

--------------------------------------------------------------------------------

*   [Build](https://docs.n8n.io/build)
    
*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Build and manage agents](https://docs.n8n.io/build/build-and-manage-agents)
    
*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Code in n8n](https://docs.n8n.io/build/code-in-n8n)
    
*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [Keyboard shortcuts](https://docs.n8n.io/build/keyboard-shortcuts)
    

[PreviousUnderstand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
[NextUnderstand n8n's data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)

Last updated 10 days ago

Was this helpful?
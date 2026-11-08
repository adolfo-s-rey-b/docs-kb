For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data.md)
.

Data transformation in n8n involves modifying, restructuring, or enriching data as it moves through your workflow. This includes changing data formats, filtering or aggregating values, adding computed fields, and converting data structures to work with different nodes.

n8n uses a predefined [data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
 that allows all nodes to process incoming data correctly. When your data doesn't match this structure, or when you need to modify it for your use case, you'll need to transform it.

n8n provides several approaches for data transformation:

*   [Expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#expressions)
     allow you to transform data directly in node parameters using n8n's expression syntax (`{{ }}`)
    
*   The [Code node](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#code-node)
     lets you write custom JavaScript or Python for complex transformations.
    
*   The [AI Transform node](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#ai-transform-node)
     generates transformation code from natural language prompts.
    
*   Advanced transformation techniques: For sophisticated data manipulation, n8n supports:
    
    *   **Ternary operators**: Conditional logic directly in expressions (`condition ? valueIfTrue : valueIfFalse`)
        
    *   **Chained functions**: Combine multiple transformation functions
        
    *   **Complex expressions**: Use JavaScript methods and operators within expression syntax
        
    
*   Specialized transformation nodes for common structural transformations:
    
    *   [Aggregate](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate)
        : group separate items together
        
    *   [Limit](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit)
        : restrict the number of items
        
    *   [Remove Duplicates](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates)
        : eliminate identical items
        
    *   [Sort](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort)
        : order items or randomize
        
    *   [Split Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout)
        : separate lists into individual items
        
    *   [Summarize](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize)
        : aggregate data like Excel pivot tables
        
    

For a comparison of these approaches, see [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
.

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Expressions for data transformation](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)
    
*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousTransform data](https://docs.n8n.io/build/work-with-data/transform-data)
[NextExpressions for data transformation](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)

Last updated 10 days ago

Was this helpful?
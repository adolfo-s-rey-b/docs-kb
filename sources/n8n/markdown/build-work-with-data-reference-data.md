For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data.md)
.

Referencing data, or data mapping, means accessing information from previous nodes in your workflow. This allows you to use output from earlier steps as input for later nodes, creating dynamic workflows that pass data through multiple operations.

When you reference data, you're not changing it. You're pointing to values that already exist so you can use them in node parameters, expressions, or custom code.

If you want to change the data you're referencing, see [Transforming data](https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data)
.

How to reference data[](https://docs.n8n.io/build/work-with-data/reference-data#how-to-reference-data)

-------------------------------------------------------------------------------------------------------

The main way to reference data is using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#expressions)
. You can create expressions by typing them in a parameter's field or dragging and dropping fields from the Input panel in the UI. Expressions will automatically figure out the correct item to use using [item linking](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
.

In this section[](https://docs.n8n.io/build/work-with-data/reference-data#in-this-section)

-------------------------------------------------------------------------------------------

*   [Use the UI mapper](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)
    : reference data by dragging and dropping fields in the editor.
    
*   [Reference previous nodes](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes)
    : methods for working with the input of the current node and the output of previous nodes.
    
*   [Link data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    : how items link back to the items that generated them.
    

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data#related-resources)

-----------------------------------------------------------------------------------------------

*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Understand n8n's data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    
*   [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    
*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Filter out unwanted data](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data)
    
*   [Pin and mock data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
    
*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
    

[PreviousExpressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
[NextUse the UI mapper](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper)

Last updated 10 days ago

Was this helpful?
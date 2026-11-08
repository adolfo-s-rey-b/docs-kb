For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md)
.

Use the Item List Output Parser node to return a list of items with a specific length and separator.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

*   **Number of Items**: Enter the maximum items to return. Set to `-1` for unlimited items.
    
*   **Separator**: Select the separator used to split the results into separate items. Defaults to a new line.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Item List Output Parser node documentation integration templates](https://n8n.io/integrations/item-list-output-parser)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's structured output documentation](https://docs.langchain.com/oss/javascript/langchain/structured-output)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousAuto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)
[NextStructured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)

Last updated 10 days ago

Was this helpful?
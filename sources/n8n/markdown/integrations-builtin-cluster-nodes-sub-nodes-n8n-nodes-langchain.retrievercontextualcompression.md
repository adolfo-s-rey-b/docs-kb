For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md)
.

The Contextual Compression Retriever node improves the answers returned from vector store document similarity searches by taking into account the context from the query.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Contextual Compression Retriever node documentation integration templates](https://n8n.io/integrations/contextual-compression-retriever)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues)
[NextMultiQuery Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery)

Last updated 10 days ago

Was this helpful?
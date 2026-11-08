For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md)
.

Use the Vector Store Retriever node to retrieve documents from a vector store.

On this page, you'll find the node parameters for the Vector Store Retriever node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

*   **Limit**: Enter the maximum number of results to return.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Vector Store Retriever node documentation integration templates](https://n8n.io/integrations/vector-store-retriever)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's semantic search tutorial](https://docs.langchain.com/oss/javascript/langchain/knowledge-base)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMultiQuery Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery)
[NextWorkflow Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow)

Last updated 10 days ago

Was this helpful?
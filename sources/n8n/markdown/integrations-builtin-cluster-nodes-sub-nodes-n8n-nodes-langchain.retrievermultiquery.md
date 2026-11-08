For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md)
.

The MultiQuery Retriever node automates the process of prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query.

On this page, you'll find the node parameters for the MultiQuery Retriever node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery#node-options)

--------------------------------------------------------------------------------------------------------------------------------------

*   **Query Count**: Enter how many different versions of the query to generate.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse MultiQuery Retriever node documentation integration templates](https://n8n.io/integrations/multiquery-retriever)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's retriever documentation](https://docs.langchain.com/oss/javascript/integrations/retrievers)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousContextual Compression Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression)
[NextVector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)

Last updated 10 days ago

Was this helpful?
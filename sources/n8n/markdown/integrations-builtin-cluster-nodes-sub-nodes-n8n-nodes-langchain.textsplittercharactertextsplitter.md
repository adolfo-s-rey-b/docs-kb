For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md)
.

Use the Character Text Splitter node to split document data based on characters.

On this page, you'll find the node parameters for the Character Text Splitter node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Separator**: Select the separator used to split the document into separate items.
    
*   **Chunk Size**: Enter the number of characters in each chunk.
    
*   **Chunk Overlap**: Enter how much overlap to have between chunks.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Character Text Splitter node documentation integration templates](https://n8n.io/integrations/character-text-splitter)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's text splitter documentation](https://docs.langchain.com/oss/javascript/integrations/splitters)
 and [LangChain's API documentation for character text splitting](https://reference.langchain.com/javascript/langchain-textsplitters/CharacterTextSplitter)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousWorkflow Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow)
[NextRecursive Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter)

Last updated 10 days ago

Was this helpful?
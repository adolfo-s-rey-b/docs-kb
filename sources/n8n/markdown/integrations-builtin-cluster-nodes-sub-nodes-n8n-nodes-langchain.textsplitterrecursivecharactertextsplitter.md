For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)
.

The Recursive Character Text Splitter node splits document data recursively to keep all paragraphs, sentences then words together as long as possible.

On this page, you'll find the node parameters for the Recursive Character Text Splitter node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Chunk Size**: Enter the number of characters in each chunk.
    
*   **Chunk Overlap**: Enter how much overlap to have between chunks.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Recursive Character Text Splitter node documentation integration templates](https://n8n.io/integrations/recursive-character-text-splitter)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's text splitter documentation](https://docs.langchain.com/oss/javascript/integrations/splitters)
 and [LangChain's recursively split by character documentation](https://reference.langchain.com/javascript/langchain-textsplitters/RecursiveCharacterTextSplitter)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousCharacter Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter)
[NextToken Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter)

Last updated 10 days ago

Was this helpful?
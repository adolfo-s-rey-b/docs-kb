For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)
.

**Feature availability**

The GitHub Document Loader node is deprecated from n8n 1.122.0. Refer to [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for more information.

Use the GitHub Document Loader node to load data from a GitHub repository for vector stores or summarization.

On this page, you'll find the node parameters for the GitHub Document Loader node, and links to more resources.

**Credentials**

Refer to the [GitHub credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/github)
 for authentication information for this node. This node doesn't support OAuth for authentication.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

*   **Text Splitting**: Choose from:
    
    *   **Simple**: Uses the [Recursive Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter)
         with a chunk size of 1000 and an overlap of 200.
        
    *   **Custom**: Allows you to connect a text splitter of your choice.
        
    
*   **Repository Link**: Enter the URL of your GitHub repository.
    
*   **Branch**: Enter the branch name to use.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

*   **Recursive**: Select whether to include sub-folders and files (turned on) or not (turned off).
    
*   **Ignore Paths**: Enter directories to ignore.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse GitHub Document Loader node documentation integration templates](https://n8n.io/integrations/github-document-loader)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's documentation on document loaders](https://docs.langchain.com/oss/javascript/integrations/document_loaders/file_loaders)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousDefault Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
[NextEmbeddings AWS Bedrock](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock)

Last updated 10 days ago

Was this helpful?
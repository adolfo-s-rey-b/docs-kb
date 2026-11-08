For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)
.

Use the Embeddings Cohere node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings Cohere node, and links to more resources.

**Credentials**

Refer to the [Cohere credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/cohere)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the embedding. Choose from:
    
    *   **Embed-English-v2.0(4096 Dimensions)**
        
    *   **Embed-English-Light-v2.0(1024 Dimensions)**
        
    *   **Embed-Multilingual-v2.0(768 Dimensions)**
        
    

Learn more about available models in [Cohere's models documentation](https://docs.cohere.com/docs/models)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Cohere node documentation integration templates](https://n8n.io/integrations/embeddings-cohere)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Cohere embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/cohere)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMicrosoft Foundry Embeddings](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai)
[NextEmbeddings Databricks](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks)

Last updated 10 days ago

Was this helpful?
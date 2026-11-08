For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)
.

Use the Embeddings OpenAI node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings OpenAI node, and links to more resources.

**Credentials**

Refer to the [OpenAI credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/openai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai#node-options)

-----------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use for generating embeddings.
    
*   **Base URL**: Enter the URL to send the request to. Use this if you are using a self-hosted OpenAI-like model.
    
*   **Batch Size**: Enter the maximum number of documents to send in each request.
    
*   **Strip New Lines**: Select whether to remove new line characters from input text (turned on) or not (turned off). n8n enables this by default.
    
*   **Timeout**: Enter the maximum amount of time a request can take in seconds. Set to `-1` for no timeout.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings OpenAI node documentation integration templates](https://n8n.io/integrations/embeddings-openai)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's OpenAI embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/openai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama)
[NextEmbeddings Oracle Database](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb)

Last updated 10 days ago

Was this helpful?
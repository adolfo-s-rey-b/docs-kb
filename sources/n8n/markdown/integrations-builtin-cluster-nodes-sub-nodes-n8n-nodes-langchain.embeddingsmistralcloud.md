For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)
.

Use the Embeddings Mistral Cloud node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings Mistral Cloud node, and links to more resources.

**Credentials**

Refer to the [Mistral Cloud credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/mistral)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the embedding.
    

Learn more about available models in [Mistral's models documentation](https://docs.mistral.ai/models/)
.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud#node-options)

-----------------------------------------------------------------------------------------------------------------------------------------

*   **Batch Size**: Enter the maximum number of documents to send in each request.
    
*   **Strip New Lines**: Select whether to remove new line characters from input text (turned on) or not (turned off). n8n enables this by default.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Mistral Cloud node documentation integration templates](https://n8n.io/integrations/embeddings-mistral-cloud)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Mistral embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/mistralai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Lemonade](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade)
[NextEmbeddings Ollama](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama)

Last updated 10 days ago

Was this helpful?
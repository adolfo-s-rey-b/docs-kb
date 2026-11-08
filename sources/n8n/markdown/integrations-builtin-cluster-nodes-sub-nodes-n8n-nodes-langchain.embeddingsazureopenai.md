For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md)
.

Use the Microsoft Foundry Embeddings node to generate embeddings for a given text.

This node was previously called the **Embeddings Azure OpenAI** node.

On this page, you'll find the node parameters for the Microsoft Foundry Embeddings node, and links to more resources.

**Credentials**

Refer to the [Microsoft Foundry credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/azureopenai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------------------

*   **Authentication**: Choose how the node signs in to Azure. Each option uses its own credential.
    
    *   **API Key**: Use a stored API key. This is the default. Refer to [Using API key](https://docs.n8n.io/integrations/builtin/credentials/azureopenai#using-api-key)
        .
        
    *   **Azure Entra ID (OAuth2)**: Sign in as your Entra application with a client ID and secret. Use this when your organization doesn't allow stored API keys. No API key is stored in n8n. Refer to [Using Microsoft Foundry (Entra ID)](https://docs.n8n.io/integrations/builtin/credentials/azureopenai#using-azure-entra-id-oauth2)
        .
        
    

Both options work with the **Classic** and the **Microsoft Foundry** endpoint types.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai#node-options)

----------------------------------------------------------------------------------------------------------------------------------------

*   **Model (Deployment) Name**: Select the model (deployment) to use for generating embeddings.
    
*   **Batch Size**: Enter the maximum number of documents to send in each request.
    
*   **Strip New Lines**: Select whether to remove new line characters from input text (turned on) or not (turned off). n8n enables this by default.
    
*   **Timeout**: Enter the maximum amount of time a request can take in seconds. Set to `-1` for no timeout.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Microsoft Foundry Embeddings node documentation integration templates](https://n8n.io/integrations/embeddings-azure-openai)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Azure OpenAI embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/azure_openai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings AWS Bedrock](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock)
[NextEmbeddings Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere)

Last updated 10 days ago

Was this helpful?
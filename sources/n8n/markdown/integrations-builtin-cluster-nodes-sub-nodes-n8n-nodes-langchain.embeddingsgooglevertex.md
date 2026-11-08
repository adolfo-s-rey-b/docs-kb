For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md)
.

Use the Embeddings Google Vertex node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings Google Vertex node, and links to more resources.

**Credentials**

Use [Google Vertex AI credentials](https://docs.n8n.io/integrations/builtin/credentials/googlevertexai)
 to store the project and region with your service account details. This node also supports [Google Service Account credentials](https://docs.n8n.io/integrations/builtin/credentials/google/service-account)
.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------

*   **Authentication**: Select **Google Service Account** (the default) or **Google Vertex AI**.
    
*   **Project ID**: For **Google Service Account** authentication, n8n loads the project list using the service account's access. Select a listed project, or enter the project ID manually. For **Google Vertex AI** authentication, configure the project in the credential.
    
*   **Model Name**: Enter the model name to use to generate the embedding.
    
*   **Region**: Select **Default (Use Credential Region)** to use the region set in the credential. To override it, select **Global**, **EU (Multi-Region)**, or **US (Multi-Region)**.
    

Learn more about available embedding models in [Google VertexAI embeddings API documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Google Vertex node documentation integration templates](https://n8n.io/integrations/embeddings-google-vertex)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Google Vertex AI embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/google_vertex_ai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Google PaLM](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm)
[NextEmbeddings HuggingFace Inference](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference)

Last updated 10 days ago

Was this helpful?
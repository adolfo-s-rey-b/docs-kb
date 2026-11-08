For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md)
.

Use the Embeddings Google Gemini node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings Google Gemini node, and links to more resources.

**Credentials**

Refer to the [Google Gemini(PaLM) credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/googleai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the embedding.
    

Learn more about available models in [Google Gemini's models documentation](https://ai.google.dev/models/gemini)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Google Gemini node documentation integration templates](https://n8n.io/integrations/embeddings-google-gemini)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Google Generative AI embeddings documentation](https://docs.langchain.com/oss/javascript/integrations/embeddings/google_generative_ai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Databricks](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks)
[NextEmbeddings Google PaLM](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm)

Last updated 10 days ago

Was this helpful?
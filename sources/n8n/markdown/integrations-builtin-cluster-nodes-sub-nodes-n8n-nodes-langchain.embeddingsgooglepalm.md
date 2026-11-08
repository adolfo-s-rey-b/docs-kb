For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md)
.

Use the Embeddings Google PaLM node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings Google PaLM node, and links to more resources.

**Credentials**

Refer to the [Google Gemini(PaLM) credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/googleai)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the embedding.
    

n8n dynamically loads models from the Google PaLM API and you'll only see the models available to your account.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Google PaLM node documentation integration templates](https://n8n.io/integrations/embeddings-google-palm)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Google Gemini](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini)
[NextEmbeddings Google Vertex](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md)
.

Use the Embeddings HuggingFace Inference node to generate embeddings for a given text.

On this page, you'll find the node parameters for the Embeddings HuggingFace Inference, and links to more resources.

**Credentials**

Refer to the [Hugging Face credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/huggingface)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the model to use to generate the embedding.
    

Refer to the [Hugging Face models documentation](https://huggingface.co/models?other=embeddings)
 for available models.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference#node-options)

-------------------------------------------------------------------------------------------------------------------------------------------------

*   **Custom Inference Endpoint**: Enter the URL of your deployed model, hosted by HuggingFace. If you set this, n8n ignores the **Model Name**.
    

Refer to [HuggingFace's guide to inference](https://huggingface.co/inference-endpoints)
 for more information.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings HuggingFace Inference node documentation integration templates](https://n8n.io/integrations/embeddings-hugging-face-inference)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings Google Vertex](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex)
[NextEmbeddings Lemonade](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade)

Last updated 10 days ago

Was this helpful?
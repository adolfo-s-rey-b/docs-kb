For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md)
.

Use the Embeddings Lemonade node to generate vector embeddings using models hosted and managed by a Lemonade server. This node is useful for workflows that perform semantic search, clustering, similarity matching, or any task that requires numerical vector representations of text.

On this page, you'll find a list of operations the Embeddings Lemonade node supports, and links to more resources.

**Credentials**

Refer to the [Lemonade credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/lemonade)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

Configure the node with the following parameters.

### Model[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade#model)

The model which will generate the embeddings. Models are loaded and managed through the Lemonade server configured for this node. Select the desired model from the list of available options served by your Lemonade instance.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Lemonade node documentation integration templates](https://n8n.io/integrations/embeddings-lemonade)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Lemonade Server's documentation](https://lemonade-server.ai/docs/)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings HuggingFace Inference](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference)
[NextEmbeddings Mistral Cloud](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud)

Last updated 10 days ago

Was this helpful?
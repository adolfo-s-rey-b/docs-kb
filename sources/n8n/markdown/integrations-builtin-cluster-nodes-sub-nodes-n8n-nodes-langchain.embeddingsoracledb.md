For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md)
.

Use the Embeddings Oracle Database node to generate embeddings with ONNX models stored in Oracle Database. This node is useful for workflows that perform semantic search, similarity matching, retrieval-augmented generation, or other tasks that require vector representations of text.

On this page, you'll find the node parameters for the Embeddings Oracle Database node, and links to more resources.

**Credentials**

Refer to the [Oracle Database credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
 for authentication information for this node.

**ONNX models**

Your Oracle Database instance must support Oracle AI Vector Search and ONNX model execution capabilities.

Import one or more ONNX embedding models into Oracle Database before using this node. Only imported models are available for selection.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: Select the ONNX model used to generate embeddings. Choose a model from the list of models available in your Oracle Database instance or specify a model ID manually. The selected model determines the embedding dimensions and supported input types.
    

The node loads available models from the `USER_MINING_MODELS` view in the configured Oracle Database connection. Only models accessible to the current database user are displayed.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Embeddings Oracle Database node documentation integration templates](https://n8n.io/integrations/embeddings-oracle-database)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Oracle's ONNX model import documentation](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/import-onnx-models-oracle-ai-database-end-end-example.html)
 for more information about importing ONNX models into Oracle Database.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousEmbeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai)
[NextQwen Cloud Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)
.

Use the Embeddings Databricks node to generate embeddings for text with an embeddings model served by your Databricks workspace. The node queries [Unity AI Gateway model services](https://docs.databricks.com/aws/en/ai-gateway/model-services)
, the same gateway the [Databricks Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks)
 node uses. Its main job is to pair with the [Databricks Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks)
 node, which needs an embeddings connection in every operation mode.

On this page, you'll find the prerequisites, setup steps, pairing rules, node parameters, and known issues for the Embeddings Databricks node.

**Credentials**

Refer to [Databricks credentials](https://docs.n8n.io/integrations/builtin/credentials/databricks)
 for guidance on setting up authentication. The node accepts the **Databricks OAuth2 API** credential only, with a service principal or user login. It doesn't accept a personal access token.

**Preview status**

The Embeddings Databricks node is in Preview from n8n 2.45.0 and may change in future releases. Avoid relying on it in production workflows.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Prerequisites[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#prerequisites)

-----------------------------------------------------------------------------------------------------------------------------------------

*   A Databricks workspace with Unity AI Gateway enabled.
    
*   A [Databricks OAuth2 credential](https://docs.n8n.io/integrations/builtin/credentials/databricks#supported-authentication-methods)
     in n8n, using either a service principal or user login.
    
*   The identity the credential authenticates as needs **USE CATALOG** and **USE SCHEMA** on the catalog and schema that hold the model service, and **EXECUTE** on the model service. Databricks grants **EXECUTE** on the `system.ai` model services to all workspace users by default. Refer to [Required Databricks privileges](https://docs.n8n.io/integrations/builtin/credentials/databricks#required-databricks-privileges)
    .
    

Set up the node[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#set-up-the-node)

---------------------------------------------------------------------------------------------------------------------------------------------

1.  Add a [Databricks Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks)
     node, or another node that takes an embeddings sub-node, to your workflow.
    
2.  Select the **+** on the node's **Embedding** connector, then select **Embeddings Databricks**.
    
3.  Under **Credential to connect with**, select an existing Databricks OAuth2 credential or create a new one.
    
4.  In **Model**, open the list and pick a model service. n8n loads the model services the credential can access that support embeddings, and leaves out chat models. Type to filter the list. To use a service that isn't listed, switch to **ID** and enter its full name, for example `system.ai.gte-large-en`.
    

Pair the node with a Databricks index[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#pair-the-node-with-a-databricks-index)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Which model you pick depends on the index the Databricks Vector Store node works with:

*   **Managed index** (a Delta Sync index with a Databricks embedding model): Databricks embeds the queries itself with the index's own model. The Embeddings Databricks node must be connected, but it's never called, so any model service works.
    
*   **Self-managed index** (a Direct Access index, or a Delta Sync index with its own vector column): the Embeddings Databricks node embeds every search query, and on a Direct Access index every inserted document. Pick the model and dimension the index was built with. An index built with `databricks-gte-large-en`, which has 1024 dimensions, needs the `system.ai.gte-large-en` model service. A different model fails with `query vector dimension <n> does not match index vector dimension <m>` on a search, and with `Databricks rejected the upsert into <index>. Failed primary keys: ...` on an insert.
    

Refer to [Index types and embeddings](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks#index-types-and-embeddings)
 on the Databricks Vector Store page for how the vector store node decides which query form to send.

The node is a standard embeddings sub-node, so it also works with the other vector store nodes in n8n, such as the [Simple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)
.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

*   **Model**: The Unity AI Gateway model service that generates the embeddings, named `catalog.schema.service`.
    
    *   **From List**: Choose from the model services the credential can access that support embeddings.
        
    *   **ID**: Enter the full name of a model service directly. Use this for a service that supports embeddings but isn't advertised as embeddings-capable.
        
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

*   **Batch Size**: The maximum number of documents to send in one request. Default `512`, maximum `2048`. Refer to [Rate limits](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#rate-limits)
     before lowering it.
    
*   **Strip New Lines**: Whether to remove new line characters from the input text before embedding it. Turned on by default.
    
*   **Timeout**: The maximum time a request may take, in milliseconds. Default `360000` (six minutes). A request that runs out of time fails with `Request timed out.`
    
*   **Max Retries**: How many times to retry a failed request. Default `2`.
    

Rate limits[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#rate-limits)

-------------------------------------------------------------------------------------------------------------------------------------

Pay-per-token model services are rate limited per workspace. When the Databricks Vector Store node inserts documents, it embeds them in chunks of its **Embedding Batch Size** (`200` by default), and each chunk is split into requests of this node's **Batch Size** that go out in parallel. A small **Batch Size** turns one chunk into many simultaneous requests, which can exceed the workspace limit of the model service. The node retries a rejected request with backoff up to **Max Retries**, then the insert fails with `Databricks rate limit reached for <service>: REQUEST_LIMIT_EXCEEDED: Exceeded workspace QPS rate limit`. The node doesn't write the chunk that hit the limit, but chunks it embedded and wrote before it stay in the index, so check the index before you retry.

To avoid it, keep **Batch Size** at its default so a chunk goes out in one request, keep concurrent inserts low, or use a [provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
 endpoint for the model.

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

*   [Databricks Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks)
    
*   [Databricks AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.databricksaiagent)
    
*   [Databricks Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks)
    
*   [Databricks credentials](https://docs.n8n.io/integrations/builtin/credentials/databricks)
    
*   [Unity AI Gateway model services](https://docs.databricks.com/aws/en/ai-gateway/model-services)
     in the Databricks documentation
    
*   Migrating from the community package: refer to [Migrate from the n8n-nodes-databricks community package](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks/migrate-from-the-community-package)
    

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#common-issues)

-----------------------------------------------------------------------------------------------------------------------------------------

### No model services found[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#no-model-services-found)

The model list is empty and the node reports `No model services found`. Unity AI Gateway isn't enabled on the workspace, or the credential's identity can't access any model service. Check the workspace settings, then grant **USE CATALOG**, **USE SCHEMA**, and **EXECUTE** on at least one model service.

### No embeddings-capable model services found[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#no-embeddings-capable-model-services-found)

The credential can see model services, but none advertises embeddings. Switch **Model** to **ID** and enter the service name directly. Chat-only services don't work in this node.

### Model service not found[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#model-service-not-found)

The node fails with `The resource you are requesting could not be found`, and the error description names the missing service. The **Model** name doesn't exist in the workspace. Check the three-part name, or pick the service **From List**.

### Query vector dimension doesn't match the index[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#query-vector-dimension-doesnt-match-the-index)

The model doesn't match the index the Databricks Vector Store node searches. Refer to [Pair the node with a Databricks index](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#pair-the-node-with-a-databricks-index)
.

### Rate limit reached[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#rate-limit-reached)

The execution fails with `Databricks rate limit reached for <service>` and a 429 status. Refer to [Rate limits](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#rate-limits)
.

### Host must use HTTPS[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#host-must-use-https)

The node fails with `Databricks host must use https` because the credential's **Host** isn't an `https://` URL, for example because it starts with `http://` or has no scheme. Every request carries a token, so the node refuses plain HTTP. Enter the full workspace URL with `https://`.

### Connection error[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks#connection-error)

The node reports `Connection error.` without a Databricks message. The credential's **Host** doesn't point at a Databricks workspace, or the workspace isn't reachable from your n8n instance. Check the host URL and the network path.

[PreviousEmbeddings Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere)
[NextEmbeddings Google Gemini](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md)
.

Azure AI Search (formerly Azure Cognitive Search) is a cloud search service with vector search capabilities for RAG and semantic search applications. Use this node to store, retrieve, and query vector embeddings alongside their content and metadata.

On this page, you'll find the node parameters for the Azure AI Search Vector Store node, and links to more resources.

**Credentials**

Refer to the [Azure AI Search credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/azureaisearch)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Prerequisites[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#prerequisites)

----------------------------------------------------------------------------------------------------------------------------------------------

Before using this node, you need:

1.  An [Azure subscription](https://azure.microsoft.com/)
    
2.  An [Azure AI Search service](https://learn.microsoft.com/azure/search/search-create-service-portal)
    
3.  API key authentication configured (admin key for write operations, query key for read-only)
    
    See [credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/azureaisearch)
     for setup instructions.
    

### Index configuration[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#index-configuration)

The node automatically creates indexes if they don't exist. When auto-creating, the node configures:

*   Vector fields with appropriate dimensions based on your embeddings model
    
*   HNSW algorithm for efficient similarity search with cosine metric
    
*   Content and metadata fields for filtering and retrieval
    

You can also pre-create indexes in Azure Portal for custom configurations. Example schema:

Copy

    {
      "name": "n8n-vectorstore",
      "fields": [\
        {\
          "name": "id",\
          "type": "Edm.String",\
          "key": true,\
          "filterable": true\
        },\
        {\
          "name": "content",\
          "type": "Edm.String",\
          "searchable": true\
        },\
        {\
          "name": "content_vector",\
          "type": "Collection(Edm.Single)",\
          "searchable": true,\
          "vectorSearchDimensions": 1536,\
          "vectorSearchProfileName": "n8n-vector-profile"\
        },\
        {\
          "name": "metadata",\
          "type": "Edm.String",\
          "filterable": true\
        }\
      ],
      "vectorSearch": {
        "profiles": [\
          {\
            "name": "n8n-vector-profile",\
            "algorithm": "n8n-vector-algorithm"\
          }\
        ],
        "algorithms": [\
          {\
            "name": "n8n-vector-algorithm",\
            "kind": "hnsw",\
            "hnswParameters": {\
              "metric": "cosine",\
              "m": 4,\
              "efConstruction": 400,\
              "efSearch": 500\
            }\
          }\
        ]
      }
    }

**Vector dimensions**

The `vectorSearchDimensions` value must match your embeddings model output.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#node-usage-patterns)

----------------------------------------------------------------------------------------------------------------------------------------------------------

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#use-as-a-regular-node-to-insert-and-retrieve-documents)

Use the node directly in workflows to insert or retrieve documents without an agent. See [this template](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)
 for an example pattern (uses Supabase, but the pattern is identical).

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#connect-directly-to-an-ai-agent-as-a-tool)

Connect to an [AI agent's](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 tool connector to use the vector store as a searchable knowledge base:

AI agent (tools connector) → Azure AI Search Vector Store node

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#use-a-retriever-to-fetch-documents)

Use with [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 and [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 for retrieval-augmented generation:

Question and Answer Chain (Retriever) → Vector Store Retriever (Vector Store) → Azure AI Search Vector Store

See [this example workflow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
.

### Use the Vector Store Question Answer Tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#use-the-vector-store-question-answer-tool)

Use [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize and answer questions:

AI agent (tools) → Vector Store Question Answer Tool (Vector Store) → Azure AI Search Vector Store

See [this example](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#node-parameters)

--------------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has five modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, **Retrieve Documents (As Tool for AI Agent)**, and **Update Documents**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

**Get Many**

In this mode, you can retrieve multiple documents from your vector database by providing a prompt. The prompt will be embedded and used for similarity search. The node will return the documents that are most similar to the prompt with their similarity score. This is useful if you want to retrieve a list of similar documents and pass them to an agent as additional context.

**Insert Documents**

Use Insert Documents mode to insert new documents into your vector database.

**Retrieve Documents (As Vector Store for Chain/Tool)**

Use Retrieve Documents (As Vector Store for Chain/Tool) mode with a vector-store retriever to retrieve documents from a vector database and provide them to the retriever connected to a chain. In this mode you must connect the node to a retriever node or root node.

**Retrieve Documents (As Tool for AI Agent)**

Use Retrieve Documents (As Tool for AI Agent) mode to use the vector store as a tool resource when answering queries. When formulating responses, the agent uses the vector store when the vector store name and description match the question details.

**Update Documents**

Use Update Documents mode to update documents in a vector database by ID. Fill in the **ID** with the ID of the embedding entry to update.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

**Azure AI Search semantic reranking**

Azure AI Search has built-in [semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
 available when you use **Semantic Hybrid** query mode with a semantic configuration. To use it:

1.  Set **Query Mode** to **Semantic Hybrid** in Options
    
2.  Set **Semantic Configuration** to your configuration name (defaults to `semantic-search-config` if not specified)
    

The built-in semantic reranker uses machine learning models to improve relevance. You can chain an additional reranking node after semantic reranking for further refinement.

[Semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
 is only available if your index has a semantic configuration defined.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#get-many-parameters)

*   **Endpoint**: Your Azure AI Search endpoint (format: `https://your-service.search.windows.net`)
    
*   **Index Name**: The index to query
    
*   **Limit**: Maximum documents to return (default: 4)
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#insert-documents-parameters)

*   **Endpoint**: Your Azure AI Search endpoint
    
*   **Index Name**: The index to use (created automatically if it doesn't exist)
    
*   **Batch Size**: Number of documents uploaded per batch to Azure AI Search. Adjust based on document size and your service tier limits. This controls upload batching only—embedding generation batching is configured in embedding nodes.
    

### Update Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#update-documents-parameters)

*   **Endpoint**: Your Azure AI Search endpoint
    
*   **Index Name**: The index to update
    

### Retrieve Documents parameters (As Vector Store for Chain/Tool)[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#retrieve-documents-parameters-as-vector-store-for-chaintool)

*   **Endpoint**: Your Azure AI Search endpoint
    
*   **Index Name**: The index to query
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: Tool name shown to the LLM
    
*   **Description**: Explain to the LLM what this tool does. Be specific to help the LLM choose when to use this tool.
    
*   **Endpoint**: Your Azure AI Search endpoint
    
*   **Index Name**: The index to query
    
*   **Limit**: Maximum results to retrieve (e.g., `10` for ten best matches)
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#node-options)

--------------------------------------------------------------------------------------------------------------------------------------------

### Options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#options)

*   **Filter**: [OData filter expression](https://learn.microsoft.com/azure/search/search-query-odata-filter)
     to filter results by document fields or metadata. See filter examples below.
    
*   **Query Mode**: Search strategy to use:
    
    *   **Vector**: Similarity search using embeddings only
        
    *   **Keyword**: Full-text search using BM25 ranking
        
    *   **Hybrid** (default): Combines vector and keyword search with Reciprocal Rank Fusion (RRF)
        
    *   **Semantic Hybrid**: Hybrid search with [semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
         for improved relevance
        
    
*   **Semantic Configuration**: Name of the semantic configuration to use for [semantic ranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
    . Defaults to `semantic-search-config` if not specified. Only required if you pre-created an index with a custom semantic configuration name.
    

**Query mode selection**

Use **Vector** for semantic similarity, **Keyword** for exact term matching, **Hybrid** for balanced results, or **Semantic Hybrid** when you've configured semantic search in your index for maximum relevance.

### OData filter examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#odata-filter-examples)

Azure AI Search uses [OData syntax](https://learn.microsoft.com/azure/search/search-query-odata-filter)
 for filtering. Metadata fields are accessed using `metadata/fieldName` format.

**Filter by document ID:**

Copy

    id eq '3da6491a-f930-4a4e-9471-c05dcd450ba0'

**Filter by metadata field:**

Copy

    metadata/source eq 'user-guide'

**Complex AND filter:**

Copy

    metadata/category eq 'technology' and metadata/author eq 'John'

**Complex OR filter:**

Copy

    metadata/source eq 'user-guide' or metadata/rating ge 4

**Numeric comparison:**

Copy

    metadata/rating ge 4 and metadata/rating lt 10

**String matching with NOT:**

Copy

    metadata/category eq 'technology' and metadata/title ne 'Deprecated'

**Supported OData operators:**

*   Comparison: `eq`, `ne`, `gt`, `ge`, `lt`, `le`
    
*   Logical: `and`, `or`, `not`
    
*   String functions: `startswith()`, `endswith()`, `contains()`
    
*   Collection functions: `any()`, `all()`
    

**Filter format**

Filters work across all query modes (Vector, Keyword, Hybrid, Semantic Hybrid) and all operation modes (retrieve, load, retrieve-as-tool).

Azure AI Search specific features[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#azure-ai-search-specific-features)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Hybrid search with RRF[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#hybrid-search-with-rrf)

Azure AI Search's hybrid search uses Reciprocal Rank Fusion to merge vector and keyword results, providing better accuracy than either method alone.

### [Semantic ranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#semantic-rankinghttpslearnmicrosoftcomazuresearchsemantic-search-overview)

Semantic Hybrid mode applies machine learning models to rerank results based on semantic understanding of your query. This requires a semantic configuration in your index.

### OData filters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#odata-filters)

Use OData syntax to filter by document fields or metadata before vector search executes. This improves performance and precision when you need results from specific sources or with certain attributes.

### HNSW algorithm[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#hnsw-algorithm)

Azure AI Search uses Hierarchical Navigable Small World (HNSW) graphs for approximate nearest neighbor search, providing fast retrieval at scale with configurable accuracy/speed tradeoffs.

Troubleshooting[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#troubleshooting)

--------------------------------------------------------------------------------------------------------------------------------------------------

### Index issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#index-issues)

**Index not found**: Verify the index name is correct (case-sensitive) and exists in your Azure AI Search service. If using auto-creation, check that the index was created successfully.

**Vector dimension mismatch**: Ensure your embedding model dimensions match the index vector field dimensions. Check the index schema to confirm the `vectorSearchDimensions` setting.

**Document insert failures**:

*   Verify write permissions (admin API key required)
    
*   Check document fields match your index schema
    
*   Ensure required fields are provided in documents
    
*   Review batch size settings if experiencing timeouts with large document sets
    

### Filter issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#filter-issues)

**Filter not working**:

*   Verify OData syntax is correct
    
*   Ensure metadata fields use `metadata/` prefix: `metadata/source eq 'value'`
    
*   Check that filtered fields are marked as `filterable` in your index schema
    
*   Test with simple filters first (`id eq 'value'`) before complex expressions
    

**Invalid OData syntax**:

*   Use single quotes for string values: `metadata/source eq 'value'`
    
*   Use proper operators: `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `and`, `or`, `not`
    
*   Refer to [OData filter documentation](https://learn.microsoft.com/azure/search/search-query-odata-filter)
     for syntax details
    

### Connection issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#connection-issues)

**Unable to connect**:

*   Verify endpoint URL format: `https://your-service.search.windows.net`
    
*   Confirm your Azure AI Search service is running and accessible
    
*   Check network security groups, firewall rules, and private endpoint configurations
    
*   For Azure-hosted n8n, verify virtual network peering or service endpoint configuration if using private endpoints
    

### Authentication issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#authentication-issues)

For authentication troubleshooting including API key errors, refer to the [credentials documentation troubleshooting section](https://docs.n8n.io/integrations/builtin/credentials/azureaisearch#troubleshooting)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Azure AI Search Vector Store node documentation integration templates](https://n8n.io/integrations/azure-ai-search-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Azure AI Search Vector Search documentation](https://learn.microsoft.com/azure/search/vector-search-overview)
    
*   [Azure AI Search REST API reference](https://learn.microsoft.com/rest/api/searchservice/)
    
*   [OData filter syntax for Azure AI Search](https://learn.microsoft.com/azure/search/search-query-odata-filter)
    

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

### Self-hosted AI Starter Kit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch#self-hosted-ai-starter-kit)

New to working with AI and using self-hosted n8n? Try n8n's [self-hosted AI Starter Kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
 to get started with a proof-of-concept or demo playground using Ollama, Qdrant, and PostgreSQL.

[PreviousDatabricks AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.databricksaiagent)
[NextSimple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)

Last updated 10 days ago

Was this helpful?
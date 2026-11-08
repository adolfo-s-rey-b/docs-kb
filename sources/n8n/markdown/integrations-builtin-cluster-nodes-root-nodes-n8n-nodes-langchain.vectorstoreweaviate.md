For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md)
.

Use the Weaviate node to interact with your Weaviate collection as a vector store. You can insert documents into or retrieve documents from a vector database. You can also retrieve documents to provide them to a retriever connected to a chain or connect this node directly to an agent to use as a tool. On this page, you'll find the node parameters for the Weaviate node, and links to more resources.

**Credentials**

Refer to the [Weaviate credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/weaviate)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#node-usage-patterns)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Weaviate Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the Weaviate Vector Store as a regular node to insert or get documents. This pattern places the Weaviate Vector Store in the regular connection flow without using an agent.

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Weaviate Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Weaviate Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Weaviate Vector Store node to fetch documents from the Weaviate Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Weaviate Vector Store node. Rather than connecting the Weaviate Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

**Multitenancy**

You can separate your data into isolated tenants for the same collection (for example, for different customers). For that, you must always provide a [Tenant Name](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#tenant-name)
 both when inserting and retrieving objects. [Read more about multi tenancy in Weaviate docs](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy)
.

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#get-many-parameters)

*   **Weaviate Collection**: Enter the name of the Weaviate collection to use.
    
*   **Prompt**: Enter the search query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#insert-documents-parameters)

*   **Weaviate Collection**: Enter the name of the Weaviate collection to use.
    
*   **Embedding Batch Size**: The number of documents to embed in a single batch. The default is 200 documents.
    

### Retrieve Documents (As Vector Store for Chain/Tool) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-vector-store-for-chaintool-parameters)

*   **Weaviate Collection**: Enter the name of the Weaviate collection to use.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Weaviate Collection**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Weaviate Collection**: Enter the name of the Weaviate collection to use.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Include Metadata[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#include-metadata)

Whether to include document metadata.

You can use this with the [Get Many](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#get-many-parameters)
 and [Retrieve Documents (As Tool for AI Agent)](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-tool-for-ai-agent-parameters)
 modes.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

### Search Filters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#search-filters)

Available for the [Get Many](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#get-many-parameters)
, [Retrieve Documents (As Vector Store for Chain/Tool)](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-vector-store-for-chaintool-parameters)
, and [Retrieve Documents (As Tool for AI Agent)](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-tool-for-ai-agent-parameters)
 operation modes.

When searching for data, use this to match metadata associated with documents. You can learn more about the operators and query structure in [Weaviate's conditional filters documentation](https://docs.weaviate.io/weaviate/api/graphql/filters)
.

You can use both `AND` and `OR` with different operators. Operators are case insensitive:

Copy

    {
      "OR": [\
        {\
            "path": ["source"],\
            "operator": "Equal",\
            "valueString": "source1"\
        },\
        {\
            "path": ["source"],\
            "operator": "Equal",\
            "valueString": "source1"\
        }\
      ]
    }

Supported operators:

Operator

Required Field(s)

Description

`'equal'`

`valueString` or `valueNumber`

Checks if the property is equal to the given string or number.

`'like'`

`valueString`

Checks if the string property matches a pattern (for example, sub-string match).

`'containsAny'`

`valueTextArray` (string\[\])

Checks if the property contains **any** of the given values.

`'containsAll'`

`valueTextArray` (string\[\])

Checks if the property contains **all** of the given values.

`'greaterThan'`

`valueNumber`

Checks if the property value is greater than the given number.

`'lessThan'`

`valueNumber`

Checks if the property value is less than the given number.

`'isNull'`

`valueBoolean` (true/false)

Checks if the property is null or not. ([must enable before ingestion](https://docs.weaviate.io/weaviate/manage-collections/collection-operations#set-inverted-index-parameters)
)

`'withinGeoRange'`

`valueGeoCoordinates` (object with geolocation data)

Filters by proximity to geographic coordinates.

When inserting data, the document loader sets the metadata. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

### Metadata Keys[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#metadata-keys)

You can define which metadata keys you want Weaviate to return on your queries. This can reduce network load, as you will only get properties you have defined. Returns all properties from the server by default.

Available for the [Get Many](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#get-many-parameters)
, [Retrieve Documents (As Vector Store for Chain/Tool)](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-vector-store-for-chaintool-parameters)
, and [Retrieve Documents (As Tool for AI Agent)](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#retrieve-documents-as-tool-for-ai-agent-parameters)
 operation modes.

### Hybrid: Query Text[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-query-text)

Provide a query text to combine vector search with a keyword/text search.

### Hybrid: Explain Score[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-explain-score)

Whether to show the score fused between hybrid and vector search explanation.

### Hybrid: Fusion Type[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-fusion-type)

Select the fusion type for combining vector and keyword search results. [Learn more about fusion algorithms](https://weaviate.io/learn/knowledgecards/fusion-algorithm)
.

Options:

*   **Relative Score**: Uses relative score fusion
    
*   **Ranked**: Uses ranked fusion
    

### Hybrid: Auto Cut Limit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-auto-cut-limit)

Limit result groups by detecting sudden jumps in score. [Learn more about autocut](https://docs.weaviate.io/weaviate/api/graphql/additional-operators#autocut)
.

### Hybrid: Alpha[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-alpha)

Change the relative weights of the keyword and vector components. 1.0 = pure vector, 0.0 = pure keyword. Default is 0.5. [Learn more about the alpha parameter](https://weaviate.io/learn/knowledgecards/alpha-parameter)
.

### Hybrid: Query Properties[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-query-properties)

Comma-separated list of properties to include in the query with optionally weighted values, e.g., "question^2,answer". [Learn more about setting weights on property values](https://docs.weaviate.io/weaviate/search/hybrid#set-weights-on-property-values)
.

### Hybrid: Max Vector Distance[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#hybrid-max-vector-distance)

Set the maximum allowable distance for the vector search component.

### Tenant Name[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#tenant-name)

The specific tenant to store or retrieve documents for. [Learn more about multi-tenancy](https://weaviate.io/learn/knowledgecards/multi-tenancy)
.

**Must enable at creation**

You must pass a tenant name at first ingestion to enable multitenancy for a collection. You can't enable or disable multitenancy after creation.

### Text Key[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#text-key)

The key in the document that contains the embedded text.

### Skip Init Checks[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#skip-init-checks)

Whether to [skip initialization checks](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#initial-connection-checks)
 when instantiating the client.

### Init Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#init-timeout)

Number of seconds to wait before [timing out](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)
 during initial checks.

### Insert Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#insert-timeout)

Number of seconds to wait before [timing out](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)
 during inserts.

### Query Timeout[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#query-timeout)

Number of seconds to wait before [timing out](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)
 during queries.

### GRPC Proxy[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#grpc-proxy)

A proxy to use for gRPC requests.

### Clear Data[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#clear-data)

Available for the [Insert Documents](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#insert-documents-parameters)
 operation mode.

Whether to clear the collection or tenant before inserting new data.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Weaviate Vector Store node documentation integration templates](https://n8n.io/integrations/weaviate-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Weaviate documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/weaviate)
 for more information about the service.

Refer to [Weaviate Installation](https://docs.weaviate.io/deploy)
 for a self-hosted Weaviate Cluster.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousSupabase Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase)
[NextZep Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep)

Last updated 10 days ago

Was this helpful?
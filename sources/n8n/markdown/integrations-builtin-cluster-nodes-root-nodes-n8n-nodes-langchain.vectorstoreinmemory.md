For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md)
.

Use the Simple Vector Store node to store and retrieve embeddings in n8n's in-app memory.

On this page, you'll find the node parameters for the Simple Vector Store node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

**This node is different from AI memory nodes**

The simple vector storage described here is different to the AI memory nodes such as [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)
.

This node creates a vector database in the app memory.

Data safety limitations[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#data-safety-limitations)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Before using the Simple Vector Store node, it's important to understand its limitations and how it works.

n8n recommends using Simple Vector store for development use only.

### Vector store data isn't persistent[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#vector-store-data-isnt-persistent)

This node stores data in memory only. All data is lost when n8n restarts and may also be purged in low-memory conditions.

### All instance users can access vector store data[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#all-instance-users-can-access-vector-store-data)

Memory keys for the Simple Vector Store node are global, not scoped to individual workflows.

This means that all users of the instance can access vector store data by adding a Simple Vector Store node and selecting the memory key, regardless of the access controls set for the original workflow. Take care not to expose sensitive information when ingesting data with the Simple Vector Store node.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#node-usage-patterns)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Simple Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the Simple Vector Store as a regular node to insert or get documents. This pattern places the Simple Vector Store in the regular connection flow without using an agent.

You can see an example of in step 2 of [this template](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
.

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Simple Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Simple Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Simple Vector Store node to fetch documents from the Simple Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
 (the linked example uses Pinecone, but the pattern is the same) would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Simple Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Simple Vector Store node. Rather than connecting the Simple Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The [connections flow](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
 in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Simple Vector store.

Memory Management[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#memory-management)

-------------------------------------------------------------------------------------------------------------------------------------------------

The Simple Vector Store implements memory management to prevent excessive memory usage:

*   Automatically cleans up old vector stores when memory pressure increases
    
*   Removes inactive stores that haven't been accessed for a configurable amount of time
    

### Configuration Options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#configuration-options)

You can control memory usage with these environment variables:

Variable

Type

Default

Description

`N8N_VECTOR_STORE_MAX_MEMORY`

Number

\-1

Maximum memory in MB allowed for all vector stores combined (-1 to disable limits).

`N8N_VECTOR_STORE_TTL_HOURS`

Number

\-1

Hours of inactivity after which a store gets removed (-1 to disable TTL).

On n8n Cloud, these values are preset to 100MB (about 8,000 documents, depending on document size and metadata) and 7 days respectively. For self-hosted instances, both values default to -1(no memory limits or time-based cleanup).

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#get-many-parameters)

*   **Memory Key**: Select or create the key containing the vector memory you want to query.
    
*   **Prompt**: Enter the search query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#insert-documents-parameters)

*   **Memory Key**: Select or create the key you want to store the vector memory as.
    
*   **Clear Store**: Use this parameter to control whether to wipe the vector store for the given memory key for this workflow before inserting data (turned on).
    

### Retrieve Documents (As Vector Store for Chain/Tool) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#retrieve-documents-as-vector-store-for-chaintool-parameters)

*   **Memory Key**: Select or create the key containing the vector memory you want to query.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Memory Key**: Select or create the key containing the vector memory you want to query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Simple Vector Store node documentation integration templates](https://n8n.io/integrations/in-memory-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Memory Vector Store documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/memory)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousAzure AI Search Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch)
[NextMilvus Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus)

Last updated 10 days ago

Was this helpful?
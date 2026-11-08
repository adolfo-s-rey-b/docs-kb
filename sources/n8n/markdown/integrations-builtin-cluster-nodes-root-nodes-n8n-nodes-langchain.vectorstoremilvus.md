For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md)
.

Use the Milvus node to interact with your Milvus database as vector store. You can insert documents into a vector database, get documents from a vector database, retrieve documents to provide them to a retriever connected to a chain, or connect directly to an agent as a tool.

On this page, you'll find the node parameters for the Milvus node, and links to more resources.

**Credentials**

Refer to the [Milvus credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/milvus)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#node-usage-patterns)

---------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Milvus Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the Milvus Vector Store as a regular node to insert, or get documents. This pattern places the Milvus Vector Store in the regular connection flow without using an agent.

See this [example template](https://n8n.io/workflows/3573-create-a-rag-system-with-paul-essays-milvus-and-openai-for-cited-answers/)
 for how to build a system that stores documents in Milvus and retrieves them to support cited, chat-based answers.

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Milvus Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Milvus Vector Store node. See this [example template](https://n8n.io/workflows/3576-paul-graham-essay-search-and-chat-with-milvus-vector-database/)
 where data is embedded and indexed in Milvus, and the AI Agent uses the vector store as a knowledge tool for question-answering.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Milvus Vector Store node to fetch documents from the Milvus Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

A typical node connection flow looks like this: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Milvus Vector Store.

Check out this [workflow example](https://n8n.io/workflows/3574-create-a-paul-graham-essay-qanda-system-with-openai-and-milvus-vector-database/)
 to see how to ingest external data into Milvus and build a chat-based semantic Q&A system.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Milvus Vector Store node. Rather than connecting the Milvus Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The connections flow would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Milvus Vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#get-many-parameters)

*   **Milvus Collection**: Select or enter the Milvus Collection to use.
    
*   **Prompt**: Enter your search query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#insert-documents-parameters)

*   **Milvus Collection**: Select or enter the Milvus Collection to use.
    
*   **Clear Collection**: Specify whether to clear the collection before inserting new documents.
    

### Retrieve Documents (As Vector Store for Chain/Tool) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#retrieve-documents-as-vector-store-for-chaintool-parameters)

*   **Milvus collection**: Select or enter the Milvus Collection to use.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Milvus Collection**: Select or enter the Milvus Collection to use.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

### Metadata Filter[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#metadata-filter)

Available in **Get Many** mode. When searching for data, use this to match with metadata associated with the document.

This is an `AND` query. If you specify more than one metadata filter field, all of them must match.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

### Clear Collection[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#clear-collection)

Available in **Insert Documents** mode. Deletes all data from the collection before inserting the new data.

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousSimple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)
[NextMongoDB Atlas Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas)

Last updated 10 days ago

Was this helpful?
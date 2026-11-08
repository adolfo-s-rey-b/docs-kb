For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md)
.

PGVector is an extension of Postgresql. Use this node to interact with the PGVector tables in your Postgresql database. You can insert documents into a vector table, get documents from a vector table, retrieve documents to provide them to a retriever connected to a chain, or connect directly to an agent as a tool.

On this page, you'll find the node parameters for the PGVector node, and links to more resources.

**Credentials**

Refer to the [Postgres credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/postgres)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#node-usage-patterns)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the PGVector Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the PGVector Vector Store as a regular node to insert or get documents. This pattern places the PGVector Vector Store in the regular connection flow without using an agent.

You can see an example of this in scenario 1 of [this template](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)
 (the template uses the Supabase Vector Store, but the pattern is the same).

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the PGVector Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> PGVector Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the PGVector Vector Store node to fetch documents from the PGVector Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
 (the linked example uses Pinecone, but the pattern is the same) would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> PGVector Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the PGVector Vector Store node. Rather than connecting the PGVector Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The [connections flow](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
 (the linked example uses the Simple Vector Store, but the pattern is the same) in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Simple Vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#get-many-parameters)

*   **Table name**: Enter the name of the table you want to query.
    
*   **Prompt**: Enter your search query.
    
*   **Limit**: Enter a number to set how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#insert-documents-parameters)

*   **Table name**: Enter the name of the table you want to query.
    

### Retrieve Documents parameters (As Vector Store for Chain/Tool)[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#retrieve-documents-parameters-as-vector-store-for-chaintool)

*   **Table name**: Enter the name of the table you want to query.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Table Name**: Enter the PGVector table to use.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

### Collection[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#collection)

A way to separate datasets in PGVector. This creates a separate table and column to keep track of which collection a vector belongs to.

*   **Use Collection**: Select whether to use a collection (turned on) or not (turned off).
    
*   **Collection Name**: Enter the name of the collection you want to use.
    
*   **Collection Table Name**: Enter the name of the table to store collection information in.
    

### Column Names[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#column-names)

The following options specify the names of the columns to store the vectors and corresponding information in:

*   **ID Column Name**
    
*   **Vector Column Name**
    
*   **Content Column Name**
    
*   **Metadata Column Name**
    

### Metadata Filter[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#metadata-filter)

Available in **Get Many** mode. When searching for data, use this to match with metadata associated with the document.

This is an `AND` query. If you specify more than one metadata filter field, all of them must match.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse PGVector Vector Store node documentation integration templates](https://n8n.io/integrations/postgres-pgvector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's PGVector documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/pgvector)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

### Self-hosted AI Starter Kit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector#self-hosted-ai-starter-kit)

New to working with AI and using self-hosted n8n? Try n8n's [self-hosted AI Starter Kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
 to get started with a proof-of-concept or demo playground using Ollama, Qdrant, and PostgreSQL.

[PreviousMongoDB Atlas Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas)
[NextOracle Database Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb)

Last updated 10 days ago

Was this helpful?
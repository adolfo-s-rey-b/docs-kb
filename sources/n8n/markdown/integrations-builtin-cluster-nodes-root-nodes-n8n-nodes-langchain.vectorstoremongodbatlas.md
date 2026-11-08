For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md)
.

MongoDB Atlas Vector Search is a feature of MongoDB Atlas that enables users to store and query vector embeddings. Use this node to interact with Vector Search indexes in your MongoDB Atlas collections. You can insert documents, retrieve documents, and use the vector store in chains or as a tool for agents.

On this page, you'll find the node parameters for the MongoDB Atlas Vector Store node, and links to more resources.

**Credentials**

Refer to the [MongoDB credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/mongodb)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Prerequisites[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#prerequisites)

---------------------------------------------------------------------------------------------------------------------------------------------

Before using this node, create a [Vector Search index](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/)
 in your MongoDB Atlas collection. Follow these steps to create one:

1.  Log in to the [MongoDB Atlas dashboard](https://cloud.mongodb.com/)
    .
    
2.  Select your organization and project.
    
3.  Find "Search & Vector Search" section.
    
4.  Select your cluster and click "Go to search".
    
5.  Click "Create Search Index".
    
6.  Choose "Vector Search" mode and use the visual or JSON editors. For example:
    
    Copy
    
        {
          "fields": [\
            {\
              "type": "vector",\
              "path": "<field-name>",\
              "numDimensions": 1536, // any other value\
              "similarity": "<similarity-function>"\
            }\
          ]
        }
    
7.  Adjust the "dimensions" value according to your embedding model (For example, `1536` for OpenAI's `text-embedding-small-3`).
    
8.  Name your index and create.
    

Make sure to note the following values which are required when configuring the node:

*   Collection name
    
*   Vector index name
    
*   Field names for embeddings and metadata
    

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#node-usage-patterns)

---------------------------------------------------------------------------------------------------------------------------------------------------------

You can use the MongoDB Atlas Vector Store node in the following patterns:

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the MongoDB Atlas Vector Store as a regular node to insert or get documents. This pattern places the MongoDB Atlas Vector Store in the regular connection flow without using an agent.

You can see an example of this in scenario 1 of [this template](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)
 (the template uses the Supabase Vector Store, but the pattern is the same).

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the MongoDB Atlas Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use the vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> MongoDB Atlas Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the MongoDB Atlas Vector Store node to fetch documents from the MongoDB Atlas Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
 (the linked example uses Pinecone, but the pattern is the same) would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> MongoDB Atlas Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the MongoDB Atlas Vector Store node. Rather than connecting the MongoDB Atlas Vector Store directly as a tool, this pattern uses a tool specifically designed to summarize data in the vector store.

The [connections flow](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
 (the linked example uses the In-Memory Vector Store, but the pattern is the same) in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> In-Memory Vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#get-many-parameters)

*   **Mongo Collection**: Enter the name of the MongoDB collection to use.
    
*   **Vector Index Name**: Enter the name of the Vector Search index in your MongoDB Atlas collection.
    
*   **Embedding Field**: Enter the field name in your documents that contains the vector embeddings.
    
*   **Metadata Field**: Enter the field name in your documents that contains the text metadata.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#insert-documents-parameters)

*   **Mongo Collection**: Enter the name of the MongoDB collection to use.
    
*   **Vector Index Name**: Enter the name of the Vector Search index in your MongoDB Atlas collection.
    
*   **Embedding Field**: Enter the field name in your documents that contains the vector embeddings.
    
*   **Metadata Field**: Enter the field name in your documents that contains the text metadata.
    

### Retrieve Documents parameters (As Vector Store for Chain/Tool)[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#retrieve-documents-parameters-as-vector-store-for-chaintool)

*   **Mongo Collection**: Enter the name of the MongoDB collection to use.
    
*   **Vector Index Name**: Enter the name of the Vector Search index in your MongoDB Atlas collection.
    
*   **Embedding Field**: Enter the field name in your documents that contains the vector embeddings.
    
*   **Metadata Field**: Enter the field name in your documents that contains the text metadata.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Mongo Collection**: Enter the name of the MongoDB collection to use.
    
*   **Vector Index Name**: Enter the name of the Vector Search index in your MongoDB Atlas collection.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#node-options)

-------------------------------------------------------------------------------------------------------------------------------------------

### Options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#options)

*   **Metadata Filter**: Filters results based on metadata.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse MongoDB Atlas Vector Store node documentation integration templates](https://n8n.io/integrations/mongodb-atlas-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Refer to:

*   [LangChain's MongoDB Atlas Vector Search documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/mongodb_atlas)
     for more information about the service.
    
*   [MongoDB Atlas Vector Search documentation](https://www.mongodb.com/docs/atlas/atlas-vector-search/)
     for more information about MongoDB Atlas Vector Search.
    

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

### Self-hosted AI Starter Kit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas#self-hosted-ai-starter-kit)

New to working with AI and using self-hosted n8n? Try n8n's [self-hosted AI Starter Kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
 to get started with a proof-of-concept or demo playground using Ollama, Qdrant, and PostgreSQL.

[PreviousMilvus Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus)
[NextPGVector Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector)

Last updated 10 days ago

Was this helpful?
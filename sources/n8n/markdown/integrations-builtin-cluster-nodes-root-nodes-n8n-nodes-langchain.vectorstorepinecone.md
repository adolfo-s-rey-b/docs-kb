For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)
.

Use the Pinecone node to interact with your Pinecone database as vector store. You can insert documents into a vector database, get documents from a vector database, retrieve documents to provide them to a retriever connected to a chain, or connect directly to an agent as a tool. You can also update an item in a vector database by its ID.

On this page, you'll find the node parameters for the Pinecone node, and links to more resources.

**Credentials**

Refer to the [Pinecone credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/pinecone)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#node-usage-patterns)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Pinecone Vector Store node in the following patterns.

### Use as a regular node to insert, update, and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-as-a-regular-node-to-insert-update-and-retrieve-documents)

You can use the Pinecone Vector Store as a regular node to insert, update, or get documents. This pattern places the Pinecone Vector Store in the regular connection flow without using an agent.

You can see an example of this in scenario 1 of [this template](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)
.

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Pinecone Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Pinecone Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Pinecone Vector Store node to fetch documents from the Pinecone Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
 would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Pinecone Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Pinecone Vector Store node. Rather than connecting the Pinecone Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The [connections flow](https://n8n.io/workflows/2705-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-and-openai/)
 in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Pinecone Vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

### Operation Mode[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#operation-mode)

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

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#get-many-parameters)

*   **Pinecone Index**: Select or enter the Pinecone Index to use.
    
*   **Prompt**: Enter your search query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#insert-documents-parameters)

*   **Pinecone Index**: Select or enter the Pinecone Index to use.
    

### Retrieve Documents (As Vector Store for Chain/Tool) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#retrieve-documents-as-vector-store-for-chaintool-parameters)

*   **Pinecone Index**: Select or enter the Pinecone Index to use.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Pinecone Index**: Select or enter the Pinecone Index to use.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Parameters for **Update Documents**[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#parameters-for-update-documents)

*   ID
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

### Pinecone Namespace[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#pinecone-namespace)

Another segregation option for how to store your data within the index.

### Metadata Filter[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#metadata-filter)

Available in **Get Many** mode. When searching for data, use this to match with metadata associated with the document.

This is an `AND` query. If you specify more than one metadata filter field, all of them must match.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

### Clear Namespace[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#clear-namespace)

Available in **Insert Documents** mode. Deletes all data from the namespace before inserting the new data.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Pinecone Vector Store node documentation integration templates](https://n8n.io/integrations/pinecone-vector-store)
 or [search all templates](https://n8n.io/workflows/)

FAQ[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#faq)

---------------------------------------------------------------------------------------------------------------------

### How do I store documents in Pinecone from n8n?[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#how-do-i-store-documents-in-pinecone-from-n8n)

Use the Pinecone Vector Store as a [regular node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-as-a-regular-node-to-insert-update-and-retrieve-documents)
 with the **Insert Documents** operation, and select your **Pinecone Index**. The node stores the documents in Pinecone as vectors, so you can retrieve them later.

### How do I retrieve the most relevant documents for a query?[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#how-do-i-retrieve-the-most-relevant-documents-for-a-query)

Enter your search in the **Prompt** field and set **Limit** to control how many results come back, for example `10` for the ten best matches. See the [Get Many parameters](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#get-many-parameters)
. To feed the results into a summarization chain, use a [retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-a-retriever-to-fetch-documents)
 with the Question and Answer Chain node.

### How do I connect the vector store to an AI agent as a tool?[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#how-do-i-connect-the-vector-store-to-an-ai-agent-as-a-tool)

Connect the Pinecone Vector Store node to the AI agent's tool connector, so the agent can query the store when it answers. See [Connect directly to an AI agent as a tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#connect-directly-to-an-ai-agent-as-a-tool)
. To summarize the results instead of returning raw documents, use the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#use-the-vector-store-question-answer-tool-to-answer-questions)
.

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Pinecone documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/pinecone)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

### Find your Pinecone index and namespace[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone#find-your-pinecone-index-and-namespace)

Your Pinecone index and namespace are available in your Pinecone account.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-677988e7c1c97ae476777fc35b05e9bbebdfcc22%252Fpinecone-index-namespace.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=971c9c9c8d415ad2caf668cc5744004e&sv=3)

Pinecone console showing the index name and namespace location for a project

[PreviousMigrate from the community package](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks/migrate-from-the-community-package)
[NextQdrant Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant)

Last updated 10 days ago

Was this helpful?
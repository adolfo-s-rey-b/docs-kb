For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)
.

Use the Qdrant node to interact with your Qdrant collection as a vector store. You can insert documents into a vector database, get documents from a vector database, retrieve documents to provide them to a retriever connected to a chain or connect it directly to an agent to use as a tool.

On this page, you'll find the node parameters for the Qdrant node, and links to more resources.

**Credentials**

Refer to the [Qdrant credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/qdrant)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#node-usage-patterns)

---------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Qdrant Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the Qdrant Vector Store as a regular node to insert or get documents. This pattern places the Qdrant Vector Store in the regular connection flow without using an agent.

You can see an example of this in the first part of [this template](https://n8n.io/workflows/2440-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai/)
.

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Qdrant Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Qdrant Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Qdrant Vector Store node to fetch documents from the Qdrant Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/2183-ai-crew-to-automate-fundamental-stock-analysis-qanda-workflow/)
 would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Qdrant Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Qdrant Vector Store node. Rather than connecting the Qdrant Vector Store directly as a tool, this pattern uses a tool specifically designed to summarizes data in the vector store.

The [connections flow](https://n8n.io/workflows/2464-scale-deal-flow-with-a-pitch-deck-ai-vision-chatbot-and-qdrant-vector-store/)
 in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Qdrant Vector store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#get-many-parameters)

*   **Qdrant collection name**: Enter the name of the Qdrant collection to use.
    
*   **Prompt**: Enter the search query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

This Operation Mode includes one **Node option**, the [Metadata Filter](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#metadata-filter)
.

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#insert-documents-parameters)

*   **Qdrant collection name**: Enter the name of the Qdrant collection to use.
    

This Operation Mode includes one **Node option**:

*   **Collection Config**: Enter JSON options for creating a Qdrant collection creation configuration. Refer to the Qdrant [Collections](https://qdrant.tech/documentation/concepts/collections/)
     documentation for more information.
    

### Retrieve Documents (As Vector Store for Chain/Tool) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#retrieve-documents-as-vector-store-for-chaintool-parameters)

*   **Qdrant Collection**: Enter the name of the Qdrant collection to use.
    

This Operation Mode includes one **Node option**, the [Metadata Filter](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#metadata-filter)
.

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Qdrant Collection**: Enter the name of the Qdrant collection to use.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

### Metadata Filter[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#metadata-filter)

Available in **Get Many** mode. When searching for data, use this to match with metadata associated with the document.

This is an `AND` query. If you specify more than one metadata filter field, all of them must match.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Qdrant Vector Store node documentation integration templates](https://n8n.io/integrations/qdrant-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Qdrant documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/qdrant)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

### Self-hosted AI Starter Kit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant#self-hosted-ai-starter-kit)

New to working with AI and using self-hosted n8n? Try n8n's [self-hosted AI Starter Kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
 to get started with a proof-of-concept or demo playground using Ollama, Qdrant, and PostgreSQL.

[PreviousPinecone Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone)
[NextRedis Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis)

Last updated 10 days ago

Was this helpful?
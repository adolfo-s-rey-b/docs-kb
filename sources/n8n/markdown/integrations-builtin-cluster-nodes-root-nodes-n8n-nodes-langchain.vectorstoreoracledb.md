For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md)
.

Use the Oracle Database Vector Store node to interact with Oracle Database as a vector store. You can insert documents into a vector table, get documents from a vector table, retrieve documents to provide them to a retriever connected to a chain, or connect directly to an agent as a tool.

On this page, you'll find the node parameters for the Oracle Database Vector Store node, and links to more resources.

**Credentials**

Refer to the [Oracle Database credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
 for authentication information for this node.

**Oracle Database vector support**

Your Oracle Database instance must support Oracle AI Vector Search for vector store operations. For more details, refer to the [Oracle AI Vector Search Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/26/arpls&id=VECSE-GUID-29B9E7E1-5A99-4D95-8614-58CA07D29957)
.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node usage patterns[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#node-usage-patterns)

-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use the Oracle Database Vector Store node in the following patterns.

### Use as a regular node to insert and retrieve documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#use-as-a-regular-node-to-insert-and-retrieve-documents)

You can use the Oracle Database Vector Store as a regular node to insert or get documents. This pattern places the Oracle Database Vector Store in the regular connection flow without using an agent.

You can see an example of this in scenario 1 of [this template](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)
 (the template uses the Supabase Vector Store, but the pattern is the same).

### Connect directly to an AI agent as a tool[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#connect-directly-to-an-ai-agent-as-a-tool)

You can connect the Oracle Database Vector Store node directly to the tool connector of an [AI agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 to use a vector store as a resource when answering queries.

Here, the connection would be: AI agent (tools connector) -> Oracle Database Vector Store node.

### Use a retriever to fetch documents[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#use-a-retriever-to-fetch-documents)

You can use the [Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
 node with the Oracle Database Vector Store node to fetch documents from the Oracle Database Vector Store node. This is often used with the [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
 node to fetch documents from the vector store that match the given chat input.

An [example of the connection flow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)
 (the linked example uses Pinecone, but the pattern is the same) would be: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Oracle Database Vector Store.

### Use the Vector Store Question Answer Tool to answer questions[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#use-the-vector-store-question-answer-tool-to-answer-questions)

Another pattern uses the [Vector Store Question Answer Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to summarize results and answer questions from the Oracle Database Vector Store node. Rather than connecting the Oracle Database Vector Store directly as a tool, this pattern uses a tool specifically designed to summarize data in the vector store.

The [connections flow](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)
 (the linked example uses the Simple Vector Store, but the pattern is the same) in this case would look like this: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Oracle Database Vector Store.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------

This Vector Store node has four modes: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)**. The mode you select determines the operations you can perform with the node and what inputs and outputs are available.

### Rerank Results[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#rerank-results)

Enables reranking. If you enable this option, you must connect a reranking node, such as [Reranker Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere)
, to the vector store. That node will then rerank the results for queries. You can use this option with the `Get Many`, `Retrieve Documents (As Vector Store for Chain/Tool)` and `Retrieve Documents (As Tool for AI Agent)` modes.

### Get Many parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#get-many-parameters)

*   **Table Name**: Enter the name of the table you want to query. If the table doesn't exist, the node creates it.
    
*   **Prompt**: Enter your search query.
    
*   **Limit**: Enter a number to set how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

### Insert Documents parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#insert-documents-parameters)

*   **Table Name**: Enter the name of the table to store vectors in. If the table doesn't exist, the node creates it.
    

### Retrieve Documents parameters (As Vector Store for Chain/Tool)[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#retrieve-documents-parameters-as-vector-store-for-chain-tool)

*   **Table Name**: Enter the name of the table you want to query.
    

### Retrieve Documents (As Tool for AI Agent) parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#retrieve-documents-as-tool-for-ai-agent-parameters)

*   **Name**: The name of the vector store.
    
*   **Description**: Explain to the LLM what this tool does. A good, specific description allows LLMs to produce expected results more often.
    
*   **Table Name**: Enter the Oracle Database vector table to query.
    
*   **Limit**: Enter how many results to retrieve from the vector store. For example, set this to `10` to get the ten best results.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#node-options)

---------------------------------------------------------------------------------------------------------------------------------------

### Distance Strategy[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#distance-strategy)

Available in **Get Many** and **Retrieve Documents** modes. This is the method to calculate the distance between two vectors. Choose from:

*   **Cosine**
    
*   **Inner Product**
    
*   **Euclidean**
    
*   **Manhattan**
    
*   **Euclidean Squared**
    
*   **Hamming**
    

### Metadata Filter[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#metadata-filter)

Available in **Get Many**, **Retrieve Documents (As Vector Store for Chain/Tool)**, and **Retrieve Documents (As Tool for AI Agent)** modes. When searching for data, use this to match with metadata associated with the document.

If you specify more than one metadata filter field using the UI, all fields must match. This works like an `AND` query.

For advanced filtering, Oracle Database Vector Store passes metadata filters through to Oracle AI Vector Search. This supports richer filter objects, including arrays, nested filters, comparison operators such as `$gte`, exclusion operators such as `$nin`, and logical operators such as `$and`.

When inserting data, the metadata is set using the document loader. Refer to [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
 for more information on loading documents.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Oracle Database Vector Store node documentation integration templates](https://n8n.io/integrations/oracle-database-vector-store)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Oracle AI Vector Search documentation](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/)
 for more information about vector search in Oracle Database.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousPGVector Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector)
[NextChroma Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context.md)
.

What is RAG[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#what-is-rag)

---------------------------------------------------------------------------------------------------------------------

Retrieval-Augmented Generation (RAG) is a technique that improves AI responses by combining language models with external data sources. Instead of relying solely on the model's internal training data, RAG systems retrieve relevant documents to ground responses in up-to-date, domain-specific, or proprietary knowledge. RAG workflows typically rely on vector stores to manage and search this external data efficiently.

What is a vector store?[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#what-is-a-vector-store)

--------------------------------------------------------------------------------------------------------------------------------------------

A vector store is a special database designed to store and search high-dimensional vectors: numerical representations of text, images, or other data. When you upload a document, the vector store splits it into chunks and converts each chunk into a vector using an embedding model.

You can query these vectors using similarity searches, which construct results based on _semantic meaning_, rather than keyword matches. This makes vector stores a powerful foundation for RAG and other AI systems that need to retrieve and reason over large sets of knowledge.

How to use RAG in n8n[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#how-to-use-rag-in-n8n)

-----------------------------------------------------------------------------------------------------------------------------------------

**Start with a RAG template**

👉 Try out RAG in n8n with the [RAG Starter Template](https://n8n.io/workflows/5010-rag-starter-template-using-simple-vector-stores-form-trigger-and-openai)
. The template includes two ready-made workflows: one for uploading files and one for querying them.

### Inserting data into your vector store[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#inserting-data-into-your-vector-store)

Before your agent can access custom knowledge, you need to upload that data to a vector store:

1.  Add the nodes needed to fetch your source data.
    
2.  Insert a **Vector Store** node (e.g. the [Simple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)
    ) and choose the **Insert Documents** operation.
    
3.  Select an **embedding model**, which converts your text into vector embeddings. Consult the FAQ for more information on [choosing the right embedding model](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#how-do-i-choose-the-right-embedding-model)
    .
    
4.  Add a [Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
     node, which splits your content into chunks. You can use the default settings or define your own chunking strategy:
    
    *   **Character Text Splitter:** splits by character length.
        
    *   **Recursive Character Text Splitter:** recursively splits by Markdown, HTML, code blocks or simple characters (recommended for most use cases).
        
    *   **Token Text Splitter:** splits by token count.
        
    
5.  (Optional) Add **metadata** to each chunk to enrich the context and allow better filtering later.
    

### Querying your data[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#querying-your-data)

You can query the data in two main ways: using an agent or directly through a node.

### Using agents[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#using-agents)

1.  Add an [agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
     to your workflow.
    
2.  Add the vector store as a **tool** and give it a **description** to help the agent understand when to use it:
    
    *   Set the **limit** to define how many chunks to return.
        
    *   Enable **Include Metadata** to provide extra context for each chunk.
        
    
3.  Add the same **embedding model** you used when inserting the data.
    

**Pro tip**

To save tokens on an expensive model, you can first use the [Vector Store Question Answer tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore)
 to retrieve relevant data, and only then pass the result to the Agent. To see this in action, check out [this template](https://n8n.io/workflows/5011-save-costs-in-rag-workflows-using-the-qanda-tool-with-multiple-models)
.

### Using the node directly[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#using-the-node-directly)

1.  Add your vector store node to the canvas and choose the **Get Many** operation.
    
2.  Enter a query or prompt:
    
    *   Set a **limit** for how many chunks to return.
        
    *   Enable **Include Metadata** if needed.
        
    

FAQs[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#faqs)

-------------------------------------------------------------------------------------------------------

### How do I choose the right embedding model?[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#how-do-i-choose-the-right-embedding-model)

The right embedding model differs from case to case.

In general, smaller models (for example, `text-embedding-ada-002`) are faster and cheaper and thus ideal for short, general-purpose documents or lightweight RAG workflows. Larger models (for example, `text-embedding-3-large`) offer better semantic understanding. These are best for long documents, complex topics, or when accuracy is critical.

### What is the best text splitting for my use case?[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#what-is-the-best-text-splitting-for-my-use-case)

This again depends a lot on your data:

*   Small chunks (for example, 200 to 500 tokens) are good for fine-grained retrieval.
    
*   Large chunks may carry more context but can become diluted or noisy.
    

Using the right overlap size is important for the AI to understand the context of the chunk. That's also why using the Markdown or Code Block splitting can often help to make chunks better.

Another good approach is to add more context to it (for example, about the document where the chunk came from). If you want you can read more about this, you can check out [this great article from Anthropic](https://www.anthropic.com/news/contextual-retrieval)
.

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context#related-resources)

---------------------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
    
*   [What agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
    
*   [How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   [How tools work](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Agents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    

[PreviousStore and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
[NextAgents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)

Last updated 10 days ago

Was this helpful?
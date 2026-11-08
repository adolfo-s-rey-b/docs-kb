For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n.md)
.

n8n's AI nodes use [LangChain](https://docs.langchain.com/oss/javascript/langchain/overview)
's JavaScript framework. Each node is configurable: choose your own agent, LLM, memory, and other components. You can connect any other n8n node to your LangChain nodes as normal, so you can combine LangChain logic with any other data source or service n8n supports.

This page is for readers who already know LangChain and want to see how its concepts map onto n8n. If you're new to AI concepts, start with [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
 instead.

How LangChain concepts map to n8n nodes[](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#how-langchain-concepts-map-to-n8n-nodes)

-------------------------------------------------------------------------------------------------------------------------------------------

n8n represents most LangChain concepts as [cluster nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes)
: a [root node](https://docs.n8n.io/key-concept-glossary#root-node-n8n)
 that defines the cluster's main functionality, with one or more [sub-nodes](https://docs.n8n.io/key-concept-glossary#sub-node-n8n)
 attached to extend it.

LangChain concept

Node category

Example nodes

Learn more

Chain

Root node

[Basic LLM Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)
, [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
, [Summarization Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization)

[What's a chain in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)

Agent

Root node

[AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)

[What's an agent in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)

Language model

Sub-node

[Anthropic Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic)
, [OpenAI Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai)
, [Ollama Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama)

[Sub-nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)

Vector store

Root node

[Pinecone Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone)
, [Qdrant Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant)
, [Simple Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)

[Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)

Memory

Sub-node

[Postgres Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat)
, [Redis Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat)
, [Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)

[How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)

Tool

Sub-node

[Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)
, [Custom Code Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode)
, [Wikipedia](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia)

[What's a tool in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)

Retriever

Sub-node

[Vector Store Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore)
, [Workflow Retriever](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow)

[Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)

Embeddings

Sub-node

[Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai)
, [Embeddings Cohere](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere)

[Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)

Document loader

Sub-node

[Default Data Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader)
, [GitHub Document Loader](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader)

[Sub-nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)

Output parser

Sub-node

[Structured Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured)
, [Auto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)

[Sub-nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)

Text splitter

Sub-node

[Recursive Character Text Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter)
, [Token Splitter](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter)

[Sub-nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)

Memory sub-nodes only attach to the [AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
 root node. Unlike LangChain, none of n8n's chain nodes support memory, so they can't reference earlier messages in a conversation. If your workflow needs to do that, use an agent instead of a chain.

The examples above aren't exhaustive. For the full, up-to-date list of nodes in each category, browse the [root nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes)
 and [sub-nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes)
 libraries. n8n also provides the [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
 node to start a workflow from a chat message, and the [LangChain Code](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code)
 node, which lets you write LangChain JavaScript code directly for functionality that doesn't have a dedicated n8n node yet.

Use LangSmith with a self-hosted n8n instance[](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#use-langsmith-with-a-self-hosted-n8n-instance)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[LangSmith](https://www.langchain.com/langsmith)
 is a developer platform from the LangChain team. Connect a self-hosted n8n instance to LangSmith to record and monitor n8n executions, the same way you'd trace a LangChain application.

**Feature availability**

LangSmith tracing is available on:

*   **Self-hosted:** All editions
    

It isn't available on n8n Cloud.

To connect n8n to LangSmith:

1.  [Log in to LangSmith](https://smith.langchain.com/settings)
     and get your API key.
    
2.  Set the following [environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
     in the environment where you host n8n:
    
    Variable
    
    Value
    
    `LANGCHAIN_ENDPOINT`
    
    `https://api.smith.langchain.com`
    
    `LANGCHAIN_TRACING_V2`
    
    `true`
    
    `LANGCHAIN_API_KEY`
    
    Your LangSmith API key
    
    `LANGCHAIN_PROJECT`
    
    Optional project name. Defaults to `default`
    
    `LANGCHAIN_CALLBACKS_BACKGROUND`
    
    `true` to upload traces asynchronously
    
3.  Restart n8n.
    

LangSmith creates a project named **default** after n8n sends its first trace, unless you set `LANGCHAIN_PROJECT` to a different name. Every trace then goes to that project instead. Traces can arrive with a short delay, because `LANGCHAIN_CALLBACKS_BACKGROUND` uploads them asynchronously by default. Set it to `false` for synchronous uploads when you're debugging.

For information on using LangSmith itself, refer to [LangSmith's documentation](https://docs.smith.langchain.com/)
.

Learn more about LangChain[](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#learn-more-about-langchain)

-----------------------------------------------------------------------------------------------------------------

You don't need to know LangChain to use n8n, but these resources can help if you want to go deeper:

*   The [LangChain documentation](https://docs.langchain.com/)
     covers key concepts and use cases. Choose [LangChain | Python](https://docs.langchain.com/oss/python/langchain/overview)
     or [LangChain | JavaScript](https://docs.langchain.com/oss/javascript/langchain/overview)
     for quickstarts, code examples, and API documentation. LangChain also provides [code templates](https://github.com/langchain-ai/cookbooks)
     for Python and JavaScript, with ideas for common patterns and use cases.
    
*   [What's LangChain?](https://www.ibm.com/think/topics/langchain)
     explains LangChain terminology in plain language, for a general audience.
    
*   This [YouTube series by Greg Kamradt](https://youtu.be/_v_fgW2SkkQ?si=8Z2tfAoXnN3lXU9s)
     works through the LangChain documentation with code examples.
    
*   Join the n8n [Discord](https://discord.gg/bAt54txhHg)
     to discuss LangChain and share your projects with the n8n community.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n#related-resources)

-----------------------------------------------------------------------------------------------

*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [MCP servers](https://docs.n8n.io/build/integrate-ai/mcp-servers)
    
*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [Test and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows)
    
*   [AI examples](https://docs.n8n.io/build/integrate-ai/ai-examples)
    

[PreviousAgents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
[NextTest and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows)

Last updated 10 days ago

Was this helpful?
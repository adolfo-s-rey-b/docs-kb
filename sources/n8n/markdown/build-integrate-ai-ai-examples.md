For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/ai-examples.md)
.

This section provides explanations of important AI concepts, and workflow templates that highlight those concepts, with explanations and configuration guides. The examples cover common use cases and highlight different features of advanced AI in n8n.

*   **Agents and chains**
    
    Learn about agents and chains in AI, including exploring key differences using the example workflow.
    
    [→ What's a chain in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
     [→ What's an agent in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
     [→ Demonstration of key differences between agents and chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    
*   **Call n8n Workflow Tool**
    
    Learn about tools in AI, then explore examples that use n8n workflows as custom tools to give your AI workflow access to more data.
    
    [→ What's a tool in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work)
     [→ Chat with Google Sheets](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)
     [→ Call an API to fetch data](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
     [→ Set up a human fallback](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows)
     [→ Let AI specify tool parameters with `$fromAI()`](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
    
*   **Vector databases**
    
    Learn about vector databases in AI, along with related concepts including embeddings and retrievers.
    
    [→ What's a vector database?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
     [→ Populate a Pinecone vector database from a website](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content)
    
*   **Memory**
    
    Learn about memory in AI.
    
    [→ What's memory in AI?](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   **AI workflow templates**
    
    You can browse AI templates, included community contributions, on the n8n website.
    
    [→ Browse all AI templates](https://n8n.io/workflows/?categories=25)
    

In this section[](https://docs.n8n.io/build/integrate-ai/ai-examples#in-this-section)

--------------------------------------------------------------------------------------

*   [Use Google Sheets as a data source](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)
    : use the n8n workflow tool to load data from Google Sheets into your AI workflow.
    
*   [Call APIs](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
    : use the n8n workflow tool to load data from an API using the HTTP Request node.
    
*   [Use website content](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content)
    : scrape a website, load the data into Pinecone, then query it in a chat workflow.
    
*   [Human-in-the-loop for tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
    : require human approval before an AI Agent runs a tool.
    
*   [Set a human fallback for AI workflows](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows)
    : trigger a human answer when the AI can't help.
    
*   [Use AI for parameters](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
    : use `$fromAI()` to dynamically populate parameters for AI app tools.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/ai-examples#related-resources)

------------------------------------------------------------------------------------------

*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [MCP servers](https://docs.n8n.io/build/integrate-ai/mcp-servers)
    
*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [LangChain in n8n](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n)
    
*   [Test and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows)
    

[PreviousFix common issues](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues)
[NextUse Google Sheets as a data source](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)

Last updated 10 days ago

Was this helpful?
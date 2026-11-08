For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work.md)
.

In AI, 'tools' has a specific meaning. Tools act like addons that your AI can use to access extra context or resources.

Here are a couple of other ways of expressing it:

> Tools are interfaces that an agent can use to interact with the world ([source](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
> )

> We can think of these tools as being almost like functions that your AI model can call ([source](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/)
> )

AI tools in n8n[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work#ai-tools-in-n8n)

------------------------------------------------------------------------------------------------------------------

n8n provides built in nodes and a registry of [MCP servers](https://docs.n8n.io/build/integrate-ai/mcp-servers)
 that you can connect to your AI agent as tools. Built-in nodes include popular services such as [Wikipedia](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia)
 and [SerpAPI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi)
. Apart from these, n8n provides three especially powerful tools:

*   [Call n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)
    : use this to load any n8n workflow as a tool.
    
*   [Custom Code Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode)
    : write code that your agent can run.
    
*   [HTTP Request Tool](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
    : make calls to fetch a website or data from an API.
    

The next three examples highlight the Call n8n Workflow Tool:

*   [Chat with Google Sheets](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)
    
*   [Call an API to fetch data](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
    
*   [Set up a human fallback](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows)
    

You can also learn how to [let AI dynamically specify parameters for tools with the `$fromAI()` function](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Related resources[](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Understand AI components](https://docs.n8n.io/build/integrate-ai/understand-ai-components)
    
*   [What chains do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do)
    
*   [What agents do](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do)
    
*   [How memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
    
*   [Store and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)
    
*   [Retrieve relevant context](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context)
    
*   [Agents vs chains](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains)
    

[PreviousHow memory works](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works)
[NextStore and search data with vectors](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors)

Last updated 10 days ago

Was this helpful?
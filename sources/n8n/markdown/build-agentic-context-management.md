For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/agentic-context-management.md)
.

Agentic context management lets you give AI tools in n8n reusable context, such as your naming rules and preferred nodes, so you don't repeat it in every prompt.

**Preview status**

Agentic context management is in Preview and may change in future releases. Avoid relying on it in production.

How context reaches AI tools[](https://docs.n8n.io/build/agentic-context-management#how-context-reaches-ai-tools)

------------------------------------------------------------------------------------------------------------------

You manage context in **Settings** > **Context**. n8n stores it once and passes it to every AI surface that reads it:

*   **n8n Assistant** reads context on every message you send, so an edit applies from your next message.
    
*   **MCP clients** connected to the [n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
     read context through MCP tools, each time they call them.
    

Context follows n8n's permissions. Each person only receives the context they're allowed to see, and only people with the right role can change context that applies to others.

Types of context[](https://docs.n8n.io/build/agentic-context-management#types-of-context)

------------------------------------------------------------------------------------------

Today, n8n supports one kind of context: [preferences](https://docs.n8n.io/build/agentic-context-management/preferences)
. A preference is a short instruction, such as "Always connect an error workflow", that AI tools apply every time they build workflows and agents for you. You can save a preference for yourself, for a project, or for everyone on the instance.

Related resources[](https://docs.n8n.io/build/agentic-context-management#related-resources)

--------------------------------------------------------------------------------------------

*   [Build](https://docs.n8n.io/build)
    
*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Build and manage agents](https://docs.n8n.io/build/build-and-manage-agents)
    
*   [Integrate AI](https://docs.n8n.io/build/integrate-ai)
    
*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Code in n8n](https://docs.n8n.io/build/code-in-n8n)
    
*   [Keyboard shortcuts](https://docs.n8n.io/build/keyboard-shortcuts)
    

[PreviousUse AI for parameters](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
[NextPreferences](https://docs.n8n.io/build/agentic-context-management/preferences)

Last updated 10 days ago

Was this helpful?
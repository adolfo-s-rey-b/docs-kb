For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md)
.

Model Context Protocol (MCP) is a standard way for AI tools to connect to other apps. n8n has a built-in MCP server, so you can describe the workflow you want in your favorite AI tool — like Claude, ChatGPT, or a coding agent — and it connects straight to your n8n instance to build and run that workflow for you.

This page gives an overview of what building with MCP looks like in n8n. For setup, authentication, and client configuration, follow the MCP guides in **Connect**.

**Ready to set it up?** The full how-to lives in Connect:

*   [Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
     — enable the server, authenticate clients, and expose workflows.
    
*   [MCP server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
     — every tool an MCP client can call.
    

What is MCP?[](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server#what-is-mcp)

-----------------------------------------------------------------------------------------------------------

Model Context Protocol (MCP) is an open standard for connecting AI applications to external systems. It defines two roles:

*   An **MCP server** exposes a set of tools and resources. n8n provides a built-in MCP server to let AI apps interface with n8n workflows and resources.
    
*   An **MCP client** — such as Claude Desktop, Claude Code, Codex, or a custom agent - connects to that server and calls those tools on your behalf.
    

What building with MCP means in n8n[](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server#what-building-with-mcp-means-in-n8n)

----------------------------------------------------------------------------------------------------------------------------------------------------------

When you connect an AI tool to n8n's MCP server, your n8n instance becomes a place that tool can build in directly. Instead of you dragging nodes onto the canvas and wiring them together by hand, you describe the workflow you want in plain language to your favorite AI tool, which then builds it in n8n for you.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-195ec50c796b786864b234b99c6a13fc8aa59860%252Fbuild-n8n-workflow-claude.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fb91f4ec718d49fee3997af6f1d3fdc6&sv=3)

Describing a workflow to build in n8n to Claude

*   **Create new workflows** from a description, and **edit existing ones** (n8n 2.13 onward).
    
*   **Build and manage data tables** to store and reuse data across your workflows.
    
*   **Iterate as you go:** run and test what you've built, review the results, and refine it — all from the same conversation, without switching back to the editor.
    
*   **Search for and run workflows** you already have access to.
    
*   **Follow your preferences:** the client reads your saved [preferences](https://docs.n8n.io/build/agentic-context-management/preferences)
     before it builds, and can save new ones when you state a lasting rule (n8n 2.42.0 onward, in Preview).
    

[Enable Instance-level MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-mcp-access)
 to start building, testing, and running your n8n workflows from an AI application.

### Related MCP features[](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server#related-mcp-features)

Instance-level MCP isn't the only way n8n works with MCP:

*   [**MCP Server Trigger node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
    **:** build a single workflow that acts as its own MCP server, exposing only the tools you design inside it. Use this to hand-craft a custom MCP server for other AI apps to call.
    
*   [**MCP Client Tool node**](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
    **:** go the other direction and let an n8n workflow act as an MCP client that calls external MCP servers.
    

Learn more[](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server#learn-more)

--------------------------------------------------------------------------------------------------------

*   [Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
     — set up instance-level MCP access, authenticate clients (OAuth or API key), and expose workflows.
    
*   [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
     — exact commands and configuration for Lovable, Claude Desktop, Claude Code, Codex, Gemini CLI, Cursor, VS Code, Windsurf, and Google ADK agents.
    
*   [MCP server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
     — full list of available tools and their parameters.
    
*   [MCP Server Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
     — expose tools from a single workflow.
    

Related resources[](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Ways of building workflows](https://docs.n8n.io/build/ways-of-building-workflows)
    
*   [Use n8n Assistant](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant)
    
*   [Use templates](https://docs.n8n.io/build/ways-of-building-workflows/use-templates)
    
*   [Use Ask n8n AI](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant)
    
*   [Use Chat Hub](https://docs.n8n.io/build/ways-of-building-workflows/chat-hub)
    

[PreviousWork with Browser Use](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant/browser-use)
[NextUse templates](https://docs.n8n.io/build/ways-of-building-workflows/use-templates)

Last updated 26 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server.md)
.

The n8n documentation publishes two [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
 servers. Connect an AI tool to a server to let it search n8n's knowledge and answer your questions as you work.

The two servers draw on different sources, so pick the one that fits how you want your AI tool to answer:

Server

Sources

Best for

**GitBook docs server**

The published n8n docs only

Searching and reading exact documentation pages. The docs are the single, authoritative source.

**Kapa.ai server**

The docs, the [community forum](https://community.n8n.io/)
, and the [n8n blog](https://blog.n8n.io/)

Broader questions that the docs alone don't cover, such as troubleshooting and real-world examples. This is the same engine that powers the AI Assistant on the docs site.

You can connect both. Use the GitBook server when you want answers grounded in the docs, and the Kapa.ai server when you want answers drawn from n8n's wider knowledge base.

Both servers use HTTP transport, so your AI tool needs to support remote MCP servers over HTTP. Neither supports stdio or SSE.

MCP server URLs[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#mcp-server-urls)

----------------------------------------------------------------------------------------------

Use the endpoint for the server you want:

Server

URL

GitBook docs server

`https://docs.n8n.io/~gitbook/mcp`

Kapa.ai server

`https://n8n.mcp.kapa.ai`

Connect your AI tool[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#connect-your-ai-tool)

--------------------------------------------------------------------------------------------------------

The steps differ by tool, but each one needs a server URL from above. The following examples set up both servers. To connect only one, keep the entry you want and remove the other.

The Kapa.ai server requires authentication. Your AI tool opens a browser-based sign-in flow when you first connect to it, or the first time you use it. Follow the prompts to approve the connection.

### Claude Code[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#claude-code)

Run these commands in your terminal:

Copy

    claude mcp add --transport http n8n-docs https://docs.n8n.io/~gitbook/mcp
    claude mcp add --transport http n8n-kapa https://n8n.mcp.kapa.ai

### Cursor[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#cursor)

Add the servers to your `mcp.json` file:

Copy

    {
    	"mcpServers": {
    		"n8n-docs": {
    			"url": "https://docs.n8n.io/~gitbook/mcp"
    		},
    		"n8n-kapa": {
    			"url": "https://n8n.mcp.kapa.ai"
    		}
    	}
    }

### VS Code[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#vs-code)

Add the servers to your `mcp.json` file:

Copy

    {
    	"servers": {
    		"n8n-docs": {
    			"type": "http",
    			"url": "https://docs.n8n.io/~gitbook/mcp"
    		},
    		"n8n-kapa": {
    			"type": "http",
    			"url": "https://n8n.mcp.kapa.ai"
    		}
    	}
    }

### Other tools[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#other-tools)

For any other MCP client, add a new remote (HTTP) server in its MCP settings and enter a server URL:

Copy

    https://docs.n8n.io/~gitbook/mcp
    https://n8n.mcp.kapa.ai

After you connect, your tool can search n8n's knowledge as you work.

The exact configuration steps and file locations vary between tools and versions. Check your tool's documentation for how it adds a remote MCP server. For more on the Kapa.ai server, see the [Kapa.ai MCP documentation](https://docs.kapa.ai/overview/build-with-ai)
.

Related resources[](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server#related-resources)

--------------------------------------------------------------------------------------------------

*   [Connect](https://docs.n8n.io/connect)
    
*   [n8n API](https://docs.n8n.io/connect/n8n-api)
    
*   [n8n CLI](https://docs.n8n.io/connect/n8n-cli)
    
*   [Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
    
*   [Create nodes](https://docs.n8n.io/connect/create-nodes)
    

[PreviousMCP server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
[NextCreate nodes](https://docs.n8n.io/connect/create-nodes)

Last updated 10 days ago

Was this helpful?
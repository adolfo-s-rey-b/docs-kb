For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient.md)
.

The MCP Client node is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)
 client that allows you to use the tools that are exposed by an external MCP server.

You can use the MCP Client node to use MCP tools as regular steps in a workflow.

If you want to use MCP tools as tools for an AI Agent, use the [MCP Client Tool node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
 instead.

**Credentials**

The MCP Client node supports [Bearer](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-bearer-auth)
, generic [header](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-header-auth)
, multiple headers, and [OAuth2](https://docs.n8n.io/integrations/builtin/credentials/mcp#using-oauth2)
 authentication methods.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient#node-parameters)

---------------------------------------------------------------------------------------------------------------------

Configure the node with the following parameters.

*   **Server Transport**: The transport protocol used by the MCP Server endpoint you want to connect to.
    
*   **MCP Endpoint URL**: The URL of the external MCP Server. For example, `https://mcp.notion.com/mcp`.
    
*   **Authentication**: The authentication method for authentication to your MCP server. The MCP Client node supports [bearer](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-bearer-auth)
    , generic [header](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-header-auth)
    , multiple headers, and [OAuth2](https://docs.n8n.io/integrations/builtin/credentials/mcp#using-oauth2)
     authentication. Select **None** to attempt to connect without authentication.
    
    *   **Multiple Headers Auth**: Use this when your MCP server requires more than one header, for example an API key and a username. Add each header as a **Name** and **Value** pair in the credential. You can add as many headers as you need.
        
    
*   **Tool**: Select the tool to use in the node. The list of tools is automatically fetched from the external MCP server.
    
*   **Input Mode**:
    
    *   **Manual**: Specify each tool parameter manually.
        
    *   **JSON**: Specify tool parameters as a JSON object. Use this mode for tools with nested parameters.
        
    

Options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient#options)

-----------------------------------------------------------------------------------------------------

*   **Convert to Binary**: Whether to convert images and audio to binary data. If false, images and audio are returned as base64 encoded strings.
    
*   **Timeout**: Time in milliseconds to wait for tool calls to finish.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------

[Browse MCP Client node documentation integration templates](https://n8n.io/integrations/mcp-client)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient#related-resources)

-------------------------------------------------------------------------------------------------------------------------

To use MCP tools with AI Agents, n8n has the [MCP Client Tool node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
.

n8n also has an [MCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)
 node that allows you to expose n8n tools to external AI Agents.

Refer to the [MCP documentation](https://modelcontextprotocol.io/introduction)
 and [MCP specification](https://modelcontextprotocol.io/specification/)
 for more details about the protocol, servers, and clients.

Refer to [LangChain's documentation on tools](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
 for more information about tools in LangChain.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousMarkdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown)
[NextMCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger)

Last updated 10 days ago

Was this helpful?
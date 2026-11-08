For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/mcp.md)
.

You can use these credentials to authenticate the following nodes:

*   [MCP Client Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/mcp#prerequisites)

----------------------------------------------------------------------------------------

You need an MCP server that supports OAuth2 authentication.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/mcp#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------

*   OAuth2
    

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/mcp#using-oauth2)

--------------------------------------------------------------------------------------

This credential extends n8n's generic [OAuth2 API credential](https://docs.n8n.io/integrations/builtin/credentials/httprequest#using-oauth2)
, with two additional fields for MCP's authorization flow:

*   **Use Dynamic Client Registration**: Turned on by default. When on, n8n automatically registers itself as an OAuth2 client with the MCP server ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591)
    ), so you don't need to manually create an app or paste in a Client ID and Client Secret. Turn this off if your MCP server doesn't support Dynamic Client Registration, or if you already have a Client ID and Client Secret from the server's own developer settings. In that case, fill in the standard OAuth2 fields (**Authorization URL**, **Access Token URL**, **Client ID**, **Client Secret**) as you would for any generic OAuth2 credential.
    
*   **Resource URL**: Optional. The exact protected resource URL required by the MCP server. Leave this empty to let n8n discover it automatically from the server.
    

**Having trouble with Dynamic Client Registration?**

If you see errors related to a mismatched or invalid redirect URI during the OAuth2 flow, double-check that your MCP server's Dynamic Client Registration endpoint is configured to accept n8n's OAuth Redirect URL exactly as shown in the credential.

[PreviousMautic credentials](https://docs.n8n.io/integrations/builtin/credentials/mautic)
[NextMedium credentials](https://docs.n8n.io/integrations/builtin/credentials/medium)

Last updated 10 days ago

Was this helpful?
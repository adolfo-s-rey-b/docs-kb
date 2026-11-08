For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api.md)
.

**Feature availability**

The n8n API is available on:

*   **n8n Cloud:** Starter, Pro, Enterprise
    
*   **Self-hosted:** All editions
    

It isn't available on the free trial.

Using n8n's public API, you can programmatically perform many of the same tasks as you can in the GUI. For supported POSTs, an [idempotency key](https://docs.n8n.io/connect/n8n-api/idempotency)
 returns the first successful response instead of running the request again.

n8n provides an [n8n API node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n)
 to access the API in your workflows.

In this section[](https://docs.n8n.io/connect/n8n-api#in-this-section)

-----------------------------------------------------------------------

*   [Authentication](https://docs.n8n.io/connect/n8n-api/authentication)
    : how to authenticate requests to the n8n API.
    
*   [Pagination](https://docs.n8n.io/connect/n8n-api/pagination)
    : paginate large result sets.
    
*   [Idempotency](https://docs.n8n.io/connect/n8n-api/idempotency)
    : retry a POST with an `Idempotency-Key` header.
    
*   [Use an API playground](https://docs.n8n.io/connect/n8n-api/use-an-api-playground)
    : try out the API in a built-in playground (self-hosted n8n only).
    
*   [Endpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)
    : the complete endpoint reference, generated from the OpenAPI specification.
    

Choose your interaction method[](https://docs.n8n.io/connect/n8n-api#choose-your-interaction-method)

-----------------------------------------------------------------------------------------------------

### REST API (this section)[](https://docs.n8n.io/connect/n8n-api#rest-api-this-section)

Interact with n8n directly using HTTP requests. Ideal for:

*   Custom integrations and applications
    
*   Language-agnostic HTTP calls
    
*   Direct REST API usage in workflows
    

### n8n CLI (recommended for developers)[](https://docs.n8n.io/connect/n8n-api#n8n-cli-recommended-for-developers)

Use [n8n CLI](https://docs.n8n.io/connect/n8n-cli)
 for a command-line experience. It wraps the public API and is a good fit for:

*   Command-line automation and scripting
    
*   CI/CD pipeline integration
    
*   AI agent integration (Claude Code, Cursor, etc.)
    
*   Developers who prefer CLI tools
    

Learn about REST APIs[](https://docs.n8n.io/connect/n8n-api#learn-about-rest-apis)

-----------------------------------------------------------------------------------

The API documentation assumes you are familiar with REST APIs. If you're not, these resources may be helpful:

*   [KnowledgeOwl's guide to working with APIs](https://support.knowledgeowl.com/help/working-with-apis)
    : a basic introduction, including examples of how to call REST APIs.
    
*   [IBM Cloud Learn Hub - What is an Application Programming Interface (API)](https://www.ibm.com/cloud/learn/api)
    : this gives a general, but technical, introduction to APIs.
    
*   [IBM Cloud Learn Hub - What is a REST API?](https://www.ibm.com/cloud/learn/rest-apis)
    : more detailed information about REST APIs.
    
*   [MDN web docs - An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
    : REST APIs work over HTTP and use HTTP verbs, or methods, to specify the action to perform.
    

**Use the API playground**

Trying out the API in the [playground](https://docs.n8n.io/connect/n8n-api/use-an-api-playground)
 can help you understand how APIs work. If you're worried about changing live data, consider setting up a test workflow, or test n8n instance, to explore safely.

Related resources[](https://docs.n8n.io/connect/n8n-api#related-resources)

---------------------------------------------------------------------------

*   [Connect](https://docs.n8n.io/connect)
    
*   [n8n CLI](https://docs.n8n.io/connect/n8n-cli)
    
*   [Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
    
*   [Connect to the n8n docs MCP server](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server)
    
*   [Create nodes](https://docs.n8n.io/connect/create-nodes)
    

[PreviousConnect](https://docs.n8n.io/connect)
[NextAuthentication](https://docs.n8n.io/connect/n8n-api/authentication)

Last updated 10 days ago

Was this helpful?
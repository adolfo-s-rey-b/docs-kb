For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node.md)
.

Variables for working with HTTP node requests and responses when using pagination.

Refer to [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 for guidance on using the HTTP node, including configuring pagination.

Refer to [HTTP Request node cookbook | Pagination](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination)
 for example pagination configurations.

**HTTP node only**

These variables are for use in expressions in the HTTP node. You can't use them in other nodes.

Variable

Description

`$pageCount`

The pagination count. Tracks how many pages the node has fetched.

`$request`

The request object sent by the HTTP node.

`$response`

The response object from the HTTP call. Includes `$response.body`, `$response.headers`, and `$response.statusCode`. The contents of `body` and `headers` depend on the data sent by the API.

Related resources[](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node#related-resources)

--------------------------------------------------------------------------------------------------------------

*   [Use built-in shortcuts](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
    
*   [JMESPath](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath)
    
*   [LangChain Code node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node)
    
*   [n8n metadata](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata)
    

[PreviousJMESPath](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath)
[NextLangChain Code node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node)

Last updated 10 days ago

Was this helpful?
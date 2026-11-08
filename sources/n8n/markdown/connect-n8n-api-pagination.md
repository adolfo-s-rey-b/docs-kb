For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/pagination.md)
.

The default page size is 100 results. You can change the page size limit. The maximum permitted size is 250.

When a response contains more than one page, it includes a cursor, which you can use to request the next pages.

For example, say you want to get all active workflows, 150 at a time.

Get the first page:

Copy

    # For a self-hosted n8n instance <a href="#for-a-self-hosted-n8n-instance" id="for-a-self-hosted-n8n-instance"></a>
    curl -X 'GET' \
      '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
      -H 'accept: application/json' \
      -H 'X-N8N-API-KEY: <your-api-key>'
    
    # For n8n Cloud <a href="#for-n8n-cloud" id="for-n8n-cloud"></a>
    curl -X 'GET' \
      '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
      -H 'accept: application/json' \
      -H 'X-N8N-API-KEY: <your-api-key>'

The response is in JSON format, and includes a `nextCursor` value. This is an example response.

Copy

    {
      "data": [\
        // The response contains an object for each workflow\
        {\
          // Workflow data\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

Then to request the next page:

Copy

    # For a self-hosted n8n instance <a href="#for-a-self-hosted-n8n-instance" id="for-a-self-hosted-n8n-instance"></a>
    curl -X 'GET' \
      '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
      -H 'accept: application/json'
    
    # For n8n Cloud <a href="#for-n8n-cloud" id="for-n8n-cloud"></a>
    curl -X 'GET' \
      '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
      -H 'accept: application/json'

Related resources[](https://docs.n8n.io/connect/n8n-api/pagination#related-resources)

--------------------------------------------------------------------------------------

*   [n8n API](https://docs.n8n.io/connect/n8n-api)
    
*   [Authentication](https://docs.n8n.io/connect/n8n-api/authentication)
    
*   [Idempotency](https://docs.n8n.io/connect/n8n-api/idempotency)
    
*   [Use an API playground](https://docs.n8n.io/connect/n8n-api/use-an-api-playground)
    
*   [Endpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)
    

[PreviousAuthentication](https://docs.n8n.io/connect/n8n-api/authentication)
[NextIdempotency](https://docs.n8n.io/connect/n8n-api/idempotency)

Last updated 10 days ago

Was this helpful?
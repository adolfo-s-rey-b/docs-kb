For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/discover.md)
.

Copy

On this page

API capability discovery

### Discover available API capabilities[](https://docs.n8n.io/connect/n8n-api/discover#get-discover)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/discover

Returns a filtered capability map based on the caller's API key scopes. Each resource includes the operations and endpoints accessible to the authenticated API key. Use query parameters to narrow the response.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

includestring · enumOptional

Include additional data. Use "schemas" to inline request body schemas per endpoint, eliminating the need to fetch the full OpenAPI spec.

Possible values: `schemas`

resourcestringOptional

Filter to a specific resource (e.g. "workflow", "tags", "credential").

operationstringOptional

Filter to endpoints with a specific operation (e.g. "read", "create", "list").

Responses

200

Operation successful.

application/json

dataobjectRequired

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

get/discover

HTTP

Copy

    GET /api/v1/discover HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": {
        "scopes": [\
          "text"\
        ],
        "resources": {
          "ANY_ADDITIONAL_PROPERTY": {
            "operations": [\
              "text"\
            ],
            "endpoints": [\
              {\
                "method": "text",\
                "path": "text",\
                "operationId": "text",\
                "requestSchema": {}\
              }\
            ]
          }
        },
        "filters": {
          "ANY_ADDITIONAL_PROPERTY": {
            "description": "text",
            "values": [\
              "text"\
            ]
          }
        },
        "specUrl": "text"
      }
    }

[PreviousData Table](https://docs.n8n.io/connect/n8n-api/data-table)
[NextEvaluation](https://docs.n8n.io/connect/n8n-api/evaluation)

Last updated 9 days ago

Was this helpful?
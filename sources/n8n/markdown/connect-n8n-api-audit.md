For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/audit.md)
.

Copy

On this page

Operations about security audit

### Generate an audit[](https://docs.n8n.io/connect/n8n-api/audit#post-audit)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/audit

Generate a security audit for your n8n instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

additionalOptionsobjectOptional

Show properties

Responses

200

Operation successful.

application/json

objectOptional

Show properties

or

any\[\]Optional

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

500

Internal server error.

post/audit

HTTP

Copy

    POST /api/v1/audit HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 78
    
    {
      "additionalOptions": {
        "daysAbandonedWorkflow": 1,
        "categories": [\
          "credentials"\
        ]
      }
    }

Test it

200

Operation successful.

Copy

    {
      "Credentials Risk Report": {
        "risk": "credentials",
        "sections": [\
          {\
            "title": "Credentials not used in any workflow",\
            "description": "These credentials are not used in any workflow. Keeping unused credentials in your instance is an unneeded security risk.",\
            "recommendation": "Consider deleting these credentials if you no longer need them.",\
            "location": [\
              {\
                "kind": "credential",\
                "id": "1",\
                "name": "My Test Account"\
              }\
            ]\
          }\
        ]
      },
      "Database Risk Report": {
        "risk": "database",
        "sections": [\
          {\
            "title": "Expressions in \"Execute Query\" fields in SQL nodes",\
            "description": "This SQL node has an expression in the \"Query\" field of an \"Execute Query\" operation. Building a SQL query with an expression may lead to a SQL injection attack.",\
            "recommendation": "Consider using the \"Query Parameters\" field to pass parameters to the query, or validating the input of the expression in the \"Query\" field.",\
            "location": [\
              {\
                "kind": "node",\
                "workflowId": "1",\
                "workflowName": "My Workflow",\
                "nodeId": "51eb5852-ce0b-4806-b4ff-e41322a4041a",\
                "nodeName": "MySQL",\
                "nodeType": "n8n-nodes-base.mySql"\
              }\
            ]\
          }\
        ]
      },
      "Filesystem Risk Report": {
        "risk": "filesystem",
        "sections": [\
          {\
            "title": "Nodes that interact with the filesystem",\
            "description": "This node reads from and writes to any accessible file in the host filesystem. Sensitive file content may be manipulated through a node operation.",\
            "recommendation": "Consider protecting any sensitive files in the host filesystem, or refactoring the workflow so that it does not require host filesystem interaction.",\
            "location": [\
              {\
                "kind": "node",\
                "workflowId": "1",\
                "workflowName": "My Workflow",\
                "nodeId": "51eb5852-ce0b-4806-b4ff-e41322a4041a",\
                "nodeName": "Ready Binary file",\
                "nodeType": "n8n-nodes-base.readBinaryFile"\
              }\
            ]\
          }\
        ]
      },
      "Nodes Risk Report": {
        "risk": "nodes",
        "sections": [\
          {\
            "title": "Community nodes",\
            "description": "This node is sourced from the community. Community nodes are not vetted by the n8n team and have full access to the host system.",\
            "recommendation": "Consider reviewing the source code in any community nodes installed in this n8n instance, and uninstalling any community nodes no longer used.",\
            "location": [\
              {\
                "kind": "community",\
                "nodeType": "n8n-nodes-test.test",\
                "packageUrl": "https://www.npmjs.com/package/n8n-nodes-test"\
              }\
            ]\
          }\
        ]
      },
      "Instance Risk Report": {
        "risk": "instance",
        "sections": [\
          {\
            "title": "Unprotected webhooks in instance",\
            "description": "These webhook nodes have the \"Authentication\" field set to \"None\" and are not directly connected to a node to validate the payload. Every unprotected webhook allows your workflow to be called by any third party who knows the webhook URL.",\
            "recommendation": "Consider setting the \"Authentication\" field to an option other than \"None\", or validating the payload with one of the following nodes.",\
            "location": [\
              {\
                "kind": "node",\
                "workflowId": "1",\
                "workflowName": "My Workflow",\
                "nodeId": "51eb5852-ce0b-4806-b4ff-e41322a4041a",\
                "nodeName": "Webhook",\
                "nodeType": "n8n-nodes-base.webhook"\
              }\
            ]\
          }\
        ]
      }
    }

[PreviousEndpoint reference](https://docs.n8n.io/connect/n8n-api/api-reference)
[NextCommunity Package](https://docs.n8n.io/connect/n8n-api/community-package)

Last updated 9 days ago

Was this helpful?
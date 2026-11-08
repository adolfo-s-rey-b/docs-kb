For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/variables.md)
.

Copy

On this page

Operations about variables

### Retrieve variables[](https://docs.n8n.io/connect/n8n-api/variables#get-variables)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/variables

Retrieve variables from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

projectIdstringOptionalExample: `VmwOO9HeTEj20kxM`

statestring · enumOptionalPossible values: `empty`

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

nextCursorstring · nullableRequired

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/variables

HTTP

Copy

    GET /api/v1/variables HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "text",\
          "key": "text",\
          "value": "test",\
          "type": "text",\
          "project": {\
            "id": "VmwOO9HeTEj20kxM",\
            "name": "Marketing",\
            "type": "team",\
            "icon": {\
              "type": "emoji",\
              "value": "text",\
              "color": "text"\
            },\
            "description": "Workflows the marketing team owns.",\
            "customTelemetryTags": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ],\
            "creatorId": "f9a2cbb8-0b1e-4b64-9c1c-0d5f5f1f2a3b",\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        }\
      ],
      "nextCursor": "text"
    }

### Create a variable[](https://docs.n8n.io/connect/n8n-api/variables#post-variables)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/variables

Create a variable in your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

idstringRead-onlyOptional

keystring · min: 1 · max: 50RequiredPattern: `^[A-Za-z_][A-Za-z0-9_]*$`

valuestring · max: 1000RequiredExample: `test`

typestringRead-onlyOptional

projectIdstring · max: 36OptionalExample: `VmwOO9HeTEj20kxM`

Responses

201

Operation successful.

No content

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

post/variables

HTTP

Copy

    POST /api/v1/variables HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 60
    
    {
      "key": "text",
      "value": "test",
      "projectId": "VmwOO9HeTEj20kxM"
    }

Test it

201

Operation successful.

No content

### Update a variable[](https://docs.n8n.io/connect/n8n-api/variables#put-variables-id)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/variables/{id}

Update a variable from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

idstringRequired

The ID of the variable.

Body

application/json

idstringRead-onlyOptional

keystring · min: 1 · max: 50RequiredPattern: `^[A-Za-z0-9_]+$`

valuestring · max: 1000RequiredExample: `test`

typestringRead-onlyOptional

projectIdstring · max: 36 · nullableOptionalExample: `VmwOO9HeTEj20kxM`

Responses

204

Operation successful.

No content

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

415

Unsupported media type.

put/variables/{id}

HTTP

Copy

    PUT /api/v1/variables/{id} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 60
    
    {
      "key": "text",
      "value": "test",
      "projectId": "VmwOO9HeTEj20kxM"
    }

Test it

204

Operation successful.

No content

### Delete a variable[](https://docs.n8n.io/connect/n8n-api/variables#delete-variables-id)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/variables/{id}

Delete a variable from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

idstringRequired

The ID of the variable.

Responses

204

Operation successful.

No content

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/variables/{id}

HTTP

Copy

    DELETE /api/v1/variables/{id} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

[PreviousUser](https://docs.n8n.io/connect/n8n-api/user)
[NextWorkflow](https://docs.n8n.io/connect/n8n-api/workflow)

Last updated 9 days ago

Was this helpful?
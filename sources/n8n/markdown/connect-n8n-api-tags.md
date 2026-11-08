For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/tags.md)
.

Copy

On this page

Operations about tags

### Retrieve all tags[](https://docs.n8n.io/connect/n8n-api/tags#get-tags)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/tags

Retrieve all tags from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

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

get/tags

HTTP

Copy

    GET /api/v1/tags HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Create a tag[](https://docs.n8n.io/connect/n8n-api/tags#post-tags)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/tags

Create a tag in your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

idstringRead-onlyOptionalExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyOptional

updatedAtstring · date-timeRead-onlyOptional

Responses

201

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

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

post/tags

HTTP

Copy

    POST /api/v1/tags HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 21
    
    {
      "name": "Production"
    }

Test it

201

Operation successful.

Copy

    {
      "id": "2tUt1wbLX592XDdX",
      "name": "Production",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Retrieves a tag[](https://docs.n8n.io/connect/n8n-api/tags#get-tags-tagid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/tags/{tagId}

Retrieves a tag.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

tagIdstringRequired

The ID of the tag.

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/tags/{tagId}

HTTP

Copy

    GET /api/v1/tags/{tagId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "2tUt1wbLX592XDdX",
      "name": "Production",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Update a tag[](https://docs.n8n.io/connect/n8n-api/tags#put-tags-tagid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/tags/{tagId}

Update a tag.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

tagIdstringRequired

The ID of the tag.

Body

application/json

idstringRead-onlyOptionalExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyOptional

updatedAtstring · date-timeRead-onlyOptional

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyOptional

updatedAtstring · date-timeRead-onlyOptional

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Conflict

415

Unsupported media type.

put/tags/{tagId}

HTTP

Copy

    PUT /api/v1/tags/{tagId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 21
    
    {
      "name": "Production"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "2tUt1wbLX592XDdX",
      "name": "Production",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Delete a tag[](https://docs.n8n.io/connect/n8n-api/tags#delete-tags-tagid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/tags/{tagId}

Deletes a tag.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

tagIdstringRequired

The ID of the tag.

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/tags/{tagId}

HTTP

Copy

    DELETE /api/v1/tags/{tagId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "2tUt1wbLX592XDdX",
      "name": "Production",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

[PreviousSource Control](https://docs.n8n.io/connect/n8n-api/source-control)
[NextUser](https://docs.n8n.io/connect/n8n-api/user)

Last updated 9 days ago

Was this helpful?
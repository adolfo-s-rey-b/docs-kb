For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/projects.md)
.

Copy

On this page

Operations about projects

### Retrieve projects[](https://docs.n8n.io/connect/n8n-api/projects#get-projects)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/projects

Retrieve projects from your instance.

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

Paginate through projects by setting the cursor parameter to a nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `eyJvZmZzZXQiOjEwMCwibGltaXQiOjEwMH0=`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/projects

HTTP

Copy

    GET /api/v1/projects HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
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
      ],
      "nextCursor": "eyJvZmZzZXQiOjEwMCwibGltaXQiOjEwMH0="
    }

### Create a project[](https://docs.n8n.io/connect/n8n-api/projects#post-projects)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/projects

Create a team project on your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · min: 1 · max: 255RequiredExample: `Marketing`

idstring · min: 1 · max: 36Optional

Project ID. The server generates an ID when omitted. An ID that is in use returns HTTP 409.

Example: `VmwOO9HeTEj20kxM`

iconobject · nullableOptional

Show properties

descriptionstring · max: 512 · nullableOptionalExample: `Workflows the marketing team owns.`

customTelemetryTagsobject\[\]Optional

Show properties

typestringRead-onlyOptional

Responses

201

Operation successful.

application/json

idstringRead-onlyRequiredExample: `VmwOO9HeTEj20kxM`

namestringRequiredExample: `Marketing`

typestring · enumRead-onlyRequiredExample: `team`Possible values: `personal``team`

iconobject · nullableRequired

Icon of the project, or null when the project has none

Show properties

descriptionstring · nullableRequiredExample: `Workflows the marketing team owns.`

customTelemetryTagsobject\[\]Required

Show properties

creatorIdstring · nullableRequiredExample: `f9a2cbb8-0b1e-4b64-9c1c-0d5f5f1f2a3b`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

rolestringRequired

The caller's role in the new project.

Example: `project:admin`

scopesstring\[\]Required

Scopes the caller holds in the new project.

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

A project with this ID exists already. The request does not change the existing project or its members.

415

Unsupported media type.

422

Unprocessable Entity

post/projects

HTTP

Copy

    POST /api/v1/projects HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 203
    
    {
      "name": "Marketing",
      "id": "VmwOO9HeTEj20kxM",
      "icon": {
        "type": "emoji",
        "value": "text",
        "color": "text"
      },
      "description": "Workflows the marketing team owns.",
      "customTelemetryTags": [\
        {\
          "key": "text",\
          "value": "text"\
        }\
      ]
    }

Test it

201

Operation successful.

Copy

    {
      "id": "VmwOO9HeTEj20kxM",
      "name": "Marketing",
      "type": "team",
      "icon": {
        "type": "emoji",
        "value": "text",
        "color": "text"
      },
      "description": "Workflows the marketing team owns.",
      "customTelemetryTags": [\
        {\
          "key": "text",\
          "value": "text"\
        }\
      ],
      "creatorId": "f9a2cbb8-0b1e-4b64-9c1c-0d5f5f1f2a3b",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "role": "project:admin",
      "scopes": [\
        "text"\
      ]
    }

### Update a project[](https://docs.n8n.io/connect/n8n-api/projects#put-projects-projectid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}

Update a project on your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

Body

application/json

namestring · min: 1 · max: 255RequiredExample: `Marketing`

idstringRead-onlyOptional

typestringRead-onlyOptional

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

put/projects/{projectId}

HTTP

Copy

    PUT /api/v1/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 20
    
    {
      "name": "Marketing"
    }

Test it

204

Operation successful.

No content

### Delete a project[](https://docs.n8n.io/connect/n8n-api/projects#delete-projects-projectid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}

Delete a project from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

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

delete/projects/{projectId}

HTTP

Copy

    DELETE /api/v1/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### List project members[](https://docs.n8n.io/connect/n8n-api/projects#get-projects-projectid-users)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/users

Returns a list of all members of a project including their role. Requires user:list scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

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

A project member (user with their role in the project).

Show properties

nextCursorstring · nullableRequired

Paginate through project members by setting the cursor parameter to the nextCursor attribute returned by a previous request. Default value fetches the first page of the collection.

Example: `eyJvZmZzZXQiOjEwMCwibGltaXQiOjEwMH0=`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/projects/{projectId}/users

HTTP

Copy

    GET /api/v1/projects/{projectId}/users HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "123e4567-e89b-12d3-a456-426614174000",\
          "email": "john.doe@company.com",\
          "firstName": "john",\
          "lastName": "Doe",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "role": "project:viewer"\
        }\
      ],
      "nextCursor": "eyJvZmZzZXQiOjEwMCwibGltaXQiOjEwMH0="
    }

### Add one or more users to a project[](https://docs.n8n.io/connect/n8n-api/projects#post-projects-projectid-users)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/users

Add one or more users to a project on your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

relationsobject\[\] · min: 1Required

A list of userIds and roles to add to the project.

Show properties

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

404

The specified resource was not found.

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/projects/{projectId}/users

HTTP

Copy

    POST /api/v1/projects/{projectId}/users HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 89
    
    {
      "relations": [\
        {\
          "userId": "91765f0d-3b29-45df-adb9-35b23937eb92",\
          "role": "project:viewer"\
        }\
      ]
    }

Test it

201

Operation successful.

No content

### Delete a user from a project[](https://docs.n8n.io/connect/n8n-api/projects#delete-projects-projectid-users-userid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/users/{userId}

Delete a user from a project on your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

userIdstringRequired

The ID of the user.

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

delete/projects/{projectId}/users/{userId}

HTTP

Copy

    DELETE /api/v1/projects/{projectId}/users/{userId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Change a user's role in a project[](https://docs.n8n.io/connect/n8n-api/projects#patch-projects-projectid-users-userid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/users/{userId}

Change a user's role in a project.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

userIdstringRequired

The ID of the user.

Body

application/json

rolestring · min: 1Required

The role assigned to the user in the project.

Example: `project:viewer`

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

patch/projects/{projectId}/users/{userId}

HTTP

Copy

    PATCH /api/v1/projects/{projectId}/users/{userId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 25
    
    {
      "role": "project:viewer"
    }

Test it

204

Operation successful.

No content

[PreviousNode Type Policy](https://docs.n8n.io/connect/n8n-api/node-type-policy)
[NextPromotions](https://docs.n8n.io/connect/n8n-api/promotions)

Last updated 9 days ago

Was this helpful?
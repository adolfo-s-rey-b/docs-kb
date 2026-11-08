For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/role.md)
.

Copy

On this page

Operations about roles

### Retrieve all roles[](https://docs.n8n.io/connect/n8n-api/role#get-roles)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/roles

Returns all roles grouped by type (global and project). Set `withUsageCount` to include how many users and projects use each role.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

withUsageCountstring · enumOptionalDefault: `false`Possible values: `true``false`

Responses

200

Operation successful.

application/json

globalobject\[\]Required

Show properties

projectobject\[\]Required

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/roles

HTTP

Copy

    GET /api/v1/roles HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "global": [\
        {\
          "slug": "text",\
          "displayName": "text",\
          "description": "text",\
          "systemRole": true,\
          "roleType": "global",\
          "scopes": [\
            "text"\
          ],\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "licensed": true,\
          "usedByUsers": 1,\
          "usedByProjects": 1\
        }\
      ],
      "project": [\
        {\
          "slug": "text",\
          "displayName": "text",\
          "description": "text",\
          "systemRole": true,\
          "roleType": "project",\
          "scopes": [\
            "text"\
          ],\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "licensed": true,\
          "usedByUsers": 1,\
          "usedByProjects": 1\
        }\
      ]
    }

### Create a custom role[](https://docs.n8n.io/connect/n8n-api/role#post-roles)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/roles

Creates a custom role. Set `roleType` to `global` for an instance-wide role or `project` for a project role.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

displayNamestring · min: 2 · max: 100Required

descriptionstring · max: 500Optional

roleTypestring · enumRequiredPossible values: `project``global`

scopesstring\[\]Required

Responses

201

Operation successful.

application/json

slugstringRequired

displayNamestringRequired

descriptionstring · nullableRequired

systemRolebooleanRequired

roleTypestring · enumRequiredPossible values: `project``global`

scopesstring\[\]Required

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

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

post/roles

HTTP

Copy

    POST /api/v1/roles HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 82
    
    {
      "displayName": "text",
      "description": "text",
      "roleType": "project",
      "scopes": [\
        "text"\
      ]
    }

Test it

201

Operation successful.

Copy

    {
      "slug": "text",
      "displayName": "text",
      "description": "text",
      "systemRole": true,
      "roleType": "project",
      "scopes": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Retrieve a role[](https://docs.n8n.io/connect/n8n-api/role#get-roles-roleslug)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/roles/{roleSlug}

Returns a single role with its scopes. Set `withUsageCount` to include how many users and projects use the role.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleSlugstringRequired

The slug of the role.

Query parameters

withUsageCountstring · enumOptionalDefault: `false`Possible values: `true``false`

Responses

200

Operation successful.

application/json

slugstringRequired

displayNamestringRequired

descriptionstring · nullableRequired

systemRolebooleanRequired

roleTypestring · enumRequiredPossible values: `project``global`

scopesstring\[\]Required

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

licensedbooleanRequired

usedByUsersnumberOptional

usedByProjectsnumberOptional

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/roles/{roleSlug}

HTTP

Copy

    GET /api/v1/roles/{roleSlug} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "slug": "text",
      "displayName": "text",
      "description": "text",
      "systemRole": true,
      "roleType": "project",
      "scopes": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "licensed": true,
      "usedByUsers": 1,
      "usedByProjects": 1
    }

### Update a custom role[](https://docs.n8n.io/connect/n8n-api/role#put-roles-roleslug)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/roles/{roleSlug}

Replaces a custom role's display name, description, and scopes. System roles cannot be updated.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleSlugstringRequired

The slug of the role.

Body

application/json

displayNamestring · min: 2 · max: 100Required

descriptionstring · max: 500 · nullableRequired

scopesstring\[\]Required

Responses

200

Operation successful.

application/json

slugstringRequired

displayNamestringRequired

descriptionstring · nullableRequired

systemRolebooleanRequired

roleTypestring · enumRequiredPossible values: `project``global`

scopesstring\[\]Required

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

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

put/roles/{roleSlug}

HTTP

Copy

    PUT /api/v1/roles/{roleSlug} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 61
    
    {
      "displayName": "text",
      "description": "text",
      "scopes": [\
        "text"\
      ]
    }

Test it

200

Operation successful.

Copy

    {
      "slug": "text",
      "displayName": "text",
      "description": "text",
      "systemRole": true,
      "roleType": "project",
      "scopes": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Delete a custom role[](https://docs.n8n.io/connect/n8n-api/role#delete-roles-roleslug)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/roles/{roleSlug}

Deletes a custom role. System roles cannot be deleted. A role with users assigned cannot be deleted unless `reassignRoleSlug` is set to move those users to another role first.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleSlugstringRequired

The slug of the role.

Query parameters

reassignRoleSlugany ofOptional

string · enumOptionalPossible values: `global:admin``global:member``global:chatUser`

or

string · min: 1Optional

Responses

200

Operation successful.

application/json

slugstringRequired

displayNamestringRequired

descriptionstring · nullableRequired

systemRolebooleanRequired

roleTypestring · enumRequiredPossible values: `project``global`

scopesstring\[\]Required

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/roles/{roleSlug}

HTTP

Copy

    DELETE /api/v1/roles/{roleSlug} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "slug": "text",
      "displayName": "text",
      "description": "text",
      "systemRole": true,
      "roleType": "project",
      "scopes": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

[PreviousPromotions](https://docs.n8n.io/connect/n8n-api/promotions)
[NextRole Mapping Rule](https://docs.n8n.io/connect/n8n-api/role-mapping-rule)

Last updated 9 days ago

Was this helpful?
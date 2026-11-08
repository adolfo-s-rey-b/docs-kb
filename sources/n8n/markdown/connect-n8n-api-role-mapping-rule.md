For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/role-mapping-rule.md)
.

Copy

On this page

Operations about identity-provider role-mapping rules

### Retrieve role-mapping rules[](https://docs.n8n.io/connect/n8n-api/role-mapping-rule#get-role-mapping-rules)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/role-mapping-rules

Returns the configured role-mapping rules. `order` is the rule's evaluation position within its own `type`, so instance and project rules each have their own sequence starting at 0 — filter by `type` to retrieve a single evaluation order.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

typestring · enumOptionalPossible values: `instance``project`

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

get/role-mapping-rules

HTTP

Copy

    GET /api/v1/role-mapping-rules HTTP/1.1
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
          "expression": "text",\
          "role": "text",\
          "type": "instance",\
          "order": 1,\
          "projectIds": [\
            "text"\
          ],\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Create a role-mapping rule[](https://docs.n8n.io/connect/n8n-api/role-mapping-rule#post-role-mapping-rules)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/role-mapping-rules

Creates a rule that maps an identity-provider claim expression to a role. Set `type` to `instance` for a rule granting a global role, or `project` for a rule granting a project role on the projects named in `projectIds`. Omitting `order` appends the rule to the end of the evaluation order for its type.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

expressionstring · min: 1Required

rolestring · min: 1 · max: 128Required

typestring · enumRequiredPossible values: `instance``project`

orderintegerOptional

projectIdsstring\[\]Optional

Responses

201

Operation successful.

application/json

idstringRequired

expressionstringRequired

rolestringRequired

typestring · enumRequiredPossible values: `instance``project`

orderintegerRequired

projectIdsstring\[\]Required

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

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/role-mapping-rules

HTTP

Copy

    POST /api/v1/role-mapping-rules HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 85
    
    {
      "expression": "text",
      "role": "text",
      "type": "instance",
      "order": 1,
      "projectIds": [\
        "text"\
      ]
    }

Test it

201

Operation successful.

Copy

    {
      "id": "text",
      "expression": "text",
      "role": "text",
      "type": "instance",
      "order": 1,
      "projectIds": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Move a role-mapping rule[](https://docs.n8n.io/connect/n8n-api/role-mapping-rule#post-role-mapping-rules-rolemappingruleid-move)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/role-mapping-rules/{roleMappingRuleId}/move

Changes a rule's position in the evaluation order for its type. `targetIndex` is the desired 0-based position within the rule's own `type` sequence; a value beyond the last position moves the rule to the end.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleMappingRuleIdstringRequired

The ID of the role mapping rule.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

targetIndexintegerRequired

Responses

200

Operation successful.

application/json

idstringRequired

expressionstringRequired

rolestringRequired

typestring · enumRequiredPossible values: `instance``project`

orderintegerRequired

projectIdsstring\[\]Required

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

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/role-mapping-rules/{roleMappingRuleId}/move

HTTP

Copy

    POST /api/v1/role-mapping-rules/{roleMappingRuleId}/move HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 17
    
    {
      "targetIndex": 1
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "expression": "text",
      "role": "text",
      "type": "instance",
      "order": 1,
      "projectIds": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Delete a role-mapping rule[](https://docs.n8n.io/connect/n8n-api/role-mapping-rule#delete-role-mapping-rules-rolemappingruleid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/role-mapping-rules/{roleMappingRuleId}

Deletes a role-mapping rule. The remaining rules of the same type close the gap, so their `order` values stay a contiguous sequence starting at 0.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleMappingRuleIdstringRequired

The ID of the role mapping rule.

Responses

200

Operation successful.

application/json

idstringRequired

expressionstringRequired

rolestringRequired

typestring · enumRequiredPossible values: `instance``project`

orderintegerRequired

projectIdsstring\[\]Required

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/role-mapping-rules/{roleMappingRuleId}

HTTP

Copy

    DELETE /api/v1/role-mapping-rules/{roleMappingRuleId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "expression": "text",
      "role": "text",
      "type": "instance",
      "order": 1,
      "projectIds": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Update a role-mapping rule[](https://docs.n8n.io/connect/n8n-api/role-mapping-rule#patch-role-mapping-rules-rolemappingruleid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/role-mapping-rules/{roleMappingRuleId}

Updates a rule's claim expression, role, and/or project assignments. A rule's type cannot be changed once created, so `type` isn't accepted here, and reordering is handled by the move endpoint.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

roleMappingRuleIdstringRequired

The ID of the role mapping rule.

Body

application/json

expressionstring · min: 1Optional

rolestring · min: 1 · max: 128Optional

projectIdsstring\[\]Optional

Responses

200

Operation successful.

application/json

idstringRequired

expressionstringRequired

rolestringRequired

typestring · enumRequiredPossible values: `instance``project`

orderintegerRequired

projectIdsstring\[\]Required

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

patch/role-mapping-rules/{roleMappingRuleId}

HTTP

Copy

    PATCH /api/v1/role-mapping-rules/{roleMappingRuleId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 57
    
    {
      "expression": "text",
      "role": "text",
      "projectIds": [\
        "text"\
      ]
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "expression": "text",
      "role": "text",
      "type": "instance",
      "order": 1,
      "projectIds": [\
        "text"\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

[PreviousRole](https://docs.n8n.io/connect/n8n-api/role)
[NextSecurity Policy](https://docs.n8n.io/connect/n8n-api/security-policy)

Last updated 9 days ago

Was this helpful?
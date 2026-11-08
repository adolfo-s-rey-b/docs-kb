For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/credential-type-policy.md)
.

Copy

On this page

Preview — breaking changes may still occur without major version bump.

### Preview: Retrieve the instance credential type policy[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#get-credential-type-policies-instance)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/instance

**Preview** — breaking changes may still occur without major version bump.

Returns the composed instance-scope policy: its default action and the rules of every attached policy document in evaluation order. An instance that was never configured reports `scopeId: null`, no rules, `defaultAction: allow`, and `version: 0`.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

scopeIdstring · nullableRequired

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny``delegate`

versionintegerRequired

401

Unauthorized

403

Forbidden

503

The requested service is temporarily unavailable.

get/credential-type-policies/instance

HTTP

Copy

    GET /api/v1/credential-type-policies/instance HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "scopeId": "text",
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1
    }

### Preview: Replace the instance credential type policy[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#put-credential-type-policies-instance)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/instance

**Preview** — breaking changes may still occur without major version bump.

Sets the instance default action and replaces the rules of its single policy document, creating both on first write. `version` must equal the version last read; a stale value is rejected with 409. Rule ids must be unique within the list.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny``delegate`

versionintegerRequired

Responses

200

Operation successful.

application/json

scopeIdstring · nullableRequired

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny``delegate`

versionintegerRequired

warningsone of\[\]Required

objectOptional

Show properties

or

objectOptional

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

503

The requested service is temporarily unavailable.

put/credential-type-policies/instance

HTTP

Copy

    PUT /api/v1/credential-type-policies/instance HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 120
    
    {
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1
    }

Test it

200

Operation successful.

Copy

    {
      "scopeId": "text",
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1,
      "warnings": [\
        {\
          "kind": "shadowed",\
          "ruleId": "text",\
          "shadowedByRuleId": "text"\
        }\
      ]
    }

### Preview: Retrieve a project's credential type policy[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#get-credential-type-policies-projects-projectid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/projects/{projectId}

**Preview** — breaking changes may still occur without major version bump.

Returns the project's own composed policy, not the result of combining it with the instance policy. A project that was never configured reports `scopeId: null`, no rules, `defaultAction: allow`, and `version: 0`.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

Responses

200

Operation successful.

application/json

scopeIdstring · nullableRequired

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny``delegate`

versionintegerRequired

401

Unauthorized

403

Forbidden

503

The requested service is temporarily unavailable.

get/credential-type-policies/projects/{projectId}

HTTP

Copy

    GET /api/v1/credential-type-policies/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "scopeId": "text",
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1
    }

### Preview: Replace a project's credential type policy[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#put-credential-type-policies-projects-projectid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/projects/{projectId}

**Preview** — breaking changes may still occur without major version bump.

Sets the project's default action and replaces the rules of its single policy document, creating both on first write. The `delegate` action is not accepted at project scope. `version` must equal the version last read; a stale value is rejected with 409, as is a project document that is shared with another scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

Body

application/json

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny`

versionintegerRequired

Responses

200

Operation successful.

application/json

scopeIdstring · nullableRequired

rulesobject\[\]Required

Show properties

defaultActionstring · enumRequiredPossible values: `allow``deny``delegate`

versionintegerRequired

warningsone of\[\]Required

objectOptional

Show properties

or

objectOptional

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

503

The requested service is temporarily unavailable.

put/credential-type-policies/projects/{projectId}

HTTP

Copy

    PUT /api/v1/credential-type-policies/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 120
    
    {
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1
    }

Test it

200

Operation successful.

Copy

    {
      "scopeId": "text",
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "defaultAction": "allow",
      "version": 1,
      "warnings": [\
        {\
          "kind": "shadowed",\
          "ruleId": "text",\
          "shadowedByRuleId": "text"\
        }\
      ]
    }

### Preview: List credential type policy documents[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#get-credential-type-policies-policies)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/policies

**Preview** — breaking changes may still occur without major version bump.

Returns a cursor-paginated list of reusable policy documents.

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

503

The requested service is temporarily unavailable.

get/credential-type-policies/policies

HTTP

Copy

    GET /api/v1/credential-type-policies/policies HTTP/1.1
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
          "kind": "text",\
          "rules": [\
            {\
              "id": "text",\
              "action": "allow",\
              "selector": {\
                "kind": "name",\
                "value": "text"\
              }\
            }\
          ],\
          "version": 1,\
          "updatedBy": "text",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Preview: Create a credential type policy document[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#post-credential-type-policies-policies)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/policies

**Preview** — breaking changes may still occur without major version bump.

Creates a reusable policy document that is not yet attached to any scope. Rule ids must be unique within the list. `warnings` lists rules that an earlier rule already shadows.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

rulesobject\[\]Required

Show properties

Responses

201

Operation successful.

application/json

policyobjectRequired

Show properties

warningsone of\[\]Required

objectOptional

Show properties

or

objectOptional

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

503

The requested service is temporarily unavailable.

post/credential-type-policies/policies

HTTP

Copy

    POST /api/v1/credential-type-policies/policies HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 84
    
    {
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ]
    }

Test it

201

Operation successful.

Copy

    {
      "policy": {
        "id": "text",
        "kind": "text",
        "rules": [\
          {\
            "id": "text",\
            "action": "allow",\
            "selector": {\
              "kind": "name",\
              "value": "text"\
            }\
          }\
        ],
        "version": 1,
        "updatedBy": "text",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "warnings": [\
        {\
          "kind": "shadowed",\
          "ruleId": "text",\
          "shadowedByRuleId": "text"\
        }\
      ]
    }

### Preview: Retrieve a credential type policy document[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#get-credential-type-policies-policies-policyid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/policies/{policyId}

**Preview** — breaking changes may still occur without major version bump.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

policyIdstringRequired

The ID of the credential type policy document.

Responses

200

Operation successful.

application/json

idstringRequired

kindstringRequired

rulesobject\[\]Required

Show properties

versionintegerRequired

updatedBystringRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/credential-type-policies/policies/{policyId}

HTTP

Copy

    GET /api/v1/credential-type-policies/policies/{policyId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "kind": "text",
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "version": 1,
      "updatedBy": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Preview: Replace the rules of a credential type policy document[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#put-credential-type-policies-policies-policyid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/policies/{policyId}

**Preview** — breaking changes may still occur without major version bump.

Replaces the document's whole rule list. `version` must equal the version last read; a stale value is rejected with 409. Every scope the document is attached to has its version bumped. A `delegate` rule is rejected when the document is attached to a project scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

policyIdstringRequired

The ID of the credential type policy document.

Body

application/json

rulesobject\[\]Required

Show properties

versionintegerRequired

Responses

200

Operation successful.

application/json

policyobjectRequired

Show properties

warningsone of\[\]Required

objectOptional

Show properties

or

objectOptional

Show properties

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

503

The requested service is temporarily unavailable.

put/credential-type-policies/policies/{policyId}

HTTP

Copy

    PUT /api/v1/credential-type-policies/policies/{policyId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 96
    
    {
      "rules": [\
        {\
          "id": "text",\
          "action": "allow",\
          "selector": {\
            "kind": "name",\
            "value": "text"\
          }\
        }\
      ],
      "version": 1
    }

Test it

200

Operation successful.

Copy

    {
      "policy": {
        "id": "text",
        "kind": "text",
        "rules": [\
          {\
            "id": "text",\
            "action": "allow",\
            "selector": {\
              "kind": "name",\
              "value": "text"\
            }\
          }\
        ],
        "version": 1,
        "updatedBy": "text",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "warnings": [\
        {\
          "kind": "shadowed",\
          "ruleId": "text",\
          "shadowedByRuleId": "text"\
        }\
      ]
    }

### Preview: Delete a credential type policy document[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#delete-credential-type-policies-policies-policyid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/policies/{policyId}

**Preview** — breaking changes may still occur without major version bump.

Deletes a policy document. A document that is still attached to a scope is rejected with 409; detach it first.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

policyIdstringRequired

The ID of the credential type policy document.

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

409

Conflict

503

The requested service is temporarily unavailable.

delete/credential-type-policies/policies/{policyId}

HTTP

Copy

    DELETE /api/v1/credential-type-policies/policies/{policyId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Preview: Retrieve a scope's attached policy documents[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#get-credential-type-policies-scopes-scopeid-attachments)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/scopes/{scopeId}/attachments

**Preview** — breaking changes may still occur without major version bump.

Returns every attached policy document and the scope version. Attachments use evaluation order: floor first, then priority ascending within each group. Use this version when replacing the attachments. `scopeId` comes from `GET /instance` or `GET /projects/{projectId}`, and is null until the scope is first written. This route needs instance-level access, also for a project scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

scopeIdstringRequired

The ID of the credential type policy scope.

Responses

200

Operation successful.

application/json

attachmentsobject\[\]Required

Show properties

versionintegerRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/credential-type-policies/scopes/{scopeId}/attachments

HTTP

Copy

    GET /api/v1/credential-type-policies/scopes/{scopeId}/attachments HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "attachments": [\
        {\
          "policyId": "text",\
          "rules": [\
            {\
              "id": "text",\
              "action": "allow",\
              "selector": {\
                "kind": "name",\
                "value": "text"\
              }\
            }\
          ],\
          "priority": 1,\
          "isFloor": true\
        }\
      ],
      "version": 1
    }

### Preview: Replace a scope's attached policy documents[](https://docs.n8n.io/connect/n8n-api/credential-type-policy#put-credential-type-policies-scopes-scopeid-attachments)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/credential-type-policies/scopes/{scopeId}/attachments

**Preview** — breaking changes may still occur without major version bump.

Replaces every attachment on a scope. `scopeId` comes from the scope's `GET` response once it has been written. Each `policyId` and each `(isFloor, priority)` pair must be unique within the list. `version` must match the current scope version. A stale version returns 409 without changes. A successful write bumps the scope's version.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

scopeIdstringRequired

The ID of the credential type policy scope.

Body

application/json

attachmentsobject\[\]Required

Show properties

versionintegerRequired

Responses

200

Operation successful.

application/json

attachmentsobject\[\]Required

Show properties

versionintegerRequired

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

503

The requested service is temporarily unavailable.

put/credential-type-policies/scopes/{scopeId}/attachments

HTTP

Copy

    PUT /api/v1/credential-type-policies/scopes/{scopeId}/attachments HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 77
    
    {
      "attachments": [\
        {\
          "policyId": "text",\
          "priority": 1,\
          "isFloor": true\
        }\
      ],
      "version": 1
    }

Test it

200

Operation successful.

Copy

    {
      "attachments": [\
        {\
          "policyId": "text",\
          "rules": [\
            {\
              "id": "text",\
              "action": "allow",\
              "selector": {\
                "kind": "name",\
                "value": "text"\
              }\
            }\
          ],\
          "priority": 1,\
          "isFloor": true\
        }\
      ],
      "version": 1
    }

[PreviousCredential](https://docs.n8n.io/connect/n8n-api/credential)
[NextData Table](https://docs.n8n.io/connect/n8n-api/data-table)

Last updated 9 days ago

Was this helpful?
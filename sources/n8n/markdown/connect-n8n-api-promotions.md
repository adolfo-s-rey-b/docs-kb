For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/promotions.md)
.

Copy

On this page

Operations about promotion providers, connections, and package operations

### List promotion providers[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-providers)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers

Returns a cursor-paginated list of providers, without their public configuration.

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

get/promotions/providers

HTTP

Copy

    GET /api/v1/promotions/providers HTTP/1.1
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
          "name": "text",\
          "type": "git",\
          "authType": "ssh-key",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Create a promotion provider[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-providers)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers

Creates a provider and its authentication material. A Git host provider validates authenticated API access before it saves. For GitLab, the service uses n8n as the Git transport username. Its auth.username is optional. The service ignores any supplied username. Plain Git token authentication requires auth.username. An SSH provider returns the generated public key; add it to the remote as a deploy key.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · min: 1 · max: 128Required

typestring · enumRequiredPossible values: `git``gitlab`

authone ofRequired

objectOptional

Show properties

or

objectOptional

Show properties

configobjectOptional

Show properties

Responses

201

Operation successful.

application/json

providerobjectRequired

Show properties

publicKeystring · nullableRequired

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

post/promotions/providers

HTTP

Copy

    POST /api/v1/promotions/providers HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 124
    
    {
      "name": "text",
      "type": "git",
      "auth": {
        "authType": "ssh-key",
        "keyType": "ed25519"
      },
      "config": {
        "schemaVersion": 1,
        "baseUrl": "text"
      }
    }

Test it

201

Operation successful.

Copy

    {
      "provider": {
        "id": "text",
        "name": "text",
        "type": "git",
        "authType": "ssh-key",
        "config": {
          "schemaVersion": 1,
          "publicKey": "text",
          "keyType": "ed25519"
        },
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "publicKey": "text"
    }

### Retrieve a promotion provider[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-providers-promotionproviderid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers/{promotionProviderId}

Returns the provider with its public configuration. Secrets are never returned.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionProviderIdstringRequired

The ID of the promotion provider.

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

typestring · enumRequiredPossible values: `git``gitlab`

authTypestring · enumRequiredPossible values: `ssh-key``token`

configany ofRequired

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

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

get/promotions/providers/{promotionProviderId}

HTTP

Copy

    GET /api/v1/promotions/providers/{promotionProviderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "git",
      "authType": "ssh-key",
      "config": {
        "schemaVersion": 1,
        "publicKey": "text",
        "keyType": "ed25519"
      },
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Update a promotion provider[](https://docs.n8n.io/connect/n8n-api/promotions#put-promotions-providers-promotionproviderid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers/{promotionProviderId}

Renames the provider, and replaces its credentials when `auth` is sent. A Git host provider can also update its base URL. A different API destination requires `auth` in the same request. Changed credentials and host settings are validated before they save. If another request changes the credentials or configuration before this update saves, the update returns 409. Reload the provider and try again. For GitLab, the service uses n8n as the Git transport username. Its auth.username is optional. The service ignores any supplied username. Plain Git token authentication requires auth.username. New credentials apply to every connection that uses this provider. The authentication method cannot change.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionProviderIdstringRequired

The ID of the promotion provider.

Body

application/json

namestring · min: 1 · max: 128Optional

authone ofOptional

objectOptional

Show properties

or

objectOptional

Show properties

configobjectOptional

Show properties

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

typestring · enumRequiredPossible values: `git``gitlab`

authTypestring · enumRequiredPossible values: `ssh-key``token`

configany ofRequired

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

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

503

The requested service is temporarily unavailable.

put/promotions/providers/{promotionProviderId}

HTTP

Copy

    PUT /api/v1/promotions/providers/{promotionProviderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 111
    
    {
      "name": "text",
      "auth": {
        "authType": "ssh-key",
        "keyType": "ed25519"
      },
      "config": {
        "schemaVersion": 1,
        "baseUrl": "text"
      }
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "git",
      "authType": "ssh-key",
      "config": {
        "schemaVersion": 1,
        "publicKey": "text",
        "keyType": "ed25519"
      },
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Delete a promotion provider[](https://docs.n8n.io/connect/n8n-api/promotions#delete-promotions-providers-promotionproviderid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers/{promotionProviderId}

A provider used by a connection cannot be deleted.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionProviderIdstringRequired

The ID of the promotion provider.

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

delete/promotions/providers/{promotionProviderId}

HTTP

Copy

    DELETE /api/v1/promotions/providers/{promotionProviderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### List repositories of a promotion provider[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-providers-promotionproviderid-repositories)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers/{promotionProviderId}/repositories

Lists repositories where the GitLab token identity has at least the Developer role. The token also needs Git write scope for promotions. Protected branches can restrict pushes. Use remoteUrl as a connection target. Search matches names and namespaces in similarity order. Unfiltered results use ascending repository ID order. The limit is an upper bound. GitLab returns at most 100 items per page. Follow nextCursor even when a page has fewer items than the requested limit. A saved connection is not required. Invalid credentials return an error, not an empty list. If a response is too large, restart the list with a smaller limit and no cursor.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionProviderIdstringRequired

The ID of the promotion provider.

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

searchstring · max: 255Optional

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

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/promotions/providers/{promotionProviderId}/repositories

HTTP

Copy

    GET /api/v1/promotions/providers/{promotionProviderId}/repositories HTTP/1.1
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
          "name": "text",\
          "fullPath": "text",\
          "remoteUrl": "text",\
          "defaultBranch": "text"\
        }\
      ],
      "nextCursor": "text"
    }

### List branches of a promotion repository[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-providers-promotionproviderid-repositories-repositoryid-branches)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/providers/{promotionProviderId}/repositories/{repositoryId}/branches

Lists branches of the selected GitLab repository and identifies its default branch. Pass the URL-encoded fullPath from repository discovery, or the repositoryPath of a saved GitLab connection, as repositoryId. GitLab project IDs are also accepted, but connections do not store them. Supports branch search and cursor pagination. The limit is an upper bound. GitLab returns at most 100 items per page. Follow nextCursor even when a page has fewer items than the requested limit. A saved connection is not required. Invalid credentials and inaccessible repositories return errors, not empty lists. If a response is too large, restart the list with a smaller limit and no cursor.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionProviderIdstringRequired

The ID of the promotion provider.

repositoryIdstring · min: 1 · max: 256Required

The URL-encoded fullPath of the repository. A GitLab project ID is also accepted.

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

searchstring · max: 255Optional

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

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/promotions/providers/{promotionProviderId}/repositories/{repositoryId}/branches

HTTP

Copy

    GET /api/v1/promotions/providers/{promotionProviderId}/repositories/{repositoryId}/branches HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "name": "text",\
          "isDefault": true\
        }\
      ],
      "nextCursor": "text"
    }

### List promotion connections[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-connections)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections

Returns a cursor-paginated list of connections with their configurations. Filter by `scope` for the instance connection, or by `providerId` to see which connections a provider edit affects.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

scopestring · enumOptionalPossible values: `instance``projects`

providerIdstring · min: 1 · max: 36Optional

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

get/promotions/connections

HTTP

Copy

    GET /api/v1/promotions/connections HTTP/1.1
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
          "name": "text",\
          "scope": "instance",\
          "target": {\
            "schemaVersion": 1,\
            "remoteUrl": "text",\
            "repositoryPath": "text"\
          },\
          "provider": {\
            "id": "text",\
            "name": "text",\
            "type": "git",\
            "authType": "ssh-key",\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          },\
          "configs": {\
            "apply": {\
              "id": "text",\
              "name": "text",\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z",\
              "settings": {\
                "schemaVersion": 1,\
                "branchName": "text"\
              }\
            },\
            "promote": {\
              "id": "text",\
              "name": "text",\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z",\
              "settings": {\
                "schemaVersion": 1,\
                "baseBranchName": "text",\
                "createBranchOnPromotion": true\
              }\
            }\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Create a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections

Creates a connection on an existing provider, with up to one initial configuration for each direction. A GitLab target URL must belong to the saved provider. The connection stores only the repository path and derives remoteUrl from the current provider base URL. Plain Git connections keep the full remote URL. Only one instance connection can exist.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · min: 1 · max: 128Required

scopestring · enumRequiredPossible values: `instance``projects`

providerIdstring · min: 1 · max: 36Required

targetobjectRequired

Show properties

configsobjectOptional

Show properties

Responses

201

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

scopestring · enumRequiredPossible values: `instance``projects`

targetobjectRequired

Show properties

providerobjectRequired

Show properties

configsobjectRequired

Show properties

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

503

The requested service is temporarily unavailable.

post/promotions/connections

HTTP

Copy

    POST /api/v1/promotions/connections HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 301
    
    {
      "name": "text",
      "scope": "instance",
      "providerId": "text",
      "target": {
        "schemaVersion": 1,
        "remoteUrl": "text"
      },
      "configs": {
        "apply": {
          "name": "text",
          "settings": {
            "schemaVersion": 1,
            "branchName": "text"
          }
        },
        "promote": {
          "name": "text",
          "settings": {
            "schemaVersion": 1,
            "baseBranchName": "text",
            "createBranchOnPromotion": true
          }
        }
      }
    }

Test it

201

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "scope": "instance",
      "target": {
        "schemaVersion": 1,
        "remoteUrl": "text",
        "repositoryPath": "text"
      },
      "provider": {
        "id": "text",
        "name": "text",
        "type": "git",
        "authType": "ssh-key",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "configs": {
        "apply": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "branchName": "text"
          }
        },
        "promote": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "baseBranchName": "text",
            "createBranchOnPromotion": true
          }
        }
      },
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Retrieve a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-connections-promotionconnectionid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}

Returns the connection with its provider summary and its configurations.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

scopestring · enumRequiredPossible values: `instance``projects`

targetobjectRequired

Show properties

providerobjectRequired

Show properties

configsobjectRequired

Show properties

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

get/promotions/connections/{promotionConnectionId}

HTTP

Copy

    GET /api/v1/promotions/connections/{promotionConnectionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "scope": "instance",
      "target": {
        "schemaVersion": 1,
        "remoteUrl": "text",
        "repositoryPath": "text"
      },
      "provider": {
        "id": "text",
        "name": "text",
        "type": "git",
        "authType": "ssh-key",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "configs": {
        "apply": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "branchName": "text"
          }
        },
        "promote": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "baseBranchName": "text",
            "createBranchOnPromotion": true
          }
        }
      },
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Update a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#put-promotions-connections-promotionconnectionid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}

Updates the name, target, or provider. A target replaces the whole saved target. GitLab connections store a repository path and derive remoteUrl from the provider. Plain Git connections keep the full remote URL. If the provider changes during a target or provider update, the update returns 409. Reload the connection and try again. Scope cannot change, and configurations have their own routes.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Body

application/json

namestring · min: 1 · max: 128Optional

targetobjectOptional

Show properties

providerIdstring · min: 1 · max: 36Optional

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

scopestring · enumRequiredPossible values: `instance``projects`

targetobjectRequired

Show properties

providerobjectRequired

Show properties

configsobjectRequired

Show properties

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

503

The requested service is temporarily unavailable.

put/promotions/connections/{promotionConnectionId}

HTTP

Copy

    PUT /api/v1/promotions/connections/{promotionConnectionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 83
    
    {
      "name": "text",
      "target": {
        "schemaVersion": 1,
        "remoteUrl": "text"
      },
      "providerId": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "scope": "instance",
      "target": {
        "schemaVersion": 1,
        "remoteUrl": "text",
        "repositoryPath": "text"
      },
      "provider": {
        "id": "text",
        "name": "text",
        "type": "git",
        "authType": "ssh-key",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      },
      "configs": {
        "apply": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "branchName": "text"
          }
        },
        "promote": {
          "id": "text",
          "name": "text",
          "createdAt": "2026-01-01T00:00:00.000Z",
          "updatedAt": "2026-01-01T00:00:00.000Z",
          "checkout": {
            "hasCheckout": true,
            "matchesConfig": true
          },
          "settings": {
            "schemaVersion": 1,
            "baseBranchName": "text",
            "createBranchOnPromotion": true
          }
        }
      },
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Delete a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#delete-promotions-connections-promotionconnectionid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}

Deletes the connection with its configurations, project links, and local checkouts. Its provider is kept.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

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

503

The requested service is temporarily unavailable.

delete/promotions/connections/{promotionConnectionId}

HTTP

Copy

    DELETE /api/v1/promotions/connections/{promotionConnectionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Create or replace the Apply configuration[](https://docs.n8n.io/connect/n8n-api/promotions#put-promotions-connections-promotionconnectionid-configs-apply)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/configs/apply

Replaces the whole configuration, so an omitted name resets it to "Apply". Answers 200 whether it created or replaced.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Body

application/json

namestring · min: 1 · max: 128Optional

settingsobjectRequired

Show properties

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

checkoutobjectRequired

Show properties

settingsobjectRequired

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

put/promotions/connections/{promotionConnectionId}/configs/apply

HTTP

Copy

    PUT /api/v1/promotions/connections/{promotionConnectionId}/configs/apply HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 66
    
    {
      "name": "text",
      "settings": {
        "schemaVersion": 1,
        "branchName": "text"
      }
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "checkout": {
        "hasCheckout": true,
        "matchesConfig": true
      },
      "settings": {
        "schemaVersion": 1,
        "branchName": "text"
      }
    }

### Create or replace the Promote configuration[](https://docs.n8n.io/connect/n8n-api/promotions#put-promotions-connections-promotionconnectionid-configs-promote)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/configs/promote

Replaces the whole configuration, so an omitted name resets it to "Promote" and `createBranchOnPromotion` is always required. Answers 200 whether it created or replaced.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Body

application/json

namestring · min: 1 · max: 128Optional

settingsobjectRequired

Show properties

Responses

200

Operation successful.

application/json

idstring · min: 1 · max: 36Required

namestringRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

checkoutobjectRequired

Show properties

settingsobjectRequired

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

put/promotions/connections/{promotionConnectionId}/configs/promote

HTTP

Copy

    PUT /api/v1/promotions/connections/{promotionConnectionId}/configs/promote HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 101
    
    {
      "name": "text",
      "settings": {
        "schemaVersion": 1,
        "baseBranchName": "text",
        "createBranchOnPromotion": true
      }
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "checkout": {
        "hasCheckout": true,
        "matchesConfig": true
      },
      "settings": {
        "schemaVersion": 1,
        "baseBranchName": "text",
        "createBranchOnPromotion": true
      }
    }

### Remove one direction[](https://docs.n8n.io/connect/n8n-api/promotions#delete-promotions-connections-promotionconnectionid-configs-direction)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/configs/{direction}

Deletes the configuration and its local checkout. Nothing in Git changes.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

directionstring · enumRequired

The direction of the promotion: apply or promote.

Possible values: `apply``promote`

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

503

The requested service is temporarily unavailable.

delete/promotions/connections/{promotionConnectionId}/configs/{direction}

HTTP

Copy

    DELETE /api/v1/promotions/connections/{promotionConnectionId}/configs/{direction} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Clone one direction's repository[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-direction-clone)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/{direction}/clone

Clones the configured branch into local storage on the instance that handles the request. Safe to call repeatedly. Cloning one direction does not make the other ready.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

directionstring · enumRequired

The direction of the promotion: apply or promote.

Possible values: `apply``promote`

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Responses

200

Operation successful.

application/json

connectionIdstring · min: 1 · max: 36Required

configIdstring · min: 1 · max: 36Required

directionstring · enumRequiredPossible values: `apply``promote`

branchNamestringRequired

hasCheckoutbooleanRequired

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/{direction}/clone

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/{direction}/clone HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "direction": "apply",
      "branchName": "text",
      "hasCheckout": true
    }

### Remove one direction's local checkout[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-direction-disconnect)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/{direction}/disconnect

Removes the local checkout and keeps the configuration, its credentials, and the trusted SSH host keys.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

directionstring · enumRequired

The direction of the promotion: apply or promote.

Possible values: `apply``promote`

Responses

200

Operation successful.

application/json

connectionIdstring · min: 1 · max: 36Required

configIdstring · min: 1 · max: 36Required

directionstring · enumRequiredPossible values: `apply``promote`

branchNamestringRequired

hasCheckoutbooleanRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/{direction}/disconnect

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/{direction}/disconnect HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "direction": "apply",
      "branchName": "text",
      "hasCheckout": true
    }

### List projects linked to a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-connections-promotionconnectionid-projects)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/projects

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Responses

200

Operation successful.

application/json

projectIdsstring\[\]Required

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/promotions/connections/{promotionConnectionId}/projects

HTTP

Copy

    GET /api/v1/promotions/connections/{promotionConnectionId}/projects HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "projectIds": [\
        "text"\
      ]
    }

### Link a project to a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-projects-projectid)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/projects/{projectId}

Links a team project to a project-scoped connection. A project can be linked to only one connection.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

projectIdstringRequired

The ID of the project.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Responses

200

Operation successful.

application/json

projectIdstring · min: 1 · max: 36Required

connectionIdstring · min: 1 · max: 36Required

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/projects/{projectId}

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "projectId": "text",
      "connectionId": "text"
    }

### Unlink a project from a promotion connection[](https://docs.n8n.io/connect/n8n-api/promotions#delete-promotions-connections-promotionconnectionid-projects-projectid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/projects/{projectId}

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

projectIdstringRequired

The ID of the project.

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

delete/promotions/connections/{promotionConnectionId}/projects/{projectId}

HTTP

Copy

    DELETE /api/v1/promotions/connections/{promotionConnectionId}/projects/{projectId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Promote all team projects[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-promote)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/promote

Exports every team project, commits it, and pushes to the configured base branch or a new timestamped branch. The response reports the target branch in `git.branchName`. Personal projects are ignored. Requires the Promote direction to be cloned first, and is available on the instance connection only. The API key also needs variable:list when the workflows reference variables.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

commitMessagestring · min: 1 · max: 1000Required

forcebooleanOptional

Responses

200

Operation successful.

application/json

connectionIdstring · min: 1 · max: 36Required

configIdstring · min: 1 · max: 36Required

countsobjectRequired

Show properties

gitobjectRequired

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/promote

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/promote HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 37
    
    {
      "commitMessage": "text",
      "force": true
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "counts": {
        "workflows": 1,
        "folders": 1,
        "credentials": 1,
        "dataTables": 1,
        "variables": 1,
        "tags": 1
      },
      "git": {
        "commitSha": "text",
        "branchName": "text"
      }
    }

### Apply a package to the instance[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-apply)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/apply

Checks the full package at the configured branch tip. Optionally send expectedSource with the configId, branchName, and full commitSha from the reviewed change preview; status `source-changed` means the branch moved since that review and nothing was imported. Returns status `blocked` before import writes if bindings need setup or if the apply would delete team projects that the package does not hold. Retain configId and git for Continue. Status `applied` includes counts and warnings. Inspect status before reading counts. Existing target variable values, including empty strings, are preserved. Requires a cloned Apply direction on an instance connection. The API key needs the gitConnection:pull scope. The importer checks user write permissions; granular API-key write scopes are not passed to it.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

expectedSourceobjectOptional

Show properties

Responses

200

Operation successful.

application/json

objectOptional

Show properties

or

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/apply

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/apply HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 77
    
    {
      "expectedSource": {
        "configId": "text",
        "branchName": "text",
        "commitSha": "text"
      }
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "git": {
        "commitSha": "text",
        "branchName": "text"
      },
      "status": "applied",
      "counts": {
        "projects": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "deleted": 1
        },
        "folders": {
          "created": 1,
          "skipped": 1,
          "removed": 1
        },
        "workflows": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "archived": 1,
          "deleted": 1,
          "publishing": {
            "published": 1,
            "unpublished": 1,
            "unchanged": 1,
            "blocked": 1,
            "failed": 1
          }
        },
        "credentials": {
          "matched": 1,
          "stubbed": 1
        },
        "dataTables": {
          "matched": 1,
          "created": 1,
          "updated": 1
        },
        "variables": {
          "matched": 1,
          "created": 1,
          "updated": 1,
          "stubbed": 1,
          "missing": 1
        },
        "tags": {
          "matched": 1,
          "created": 1,
          "renamed": 1,
          "reconciled": 1,
          "skipped": 1
        }
      },
      "warnings": [\
        {\
          "kind": "variable",\
          "code": "variable-shadowed",\
          "name": "text",\
          "scope": {\
            "kind": "global"\
          },\
          "consumers": [\
            {\
              "project": {\
                "id": "text",\
                "name": "text"\
              },\
              "workflows": [\
                {\
                  "id": "text",\
                  "name": "text"\
                }\
              ]\
            }\
          ]\
        }\
      ]
    }

### Continue Apply after binding setup[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-connections-promotionconnectionid-apply-continue)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/connections/{promotionConnectionId}/apply/continue

Rechecks the configured source and current target bindings. Send expectedSource with the configId, branchName, and full commitSha from the reviewed Apply result. Send `confirmDestructiveChanges: true` to also apply destructive data table changes and delete the reported team projects. Status `source-changed` requires a new Apply review. Status `blocked` returns fresh binding details without import writes. Status `applied` includes counts and warnings. Inspect status before reading counts. Existing target variable values are preserved. Requires the same cloned instance connection and permissions as Apply. The importer checks user write permissions; granular API-key write scopes are not passed to it. No server session or exactly-once guarantee is provided.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

promotionConnectionIdstringRequired

The ID of the promotion connection.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

expectedSourceobjectRequired

Show properties

confirmDestructiveChangesbooleanOptional

Also applies destructive data table changes, which a `destructive-change` conflict reports: removed or retyped columns. The values in those columns are removed. Rows and other columns are kept. On a full apply, also deletes the team projects that a `project-deletion` conflict reports, with everything in them. The confirmation covers every such change and deletion when Continue runs, including those that are not in the reviewed result.

Responses

200

Operation successful.

application/json

objectOptional

Show properties

or

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/connections/{promotionConnectionId}/apply/continue

HTTP

Copy

    POST /api/v1/promotions/connections/{promotionConnectionId}/apply/continue HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 110
    
    {
      "expectedSource": {
        "configId": "text",
        "branchName": "text",
        "commitSha": "text"
      },
      "confirmDestructiveChanges": true
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "git": {
        "commitSha": "text",
        "branchName": "text"
      },
      "status": "applied",
      "counts": {
        "projects": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "deleted": 1
        },
        "folders": {
          "created": 1,
          "skipped": 1,
          "removed": 1
        },
        "workflows": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "archived": 1,
          "deleted": 1,
          "publishing": {
            "published": 1,
            "unpublished": 1,
            "unchanged": 1,
            "blocked": 1,
            "failed": 1
          }
        },
        "credentials": {
          "matched": 1,
          "stubbed": 1
        },
        "dataTables": {
          "matched": 1,
          "created": 1,
          "updated": 1
        },
        "variables": {
          "matched": 1,
          "created": 1,
          "updated": 1,
          "stubbed": 1,
          "missing": 1
        },
        "tags": {
          "matched": 1,
          "created": 1,
          "renamed": 1,
          "reconciled": 1,
          "skipped": 1
        }
      },
      "warnings": [\
        {\
          "kind": "variable",\
          "code": "variable-shadowed",\
          "name": "text",\
          "scope": {\
            "kind": "global"\
          },\
          "consumers": [\
            {\
              "project": {\
                "id": "text",\
                "name": "text"\
              },\
              "workflows": [\
                {\
                  "id": "text",\
                  "name": "text"\
                }\
              ]\
            }\
          ]\
        }\
      ]
    }

### List the changes of a project in one direction[](https://docs.n8n.io/connect/n8n-api/promotions#get-promotions-projects-projectid-changes-direction)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/projects/{projectId}/changes/{direction}

Compares a team project on this instance with the branch of its promotion configuration and lists the workflows that differ. For `promote` the rows are what a promotion sends to the branch, and the key needs the gitConnection:push scope. For `apply` the rows are what applying the branch changes on this instance, and the key needs the gitConnection:pull scope. `commitSha` is the commit the rows were read from. Requires the direction to be cloned first.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

directionstring · enumRequired

The direction of the promotion: apply or promote.

Possible values: `apply``promote`

Query parameters

searchstringOptional

sortstring · enumOptionalDefault: `name`Possible values: `name``updatedAt``status`

orderstring · enumOptionalDefault: `asc`Possible values: `asc``desc`

Responses

200

Operation successful.

application/json

commitShastring · nullableRequired

sourceobjectRequired

Show properties

changesobject\[\]Required

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

503

The requested service is temporarily unavailable.

get/promotions/projects/{projectId}/changes/{direction}

HTTP

Copy

    GET /api/v1/promotions/projects/{projectId}/changes/{direction} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "commitSha": "text",
      "source": {
        "configId": "text",
        "branchName": "text"
      },
      "changes": [\
        {\
          "id": "text",\
          "name": "text",\
          "type": "workflow",\
          "status": "new",\
          "version": 1,\
          "updatedAt": "text",\
          "updatedBy": "text",\
          "dependencyCount": 1\
        }\
      ]
    }

### Promote a selection of a project's workflows[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-projects-projectid-promote)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/projects/{projectId}/promote

Promotes a chosen set of a team project's workflows to the Promote branch of the project's promotion configuration. Send workflow ids only; the server reads each one now, so the push carries the current state. Live and archived workflows the project owns are exported, so an archived id stays on the branch as archived; an id the project no longer owns (its workflow is gone, or moved to another project) leaves the branch, matching the project's change list. A deletion the branch does not hold under this project rejects the whole request before any write. Requires the Promote direction to be cloned first, and a promotion connection to resolve for the project (its own connection, otherwise the instance connection). The API key also needs variable:list when the workflows reference variables.

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

workflowIdsstring\[\] · min: 1Required

commitMessagestring · min: 1 · max: 1000Optional

Message for the promotion commit. A default is used when omitted.

Responses

200

Operation successful.

application/json

connectionIdstring · min: 1 · max: 36Required

configIdstring · min: 1 · max: 36Required

countsobjectRequired

Show properties

gitobjectRequired

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/projects/{projectId}/promote

HTTP

Copy

    POST /api/v1/promotions/projects/{projectId}/promote HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 47
    
    {
      "workflowIds": [\
        "text"\
      ],
      "commitMessage": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "counts": {
        "workflows": 1,
        "folders": 1,
        "credentials": 1,
        "dataTables": 1,
        "variables": 1,
        "tags": 1
      },
      "git": {
        "commitSha": "text",
        "branchName": "text"
      }
    }

### Apply a selection of a project's workflows[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-projects-projectid-apply)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/projects/{projectId}/apply

Applies selected workflow changes from the project's Apply branch. Send the selected change-list IDs in workflowIds. The server imports IDs present on the branch for this project. It removes instance workflows owned by this project when their IDs are absent from the branch. Duplicate or invalid IDs reject the whole request. Unselected content stays unchanged. Optionally send expectedSource with the configId, branchName, and full commitSha from the reviewed change preview. Status `source-changed` means the source changed since that review and nothing was imported. Status `blocked` returns binding details before import writes when the selection needs binding setup. Retain configId and git for Continue. Status `applied` includes counts and warnings. Inspect status before reading counts. Requires a cloned Apply direction for the project's resolved promotion connection. The API key needs the gitConnection:pull scope. The importer checks user write permissions.

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

workflowIdsstring\[\] · min: 1Required

expectedSourceobjectOptional

Show properties

Responses

200

Operation successful.

application/json

objectOptional

Show properties

or

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/projects/{projectId}/apply

HTTP

Copy

    POST /api/v1/promotions/projects/{projectId}/apply HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 100
    
    {
      "workflowIds": [\
        "text"\
      ],
      "expectedSource": {
        "configId": "text",
        "branchName": "text",
        "commitSha": "text"
      }
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "git": {
        "commitSha": "text",
        "branchName": "text"
      },
      "status": "applied",
      "counts": {
        "projects": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "deleted": 1
        },
        "folders": {
          "created": 1,
          "skipped": 1,
          "removed": 1
        },
        "workflows": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "archived": 1,
          "deleted": 1,
          "publishing": {
            "published": 1,
            "unpublished": 1,
            "unchanged": 1,
            "blocked": 1,
            "failed": 1
          }
        },
        "credentials": {
          "matched": 1,
          "stubbed": 1
        },
        "dataTables": {
          "matched": 1,
          "created": 1,
          "updated": 1
        },
        "variables": {
          "matched": 1,
          "created": 1,
          "updated": 1,
          "stubbed": 1,
          "missing": 1
        },
        "tags": {
          "matched": 1,
          "created": 1,
          "renamed": 1,
          "reconciled": 1,
          "skipped": 1
        }
      },
      "warnings": [\
        {\
          "kind": "variable",\
          "code": "variable-shadowed",\
          "name": "text",\
          "scope": {\
            "kind": "global"\
          },\
          "consumers": [\
            {\
              "project": {\
                "id": "text",\
                "name": "text"\
              },\
              "workflows": [\
                {\
                  "id": "text",\
                  "name": "text"\
                }\
              ]\
            }\
          ]\
        }\
      ]
    }

### Continue applying a selection after binding setup[](https://docs.n8n.io/connect/n8n-api/promotions#post-promotions-projects-projectid-apply-continue)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/promotions/projects/{projectId}/apply/continue

Rechecks the project's Apply source and the current bindings for the selection. Resend the full selection in workflowIds. Send the required expectedSource with the configId, branchName, and full commitSha from the reviewed Apply result. Send `confirmDestructiveChanges: true` to also apply destructive data table changes. The server does not keep a session. Status `source-changed` requires a new Apply review. Status `blocked` returns fresh binding details before import writes. Status `applied` includes counts and warnings. Inspect status before reading counts. Unselected content stays unchanged. Requires the same cloned Apply direction and permissions as the initial selection apply. The API key needs the gitConnection:pull scope. The importer checks user write permissions.

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

workflowIdsstring\[\] · min: 1Required

expectedSourceobjectRequired

Show properties

confirmDestructiveChangesbooleanOptional

Also applies destructive data table changes, which a `destructive-change` conflict reports: removed or retyped columns. The values in those columns are removed. Rows and other columns are kept. On a full apply, also deletes the team projects that a `project-deletion` conflict reports, with everything in them. The confirmation covers every such change and deletion when Continue runs, including those that are not in the reviewed result.

Responses

200

Operation successful.

application/json

objectOptional

Show properties

or

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

422

Unprocessable Entity

503

The requested service is temporarily unavailable.

post/promotions/projects/{projectId}/apply/continue

HTTP

Copy

    POST /api/v1/promotions/projects/{projectId}/apply/continue HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 133
    
    {
      "workflowIds": [\
        "text"\
      ],
      "expectedSource": {
        "configId": "text",
        "branchName": "text",
        "commitSha": "text"
      },
      "confirmDestructiveChanges": true
    }

Test it

200

Operation successful.

Copy

    {
      "connectionId": "text",
      "configId": "text",
      "git": {
        "commitSha": "text",
        "branchName": "text"
      },
      "status": "applied",
      "counts": {
        "projects": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "deleted": 1
        },
        "folders": {
          "created": 1,
          "skipped": 1,
          "removed": 1
        },
        "workflows": {
          "created": 1,
          "updated": 1,
          "skipped": 1,
          "archived": 1,
          "deleted": 1,
          "publishing": {
            "published": 1,
            "unpublished": 1,
            "unchanged": 1,
            "blocked": 1,
            "failed": 1
          }
        },
        "credentials": {
          "matched": 1,
          "stubbed": 1
        },
        "dataTables": {
          "matched": 1,
          "created": 1,
          "updated": 1
        },
        "variables": {
          "matched": 1,
          "created": 1,
          "updated": 1,
          "stubbed": 1,
          "missing": 1
        },
        "tags": {
          "matched": 1,
          "created": 1,
          "renamed": 1,
          "reconciled": 1,
          "skipped": 1
        }
      },
      "warnings": [\
        {\
          "kind": "variable",\
          "code": "variable-shadowed",\
          "name": "text",\
          "scope": {\
            "kind": "global"\
          },\
          "consumers": [\
            {\
              "project": {\
                "id": "text",\
                "name": "text"\
              },\
              "workflows": [\
                {\
                  "id": "text",\
                  "name": "text"\
                }\
              ]\
            }\
          ]\
        }\
      ]
    }

[PreviousProjects](https://docs.n8n.io/connect/n8n-api/projects)
[NextRole](https://docs.n8n.io/connect/n8n-api/role)

Last updated 9 days ago

Was this helpful?
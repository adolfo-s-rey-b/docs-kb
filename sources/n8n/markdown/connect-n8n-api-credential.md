For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/credential.md)
.

Copy

On this page

Operations about credentials

### List credentials[](https://docs.n8n.io/connect/n8n-api/credential#get-credentials)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials

Retrieve all credentials from your instance. Only available for the instance owner and admin. Credential data (secrets) is not included.

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

get/credentials

HTTP

Copy

    GET /api/v1/credentials HTTP/1.1
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
          "type": "text",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "shared": [\
            {\
              "id": "text",\
              "name": "text",\
              "role": "text",\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z"\
            }\
          ]\
        }\
      ],
      "nextCursor": "text"
    }

### Create a credential[](https://docs.n8n.io/connect/n8n-api/credential#post-credentials)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials

Creates a credential that can be used by nodes of the specified type.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

idstring · min: 1 · max: 16Optional

An unused credential ID of 1–16 letters, digits, underscores, or hyphens. The supplied ID is preserved exactly. Omit to generate an ID.

Example: `R2DjclaysHbqn778`Pattern: `^[a-zA-Z0-9_-]+$`

namestringRequiredExample: `Joe's Github Credentials`

descriptionstring · max: 512 · nullableOptional

Plain text, up to 512 characters. A blank value is saved as null. Ignored when credential descriptions are disabled.

Example: `Read-only key for the reporting database`

typestringRequiredExample: `githubApi`

dataobjectWrite-onlyRequiredExample: `{"accessToken":"ada612vad6fa5df4adf5a5dsf4389adsf76da7s"}`

Show properties

isResolvablebooleanOptional

Whether this credential has resolvable fields

Example: `false`

createdAtstring · date-timeRead-onlyOptionalExample: `2022-04-29T11:02:29.842Z`

updatedAtstring · date-timeRead-onlyOptionalExample: `2022-04-29T11:02:29.842Z`

projectIdstringOptional

Project to create the credential in. Defaults to the user's personal project.

Example: `VmwOO9HeTEj20kxM`

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

typestringRequired

isManagedbooleanRequired

isGlobalbooleanRequired

isResolvablebooleanRequired

resolvableAllowFallbackbooleanRequired

resolverIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

descriptionstring · nullableOptional

Present only when credential descriptions are enabled.

Example: `Read-only key for the reporting database`

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

post/credentials

HTTP

Copy

    POST /api/v1/credentials HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 252
    
    {
      "id": "R2DjclaysHbqn778",
      "name": "Joe's Github Credentials",
      "description": "Read-only key for the reporting database",
      "type": "githubApi",
      "data": {
        "accessToken": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"
      },
      "isResolvable": false,
      "projectId": "VmwOO9HeTEj20kxM"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "text",
      "isManaged": true,
      "isGlobal": true,
      "isResolvable": true,
      "resolvableAllowFallback": true,
      "resolverId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "description": "Read-only key for the reporting database"
    }

### Get credential by ID[](https://docs.n8n.io/connect/n8n-api/credential#get-credentials-credentialid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/{credentialId}

Retrieves a credential by ID. Credential data (secrets) is not included.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialIdstringRequired

The ID of the credential.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

typestringRequired

isManagedbooleanRequired

isGlobalbooleanRequired

isResolvablebooleanRequired

resolvableAllowFallbackbooleanRequired

resolverIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

descriptionstring · nullableOptional

Present only when credential descriptions are enabled.

Example: `Read-only key for the reporting database`

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/credentials/{credentialId}

HTTP

Copy

    GET /api/v1/credentials/{credentialId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "text",
      "isManaged": true,
      "isGlobal": true,
      "isResolvable": true,
      "resolvableAllowFallback": true,
      "resolverId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "description": "Read-only key for the reporting database"
    }

### Delete credential by ID[](https://docs.n8n.io/connect/n8n-api/credential#delete-credentials-credentialid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/{credentialId}

Deletes a credential from your instance. You must be the owner of the credential.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialIdstringRequired

The ID of the credential.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

typestringRequired

isManagedbooleanRequired

isGlobalbooleanRequired

isResolvablebooleanRequired

resolvableAllowFallbackbooleanRequired

resolverIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

descriptionstring · nullableOptional

Present only when credential descriptions are enabled.

Example: `Read-only key for the reporting database`

usageScopestring · enumRequiredPossible values: `project``instance`

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/credentials/{credentialId}

HTTP

Copy

    DELETE /api/v1/credentials/{credentialId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "text",
      "isManaged": true,
      "isGlobal": true,
      "isResolvable": true,
      "resolvableAllowFallback": true,
      "resolverId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "description": "Read-only key for the reporting database",
      "usageScope": "project"
    }

### Update credential by ID[](https://docs.n8n.io/connect/n8n-api/credential#patch-credentials-credentialid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/{credentialId}

Updates an existing credential. You must be the owner of the credential.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialIdstringRequired

The ID of the credential.

Body

application/json

namestringOptional

The name of the credential

Example: `Updated Credential Name`

descriptionstring · max: 512 · nullableOptional

Plain text, up to 512 characters. Send null or a blank value to clear it. Omit it to keep the stored value. Ignored when credential descriptions are disabled.

Example: `Read-only key for the reporting database`

typestringOptional

The credential type. If changing type, data must also be provided.

Example: `githubApi`

dataobjectWrite-onlyOptional

The credential data. Required when changing credential type.

Example: `{"accessToken":"new_token_value"}`

Show properties

isGlobalbooleanOptional

Whether this credential is available globally

Example: `false`

isResolvablebooleanOptional

Whether this credential has resolvable fields

Example: `false`

isPartialDatabooleanOptional

If true, unredacts and merges existing credential data with the provided data. If false, replaces the entire data object.

Default: `false`Example: `false`

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

typestringRequired

isManagedbooleanRequired

isGlobalbooleanRequired

isResolvablebooleanRequired

resolvableAllowFallbackbooleanRequired

resolverIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

descriptionstring · nullableOptional

Present only when credential descriptions are enabled.

Example: `Read-only key for the reporting database`

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

patch/credentials/{credentialId}

HTTP

Copy

    PATCH /api/v1/credentials/{credentialId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 211
    
    {
      "name": "Updated Credential Name",
      "description": "Read-only key for the reporting database",
      "type": "githubApi",
      "data": {
        "accessToken": "new_token_value"
      },
      "isGlobal": false,
      "isResolvable": false,
      "isPartialData": false
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "text",
      "isManaged": true,
      "isGlobal": true,
      "isResolvable": true,
      "resolvableAllowFallback": true,
      "resolverId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "description": "Read-only key for the reporting database"
    }

### Transfer a credential to another project.[](https://docs.n8n.io/connect/n8n-api/credential#put-credentials-credentialid-transfer)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/{credentialId}/transfer

Transfer a credential to another project.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialIdstringRequired

The ID of the credential.

Body

application/json

destinationProjectIdstringRequired

The ID of the project to transfer the credential to.

Example: `VmwOO9HeTEj20kxM`

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

put/credentials/{credentialId}/transfer

HTTP

Copy

    PUT /api/v1/credentials/{credentialId}/transfer HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 43
    
    {
      "destinationProjectId": "VmwOO9HeTEj20kxM"
    }

Test it

204

Operation successful.

No content

### Test credential by ID[](https://docs.n8n.io/connect/n8n-api/credential#post-credentials-credentialid-test)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/{credentialId}/test

Tests a credential by ID using the stored credential data.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialIdstringRequired

The ID of the credential.

Responses

200

Operation successful.

application/json

statusstring · enumRequiredExample: `OK`Possible values: `OK``Error`

messagestringRequiredExample: `Connection successful!`

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/credentials/{credentialId}/test

HTTP

Copy

    POST /api/v1/credentials/{credentialId}/test HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "status": "OK",
      "message": "Connection successful!"
    }

### Show credential data schema[](https://docs.n8n.io/connect/n8n-api/credential#get-credentials-schema-credentialtypename)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/credentials/schema/{credentialTypeName}

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

credentialTypeNamestringRequired

The credential type name that you want to get the schema for

Responses

200

Operation successful.

application/json

additionalPropertiesboolean · enumRequiredPossible values: `false`

typestring · enumRequiredPossible values: `object`

propertiesobjectRequired

JSON Schema fragment for each of the credential type's fields, keyed by field name.

Example: `{"apiKey":{"type":"string"},"domain":{"type":"string"}}`

Show properties

requiredstring\[\]Required

Names of the fields that a request must include. A field with a default value is not listed.

Example: `["apiKey","domain"]`

allOfany\[\]Optional

Show properties

401

Unauthorized

404

The specified resource was not found.

get/credentials/schema/{credentialTypeName}

HTTP

Copy

    GET /api/v1/credentials/schema/{credentialTypeName} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "additionalProperties": false,
      "type": "object",
      "properties": {
        "apiKey": {
          "type": "string"
        },
        "domain": {
          "type": "string"
        }
      },
      "required": [\
        "apiKey",\
        "domain"\
      ],
      "allOf": []
    }

[PreviousCommunity Package](https://docs.n8n.io/connect/n8n-api/community-package)
[NextCredential Type Policy](https://docs.n8n.io/connect/n8n-api/credential-type-policy)

Last updated 9 days ago

Was this helpful?
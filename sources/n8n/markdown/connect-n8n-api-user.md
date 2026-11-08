For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/user.md)
.

Copy

On this page

Operations about users

### Retrieve all users[](https://docs.n8n.io/connect/n8n-api/user#get-users)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/users

Retrieve all users from your instance. Only available for the instance owner.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

includeRolestring · enumOptionalDefault: `false`Possible values: `true``false`

projectIdstringOptional

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

nextCursorstring · nullableRequired

Paginate through users by setting the cursor parameter to a nextCursor attribute returned by a previous request. Default value fetches the first page of the collection.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The given `projectId` does not exist.

get/users

HTTP

Copy

    GET /api/v1/users HTTP/1.1
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
          "isPending": true,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "mfaEnabled": false,\
          "role": "global:owner"\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Create multiple users[](https://docs.n8n.io/connect/n8n-api/user#post-users)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/users

Create one or more users.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Bodyobject\[\]

application/json

emailstring · emailRequired

roleany ofOptionalDefault: `global:member`

string · enumOptionalPossible values: `global:admin``global:member``global:chatUser`

or

string · min: 1Optional

Responses

201

Operation successful.

application/json

userobjectRequired

Show properties

errorstringRead-onlyOptional

The reason the invite failed for this user. Empty when the invite succeeded.

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

post/users

HTTP

Copy

    POST /api/v1/users HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 51
    
    [\
      {\
        "email": "name@gmail.com",\
        "role": "global:member"\
      }\
    ]

Test it

201

Operation successful.

Copy

    [\
      {\
        "user": {\
          "id": "123e4567-e89b-12d3-a456-426614174000",\
          "email": "john.doe@company.com",\
          "inviteAcceptUrl": "text",\
          "emailSent": true,\
          "role": "global:member"\
        },\
        "error": "text"\
      }\
    ]

### Get user by ID/Email[](https://docs.n8n.io/connect/n8n-api/user#get-users-userid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/users/{userId}

Retrieve a user from your instance. Only available for the instance owner.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

userIdstringRequired

The ID or email of the user.

Query parameters

includeRolestring · enumOptionalDefault: `false`Possible values: `true``false`

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `123e4567-e89b-12d3-a456-426614174000`

emailstring · email · nullableRequiredExample: `john.doe@company.com`

firstNamestring · nullableRead-onlyRequiredExample: `john`

lastNamestring · nullableRead-onlyRequiredExample: `Doe`

isPendingbooleanRead-onlyRequired

Whether the user finished setting up their account in response to the invitation (true) or not (false).

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

mfaEnabledbooleanRead-onlyRequired

Whether the user has multi-factor authentication (MFA/2FA) enabled.

Example: `false`

rolestringRead-onlyOptionalExample: `global:owner`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

No user with that ID or email.

get/users/{userId}

HTTP

Copy

    GET /api/v1/users/{userId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "email": "john.doe@company.com",
      "firstName": "john",
      "lastName": "Doe",
      "isPending": true,
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "mfaEnabled": false,
      "role": "global:owner"
    }

### Delete user[](https://docs.n8n.io/connect/n8n-api/user#delete-users-userid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/users/{userId}

Delete a user from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

userIdstringRequired

The ID of the user.

Query parameters

transferIdstringOptional

ID of the project to transfer the deleted user's workflows and credentials to. Omit to delete those resources instead of transferring them.

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

delete/users/{userId}

HTTP

Copy

    DELETE /api/v1/users/{userId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Change a user's global role[](https://docs.n8n.io/connect/n8n-api/user#patch-users-userid-role)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/users/{userId}/role

Change a user's global role

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

userIdstringRequired

The ID of the user.

Body

application/json

newRoleNameany ofRequired

string · enumOptionalPossible values: `global:admin``global:member``global:chatUser`

or

string · min: 1Optional

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

patch/users/{userId}/role

HTTP

Copy

    PATCH /api/v1/users/{userId}/role HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 30
    
    {
      "newRoleName": "global:admin"
    }

Test it

204

Operation successful.

No content

[PreviousTags](https://docs.n8n.io/connect/n8n-api/tags)
[NextVariables](https://docs.n8n.io/connect/n8n-api/variables)

Last updated 9 days ago

Was this helpful?
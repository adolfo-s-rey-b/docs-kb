For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/community-package.md)
.

Copy

On this page

Operations about community packages

### List installed community packages[](https://docs.n8n.io/connect/n8n-api/community-package#get-community-packages)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/community-packages

Retrieve all installed community packages with pending update info.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

packageNamestringRequired

npm package name

installedVersionstringRequired

Currently installed version

authorNamestringOptional

Package author name

authorEmailstringOptional

Package author email

installedNodesobject\[\]Required

Nodes included in this package

Show properties

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

updateAvailablestringOptional

Version available for update, if any

failedLoadingbooleanOptional

Whether the package failed to load

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/community-packages

HTTP

Copy

    GET /api/v1/community-packages HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    [\
      {\
        "packageName": "text",\
        "installedVersion": "text",\
        "authorName": "text",\
        "authorEmail": "text",\
        "installedNodes": [\
          {\
            "name": "text",\
            "type": "text",\
            "latestVersion": 1\
          }\
        ],\
        "createdAt": "2026-01-01T00:00:00.000Z",\
        "updatedAt": "2026-01-01T00:00:00.000Z",\
        "updateAvailable": "text",\
        "failedLoading": true\
      }\
    ]

### Install a community package[](https://docs.n8n.io/connect/n8n-api/community-package#post-community-packages)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/community-packages

Install a community package by npm name and optional version.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestringRequired

npm package name. Unscoped names start with n8n-nodes-. Scoped names use the @\[author\]/n8n-nodes- form.

versionstringOptional

Semver version or npm dist-tag, such as latest or beta. When unverified packages are disabled, only versions verified by n8n can be installed.

Responses

200

Operation successful.

application/json

packageNamestringRequired

npm package name

installedVersionstringRequired

Currently installed version

authorNamestringOptional

Package author name

authorEmailstringOptional

Package author email

installedNodesobject\[\]Required

Nodes included in this package

Show properties

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

updateAvailablestringOptional

Version available for update, if any

failedLoadingbooleanOptional

Whether the package failed to load

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

post/community-packages

HTTP

Copy

    POST /api/v1/community-packages HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 32
    
    {
      "name": "text",
      "version": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "packageName": "text",
      "installedVersion": "text",
      "authorName": "text",
      "authorEmail": "text",
      "installedNodes": [\
        {\
          "name": "text",\
          "type": "text",\
          "latestVersion": 1\
        }\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "updateAvailable": "text",
      "failedLoading": true
    }

### Uninstall a community package[](https://docs.n8n.io/connect/n8n-api/community-package#delete-community-packages-name)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/community-packages/{name}

Uninstall a community package by name.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

namestringRequired

npm package name

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

delete/community-packages/{name}

HTTP

Copy

    DELETE /api/v1/community-packages/{name} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Update a community package[](https://docs.n8n.io/connect/n8n-api/community-package#patch-community-packages-name)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/community-packages/{name}

Update an installed community package to a new version.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

namestringRequired

npm package name

Body

application/json

versionstringOptional

Semver version or npm dist-tag to update to, such as latest or beta. When unverified packages are disabled, only versions verified by n8n can be installed.

Responses

200

Operation successful.

application/json

packageNamestringRequired

npm package name

installedVersionstringRequired

Currently installed version

authorNamestringOptional

Package author name

authorEmailstringOptional

Package author email

installedNodesobject\[\]Required

Nodes included in this package

Show properties

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

updateAvailablestringOptional

Version available for update, if any

failedLoadingbooleanOptional

Whether the package failed to load

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

patch/community-packages/{name}

HTTP

Copy

    PATCH /api/v1/community-packages/{name} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 18
    
    {
      "version": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "packageName": "text",
      "installedVersion": "text",
      "authorName": "text",
      "authorEmail": "text",
      "installedNodes": [\
        {\
          "name": "text",\
          "type": "text",\
          "latestVersion": 1\
        }\
      ],
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "updateAvailable": "text",
      "failedLoading": true
    }

[PreviousAudit](https://docs.n8n.io/connect/n8n-api/audit)
[NextCredential](https://docs.n8n.io/connect/n8n-api/credential)

Last updated 9 days ago

Was this helpful?
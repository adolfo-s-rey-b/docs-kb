For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/folders.md)
.

Copy

On this page

Operations about folders

### Retrieve folders[](https://docs.n8n.io/connect/n8n-api/folders#get-projects-projectid-folders)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/folders

Retrieve folders within a project. Supports filtering, sorting, field selection, and pagination.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

Query parameters

filterstringOptional

JSON-encoded filter object. Supported fields — parentFolderId, name, tags (array of tag names), excludeFolderIdAndDescendants.

Example: `{"parentFolderId":"abc123","name":"My Folder"}`

selectstringOptional

JSON-encoded array of fields to include. Valid fields — id, name, createdAt, updatedAt, project, tags, parentFolder, workflowCount, subFolderCount, path.

Example: `["id","name","tags","workflowCount"]`

sortBystring · enumOptional

Sort order for results.

Possible values: `name:asc``name:desc``createdAt:asc``createdAt:desc``updatedAt:asc``updatedAt:desc`

skipstringOptional

Number of items to skip for pagination. Defaults to 0.

takestringOptional

Number of items to return. Defaults to 10.

Responses

200

Operation successful.

application/json

countintegerRequired

Total number of folders matching the query.

dataobject\[\]Required

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/projects/{projectId}/folders

HTTP

Copy

    GET /api/v1/projects/{projectId}/folders HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "count": 1,
      "data": [\
        {\
          "id": "zLXWgYyZrZ4Gn1Vk",\
          "name": "My Folder",\
          "parentFolderId": "kRZ0ewrAEAhCkTBd",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "homeProject": {\
            "id": "VmwOO9HeTEj20kxM",\
            "name": "Marketing",\
            "type": "team",\
            "icon": {\
              "type": "emoji",\
              "value": "text",\
              "color": "text"\
            }\
          },\
          "parentFolder": {\
            "id": "zLXWgYyZrZ4Gn1Vk",\
            "name": "My Folder",\
            "parentFolderId": "text"\
          },\
          "tags": [\
            {\
              "id": "text",\
              "name": "text"\
            }\
          ],\
          "workflowCount": 1,\
          "subFolderCount": 1,\
          "path": [\
            "Marketing",\
            "Campaigns"\
          ]\
        }\
      ]
    }

### Create a folder[](https://docs.n8n.io/connect/n8n-api/folders#post-projects-projectid-folders)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/folders

Create a folder within a project.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project, or `personal` to create the folder in the calling user's own personal project.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · max: 128RequiredExample: `My Folder`

parentFolderIdstring · max: 36OptionalExample: `kRZ0ewrAEAhCkTBd`

Responses

201

Operation successful.

application/json

idstringRead-onlyRequiredExample: `zLXWgYyZrZ4Gn1Vk`

namestringRequiredExample: `My Folder`

parentFolderIdstring · nullableRequiredExample: `kRZ0ewrAEAhCkTBd`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

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

post/projects/{projectId}/folders

HTTP

Copy

    POST /api/v1/projects/{projectId}/folders HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 56
    
    {
      "name": "My Folder",
      "parentFolderId": "kRZ0ewrAEAhCkTBd"
    }

Test it

201

Operation successful.

Copy

    {
      "id": "zLXWgYyZrZ4Gn1Vk",
      "name": "My Folder",
      "parentFolderId": "kRZ0ewrAEAhCkTBd",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Get folder details[](https://docs.n8n.io/connect/n8n-api/folders#get-projects-projectid-folders-folderid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/folders/{folderId}

Get folder details including sub-folder and workflow counts.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

folderIdstringRequired

The ID of the folder.

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `zLXWgYyZrZ4Gn1Vk`

namestringRequiredExample: `My Folder`

parentFolderIdstring · nullableRequiredExample: `kRZ0ewrAEAhCkTBd`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

totalSubFoldersintegerRequired

Total number of sub-folders (recursive).

totalWorkflowsintegerRequired

Total number of workflows (recursive).

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/projects/{projectId}/folders/{folderId}

HTTP

Copy

    GET /api/v1/projects/{projectId}/folders/{folderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "zLXWgYyZrZ4Gn1Vk",
      "name": "My Folder",
      "parentFolderId": "kRZ0ewrAEAhCkTBd",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "totalSubFolders": 1,
      "totalWorkflows": 1
    }

### Delete a folder[](https://docs.n8n.io/connect/n8n-api/folders#delete-projects-projectid-folders-folderid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/folders/{folderId}

Delete a folder within a project. When `transferToFolderId` is provided, workflows and sub-folders are moved to the target folder before deletion. When omitted, workflows are moved to the project root and archived, and child folders are deleted.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

folderIdstringRequired

The ID of the folder.

Query parameters

transferToFolderIdstring · min: 1 · max: 36Optional

Optional target folder ID to move workflows and sub-folders into before deleting.

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

delete/projects/{projectId}/folders/{folderId}

HTTP

Copy

    DELETE /api/v1/projects/{projectId}/folders/{folderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Update a folder[](https://docs.n8n.io/connect/n8n-api/folders#patch-projects-projectid-folders-folderid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/projects/{projectId}/folders/{folderId}

Update folder name or parent folder.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

projectIdstringRequired

The ID of the project.

folderIdstringRequired

The ID of the folder.

Body

application/json

namestring · max: 128OptionalExample: `Renamed Folder`

parentFolderIdstringOptional

ID of the parent folder to move this folder into. Set to "0" to move the folder to the project root.

Example: `abc123`

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `zLXWgYyZrZ4Gn1Vk`

namestringRequiredExample: `My Folder`

parentFolderIdstring · nullableRequiredExample: `kRZ0ewrAEAhCkTBd`

createdAtstring · date-timeRead-onlyRequired

updatedAtstring · date-timeRead-onlyRequired

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

patch/projects/{projectId}/folders/{folderId}

HTTP

Copy

    PATCH /api/v1/projects/{projectId}/folders/{folderId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 51
    
    {
      "name": "Renamed Folder",
      "parentFolderId": "abc123"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "zLXWgYyZrZ4Gn1Vk",
      "name": "My Folder",
      "parentFolderId": "kRZ0ewrAEAhCkTBd",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

[PreviousExecutions](https://docs.n8n.io/connect/n8n-api/executions)
[NextInsights](https://docs.n8n.io/connect/n8n-api/insights)

Last updated 9 days ago

Was this helpful?
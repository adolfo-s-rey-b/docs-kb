For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/source-control.md)
.

Copy

On this page

Operations about source control

### Preview pending source control changes[](https://docs.n8n.io/connect/n8n-api/source-control#get-source-control-status)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/source-control/status

Previews the pending changes between the instance and the connected Git branch in either the `push` or `pull` direction.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

directionstring · enumRequiredPossible values: `push``pull`

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/source-control/status

HTTP

Copy

    GET /api/v1/source-control/status?direction=push HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "file": "text",\
          "id": "text",\
          "name": "text",\
          "type": "credential",\
          "status": "new",\
          "location": "local",\
          "conflict": true,\
          "updatedAt": "text",\
          "pushed": true,\
          "isLocalPublished": true,\
          "isRemoteArchived": true,\
          "parentFolderId": "text",\
          "folderPath": [\
            "text"\
          ],\
          "remoteFolderPath": [\
            "text"\
          ],\
          "owner": {\
            "type": "personal",\
            "projectId": "text",\
            "projectName": "text"\
          },\
          "publishingError": "text",\
          "publishingErrorDetails": {\
            "reason": "review_pending",\
            "workflowReviewRequestId": "text",\
            "versionId": "text"\
          },\
          "contentImportPolicy": {\
            "violations": [\
              {\
                "kind": "text",\
                "checkId": "text",\
                "message": "text",\
                "subject": "text",\
                "subjectType": "text",\
                "scope": "text",\
                "matchedRuleId": "text",\
                "projectId": "text",\
                "optInAvailable": true\
              }\
            ],\
            "checkErrors": [\
              {\
                "checkId": "text",\
                "correlationId": "text"\
              }\
            ]\
          }\
        }\
      ]
    }

### Push local source control changes[](https://docs.n8n.io/connect/n8n-api/source-control#post-source-control-push)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/source-control/push

Commits and pushes the selected files to the connected Git branch. Each entry in `fileNames` is resolved against a fresh preview of the pending changes.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

commitMessagestring · min: 1 · max: 1000Required

fileNamesobject\[\] · min: 1Required

Show properties

forcebooleanOptional

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

The push includes files with unresolved conflicts. Retry with `force: true` to push anyway.

application/json

415

Unsupported media type.

422

Unprocessable Entity

post/source-control/push

HTTP

Copy

    POST /api/v1/source-control/push HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 85
    
    {
      "commitMessage": "text",
      "fileNames": [\
        {\
          "id": "text",\
          "type": "credential"\
        }\
      ],
      "force": true
    }

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "file": "text",\
          "id": "text",\
          "name": "text",\
          "type": "credential",\
          "status": "new",\
          "location": "local",\
          "conflict": true,\
          "updatedAt": "text",\
          "pushed": true,\
          "isLocalPublished": true,\
          "isRemoteArchived": true,\
          "parentFolderId": "text",\
          "folderPath": [\
            "text"\
          ],\
          "remoteFolderPath": [\
            "text"\
          ],\
          "owner": {\
            "type": "personal",\
            "projectId": "text",\
            "projectName": "text"\
          },\
          "publishingError": "text",\
          "publishingErrorDetails": {\
            "reason": "review_pending",\
            "workflowReviewRequestId": "text",\
            "versionId": "text"\
          },\
          "contentImportPolicy": {\
            "violations": [\
              {\
                "kind": "text",\
                "checkId": "text",\
                "message": "text",\
                "subject": "text",\
                "subjectType": "text",\
                "scope": "text",\
                "matchedRuleId": "text",\
                "projectId": "text",\
                "optInAvailable": true\
              }\
            ],\
            "checkErrors": [\
              {\
                "checkId": "text",\
                "correlationId": "text"\
              }\
            ]\
          }\
        }\
      ]
    }

### Pull changes from the remote repository[](https://docs.n8n.io/connect/n8n-api/source-control#post-source-control-pull)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/source-control/pull

Fetches changes from the connected Git branch into the instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

forcebooleanOptional

Discard local changes and force the pull to complete.

autoPublishstring · enumOptional

Controls automatic workflow publishing after import:

*   `none`: Keep workflows in their local published state (default)
*   `all`: Publish all imported workflows
*   `published`: Publish only workflows that were published locally before import

Default: `none`Possible values: `none``all``published`

Responses

200

Operation successful.

application/json

filestringRequired

idstringRequired

namestringRequired

typestring · enumRequiredPossible values: `credential``workflow``tags``variables``file``folders``project``datatable`

statusstring · enumRequiredPossible values: `new``modified``deleted``created``renamed``conflicted``ignored``staged``unknown`

locationstring · enumRequiredPossible values: `local``remote`

conflictbooleanRequired

updatedAtstringRequired

pushedbooleanOptional

isLocalPublishedbooleanOptional

isRemoteArchivedbooleanOptional

parentFolderIdstring · nullableOptional

folderPathstring\[\]Optional

remoteFolderPathstring\[\]Optional

ownerobjectOptional

Show properties

publishingErrorstringOptional

publishingErrorDetailsobjectOptional

Show properties

contentImportPolicyobjectOptional

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

Conflict due to uncommitted local changes or merge conflicts. The response body lists every file in the pull diff; files causing the conflict have `conflict: true` or `status: modified`. Retry with `force: true` to discard local changes.

application/json

415

Unsupported media type.

422

Unprocessable Entity

post/source-control/pull

HTTP

Copy

    POST /api/v1/source-control/pull HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 35
    
    {
      "force": true,
      "autoPublish": "none"
    }

Test it

200

Operation successful.

Copy

    [\
      {\
        "file": "text",\
        "id": "text",\
        "name": "text",\
        "type": "credential",\
        "status": "new",\
        "location": "local",\
        "conflict": true,\
        "updatedAt": "text",\
        "pushed": true,\
        "isLocalPublished": true,\
        "isRemoteArchived": true,\
        "parentFolderId": "text",\
        "folderPath": [\
          "text"\
        ],\
        "remoteFolderPath": [\
          "text"\
        ],\
        "owner": {\
          "type": "personal",\
          "projectId": "text",\
          "projectName": "text"\
        },\
        "publishingError": "text",\
        "publishingErrorDetails": {\
          "reason": "review_pending",\
          "workflowReviewRequestId": "text",\
          "versionId": "text"\
        },\
        "contentImportPolicy": {\
          "violations": [\
            {\
              "kind": "text",\
              "checkId": "text",\
              "message": "text",\
              "subject": "text",\
              "subjectType": "text",\
              "scope": "text",\
              "matchedRuleId": "text",\
              "projectId": "text",\
              "optInAvailable": true\
            }\
          ],\
          "checkErrors": [\
            {\
              "checkId": "text",\
              "correlationId": "text"\
            }\
          ]\
        }\
      }\
    ]

[PreviousSettings Sso Saml](https://docs.n8n.io/connect/n8n-api/settings-sso-saml)
[NextTags](https://docs.n8n.io/connect/n8n-api/tags)

Last updated 9 days ago

Was this helpful?
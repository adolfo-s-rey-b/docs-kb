For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/workflow.md)
.

Copy

On this page

Operations about workflows

### Retrieve all workflows[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows

Retrieve all workflows from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

offsetnumberOptional

The number of items to skip before starting to collect the result set.

Default: `0`Example: `0`

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

activestring · enumOptionalPossible values: `true``false`

tagsstringOptional

namestringOptional

projectIdstringOptional

excludePinnedDatastring · enumOptionalDefault: `false`Possible values: `true``false`

includeParentFolderstring · enumOptional

Set to `true` to add `parentFolder` to each workflow. `parentFolder` holds the folder `id`, or is `null` at the project root.

Default: `false`Possible values: `true``false`

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

get/workflows

HTTP

Copy

    GET /api/v1/workflows HTTP/1.1
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
          "activeVersionId": "text",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "isArchived": true,\
          "versionId": "text",\
          "triggerCount": 1,\
          "nodes": [\
            {\
              "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
              "name": "Jira",\
              "webhookId": "text",\
              "disabled": true,\
              "notesInFlow": true,\
              "notes": "text",\
              "type": "n8n-nodes-base.jira",\
              "typeVersion": 1,\
              "executeOnce": false,\
              "alwaysOutputData": false,\
              "retryOnFail": false,\
              "maxTries": 1,\
              "waitBetweenTries": 1,\
              "onError": "stopWorkflow",\
              "position": [\
                -100,\
                80\
              ],\
              "parameters": {\
                "ANY_ADDITIONAL_PROPERTY": "anything"\
              },\
              "credentials": {\
                "jiraSoftwareCloudApi": {\
                  "name": "jiraApi"\
                }\
              },\
              "customTelemetryTags": {\
                "tag": [\
                  {\
                    "key": "text",\
                    "value": "text"\
                  }\
                ]\
              },\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z"\
            }\
          ],\
          "connections": {\
            "Jira": {\
              "main": [\
                [\
                  {\
                    "node": "Jira",\
                    "type": "main",\
                    "index": 0\
                  }\
                ]\
              ]\
            }\
          },\
          "nodeGroups": [\
            {\
              "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
              "name": "Data processing",\
              "description": "Cleans and normalizes incoming records",\
              "nodeIds": [\
                "text"\
              ]\
            }\
          ],\
          "settings": {\
            "saveExecutionProgress": true,\
            "saveManualExecutions": true,\
            "saveDataErrorExecution": "DEFAULT",\
            "saveDataSuccessExecution": "DEFAULT",\
            "executionTimeout": 3600,\
            "errorWorkflow": "VzqKEW0ShTXA5vPj",\
            "timezone": "America/New_York",\
            "executionOrder": "v1",\
            "binaryMode": "separate",\
            "callerPolicy": "workflowsFromSameOwner",\
            "callerIds": "14, 18, 23",\
            "timeSavedMode": "fixed",\
            "timeSavedPerExecution": 1,\
            "redactionPolicy": "non-manual",\
            "availableInMCP": false,\
            "customTelemetryTags": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ],\
            "credentialResolverId": "text"\
          },\
          "staticData": {\
            "lastId": 1\
          },\
          "pinData": {},\
          "meta": {\
            "onboardingId": "text",\
            "templateId": "text",\
            "instanceId": "text",\
            "templateCredsSetupCompleted": true\
          },\
          "tags": [\
            {\
              "id": "2tUt1wbLX592XDdX",\
              "name": "Production",\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z"\
            }\
          ],\
          "shared": [\
            {\
              "role": "text",\
              "workflowId": "text",\
              "projectId": "text",\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z"\
            }\
          ],\
          "activeVersion": {\
            "versionId": "text",\
            "workflowId": "text",\
            "nodes": [\
              {\
                "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
                "name": "Jira",\
                "webhookId": "text",\
                "disabled": true,\
                "notesInFlow": true,\
                "notes": "text",\
                "type": "n8n-nodes-base.jira",\
                "typeVersion": 1,\
                "executeOnce": false,\
                "alwaysOutputData": false,\
                "retryOnFail": false,\
                "maxTries": 1,\
                "waitBetweenTries": 1,\
                "onError": "stopWorkflow",\
                "position": [\
                  -100,\
                  80\
                ],\
                "parameters": {\
                  "ANY_ADDITIONAL_PROPERTY": "anything"\
                },\
                "credentials": {\
                  "jiraSoftwareCloudApi": {\
                    "name": "jiraApi"\
                  }\
                },\
                "customTelemetryTags": {\
                  "tag": [\
                    {\
                      "key": "text",\
                      "value": "text"\
                    }\
                  ]\
                },\
                "createdAt": "2026-01-01T00:00:00.000Z",\
                "updatedAt": "2026-01-01T00:00:00.000Z"\
              }\
            ],\
            "connections": {\
              "Jira": {\
                "main": [\
                  [\
                    {\
                      "node": "Jira",\
                      "type": "main",\
                      "index": 0\
                    }\
                  ]\
                ]\
              }\
            },\
            "nodeGroups": [\
              {\
                "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
                "name": "Data processing",\
                "description": "Cleans and normalizes incoming records",\
                "nodeIds": [\
                  "text"\
                ]\
              }\
            ],\
            "authors": "text",\
            "name": "text",\
            "description": "text",\
            "autosaved": true,\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          },\
          "parentFolder": {\
            "id": "text"\
          }\
        }\
      ],
      "nextCursor": "text"
    }

### Create a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows

Create a workflow in your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

idstringRead-onlyOptionalExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Workflow 1`

activebooleanRead-onlyOptionalDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRead-onlyOptional

createdAtstring · date-timeRead-onlyOptional

updatedAtstring · date-timeRead-onlyOptional

isArchivedbooleanRead-onlyOptional

versionIdstringRead-onlyOptional

Current version identifier used for optimistic locking

triggerCountintegerRead-onlyOptional

Number of active trigger nodes in the workflow

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

settingsobjectRequired

Show properties

nodeGroupsobject\[\]Optional

Visual groupings of nodes shown as frames on the canvas

Show properties

staticDataany ofOptional

Data the workflow keeps between executions

Example: `{"lastId":1}`

string · jsonStringOptional

or

objectOptional

Show properties

or

anyOptional

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

Show properties

projectIdstringOptional

Target project to create the workflow in. Defaults to the user's personal project.

Example: `VmwOO9HeTEj20kxM`

parentFolderIdstring · nullableOptional

ID of the folder to place the workflow in. Omit or null to place at the project root.

Example: `X8ovzm8lTQjcXRZQ`

metaobject · nullableRead-onlyOptional

Workflow metadata such as template information

Show properties

tagsobject\[\]Read-onlyOptional

Show properties

sharedobject\[\]Optional

Accepted for compatibility and ignored. The owner share is derived from the target project.

Show properties

activeVersionobject · nullableRead-onlyOptional

Show properties

descriptionstringOptional

Description of the workflow

Example: `My workflow description`

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

parentFolderobject · nullableRequired

Folder the workflow was placed in, or null at the project root

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

post/workflows

HTTP

Copy

    POST /api/v1/workflows HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 1615
    
    {
      "name": "Workflow 1",
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "extendsCredential": "text"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "all",
        "saveDataSuccessExecution": "all",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "staticData": {
        "lastId": 1
      },
      "pinData": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "projectId": "VmwOO9HeTEj20kxM",
      "parentFolderId": "X8ovzm8lTQjcXRZQ",
      "shared": [\
        {\
          "role": "workflow:owner",\
          "workflowId": "2tUt1wbLX592XDdX",\
          "projectId": "2tUt1wbLX592XDdX",\
          "project": {\
            "name": "text"\
          }\
        }\
      ],
      "description": "My workflow description"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      },
      "parentFolder": {
        "id": "text",
        "name": "text",
        "parentFolderId": "text",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      }
    }

### Retrieve a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows-workflowid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}

Retrieve a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Query parameters

excludePinnedDatastring · enumOptionalDefault: `false`Possible values: `true``false`

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

parentFolderobject · nullableRequired

Folder that contains the workflow, or null at the project root

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}

HTTP

Copy

    GET /api/v1/workflows/{workflowId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      },
      "parentFolder": {
        "id": "text",
        "name": "text",
        "parentFolderId": "text",
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z"
      }
    }

### Update a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#put-workflows-workflowid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}

Update a workflow. If the workflow is published, the updated version will be automatically re-published unless `publishIfActive` is set to `false`. Because that re-publication puts a new version live, it additionally requires the `workflow:activate` API key scope and the `workflow:publish` project permission. A caller without either can still save: the new version is stored as a draft and the response is a `403` naming the missing permission, leaving the published version live. Saving an unpublished workflow, or saving with `publishIfActive=false`, only needs `workflow:update`.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Query parameters

publishIfActivestring · enumOptional

Whether to publish the update if the workflow is currently published. Set to `false` to save the change as a draft on the existing published version instead of releasing it. Has no effect on a workflow that isn't currently published.

Default: `true`Possible values: `true``false`

Body

application/json

idstringRead-onlyOptionalExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Workflow 1`

activebooleanRead-onlyOptionalDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRead-onlyOptional

createdAtstring · date-timeRead-onlyOptional

updatedAtstring · date-timeRead-onlyOptional

isArchivedbooleanRead-onlyOptional

versionIdstringRead-onlyOptional

Current version identifier used for optimistic locking

triggerCountintegerRead-onlyOptional

Number of active trigger nodes in the workflow

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

settingsobjectRequired

Show properties

nodeGroupsobject\[\]Optional

Visual groupings of nodes shown as frames on the canvas

Show properties

staticDataany ofOptional

Data the workflow keeps between executions

Example: `{"lastId":1}`

string · jsonStringOptional

or

objectOptional

Show properties

or

anyOptional

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

Show properties

parentFolderIdstring · nullableWrite-onlyOptional

ID of the folder to move the workflow into. Pass null to move it to the project root; omit to leave its current folder unchanged.

Example: `X8ovzm8lTQjcXRZQ`

metaobject · nullableRead-onlyOptional

Workflow metadata such as template information

Show properties

tagsobject\[\]Read-onlyOptional

Show properties

sharedobject\[\]Optional

Accepted for compatibility and ignored. The owner share is derived from the target project.

Show properties

activeVersionobject · nullableRead-onlyOptional

Show properties

descriptionstringOptional

Description of the workflow

Example: `My workflow description`

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

activeVersionobject · nullableRequired

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

The update would re-publish the workflow, but the API key lacks `workflow:activate` or the caller lacks `workflow:publish` on the project. The update is still saved as a draft, named by `versionId`, and the published version stays live.

application/json

404

The specified resource was not found.

409

Conflict, e.g. re-publication blocked by an open workflow review (then `reason` and `workflowReviewRequestId` are present; the update itself is still saved as a draft) or a webhook path conflict.

application/json

415

Unsupported media type.

422

Unprocessable Entity

put/workflows/{workflowId}

HTTP

Copy

    PUT /api/v1/workflows/{workflowId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 1584
    
    {
      "name": "Workflow 1",
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "extendsCredential": "text"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "all",
        "saveDataSuccessExecution": "all",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "staticData": {
        "lastId": 1
      },
      "pinData": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "parentFolderId": "X8ovzm8lTQjcXRZQ",
      "shared": [\
        {\
          "role": "workflow:owner",\
          "workflowId": "2tUt1wbLX592XDdX",\
          "projectId": "2tUt1wbLX592XDdX",\
          "project": {\
            "name": "text"\
          }\
        }\
      ],
      "description": "My workflow description"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Delete a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#delete-workflows-workflowid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}

Delete a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableOptional

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Conflict

delete/workflows/{workflowId}

HTTP

Copy

    DELETE /api/v1/workflows/{workflowId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Archive a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-archive)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/archive

Soft-deletes a workflow by archiving it. Idempotent: archiving an already archived workflow returns 200 with the current workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/workflows/{workflowId}/archive

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/archive HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Unarchive a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-unarchive)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/unarchive

Restores an archived workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/workflows/{workflowId}/unarchive

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/unarchive HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Transfer a workflow to another project[](https://docs.n8n.io/connect/n8n-api/workflow#put-workflows-workflowid-transfer)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/transfer

Transfer a workflow to another project.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Body

application/json

destinationProjectIdstringRequired

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

put/workflows/{workflowId}/transfer

HTTP

Copy

    PUT /api/v1/workflows/{workflowId}/transfer HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 31
    
    {
      "destinationProjectId": "text"
    }

Test it

204

Operation successful.

No content

### Publish a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-publish)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/publish

Publish a workflow. In n8n v1, this action was termed activating a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Body

application/json

versionIdstringOptional

The specific version ID to publish. If not provided, the latest version is used.

namestringOptional

Optional name for the workflow version during publication.

descriptionstringOptional

Optional description for the workflow version during publication.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

activeVersionobject · nullableRequired

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

Conflict, e.g. publication blocked by an open workflow review (then `reason` and `workflowReviewRequestId` are present) or a webhook path conflict.

application/json

415

Unsupported media type.

post/workflows/{workflowId}/publish

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/publish HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 55
    
    {
      "versionId": "text",
      "name": "text",
      "description": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Unpublish a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-unpublish)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/unpublish

Unpublish a workflow. In n8n v1, this action was termed deactivating a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/workflows/{workflowId}/unpublish

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/unpublish HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

Deprecated

### Publish a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-activate)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/activate

Deprecated: use POST /workflows/{id}/publish instead. Publish a workflow. In n8n v1, this action was termed activating a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Body

application/json

versionIdstringOptional

The specific version ID to activate or publish. If not provided, the latest version is used.

namestringOptional

Optional name for the workflow version during activation.

descriptionstringOptional

Optional description for the workflow version during activation.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

activeVersionobject · nullableRequired

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

Conflict, e.g. publication blocked by an open workflow review (then `reason` and `workflowReviewRequestId` are present) or a webhook path conflict.

application/json

415

Unsupported media type.

post/workflows/{workflowId}/activate

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/activate HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 55
    
    {
      "versionId": "text",
      "name": "text",
      "description": "text"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

Deprecated

### Deactivate a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#post-workflows-workflowid-deactivate)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/deactivate

Deprecated: use POST /workflows/{id}/unpublish instead. Deactivate a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

namestringRequired

descriptionstring · nullableRequired

activebooleanRequiredDeprecated

Deprecated. Check whether `activeVersionId` is not null instead.

activeVersionIdstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

isArchivedbooleanRequired

versionIdstringRequired

versionCounternumberRequired

sourceWorkflowIdstring · nullableRequired

triggerCountnumberRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

settingsobject · nullableRequired

Execution and behaviour settings for the workflow

Show properties

staticDataobject · nullableRequired

Data the workflow keeps between executions

Example: `{"lastId":1}`

pinDataobject · nullableOptional

Pinned sample data for nodes, keyed by node name

metaobject · nullableRequired

Workflow metadata such as template information

Show properties

tagsobject\[\]Optional

Show properties

sharedobject\[\]Required

Show properties

activeVersionobject · nullableRequired

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/workflows/{workflowId}/deactivate

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/deactivate HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "description": "text",
      "activeVersionId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "isArchived": true,
      "versionId": "text",
      "versionCounter": 1,
      "sourceWorkflowId": "text",
      "triggerCount": 1,
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "settings": {
        "saveExecutionProgress": true,
        "saveManualExecutions": true,
        "saveDataErrorExecution": "DEFAULT",
        "saveDataSuccessExecution": "DEFAULT",
        "executionTimeout": 3600,
        "errorWorkflow": "VzqKEW0ShTXA5vPj",
        "timezone": "America/New_York",
        "executionOrder": "v1",
        "binaryMode": "separate",
        "callerPolicy": "workflowsFromSameOwner",
        "callerIds": "14, 18, 23",
        "timeSavedMode": "fixed",
        "timeSavedPerExecution": 1,
        "redactionPolicy": "non-manual",
        "availableInMCP": false,
        "customTelemetryTags": [\
          {\
            "key": "text",\
            "value": "text"\
          }\
        ],
        "credentialResolverId": "text"
      },
      "staticData": {
        "lastId": 1
      },
      "pinData": {},
      "meta": {
        "onboardingId": "text",
        "templateId": "text",
        "instanceId": "text",
        "templateCredsSetupCompleted": true
      },
      "tags": [\
        {\
          "id": "2tUt1wbLX592XDdX",\
          "name": "Production",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "shared": [\
        {\
          "role": "text",\
          "workflowId": "text",\
          "projectId": "text",\
          "project": {\
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
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "activeVersion": {
        "versionId": "text",
        "workflowId": "text",
        "nodes": [\
          {\
            "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
            "name": "Jira",\
            "webhookId": "text",\
            "disabled": true,\
            "notesInFlow": true,\
            "notes": "text",\
            "type": "n8n-nodes-base.jira",\
            "typeVersion": 1,\
            "executeOnce": false,\
            "alwaysOutputData": false,\
            "retryOnFail": false,\
            "maxTries": 1,\
            "waitBetweenTries": 1,\
            "onError": "stopWorkflow",\
            "position": [\
              -100,\
              80\
            ],\
            "parameters": {\
              "ANY_ADDITIONAL_PROPERTY": "anything"\
            },\
            "credentials": {\
              "jiraSoftwareCloudApi": {\
                "name": "jiraApi"\
              }\
            },\
            "customTelemetryTags": {\
              "tag": [\
                {\
                  "key": "text",\
                  "value": "text"\
                }\
              ]\
            },\
            "createdAt": "2026-01-01T00:00:00.000Z",\
            "updatedAt": "2026-01-01T00:00:00.000Z"\
          }\
        ],
        "connections": {
          "Jira": {
            "main": [\
              [\
                {\
                  "node": "Jira",\
                  "type": "main",\
                  "index": 0\
                }\
              ]\
            ]
          }
        },
        "nodeGroups": [\
          {\
            "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
            "name": "Data processing",\
            "description": "Cleans and normalizes incoming records",\
            "nodeIds": [\
              "text"\
            ]\
          }\
        ],
        "authors": "text",
        "name": "text",
        "description": "text",
        "autosaved": true,
        "createdAt": "2026-01-01T00:00:00.000Z",
        "updatedAt": "2026-01-01T00:00:00.000Z",
        "workflowPublishHistory": [\
          {\
            "id": 1,\
            "workflowId": "text",\
            "versionId": "text",\
            "event": "activated",\
            "userId": "text",\
            "createdAt": "2026-01-01T00:00:00.000Z"\
          }\
        ]
      }
    }

### Retrieve workflow version history[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows-workflowid-history)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/history

Returns a paginated list of workflow versions (version IDs and metadata) for a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

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

404

The specified resource was not found.

get/workflows/{workflowId}/history

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/history HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "versionId": "text",\
          "workflowId": "text",\
          "authors": "text",\
          "name": "text",\
          "description": "text",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "text"
    }

### Retrieve a workflow version[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows-workflowid-versions-workflowversionid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/versions/{workflowVersionId}

Retrieve a single version of a workflow from its version history.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

workflowVersionIdstringRequired

The ID of the workflow version.

Responses

200

Operation successful.

application/json

versionIdstringRequired

workflowIdstringRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Required

Visual groupings of nodes shown as frames on the canvas

Show properties

authorsstringRequired

namestring · nullableRequired

descriptionstring · nullableRequired

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}/versions/{workflowVersionId}

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/versions/{workflowVersionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "versionId": "text",
      "workflowId": "text",
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "authors": "text",
      "name": "text",
      "description": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Get workflow tags[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows-workflowid-tags)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/tags

Get workflow tags.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

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

get/workflows/{workflowId}/tags

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/tags HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    [\
      {\
        "id": "2tUt1wbLX592XDdX",\
        "name": "Production",\
        "createdAt": "2026-01-01T00:00:00.000Z",\
        "updatedAt": "2026-01-01T00:00:00.000Z"\
      }\
    ]

### Update tags of a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#put-workflows-workflowid-tags)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/tags

Update tags of a workflow.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Bodyobject\[\]

application/json

idstringRequiredExample: `2tUt1wbLX592XDdX`

Responses

200

Operation successful.

application/json

idstringRead-onlyRequiredExample: `2tUt1wbLX592XDdX`

namestringRequiredExample: `Production`

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

put/workflows/{workflowId}/tags

HTTP

Copy

    PUT /api/v1/workflows/{workflowId}/tags HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 27
    
    [\
      {\
        "id": "2tUt1wbLX592XDdX"\
      }\
    ]

Test it

200

Operation successful.

Copy

    [\
      {\
        "id": "2tUt1wbLX592XDdX",\
        "name": "Production",\
        "createdAt": "2026-01-01T00:00:00.000Z",\
        "updatedAt": "2026-01-01T00:00:00.000Z"\
      }\
    ]

Deprecated

### Retrieves a specific version of a workflow[](https://docs.n8n.io/connect/n8n-api/workflow#get-workflows-workflowid-workflowversionid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/{workflowVersionId}

Deprecated: use GET /workflows/{workflowId}/versions/{workflowVersionId} instead. Retrieves a specific version of a workflow from workflow history.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

workflowVersionIdstringRequired

The ID of the workflow version.

Responses

200

Operation successful.

application/json

versionIdstringRequired

workflowIdstringRequired

nodesobject\[\]Required

Nodes that make up the workflow

Show properties

connectionsobjectRequired

Connections between nodes, keyed by source node name

Example: `{"Jira":{"main":[[{"node":"Jira","type":"main","index":0}]]}}`

nodeGroupsobject\[\]Optional

Visual groupings of nodes shown as frames on the canvas

Show properties

authorsstringRequired

namestring · nullableOptional

descriptionstring · nullableOptional

createdAtstring · date-timeOptional

updatedAtstring · date-timeOptional

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}/{workflowVersionId}

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/{workflowVersionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "versionId": "text",
      "workflowId": "text",
      "nodes": [\
        {\
          "id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
          "name": "Jira",\
          "webhookId": "text",\
          "disabled": true,\
          "notesInFlow": true,\
          "notes": "text",\
          "type": "n8n-nodes-base.jira",\
          "typeVersion": 1,\
          "executeOnce": false,\
          "alwaysOutputData": false,\
          "retryOnFail": false,\
          "maxTries": 1,\
          "waitBetweenTries": 1,\
          "onError": "stopWorkflow",\
          "position": [\
            -100,\
            80\
          ],\
          "parameters": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "credentials": {\
            "jiraSoftwareCloudApi": {\
              "name": "jiraApi"\
            }\
          },\
          "customTelemetryTags": {\
            "tag": [\
              {\
                "key": "text",\
                "value": "text"\
              }\
            ]\
          },\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "connections": {
        "Jira": {
          "main": [\
            [\
              {\
                "node": "Jira",\
                "type": "main",\
                "index": 0\
              }\
            ]\
          ]
        }
      },
      "nodeGroups": [\
        {\
          "id": "9b1c8e2a-4d3f-4a6b-8c7d-1e2f3a4b5c6d",\
          "name": "Data processing",\
          "description": "Cleans and normalizes incoming records",\
          "nodeIds": [\
            "text"\
          ]\
        }\
      ],
      "authors": "text",
      "name": "text",
      "description": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

[PreviousVariables](https://docs.n8n.io/connect/n8n-api/variables)
[NextModels](https://docs.n8n.io/connect/n8n-api/models)

Last updated 9 days ago

Was this helpful?
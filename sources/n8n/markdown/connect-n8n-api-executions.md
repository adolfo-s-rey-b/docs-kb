For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/executions.md)
.

Copy

On this page

Operations about executions

### Retrieve all executions[](https://docs.n8n.io/connect/n8n-api/executions#get-executions)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/executions

Retrieve all executions from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

includeDatastring · enumOptional

Whether or not to include the execution's detailed data.

Default: `false`Possible values: `true``false`

ignoreDataSizeLimitstring · enumOptional

Whether to return the full execution data even if it exceeds the configured size limit (EXECUTIONS\_DATA\_MAX\_DISPLAY\_SIZE). Oversized executions are otherwise returned without their data.

Default: `false`Possible values: `true``false`

redactExecutionDatastring · enumOptional

Controls execution data redaction. When `true`, execution output data is always redacted. When `false`, requests unredacted (revealed) data — requires the `execution:reveal` scope. When omitted, follows the workflow redaction policy.

Possible values: `true``false`

statusstring · enumOptional

Status to filter the executions by.

Possible values: `canceled``crashed``error``new``running``success``unknown``waiting`

workflowIdstringOptional

Workflow to filter the executions by.

Example: `1000`

projectIdstringOptionalExample: `VmwOO9HeTEj20kxM`

startedAfterstring · date-timeOptional

Only return executions that started after this time.

Example: `2024-01-01T00:00:00.000Z`

startedBeforestring · date-timeOptional

Only return executions that started before this time.

Example: `2024-12-31T23:59:59.999Z`

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

nextCursorstring · nullableRequired

Paginate through executions by setting the cursor parameter to a nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `eyJsYXN0SWQiOiIxMDAwIiwibGltaXQiOjEwMH0=`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/executions

HTTP

Copy

    GET /api/v1/executions HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "1000",\
          "mode": "manual",\
          "retryOf": "text",\
          "retrySuccessId": "2",\
          "status": "canceled",\
          "startedAt": "2026-01-01T00:00:00.000Z",\
          "stoppedAt": "2026-01-01T00:00:00.000Z",\
          "workflowId": "1000",\
          "waitTill": "2026-01-01T00:00:00.000Z",\
          "storedAt": "db",\
          "jsonSizeBytes": 0,\
          "workflowVersionId": "text",\
          "data": {\
            "redactionInfo": {\
              "isRedacted": true,\
              "reason": "text",\
              "canReveal": true\
            },\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "workflowData": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "customData": {\
            "ANY_ADDITIONAL_PROPERTY": "text"\
          },\
          "dataTooLargeToDisplay": true\
        }\
      ],
      "nextCursor": "eyJsYXN0SWQiOiIxMDAwIiwibGltaXQiOjEwMH0="
    }

### Retrieve an execution[](https://docs.n8n.io/connect/n8n-api/executions#get-executions-executionid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}

Retrieve an execution from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

Query parameters

includeDatastring · enumOptional

Whether or not to include the execution's detailed data.

Default: `false`Possible values: `true``false`

ignoreDataSizeLimitstring · enumOptional

Whether to return the full execution data even if it exceeds the configured size limit (EXECUTIONS\_DATA\_MAX\_DISPLAY\_SIZE). Oversized executions are otherwise returned without their data.

Default: `false`Possible values: `true``false`

redactExecutionDatastring · enumOptional

Controls execution data redaction. When `true`, execution output data is always redacted. When `false`, requests unredacted (revealed) data — requires the `execution:reveal` scope. When omitted, follows the workflow redaction policy.

Possible values: `true``false`

Responses

200

Operation successful.

application/json

idstringRequiredExample: `1000`

finishedbooleanRequiredDeprecated

Whether the execution ran to completion. Use `status` instead.

Example: `true`

modestring · enumRequiredExample: `manual`Possible values: `cli``error``integrated``internal``manual``retry``trigger``webhook``evaluation``chat``agent`

retryOfstring · nullableRequired

ID of the execution this one is a retry of.

retrySuccessIdstring · nullableRequired

ID of the retry that succeeded, if this execution failed and a retry did not.

Example: `2`

statusstring · enumRequiredPossible values: `canceled``crashed``error``new``running``success``unknown``waiting`

createdAtstring · date-timeRequired

startedAtstring · date-time · nullableRequired

Null until the execution leaves the queue and starts running.

stoppedAtstring · date-time · nullableRequired

When the execution stopped. Null for the `new`, `running` and `unknown` statuses; a `waiting` execution has stopped its current run, so it has a value.

deletedAtstring · date-time · nullableRequired

Always null. Soft-deleted executions are not returned.

workflowIdstringRequiredExample: `1000`

waitTillstring · date-time · nullableRequired

The time at which a waiting execution resumes.

storedAtstring · enumRequired

Where the execution data is stored.

Possible values: `db``fs``s3``az`

tracingContextobject · nullableRequired

W3C trace context propagated with the execution.

Show properties

deduplicationKeystring · nullableRequired

Key used to stop a duplicate execution from being created.

jsonSizeBytesnumberRequired

Size of the stored execution data in bytes. 0 means unknown.

Example: `0`

binaryDataSizeBytesnumberRequired

Size of the stored binary data in bytes. 0 means unknown.

Example: `0`

workflowVersionIdstring · nullableRequired

ID of the workflow version this execution ran.

usedPrivateCredentialsbooleanRequired

Whether the execution used credentials that are not shared with the project.

Example: `false`

dataobjectOptional

Detailed execution data. Only included when `includeData` is `true`.

Show properties

customDataobjectOptional

Execution metadata set by the workflow. Only included when `includeData` is `true`.

Show properties

workflowDataobjectOptional

The workflow as it was saved when the execution ran. Only included when `includeData` is `true`. Older executions carry more fields than newer ones.

Show properties

dataTooLargeToDisplaybooleanOptional

Present and true when the execution data was larger than `EXECUTIONS_DATA_MAX_DISPLAY_SIZE`. `data` is then empty and `jsonSizeBytes` holds the real size. Use `ignoreDataSizeLimit` to read it anyway.

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/executions/{executionId}

HTTP

Copy

    GET /api/v1/executions/{executionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "1000",
      "mode": "manual",
      "retryOf": "text",
      "retrySuccessId": "2",
      "status": "canceled",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "startedAt": "2026-01-01T00:00:00.000Z",
      "stoppedAt": "2026-01-01T00:00:00.000Z",
      "deletedAt": "2026-01-01T00:00:00.000Z",
      "workflowId": "1000",
      "waitTill": "2026-01-01T00:00:00.000Z",
      "storedAt": "db",
      "tracingContext": {
        "traceparent": "text",
        "tracestate": "text"
      },
      "deduplicationKey": "text",
      "jsonSizeBytes": 0,
      "binaryDataSizeBytes": 0,
      "workflowVersionId": "text",
      "usedPrivateCredentials": false,
      "data": {
        "redactionInfo": {
          "isRedacted": true,
          "reason": "text",
          "canReveal": true
        },
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "customData": {
        "ANY_ADDITIONAL_PROPERTY": "text"
      },
      "workflowData": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "dataTooLargeToDisplay": true
    }

### Delete an execution[](https://docs.n8n.io/connect/n8n-api/executions#delete-executions-executionid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}

Deletes an execution from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

Responses

200

Operation successful.

application/json

idnumberRequired

ID of the deleted execution. This endpoint returns it as a number, where every other execution endpoint returns a string.

Example: `1000`

finishedbooleanRequiredDeprecated

Whether the execution ran to completion. Use `status` instead.

Example: `true`

modestring · enumRequiredExample: `manual`Possible values: `cli``error``integrated``internal``manual``retry``trigger``webhook``evaluation``chat``agent`

retryOfstring · nullableRequired

ID of the execution this one is a retry of.

retrySuccessIdstring · nullableRequired

ID of the retry that succeeded, if this execution failed and a retry did not.

Example: `2`

statusstring · enumRequiredPossible values: `canceled``crashed``error``new``running``success``unknown``waiting`

createdAtstring · date-timeRequired

startedAtstring · date-time · nullableRequired

Null until the execution leaves the queue and starts running.

stoppedAtstring · date-time · nullableRequired

When the execution stopped. Null for the `new`, `running` and `unknown` statuses; a `waiting` execution has stopped its current run, so it has a value.

deletedAtstring · date-time · nullableRequired

Always null. Soft-deleted executions are not returned.

workflowIdstringRequiredExample: `1000`

waitTillstring · date-time · nullableRequired

The time at which a waiting execution resumes.

storedAtstring · enumRequired

Where the execution data is stored.

Possible values: `db``fs``s3``az`

tracingContextobject · nullableRequired

W3C trace context propagated with the execution.

Show properties

deduplicationKeystring · nullableRequired

Key used to stop a duplicate execution from being created.

jsonSizeBytesnumberRequired

Size of the stored execution data in bytes. 0 means unknown.

Example: `0`

binaryDataSizeBytesnumberRequired

Size of the stored binary data in bytes. 0 means unknown.

Example: `0`

workflowVersionIdstring · nullableRequired

ID of the workflow version this execution ran.

usedPrivateCredentialsbooleanRequired

Whether the execution used credentials that are not shared with the project.

Example: `false`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/executions/{executionId}

HTTP

Copy

    DELETE /api/v1/executions/{executionId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": 1000,
      "mode": "manual",
      "retryOf": "text",
      "retrySuccessId": "2",
      "status": "canceled",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "startedAt": "2026-01-01T00:00:00.000Z",
      "stoppedAt": "2026-01-01T00:00:00.000Z",
      "deletedAt": "2026-01-01T00:00:00.000Z",
      "workflowId": "1000",
      "waitTill": "2026-01-01T00:00:00.000Z",
      "storedAt": "db",
      "tracingContext": {
        "traceparent": "text",
        "tracestate": "text"
      },
      "deduplicationKey": "text",
      "jsonSizeBytes": 0,
      "binaryDataSizeBytes": 0,
      "workflowVersionId": "text",
      "usedPrivateCredentials": false
    }

### Get execution tags[](https://docs.n8n.io/connect/n8n-api/executions#get-executions-executionid-tags)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}/tags

Get annotation tags for an execution.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

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

get/executions/{executionId}/tags

HTTP

Copy

    GET /api/v1/executions/{executionId}/tags HTTP/1.1
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

### Update tags of an execution[](https://docs.n8n.io/connect/n8n-api/executions#put-executions-executionid-tags)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}/tags

Update annotation tags of an execution.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

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

put/executions/{executionId}/tags

HTTP

Copy

    PUT /api/v1/executions/{executionId}/tags HTTP/1.1
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

### Stop multiple executions[](https://docs.n8n.io/connect/n8n-api/executions#post-executions-stop)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/stop

Stop multiple executions from your instance based on filter criteria.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

statusstring · enum\[\] · min: 1Required

Array of execution statuses to stop. Must include at least one status.

Example: `["queued","running","waiting"]`

Show properties

workflowIdstringOptional

Optional workflow ID to filter executions. If not provided, will stop executions across all accessible workflows. The literal value `all` has the same effect as omitting it.

Example: `2tUt1wbLX592XDdX`

startedAfterstring · date-timeOptional

Only stop executions that started after this time.

Example: `2024-01-01T00:00:00.000Z`

startedBeforestring · date-timeOptional

Only stop executions that started before this time.

Example: `2024-12-31T23:59:59.999Z`

Responses

200

Operation successful.

application/json

stoppedintegerRequired

The number of executions that were successfully stopped.

Example: `5`

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

post/executions/stop

HTTP

Copy

    POST /api/v1/executions/stop HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 158
    
    {
      "status": [\
        "queued",\
        "running",\
        "waiting"\
      ],
      "workflowId": "2tUt1wbLX592XDdX",
      "startedAfter": "2024-01-01T00:00:00.000Z",
      "startedBefore": "2024-12-31T23:59:59.999Z"
    }

Test it

200

Operation successful.

Copy

    {
      "stopped": 5
    }

### Stop an execution[](https://docs.n8n.io/connect/n8n-api/executions#post-executions-executionid-stop)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}/stop

Stop an execution by id.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Responses

200

Operation successful.

application/json

modestring · enumRequiredExample: `manual`Possible values: `cli``error``integrated``internal``manual``retry``trigger``webhook``evaluation``chat``agent`

startedAtstring · date-timeRequired

The time at which the execution started.

stoppedAtstring · date-timeOptional

The time at which the execution stopped. Absent when no stop time was recorded.

finishedbooleanRequiredDeprecated

Whether the execution ran to completion. Use `status` instead.

Example: `false`

statusstring · enumRequiredExample: `canceled`Possible values: `canceled``crashed``error``new``running``success``unknown``waiting`

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

post/executions/{executionId}/stop

HTTP

Copy

    POST /api/v1/executions/{executionId}/stop HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "mode": "manual",
      "startedAt": "2026-01-01T00:00:00.000Z",
      "stoppedAt": "2026-01-01T00:00:00.000Z",
      "status": "canceled"
    }

### Retry an execution[](https://docs.n8n.io/connect/n8n-api/executions#post-executions-executionid-retry)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/executions/{executionId}/retry

Retry an execution from your instance.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

executionIdinteger · min: 1Required

The ID of the execution.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

loadWorkflowbooleanOptional

Whether to load the currently saved workflow to execute instead of the one saved at the time of the execution. If set to true, it will retry with the latest version of the workflow.

Responses

200

Operation successful.

application/json

idstringRequired

ID of the new execution that the retry started.

Example: `1001`

modestring · enumRequiredExample: `retry`Possible values: `cli``error``integrated``internal``manual``retry``trigger``webhook``evaluation``chat``agent`

startedAtstring · date-time · nullableRequired

The time at which the new execution started.

workflowIdstringRequiredExample: `1000`

finishedbooleanRequiredDeprecated

Whether the execution ran to completion. Use `status` instead.

Example: `true`

retryOfstring · nullableRequired

ID of the execution this one is a retry of.

statusstring · enumRequiredPossible values: `canceled``crashed``error``new``running``success``unknown``waiting`

waitTillstring · date-time · nullableOptional

The time at which a waiting execution resumes.

dataobjectRequired

Run data of the new execution.

Show properties

workflowDataobjectRequired

The workflow as it was saved when the original execution ran. `loadWorkflow` changes which workflow the retry runs, not what this field reports.

Show properties

customDataobjectRequired

Execution metadata carried over from the original execution.

Show properties

annotationobjectOptional

Annotation on the original execution. Absent when it carries none.

Show properties

storedAtstring · enumRequired

Where the execution data is stored.

Possible values: `db``fs``s3``az`

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

post/executions/{executionId}/retry

HTTP

Copy

    POST /api/v1/executions/{executionId}/retry HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 21
    
    {
      "loadWorkflow": true
    }

Test it

200

Operation successful.

Copy

    {
      "id": "1001",
      "mode": "retry",
      "startedAt": "2026-01-01T00:00:00.000Z",
      "workflowId": "1000",
      "retryOf": "text",
      "status": "canceled",
      "waitTill": "2026-01-01T00:00:00.000Z",
      "data": {
        "redactionInfo": {
          "isRedacted": true,
          "reason": "text",
          "canReveal": true
        },
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "workflowData": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "customData": {
        "ANY_ADDITIONAL_PROPERTY": "text"
      },
      "annotation": {
        "id": 1,
        "vote": "up",
        "tags": [\
          {\
            "id": "text",\
            "name": "text"\
          }\
        ]
      },
      "storedAt": "db"
    }

[PreviousEvaluation](https://docs.n8n.io/connect/n8n-api/evaluation)
[NextFolders](https://docs.n8n.io/connect/n8n-api/folders)

Last updated 9 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/evaluation.md)
.

Copy

On this page

Operations about evaluation test runs

### Retrieve test runs[](https://docs.n8n.io/connect/n8n-api/evaluation#get-workflows-workflowid-test-runs)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/test-runs

Retrieve the evaluation test runs of a workflow.

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

statusstring · enumOptional

Status to filter the test runs by.

Possible values: `new``running``completed``error``cancelled`

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

nextCursorstring · nullableRequired

Paginate through test runs by setting the cursor parameter to the nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}/test-runs

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/test-runs HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "9f8e7d6c5b4a3210",\
          "status": "new",\
          "runAt": "2026-01-01T00:00:00.000Z",\
          "completedAt": "2026-01-01T00:00:00.000Z",\
          "metrics": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "errorCode": "text",\
          "errorDetails": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "finalResult": "success",\
          "testCaseCount": 42,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Trigger a test run[](https://docs.n8n.io/connect/n8n-api/evaluation#post-workflows-workflowid-test-runs)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/test-runs

Start a new evaluation test run for a workflow. The workflow must contain a configured evaluation trigger. Requires the `workflow:execute` project scope in addition to the `testRun:create` API key scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Responses

201

Operation successful.

application/json

idstringRequiredExample: `9f8e7d6c5b4a3210`

statusstring · enumRequiredPossible values: `new``running``completed``error``cancelled`

createdAtstring · date-timeRequired

400

The request is invalid or provides malformed data.

401

Unauthorized

402

Payment required

403

Forbidden

404

The specified resource was not found.

409

Conflict

422

Unprocessable Entity

post/workflows/{workflowId}/test-runs

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/test-runs HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

201

Operation successful.

Copy

    {
      "id": "9f8e7d6c5b4a3210",
      "status": "new",
      "createdAt": "2026-01-01T00:00:00.000Z"
    }

### Retrieve a test run[](https://docs.n8n.io/connect/n8n-api/evaluation#get-workflows-workflowid-test-runs-runid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/test-runs/{runId}

Retrieve a single evaluation test run of a workflow, including its aggregated metrics and final result.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

runIdstringRequired

The ID of the test run.

Responses

200

Operation successful.

application/json

idstringRequiredExample: `9f8e7d6c5b4a3210`

statusstring · enumRequiredPossible values: `new``running``completed``error``cancelled`

runAtstring · date-time · nullableRequired

completedAtstring · date-time · nullableRequired

metricsobject · nullableRequired

Aggregated metrics collected across the run's test cases.

Show properties

errorCodestring · nullableRequired

errorDetailsobject · nullableRequired

Show properties

finalResultstring · enum · nullableRequired

Overall result of the run, derived from its test cases once completed.

Possible values: `success``error``warning`

testCaseCountintegerRequiredExample: `42`

createdAtstring · date-timeRequired

updatedAtstring · date-timeRequired

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}/test-runs/{runId}

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/test-runs/{runId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "9f8e7d6c5b4a3210",
      "status": "new",
      "runAt": "2026-01-01T00:00:00.000Z",
      "completedAt": "2026-01-01T00:00:00.000Z",
      "metrics": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "errorCode": "text",
      "errorDetails": {
        "ANY_ADDITIONAL_PROPERTY": "anything"
      },
      "finalResult": "success",
      "testCaseCount": 42,
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z"
    }

### Retrieve test run cases[](https://docs.n8n.io/connect/n8n-api/evaluation#get-workflows-workflowid-test-runs-runid-test-cases)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/test-runs/{runId}/test-cases

Retrieve the per-case results of an evaluation test run.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

runIdstringRequired

The ID of the test run.

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

Paginate through test cases by setting the cursor parameter to the nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/workflows/{workflowId}/test-runs/{runId}/test-cases

HTTP

Copy

    GET /api/v1/workflows/{workflowId}/test-runs/{runId}/test-cases HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": "1a2b3c4d5e6f7080",\
          "status": "new",\
          "runAt": "2026-01-01T00:00:00.000Z",\
          "completedAt": "2026-01-01T00:00:00.000Z",\
          "metrics": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "errorCode": "text",\
          "errorDetails": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "inputs": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "outputs": {\
            "ANY_ADDITIONAL_PROPERTY": "anything"\
          },\
          "executionId": 1\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Cancel a test run[](https://docs.n8n.io/connect/n8n-api/evaluation#post-workflows-workflowid-test-runs-runid-cancel)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/workflows/{workflowId}/test-runs/{runId}/cancel

Cancel a running evaluation test run of a workflow. Requires the `workflow:execute` project scope in addition to the `testRun:cancel` API key scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

workflowIdstringRequired

The ID of the workflow.

runIdstringRequired

The ID of the test run.

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Responses

202

Operation successful.

application/json

idstringRequiredExample: `9f8e7d6c5b4a3210`

statusstring · enumRequiredPossible values: `cancelled`

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

post/workflows/{workflowId}/test-runs/{runId}/cancel

HTTP

Copy

    POST /api/v1/workflows/{workflowId}/test-runs/{runId}/cancel HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

202

Operation successful.

Copy

    {
      "id": "9f8e7d6c5b4a3210",
      "status": "cancelled"
    }

[PreviousDiscover](https://docs.n8n.io/connect/n8n-api/discover)
[NextExecutions](https://docs.n8n.io/connect/n8n-api/executions)

Last updated 9 days ago

Was this helpful?
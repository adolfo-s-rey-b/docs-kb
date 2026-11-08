For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/settings-otel.md)
.

Copy

On this page

Operations about OpenTelemetry settings

### Retrieve the OpenTelemetry configuration[](https://docs.n8n.io/connect/n8n-api/settings-otel#get-settings-otel)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/otel

Retrieve the current OpenTelemetry configuration, including every field exposed in the UI. Requires the `otel:manage` scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

The OpenTelemetry configuration, matching the fields exposed in the UI. On a write this is a full replacement: every field must be provided, except `exporterProtocol`, which defaults to `http/protobuf` when omitted, and `emitWorkflowStartSpan` and `emitNodeStartSpan`, which default to `false` when omitted. Fields managed declaratively via environment variables are returned with their effective value. A write can repeat these values, but changing them returns 409.

enabledbooleanRequired

Whether OpenTelemetry tracing is enabled.

Example: `true`

exporterProtocolstring · enumRequired

The wire protocol used to export spans. Collectors conventionally serve OTLP/HTTP on port 4318 and OTLP/gRPC on port 4317. The endpoint scheme (`http://` or `https://`) controls TLS for both protocols. Optional: a write that omits it selects `http/protobuf`, but an instance that sets this field to another value with an environment variable rejects that write with 409.

Default: `http/protobuf`Example: `http/protobuf`Possible values: `http/protobuf``grpc`

exporterEndpointstring · uriRequired

The base URL of the OTLP collector to export traces to. The value must be an `http://` or `https://` URL, because the scheme selects TLS — for gRPC, `https://` uses SSL and `http://` is plaintext.

Example: `http://localhost:4318`

exporterTracingPathstringRequired

The path appended to the endpoint for the OTLP traces signal. Ignored when `exporterProtocol` is `grpc`, which takes no URL path.

Example: `/v1/traces`

exporterServiceNamestring · min: 1Required

The `service.name` resource attribute reported on every span.

Example: `n8n`

exporterHeadersstringRequired

Additional headers sent to the OTLP collector, as a single string of comma-separated `key=value` pairs (e.g. `authorization=Bearer my-token,x-tenant-id=acme`). Whitespace around each key and value is trimmed; a value may contain spaces but not commas. Use an empty string when unused.

Example: `authorization=Bearer my-token,x-tenant-id=acme`

tracesSampleRatenumber · max: 1Required

The ratio of traces to sample, between 0 (none) and 1 (all).

Example: `1`

startupConnectivityTimeoutMsintegerRequired

How long, in milliseconds, to wait when checking the collector is reachable. Also used as the timeout for the test-trace endpoint.

Example: `2000`

includeNodeSpansbooleanRequired

Whether to emit a span for each node execution in addition to the workflow span.

Example: `true`

emitWorkflowStartSpanbooleanRequired

Whether to emit a `workflow.execute.started` span with a duration of 0 ms when each execution or resumed segment starts. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Example: `false`

emitNodeStartSpanbooleanRequired

Whether to emit a `node.execute.started` span with a duration of 0 ms when each node span starts. This doubles the number of node spans. Has no effect when `includeNodeSpans` is false. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Example: `false`

injectOutboundbooleanRequired

Whether to inject trace context headers into outbound HTTP requests made by nodes.

Example: `true`

productionExecutionsOnlybooleanRequired

When true, only production executions of published (active) workflows are traced, not manual/test runs.

Example: `true`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/settings/otel

HTTP

Copy

    GET /api/v1/settings/otel HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "enabled": true,
      "exporterProtocol": "http/protobuf",
      "exporterEndpoint": "http://localhost:4318",
      "exporterTracingPath": "/v1/traces",
      "exporterServiceName": "n8n",
      "exporterHeaders": "authorization=Bearer my-token,x-tenant-id=acme",
      "tracesSampleRate": 1,
      "startupConnectivityTimeoutMs": 2000,
      "includeNodeSpans": true,
      "emitWorkflowStartSpan": false,
      "emitNodeStartSpan": false,
      "injectOutbound": true,
      "productionExecutionsOnly": true
    }

### Set the OpenTelemetry configuration[](https://docs.n8n.io/connect/n8n-api/settings-otel#put-settings-otel)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/otel

Set the OpenTelemetry configuration. This is a full replacement: every field must be provided, and a partial body is rejected. The exceptions are `exporterProtocol`, which defaults to `http/protobuf` when omitted, and `emitWorkflowStartSpan` and `emitNodeStartSpan`, which default to `false` when omitted. The update takes effect exactly as it would from the UI, using the same validation, and is applied to the running instance immediately. Fields managed declaratively via environment variables are read-only: attempting to change one is rejected with 409, while re-submitting its current value (as returned by GET) is accepted. Requires the `otel:manage` scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

The OpenTelemetry configuration, matching the fields exposed in the UI. On a write this is a full replacement: every field must be provided, except `exporterProtocol`, which defaults to `http/protobuf` when omitted, and `emitWorkflowStartSpan` and `emitNodeStartSpan`, which default to `false` when omitted. Fields managed declaratively via environment variables are returned with their effective value. A write can repeat these values, but changing them returns 409.

enabledbooleanRequired

Whether OpenTelemetry tracing is enabled.

Example: `true`

exporterProtocolstring · enumOptional

The wire protocol used to export spans. Collectors conventionally serve OTLP/HTTP on port 4318 and OTLP/gRPC on port 4317. The endpoint scheme (`http://` or `https://`) controls TLS for both protocols. Optional: a write that omits it selects `http/protobuf`, but an instance that sets this field to another value with an environment variable rejects that write with 409.

Default: `http/protobuf`Example: `http/protobuf`Possible values: `http/protobuf``grpc`

exporterEndpointstring · uriRequired

The base URL of the OTLP collector to export traces to. The value must be an `http://` or `https://` URL, because the scheme selects TLS — for gRPC, `https://` uses SSL and `http://` is plaintext.

Example: `http://localhost:4318`Pattern: `^https?:\/\/`

exporterTracingPathstringRequired

The path appended to the endpoint for the OTLP traces signal. Ignored when `exporterProtocol` is `grpc`, which takes no URL path.

Example: `/v1/traces`

exporterServiceNamestring · min: 1Required

The `service.name` resource attribute reported on every span.

Example: `n8n`

exporterHeadersstringRequired

Additional headers sent to the OTLP collector, as a single string of comma-separated `key=value` pairs (e.g. `authorization=Bearer my-token,x-tenant-id=acme`). Whitespace around each key and value is trimmed; a value may contain spaces but not commas. Use an empty string when unused.

Example: `authorization=Bearer my-token,x-tenant-id=acme`

tracesSampleRatenumber · max: 1Required

The ratio of traces to sample, between 0 (none) and 1 (all).

Example: `1`

startupConnectivityTimeoutMsintegerRequired

How long, in milliseconds, to wait when checking the collector is reachable. Also used as the timeout for the test-trace endpoint.

Example: `2000`

includeNodeSpansbooleanRequired

Whether to emit a span for each node execution in addition to the workflow span.

Example: `true`

emitWorkflowStartSpanbooleanOptional

Whether to emit a `workflow.execute.started` span with a duration of 0 ms when each execution or resumed segment starts. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Default: `false`Example: `false`

emitNodeStartSpanbooleanOptional

Whether to emit a `node.execute.started` span with a duration of 0 ms when each node span starts. This doubles the number of node spans. Has no effect when `includeNodeSpans` is false. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Default: `false`Example: `false`

injectOutboundbooleanRequired

Whether to inject trace context headers into outbound HTTP requests made by nodes.

Example: `true`

productionExecutionsOnlybooleanRequired

When true, only production executions of published (active) workflows are traced, not manual/test runs.

Example: `true`

Responses

200

Operation successful.

application/json

The OpenTelemetry configuration, matching the fields exposed in the UI. On a write this is a full replacement: every field must be provided, except `exporterProtocol`, which defaults to `http/protobuf` when omitted, and `emitWorkflowStartSpan` and `emitNodeStartSpan`, which default to `false` when omitted. Fields managed declaratively via environment variables are returned with their effective value. A write can repeat these values, but changing them returns 409.

enabledbooleanRequired

Whether OpenTelemetry tracing is enabled.

Example: `true`

exporterProtocolstring · enumRequired

The wire protocol used to export spans. Collectors conventionally serve OTLP/HTTP on port 4318 and OTLP/gRPC on port 4317. The endpoint scheme (`http://` or `https://`) controls TLS for both protocols. Optional: a write that omits it selects `http/protobuf`, but an instance that sets this field to another value with an environment variable rejects that write with 409.

Default: `http/protobuf`Example: `http/protobuf`Possible values: `http/protobuf``grpc`

exporterEndpointstring · uriRequired

The base URL of the OTLP collector to export traces to. The value must be an `http://` or `https://` URL, because the scheme selects TLS — for gRPC, `https://` uses SSL and `http://` is plaintext.

Example: `http://localhost:4318`

exporterTracingPathstringRequired

The path appended to the endpoint for the OTLP traces signal. Ignored when `exporterProtocol` is `grpc`, which takes no URL path.

Example: `/v1/traces`

exporterServiceNamestring · min: 1Required

The `service.name` resource attribute reported on every span.

Example: `n8n`

exporterHeadersstringRequired

Additional headers sent to the OTLP collector, as a single string of comma-separated `key=value` pairs (e.g. `authorization=Bearer my-token,x-tenant-id=acme`). Whitespace around each key and value is trimmed; a value may contain spaces but not commas. Use an empty string when unused.

Example: `authorization=Bearer my-token,x-tenant-id=acme`

tracesSampleRatenumber · max: 1Required

The ratio of traces to sample, between 0 (none) and 1 (all).

Example: `1`

startupConnectivityTimeoutMsintegerRequired

How long, in milliseconds, to wait when checking the collector is reachable. Also used as the timeout for the test-trace endpoint.

Example: `2000`

includeNodeSpansbooleanRequired

Whether to emit a span for each node execution in addition to the workflow span.

Example: `true`

emitWorkflowStartSpanbooleanRequired

Whether to emit a `workflow.execute.started` span with a duration of 0 ms when each execution or resumed segment starts. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Example: `false`

emitNodeStartSpanbooleanRequired

Whether to emit a `node.execute.started` span with a duration of 0 ms when each node span starts. This doubles the number of node spans. Has no effect when `includeNodeSpans` is false. Optional: a write that omits it selects `false`, but an instance that sets this field to `true` with an environment variable rejects that write with 409.

Example: `false`

injectOutboundbooleanRequired

Whether to inject trace context headers into outbound HTTP requests made by nodes.

Example: `true`

productionExecutionsOnlybooleanRequired

When true, only production executions of published (active) workflows are traced, not manual/test runs.

Example: `true`

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

put/settings/otel

HTTP

Copy

    PUT /api/v1/settings/otel HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 415
    
    {
      "enabled": true,
      "exporterProtocol": "http/protobuf",
      "exporterEndpoint": "http://localhost:4318",
      "exporterTracingPath": "/v1/traces",
      "exporterServiceName": "n8n",
      "exporterHeaders": "authorization=Bearer my-token,x-tenant-id=acme",
      "tracesSampleRate": 1,
      "startupConnectivityTimeoutMs": 2000,
      "includeNodeSpans": true,
      "emitWorkflowStartSpan": false,
      "emitNodeStartSpan": false,
      "injectOutbound": true,
      "productionExecutionsOnly": true
    }

Test it

200

Operation successful.

Copy

    {
      "enabled": true,
      "exporterProtocol": "http/protobuf",
      "exporterEndpoint": "http://localhost:4318",
      "exporterTracingPath": "/v1/traces",
      "exporterServiceName": "n8n",
      "exporterHeaders": "authorization=Bearer my-token,x-tenant-id=acme",
      "tracesSampleRate": 1,
      "startupConnectivityTimeoutMs": 2000,
      "includeNodeSpans": true,
      "emitWorkflowStartSpan": false,
      "emitNodeStartSpan": false,
      "injectOutbound": true,
      "productionExecutionsOnly": true
    }

### Test the connection to an OTLP collector[](https://docs.n8n.io/connect/n8n-api/settings-otel#post-settings-otel-test-trace)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/otel/test-trace

Send a single test span to the given OTLP collector and report whether it was accepted. This tests the supplied connection details without changing the stored configuration. Fields managed declaratively via environment variables are overridden with their effective value before the test is sent. Requires the `otel:manage` scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

The connection details to test against an OTLP collector. Fields managed declaratively via environment variables are overridden with their effective value before the test is sent.

exporterProtocolstring · enumOptional

The wire protocol used to send the test span. Collectors conventionally serve OTLP/HTTP on port 4318 and OTLP/gRPC on port 4317. The endpoint scheme (`http://` or `https://`) controls TLS for both protocols. Optional: omitting it selects `http/protobuf`, unless an environment variable manages this field, which then supplies the value.

Default: `http/protobuf`Example: `http/protobuf`Possible values: `http/protobuf``grpc`

exporterEndpointstring · uriRequired

The base URL of the OTLP collector to export traces to. The value must be an `http://` or `https://` URL, because the scheme selects TLS — for gRPC, `https://` uses SSL and `http://` is plaintext.

Example: `http://localhost:4318`Pattern: `^https?:\/\/`

exporterTracingPathstringRequired

The path appended to the endpoint for the OTLP traces signal. Ignored when `exporterProtocol` is `grpc`, which takes no URL path.

Example: `/v1/traces`

exporterServiceNamestring · min: 1Required

The `service.name` resource attribute reported on the test span.

Example: `n8n`

exporterHeadersstringRequired

Additional headers sent to the OTLP collector, as a single string of comma-separated `key=value` pairs (e.g. `authorization=Bearer my-token,x-tenant-id=acme`). Whitespace around each key and value is trimmed; a value may contain spaces but not commas. Use an empty string when unused.

Example: `authorization=Bearer my-token,x-tenant-id=acme`

startupConnectivityTimeoutMsintegerRequired

How long, in milliseconds, to wait for the collector to respond.

Example: `2000`

Responses

200

Operation successful.

application/json

The outcome of the test connection to the OTLP collector.

successbooleanRequired

Whether the test span was accepted by the collector.

Example: `true`

errorstringOptional

The error reported by the collector or exporter. Present only when `success` is false.

Example: `Failed to connect: 401 Unauthorized`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

415

Unsupported media type.

post/settings/otel/test-trace

HTTP

Copy

    POST /api/v1/settings/otel/test-trace HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 245
    
    {
      "exporterProtocol": "http/protobuf",
      "exporterEndpoint": "http://localhost:4318",
      "exporterTracingPath": "/v1/traces",
      "exporterServiceName": "n8n",
      "exporterHeaders": "authorization=Bearer my-token,x-tenant-id=acme",
      "startupConnectivityTimeoutMs": 2000
    }

Test it

200

Operation successful.

Copy

    {
      "success": true,
      "error": "Failed to connect: 401 Unauthorized"
    }

[PreviousSettings Ldap](https://docs.n8n.io/connect/n8n-api/settings-ldap)
[NextSettings Sso Oidc](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc)

Last updated 9 days ago

Was this helpful?
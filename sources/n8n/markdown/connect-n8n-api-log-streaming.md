For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/log-streaming.md)
.

Copy

On this page

Operations about log streaming destinations

### List streamable event types[](https://docs.n8n.io/connect/n8n-api/log-streaming#get-settings-log-streaming-event-types)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/event-types

List the event types that can be streamed to a log streaming destination. Requires the `eventBusDestination:list` scope and the Log Streaming feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

datastring\[\]Required

Event names that can be streamed to a destination.

Example: `["n8n.workflow.started","n8n.workflow.success","n8n.workflow.failed"]`

401

Unauthorized

403

Forbidden

get/settings/log-streaming/event-types

HTTP

Copy

    GET /api/v1/settings/log-streaming/event-types HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        "n8n.workflow.started",\
        "n8n.workflow.success",\
        "n8n.workflow.failed"\
      ]
    }

### List log streaming destinations[](https://docs.n8n.io/connect/n8n-api/log-streaming#get-settings-log-streaming-destinations)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations

List the configured log streaming destinations. Requires the `eventBusDestination:list` scope and the Log Streaming feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

dataone of\[\]Required

The configured log streaming destinations.

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

401

Unauthorized

403

Forbidden

get/settings/log-streaming/destinations

HTTP

Copy

    GET /api/v1/settings/log-streaming/destinations HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "label": "My destination",\
          "enabled": true,\
          "subscribedEvents": [\
            "n8n.workflow",\
            "n8n.audit"\
          ],\
          "anonymizeAuditMessages": false,\
          "circuitBreaker": {\
            "maxFailures": 1,\
            "failureWindow": 1\
          },\
          "type": "webhook",\
          "url": "https://example.com/n8n-events",\
          "method": "POST",\
          "sendHeaders": false,\
          "specifyHeaders": "keypair",\
          "headerParameters": {\
            "parameters": [\
              {\
                "name": "Authorization",\
                "value": "Bearer <token>"\
              }\
            ]\
          },\
          "jsonHeaders": "text",\
          "sendQuery": false,\
          "specifyQuery": "text",\
          "queryParameters": {\
            "parameters": [\
              {\
                "name": "Authorization",\
                "value": "Bearer <token>"\
              }\
            ]\
          },\
          "jsonQuery": "text",\
          "options": {\
            "timeout": 1,\
            "allowUnauthorizedCerts": true,\
            "queryParameterArrays": "indices",\
            "redirect": {\
              "redirect": {\
                "followRedirects": true,\
                "maxRedirects": 1\
              }\
            },\
            "proxy": {\
              "proxy": {\
                "protocol": "https",\
                "host": "text",\
                "port": 1\
              }\
            },\
            "socket": {\
              "keepAlive": true,\
              "maxSockets": 1,\
              "maxFreeSockets": 1\
            }\
          },\
          "id": "88be6560-bfb4-455c-8aa1-06971e9e5522"\
        }\
      ]
    }

### Create a log streaming destination[](https://docs.n8n.io/connect/n8n-api/log-streaming#post-settings-log-streaming-destinations)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations

Create a log streaming destination. The destination takes effect exactly as it would from the UI, using the same validation. Requires the `eventBusDestination:create` scope and the Log Streaming feature to be licensed. When destinations are managed via environment variables, the write is rejected with 409 and nothing is created; reads still return the current values.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

Responses

200

Operation successful.

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

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

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/settings/log-streaming/destinations

HTTP

Copy

    POST /api/v1/settings/log-streaming/destinations HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 820
    
    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      }
    }

Test it

200

Operation successful.

Copy

    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      },
      "id": "88be6560-bfb4-455c-8aa1-06971e9e5522"
    }

### Retrieve a log streaming destination[](https://docs.n8n.io/connect/n8n-api/log-streaming#get-settings-log-streaming-destinations-destinationid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations/{destinationId}

Retrieve a single log streaming destination by id. Requires the `eventBusDestination:read` scope and the Log Streaming feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

destinationIdstringRequired

The id of the log streaming destination.

Responses

200

Operation successful.

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/settings/log-streaming/destinations/{destinationId}

HTTP

Copy

    GET /api/v1/settings/log-streaming/destinations/{destinationId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      },
      "id": "88be6560-bfb4-455c-8aa1-06971e9e5522"
    }

### Update a log streaming destination[](https://docs.n8n.io/connect/n8n-api/log-streaming#put-settings-log-streaming-destinations-destinationid)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations/{destinationId}

Replace an existing log streaming destination. The update takes effect exactly as it would from the UI, using the same validation. Requires the `eventBusDestination:update` scope and the Log Streaming feature to be licensed. When destinations are managed via environment variables, the write is rejected with 409 and nothing is changed; reads still return the current values.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

destinationIdstringRequired

The id of the log streaming destination.

Body

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

Responses

200

Operation successful.

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

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

put/settings/log-streaming/destinations/{destinationId}

HTTP

Copy

    PUT /api/v1/settings/log-streaming/destinations/{destinationId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 820
    
    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      }
    }

Test it

200

Operation successful.

Copy

    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      },
      "id": "88be6560-bfb4-455c-8aa1-06971e9e5522"
    }

### Delete a log streaming destination[](https://docs.n8n.io/connect/n8n-api/log-streaming#delete-settings-log-streaming-destinations-destinationid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations/{destinationId}

Remove a log streaming destination. Requires the `eventBusDestination:delete` scope and the Log Streaming feature to be licensed. When destinations are managed via environment variables, the delete is rejected with 409 and nothing is removed; reads still return the current values.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

destinationIdstringRequired

The id of the log streaming destination.

Responses

200

Operation successful.

application/json

A log streaming destination. The `type` field selects the variant and its type-specific fields: `webhook`, `syslog`, or `sentry`.

objectOptional

Show properties

or

objectOptional

Show properties

or

objectOptional

Show properties

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Conflict

delete/settings/log-streaming/destinations/{destinationId}

HTTP

Copy

    DELETE /api/v1/settings/log-streaming/destinations/{destinationId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "label": "My destination",
      "enabled": true,
      "subscribedEvents": [\
        "n8n.workflow",\
        "n8n.audit"\
      ],
      "anonymizeAuditMessages": false,
      "circuitBreaker": {
        "maxFailures": 1,
        "failureWindow": 1
      },
      "type": "webhook",
      "url": "https://example.com/n8n-events",
      "method": "POST",
      "sendHeaders": false,
      "specifyHeaders": "keypair",
      "headerParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonHeaders": "text",
      "sendQuery": false,
      "specifyQuery": "text",
      "queryParameters": {
        "parameters": [\
          {\
            "name": "Authorization",\
            "value": "Bearer <token>"\
          }\
        ]
      },
      "jsonQuery": "text",
      "options": {
        "timeout": 1,
        "allowUnauthorizedCerts": true,
        "queryParameterArrays": "indices",
        "redirect": {
          "redirect": {
            "followRedirects": true,
            "maxRedirects": 1
          }
        },
        "proxy": {
          "proxy": {
            "protocol": "https",
            "host": "text",
            "port": 1
          }
        },
        "socket": {
          "keepAlive": true,
          "maxSockets": 1,
          "maxFreeSockets": 1
        }
      },
      "id": "88be6560-bfb4-455c-8aa1-06971e9e5522"
    }

### Send a test message to a log streaming destination[](https://docs.n8n.io/connect/n8n-api/log-streaming#post-settings-log-streaming-destinations-destinationid-test)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/log-streaming/destinations/{destinationId}/test

Send a test message to the destination to verify it is reachable and configured correctly. Requires the `eventBusDestination:test` scope and the Log Streaming feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

destinationIdstringRequired

The id of the log streaming destination.

Responses

200

Operation successful.

application/json

successbooleanRequired

Whether the test message was delivered to the destination successfully.

Example: `true`

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

post/settings/log-streaming/destinations/{destinationId}/test

HTTP

Copy

    POST /api/v1/settings/log-streaming/destinations/{destinationId}/test HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "success": true
    }

[PreviousInsights](https://docs.n8n.io/connect/n8n-api/insights)
[NextN8n Package](https://docs.n8n.io/connect/n8n-api/n8n-package)

Last updated 9 days ago

Was this helpful?
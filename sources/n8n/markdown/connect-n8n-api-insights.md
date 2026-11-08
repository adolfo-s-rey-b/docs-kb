For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/insights.md)
.

Copy

On this page

Operations about insights

### Retrieve insights summary[](https://docs.n8n.io/connect/n8n-api/insights#get-insights-summary)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/insights/summary

Retrieve the insights summary for the selected date range.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

startDatestring · date-timeOptional

ISO 8601 start date. Defaults to 7 days ago.

endDatestring · date-timeOptional

ISO 8601 end date. Defaults to now.

projectIdstringOptional

Project identifier to filter insights by project.

Example: `VmwOO9HeTEj20kxM`

Responses

200

Operation successful.

application/json

totalobjectRequired

Show properties

failedobjectRequired

Show properties

failureRateobjectRequired

Show properties

timeSavedobjectRequired

Show properties

averageRunTimeobjectRequired

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/insights/summary

HTTP

Copy

    GET /api/v1/insights/summary HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "total": {
        "value": 1,
        "deviation": 1,
        "unit": "count"
      },
      "failed": {
        "value": 1,
        "deviation": 1,
        "unit": "count"
      },
      "failureRate": {
        "value": 1,
        "deviation": 1,
        "unit": "ratio"
      },
      "timeSaved": {
        "value": 1,
        "deviation": 1,
        "unit": "minute"
      },
      "averageRunTime": {
        "value": 1,
        "deviation": 1,
        "unit": "millisecond"
      }
    }

[PreviousFolders](https://docs.n8n.io/connect/n8n-api/folders)
[NextLog Streaming](https://docs.n8n.io/connect/n8n-api/log-streaming)

Last updated 9 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/data-table.md)
.

Copy

On this page

Operations about data tables and their rows

### List all data tables[](https://docs.n8n.io/connect/n8n-api/data-table#get-data-tables)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables

Retrieve a list of all data tables with optional filtering, sorting, and pagination. Each table includes `sizeBytes`, the value the `size` sort option orders by.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

filterstring · jsonStringOptional

JSON string of filter conditions

Example: `{"name":"my-table"}`

sortBystring · enumOptional

Sort format: field:asc or field:desc

Example: `name:asc`Possible values: `name:asc``name:desc``createdAt:asc``createdAt:desc``updatedAt:asc``updatedAt:desc``size:asc``size:desc`

Responses

200

Operation successful.

application/json

dataobject\[\]Required

Show properties

nextCursorstring · nullableRequired

Paginate through data tables by setting the cursor parameter to a nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/data-tables

HTTP

Copy

    GET /api/v1/data-tables HTTP/1.1
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
          "columns": [\
            {\
              "id": "text",\
              "name": "text",\
              "type": "string",\
              "index": 1,\
              "createdAt": "2026-01-01T00:00:00.000Z",\
              "updatedAt": "2026-01-01T00:00:00.000Z"\
            }\
          ],\
          "projectId": "text",\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z",\
          "sizeBytes": 1\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Create a new data table[](https://docs.n8n.io/connect/n8n-api/data-table#post-data-tables)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables

Create a new data table in your personal project or a team project you have access to.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · min: 1 · max: 128Required

Name of the data table

Example: `customers`

columnsobject\[\]Required

Column definitions for the table

Show properties

projectIdstringOptional

ID of the project to create the table in. When omitted, the table is created in the user's personal project.

Example: `a1b2c3d4`

fileIdstringOptional

ID of a CSV file that you uploaded in the n8n editor. If you set it, n8n fills the new table with the rows from that file. Only a session-authenticated caller can upload a file, so an API-key caller cannot use this field.

hasHeadersbooleanOptional

Set to true if the first row of the CSV file holds the column names. Applies only when you set `fileId`. The default is true.

Responses

201

Operation successful.

application/json

idstringRequired

Unique identifier for the data table

namestringRequired

Name of the data table

columnsobject\[\]Required

Column definitions

Show properties

projectIdstringRequired

ID of the project this table belongs to

createdAtstring · date-timeRequired

Timestamp when the table was created

updatedAtstring · date-timeRequired

Timestamp when the table was last updated

sizeBytesintegerRequired

Physical storage in bytes, including indexes and internal overhead. Not reduced immediately by row deletion, and may be a few seconds stale.

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

post/data-tables

HTTP

Copy

    POST /api/v1/data-tables HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 153
    
    {
      "name": "customers",
      "columns": [\
        {\
          "name": "text",\
          "type": "string",\
          "csvColumnName": "Email Address"\
        }\
      ],
      "projectId": "a1b2c3d4",
      "fileId": "text",
      "hasHeaders": true
    }

Test it

201

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "columns": [\
        {\
          "id": "text",\
          "name": "text",\
          "type": "string",\
          "index": 1,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "projectId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "sizeBytes": 1
    }

### Get a data table[](https://docs.n8n.io/connect/n8n-api/data-table#get-data-tables-datatableid)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}

Retrieve a specific data table by ID.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Responses

200

Operation successful.

application/json

idstringRequired

Unique identifier for the data table

namestringRequired

Name of the data table

columnsobject\[\]Required

Column definitions

Show properties

projectIdstringRequired

ID of the project this table belongs to

createdAtstring · date-timeRequired

Timestamp when the table was created

updatedAtstring · date-timeRequired

Timestamp when the table was last updated

sizeBytesintegerRequired

Physical storage in bytes, including indexes and internal overhead. Not reduced immediately by row deletion, and may be a few seconds stale.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/data-tables/{dataTableId}

HTTP

Copy

    GET /api/v1/data-tables/{dataTableId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "columns": [\
        {\
          "id": "text",\
          "name": "text",\
          "type": "string",\
          "index": 1,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "projectId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "sizeBytes": 1
    }

### Delete a data table[](https://docs.n8n.io/connect/n8n-api/data-table#delete-data-tables-datatableid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}

Delete a data table. This will also delete all rows in the table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Responses

204

Operation successful.

No content

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/data-tables/{dataTableId}

HTTP

Copy

    DELETE /api/v1/data-tables/{dataTableId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Update a data table[](https://docs.n8n.io/connect/n8n-api/data-table#patch-data-tables-datatableid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}

Update a data table's name.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Body

application/json

namestring · min: 1 · max: 128Required

New name for the data table

Example: `updated-customers`

Responses

200

Operation successful.

application/json

idstringRequired

Unique identifier for the data table

namestringRequired

Name of the data table

columnsobject\[\]Required

Column definitions

Show properties

projectIdstringRequired

ID of the project this table belongs to

createdAtstring · date-timeRequired

Timestamp when the table was created

updatedAtstring · date-timeRequired

Timestamp when the table was last updated

sizeBytesintegerRequired

Physical storage in bytes, including indexes and internal overhead. Not reduced immediately by row deletion, and may be a few seconds stale.

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

patch/data-tables/{dataTableId}

HTTP

Copy

    PATCH /api/v1/data-tables/{dataTableId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 28
    
    {
      "name": "updated-customers"
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "columns": [\
        {\
          "id": "text",\
          "name": "text",\
          "type": "string",\
          "index": 1,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "projectId": "text",
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "sizeBytes": 1
    }

### List columns of a data table[](https://docs.n8n.io/connect/n8n-api/data-table#get-data-tables-datatableid-columns)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/columns

Retrieve all columns for a specific data table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Responses

200

Operation successful.

application/json

idstringRequired

Column ID

namestringRequired

Column name

typestring · enumRequired

Column data type

Possible values: `string``number``boolean``date`

indexintegerRequired

Column position

createdAtstring · date-timeRequired

Timestamp when the column was created

updatedAtstring · date-timeRequired

Timestamp when the column was last updated

dataTableIdstringRequired

ID of the data table this column belongs to

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/data-tables/{dataTableId}/columns

HTTP

Copy

    GET /api/v1/data-tables/{dataTableId}/columns HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    [\
      {\
        "id": "text",\
        "name": "text",\
        "type": "string",\
        "index": 1,\
        "createdAt": "2026-01-01T00:00:00.000Z",\
        "updatedAt": "2026-01-01T00:00:00.000Z",\
        "dataTableId": "text"\
      }\
    ]

### Add a column to a data table[](https://docs.n8n.io/connect/n8n-api/data-table#post-data-tables-datatableid-columns)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/columns

Add a new column to an existing data table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

namestring · min: 1 · max: 63Required

Column name. Must start with a letter; only letters, digits, and underscores after that; maximum 63 characters.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`

typestring · enumRequired

Column data type

Possible values: `string``number``boolean``date`

indexintegerOptional

Column position (optional, appended to end if omitted)

Responses

201

Operation successful.

application/json

idstringRequired

Column ID

namestringRequired

Column name

typestring · enumRequired

Column data type

Possible values: `string``number``boolean``date`

indexintegerRequired

Column position

createdAtstring · date-timeRequired

Timestamp when the column was created

updatedAtstring · date-timeRequired

Timestamp when the column was last updated

dataTableIdstringRequired

ID of the data table this column belongs to

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

post/data-tables/{dataTableId}/columns

HTTP

Copy

    POST /api/v1/data-tables/{dataTableId}/columns HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 41
    
    {
      "name": "text",
      "type": "string",
      "index": 1
    }

Test it

201

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "string",
      "index": 1,
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "dataTableId": "text"
    }

### Delete a column[](https://docs.n8n.io/connect/n8n-api/data-table#delete-data-tables-datatableid-columns-columnid)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/columns/{columnId}

Remove a column from a data table. This will also delete all data in the column.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

columnIdstring · nanoidRequired

The ID of the column

Pattern: `^[A-Za-z0-9]{16}$`

Responses

204

Operation successful.

No content

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/data-tables/{dataTableId}/columns/{columnId}

HTTP

Copy

    DELETE /api/v1/data-tables/{dataTableId}/columns/{columnId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

204

Operation successful.

No content

### Update a column[](https://docs.n8n.io/connect/n8n-api/data-table#patch-data-tables-datatableid-columns-columnid)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/columns/{columnId}

Rename and/or reorder a column in a data table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

columnIdstring · nanoidRequired

The ID of the column

Pattern: `^[A-Za-z0-9]{16}$`

Body

application/json

namestring · min: 1 · max: 63Optional

Column name. Must start with a letter; only letters, digits, and underscores after that; maximum 63 characters.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`

indexintegerOptional

New zero-based position for the column

Responses

200

Operation successful.

application/json

idstringRequired

Column ID

namestringRequired

Column name

typestring · enumRequired

Column data type

Possible values: `string``number``boolean``date`

indexintegerRequired

Column position

createdAtstring · date-timeRequired

Timestamp when the column was created

updatedAtstring · date-timeRequired

Timestamp when the column was last updated

dataTableIdstringRequired

ID of the data table this column belongs to

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

patch/data-tables/{dataTableId}/columns/{columnId}

HTTP

Copy

    PATCH /api/v1/data-tables/{dataTableId}/columns/{columnId} HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 25
    
    {
      "name": "text",
      "index": 1
    }

Test it

200

Operation successful.

Copy

    {
      "id": "text",
      "name": "text",
      "type": "string",
      "index": 1,
      "createdAt": "2026-01-01T00:00:00.000Z",
      "updatedAt": "2026-01-01T00:00:00.000Z",
      "dataTableId": "text"
    }

### List rows of a data table[](https://docs.n8n.io/connect/n8n-api/data-table#get-data-tables-datatableid-rows)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows

Retrieve rows from a data table with optional filtering, sorting, and pagination.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

filterstring · jsonStringOptional

JSON string of filter conditions

Example: `{"type":"and","filters":[{"columnName":"status","condition":"eq","value":"active"}]}`

sortBystringOptional

Sort format: columnName:asc or columnName:desc

Example: `createdAt:desc`

searchstringOptional

Search text across all string columns

Responses

200

Operation successful.

application/json

dataobject\[\]Required

A data table row with system columns (id, createdAt, updatedAt) and user-defined columns

Show properties

nextCursorstring · nullableRequired

Paginate through rows by setting the cursor parameter to a nextCursor attribute returned by a previous request. Default value fetches the first "page" of the collection.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

get/data-tables/{dataTableId}/rows

HTTP

Copy

    GET /api/v1/data-tables/{dataTableId}/rows HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": 1,\
          "createdAt": "2026-01-01T00:00:00.000Z",\
          "updatedAt": "2026-01-01T00:00:00.000Z"\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Insert rows into a data table[](https://docs.n8n.io/connect/n8n-api/data-table#post-data-tables-datatableid-rows)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows

Insert one or more rows into a data table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

dataobject\[\] · min: 1Required

Array of rows to insert. Each row is an object with column names as keys.

Show properties

returnTypeany ofOptional

count: return only the number of rows inserted. id: return an array of objects with the id of each inserted row. all: return the full row data for all inserted rows.

Default: `count`

string · enumOptionalPossible values: `all`

or

string · enumOptionalPossible values: `count`

or

string · enumOptionalPossible values: `id`

Responses

200

Operation successful.

application/json

objectOptional

Returned when returnType is 'count'

Show properties

or

object\[\]Optional

Returned when returnType is 'id'

Show properties

or

object\[\]Optional

Returned when returnType is 'all'

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

post/data-tables/{dataTableId}/rows

HTTP

Copy

    POST /api/v1/data-tables/{dataTableId}/rows HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 66
    
    {
      "data": [\
        {\
          "ANY_ADDITIONAL_PROPERTY": "text"\
        }\
      ],
      "returnType": "count"
    }

Test it

200

Operation successful.

Copy

    {
      "success": true,
      "insertedRows": 1
    }

### Upsert a row in a data table[](https://docs.n8n.io/connect/n8n-api/data-table#post-data-tables-datatableid-rows-upsert)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows/upsert

Update an existing row, or insert a new one if no row matches the filter conditions.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

filterobjectRequired

Filter conditions to match an existing row. If no row matches, n8n inserts a new row.

Show properties

dataobjectRequired

Column values for the row

Show properties

returnDatabooleanOptional

Set to true to return the upserted row(s): the matching rows if updated, or the new row if one was inserted. Set to false to return true on success.

Default: `false`

dryRunbooleanOptional

Set to true to preview the change without saving it.

Default: `false`

Responses

200

Operation successful.

application/json

booleanOptional

Returned when returnData is false and dryRun is false

or

object\[\]Optional

Returned when dryRun is true: one entry per row per before/after state

Show properties

or

object\[\]Optional

Returned when returnData is true and dryRun is false

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

post/data-tables/{dataTableId}/rows/upsert

HTTP

Copy

    POST /api/v1/data-tables/{dataTableId}/rows/upsert HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 167
    
    {
      "filter": {
        "type": "and",
        "filters": [\
          {\
            "columnName": "text",\
            "condition": "eq",\
            "value": "text"\
          }\
        ]
      },
      "data": {
        "ANY_ADDITIONAL_PROPERTY": "text"
      },
      "returnData": false,
      "dryRun": false
    }

Test it

200

Operation successful.

Copy

    true

### Update rows in a data table[](https://docs.n8n.io/connect/n8n-api/data-table#patch-data-tables-datatableid-rows-update)

patch

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows/update

Update rows matching filter conditions in a data table.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Body

application/json

filterobjectRequired

Filter conditions to match rows for update.

Show properties

dataobjectRequired

Column values to update

Show properties

returnDatabooleanOptional

Set to true to return the updated row(s). Set to false to return true on success.

Default: `false`

dryRunbooleanOptional

Set to true to preview the change without saving it.

Default: `false`

Responses

200

Operation successful.

application/json

booleanOptional

Returned when returnData is false and dryRun is false

or

object\[\]Optional

Returned when dryRun is true: one entry per row per before/after state

Show properties

or

object\[\]Optional

Returned when returnData is true and dryRun is false

Show properties

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

patch/data-tables/{dataTableId}/rows/update

HTTP

Copy

    PATCH /api/v1/data-tables/{dataTableId}/rows/update HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 167
    
    {
      "filter": {
        "type": "and",
        "filters": [\
          {\
            "columnName": "text",\
            "condition": "eq",\
            "value": "text"\
          }\
        ]
      },
      "data": {
        "ANY_ADDITIONAL_PROPERTY": "text"
      },
      "returnData": false,
      "dryRun": false
    }

Test it

200

Operation successful.

Copy

    true

### Clear all rows from a data table[](https://docs.n8n.io/connect/n8n-api/data-table#delete-data-tables-datatableid-rows-clear)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows/clear

Permanently delete all rows from a data table. The table structure is retained. This action cannot be undone.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Responses

200

Operation successful.

application/json

deletedCountintegerRequired

The number of rows that were deleted

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/data-tables/{dataTableId}/rows/clear

HTTP

Copy

    DELETE /api/v1/data-tables/{dataTableId}/rows/clear HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "deletedCount": 1
    }

### Delete rows from a data table[](https://docs.n8n.io/connect/n8n-api/data-table#delete-data-tables-datatableid-rows-delete)

delete

/api/v1Current n8n instance (self-hosted built-in playground)

/data-tables/{dataTableId}/rows/delete

Delete rows matching filter conditions from a data table. Filter is required to prevent accidental deletion of all data.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Path parameters

dataTableIdstring · nanoidRequired

The ID of the data table

Pattern: `^[A-Za-z0-9]{16}$`

Query parameters

filterstring · jsonStringRequired

JSON string of filter conditions. Required to prevent accidental deletion of all data.

Example: `{"type":"and","filters":[{"columnName":"status","condition":"eq","value":"archived"}]}`

returnDatastring · enumOptional

If true, return the deleted rows. If false, return true on success.

Default: `false`Possible values: `true``false`

dryRunstring · enumOptional

If true, preview which rows would be deleted without actually deleting them.

Default: `false`Possible values: `true``false`

Responses

200

Operation successful.

application/json

booleanOptional

Returned when returnData is false and dryRun is false

or

object\[\]Optional

Returned when dryRun is true: one entry per row per before/after state

Show properties

or

object\[\]Optional

Returned when returnData is true and dryRun is false

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

delete/data-tables/{dataTableId}/rows/delete

HTTP

Copy

    DELETE /api/v1/data-tables/{dataTableId}/rows/delete?filter=text HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    true

[PreviousCredential Type Policy](https://docs.n8n.io/connect/n8n-api/credential-type-policy)
[NextDiscover](https://docs.n8n.io/connect/n8n-api/discover)

Last updated 9 days ago

Was this helpful?
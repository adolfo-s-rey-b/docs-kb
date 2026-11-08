For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres.md)
.

Use the Postgres node to automate work in Postgres, and integrate Postgres with other applications. n8n has built-in support for a wide range of Postgres features, including executing queries, as well as inserting and updating rows in a database.

On this page, you'll find a list of operations the Postgres node supports and links to more resources.

**Credentials**

Refer to [Postgres credentials](https://docs.n8n.io/integrations/builtin/credentials/postgres)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#operations)

----------------------------------------------------------------------------------------------------

*   [**Delete**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#delete)
    : Delete an entire table or rows in a table
    
*   [**Execute Query**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#execute-query)
    : Execute an SQL query
    
*   [**Insert**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert)
    : Insert rows in a table
    
*   [**Insert or Update**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert-or-update)
    : Insert or update rows in a table
    
*   [**Select**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#select)
    : Select rows from a table
    
*   [**Update**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#update)
    : Update rows in a table
    

### Delete[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#delete)

Use this operation to delete an entire table or rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Delete**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
    
*   **Command**: The deletion action to take:
    
    *   **Truncate**: Removes the table's data but preserves the table's structure.
        
        *   **Restart Sequences**: Whether to reset auto increment columns to their initial values as part of the Truncate process.
            
        
    *   **Delete**: Delete the rows that match the "Select Rows" condition. If you don't select anything, Postgres deletes all rows.
        
        *   **Select Rows**: Define a **Column**, **Operator**, and **Value** to match rows on.
            
        *   **Combine Conditions**: How to combine the conditions in "Select Rows". **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
            
        
    *   **Drop**: Deletes the table's data and structure permanently.
        
    

#### Delete options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#delete-options)

*   **Cascade**: Whether to also drop all objects that depend on the table, like views and sequences. Available if using **Truncate** or **Drop** commands.
    
*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    

### Execute Query[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#execute-query)

Use this operation to execute an SQL query.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Execute Query**.
    
*   **Query**: The SQL query to execute. You can use n8n [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
     and tokens like `$1`, `$2`, and `$3` to build [prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html)
     to use with [query parameters](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#use-query-parameters)
    .
    

#### Execute Query options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#execute-query-options)

*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Query Parameters**: A comma-separated list of values that you want to use as [query parameters](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#use-query-parameters)
    .
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    
*   **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.
    

### Insert[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert)

Use this operation to insert rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Insert**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column.
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Insert options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert-options)

*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    
*   **Skip on Conflict**: Whether to skip the row if the insert violates a unique or exclusion constraint instead of throwing an error.
    
*   **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.
    

### Insert or Update[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert-or-update)

Use this operation to insert or update rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Insert or Update**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column.
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Insert or Update options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#insert-or-update-options)

*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    
*   **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.
    

### Select[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#select)

Use this operation to select rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Select**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
    
*   **Return All**: Whether to return all results or only up to a given limit.
    
*   **Limit**: The maximum number of items to return when **Return All** is disabled.
    
*   **Select Rows**: Set the conditions to select rows. Define a **Column**, **Operator**, and **Value** to match rows on. If you don't select anything, Postgres selects all rows.
    
*   **Combine Conditions**: How to combine the conditions in **Select Rows**. **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
    
*   **Sort**: Choose how to sort the selected rows. Choose a **Column** from a list or by ID and a sort **Direction**.
    

#### Select options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#select-options)

*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    

### Update[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#update)

Use this operation to update rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Postgres credential](https://docs.n8n.io/integrations/builtin/credentials/postgres)
    .
    
*   **Operation**: Select **Update**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column.
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Update options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#update-options)

*   **Connection Timeout**: The number of seconds to try to connect to the database.
    
*   **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
    
*   **Query Batching**: The way to send queries to the database:
    
    *   **Single Query**: A single query for all incoming items.
        
    *   **Independently**: Execute one query per incoming item of the execution.
        
    *   **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
        
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
    
    *   **Numbers**: Use this for standard numbers.
        
    *   **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
        
    
*   **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.postgres integration templates](https://n8n.io/integrations/postgres)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#related-resources)

------------------------------------------------------------------------------------------------------------------

n8n provides a trigger node for Postgres. Refer to the [Postgres Trigger node documentation](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger)
 for more information.

Use query parameters[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#use-query-parameters)

------------------------------------------------------------------------------------------------------------------------

When creating a query to run on a Postgres database, you can use the **Query Parameters** field in the **Options** section to load data into the query. n8n sanitizes data in query parameters, which prevents SQL injection.

For example, you want to find a person by their email address. Given the following input data:

Copy

    [\
        {\
            "email": "alex@example.com",\
            "name": "Alex",\
            "age": 21 \
        },\
        {\
            "email": "jamie@example.com",\
            "name": "Jamie",\
            "age": 33 \
        }\
    ]

You can write a query like:

Copy

    SELECT * FROM $1:name WHERE email = $2;

Then in **Query Parameters**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the email address from each input item in turn:

Copy

    // users is an example table name
    {{ [ 'users', $json.email ] }} 

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres#common-issues)

----------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues)
.

[PreviousPostBin](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues)

Last updated 10 days ago

Was this helpful?
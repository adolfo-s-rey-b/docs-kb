For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb.md)
.

Use the Oracle Database node to automate work in Oracle Database, and integrate Oracle Database with other applications. n8n has built-in support for a wide range of Oracle Database features which includes executing an SQL statement, fetching, inserting, updating or deleting data from Oracle Database. This node uses the [node-oracledb driver](https://github.com/oracle/node-oracledb)
 internally.

On this page, you'll find a list of operations the Oracle Database node supports and links to more resources.

Refer to [Oracle Database credentials](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
 for guidance on setting up authentication.

Requires Oracle Database **19c or later**. For advanced Oracle Database features like Transparent Application Continuity (TAC) and Sharding, also requires Oracle Client Libraries **19c or later**.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#operations)

----------------------------------------------------------------------------------------------------

*   [**Delete**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#delete)
    : Delete an entire table or rows in a table
    
*   [**Execute SQL**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#execute-sql)
    : Execute an SQL statement
    
*   [**Insert**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert)
    : Insert rows in a table
    
*   [**Insert or Update**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert-or-update)
    : Insert or update rows in a table
    
*   [**Select**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#select)
    : Select rows from a table
    
*   [**Update**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#update)
    : Update rows in a table
    

### Delete[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#delete)

Use this operation to delete an entire table or rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Select **Delete**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list, or select **By Name** to enter the table name.
    
*   **Command**: The deletion action to take:
    
    *   **Truncate**: Removes the table's data but preserves the table's structure.
        
    *   **Delete**: Delete the rows that match the "Select Rows" condition. If you don't select anything, Oracle Database deletes all rows.
        
        *   **Select Rows**: Define a **Column**, **Operator**, and **Value** to match rows on. The value can be passed as JSON using expression or string.
            
        *   **Combine Conditions**: How to combine the conditions in "Select Rows". The **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
            
        
    *   **Drop**: Deletes the table's data and structure permanently.
        
    

#### Delete options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#delete-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Statement Batching**: The way to send statements to the database:
    
    *   **Single Statement**: A single statement for all incoming items.
        
    *   **Independently**: Execute one statement per incoming item of the execution.
        
    *   **Transaction**: Execute all statements in a transaction. If a failure occurs, Oracle Database rolls back all changes.
        
    

### Execute SQL[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#execute-sql)

Use this operation to execute an SQL statement.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Execute SQL **Execute SQL**.
    
*   **Statement**: The SQL statement to execute. You can use n8n [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
     and positional parameters like `:1`, `:2`, or named parameters like `:name`, `:id` to use with [Use bind parameters](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-bind-parameters)
    . To run a PL/SQL procedure, for example `demo`, you can use:
    

Copy

    BEGIN
      demo;
    END;

#### Execute Statement options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#execute-statement-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Bind Variable Placeholder Values**: Enter the values for the bind parameters used in the statement [Use bind parameters](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-bind-parameters)
    .
    
*   **Output Numbers As String**: Indicates if the numbers should be retrieved as a String.
    
*   **Fetch Array Size**: This property is a number that sets the size of an internal buffer used for fetching query rows from Oracle Database. Changing it may affect query performance but does not affect how many rows are returned to the application.
    
*   **Number of Rows to Prefetch**: This property is a query tuning option to set the number of additional rows the underlying Oracle driver fetches during the internal initial statement execution phase of a query.
    

### Insert[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert)

Use this operation to insert rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Select **Insert**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list, or select **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column [Use n8n expressions for bind values](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-n8n-expressions-for-bind-values)
        .
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Oracle Database. The incoming data field names must match the column names in Oracle Database for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Insert options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Statement Batching**: The way to send statements to the database:
    
    *   **Single Statement**: A single statement for all incoming items.
        
    *   **Independently**: Execute one statement per incoming item of the execution.
        
    *   **Transaction**: Execute all statements in a transaction. If a failure occurs, Oracle Database rolls back all changes.
        
    

### Insert or Update[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert-or-update)

Use this operation to insert or update rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Select **Insert or Update**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list, or select **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column [Use n8n expressions for bind values](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-n8n-expressions-for-bind-values)
        .
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Oracle Database. The incoming data field names must match the column names in Oracle Database for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Insert or Update options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#insert-or-update-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Statement Batching**: The way to send statements to the database:
    
    *   **Single Statement**: A single statement for all incoming items.
        
    *   **Independently**: Execute one statement per incoming item of the execution.
        
    *   **Transaction**: Execute all statements in a transaction. If a failure occurs, Oracle Database rolls back all changes.
        
    

### Select[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#select)

Use this operation to select rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Select **Select**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list, or select **By Name** to enter the table name.
    
*   **Return All**: Whether to return all results or only up to a given limit.
    
*   **Limit**: The maximum number of items to return when **Return All** is disabled.
    
*   **Select Rows**: Set the conditions to select rows. Define a **Column**, **Operator**, and **Value**(as `json`) to match rows on. The **Value** can vary by type — for example with Fixed mode:
    
    *   String: "hello", hellowithoutquotes, "hello with space"
        
    *   Number: 12
        
    *   JSON: { "key": "val" }
        
    

If you don't select anything, Oracle Database selects all rows.

*   **Combine Conditions**: How to combine the conditions in **Select Rows**. The **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
    
*   **Sort**: Choose how to sort the selected rows. Choose a **Column** from a list or by ID and a sort **Direction**.
    

#### Select options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#select-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Output Numbers As String**: Indicates if the numbers should be retrieved as a String.
    
*   **Fetch Array Size**: This property is a number that sets the size of an internal buffer used for fetching query rows from Oracle Database. Changing it may affect query performance but does not affect how many rows are returned to the application.
    
*   **Number of Rows to Prefetch**: This property is a query tuning option to set the number of additional rows the underlying Oracle driver fetches during the internal initial statement execution phase of a query.
    

### Update[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#update)

Use this operation to update rows in a table.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [Oracle Database credential](https://docs.n8n.io/integrations/builtin/credentials/oracledb)
    .
    
*   **Operation**: Select **Update**.
    
*   **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
    
*   **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list, or select **By Name** to enter the table name.
    
*   **Mapping Column Mode**: How to map column names to incoming data:
    
    *   **Map Each Column Manually**: Select the values to use for each column [Use n8n expressions for bind values](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-n8n-expressions-for-bind-values)
        .
        
    *   **Map Automatically**: Automatically map incoming data to matching column names in Oracle Database. The incoming data field names must match the column names in Oracle Database for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
         before this node to adjust the format as needed.
        
    

#### Update options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#update-options)

*   **Auto Commit**: When this property is set to true, the transaction in the current connection is automatically committed at the end of statement execution.
    
*   **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Statement Batching**: The way to send statements to the database:
    
    *   **Single Statement**: A single statement for all incoming items.
        
    *   **Independently**: Execute one statement per incoming item of the execution.
        
    *   **Transaction**: Execute all statements in a transaction. If a failure occurs, Oracle Database rolls back all changes.
        
    

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#related-resources)

------------------------------------------------------------------------------------------------------------------

Refer to [SQL Language Reference](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=SQLRF)
 for more information about the service.

Refer to [node-oracledb documentation](https://node-oracledb.readthedocs.io/en/latest/)
 for more information about the node-oracledb driver.

Use bind parameters[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-bind-parameters)

----------------------------------------------------------------------------------------------------------------------

When creating a statement to run on an Oracle database instance, you can use the **Bind Variable Placeholder Values** field in the **Options** section to load data into the statement. n8n sanitizes data in statement parameters, which prevents SQL injection.

For example, you would want to find specific fruits by their color. Given the following input data:

Copy

    [\
        {\
            "FRUIT_ID": 1,\
            "FRUIT_NAME": "Apple",\
            "COLOR": "Red" \
        },\
        {\
            "FRUIT_ID": 2,\
            "FRUIT_NAME": "Banana",\
            "COLOR": "Yellow"\
        }\
    ]

You can write a statement like:

Copy

    SELECT * FROM FRUITS WHERE COLOR = :col

Then in **Bind Variable Placeholder Values**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the color from each input item in turn:

Copy

    // fruits is an example table name
    fruits, {{ $json.color }} 

Use n8n Expressions for bind values[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#use-n8n-expressions-for-bind-values)

------------------------------------------------------------------------------------------------------------------------------------------------------

For **Values to Send**, you can provide inputs using n8n Expressions. Below are examples for different data types — you can either enter constant values or reference fields from previous items (`$json`):

### JSON[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#json)

*   Constant: `{{ { k1: "v1", k2: "v2" } }}`
    
*   From a previous item: `{{ $json.COL_JSON }}`
    

### VECTOR[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#vector)

*   Constant: `{{ [1, 2, 3, 4.5] }}`
    
*   From a previous item: `{{ $json.COL_VECTOR }}`
    

### BLOB[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#blob)

*   Constant: `{{ [94, 87, 34] }}` or `{{ ' BLOB data string' }}`
    
*   From a previous item: `{{ $json.COL_BLOB }}`
    

### RAW[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#raw)

*   Constant: `{{ [94, 87, 34] }}`
    
*   From a previous item: `{{ $json.COL_RAW }}`
    

### BOOLEAN[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#boolean)

*   Constant: `{{ true }}`
    
*   From a previous item: `{{ $json.COL_BOOLEAN }}`
    

### NUMBER[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#number)

*   Constant: `1234`
    
*   From a previous item: `{{ $json.COL_NUMBER }}`
    

VARCHAR[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb#varchar)

----------------------------------------------------------------------------------------------

*   Constant: `' Hello World '`
    
*   From a previous item: `{{ $json.COL_CHAR }}`
    

These examples assume JSON keys (e.g. `COL_JSON, COL_VECTOR`) map directly to the respective SQL column types.

[PreviousOpenWeatherMap](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.openweathermap)
[NextOura](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oura)

Last updated 10 days ago

Was this helpful?
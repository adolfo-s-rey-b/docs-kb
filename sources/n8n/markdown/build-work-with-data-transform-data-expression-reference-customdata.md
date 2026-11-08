For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata.md)
.

`$execution.customData`.`**get()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdataget)

------------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the custom execution data stored under the given key. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)

**Syntax:** `$execution.customData`.get(key)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `key` (String) - The key (identifier) under which the data is stored
    

**Examples:**

Copy

    // Get the user's email (which was previously stored)
    $execution.customData.get("user_email") //=> "me@example.com"

`$execution.customData`.`**getAll()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdatagetall)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns all the key-value pairs of custom data that have been set in the current execution. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)

**Syntax:** `$execution.customData`.getAll()

**Returns:** Object

**Source:** Custom n8n functionality

**Examples:**

Copy

    $execution.customData.getAll() //=> {"user_email": "me@example.com", "id": 1234}

`$execution.customData`.`**set()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdataset)

------------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Stores custom execution data under the key specified. Use this to easily filter executions by this data. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)

**Syntax:** `$execution.customData`.set(key, value)

**Source:** Custom n8n functionality

**Parameters:**

*   `key` (String) - The key (identifier) under which the data is stored
    
*   `value` (String) - The data to store
    

**Examples:**

Copy

    // Store the user's email, to easily retrieve all execs related to that user later
    $execution.customData.set("user_email", "me@example.com")

`$execution.customData`.`**setAll()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#dollarexecutioncustomdatasetall)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Sets multiple key-value pairs of custom data for the execution. Use this to easily filter executions by this data. [More info](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)

**Syntax:** `$execution.customData`.setAll(obj)

**Source:** Custom n8n functionality

**Parameters:**

*   `obj` (Object) - A JavaScript object containing key-value pairs of the data to set
    

**Examples:**

Copy

    $execution.customData.setAll({"user_email": "me@example.com", "id": 1234})

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata#related-resources)

-------------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousBoolean](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean)
[NextDate](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date)

Last updated 10 days ago

Was this helpful?
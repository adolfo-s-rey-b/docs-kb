For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root.md)
.

`**$()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollar)

------------------------------------------------------------------------------------------------------

**Description:** Returns the data of the specified node

**Syntax:** $(nodeName)

**Returns:** NodeData

**Source:** Custom n8n functionality

**Parameters:**

*   `nodeName` (String) - The name of the node to retrieve data for
    

`**$binary**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarbinary)

----------------------------------------------------------------------------------------------------------------

**Description:** Returns any binary input data to the current node, for the current item. Shorthand for `$input.item.binary`.

**Syntax:** `**$binary**`

**Returns:** Array

**Source:** Custom n8n functionality

`**$execution**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarexecution)

----------------------------------------------------------------------------------------------------------------------

**Description:** Retrieve or set metadata for the current execution

**Syntax:** `**$execution**`

**Returns:** ExecData

**Source:** Custom n8n functionality

`**$fromAI()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarfromai)

------------------------------------------------------------------------------------------------------------------

**Description:** Use when a large language model should provide the value of a node parameter. Consider providing a description for better results.

**Syntax:** $fromAI(key, description?, type?, defaultValue?)

**Returns:** any

**Source:** Custom n8n functionality

**Parameters:**

*   `key` (String) - The name of the field to fetch. May only contain letters, numbers, underscores and hyphens.
    
*   `description` (String) - optional - Use to give the model more context on exactly what it should return
    
*   `type` (String) - optional - The type of the value to return. One of `string`, `number`, `boolean`, `json`, `date`, `datetime`. Defaults to `string`.
    
*   `defaultValue` (any) - optional - A value to use if the model doesn’t return the key
    

**Examples:**

Copy

    // Ask the model to provide a name, and use it here
    $fromAI('name')

Copy

    // Ask the model to provide the age of the person (as a number with a default value of 18), and use it here
    $fromAI('age', 'The age of the person', 'number', 18)

Copy

    // Ask the model to provide a boolean signifying whether the person is a student (with default value false), and use it here
    $fromAI('isStudent', 'Is the person a student', 'boolean', false)

`**$if()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarif)

----------------------------------------------------------------------------------------------------------

**Description:** Returns one of two values depending on the `condition`. Similar to the `?` operator in JavaScript.

**Syntax:** $if(condition, valueIfTrue, valueIfFalse)

**Returns:** any

**Source:** Custom n8n functionality

**Parameters:**

*   `condition` (Boolean) - The check to make. Should evaluate to either `true` or `false`
    
*   `valueIfTrue` (any) - The value to return if the condition is true
    
*   `valueIfFalse` (any) - The value to return if the condition is false
    

**Examples:**

Copy

    // Return "Good day" if time is before 5pm, otherwise "Good evening"
    $if($now.hour < 17, "Good day", "Good evening")

Copy

    // $if() calls can be combined:
    // Return "Good morning" if time is before 10am, "Good day" it's before 5pm, otherwise "Good evening"
    $if($now.hour < 10, "Good morning", $if($now.hour < 17, "Good day", "Good evening"))

`**$ifEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarifempty)

--------------------------------------------------------------------------------------------------------------------

**Description:** Returns the first parameter if it isn’t empty, otherwise returns the second parameter. The following count as empty: `””`, `[]`, `{}`, `null`, `undefined`

**Syntax:** $ifEmpty(value, valueIfEmpty)

**Returns:** any

**Source:** Custom n8n functionality

**Parameters:**

*   `value` (any) - The value to return, provided it isn’t empty
    
*   `valueIfEmpty` (any) - What to return if `value` is empty
    

**Examples:**

Copy

    "Hi " + $ifEmpty(name, "there") // e.g. "Hi Nathan" or "Hi there"

`**$input**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarinput)

--------------------------------------------------------------------------------------------------------------

**Description:** The input data of the current node

**Syntax:** `**$input**`

**Returns:** NodeData

**Source:** Custom n8n functionality

`**$itemIndex**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollaritemindex)

----------------------------------------------------------------------------------------------------------------------

**Description:** The position of the item currently being processed in the list of input items

**Syntax:** `**$itemIndex**`

**Returns:** Number

**Source:** Custom n8n functionality

`**$jmespath()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarjmespath)

----------------------------------------------------------------------------------------------------------------------

**Description:** Extracts data from an object (or array of objects) using a <a href=”/code/cookbook/jmespath/”>JMESPath expression. Useful for querying complex, nested objects. Returns `undefined` if the expression is invalid.

**Syntax:** $jmespath(obj, expression)

**Returns:** any

**Source:** Custom n8n functionality

**Parameters:**

*   `obj` (Object|Array) - The Object or array of Objects to retrieve data from
    
*   `expression` (String) - A <a href=”https://jmespath.org/examples.html”>JMESPath expression defining the data to retrieve from the object
    

**Examples:**

Copy

    data = {
      "people": [\
        {\
          "age": 20,\
          "other": "foo",\
          "name": "Bob"\
        },\
        {\
          "age": 25,\
          "other": "bar",\
          "name": "Fred"\
        },\
        {\
          "age": 30,\
          "other": "baz",\
          "name": "George"\
        }\
      ]
    }
    
    // Get all names, in an array
    {{ $jmespath(data, '[*].name') }} //=> ["Bob", "Fred", "George"]
    
    // Get the names and ages of everyone under 20
    $jmespath(data, '[?age > `20`].[name, age]') //=> [ ["Fred",25], ["George",30] ]
    
    // Get the name of the first person under 20
    $jmespath($json.people, '[?age > `20`].name | [0]') //=> Fred

Copy

    data = {
        "reservations": [\
          {\
            "id": 1,\
            "guests": [\
              {\
                "name": "Nathan",\
                "requirements": {\
                  "room": "double",\
                  "meal": "vegetarian"\
                }\
              },\
              {\
                "name": "Meg",\
                "requirements": {\
                  "room": "single"\
                }\
              }\
            ]\
          },\
          {\
            "id": 2,\
            "guests": [\
              {\
                "name": "Lex",\
                "requirements": {\
                  "room": "double"\
                }\
              }\
            ]\
          }\
        ]
      }
    
    // Get the names of all the guests in each reservation that require a double room
    $jmespath(data, 'reservations[].guests[?requirements.room==`double`].name')

`**$json**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarjson)

------------------------------------------------------------------------------------------------------------

**Description:** Returns the JSON input data to the current node, for the current item. Shorthand for `$input.item.json`. [More info](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)

**Syntax:** `**$json**`

**Returns:** Object

**Source:** Custom n8n functionality

`**$max()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarmax)

------------------------------------------------------------------------------------------------------------

**Description:** Returns the highest of the given numbers

**Syntax:** $max(num1, num2, …, numN)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `num1` (Number) - The first number to compare
    
*   `num2` (Number) - The second number to compare
    

`**$min()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarmin)

------------------------------------------------------------------------------------------------------------

**Description:** Returns the lowest of the given numbers

**Syntax:** $min(num1, num2, …, numN)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `num1` (Number) - The first number to compare
    
*   `num2` (Number) - The second number to compare
    

`**$nodeVersion**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarnodeversion)

--------------------------------------------------------------------------------------------------------------------------

**Description:** The version of the current node (as displayed at the bottom of the nodes’s settings pane)

**Syntax:** `**$nodeVersion**`

**Returns:** String

**Source:** Custom n8n functionality

`**$now**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarnow)

----------------------------------------------------------------------------------------------------------

**Description:** A DateTime representing the current moment.

Uses the workflow’s time zone (which can be changed in the workflow settings).

**Syntax:** `**$now**`

**Returns:** DateTime

**Source:** Custom n8n functionality

`**$pageCount**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarpagecount)

----------------------------------------------------------------------------------------------------------------------

**Description:** The number of results pages the node has fetched. Only available in the ‘HTTP Request’ node.

**Syntax:** `**$pageCount**`

**Returns:** Number

**Source:** Custom n8n functionality

`**$parameter**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarparameter)

----------------------------------------------------------------------------------------------------------------------

**Description:** The configuration settings of the current node. These are the parameters you fill out within the node’s UI (e.g. its operation).

**Syntax:** `**$parameter**`

**Returns:** NodeParams

**Source:** Custom n8n functionality

`**$prevNode**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarprevnode)

--------------------------------------------------------------------------------------------------------------------

**Description:** Information about the node that the current input came from.

When in a ‘Merge’ node, always uses the first input connector.

**Syntax:** `**$prevNode**`

**Returns:** PrevNodeData

**Source:** Custom n8n functionality

`**$request**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarrequest)

------------------------------------------------------------------------------------------------------------------

**Description:** The request object sent during the last run of the node. Only available in the ‘HTTP Request’ node.

**Syntax:** `**$request**`

**Returns:** Object

**Source:** Custom n8n functionality

`**$response**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarresponse)

--------------------------------------------------------------------------------------------------------------------

**Description:** The response returned by the last HTTP call. Only available in the ‘HTTP Request’ node.

**Syntax:** `**$response**`

**Returns:** HTTPResponse

**Source:** Custom n8n functionality

`**$runIndex**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarrunindex)

--------------------------------------------------------------------------------------------------------------------

**Description:** The index of the current run of the current node execution. Starts at 0.

**Syntax:** `**$runIndex**`

**Returns:** Number

**Source:** Custom n8n functionality

`**$secrets**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarsecrets)

------------------------------------------------------------------------------------------------------------------

**Description:** The secrets from an [external secrets vault](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets)
, if configured. Secret values are never displayed to the user. Only available in credential fields.

**Syntax:** `**$secrets**`

**Returns:** Object

**Source:** Custom n8n functionality

`**$today**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollartoday)

--------------------------------------------------------------------------------------------------------------

**Description:** A DateTime representing midnight at the start of the current day.

Uses the instance’s time zone (unless overridden in the workflow’s settings).

**Syntax:** `**$today**`

**Returns:** DateTime

**Source:** Custom n8n functionality

`**$vars**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarvars)

------------------------------------------------------------------------------------------------------------

**Description:** The [variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
 available to the workflow

**Syntax:** `**$vars**`

**Returns:** Object

**Source:** Custom n8n functionality

`**$workflow**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#dollarworkflow)

--------------------------------------------------------------------------------------------------------------------

**Description:** Information about the current workflow

**Syntax:** `**$workflow**`

**Returns:** WorkflowData

**Source:** Custom n8n functionality

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root#related-resources)

-------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousPrevnodedata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata)
[NextString](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string)

Last updated 10 days ago

Was this helpful?
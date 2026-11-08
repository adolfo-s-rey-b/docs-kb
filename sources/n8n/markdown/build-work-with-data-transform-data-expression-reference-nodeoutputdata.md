For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata.md)
.

`$()`.`**all()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarall)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array of the node’s output items

**Syntax:** `$()`.all(branchIndex?, runIndex?)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$()`.`**first()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarfirst)

-------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the first item output by the node

**Syntax:** `$()`.first(branchIndex?, runIndex?)

**Returns:** Item

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$()`.`**isExecuted**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarisexecuted)

---------------------------------------------------------------------------------------------------------------------------------------

**Description:** Is `true` if the node has executed, `false` otherwise

**Syntax:** `$()`.`$()`.`**isExecuted**`

**Returns:** Boolean

**Source:** Custom n8n functionality

`$()`.`**item**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollaritem)

---------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the matching item, i.e. the one used to produce the current item in the current node. [More info](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)

**Syntax:** `$()`.`$()`.`**item**`

**Returns:** Item

**Source:** Custom n8n functionality

`$()`.`**itemMatching()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollaritemmatching)

---------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the matching item, i.e. the one used to produce the item in the current node at the specified index. [More info](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)

**Syntax:** `$()`.itemMatching(currentItemIndex?)

**Returns:** Item

**Source:** Custom n8n functionality

**Parameters:**

*   `currentItemIndex` (Number) - The index of the item in the current node to be matched with.
    

`$()`.`**last()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarlast)

-----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the last item output by the node

**Syntax:** `$()`.last(branchIndex?, runIndex?)

**Returns:** Item

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$()`.`**params**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#dollarparams)

-------------------------------------------------------------------------------------------------------------------------------

**Description:** The configuration settings of the given node. These are the parameters you fill out within the node’s UI (e.g. its operation).

**Syntax:** `$()`.`$()`.`**params**`

**Returns:** NodeParams

**Source:** Custom n8n functionality

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousNodeinputdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata)
[NextNumber](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number)

Last updated 10 days ago

Was this helpful?
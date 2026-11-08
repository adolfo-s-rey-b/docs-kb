For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata.md)
.

`$input`.`**all()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputall)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array of the current node’s input items

**Syntax:** `$input`.all(branchIndex?, runIndex?)

**Returns:** Array

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch index of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$input`.`**first()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputfirst)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the current node’s first input item

**Syntax:** `$input`.first(branchIndex?, runIndex?)

**Returns:** Item

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch index of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$input`.`**item**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputitem)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the input item currently being processed

**Syntax:** `$input`.`$input`.`**item**`

**Returns:** Item

**Source:** Custom n8n functionality

`$input`.`**last()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputlast)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the current node’s last input item

**Syntax:** `$input`.last(branchIndex?, runIndex?)

**Returns:** Item

**Source:** Custom n8n functionality

**Parameters:**

*   `branchIndex` (Number) - optional - The output branch index of the node to use. Defaults to the first branch (index 0)
    
*   `runIndex` (Number) - optional - The run of the node to use. Defaults to the first run (index 0)
    

`$input`.`**params**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#dollarinputparams)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** The configuration settings of the current node. These are the parameters you fill out within the node when configuring it (e.g. its operation).

**Syntax:** `$input`.`$input`.`**params**`

**Returns:** NodeParams

**Source:** Custom n8n functionality

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata#related-resources)

----------------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousItem](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/item)
[NextNodeoutputdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata)

Last updated 10 days ago

Was this helpful?
For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata.md)
.

`**name**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#name)

-------------------------------------------------------------------------------------------------------------

**Description:** The name of the node that the current input came from.

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

**Syntax:** `**name**`

**Returns:** String

**Source:** Custom n8n functionality

`**outputIndex**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#outputindex)

---------------------------------------------------------------------------------------------------------------------------

**Description:** The index of the output connector that the current input came from. Use this when the previous node had multiple outputs (such as an ‘If’ or ‘Switch’ node).

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

**Syntax:** `**outputIndex**`

**Returns:** Number

**Source:** Custom n8n functionality

`**runIndex**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#runindex)

---------------------------------------------------------------------------------------------------------------------

**Description:** The run of the previous node that generated the current input.

Always uses the current node’s first input connector if there is more than one (e.g. in the ‘Merge’ node).

**Syntax:** `**runIndex**`

**Returns:** Number

**Source:** Custom n8n functionality

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata#related-resources)

---------------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousObject](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object)
[NextRoot](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root)

Last updated 10 days ago

Was this helpful?
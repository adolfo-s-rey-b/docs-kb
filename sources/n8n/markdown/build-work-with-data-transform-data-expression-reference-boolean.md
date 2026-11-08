For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean.md)
.

`_Boolean_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleanisempty)

-----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the boolean is `false`, `null`, or `undefined`. Returns `false` if the boolean is `true`.

`isEmpty()` isn't a null check. On a boolean it treats `false` as empty, so `{{ $json.flag.isEmpty() }}` returns `true` for both a missing field and a field set to `false`. To test only for a missing value, compare directly, for example `{{ $json.flag === null }}`, or use the **exists** operator in the **If** node.

**Syntax:** `_Boolean_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // bool = true
    bool.isEmpty() // => false

Copy

    // bool = false
    bool.isEmpty() // => true

Copy

    // bool = null
    bool.isEmpty() // => true

`_Boolean_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleanisnotempty)

-----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the boolean is `true`. Returns `false` if the boolean is `false`, `null`, or `undefined`. This is the inverse of `isEmpty()`.

**Syntax:** `_Boolean_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // bool = true
    bool.isNotEmpty() // => true

Copy

    // bool = false
    bool.isNotEmpty() // => false

Copy

    // bool = null
    bool.isNotEmpty() // => false

`_Boolean_`.`**toNumber()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleantonumber)

-------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts `true` to 1 and `false` to 0

**Syntax:** `_Boolean_`.toNumber()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    true.toNumber() //=> 1

Copy

    false.toNumber() //=> 0

`_Boolean_`.`**toString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#booleantostring)

-------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts `true` to the string ‘true’ and `false` to the string ‘false’

**Syntax:** `_Boolean_`.toString()

**Returns:** String

**Source:** JavaScript function

**Examples:**

Copy

    // bool = true
    bool.toString() //=> 'true'

Copy

    // bool = false
    bool.toString() //=> 'false'

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean#related-resources)

----------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousBinaryfile](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile)
[NextCustomdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata)

Last updated 10 days ago

Was this helpful?
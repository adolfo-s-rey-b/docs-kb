For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number.md)
.

`_Number_`.`**abs()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberabs)

------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the number’s absolute value, i.e. removes any minus sign

**Syntax:** `_Number_`.abs()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // x = -1.7
    x.abs() //=> 1.7

`_Number_`.`**ceil()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberceil)

--------------------------------------------------------------------------------------------------------------------------

**Description:** Rounds the number up to the next whole number

**Syntax:** `_Number_`.ceil()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // x = 1.234
    x.ceil() //=> 2

`_Number_`.`**floor()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberfloor)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Rounds the number down to the nearest whole number

**Syntax:** `_Number_`.floor()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    // x = 1.234
    x.floor() //=> 1

`_Number_`.`**format()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberformat)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a formatted string representing the number. Useful for formatting for a specific language or currency. The same as <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Intl/NumberFormat/NumberFormat”>`Intl.NumberFormat()`.

**Syntax:** `_Number_`.format(locale?, options?)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `locale` (String) - optional - A <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Intl#locales\_argument”>locale tag for formatting the number, e.g. `fr-FR`, `en-GB`, `pr-BR`
    
*   `options` (Object) - optional - Configuration options for number formatting. [More info](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat)
    

**Examples:**

Copy

    // number = 123456.789;
    number.format('de-DE') //=> 123.456,789

Copy

    // number = 123456.789;
    number.format('de-DE', {'style': 'currency', 'currency': 'EUR'}) //=> 123.456,79 €

`_Number_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisempty)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the number is `0`, `NaN`, `null`, or `undefined`. Returns `false` for every other number.

`isEmpty()` isn't a null check. On a number it treats `0` as empty, so `{{ $json.count.isEmpty() }}` returns `true` for both a missing field and a field set to `0`. To test only for a missing value, compare directly, for example `{{ $json.count === null }}`, or use the **exists** operator in the **If** node.

**Syntax:** `_Number_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // num = 10
    num.isEmpty() // => false

Copy

    // num = 0
    num.isEmpty() // => true

Copy

    // num = null
    num.isEmpty() // => true

`_Number_`.`**isEven()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberiseven)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the number is even. Throws an error if the number isn’t a whole number.

**Syntax:** `_Number_`.isEven()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // number = 33
    number.isEven() //=> false

`_Number_`.`**isInteger()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisinteger)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the number is a whole number

**Syntax:** `_Number_`.isInteger()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // number = 4
    number.isInteger() //=> true

Copy

    // number = 4.12
    number.isInteger() //=> false

`_Number_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisnotempty)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` for every number except `0` and `NaN`. Returns `false` if the number is `0`, `NaN`, `null`, or `undefined`. This is the inverse of `isEmpty()`.

**Syntax:** `_Number_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // num = 10
    num.isNotEmpty() // => true

Copy

    // num = 0
    num.isNotEmpty() // => false

Copy

    // num = null
    num.isNotEmpty() // => false

`_Number_`.`**isOdd()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberisodd)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the number is odd. Throws an error if the number isn’t a whole number.

**Syntax:** `_Number_`.isOdd()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // number = 33
    number.isOdd() //=> true

`_Number_`.`**round()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numberround)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the number rounded to the nearest whole number (or specified number of decimal places)

**Syntax:** `_Number_`.round(decimalPlaces?)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `decimalPlaces` (Number) - optional - The number of decimal places to round to
    

**Examples:**

Copy

    // number = 1.256
    number.round() //=> 1

Copy

    // number = 1.256
    number.round(1) //=> 1.3
    number.round(2) //=> 1.26

`_Number_`.`**toBoolean()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertoboolean)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the number to a boolean value. `0` becomes `false`; everything else becomes `true`.

**Syntax:** `_Number_`.toBoolean()

**Source:** Custom n8n functionality

**Examples:**

Copy

    // number = 12
    number.toBoolean() //=> true

Copy

    // number = 0
    number.toBoolean() //=> false

`_Number_`.`**toDateTime()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertodatetime)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a numerical timestamp into a DateTime. The format of the timestamp must be specified if it’s not in milliseconds. Uses the time zone in n8n (or in the workflow’s settings).

**Syntax:** `_Number_`.toDateTime(format?)

**Returns:** DateTime

**Source:** Custom n8n functionality

**Parameters:**

*   `format` (String) - optional - The type of timestamp to convert. Options are `ms` (for Unix timestamp in milliseconds), `s` (for Unix timestamp in seconds) or `excel` (for days since 1900).
    

**Examples:**

Copy

    // ts = 1708695471
    ts.toDateTime('s') //=> 2024-02-23T14:37:51+01:00

Copy

    // ts = 1708695471000
    ts.toDateTime('ms') //=> 2024-02-23T14:37:51+01:00

Copy

    // ts = 45345
    ts.toDateTime('excel') //=> 2024-02-23T01:00:00+01:00

`_Number_`.`**toLocaleString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertolocalestring)

----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a localised string representing the number, i.e. in the language and format corresponding to its locale. Defaults to the system's locale if none specified.

**Syntax:** `_Number_`.toLocaleString(locales?, options?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `locales` (String|Array) - optional - The locale to assign, e.g. ‘en-GB’ for British English or ‘pt-BR’ for Brazilian Portuguese. See <a href=”https://www.localeplanet.com/icu/”>full list (unofficial). Also accepts an array of locales. Defaults to the system locale if not specified.
    
*   `options` (Object) - optional - An object with <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Intl/NumberFormat/NumberFormat#parameters”>formatting options
    

**Examples:**

Copy

    // num = 500000.125
    num.toLocaleString() //=> '500,000.125' (if in US English locale)

Copy

    // num = 500000.125
    num.toLocaleString('fr-FR') //=> '500 000,125'

Copy

    // num = 500000.125
    num.toLocaleString('fr-FR', {style:'currency', currency:'EUR'}) //=> '500 000,13 €'

`_Number_`.`**toString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#numbertostring)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the number to a simple textual representation. For more formatting options, see `toLocaleString()`.

**Syntax:** `_Number_`.toString(radix?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `radix` (Number) - optional - The base to use. Must be an integer between 2 and 36. E.g. base `2` is binary and base `16` is hexadecimal.
    

**Examples:**

Copy

    // num = 500000.125
    num.toString() //=> '500000.125'

Copy

    // num = 500000.125
    num.toString(16) //=> '7a120.2'

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousNodeoutputdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata)
[NextObject](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object)

Last updated 10 days ago

Was this helpful?
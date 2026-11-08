For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime.md)
.

`_DateTime_`.`**day**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeday)

----------------------------------------------------------------------------------------------------------------------------

**Description:** The day of the month (1-31)

**Syntax:** `_DateTime_`.day

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.day //=> 30

`_DateTime_`.`**diffTo()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimediffto)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the difference between two DateTimes, in the given unit(s)

**Syntax:** `_DateTime_`.diffTo(otherDateTime, unit)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `otherDateTime` (String|DateTime) - The moment to subtract the base DateTime from. Can be an ISO date string or a Luxon DateTime.
    
*   `unit` (String|Array) - optional - The unit, or array of units, to return the result in. Possible values: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`.
    

**Examples:**

Copy

    // dt1 = "2024-03-30T18:49:07.234".toDateTime()
    dt1.diffTo('2025-01-01', 'days') //=> 276.21

Copy

    // dt1 = "2024-03-30T18:49:07.234".toDateTime()
    // dt2 = "2025-01-01T00:00:00.000".toDateTime()
    dt1.diffTo(dt2, ['months', 'days']) //=> {'months':, 'days':}

Copy

    Note: should support both day and days, etc.

`_DateTime_`.`**diffToNow()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimedifftonow)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the difference between the current moment and the DateTime, in the given unit(s). For a textual representation, use `toRelative()` instead.

**Syntax:** `_DateTime_`.diffToNow(unit)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `unit` (String|Array) - optional - The unit, or array of units, to return the result in. Possible values: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`.
    

**Examples:**

Copy

    // dt = "2023-03-30T18:49:07.234".toDateTime()
    dt.diffToNow('days') //=> 371.9

Copy

    // dt = "2023-03-30T18:49:07.234".toDateTime()
    dt.diffToNow(['months', 'days']) //=> {"months":12, "days":5.9}

Copy

    Note: should support both day and days, etc.

`_DateTime_`.`**endOf()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeendof)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Rounds the DateTime up to the end of one of its units, e.g. the end of the month

**Syntax:** `_DateTime_`.endOf(unit, opts)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `unit` (String) - The unit to round to the end of. Can be `year`, `quarter`, `month`, `week`, `day`, `hour`, `minute`, `second`, or `millisecond`.
    
*   `opts` (Object) - optional - Object with options that affect the output. Possible properties: `useLocaleWeeks` (boolean): Whether to use the locale when calculating the start of the week. Defaults to false.
    

**Examples:**

Copy

    // dt = "2024-03-20T18:49".toDateTime()
    dt.endOf('month') //=> 2024-03-31T23:59

`_DateTime_`.`**equals()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeequals)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the two DateTimes represent exactly the same moment and are in the same time zone. For a less strict comparison, use `hasSame()`.

**Syntax:** `_DateTime_`.equals(other)

**Returns:** Boolean

**Type:** Luxon

**Parameters:**

*   `other` (DateTime) - The other DateTime to compare
    

**Examples:**

Copy

    // dt1 = "2024-03-20T18:49+01:00".toDateTime()
    // dt2 = "2024-03-20T19:49+02:00".toDateTime()
    dt1.equals(dt2) //=> false

`_DateTime_`.`**extract()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeextract)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Extracts a part of the date or time, e.g. the month, as a number. To extract textual names instead, see `format()`.

**Syntax:** `_DateTime_`.extract(unit?)

**Returns:** Number

**Source:** Custom n8n functionality

**Parameters:**

*   `unit` (String) - optional - The part of the date or time to return. One of: `year`, `month`, `week`, `day`, `hour`, `minute`, `second`
    

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.extract('month') //=> 3

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.extract('hour') //=> 18

`_DateTime_`.`**format()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeformat)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the DateTime to a string, using the format specified. [Formatting guide](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)
. For common formats, `toLocaleString()` may be easier.

**Syntax:** `_DateTime_`.format(fmt)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `fmt` (String) - The [format](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)
     of the string to return
    

**Examples:**

Copy

    // dt = "2024-04-30T18:49".toDateTime()
    dt.format('dd/LL/yyyy') //=> '30/04/2024'

Copy

    // dt = "2024-04-30T18:49".toDateTime()
    dt.format('dd LLL yy') //=> '30 Apr 24'
    dt.setLocale('fr').format('dd LLL yyyy') //=> '30 avr. 2024'
    dt.format("HH 'hours and' mm 'minutes'") //=> '18 hours and 49 minutes'

**Not available in the Code node**

`format()` is a custom n8n extension added to Luxon `DateTime` objects in the expressions editor. It doesn't exist in the Code node, because Code node scripts run against plain, unmodified Luxon. Calling it there throws `... .format is not a function`.

Use Luxon's native [`toFormat()`](https://moment.github.io/luxon/api-docs/index.html#datetimetoformat)
 instead:

Copy

    // In the Code node
    DateTime.now().toFormat('dd/LL/yyyy'); //=> '30/04/2024'

This applies to any method on this page marked **Source: Custom n8n functionality**: it's available in expressions (e.g. the Set node) but may not be available in the Code node. See [Built-in methods and variables](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
 for more on this distinction.

`_DateTime_`.`**hasSame()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimehassame)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the two DateTimes are the same, down to the unit specified. Time zones are ignored (only local times are compared), so use `toUTC()` first if needed.

**Syntax:** `_DateTime_`.hasSame(otherDateTime, unit)

**Returns:** Boolean

**Type:** Luxon

**Parameters:**

*   `otherDateTime` (DateTime) - The other DateTime to compare
    
*   `unit` (String) - The unit of time to check sameness down to. One of `year`, `quarter`, `month`, `week`, `day`, `hour`, `minute`, `second`, or `millisecond`.
    

**Examples:**

Copy

    // dt1 = "2024-03-20".toDateTime()
    // dt2 = "2024-03-18".toDateTime()
    dt1.hasSame(dt2, 'month') //=> true

Copy

    // dt1 = "1982-03-20".toDateTime()
    // dt2 = "2024-03-18".toDateTime()
    dt1.hasSame(dt2, 'month') //=> false

`_DateTime_`.`**hour**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimehour)

------------------------------------------------------------------------------------------------------------------------------

**Description:** The hour of the day (0-23)

**Syntax:** `_DateTime_`.hour

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.hour //=> 18

`_DateTime_`.`**isBetween()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisbetween)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the DateTime lies between the two moments specified

**Syntax:** `_DateTime_`.isBetween(date1, date2)

**Returns:** Boolean

**Source:** Custom n8n functionality

**Parameters:**

*   `date1` (String|DateTime) - The moment that the base DateTime must be after. Can be an ISO date string or a Luxon DateTime.
    
*   `date2` (String|DateTime) - The moment that the base DateTime must be before. Can be an ISO date string or a Luxon DateTime.
    

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.isBetween('2020-06-01', '2025-06-01') //=> true

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.isBetween('2020', $now) //=> true

`_DateTime_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisempty)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `false` for all DateTimes. Returns `true` for `null` or `undefined`.

**Syntax:** `_DateTime_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // dt = '2023-03-30T18:49:07.234'.toDateTime()
    dt.isEmpty() // => false

Copy

    // dt = null
    dt.isEmpty() // => true

`_DateTime_`.`**isInDST**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisindst)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Whether the DateTime is in daylight saving time

**Syntax:** `_DateTime_`.isInDST

**Returns:** Boolean

**Type:** Luxon

`_DateTime_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeisnotempty)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` for all DateTimes. Returns `false` for `null` or `undefined`.

**Syntax:** `_DateTime_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // dt = '2023-03-30T18:49:07.234'.toDateTime()
    dt.isNotEmpty() // => true

Copy

    // dt = null
    dt.isNotEmpty() // => false

`_DateTime_`.`**locale**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimelocale)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** The locale of a DateTime, such 'en-GB'. The locale is used when formatting the DateTime.

**Syntax:** `_DateTime_`.locale

**Returns:** String

**Type:** Luxon

**Examples:**

Copy

    $now.locale //=> 'en-US'

`_DateTime_`.`**millisecond**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemillisecond)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The millisecond of the second (0-999)

**Syntax:** `_DateTime_`.millisecond

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49:07.234".toDateTime()
    dt.millisecond //=> 234

`_DateTime_`.`**minus()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeminus)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Subtracts a given period of time from the DateTime

**Syntax:** `_DateTime_`.minus(n, unit?)

**Returns:** DateTime

**Source:** Custom n8n functionality

**Parameters:**

*   `n` (Number|Object) - The number of units to subtract. Or use a Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration object to subtract multiple units at once.
    
*   `unit` (String) - optional - The units of the number. One of: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`
    

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.minus(7, 'days') //=> 2024-04-23T18:49

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.minus(4, 'years') //=> 2020-04-30T18:49

**Code node:** Luxon's native `DateTime.prototype.minus()` also exists in the Code node, but only accepts a single [Duration-like object](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)
 (e.g. `dt.minus({ days: 7 })`), not this page's n8n-only `(n, unit)` shorthand. Passing `dt.minus(7, 'days')` in the Code node will not raise an error but will not subtract 7 days either — double-check the result if you use this signature there.

`_DateTime_`.`**minute**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeminute)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** The minute of the hour (0-59)

**Syntax:** `_DateTime_`.minute

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.minute //=> 49

`_DateTime_`.`**month**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonth)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** The month (1-12)

**Syntax:** `_DateTime_`.month

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.month //=> 3

`_DateTime_`.`**monthLong**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonthlong)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** The textual long month name, e.g. 'October'. Defaults to the system's locale if no locale has been specified.

**Syntax:** `_DateTime_`.monthLong

**Returns:** String

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.monthLong //=> 'March'

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.setLocale('de-DE').monthLong //=> 'März'

`_DateTime_`.`**monthShort**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimemonthshort)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The textual abbreviated month name, e.g. 'Oct'. Defaults to the system's locale if no locale has been specified.

**Syntax:** `_DateTime_`.monthShort

**Returns:** String

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.monthShort //=> 'Mar'

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.setLocale('de-DE').monthShort //=> 'Mär'

`_DateTime_`.`**plus()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeplus)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Adds a given period of time to the DateTime

**Syntax:** `_DateTime_`.plus(n, unit?)

**Returns:** DateTime

**Source:** Custom n8n functionality

**Parameters:**

*   `n` (Number|Object) - The number of units to add. Or use a Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration object to add multiple units at once.
    
*   `unit` (String) - optional - The units of the number. One of: `years`, `months`, `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`
    

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.plus(7, 'days') //=> 2024-04-06T18:49

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.plus(4, 'years') //=> 2028-04-30T18:49

**Code node:** Luxon's native `DateTime.prototype.plus()` also exists in the Code node, but only accepts a single [Duration-like object](https://moment.github.io/luxon/api-docs/index.html#datetimeplus)
 (e.g., `dt.plus({ days: 7 })`), not this page's n8n-only `(n, unit)` shorthand. Passing `dt.plus(7, 'days')` in the Code node will not raise an error but will not add 7 days either. Double-check the result if you use this signature there.

`_DateTime_`.`**quarter**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimequarter)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** The quarter of the year (1-4)

**Syntax:** `_DateTime_`.quarter

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.quarter //=> 1

`_DateTime_`.`**second**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesecond)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** The second of the minute (0-59)

**Syntax:** `_DateTime_`.second

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49:07.234".toDateTime()
    dt.second //=> 7

`_DateTime_`.`**set()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeset)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Assigns new values to specified units of the DateTime. To round a DateTime, see also `startOf()` and `endOf()`.

**Syntax:** `_DateTime_`.set(values)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `values` (Object) - An object containing the units to set and corresponding values to assign. Possible keys are `year`, `month`, `day`, `hour`, `minute`, `second` and `millsecond`.
    

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.set({year:1982, month:10}) //=> 1982-10-20T18:49

`_DateTime_`.`**setLocale()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesetlocale)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Sets the locale, which determines the language and formatting for the DateTime. Useful when generating a textual representation of the DateTime, e.g. with `format()` or `toLocaleString()`.

**Syntax:** `_DateTime_`.setLocale(locale)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `locale` (String) - The locale to assign, e.g. ‘en-GB’ for British English or ‘pt-BR’ for Brazilian Portuguese. <a href=”https://www.localeplanet.com/icu/”>List (unofficial)
    

**Examples:**

Copy

    $now.setLocale('de-DE').toLocaleString({'dateStyle':'long'}) //=> 5. Oktober 2024

Copy

    $now.setLocale('fr-FR').toLocaleString({'dateStyle':'long'}) //=> 5 octobre 2024

`_DateTime_`.`**setZone()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimesetzone)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the DateTime to the given time zone. The DateTime still represents the same moment unless specified in the options. See also `toLocal()` and `toUTC()`.

**Syntax:** `_DateTime_`.setZone(zone, opts)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `zone` (String) - optional - A zone identifier, either in the format ‘America/New\_York’, 'UTC+3', or the strings 'local' or 'utc'
    
*   `opts` (Object) - optional - Options that affect the output. Possible properties: `keepCalendarTime` (boolean): Whether to keep the time the same and only change the offset. Defaults to false.
    

**Examples:**

Copy

    // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
    dt.setZone('America/Buenos_aires') //=> 2023-12-31T19:00:00.000-03:00

Copy

    // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
    dt.setZone('UTC+7') //=> 2024-01-01T05:00:00.000+07:00

`_DateTime_`.`**startOf()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimestartof)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Rounds the DateTime down to the beginning of one of its units, e.g. the start of the month

**Syntax:** `_DateTime_`.startOf(unit, opts)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `unit` (String) - The unit to round to the beginning of. One of `year`, `quarter`, `month`, `week`, `day`, `hour`, `minute`, `second`, or `millisecond`.
    
*   `opts` (Object) - optional - Object with options that affect the output. Possible properties: `useLocaleWeeks` (boolean): Whether to use the locale when calculating the start of the week. Defaults to false.
    

**Examples:**

Copy

    // dt = "2024-03-20T18:49".toDateTime()
    dt.startOf('month') //=> 2024-03-01T00:00

`_DateTime_`.`**toISO()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoiso)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an ISO 8601-compliant string representation of the DateTime

**Syntax:** `_DateTime_`.toISO(opts)

**Returns:** String

**Type:** Luxon

**Parameters:**

*   `opts` (Object) - optional - Configuration options. See <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimetoiso”>Luxon docs for more info.
    

**Examples:**

Copy

    $now.toISO() //=> 2024-04-05T18:44:55.525+02:00

`_DateTime_`.`**toLocal()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetolocal)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a DateTime to the workflow’s local time zone. The DateTime still represents the same moment unless specified in the parameters. The workflow’s time zone can be set in the workflow settings.

**Syntax:** `_DateTime_`.toLocal()

**Returns:** DateTime

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-01-01T00:00:00.000Z".toDateTime()
    dt.toLocal() //=> 2024-01-01T01:00:00.000+01:00, if time zone is Europe/Berlin

`_DateTime_`.`**toLocaleString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetolocalestring)

----------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a localised string representing the DateTime, i.e. in the language and format corresponding to its locale. Defaults to the system's locale if none specified.

**Syntax:** `_DateTime_`.toLocaleString(formatOpts)

**Returns:** String

**Type:** Luxon

**Parameters:**

*   `formatOpts` (Object) - optional - Configuration options for the rendering. See <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Intl/DateTimeFormat/DateTimeFormat#parameters”>Intl.DateTimeFormat for a full list. Defaults to rendering a short date.
    

**Examples:**

Copy

    $now.toLocaleString() //=> '4/30/2024'
    $now.toLocaleString({'dateStyle':'medium', 'timeStyle':'short'}) //=> 'Apr 30, 2024, 10:00 PM'
    // (if in US English locale)

Copy

    $now.setLocale('de-DE').toLocaleString() //=> '30.4.2024'

Copy

    $now.toLocaleString({'dateStyle':'short'}) //=> '4/30/2024'
    $now.toLocaleString({'dateStyle':'medium'}) //=> 'Apr 30, 2024'
    $now.toLocaleString({'dateStyle':'long'}) //=> 'April 30, 2024'
    $now.toLocaleString({'dateStyle':'full'}) //=> 'Tuesday, April 30, 2024'
    // (if in US English locale)

Copy

    $now.toLocaleString({'year':'numeric', 'month':'numeric', 'day':'numeric'}) //=> '4/30/2024'
    $now.toLocaleString({'year':'2-digit', 'month':'2-digit', 'day':'2-digit'}) //=> '04/30/24'
    $now.toLocaleString({'month':'short', 'weekday':'short', 'day':'numeric'}) //=> 'Tue, Apr 30'
    $now.toLocaleString({'month':'long', 'weekday':'long', 'day':'numeric'}) //=> 'Tuesday, April 30'
    // (if in US English locale)

Copy

    $now.toLocaleString({'timeStyle':'short'}) //=> '10:00 PM'
    $now.toLocaleString({'timeStyle':'medium'}) //=> '10:00:58 PM'
    $now.toLocaleString({'timeStyle':'long'}) //=> '10:00:58 PM GMT+2'
    $now.toLocaleString({'timeStyle':'full'}) //=> '10:00:58 PM Central European Summer Time'
    // (if in US English locale)

Copy

    $now.toLocaleString({'hour':'numeric', 'minute':'numeric', hourCycle:'h24'}) //=> '22:00'
    $now.toLocaleString({'hour':'2-digit', 'minute':'2-digit', hourCycle:'h12'}) //=> '10:00 PM'
    // (if in US English locale)

`_DateTime_`.`**toMillis()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetomillis)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a Unix timestamp in milliseconds (the number elapsed since 1st Jan 1970)

**Syntax:** `_DateTime_`.toMillis()

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    $now.toMillis() //=> 1712334324677

`_DateTime_`.`**toRelative()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetorelative)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a textual representation of the time relative to now, e.g. ‘in two days’. Rounds down by default.

**Syntax:** `_DateTime_`.toRelative(options)

**Returns:** String

**Type:** Luxon

**Parameters:**

*   `options` (Object) - optional - Options that affect the output. Possible properties: `unit` = the unit to default to (`years`, `months`, `days`, etc.). `locale` = the language and formatting to use (e.g. `de`, `fr`)
    

**Examples:**

Copy

    $now.plus(1, 'day').toRelative() //=> "in 1 day"

Copy

    $now.plus(1, 'day').toRelative({unit:'hours'}) //=> "in 24 hours"

Copy

    $now.plus(1, 'day').toRelative({locale:'es'}) //=> "dentro de 1 día"

`_DateTime_`.`**toSeconds()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoseconds)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a Unix timestamp in seconds (the number elapsed since 1st Jan 1970)

**Syntax:** `_DateTime_`.toSeconds()

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    $now.toSeconds() //=> 1712334442.372

`_DateTime_`.`**toString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetostring)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a string representation of the DateTime. Similar to `toISO()`. For more formatting options, see `format()` or `toLocaleString()`.

**Syntax:** `_DateTime_`.toString()

**Returns:** string

**Type:** Luxon

**Examples:**

Copy

    $now.toString() //=> 2024-04-05T18:44:55.525+02:00

`_DateTime_`.`**toUTC()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimetoutc)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a DateTime to the UTC time zone. The DateTime still represents the same moment unless specified in the parameters. Use `setZone()` to convert to other zones.

**Syntax:** `_DateTime_`.toUTC(offset, opts)

**Returns:** DateTime

**Type:** Luxon

**Parameters:**

*   `offset` (Number) - optional - An offset from UTC in minutes
    
*   `opts` (Object) - optional - Object with options that affect the output. Possible properties: `keepCalendarTime` (boolean): Whether to keep the time the same and only change the offset. Defaults to false.
    

**Examples:**

Copy

    // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
    dt.toUTC() //=> 2023-12-31T22:00:00.000Z

`_DateTime_`.`**weekday**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekday)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** The day of the week. 1 is Monday and 7 is Sunday.

**Syntax:** `_DateTime_`.weekday

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.weekday //=> 6

`_DateTime_`.`**weekdayLong**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekdaylong)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The textual long weekday name, e.g. 'Wednesday'. Defaults to the system's locale if no locale has been specified.

**Syntax:** `_DateTime_`.weekdayLong

**Returns:** String

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.weekdayLong //=> 'Saturday'

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.setLocale('de-DE').weekdayLong //=> 'Samstag'

`_DateTime_`.`**weekdayShort**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweekdayshort)

----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The textual abbreviated weekday name, e.g. 'Wed'. Defaults to the system's locale if no locale has been specified.

**Syntax:** `_DateTime_`.weekdayShort

**Returns:** String

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.weekdayShort //=> 'Sat'

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.setLocale('fr-FR').weekdayShort //=> 'sam.'

`_DateTime_`.`**weekNumber**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeweeknumber)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** The week number of the year (1-52ish)

**Syntax:** `_DateTime_`.weekNumber

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.weekNumber //=> 13

`_DateTime_`.`**year**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeyear)

------------------------------------------------------------------------------------------------------------------------------

**Description:** The year

**Syntax:** `_DateTime_`.year

**Returns:** Number

**Type:** Luxon

**Examples:**

Copy

    // dt = "2024-03-30T18:49".toDateTime()
    dt.year //=> 2024

`_DateTime_`.`**zone**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimezone)

------------------------------------------------------------------------------------------------------------------------------

**Description:** The time zone associated with the DateTime

**Syntax:** `_DateTime_`.zone

**Returns:** Object

**Type:** Luxon

**Examples:**

Copy

    $now.zone //=> {"zoneName": "Europe/Berlin", "valid": true}

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#related-resources)

-----------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousDate](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date)
[NextExecdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata)

Last updated 10 days ago

Was this helpful?
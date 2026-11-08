*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#mdn-search)
    

Date.parse()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Date.parse()`** static method parses a string representation of a date, and returns the date's [timestamp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#parameters)

[`dateString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#datestring)

A string in [the date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
. See the linked reference for caveats on using different formats.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#return_value)

A number representing the [timestamp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
 of the given date. If `dateString` fails to be parsed as a valid date, [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 is returned.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#description)

-----------------------------------------------------------------------------------------------------------------------

This function is useful for setting date values based on string values, for example in conjunction with the [`setTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime)
 method.

The formats that `parse()` can handle are not explicitly specified, but there are a few [invariants](https://developer.mozilla.org/en-US/docs/Glossary/Invariant)
:

*   The [date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
     (produced by [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
    ) must be supported.
*   If `x` is any Date whose milliseconds amount is zero, then `x.valueOf()` should be equal to any of the following: `Date.parse(x.toString())`, `Date.parse(x.toUTCString())`, `Date.parse(x.toISOString())`. This means the formats produced by [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
     and [`toUTCString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)
     should be supported too.
*   The spec does _not_ require support for the format produced by [`toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)
    . However, major engines all try to support `toLocaleString("en-US")` format.

Other formats are implementation-defined and may not work across all browsers. A library can help if many different formats are to be accommodated. In fact, the unreliability of `Date.parse()` is one of the motivations for the [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
 API to be introduced.

Because `parse()` is a static method of `Date`, you always use it as `Date.parse()`, rather than as a method of a `Date` object you created.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using Date.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#using_date.parse)

The following calls all return `1546300800000`. The first will imply UTC time because it's date-only, and the others explicitly specify the UTC timezone.

The following call, which does not specify a time zone will be set to 2019-01-01 at 00:00:00 in the local timezone of the system, because it has both date and time.

### [toString() and toUTCString() formats](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#tostring_and_toutcstring_formats)

Apart from the standard date time string format, the [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
 and [`toUTCString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)
 formats are supported:

### [Non-standard date strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#non-standard_date_strings)

**Note:** This section contains implementation-specific behavior that may be inconsistent across browsers or different versions of browsers. It is not meant to be a comprehensive browser compatibility table and you should always conduct your own tests before using any format in your code.

Implementations usually default to the local time zone when the date string is non-standard. For consistency, we will assume that the runtime uses the UTC timezone, and unless specified otherwise, the output will vary with the device's time zone. [Daylight Saving Time (DST), of the local time zone, can also have an effect on this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#varied_results_in_daylight_saving_time_dst_regions)
.

Here are some more examples of non-standard date strings. Browsers are very lenient when parsing date strings and may discard any part of a string that they cannot parse. For compatibility reasons, browsers often copy each other's behavior, so these handling patterns tend to propagate cross-browser. As previously stated, the following examples are for illustration only, and are not exhaustive by any means:

| Description | Example | Chrome | Firefox | Safari |
| --- | --- | --- | --- | --- |
| Single number | `0` (single-digit) | 946684800000 (Jan 01 2000); NaN in Firefox ≤122 |     | \-62167219200000 (Jan 01 0000) |
| `31` (two-digit) | NaN |     | \-61188912000000 (Jan 01 0031) |
| `999` (three-/four-digit) | \-30641733102000 (Jan 01 0999) |     |     |
| Date strings that use different separators | `1970-01-01` (standard) | 0 in all time zones |     |     |
| `1970/01/01` | 0   |     |     |
| `1970,01,01` | 0   |     | NaN |
| `1970 01 01` | 0   |     | NaN |
| Strings that look like `toString()` | `Thu Jan 01 1970 00:00:00`  <br>`Thu Jan 01 1970`  <br>`Jan 01 1970 00:00:00`  <br>`Jan 01 1970` | 0   |     |     |
| Strings that look like `toUTCString()` | `Thu, 01 Jan 1970 00:00:00`  <br>`Thu, 01 Jan 1970`  <br>`01 Jan 1970 00:00:00`  <br>`01 Jan 1970` | 0   |     |     |
| First date component is 2-digit | `01-02-03` (first segment can be valid month) | 1041465600000 (Jan 02 2003) |     | \-62132745600000 (Feb 03 0001)  <br>Note: Safari always assumes YY-MM-DD, but MM/DD/YY. |
| `27-02-03` (first segment can be valid day but not month) | NaN |     | \-61312291200000 (Feb 03 0027) |
| `49-02-03` (first segment cannot be valid day and is <50) | 2495923200000 (Feb 03 2049) |     | \-60617980800000 (Feb 03 0049) |
| `50-02-03` (first segment cannot be valid day and is ≥50) | \-628300800000 (Feb 03 1950) |     | \-60586444800000 (Feb 03 0050) |
| Out-of-bounds date components | `2014-25-23`  <br>`Mar 32, 2014`  <br>`2014/25/23` | NaN |     |     |
| `2014-02-30` | 1393718400000 (Mar 02 2014) |     | NaN |
| `02/30/2014` | 1393718400000 |     |     |
| Extraneous characters after the month name | `04 Dec 1995`  <br>`04 Decem 1995`  <br>`04 December 1995` | 818031600000 |     |     |
| `04 DecFoo 1995` | 818031600000  <br>Only the first three characters are read.  <br>Firefox ≤121 reads up to the valid month name, thus returning NaN when it sees "F". |     |     |
| `04 De 1995` | NaN |     |     |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date.parse](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date.parse) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/parse/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date/parse (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2Fparse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fparse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2Fparse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fparse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
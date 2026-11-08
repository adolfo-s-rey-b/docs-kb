*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#mdn-search)
    

Date() constructor
==================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Date()`** constructor creates [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 objects. When called as a function, it returns a string representing the current time.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#syntax)

------------------------------------------------------------------------------------------------------------

**Note:** `Date()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, but with different effects. See [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#return_value)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#parameters)

There are five basic forms for the `Date()` constructor:

#### No parameters

When no parameters are provided, the newly-created `Date` object represents the current date and time as of the time of instantiation. The returned date's [timestamp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
 is the same as the number returned by [`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
.

#### Time value or timestamp number

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#value)

An integer value representing the [timestamp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
 (the number of milliseconds since midnight at the beginning of January 1, 1970, UTC — a.k.a. the [epoch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
).

#### Date string

[`dateString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#datestring)

A string value representing a date, parsed and interpreted using the same algorithm implemented by [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
. See [date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
 for caveats on using different formats.

#### Date object

[`dateObject`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#dateobject)

An existing `Date` object. This effectively makes a copy of the existing `Date` object with the same date and time. This is equivalent to `new Date(dateObject.valueOf())`, except the `valueOf()` method is not called.

When one parameter is passed to the `Date()` constructor, `Date` instances are specially treated. All other values are [converted to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
. If the result is a string, it will be parsed as a date string. Otherwise, the resulting primitive is further coerced to a number and treated as a timestamp.

#### Individual date and time component values

Given at least a year and month, this form of `Date()` returns a `Date` object whose component values (year, month, day, hour, minute, second, and millisecond) all come from the following parameters. Any missing fields are given the lowest possible value (`1` for `day` and `0` for every other component). The parameter values are all evaluated against the local time zone, rather than UTC. [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC)
 accepts similar parameters but interprets the components as UTC and returns a timestamp.

If any parameter overflows its defined bounds, it "carries over". For example, if a `monthIndex` greater than `11` is passed in, those months will cause the year to increment; if a `minutes` greater than `59` is passed in, `hours` will increment accordingly, etc. Therefore, `new Date(1990, 12, 1)` will return January 1st, 1991; `new Date(2020, 5, 19, 25, 65)` will return 2:05 A.M. June 20th, 2020.

Similarly, if any parameter underflows, it "borrows" from the higher positions. For example, `new Date(2020, 5, 0)` will return May 31st, 2020.

[`year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#year)

Integer value representing the year. Values from `0` to `99` map to the years `1900` to `1999`. All other values are the actual year. See the [example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#interpretation_of_two-digit_years)
.

[`monthIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#monthindex)

Integer value representing the month, beginning with `0` for January to `11` for December.

[`day` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#day)

Integer value representing the day of the month. Defaults to `1`.

[`hours` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#hours)

Integer value between `0` and `23` representing the hour of the day. Defaults to `0`.

[`minutes` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#minutes)

Integer value representing the minute segment of a time. Defaults to `0`.

[`seconds` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#seconds)

Integer value representing the second segment of a time. Defaults to `0`.

[`milliseconds` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#milliseconds)

Integer value representing the millisecond segment of a time. Defaults to `0`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#return_value)

Calling `new Date()` (the `Date()` constructor) returns a [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 object. If called with an invalid date string, or if the date to be constructed will have a timestamp less than `-8,640,000,000,000,000` or greater than `8,640,000,000,000,000` milliseconds, it returns an [invalid date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
 (a `Date` object whose [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
 method returns `"Invalid Date"` and [`valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/valueOf)
 method returns `NaN`).

Calling the `Date()` function (without the `new` keyword) returns a string representation of the current date and time, exactly as `new Date().toString()` does. Any arguments given in a `Date()` function call (without the `new` keyword) are ignored; regardless of whether it's called with an invalid date string — or even called with any arbitrary object or other primitive as an argument — it always returns a string representation of the current date and time.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#description)

----------------------------------------------------------------------------------------------------------------------

### [Reduced time precision](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#reduced_time_precision)

To offer protection against timing attacks and [fingerprinting](https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting)
, the precision of `new Date()` may be reduced depending on browser settings.

When a timestamp, date string, date object, or date component values are supplied to the constructor, the browser does not apply timer rounding to the supplied time.

When called without arguments, the constructor obtains the current time in the same way as [`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
. It inherits the precision of that clock reading without introducing additional inaccuracy.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#examples)

----------------------------------------------------------------------------------------------------------------

### [Several ways to create a Date object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#several_ways_to_create_a_date_object)

The following examples show several ways to create JavaScript dates:

### [Passing a non-Date, non-string, non-number value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#passing_a_non-date_non-string_non-number_value)

If the `Date()` constructor is called with one parameter which is not a `Date` instance, it will be coerced to a primitive and then checked whether it's a string. For example, `new Date(undefined)` is different from `new Date()`:

This is because `undefined` is already a primitive but not a string, so it will be coerced to a number, which is [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 and therefore not a valid timestamp. On the other hand, `null` will be coerced to `0`.

[Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
 would be coerced to a string via [`Array.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)
, which joins the elements with commas. However, the resulting string for any array with more than one element is not a valid ISO 8601 date string, so its parsing behavior would be implementation-defined. **Do not pass arrays to the `Date()` constructor.**

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date-constructor](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/date/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date/date (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FDate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fdate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FDate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fdate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F91b5a448a517239876a4bc92640bbbf29e30b106%0A*+Document+last+modified%3A+2026-09-01T00%3A52%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
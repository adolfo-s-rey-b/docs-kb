*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#mdn-search)
    

Temporal.ZonedDateTime.prototype.since()
========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`since()`** method of [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
 instances returns a new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration from another date-time (in a form convertible by [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
) to this date-time. The duration is positive if the other date-time is before this date-time, and negative if after.

This method does `this - other`. To do `other - this`, use the [`until()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/until)
 method.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#syntax)

-------------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#parameters)

[`other`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#other)

A string, an object, or a [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
 instance representing a date-time to subtract from this date-time. It is converted to a `Temporal.ZonedDateTime` object using the same algorithm as [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
. It must have the same calendar as `this`.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#options)

An object containing the options for [`Temporal.Duration.prototype.round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round)
, which includes `largestUnit`, `roundingIncrement`, `roundingMode`, and `smallestUnit`. `largestUnit` and `smallestUnit` accept all possible units. For `largestUnit`, the default value `"auto"` means `"hours"` or `smallestUnit`, whichever is greater. For `smallestUnit`, the default value is `"nanoseconds"`. The current date is used as the `relativeTo` option. Note that using [units larger than `"hours"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#calendar_durations)
 may make the duration not portable to other calendars, dates, or time zones.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#return_value)

A new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration _since_ `other` to this date-time. The duration is positive if `other` is before this date-time, and negative if after.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown in one of the following cases:

*   `other` has a different calendar than `this`.
*   Any of the options is invalid.
*   `other` has a different time zone than `this`, and `largestUnit` is `"days"` or above.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#description)

-----------------------------------------------------------------------------------------------------------------------------------------

The duration returned is a "hybrid" duration. This means that the duration's date portion represents full calendar days like [`Temporal.PlainDateTime.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/since)
 would return, while its time portion represents real-world elapsed time like [`Temporal.Instant.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant/since)
 would return. This "hybrid duration" approach automatically adjusts for DST and matches widely-adopted industry standards like [RFC 5545 (iCalendar)](https://datatracker.ietf.org/doc/html/rfc5545 "External link (opens in new tab)")
. See below for examples.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#examples)

-----------------------------------------------------------------------------------------------------------------------------------

### [Offset transitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#offset_transitions)

When transitions happen, a day may not have exactly 24 hours.

For this reason, the returned duration is purely time-based with no date portion by default, so that it stays unambiguous.

### [Different time zones](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#different_time_zones)

The time portion of the returned duration is purely based on instants and is not affected by time zones. However, if you want to include any date units like `day`, then the start and end must be in the same time zone.

For more examples about how to use `since()`, especially with rounding, see [`Temporal.PlainDate.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/since)
 and [`Temporal.PlainTime.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime/since)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal.zoneddatetime.prototype.since](https://tc39.es/proposal-temporal/#sec-temporal.zoneddatetime.prototype.since) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since#see_also)

-----------------------------------------------------------------------------------------------------------------------------------

*   [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
    
*   [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
    
*   [`Temporal.ZonedDateTime.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/add)
    
*   [`Temporal.ZonedDateTime.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/subtract)
    
*   [`Temporal.ZonedDateTime.prototype.until()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/until)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/zoneddatetime/since/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/zoneddatetime/since (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FZonedDateTime%2Fsince&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fzoneddatetime%2Fsince%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FZonedDateTime%2Fsince%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fzoneddatetime%2Fsince%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
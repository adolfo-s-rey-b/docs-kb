*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#mdn-search)
    

Temporal.Duration.prototype.round()
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`round()`** method of [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 instances returns a new `Temporal.Duration` object with the duration rounded to the given smallest unit and/or [balanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_balancing)
 to the given largest unit.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#syntax)

--------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#parameters)

[`smallestUnit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#smallestunit)

A string representing the [`smallestUnit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#smallestunit_2)
 option. This is a convenience overload, so `round(smallestUnit)` is equivalent to `round({ smallestUnit })`, where `smallestUnit` is a string.

[`options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#options)

An object containing some or all of the following properties (in the order they are retrieved and validated):

[`largestUnit` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#largestunit)

Any of the temporal units: `"years"`, `"months"`, `"weeks"`, `"days"`, `"hours"`, `"minutes"`, `"seconds"`, `"milliseconds"`, `"microseconds"`, `"nanoseconds"`, or their singular forms, or the value `"auto"` which means the largest non-zero component of this duration or `smallestUnit`, whichever is greater. Defaults to `"auto"`. The result will not contain units larger than this; for example, if the largest unit is `"minutes"`, then "1 hour 30 minutes" will become "90 minutes".

[`relativeTo` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#relativeto)

A zoned or plain date(time) that provides the time and calendar information to resolve [calendar durations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#calendar_durations)
 (see the link for the general interpretation of this option). Required if either `this` or `other` is a calendar duration, or `smallestUnit` is a calendar unit.

[`roundingIncrement` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#roundingincrement)

A number (truncated to an integer) representing the rounding increment in the given `smallestUnit`. Defaults to `1`. Must be in the inclusive range of 1 to 1e9. If the smallest unit is hours, minutes, seconds, milliseconds, microseconds, or nanoseconds, the increment must be a divisor of the maximum value of the unit; for example, if the unit is hours, the increment must be a divisor of 24 and must not be 24 itself, which means it can be 1, 2, 3, 4, 6, 8, or 12.

[`roundingMode` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#roundingmode)

A string representing the rounding mode specifying to round up or down in various scenarios. See [`Intl.NumberFormat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#roundingmode)
. Defaults to `"halfExpand"`.

[`smallestUnit` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#smallestunit_2)

Any of the temporal units: `"years"`, `"months"`, `"weeks"`, `"days"`, `"hours"`, `"minutes"`, `"seconds"`, `"milliseconds"`, `"microseconds"`, `"nanoseconds"`, or their singular forms. Defaults to `"nanoseconds"`. For units larger than `"nanoseconds"`, fractional parts of the `smallestUnit` will be rounded according to the `roundingIncrement` and `roundingMode` settings. Must be smaller or equal to `largestUnit`. At least one of `smallestUnit` and `largestUnit` must be provided.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#return_value)

A new `Temporal.Duration` object, where the largest unit is no larger than the `largestUnit` option, and the smallest unit is no smaller than the `smallestUnit` option. The fractional parts of the `smallestUnit` are rounded according to the `roundingIncrement` and `roundingMode` settings.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if any of the options is invalid.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#description)

------------------------------------------------------------------------------------------------------------------------------------

The `round()` method performs two operations: rounding and balancing. It does the following:

1.  It makes sure the duration is balanced. If a component is above its preferred maximum (24 hours per day, 60 minutes per hour, etc.), the excess is carried over to the next larger unit, until we reach `largestUnit`. For example, "24 hours 90 minutes" becomes "25 hours 30 minutes" if `largestUnit` is `"auto"`, and "1 day 1 hour 30 minutes" if `largestUnit` is `"days"`.
2.  For all components larger than `largestUnit`, they are carried down into `largestUnit`; for example, "2 hours 30 minutes" becomes "150 minutes" if `largestUnit` is `"minutes"`.
3.  For all components smaller than `smallestUnit`, they are carried up into `smallestUnit` as a fractional part, and then rounded according to the `roundingIncrement` and `roundingMode` settings. For example, "1 hour 30 minutes" becomes "1.5 hours" if `smallestUnit` is `"hours"`, and then rounded to "2 hours" using the default settings.

[Calendar units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#calendar_durations)
 have uneven lengths. Their lengths are resolved relative to a starting point. For example, a duration of "2 years" in the Gregorian calendar may be 730 days or 731 days long, depending on whether it moves through a leap year or not. When rounding to a calendar unit, we first get the exact date-time represented by `relativeTo + duration`, then round it down and up according to `smallestUnit` and `roundingIncrement` to get two candidates. Then, we choose the candidate according to the `roundingMode` setting, and finally subtract `relativeTo` to get the final duration.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Rounding off small units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#rounding_off_small_units)

### [Avoiding larger units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#avoiding_larger_units)

### [Rounding to a whole number of hours](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#rounding_to_a_whole_number_of_hours)

### [Rounding by 15-minute increments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#rounding_by_15-minute_increments)

### [Resolving calendar durations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#resolving_calendar_durations)

If either the initial duration or largest/smallest unit contains a calendar unit, you must provide a `relativeTo` option to resolve the calendar durations.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal.duration.prototype.round](https://tc39.es/proposal-temporal/#sec-temporal.duration.prototype.round) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
    
*   [`Temporal.Duration.prototype.total()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/total)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/duration/round/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/duration/round (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FDuration%2Fround&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fduration%2Fround%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FDuration%2Fround%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fduration%2Fround%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
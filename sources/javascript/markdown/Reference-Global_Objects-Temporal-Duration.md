*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#mdn-search)
    

Temporal.Duration
=================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Temporal.Duration`** object represents a difference between two time points, which can be used in date/time arithmetic. It is fundamentally represented as a combination of years, months, weeks, days, hours, minutes, seconds, milliseconds, microseconds, and nanoseconds values.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#description)

------------------------------------------------------------------------------------------------------------------------------

### [ISO 8601 duration format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#iso_8601_duration_format)

`Duration` objects can be serialized and parsed using the [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations "External link (opens in new tab)")
 (with some extensions specified by ECMAScript). The string has the following form (spaces are only for readability and should not be present in the actual string):

±P nY nM nW nD T nH nM nS

[`±` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#%C2%B1)

An optional sign character (`+` or `-`), which represents positive or negative duration. Default is positive.

[`P`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#p)

A literal character `P` or `p` that stands for "period".

[`nY`, `nM`, `nW`, `nD`, `nH`, `nM`, `nS`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#ny)

A number followed by a literal character, which represents the number of years (`Y`), months (`M`), weeks (`W`), days (`D`), hours (`H`), minutes (`M`), or seconds (`S`), respectively. All except the last existing component must be an integer. The last component, if it is a time component (hours, minutes, or seconds), may have a fractional part of 1 to 9 digits, led by a dot or a comma, such as `PT0.0021S` or `PT1.1H`. Any zero components may be omitted, but at least one component should be present (even if it has value zero, in which case the duration is zero).

[`T`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#t)

A literal character `T` or `t` that separates the date part from the time part, which should be present if and only if there's at least one component after it.

Here are some examples:

| ISO 8601 | Meaning |
| --- | --- |
| `P1Y1M1DT1H1M1.1S` | 1 year, 1 month, 1 day, 1 hour, 1 minute, 1 second, and 100 milliseconds |
| `P40D` | 40 days |
| `P1Y1D` | 1 year and 1 day |
| `P3DT4H59M` | 3 days, 4 hours and 59 minutes |
| `PT2H30M` | 2 hours and 30 minutes |
| `P1M` | 1 month |
| `PT1M` | 1 minute |
| `PT0.0021S` | 2.1 milliseconds (2 milliseconds and 100 microseconds) |
| `PT0S` | Zero (canonical representation) |
| `P0D` | Zero |

**Note:** According to the ISO 8601-1 standard, weeks are not allowed to appear together with any other units, and durations can only be positive. As extensions to the standard, ISO 8601-2, which Temporal uses, allows a sign character at the start of the string, and allows combining weeks with other units. Therefore, if your duration is serialized to a string like `P3W1D`, `+P1M`, or `-P1M`, note that other programs may not accept it.

When serializing, the output respects the stored components as much as possible, preserving [unbalanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_balancing)
 components. However, subsecond components are serialized as a single fractional second, so their precise values, if unbalanced may be lost. The plus sign is omitted for positive durations. The zero duration is always serialized as `PT0S`.

### [Calendar durations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#calendar_durations)

A _calendar duration_ is one that contains any of the [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
 units: weeks, months, and years. A non-calendar duration is portable and can participate in date/time arithmetic without any calendar information, because they unambiguously represent a fixed amount of time. However, a calendar duration is not portable because the number of days in a month or year depends on the calendar system and the reference time point. Therefore, attempting to perform any arithmetic operation on a calendar durations throws an error because durations don't keep track of a calendar themselves. For example, if we are in May of the Gregorian calendar, then "1 month" is "31 days", but if we are in April, then "1 month" becomes "30 days". To add or subtract calendar durations, you need to add them to dates instead:

js

    const dur1 = Temporal.Duration.from({ years: 1 });
    const dur2 = Temporal.Duration.from({ months: 1 });
    
    dur1.add(dur2); // RangeError: for calendar duration arithmetic, use date arithmetic relative to a starting point
    
    const startingPoint = Temporal.PlainDate.from("2021-01-01"); // ISO 8601 calendar
    startingPoint.add(dur1).add(dur2).since(startingPoint); // "P396D"
    

Other operations, `round()`, `total()`, and `compare()`, take a `relativeTo` option to provide the necessary calendar and reference time information. This option can be a [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
, [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
, [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
, or otherwise an object or string that's convertible using [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
 (if the `timeZone` option is provided or the string contains time zone annotation) or [`Temporal.PlainDate.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/from)
.

Note that `days` to `hours` conversion is also technically ambiguous because the length of a day may vary due to offset changes, such as daylight saving time. You can provide a zoned `relativeTo` to account for these changes; otherwise 24-hour days are assumed.

### [Duration balancing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_balancing)

There are many ways to represent the same duration: for example, "1 minute and 30 seconds" and "90 seconds" are equivalent. However, depending on the context, one representation may be more appropriate than the other. Therefore, generally, the `Duration` object preserves the input values as much as possible, so that when you format it, it will be displayed as you expect.

Each component of a duration has its optimal range; hours should be from 0 to 23, minutes from 0 to 59, and so on. When a component overflows its optimal range, the excess may be "carried" into the next larger component. To carry over, we need to answer the question of "how many X are in a Y?", which is a complicated question for [calendar units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#calendar_durations)
, so in this case a calendar is needed. Also note that by default, `days` are directly carried into `months`; the weeks unit is only carried into if explicitly requested. If we carry as much as possible, the eventual result where all components are within their optimal range is called a "balanced" duration. Unbalanced durations usually come in the "top-heavy" form, where the largest unit is unbalanced (e.g., "27 hours and 30 minutes"); other forms, such as "23 hours and 270 minutes", are rarely seen.

The [`round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round)
 method always balances the duration into the "top-heavy" form, up to the `largestUnit` option. With a manual `largestUnit` option that's large enough, you can fully balance the duration. Similarly, the [`add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/add)
 and [`subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/subtract)
 methods balance the result duration to the largest unit of the input durations.

Note that because the ISO 8601 duration format represents subsecond components as one single fraction number, it is not possible to preserve unbalanced subsecond components during serialization using the default format. For example, "1000 milliseconds" is serialized as `"PT1S"`, and then deserialized as "1 second". If you need to preserve the subsecond components' magnitudes, you need to manually serialize it as a JSON object instead (because by default the [`toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/toJSON)
 method serializes the duration in the ISO 8601 format).

### [Duration sign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_sign)

Because a duration is a difference between two time points, it can be positive, negative, or zero. For example, if you are displaying event times in relative time, then negative durations may represent events in the past, and positive durations for the future. In our representation using a combination of time components, the sign is stored within each component: a negative duration always has all components negative (or zero), and a positive duration always has all components positive (or zero). Constructing a duration with components of mixed signs is invalid and will be rejected by the constructor or the [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/with)
 method. The `add()` and `subtract()` methods will balance the result duration to avoid mixed signs.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#constructor)

------------------------------------------------------------------------------------------------------------------------------

[`Temporal.Duration()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/Duration)

Creates a new `Temporal.Duration` object by directly supplying the underlying data.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#static_methods)

------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.Duration.compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/compare)

Returns a number (-1, 0, or 1) indicating whether the first duration is shorter, equal to, or longer than the second duration.

[`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)

Creates a new `Temporal.Duration` object from another `Temporal.Duration` object, an object with duration properties, or an ISO 8601 string.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#instance_properties)

----------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Temporal.Duration.prototype` and shared by all `Temporal.Duration` instances.

[`Temporal.Duration.prototype.blank`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/blank)

Returns a boolean that is `true` if this duration represents a zero duration, and `false` otherwise. Equivalent to `duration.sign === 0`.

[`Temporal.Duration.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Temporal.Duration` instances, the initial value is the [`Temporal.Duration()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/Duration)
 constructor.

[`Temporal.Duration.prototype.days`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/days)

Returns an integer representing the number of days in the duration.

[`Temporal.Duration.prototype.hours`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/hours)

Returns an integer representing the number of hours in the duration.

[`Temporal.Duration.prototype.microseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/microseconds)

Returns an integer representing the number of microseconds in the duration.

[`Temporal.Duration.prototype.milliseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/milliseconds)

Returns an integer representing the number of milliseconds in the duration.

[`Temporal.Duration.prototype.minutes`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/minutes)

Returns an integer representing the number of minutes in the duration.

[`Temporal.Duration.prototype.months`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/months)

Returns an integer representing the number of months in the duration.

[`Temporal.Duration.prototype.nanoseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/nanoseconds)

Returns an integer representing the number of nanoseconds in the duration.

[`Temporal.Duration.prototype.seconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/seconds)

Returns an integer representing the number of seconds in the duration.

[`Temporal.Duration.prototype.sign`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/sign)

Returns `1` if this duration is positive, `-1` if negative, and `0` if zero.

[`Temporal.Duration.prototype.weeks`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/weeks)

Returns an integer representing the number of weeks in the duration.

[`Temporal.Duration.prototype.years`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/years)

Returns an integer representing the number of years in the duration.

[`Temporal.Duration.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#temporal.duration.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Temporal.Duration"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#instance_methods)

----------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.Duration.prototype.abs()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/abs)

Returns a new `Temporal.Duration` object with the absolute value of this duration (all fields keep the same magnitude, but sign becomes positive).

[`Temporal.Duration.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/add)

Returns a new `Temporal.Duration` object with the sum of this duration and a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
). The result is [balanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_balancing)
.

[`Temporal.Duration.prototype.negated()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/negated)

Returns a new `Temporal.Duration` object with the negated value of this duration (all fields keep the same magnitude, but sign becomes reversed).

[`Temporal.Duration.prototype.round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/round)

Returns a new `Temporal.Duration` object with the duration rounded to the given smallest unit and/or [balanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#duration_balancing)
 to the given largest unit.

[`Temporal.Duration.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/subtract)

Returns a new `Temporal.Duration` object with the difference between this duration and a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
). Equivalent to [adding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/add)
 the [negated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/negated)
 value of the other duration.

[`Temporal.Duration.prototype.toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/toJSON)

Returns a string representing this duration in the same [ISO 8601 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#iso_8601_duration_format)
 as calling [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/toString)
. Intended to be implicitly called by [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
.

[`Temporal.Duration.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/toLocaleString)

Returns a string with a language-sensitive representation of this duration. In implementations with [`Intl.DurationFormat` API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat)
 support, this method delegates to `Intl.DurationFormat`.

[`Temporal.Duration.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/toString)

Returns a string representing this duration in the [ISO 8601 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#iso_8601_duration_format)
.

[`Temporal.Duration.prototype.total()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/total)

Returns a number representing the total duration in the given unit.

[`Temporal.Duration.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/valueOf)

Throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, which prevents `Temporal.Duration` instances from being [implicitly converted to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
 when used in arithmetic or comparison operations.

[`Temporal.Duration.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/with)

Returns a new `Temporal.Duration` object representing this duration with some fields replaced by new values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal-duration-objects](https://tc39.es/proposal-temporal/#sec-temporal-duration-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/duration/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/duration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FDuration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fduration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FDuration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fduration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
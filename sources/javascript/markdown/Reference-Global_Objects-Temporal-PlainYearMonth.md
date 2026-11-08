*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#mdn-search)
    

Temporal.PlainYearMonth
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Temporal.PlainYearMonth`** object represents the year and month of a calendar date, without a day or time zone; for example, an event on a calendar that happens during the whole month. It is fundamentally represented as an ISO 8601 calendar date, with year, month, and day fields, and an associated calendar system. The day is used to disambiguate the year-month in non-ISO calendar systems.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#description)

------------------------------------------------------------------------------------------------------------------------------------

A `PlainYearMonth` is essentially the year-month part of a [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
 object, without the day.

### [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#rfc_9557_format)

`PlainYearMonth` objects can be serialized and parsed using the [RFC 9557](https://datatracker.ietf.org/doc/html/rfc9557 "External link (opens in new tab)")
 format, an extension to the [ISO 8601 / RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339 "External link (opens in new tab)")
 format. The string has the following form (spaces are only for readability and should not be present in the actual string):

YYYY-MM-DD \[u-ca=calendar\_id\]

[`YYYY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#yyyy)

Either a four-digit number, or a six-digit number with a `+` or `-` sign.

[`MM`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#mm)

A two-digit number from `01` to `12`.

[`DD` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#dd)

A two-digit number from `01` to `31`. It is required for non-ISO calendars, and optional otherwise. If omitted, the string looks like `YYYY-MM` or `YYYYMM`. Note that the reference day actually stored may be different from the one you provide, but the represented year-month is the same. See [`Temporal.PlainYearMonth.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/from)
 for more information. The `YYYY`, `MM`, and `DD` components can be separated by `-` or nothing.

[`[u-ca=calendar_id]` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#u-cacalendar_id)

Replace `calendar_id` with the calendar to use. See [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
 for a list of commonly supported calendar types. Defaults to `[u-ca=iso8601]`. May have a _critical flag_ by prefixing the key with `!`: e.g., `[!u-ca=iso8601]`. This flag generally tells other systems that it cannot be ignored if they don't support it. The `Temporal` parser will throw an error if the annotations contain two or more calendar annotations and one of them is critical. Note that the `YYYY-MM-DD` is always interpreted as an ISO 8601 calendar date and then converted to the specified calendar.

As an input, you may optionally include the time, offset, and time zone identifier, in the same format as [`PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime#rfc_9557_format)
, but they will be ignored. Other annotations in the `[key=value]` format are also ignored, and they must not have the critical flag.

When serializing, you can configure whether to display the calendar ID, and whether to add a critical flag for it.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#constructor)

------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.PlainYearMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/PlainYearMonth)

Creates a new `Temporal.PlainYearMonth` object by directly supplying the underlying data.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#static_methods)

------------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.PlainYearMonth.compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/compare)

Returns a number (-1, 0, or 1) indicating whether the first year-month comes before, is the same as, or comes after the second year-month. Equivalent to comparing their underlying ISO 8601 dates. Two year-months from different calendars may be considered equal if they start on the same ISO date.

[`Temporal.PlainYearMonth.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/from)

Creates a new `Temporal.PlainYearMonth` object from another `Temporal.PlainYearMonth` object, an object with year and month properties, or an [RFC 9557](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#rfc_9557_format)
 string.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#instance_properties)

----------------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Temporal.PlainYearMonth.prototype` and shared by all `Temporal.PlainYearMonth` instances.

[`Temporal.PlainYearMonth.prototype.calendarId`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/calendarId)

Returns a string representing the [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
 used to interpret the internal ISO 8601 date.

[`Temporal.PlainYearMonth.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Temporal.PlainYearMonth` instances, the initial value is the [`Temporal.PlainYearMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/PlainYearMonth)
 constructor.

[`Temporal.PlainYearMonth.prototype.daysInMonth`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/daysInMonth)

Returns a positive integer representing the number of days in the month of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.PlainYearMonth.prototype.daysInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/daysInYear)

Returns a positive integer representing the number of days in the year of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For the ISO 8601 calendar, this is 365, or 366 in a leap year.

[`Temporal.PlainYearMonth.prototype.era`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/era)

Returns a calendar-specific lowercase string representing the era of this year-month, or `undefined` if the calendar does not use eras (e.g., ISO 8601). `era` and `eraYear` together uniquely identify a year in a calendar, in the same way that `year` does. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For Gregorian, it is either `"ce"` or `"bce"`.

[`Temporal.PlainYearMonth.prototype.eraYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/eraYear)

Returns a non-negative integer representing the year of this year-month within the era, or `undefined` if the calendar does not use eras (e.g., ISO 8601). The year index usually starts from 1 (more common) or 0, and years in an era can decrease with time (e.g., Gregorian BCE). `era` and `eraYear` together uniquely identify a year in a calendar, in the same way that `year` does. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.PlainYearMonth.prototype.inLeapYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/inLeapYear)

Returns a boolean indicating whether this year-month is in a leap year. A leap year is a year that has more days (due to a leap day or leap month) than a common year. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.PlainYearMonth.prototype.month`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/month)

Returns a positive integer representing the 1-based month index in the year of this year-month. The first month of this year is `1`, and the last month is the [`monthsInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/monthsInYear)
. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Note that unlike [`Date.prototype.getMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)
, the index is 1-based. If the calendar has leap months, then the month with the same [`monthCode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/monthCode)
 may have different `month` indexes for different years.

[`Temporal.PlainYearMonth.prototype.monthCode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/monthCode)

Returns a calendar-specific string representing the month of this year-month. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Usually it is `M` plus a two-digit month number. For leap months, it is the previous month's code followed by `L`. If the leap month is the first month of the year, the code is `M00L`.

[`Temporal.PlainYearMonth.prototype.monthsInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/monthsInYear)

Returns a positive integer representing the number of months in the year of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For the ISO 8601 calendar, this is always 12, but in other calendar systems it may differ.

[`Temporal.PlainYearMonth.prototype.year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/year)

Returns an integer representing the number of years of this year-month relative to the start of a calendar-specific epoch year. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Usually year 1 is either the first year of the latest era or the ISO 8601 year `0001`. If the epoch is in the middle of the year, that year will have the same value before and after the start date of the era.

[`Temporal.PlainYearMonth.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#temporal.plainyearmonth.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Temporal.PlainYearMonth"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#instance_methods)

----------------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.PlainYearMonth.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/add)

Returns a new `Temporal.PlainYearMonth` object representing this year-month moved forward by a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
).

[`Temporal.PlainYearMonth.prototype.equals()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/equals)

Returns `true` if this year-month is equivalent in value to another year-month (in a form convertible by [`Temporal.PlainYearMonth.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/from)
), and `false` otherwise. They are compared both by their underlying ISO date values and their calendars, so two year-months from different calendars may be considered equal by [`Temporal.PlainYearMonth.compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/compare)
 but not by `equals()`.

[`Temporal.PlainYearMonth.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/since)

Returns a new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration from another year-month (in a form convertible by [`Temporal.PlainYearMonth.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/from)
) to this year-month. The duration is positive if the other month is before this month, and negative if after.

[`Temporal.PlainYearMonth.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/subtract)

Returns a new `Temporal.PlainYearMonth` object representing this year-month moved backward by a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
).

[`Temporal.PlainYearMonth.prototype.toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/toJSON)

Returns a string representing this year-month in the same [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#rfc_9557_format)
 as calling [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/toString)
. Intended to be implicitly called by [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
.

[`Temporal.PlainYearMonth.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/toLocaleString)

Returns a string with a language-sensitive representation of this year-month.

[`Temporal.PlainYearMonth.prototype.toPlainDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/toPlainDate)

Returns a new [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
 object representing this year-month and a supplied day in the same calendar system.

[`Temporal.PlainYearMonth.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/toString)

Returns a string representing this year-month in the [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#rfc_9557_format)
.

[`Temporal.PlainYearMonth.prototype.until()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/until)

Returns a new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration from this year-month to another year-month (in a form convertible by [`Temporal.PlainYearMonth.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/from)
). The duration is positive if the other month is after this month, and negative if before.

[`Temporal.PlainYearMonth.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/valueOf)

Throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, which prevents `Temporal.PlainYearMonth` instances from being [implicitly converted to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
 when used in arithmetic or comparison operations.

[`Temporal.PlainYearMonth.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/with)

Returns a new `Temporal.PlainYearMonth` object representing this year-month with some fields replaced by new values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal-plainyearmonth-objects](https://tc39.es/proposal-temporal/#sec-temporal-plainyearmonth-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
    
*   [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
    
*   [`Temporal.PlainMonthDay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainMonthDay)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/plainyearmonth/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/plainyearmonth (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainYearMonth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplainyearmonth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainYearMonth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplainyearmonth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F76c2e04d720aa8260ba7d75788ed96776aac35c6%0A*+Document+last+modified%3A+2026-09-18T02%3A05%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
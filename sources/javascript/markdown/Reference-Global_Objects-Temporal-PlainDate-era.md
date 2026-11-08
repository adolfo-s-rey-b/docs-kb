*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#mdn-search)
    

Temporal.PlainDate.prototype.era
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`era`** accessor property of [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
 instances returns a calendar-specific lowercase string representing the era of this date, or `undefined` if the calendar does not use eras (e.g., ISO 8601). `era` and `eraYear` together uniquely identify a year in a calendar, in the same way that `year` does. It is [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For Gregorian, it is either `"ce"` or `"bce"`.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#value)

-----------------------------------------------------------------------------------------------------------------------

All [specified calendars](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
 have eras fully defined by the spec.

*   The following calendars have a single era:
    
    *   `buddhist`: `"be"`
    *   `coptic`: `"am"`
    *   `ethioaa`: `"aa"`
    *   `hebrew`: `"am"`
    *   `indian`: `"shaka"`
    *   `persian`: `"ap"`
*   The following calendars have two eras. One is the _epoch era_, in which `eraYear` starts at 1 and is the same as [`year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year)
    . The other is the inverse era, in which `eraYear` also starts at 1 and is equal to `1 - year` (so `eraYear: 1` corresponds to year `0`, `eraYear: 2` to year `-1`, etc.):
    
    *   `gregory`: epoch era `"ce"`, inverse era `"bce"`
    *   `islamic-civil`, `islamic-tbla`, `islamic-umalqura`: epoch era `"ah"`, inverse era `"bh"`
    *   `roc`: epoch era `"roc"`, inverse era `"broc"`
*   The `ethiopic` calendar has an `"am"` era which is the epoch era. Years before `1` belong to the `"aa"` era, whose `eraYear` is equal to `year - 5500` (so `eraYear: -1000` corresponds to year `-6500`, `eraYear: 1` corresponds to year `-5499`, up to `eraYear: 5500` as year `0`).
    
*   The `japanese` calendar adds an era for each new emperor, so the output year and era for a future date may not match the input year and era when your code runs on a future engine version, and we won't enumerate them here. Each era's year starts at 1. It is also the only calendar known to have eras starting in the middle of a year, which means that the same `year` may correspond to different `(era, eraYear)` pairs depending on the month and day.
    
    **Warning:** As of October 2025, in the `japanese` calendar, dates prior to 1868-10-23 ISO (the start date of the year 1 Meiji) don't work as expected in browsers in two ways. First, [CLDR had the wrong start date for the Meiji era](https://unicode-org.atlassian.net/browse/CLDR-11375 "External link (opens in new tab)")
    , which causes calendar implementations to extend the Meiji era further to the past than it actually did. Second, the upcoming [Intl era and monthCode Proposal](https://tc39.es/proposal-intl-era-monthcode/ "External link (opens in new tab)")
     specifies that dates prior to 1873-01-01 ISO should use Gregorian eras, but browsers have traditionally used approximations of prior Japanese eras instead. The `japanese` calendar was taken into use on January 1, 6 Meiji / 1873-01-01 ISO, so these problems only affect proleptic dates.
    
*   Other [specified calendars](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
    : `chinese`, `dangi`, `iso8601`, don't use eras and return `undefined`.
    

The set accessor of `era` is `undefined`. You cannot change this property directly. Use the [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/with)
 method to create a new `Temporal.PlainDate` object with the desired new value. When setting eras, the `"ad"` and `"bc"` aliases are also accepted for the `"ce"` and `"bce"` eras of the `gregory` or `japanese` calendars.

**Note:** This string is not intended for display to users. Use [`toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/toLocaleString)
 with the appropriate options to get a localized string.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#examples)

-----------------------------------------------------------------------------------------------------------------------------

### [Using era](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#using_era)

### [Changing era](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#changing_era)

You can only set `era` for calendars that support them. For example, the ISO 8601 calendar does not have eras. Note that you must provide `era` and `eraYear` together.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-get-temporal.plaindate.prototype.era](https://tc39.es/proposal-temporal/#sec-get-temporal.plaindate.prototype.era) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
    
*   [`Temporal.PlainDate.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/with)
    
*   [`Temporal.PlainDate.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/add)
    
*   [`Temporal.PlainDate.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/subtract)
    
*   [`Temporal.PlainDate.prototype.year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year)
    
*   [`Temporal.PlainDate.prototype.eraYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/eraYear)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 19, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/plaindate/era/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/plaindate/era (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDate%2Fera&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindate%2Fera%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDate%2Fera%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindate%2Fera%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F483ce811e1ea52cb2d9d2a5af0c4d1c4d591ea4a%0A*+Document+last+modified%3A+2026-02-19T02%3A31%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
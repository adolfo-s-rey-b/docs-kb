*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#mdn-search)
    

Temporal.PlainDate.prototype.year
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`year`** accessor property of [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
 instances returns an integer representing the number of years of this date relative to the start of a calendar-specific epoch year. This property has the same function as the [`era`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era)
/[`eraYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/eraYear)
 pair as a unique identifier of a year in a calendar. It is [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#value)

------------------------------------------------------------------------------------------------------------------------

Usually year 1 is either the first year of the latest era or the ISO 8601 year `0001`. Because `year` is relative to the start of the epoch year, not the epoch date, if the epoch is in the middle of the year (only known to happen for the `japanese` calendar), that year will have the same `year` value before and after the start date of the era (for the `japanese` calendar, `year` is the same as the ISO 8601 year).

All [specified calendars](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
 have arithmetic years fully defined by the spec.

*   The following calendars have the same epoch year as ISO 8601: `chinese`, `dangi`, `gregory`, `japanese`, in which `year: 1` corresponds to the ISO year `1`.
*   The `buddhist` calendar uses the Buddhist epoch of 543 BCE, so `year: 1` corresponds to the ISO year `-542`.
*   The `coptic` calendar uses the Coptic epoch of 284 CE, so `year: 1` corresponds to the ISO year `284`.
*   The `ethioaa` calendar uses the Anno Mundi epoch of 5493 BCE, so `year: 1` corresponds to the ISO year `-5492`.
*   The `ethiopic` calendar uses the Ethiopic epoch of 8 CE, so `year: 1` corresponds to the ISO year `8`.
*   The `hebrew` calendar uses the Anno Mundi epoch of 3761 BCE, so `year: 1` corresponds to the ISO year `-3760`.
*   The `indian` calendar uses the Śaka epoch of 79 CE, so `year: 1` corresponds to the ISO year `79`.
*   The following calendars use the Hijri epoch of 622 CE: `islamic-civil`, `islamic-tbla`, `islamic-umalqura`, `persian`, in which `year: 1` corresponds to the ISO year `622`.
*   The `roc` calendar uses the Minguo epoch of 1912 CE, so `year: 1` corresponds to the ISO year `1912`.

**Note:** For the `chinese` and `dangi` calendars, the CLDR data uses the Huangdi epoch of 2637 BCE by default, but Temporal defined it to use the ISO 8601 epoch for simplicity.

The set accessor of `year` is `undefined`. You cannot change this property directly. Use the [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/with)
 method to create a new `Temporal.PlainDate` object with the desired new value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Using year](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#using_year)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-get-temporal.plaindate.prototype.year](https://tc39.es/proposal-temporal/#sec-get-temporal.plaindate.prototype.year) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
    
*   [`Temporal.PlainDate.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/with)
    
*   [`Temporal.PlainDate.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/add)
    
*   [`Temporal.PlainDate.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/subtract)
    
*   [`Temporal.PlainDate.prototype.era`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/era)
    
*   [`Temporal.PlainDate.prototype.eraYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/eraYear)
    
*   [`Temporal.PlainDate.prototype.yearOfWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/yearOfWeek)
    
*   [`Temporal.PlainDate.prototype.month`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/month)
    
*   [`Temporal.PlainDate.prototype.day`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/day)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate/year/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/plaindate/year/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/plaindate/year (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDate%2Fyear&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindate%2Fyear%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDate%2Fyear%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindate%2Fyear%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9b86874b5762b52ce0055f58d561004d1a204ad5%0A*+Document+last+modified%3A+2026-02-17T02%3A27%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
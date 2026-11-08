*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#mdn-search)
    

Temporal.PlainDateTime.prototype.toZonedDateTime()
==================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`toZonedDateTime()`** method of [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
 instances returns a new [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
 instance representing the same date-time as this plain date-time, but in the specified time zone.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#syntax)

-----------------------------------------------------------------------------------------------------------------------------------------

js

    toZonedDateTime(timeZone)
    toZonedDateTime(timeZone, options)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#parameters)

[`timeZone`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#timezone)

Either a string or a [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
 instance representing the time zone to use. If a `Temporal.ZonedDateTime` instance, its time zone is used. If a string, it can be a named time zone identifier, an offset time zone identifier, or a date-time string containing a time zone identifier or an offset (see [time zones and offsets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
 for more information).

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#options)

An object containing the following property:

[`disambiguation` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#disambiguation)

A string specifying what to do when this plain time corresponds to zero or more than one instants in the time zone, usually because of daylight saving time shifts. Possible values are `"compatible"`, `"earlier"`, `"later"`, and `"reject"`. Defaults to `"compatible"`. For more information about these values, see [ambiguity and gaps from local time to UTC time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ambiguity_and_gaps_from_local_time_to_utc_time)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#return_value)

A new [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
 instance representing the same date-time as this plain date-time, but in the specified time zone.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown in one of the following cases:

*   Any of the options is invalid.
*   `timeZone` is not a valid time zone identifier.
*   The wall-clock time is ambiguous in the time zone, and `options.disambiguation` is set to `"reject"`.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if any of the arguments are not of the expected type.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#examples)

---------------------------------------------------------------------------------------------------------------------------------------------

### [Using toZonedDateTime()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#using_tozoneddatetime)

js

    const dt = Temporal.PlainDateTime.from("2021-08-01T12:34:56");
    const zdt = dt.toZonedDateTime("America/New_York");
    console.log(zdt.toString()); // '2021-08-01T12:34:56-04:00[America/New_York]'
    
    const dt2 = Temporal.PlainDateTime.from("2021-01-01T12:34:56");
    const zdt2 = dt2.toZonedDateTime("America/New_York");
    console.log(zdt2.toString()); // '2021-01-01T12:34:56-05:00[America/New_York]'
    

### [Handling ambiguous times](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#handling_ambiguous_times)

Below, we have two wall-clock times that we want to interpret in the `America/New_York` time zone. The first one, `dtNotExist`, never existed because of a forward daylight saving time shift, so we need to choose from the times `01:05:00-05:00` or `03:05:00-04:00`. The second one, `dtAmbiguous`, appeared twice because of a backward daylight saving time shift, so we need to choose from the times `01:05:00-04:00` or `01:05:00-05:00`. For a more detailed explanation of this situation, see [ambiguity and gaps from local time to UTC time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ambiguity_and_gaps_from_local_time_to_utc_time)
.

js

    const dtNotExist = Temporal.PlainDateTime.from("2024-03-10T02:05:00");
    const dtAmbiguous = Temporal.PlainDateTime.from("2024-11-03T01:05:00");
    
    // Default: compatible
    console.log(dtNotExist.toZonedDateTime("America/New_York").toString());
    // '2024-03-10T03:05:00-04:00[America/New_York]'
    console.log(dtAmbiguous.toZonedDateTime("America/New_York").toString());
    // '2024-11-03T01:05:00-04:00[America/New_York]'
    
    // Use the earlier time for ambiguous times
    console.log(
      dtNotExist
        .toZonedDateTime("America/New_York", { disambiguation: "earlier" })
        .toString(),
    );
    // '2024-03-10T01:05:00-05:00[America/New_York]'
    console.log(
      dtAmbiguous
        .toZonedDateTime("America/New_York", { disambiguation: "earlier" })
        .toString(),
    );
    // '2024-11-03T01:05:00-04:00[America/New_York]'
    
    // Use the later time for ambiguous times
    console.log(
      dtNotExist
        .toZonedDateTime("America/New_York", { disambiguation: "later" })
        .toString(),
    );
    // '2024-03-10T03:05:00-04:00[America/New_York]'
    console.log(
      dtAmbiguous
        .toZonedDateTime("America/New_York", { disambiguation: "later" })
        .toString(),
    );
    // '2024-11-03T01:05:00-05:00[America/New_York]'
    
    // Throw an error for ambiguous times
    dtNotExist.toZonedDateTime("America/New_York", { disambiguation: "reject" });
    // RangeError: instant is ambiguous
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#specifications)

---------------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal.plaindatetime.prototype.tozoneddatetime](https://tc39.es/proposal-temporal/#sec-temporal.plaindatetime.prototype.tozoneddatetime) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime#see_also)

---------------------------------------------------------------------------------------------------------------------------------------------

*   [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
    
*   [`Temporal.ZonedDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime)
    
*   [`Temporal.PlainDateTime.prototype.toPlainDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toPlainDate)
    
*   [`Temporal.PlainDateTime.prototype.toPlainTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toPlainTime)
    
*   [`Temporal.ZonedDateTime.prototype.toPlainDateTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toPlainDateTime)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/plaindatetime/tozoneddatetime/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/plaindatetime/tozoneddatetime (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDateTime%2FtoZonedDateTime&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindatetime%2Ftozoneddatetime%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FPlainDateTime%2FtoZonedDateTime%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fplaindatetime%2Ftozoneddatetime%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
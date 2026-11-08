*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#mdn-search)
    

Date.prototype.getTimezoneOffset()
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`getTimezoneOffset()`** method of [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 instances returns the difference, in minutes, between this date as evaluated in the UTC time zone, and the same date as evaluated in the local time zone.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#try_it)

-------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#syntax)

-------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#return_value)

A number representing the difference, in minutes, between the date as evaluated in the UTC time zone and as evaluated in the local time zone. The actual local time algorithm is implementation-defined, and the return value is allowed to be zero in runtimes without appropriate data. Returns `NaN` if the date is [invalid](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#description)

-----------------------------------------------------------------------------------------------------------------------------------

`date.getTimezoneOffset()` returns the difference, in minutes, between `date` as evaluated in the UTC time zone and as evaluated in the local time zone — that is, the time zone of the host system in which the browser is being used (if the code is run from the Web in a browser), or otherwise the host system of whatever JavaScript runtime (for example, a Node.js environment) the code is executed in.

### [Negative values and positive values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#negative_values_and_positive_values)

The number of minutes returned by `getTimezoneOffset()` is positive if the local time zone is behind UTC, and negative if the local time zone is ahead of UTC. For example, for UTC+10, `-600` will be returned.

| Current time zone | Return value |
| --- | --- |
| UTC-8 | 480 |
| UTC | 0   |
| UTC+3 | \-180 |

### [Varied results in Daylight Saving Time (DST) regions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#varied_results_in_daylight_saving_time_dst_regions)

In a region that annually shifts in and out of Daylight Saving Time (DST), as `date` varies, the number of minutes returned by calling `getTimezoneOffset()` can be non-uniform.

**Note:** `getTimezoneOffset()`'s behavior will never differ based on the time when the code is run — its behavior is always consistent when running in the same region. Only the value of `date` affects the result.

**Note:** [Many countries have experimented with not changing the time twice a year](https://en.wikipedia.org/wiki/Daylight_saving_time_by_country#Past_observance "External link (opens in new tab)")
 and this has meant that DST has continued over the winter too. For example in the UK DST lasted from 2:00AM 18 February 1968 to 3:00AM 31 October 1971, so during the winter the clocks were not set back.

In most implementations, the [IANA time zone database](https://en.wikipedia.org/wiki/Daylight_saving_time#IANA_time_zone_database "External link (opens in new tab)")
 (tzdata) is used to precisely determine the offset of the local timezone at the moment of the `date`. However, if such information is unavailable, an implementation may return zero.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#examples)

-----------------------------------------------------------------------------------------------------------------------------

### [Using getTimezoneOffset()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#using_gettimezoneoffset)

### [getTimezoneOffset() and DST](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#gettimezoneoffset_and_dst)

In regions that use DST, the return value may change based on the time of the year `date` is in. Below is the output in a runtime in New York, where the timezone is UTC-05:00.

### [getTimezoneOffset() and historical data](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#gettimezoneoffset_and_historical_data)

Due to historical reasons, the timezone a region is in can be constantly changing, even disregarding DST. For example, below is the output in a runtime in Shanghai, where the timezone is UTC+08:00.

This is because during the [Sino-Japanese War](https://en.wikipedia.org/wiki/Second_Sino-Japanese_War "External link (opens in new tab)")
 when Shanghai was under Japanese control, the timezone was changed to UTC+09:00 to align with Japan's (in effect, it was a "year-round DST"), and this was recorded in the IANA database.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date.prototype.gettimezoneoffset](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date.prototype.gettimezoneoffset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/gettimezoneoffset/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date/gettimezoneoffset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FgetTimezoneOffset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fgettimezoneoffset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FgetTimezoneOffset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fgettimezoneoffset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
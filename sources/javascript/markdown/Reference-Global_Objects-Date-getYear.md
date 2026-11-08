*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#mdn-search)
    

Date.prototype.getYear()
========================

Deprecated

Avoid using this feature in new projects. The `getYear()` and `setYear()` methods use a truncated number instead of the actual year number, known as a year 2000 problem. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`getYear()`** method of [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 instances returns the year for this date according to local time. Because `getYear()` does not return full years ("year 2000 problem"), it is deprecated and has been replaced by the [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
 method.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#syntax)

---------------------------------------------------------------------------------------------------------------

js

    getYear()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#return_value)

An integer representing the year for the given date according to local time, minus 1900. Returns `NaN` if the date is [invalid](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
.

*   For years greater than or equal to 2000, the value is 100 or greater. For example, if the year is 2026, `getYear()` returns 126.
*   For years between and including 1900 and 1999, the value returned by `getYear()` is between 0 and 99. For example, if the year is 1976, `getYear()` returns 76.
*   For years less than 1900, the value returned by `getYear()` is less than 0. For example, if the year is 1800, `getYear()` returns -100.

This method essentially returns the value of [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
 minus 1900. You should use `getFullYear()` instead, so that the year is specified in full.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#examples)

-------------------------------------------------------------------------------------------------------------------

### [Years between 1900 and 1999](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#years_between_1900_and_1999)

The second statement assigns the value 95 to the variable `year`.

js

    const xmas = new Date("1995-12-25");
    const year = xmas.getYear(); // returns 95
    

### [Years above 1999](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#years_above_1999)

The second statement assigns the value 100 to the variable `year`.

js

    const xmas = new Date("2000-12-25");
    const year = xmas.getYear(); // returns 100
    

### [Years below 1900](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#years_below_1900)

The second statement assigns the value -100 to the variable `year`.

js

    const xmas = new Date("1800-12-25");
    const year = xmas.getYear(); // returns -100
    

### [Setting and getting a year between 1900 and 1999](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#setting_and_getting_a_year_between_1900_and_1999)

The third statement assigns the value 95 to the variable `year`, representing the year 1995.

js

    const xmas = new Date("2015-12-25");
    xmas.setYear(95);
    const year = xmas.getYear(); // returns 95
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date.prototype.getyear](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html#sec-date.prototype.getyear) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Date.prototype.getYear` in `core-js`](https://core-js.io/docs/features/ecmascript/date "External link (opens in new tab)")
    
*   [es-shims polyfill of `Date.prototype.getYear`](https://www.npmjs.com/package/date.prototype.getyear "External link (opens in new tab)")
    
*   [`Date.prototype.getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
    
*   [`Date.prototype.getUTCFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCFullYear)
    
*   [`Date.prototype.setYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setYear)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/getyear/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date/getyear (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FgetYear&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fgetyear%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FgetYear%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Fgetyear%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
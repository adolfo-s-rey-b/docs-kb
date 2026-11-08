*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#mdn-search)
    

RangeError: invalid date
========================

The JavaScript exception "invalid date" occurs when an invalid date is attempted to be converted to an ISO date string.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#message)

---------------------------------------------------------------------------------------------------------

RangeError: Invalid time value (V8-based)
RangeError: invalid date (Firefox)
RangeError: Invalid Date (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#error_type)

---------------------------------------------------------------------------------------------------------------

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------

You are converting an [invalid date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
 value to an ISO date string by calling the [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
 method.

An _invalid date_ is produced when you attempt to parse an invalid date string, or set the timestamp to an out-of-bounds value. Invalid dates usually cause all date methods to return [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 or other special values. However, such dates do not have valid ISO string representations, so an error is thrown when you attempt to do so.

**Note:** [`toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON)
 does not throw this error. It checks whether the date is finite before formatting it, and returns `null` for an invalid date instead of calling `toISOString()`. [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
, which calls `toJSON()`, therefore serializes an invalid date as `null` rather than throwing.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#examples)

-----------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#invalid_cases)

js

    const invalid = new Date("nothing");
    invalid.toISOString(); // RangeError: invalid date
    

However, most other methods return special values:

js

    invalid.toString(); // "Invalid Date"
    invalid.getDate(); // NaN
    invalid.toJSON(); // null
    JSON.stringify({ date: invalid }); // '{"date":null}'
    

For more details, see the [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
 documentation.

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#valid_cases)

js

    new Date("05 October 2011 14:48 UTC").toISOString(); // "2011-10-05T14:48:00.000Z"
    new Date(1317826080).toISOString(); // "2011-10-05T14:48:00.000Z"
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    
*   [`Date.prototype.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
    
*   [`Date.prototype.toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_date/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/invalid_date/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/invalid_date (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FInvalid_date&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Finvalid_date%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FInvalid_date%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Finvalid_date%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d4628c5144f459ddb081a3e58d0e56f0c2db673%0A*+Document+last+modified%3A+2026-09-02T02%3A16%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
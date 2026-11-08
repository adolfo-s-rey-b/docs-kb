*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times#mdn-search)
    

Representing dates & times
==========================

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
    

**Note:** The `Date` object is now considered legacy and should be avoided in new code. We will update this page with modern alternatives soon.

[Date object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times#date_object)

------------------------------------------------------------------------------------------------------------------

JavaScript does not have a date data type. However, you can use the [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 object and its methods to work with dates and times in your applications. The `Date` object has a large number of methods for setting, getting, and manipulating dates. It does not have any properties.

JavaScript handles dates similarly to Java. The two languages have many of the same date methods, and both languages store dates as the number of milliseconds since midnight at the beginning of January 1, 1970, UTC, with a Unix Timestamp being the number of seconds since the same instant. The instant at the midnight at the beginning of January 1, 1970, UTC is called the [epoch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
.

The `Date` object range is -100,000,000 days to 100,000,000 days relative to the epoch.

To create a `Date` object:

where `dateObjectName` is the name of the `Date` object being created; it can be a new object or a property of an existing object.

Calling `Date` without the `new` keyword returns a string representing the current date and time.

The `parameters` in the preceding syntax can be any of the following:

*   Nothing: creates today's date and time. For example, `today = new Date();`.
*   A string representing a date, in many different forms. The exact forms supported differ among engines, but the following form is always supported: `YYYY-MM-DDTHH:mm:ss.sssZ`. For example, `xmas95 = new Date("1995-12-25")`. If you omit hours, minutes, or seconds, the value will be set to zero.
*   A set of integer values for year, month, and day. For example, `xmas95 = new Date(1995, 11, 25)`.
*   A set of integer values for year, month, day, hour, minute, and seconds. For example, `xmas95 = new Date(1995, 11, 25, 9, 30, 0);`.

### [Methods of the Date object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times#methods_of_the_date_object)

The `Date` object methods for handling dates and times fall into these broad categories:

*   "set" methods, for setting date and time values in `Date` objects.
*   "get" methods, for getting date and time values from `Date` objects.
*   "to" methods, for returning string values from `Date` objects.
*   parse and UTC methods, for parsing `Date` strings.

With the "get" and "set" methods you can get and set seconds, minutes, hours, day of the month, day of the week, months, and years separately. There is a `getDay` method that returns the day of the week, but no corresponding `setDay` method, because the day of the week is set automatically. These methods use integers to represent these values as follows:

*   Seconds and minutes: 0 to 59
*   Hours: 0 to 23
*   Day: 0 (Sunday) to 6 (Saturday)
*   Date: 1 to 31 (day of the month)
*   Months: 0 (January) to 11 (December)
*   Year: years since 1900

For example, suppose you define the following date:

Then `xmas95.getMonth()` returns 11, and `xmas95.getFullYear()` returns 1995.

The `getTime` and `setTime` methods are useful for comparing dates. The `getTime` method returns the number of milliseconds since the epoch for a `Date` object.

For example, the following code displays the number of days left in the current year:

This example creates a `Date` object named `today` that contains today's date. It then creates a `Date` object named `endYear` and sets the year to the current year. Then, using the number of milliseconds per day, it computes the number of days between `today` and `endYear`, using `getTime` and rounding to a whole number of days.

The `parse` method is useful for assigning values from date strings to existing `Date` objects. For example, the following code uses `parse` and `setTime` to assign a date value to the `ipoDate` object:

### [Example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times#example)

In the following example, the function `JSClock()` returns the time in the format of a digital clock.

The `JSClock` function first creates a new `Date` object called `time`; since no arguments are given, time is created with the current date and time. Then calls to the `getHours`, `getMinutes`, and `getSeconds` methods assign the value of the current hour, minute, and second to `hour`, `minute`, and `second`.

The following statements build a string value based on the time. The first statement creates a variable `temp`. Its value is `hour % 12`, which is `hour` in the 12-hour system. Then, if the hour is `0`, it gets re-assigned to `12`, so that midnights and noons are displayed as `12:00` instead of `0:00`.

The next statement appends a `minute` value to `temp`. If the value of `minute` is less than 10, the conditional expression adds a string with a preceding zero; otherwise it adds a string with a demarcating colon. Then a statement appends a seconds value to `temp` in the same way.

Finally, a conditional expression appends "P.M." to `temp` if `hour` is 12 or greater; otherwise, it appends "A.M." to `temp`.

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/representing_dates_times/index.md?plain=1 "Folder: en-us/web/javascript/guide/representing_dates_times (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRepresenting_dates_times&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Frepresenting_dates_times%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRepresenting_dates_times%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Frepresenting_dates_times%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
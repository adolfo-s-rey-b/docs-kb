*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#mdn-search)
    

Date.prototype.toLocaleTimeString()
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`toLocaleTimeString()`** method of [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 instances returns a string with a language-sensitive representation of the time portion of this date in the local timezone. In implementations with [`Intl.DateTimeFormat` API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
 support, this method delegates to `Intl.DateTimeFormat`.

Every time `toLocaleTimeString` is called, it has to perform a search in a big database of localization strings, which is potentially inefficient. When the method is called many times with the same arguments, it is better to create an [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
 object and use its [`format()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)
 method, because a `DateTimeFormat` object remembers the arguments passed to it and may decide to cache a slice of the database, so future `format` calls can search for localization strings within a more constrained context.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#try_it)

--------------------------------------------------------------------------------------------------------------------------

    // Depending on timezone, your results will vary
    const event = new Date("August 19, 1975 23:15:30 GMT+00:00");
    
    console.log(event.toLocaleTimeString("en-US"));
    // Expected output: "1:15:30 AM"
    
    console.log(event.toLocaleTimeString("it-IT"));
    // Expected output: "01:15:30"
    
    console.log(event.toLocaleTimeString("ar-EG"));
    // Expected output: "١٢:١٥:٣٠ ص"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#syntax)

--------------------------------------------------------------------------------------------------------------------------

js

    toLocaleTimeString()
    toLocaleTimeString(locales)
    toLocaleTimeString(locales, options)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#parameters)

The `locales` and `options` parameters customize the behavior of the function and let applications specify the language whose formatting conventions should be used.

In implementations that support the [`Intl.DateTimeFormat` API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
, these parameters correspond exactly to the [`Intl.DateTimeFormat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)
 constructor's parameters. Implementations without `Intl.DateTimeFormat` support are asked to ignore both parameters, making the locale used and the form of the string returned entirely implementation-dependent.

[`locales` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
, or an array of such strings. Corresponds to the [`locales`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#locales)
 parameter of the `Intl.DateTimeFormat()` constructor.

In implementations without `Intl.DateTimeFormat` support, this parameter is ignored and the host's locale is usually used.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#options)

An object adjusting the output format. Corresponds to the [`options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#options)
 parameter of the `Intl.DateTimeFormat()` constructor. If `dayPeriod`, `hour`, `minute`, `second`, and `fractionalSecondDigits` are all undefined, then `hour`, `minute`, `second` will be set to `"numeric"`.

In implementations without `Intl.DateTimeFormat` support, this parameter is ignored.

See the [`Intl.DateTimeFormat()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat)
 for details on these parameters and how to use them.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#return_value)

A string representing the time portion of the given date according to language-specific conventions.

In implementations with `Intl.DateTimeFormat`, this is equivalent to `new Intl.DateTimeFormat(locales, options).format(date)`, where `options` has been normalized as described above.

**Note:** Most of the time, the formatting returned by `toLocaleTimeString()` is consistent. However, the output may vary between implementations, even within the same locale — output variations are by design and allowed by the specification. It may also not be what you expect. For example, the string may use non-breaking spaces or be surrounded by bidirectional control characters. You should not compare the results of `toLocaleTimeString()` to hardcoded constants.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Using toLocaleTimeString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#using_tolocaletimestring)

Basic use of this method without specifying a `locale` returns a formatted string in the default locale and with default options.

js

    const date = new Date(Date.UTC(2012, 11, 12, 3, 0, 0));
    
    // toLocaleTimeString() without arguments depends on the implementation,
    // the default locale, and the default time zone
    console.log(date.toLocaleTimeString());
    // "7:00:00 PM" if run in en-US locale with time zone America/Los_Angeles
    

### [Checking for support for locales and options parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#checking_for_support_for_locales_and_options_parameters)

The `locales` and `options` parameters may not be supported in all implementations, because support for the internationalization API is optional, and some systems may not have the necessary data. For implementations without internationalization support, `toLocaleTimeString()` always uses the system's locale, which may not be what you want. Because any implementation that supports the `locales` and `options` parameters must support the [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
 API, you can check the existence of the latter for support:

js

    function toLocaleTimeStringSupportsLocales() {
      return (
        typeof Intl === "object" &&
        !!Intl &&
        typeof Intl.DateTimeFormat === "function"
      );
    }
    

### [Using locales](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#using_locales)

This example shows some of the variations in localized time formats. In order to get the format of the language used in the user interface of your application, make sure to specify that language (and possibly some fallback languages) using the `locales` argument:

js

    const date = new Date(Date.UTC(2012, 11, 20, 3, 0, 0));
    
    // formats below assume the local time zone of the locale;
    // America/Los_Angeles for the US
    
    // US English uses 12-hour time with AM/PM
    console.log(date.toLocaleTimeString("en-US"));
    // "7:00:00 PM"
    
    // British English uses 24-hour time without AM/PM
    console.log(date.toLocaleTimeString("en-GB"));
    // "03:00:00"
    
    // Korean uses 12-hour time with AM/PM
    console.log(date.toLocaleTimeString("ko-KR"));
    // "오후 12:00:00"
    
    // Arabic in most Arabic speaking countries uses real Arabic digits
    console.log(date.toLocaleTimeString("ar-EG"));
    // "٧:٠٠:٠٠ م"
    
    // when requesting a language that may not be supported, such as
    // Balinese, include a fallback language, in this case Indonesian
    console.log(date.toLocaleTimeString(["ban", "id"]));
    // "11.00.00"
    

### [Using options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#using_options)

The results provided by `toLocaleTimeString()` can be customized using the `options` parameter:

js

    const date = new Date(Date.UTC(2012, 11, 20, 3, 0, 0));
    
    // An application may want to use UTC and make that visible
    const options = { timeZone: "UTC", timeZoneName: "short" };
    console.log(date.toLocaleTimeString("en-US", options));
    // "3:00:00 AM GMT"
    
    // Sometimes even the US needs 24-hour time
    console.log(date.toLocaleTimeString("en-US", { hour12: false }));
    // "19:00:00"
    
    // Show only hours and minutes, use options with the default locale - use an empty array
    console.log(
      date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    );
    // "20:01"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#specifications)

------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date.prototype.tolocaletimestring](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date.prototype.tolocaletimestring) |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sup-date.prototype.tolocaletimestring](https://tc39.es/ecma402/#sup-date.prototype.tolocaletimestring) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
    
*   [`Date.prototype.toLocaleDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)
    
*   [`Date.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)
    
*   [`Date.prototype.toTimeString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString)
    
*   [`Date.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/tolocaletimestring/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date/tolocaletimestring (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FtoLocaleTimeString&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Ftolocaletimestring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%2FtoLocaleTimeString%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Ftolocaletimestring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
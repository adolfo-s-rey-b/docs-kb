*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#mdn-search)
    

Intl.RelativeTimeFormat.prototype.format()
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`format()`** method of [`Intl.RelativeTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)
 instances formats a `value` and `unit` according to the locale and formatting options of this `Intl.RelativeTimeFormat` object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#try_it)

---------------------------------------------------------------------------------------------------------------------------------

    const rtf = new Intl.RelativeTimeFormat("en", { style: "short" });
    
    console.log(rtf.format(3, "quarter"));
    // Expected output: "in 3 qtrs."
    
    console.log(rtf.format(-1, "day"));
    // Expected output: "1 day ago"
    
    console.log(rtf.format(10, "seconds"));
    // Expected output: "in 10 sec."
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#syntax)

---------------------------------------------------------------------------------------------------------------------------------

js

    format(value, unit)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#parameters)

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#value)

Numeric value to use in the internationalized relative time message.

[`unit`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#unit)

Unit to use in the relative time internationalized message. Possible values are: `"year"`, `"quarter"`, `"month"`, `"week"`, `"day"`, `"hour"`, `"minute"`, `"second"`. Plural forms are also permitted.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#return_value)

A string representing the given `value` and `unit` formatted according to the locale and formatting options of this [`Intl.RelativeTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)
 object.

**Note:** Most of the time, the formatting returned by `format()` is consistent. However, the output may vary between implementations, even within the same locale — output variations are by design and allowed by the specification. It may also not be what you expect. For example, the string may use non-breaking spaces or be surrounded by bidirectional control characters. You should not compare the results of `format()` to hardcoded constants.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#examples)

-------------------------------------------------------------------------------------------------------------------------------------

### [Basic format usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#basic_format_usage)

The following example shows how to create a relative time formatter using the English language.

js

    // Create a relative time formatter in your locale
    // with default values explicitly passed in.
    const rtf = new Intl.RelativeTimeFormat("en", {
      localeMatcher: "best fit", // other values: "lookup"
      numeric: "always", // other values: "auto"
      style: "long", // other values: "short" or "narrow"
    });
    
    // Format relative time using negative value (-1).
    rtf.format(-1, "day"); // "1 day ago"
    
    // Format relative time using positive value (1).
    rtf.format(1, "day"); // "in 1 day"
    

### [Using the auto option](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#using_the_auto_option)

If the `numeric: "auto"` option is passed, it will produce the string `yesterday`, `today`, or `tomorrow` instead of `1 day ago`, `in 0 days`, or `in 1 day`. This allows you to avoid using numeric values in the output.

js

    // Create a relative time formatter in your locale
    // with numeric: "auto" option value passed in.
    const rtf = new Intl.RelativeTimeFormat("en", { numeric: "auto" });
    
    // Format relative time using negative value (-1).
    rtf.format(-1, "day"); // "yesterday"
    
    rtf.format(0, "day"); // "today"
    
    // Format relative time using positive day unit (1).
    rtf.format(1, "day"); // "tomorrow"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-Intl.RelativeTimeFormat.prototype.format](https://tc39.es/ecma402/#sec-Intl.RelativeTimeFormat.prototype.format) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format#see_also)

-------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.RelativeTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/relativetimeformat/format/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/relativetimeformat/format (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FRelativeTimeFormat%2Fformat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Frelativetimeformat%2Fformat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FRelativeTimeFormat%2Fformat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Frelativetimeformat%2Fformat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
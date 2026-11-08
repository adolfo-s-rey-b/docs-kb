*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#mdn-search)
    

Intl.DisplayNames.prototype.of()
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`of()`** method of [`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)
 instances receives a code and returns a string based on the locale and options provided when instantiating this `Intl.DisplayNames` object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#try_it)

-----------------------------------------------------------------------------------------------------------------------

    const regionNamesInEnglish = new Intl.DisplayNames(["en"], { type: "region" });
    const regionNamesInTraditionalChinese = new Intl.DisplayNames(["zh-Hant"], {
      type: "region",
    });
    
    console.log(regionNamesInEnglish.of("US"));
    // Expected output: "United States"
    
    console.log(regionNamesInTraditionalChinese.of("US"));
    // Expected output: "美國"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#syntax)

-----------------------------------------------------------------------------------------------------------------------

js

    of(code)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#parameters)

[`code`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#code)

The `code` to provide depends on the `type`:

*   If the type is "region", `code` should be either a [two-letter ISO 3166 region code](https://www.iso.org/iso-3166-country-codes.html "External link (opens in new tab)")
    , or a [three-digit UN M49 geographic region](https://unstats.un.org/unsd/methodology/m49/ "External link (opens in new tab)")
    . It is required to follow the [`unicode_region_subtag`](https://unicode.org/reports/tr35/#unicode_region_subtag "External link (opens in new tab)")
     grammar. Use uppercase codes (e.g., `"US"`), because lowercase ones (e.g., `"us"`) may not work reliably everywhere.
*   If the type is "script", `code` should be a [four-letter ISO 15924 script code](https://unicode.org/iso15924/iso15924-codes.html "External link (opens in new tab)")
    . It is required to follow the [`unicode_script_subtag`](https://unicode.org/reports/tr35/#unicode_script_subtag "External link (opens in new tab)")
     grammar.
*   If the type is "language", `code` should be matched by the [`unicode_language_id`](https://unicode.org/reports/tr35/#Unicode_language_identifier "External link (opens in new tab)")
     nonterminal.
*   If the type is "currency", `code` should be a [three-letter ISO 4217 currency code](https://www.iso.org/iso-4217-currency-codes.html "External link (opens in new tab)")
    . It is required to have exactly three alphabetic characters.
*   If the type is "dateTimeField", `code` should be one of: `"era"`, `"year"`, `"quarter"`, `"month"`, `"weekOfYear"`, `"weekday"`, `"day"`, `"dayPeriod"`, `"hour"`, `"minute"`, `"second"`, `"timeZoneName"`.
*   If the type is "calendar", `code` should be a [calendar key](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar)
    . It is required to follow the `type` grammar of a [Unicode locale identifier](https://unicode.org/reports/tr35/#32-unicode-locale-identifier "External link (opens in new tab)")
    .

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#return_value)

A language-specific formatted string, or `undefined` if there's no data for the input and `fallback` is `"none"`.

**Note:** `fallback` is only used if `code` is structurally valid. See [using fallback](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#using_fallback)
.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `code` is not structurally valid for the given `type`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Using the of method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#using_the_of_method)

js

    const regionNames = new Intl.DisplayNames("en", { type: "region" });
    regionNames.of("419"); // "Latin America"
    
    const languageNames = new Intl.DisplayNames("en", { type: "language" });
    languageNames.of("fr"); // "French"
    
    const currencyNames = new Intl.DisplayNames("en", { type: "currency" });
    currencyNames.of("EUR"); // "Euro"
    
    const languageNamesStandard = new Intl.DisplayNames("fr", {
      type: "language",
      languageDisplay: "standard",
    });
    languageNamesStandard.of("fr-CA"); // "français (Canada)"
    
    const languageNamesDialect = new Intl.DisplayNames("fr", {
      type: "language",
      languageDisplay: "dialect",
    });
    languageNamesDialect.of("fr-CA"); // "français canadien"
    

### [Using fallback](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#using_fallback)

When the `Intl.DisplayNames` is constructed with `fallback: "code"`, the `of()` method will return the `code` if the input looks structurally valid but there's no data for the input. If `fallback` is `"none"`, `undefined` is returned.

js

    console.log(
      new Intl.DisplayNames("en", { type: "region", fallback: "code" }).of("ZL"),
    ); // "ZL"
    
    console.log(
      new Intl.DisplayNames("en", { type: "region", fallback: "none" }).of("ZL"),
    ); // undefined
    

However, this only applies if the `code` is structurally valid. For example, if `type` is `"region"` but `code` does not follow the `unicode_region_subtag` grammar (2 alphabetic characters or 3 numeric characters), a [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 is directly thrown instead of using the fallback.

js

    console.log(
      new Intl.DisplayNames("en", { type: "region", fallback: "code" }).of("ZLC"),
    ); // throws RangeError: invalid value "ZLC" for option region
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-Intl.DisplayNames.prototype.of](https://tc39.es/ecma402/#sec-Intl.DisplayNames.prototype.of) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/displaynames/of/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/displaynames/of (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames%2Fof&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%2Fof%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames%2Fof%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%2Fof%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#mdn-search)
    

Intl.DisplayNames() constructor
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.DisplayNames()`** constructor creates [`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)
 objects.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#try_it)

---------------------------------------------------------------------------------------------------------------------------------

    const regionNamesInEnglish = new Intl.DisplayNames(["en"], { type: "region" });
    const regionNamesInTraditionalChinese = new Intl.DisplayNames(["zh-Hant"], {
      type: "region",
    });
    
    console.log(regionNamesInEnglish.of("US"));
    // Expected output: "United States"
    
    console.log(regionNamesInTraditionalChinese.of("US"));
    // Expected output: "美國"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#syntax)

---------------------------------------------------------------------------------------------------------------------------------

js

    new Intl.DisplayNames(locales, options)
    

**Note:** `Intl.DisplayNames()` can only be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Attempting to call it without `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#parameters)

[`locales`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 or an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instance, or an array of such locale identifiers. The runtime's default locale is used when `undefined` is passed or when none of the specified locale identifiers is supported. For the general form and interpretation of the `locales` argument, see [the parameter description on the `Intl` main page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)
.

[`options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#options)

An object containing the following properties, in the order they are retrieved:

[`localeMatcher` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#localematcher)

The locale matching algorithm to use. Possible values are `"lookup"` and `"best fit"`; the default is `"best fit"`. For information about this option, see [Locale identification and negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
.

[`style` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#style)

The formatting style to use. Possible values are `"narrow"`, `"short"`, and `"long"`; the default is `"long"`.

[`type`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#type)

The type of display names to return from [`of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of)
. Possible values are `"language"`, `"region"`, `"script"`, `"currency"`, `"calendar"`, and `"dateTimeField"`.

[`fallback` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#fallback)

What to return from `of()` if the input is structurally valid but there's no matching display name. Possible values are:

[`"code"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#code)

Return the input code itself.

[`"none"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#none)

Return `undefined`.

[`languageDisplay` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#languagedisplay)

How language names should be displayed. Only usable along with `type: "language"`. Possible values are:

[`"dialect"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#dialect)

Display special regional dialects using their own name. E.g. `"nl-BE"` will be displayed as `"Flemish"`.

[`"standard"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#standard)

Display all languages using standard format. E.g. `"nl-BE"` will be displayed as `"Dutch (Belgium)"`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if `options.type` is not provided.

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `locales` or `options` contain invalid values.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#examples)

-------------------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#basic_usage)

In basic use without specifying a locale, a formatted string in the default locale and with default options is returned.

js

    console.log(new Intl.DisplayNames([], { type: "language" }).of("US"));
    // 'us'
    

### [Using type `dateTimeField`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#using_type_datetimefield)

Example using `dateTimeField` as a type option, will return the localized date time names strings.

js

    const dn = new Intl.DisplayNames("pt", { type: "dateTimeField" });
    console.log(dn.of("era")); // 'era'
    console.log(dn.of("year")); // 'ano'
    console.log(dn.of("month")); // 'mês'
    console.log(dn.of("quarter")); // 'trimestre'
    console.log(dn.of("weekOfYear")); // 'semana'
    console.log(dn.of("weekday")); // 'dia da semana'
    console.log(dn.of("dayPeriod")); // 'AM/PM'
    console.log(dn.of("day")); // 'dia'
    console.log(dn.of("hour")); // 'hora'
    console.log(dn.of("minute")); // 'minuto'
    console.log(dn.of("second")); // 'segundo'
    

### [Using type `calendar`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#using_type_calendar)

Example using `calendar` as a type option, will return the localized calendar names strings.

js

    const dn = new Intl.DisplayNames("en", { type: "calendar" });
    console.log(dn.of("roc")); // 'Minguo Calendar'
    console.log(dn.of("gregory")); // 'Gregorian Calendar'
    console.log(dn.of("chinese")); // 'Chinese Calendar'
    

### [Using type `language` with `languageDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#using_type_language_with_languagedisplay)

Example using `language` as a type with `languageDisplay` options.

js

    // Using `dialect` option
    const dnDialect = new Intl.DisplayNames("en", {
      type: "language",
      languageDisplay: "dialect",
    });
    console.log(dnDialect.of("en-GB")); // 'British English'
    
    // Using `standard` option
    const dnStd = new Intl.DisplayNames("en", {
      type: "language",
      languageDisplay: "standard",
    });
    console.log(dnStd.of("en-GB")); // 'English (United Kingdom)'
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-intl-displaynames-constructor](https://tc39.es/ecma402/#sec-intl-displaynames-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames#see_also)

-------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)
    
*   [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf)
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/displaynames/displaynames/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/displaynames/displaynames (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames%2FDisplayNames&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%2Fdisplaynames%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames%2FDisplayNames%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%2Fdisplaynames%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
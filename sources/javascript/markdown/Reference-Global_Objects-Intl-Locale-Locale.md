*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#mdn-search)
    

Intl.Locale() constructor
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.Locale()`** constructor creates [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 objects.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#try_it)

---------------------------------------------------------------------------------------------------------------------

    const korean = new Intl.Locale("ko", {
      script: "Kore",
      region: "KR",
      hourCycle: "h23",
      calendar: "gregory",
    });
    
    const japanese = new Intl.Locale("ja-Jpan-JP-u-ca-japanese-hc-h12");
    
    console.log(korean.baseName, japanese.baseName);
    // Expected output: "ko-Kore-KR" "ja-Jpan-JP"
    
    console.log(korean.hourCycle, japanese.hourCycle);
    // Expected output: "h23" "h12"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#syntax)

---------------------------------------------------------------------------------------------------------------------

js

    new Intl.Locale(tag)
    new Intl.Locale(tag, options)
    

**Note:** `Intl.Locale()` can only be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Attempting to call it without `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#parameters)

[`tag`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#tag)

The Unicode locale identifier string. For the syntax of locale identifier strings, see the [Intl main page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)
. Note that the `Intl.Locale` constructor, unlike most other `Intl` constructors, does not accept an array of locales or `undefined`.

[`options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#options)

An object that contains configuration for the Locale. Option values here take priority over extension keys in the locale identifier. Possible properties are:

[`language`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#language)

The [language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language)
. Any syntactically valid string following the [`unicode_language_subtag`](https://unicode.org/reports/tr35/#unicode_language_subtag "External link (opens in new tab)")
 grammar (2–3 or 5–8 letters) is accepted, but the implementation only recognizes certain kinds.

[`script`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#script)

The [script](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script)
. Any syntactically valid string following the [`unicode_script_subtag`](https://unicode.org/reports/tr35/#unicode_script_subtag "External link (opens in new tab)")
 grammar (4 letters) is accepted, but the implementation only recognizes certain kinds.

[`region`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#region)

The [region](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/region)
. Any syntactically valid string following the [`unicode_region_subtag`](https://unicode.org/reports/tr35/#unicode_region_subtag "External link (opens in new tab)")
 grammar (either 2 letters or 3 digits) is accepted, but the implementation only recognizes certain kinds.

[`variants`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#variants)

The [variants](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/variants)
. It should be a dash (`-`) separated list of _unique_ variant tags, where each tag is any syntactically valid string following the [`unicode_variant_subtag`](https://unicode.org/reports/tr35/#unicode_variant_subtag "External link (opens in new tab)")
 grammar (either 5–8 alphanumerals or a digit followed by 3 alphanumerals), but the implementation only recognizes certain kinds.

[`calendar`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#calendar)

The [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar)
. Any syntactically valid string following the [`type`](https://unicode.org/reports/tr35/#Unicode_locale_identifier "External link (opens in new tab)")
 grammar (one or more segments of 3–8 alphanumerals, joined by hyphens) is accepted, but the implementation only recognizes certain kinds, which are listed in [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
.

[`collation`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#collation)

The [collation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/collation)
. Any syntactically valid string following the `type` grammar is accepted, but the implementation only recognizes certain kinds, which are listed in [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_collation_types)
.

[`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numberingsystem)

The [numbering system](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numberingSystem)
. Any syntactically valid string following the `type` grammar is accepted, but the implementation only recognizes certain kinds, which are listed in [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_numbering_system_types)
.

[`caseFirst`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#casefirst)

The [case-first sort option](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst)
. Possible values are `"upper"`, `"lower"`, or `"false"`.

[`hourCycle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#hourcycle)

The [hour cycle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/hourCycle)
. Possible values are `"h23"`, `"h12"`, `"h11"`, or the practically unused `"h24"`, which are explained in [`Intl.Locale.prototype.getHourCycles`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getHourCycles#supported_hour_cycle_types)

[`numeric`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#numeric)

The [numeric sort option](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/numeric)
. A boolean.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#basic_usage)

At its very simplest, the `Intl.Locale()` constructor takes a locale identifier string as its argument:

js

    const us = new Intl.Locale("en-US");
    

### [Using the Locale constructor with an options object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#using_the_locale_constructor_with_an_options_object)

The constructor also takes an optional configuration object argument, which can contain any of several extension types. For example, set the [`hourCycle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/hourCycle)
 property of the configuration object to your desired hour cycle type, and then pass it into the constructor:

js

    const locale = new Intl.Locale("en-US", { hourCycle: "h12" });
    console.log(locale.hourCycle); // "h12"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-intl-locale-constructor](https://tc39.es/ecma402/#sec-intl-locale-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
    
*   [Canonical Unicode Locale Identifiers](https://www.unicode.org/reports/tr35/#Canonical_Unicode_Locale_Identifiers "External link (opens in new tab)")
     in the Unicode locale data markup language spec

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 22, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/locale/locale/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/locale/locale (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2FLocale&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Flocale%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2FLocale%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Flocale%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe509776556a47f12843b91ab5c6e9be6585698c6%0A*+Document+last+modified%3A+2025-07-22T12%3A08%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
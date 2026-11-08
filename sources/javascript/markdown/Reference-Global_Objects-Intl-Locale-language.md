*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#mdn-search)
    

Intl.Locale.prototype.language
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`language`** accessor property of [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instances returns the language associated with this locale.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#description)

---------------------------------------------------------------------------------------------------------------------------------

Language is one of the core attributes of a locale. The Unicode specification treats the language identifier of a locale as the language and the region together (to make a distinction between dialects and variations, e.g., British English vs. American English). The `language` property of an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 returns strictly the locale's language subtag.

The `language` property's value is set at construction time, either through the first part of the locale identifier or through the `language` option of the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor. The latter takes priority if they are both present.

The set accessor of `language` is `undefined`. You cannot change this property directly.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#examples)

---------------------------------------------------------------------------------------------------------------------------

Like other locale subtags, the language can be added to the [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 object via the locale string, or a configuration object argument to the constructor.

### [Setting the language via the locale string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#setting_the_language_via_the_locale_string)

In order to be a valid Unicode locale identifier, a string must start with the language subtag. The main argument to the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor must be a valid Unicode locale identifier, so whenever the constructor is used, it must be passed an identifier with a language subtag.

### [Overriding language via the configuration object argument](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#overriding_language_via_the_configuration_object_argument)

While the language subtag must be specified, the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor has an optional configuration object argument, which can override the language subtag.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-Intl.Locale.prototype.language](https://tc39.es/ecma402/#sec-Intl.Locale.prototype.language) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
    
*   [Unicode language subtag](https://www.unicode.org/reports/tr35/#unicode_language_subtag_validity "External link (opens in new tab)")
     in the Unicode locale data markup language spec

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/language/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/locale/language/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/locale/language (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2Flanguage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Flanguage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2Flanguage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Flanguage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
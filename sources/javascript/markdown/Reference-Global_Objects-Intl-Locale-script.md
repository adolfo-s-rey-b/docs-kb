*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#mdn-search)
    

Intl.Locale.prototype.script
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`script`** accessor property of [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instances returns the script used for writing the particular language used in this locale.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#description)

-------------------------------------------------------------------------------------------------------------------------------

Script, sometimes called writing system, is one of the core attributes of a locale. It indicates the set of symbols, or glyphs, that are used to write a particular language. For instance, the script associated with English is Latin, whereas the script typically associated with Korean is Hangul. In many cases, denoting a script is not strictly necessary, since the language (which is necessary) is only written in a single script. There are exceptions to this rule, however, and it is important to indicate the script when multiple scripts are applicable.

The `script` property's value is set at construction time, either through the part of the locale identifier after `language` or through the `script` option of the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor. The latter takes priority if they are both present; and if neither is present, the property has value `undefined`.

The set accessor of `script` is `undefined`. You cannot change this property directly.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#examples)

-------------------------------------------------------------------------------------------------------------------------

Like other locale subtags, the script can be added to the [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 object via the locale string, or a configuration object argument to the constructor.

### [Adding a script via the locale string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#adding_a_script_via_the_locale_string)

The script, if present, is the second part of a valid Unicode language identifier string, and can be added to the initial locale identifier string that is passed into the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor. Note that the script is not a required part of a locale identifier.

js

    const locale = new Intl.Locale("en-Latn-US");
    console.log(locale.script); // "Latn"
    

### [Adding a script via the configuration object argument](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#adding_a_script_via_the_configuration_object_argument)

The [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor has an optional configuration object argument. Set the `script` property of the configuration object to your desired script, and then pass it into the constructor.

js

    const locale = new Intl.Locale("fr-FR", { script: "Latn" });
    console.log(locale.script); // "Latn"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-Intl.Locale.prototype.script](https://tc39.es/ecma402/#sec-Intl.Locale.prototype.script) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
    
*   [Unicode script subtag](https://www.unicode.org/reports/tr35/#unicode_script_subtag_validity "External link (opens in new tab)")
     in the Unicode locale data markup language spec

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 22, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/script/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/locale/script/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/locale/script (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2Fscript&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Fscript%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2Fscript%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Fscript%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe509776556a47f12843b91ab5c6e9be6585698c6%0A*+Document+last+modified%3A+2025-07-22T12%3A08%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
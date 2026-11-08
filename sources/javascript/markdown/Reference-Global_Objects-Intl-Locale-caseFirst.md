*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#mdn-search)
    

Intl.Locale.prototype.caseFirst
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`caseFirst`** accessor property of [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instances returns whether case is taken into account for this locale's collation rules.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#description)

----------------------------------------------------------------------------------------------------------------------------------

A locale's collation rules are used to determine how strings are ordered in that locale. Certain locales use a character's case (UPPERCASE or lowercase) in the collation process. This additional rule can be expressed in an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 object's `caseFirst` property. There are 3 values that the `caseFirst` property can have, outlined in the table below.

| Value | Description |
| --- | --- |
| `upper` | Upper case to be sorted before lower case. |
| `lower` | Lower case to be sorted before upper case. |
| `false` | No special case ordering. |

The `caseFirst` property's value is set at construction time, either through the `kf` key of the locale identifier or through the `caseFirst` option of the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor. The latter takes priority if they are both present; and if neither is present, the property has value `undefined`.

The set accessor of `caseFirst` is `undefined`. You cannot change this property directly.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#examples)

----------------------------------------------------------------------------------------------------------------------------

Like other locale subtags, the `caseFirst` value can be added to the [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 object via the locale string, or a configuration object argument to the constructor.

### [Adding a caseFirst value via the locale string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#adding_a_casefirst_value_via_the_locale_string)

In the [Unicode locale string spec](https://www.unicode.org/reports/tr35/ "External link (opens in new tab)")
, `caseFirst` is an "extension subtag". These subtags add additional data about the locale, and are added to locale identifiers using the `-u` extension key. To add the `caseFirst` value to the initial locale identifier string passed into the [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor, first add the `-u` extension key if it doesn't exist. Next, add the `-kf` extension to indicate that you are adding a value for `caseFirst`. Finally, add the `caseFirst` value.

js

    const locale = new Intl.Locale("fr-Latn-FR-u-kf-upper");
    console.log(locale.caseFirst); // "upper"
    

### [Adding a caseFirst value via the configuration object argument](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#adding_a_casefirst_value_via_the_configuration_object_argument)

The [`Intl.Locale()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale)
 constructor has an optional configuration object argument, which can contain any of several extension types, including `caseFirst`. Set the `caseFirst` property of the configuration object to your desired `caseFirst` value, and then pass it into the constructor.

js

    const locale = new Intl.Locale("en-Latn-US", { caseFirst: "lower" });
    console.log(locale.caseFirst); // "lower"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-Intl.Locale.prototype.caseFirst](https://tc39.es/ecma402/#sec-Intl.Locale.prototype.caseFirst) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
    
*   [Unicode case first collation spec](https://github.com/unicode-org/cldr/blob/main/common/bcp47/collation.xml#L49 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/caseFirst/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/locale/casefirst/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/locale/casefirst (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2FcaseFirst&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Fcasefirst%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FLocale%2FcaseFirst%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Flocale%2Fcasefirst%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#mdn-search)
    

Intl.DisplayNames
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.DisplayNames`** object enables the consistent translation of language, region and script display names.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#try_it)

--------------------------------------------------------------------------------------------------------------------

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#constructor)

------------------------------------------------------------------------------------------------------------------------------

[`Intl.DisplayNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames)

Creates a new `Intl.DisplayNames` object.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#static_methods)

------------------------------------------------------------------------------------------------------------------------------------

[`Intl.DisplayNames.supportedLocalesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/supportedLocalesOf)

Returns an array containing those of the provided locales that are supported without having to fall back to the runtime's default locale.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#instance_properties)

----------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Intl.DisplayNames.prototype` and shared by all `Intl.DisplayNames` instances.

[`Intl.DisplayNames.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Intl.DisplayNames` instances, the initial value is the [`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/DisplayNames)
 constructor.

[`Intl.DisplayNames.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#intl.displaynames.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Intl.DisplayNames"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#instance_methods)

----------------------------------------------------------------------------------------------------------------------------------------

[`Intl.DisplayNames.prototype.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/of)

This method receives a `code` and returns a string based on the locale and options provided when instantiating `Intl.DisplayNames`.

[`Intl.DisplayNames.prototype.resolvedOptions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/resolvedOptions)

Returns a new object with properties reflecting the locale and formatting options computed during initialization of the object.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#examples)

------------------------------------------------------------------------------------------------------------------------

### [Region Code Display Names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#region_code_display_names)

To create an `Intl.DisplayNames` for a locale and get the display name for a region code.

### [Language Display Names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#language_display_names)

To create an `Intl.DisplayNames` for a locale and get the display name for a language-script-region sequence.

### [Script Code Display Names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#script_code_display_names)

To create an `Intl.DisplayNames` for a locale and get the display name for a script code.

### [Currency Code Display Names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#currency_code_display_names)

To create an `Intl.DisplayNames` for a locale and get the display name for currency code.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#specifications)

------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# intl-displaynames-objects](https://tc39.es/ecma402/#intl-displaynames-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Intl.DisplayNames` in FormatJS](https://formatjs.github.io/docs/polyfills/intl-displaynames/ "External link (opens in new tab)")
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/displaynames/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/displaynames (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDisplayNames%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdisplaynames%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#mdn-search)
    

String.prototype.toLocaleUpperCase()
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`toLocaleUpperCase()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns this string converted to upper case, according to any locale-specific case mappings.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#try_it)

---------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#syntax)

---------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#parameters)

[`locales` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
, or an array of such strings. Indicates the locale to be used to convert to upper case according to any locale-specific case mappings. For the general form and interpretation of the `locales` argument, see [the parameter description on the `Intl` main page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)
.

Unlike other methods that use the `locales` argument, `toLocaleUpperCase()` does not allow locale matching. Therefore, after checking the validity of the `locales` argument, `toLocaleUpperCase()` always uses the first locale in the list (or the default locale if the list is empty), even if this locale is not supported by the implementation.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#return_value)

A new string representing the calling string converted to upper case, according to any locale-specific case mappings.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#description)

-------------------------------------------------------------------------------------------------------------------------------------

The `toLocaleUpperCase()` method returns the value of the string converted to upper case according to any locale-specific case mappings. `toLocaleUpperCase()` does not affect the value of the string itself. In most cases, this will produce the same result as [`toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
, but for some locales, such as Turkish, whose case mappings do not follow the default case mappings in Unicode, there may be a different result.

Also notice that conversion is not necessarily a 1:1 character mapping, as some characters might result in two (or even more) characters when transformed to upper-case. Therefore the length of the result string can differ from the input length. This also implies that the conversion is not stable, so for example the following can return `false`: `x.toLocaleLowerCase() === x.toLocaleUpperCase().toLocaleLowerCase()`

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#examples)

-------------------------------------------------------------------------------------------------------------------------------

### [Using toLocaleUpperCase()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#using_tolocaleuppercase)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.tolocaleuppercase](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.tolocaleuppercase) |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sup-string.prototype.tolocaleuppercase](https://tc39.es/ecma402/#sup-string.prototype.tolocaleuppercase) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [`String.prototype.toLocaleLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleLowerCase)
    
*   [`String.prototype.toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
    
*   [`String.prototype.toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/tolocaleuppercase/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/tolocaleuppercase (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FtoLocaleUpperCase&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ftolocaleuppercase%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FtoLocaleUpperCase%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ftolocaleuppercase%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
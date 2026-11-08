*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#mdn-search)
    

String.prototype.localeCompare()
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`localeCompare()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns a number indicating whether this string comes before, or after, or is the same as the given string in sort order. In implementations with [`Intl.Collator` API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
 support, this method delegates to `Intl.Collator`.

When comparing large numbers of strings, such as in sorting large arrays, it is better to create an [`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
 object and use the function provided by its [`compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/compare)
 method.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#try_it)

-----------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#syntax)

-----------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#parameters)

The `locales` and `options` parameters customize the behavior of the function and let applications specify the language whose formatting conventions should be used.

In implementations that support the [`Intl.Collator` API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
, these parameters correspond exactly to the [`Intl.Collator()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator)
 constructor's parameters. Implementations without `Intl.Collator` support are asked to ignore both parameters, making the comparison result returned entirely implementation-dependent — it's only required to be _consistent_.

[`compareString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#comparestring)

The string against which the `referenceStr` is compared. All values are [coerced to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
, so omitting it or passing `undefined` causes `localeCompare()` to compare against the string `"undefined"`, which is rarely what you want.

[`locales` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
, or an array of such strings. Corresponds to the [`locales`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator#locales)
 parameter of the `Intl.Collator()` constructor.

In implementations without `Intl.Collator` support, this parameter is ignored and the host's locale is usually used.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#options)

An object adjusting the output format. Corresponds to the [`options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator#options)
 parameter of the `Intl.Collator()` constructor.

In implementations without `Intl.Collator` support, this parameter is ignored.

See the [`Intl.Collator()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator)
 for details on the `locales` and `options` parameters and how to use them.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#return_value)

A **negative** number if `referenceStr` occurs before `compareString`; **positive** if the `referenceStr` occurs after `compareString`; `0` if they are equivalent.

In implementations with `Intl.Collator`, this is equivalent to `new Intl.Collator(locales, options).compare(referenceStr, compareString)`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#description)

---------------------------------------------------------------------------------------------------------------------------------

Returns an integer indicating whether the `referenceStr` comes before, after or is equivalent to the `compareString`.

*   Negative when the `referenceStr` occurs before `compareString`
*   Positive when the `referenceStr` occurs after `compareString`
*   Returns `0` if they are equivalent

**Warning:** Do not rely on exact return values of `-1` or `1`!

Negative and positive integer results vary between browsers (as well as between browser versions) because the ECMAScript specification only mandates negative and positive values. Some browsers may return `-2` or `2`, or even some other negative or positive value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Using localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#using_localecompare)

### [Sort an array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#sort_an_array)

`localeCompare()` enables case-insensitive sorting for an array.

### [Check browser support for extended arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#check_browser_support_for_extended_arguments)

The `locales` and `options` arguments are not supported in all browsers yet.

To check whether an implementation supports them, use the `"i"` argument (a requirement that illegal language tags are rejected) and look for a [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 exception:

### [Using locales](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#using_locales)

The results provided by `localeCompare()` vary between languages. In order to get the sort order of the language used in the user interface of your application, make sure to specify that language (and possibly some fallback languages) using the `locales` argument:

### [Using options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#using_options)

The results provided by `localeCompare()` can be customized using the `options` argument:

### [Numeric sorting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#numeric_sorting)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.localecompare](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.localecompare) |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sup-String.prototype.localeCompare](https://tc39.es/ecma402/#sup-String.prototype.localeCompare) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/localecompare/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/localecompare (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FlocaleCompare&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Flocalecompare%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FlocaleCompare%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Flocalecompare%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
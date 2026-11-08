*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#mdn-search)
    

RegExp.$1, …, RegExp.$9
=======================

Deprecated

Avoid using this feature in new projects. The `RegExp` static properties may have unintended side effects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** All `RegExp` static properties that expose the last match state globally are deprecated. See [deprecated RegExp features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
 for more information.

The **`RegExp.$1, …, RegExp.$9`** static accessor properties return parenthesized substring matches.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#description)

---------------------------------------------------------------------------------------------------------------------

Because `$1`–`$9` are static properties of [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
, you always use them as `RegExp.$1`, `RegExp.$2`, etc., rather than as properties of a `RegExp` object you created.

The values of `$1, …, $9` update whenever a `RegExp` (but not a `RegExp` subclass) instance makes a successful match. If no matches have been made, or if the last match does not have the corresponding capturing group, the respective property is an empty string. The set accessor of each property is `undefined`, so you cannot change the properties directly.

The number of possible parenthesized substrings is unlimited, but the `RegExp` object can only hold the first nine. You can access all parenthesized substrings through the returned array's indexes.

`$1, …, $9` can also be used in the replacement string of [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
, but that's unrelated to the `RegExp.$n` legacy properties.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#examples)

---------------------------------------------------------------------------------------------------------------

### [Using $n with RegExp.prototype.test()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#using_n_with_regexp.prototype.test)

The following script uses the [`RegExp.prototype.test()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)
 method to grab a number in a generic string.

Please note that any operation involving the usage of other regular expressions between a `re.test(str)` call and the `RegExp.$n` property, might have side effects, so that accessing these special properties should be done instantly, otherwise the result might be unexpected.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Legacy RegExp features  <br>\# additional-properties-of-the-regexp-constructor](https://github.com/tc39/proposal-regexp-legacy-features/#additional-properties-of-the-regexp-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`RegExp.input` (`$_`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/input)
    
*   [`RegExp.lastMatch` (`$&`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastMatch)
    
*   [`RegExp.lastParen` (`$+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastParen)
    
*   [`RegExp.leftContext` (`` $` ``)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/leftContext)
    
*   [`RegExp.rightContext` (`$'`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/rightContext)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/regexp/n/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/regexp/n (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp%2Fn&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%2Fn%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp%2Fn%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%2Fn%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
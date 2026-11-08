*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#mdn-search)
    

String.prototype.normalize()
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`normalize()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns the Unicode Normalization Form of this string.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#try_it)

-------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#syntax)

-------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#parameters)

[`form` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#form)

One of `"NFC"`, `"NFD"`, `"NFKC"`, or `"NFKD"`, specifying the Unicode Normalization Form. If omitted or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
, `"NFC"` is used.

These values have the following meanings:

[`"NFC"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#nfc)

Canonical Decomposition, followed by Canonical Composition.

[`"NFD"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#nfd)

Canonical Decomposition.

[`"NFKC"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#nfkc)

Compatibility Decomposition, followed by Canonical Composition.

[`"NFKD"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#nfkd)

Compatibility Decomposition.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#return_value)

A string containing the Unicode Normalization Form of the given string.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `form` isn't one of the values specified above.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#description)

-----------------------------------------------------------------------------------------------------------------------------

Unicode assigns a unique numerical value, called a _code point_, to each character. For example, the code point for `"A"` is given as U+0041. However, sometimes more than one code point, or sequence of code points, can represent the same abstract character — the character `"ñ"` for example can be represented by either of:

*   The single code point U+00F1.
*   The code point for `"n"` (U+006E) followed by the code point for the combining tilde (U+0303).

However, since the code points are different, string comparison will not treat them as equal. And since the number of code points in each version is different, they even have different lengths.

The `normalize()` method helps solve this problem by converting a string into a normalized form common for all sequences of code points that represent the same characters. There are two main normalization forms, one based on **canonical equivalence** and the other based on **compatibility**.

### [Canonical equivalence normalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#canonical_equivalence_normalization)

In Unicode, two sequences of code points have canonical equivalence if they represent the same abstract characters, and should always have the same visual appearance and behavior (for example, they should always be sorted in the same way).

You can use `normalize()` using the `"NFD"` or `"NFC"` arguments to produce a form of the string that will be the same for all canonically equivalent strings. In the example below we normalize two representations of the character `"ñ"`:

#### Composed and decomposed forms

Note that the length of the normalized form under `"NFD"` is `2`. That's because `"NFD"` gives you the **decomposed** version of the canonical form, in which single code points are split into multiple combining ones. The decomposed canonical form for `"ñ"` is `"\u006E\u0303"`.

You can specify `"NFC"` to get the **composed** canonical form, in which multiple code points are replaced with single code points where possible. The composed canonical form for `"ñ"` is `"\u00F1"`:

### [Compatibility normalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#compatibility_normalization)

In Unicode, two sequences of code points are compatible if they represent the same abstract characters, and should be treated alike in some — but not necessarily all — applications.

All canonically equivalent sequences are also compatible, but not vice versa.

For example:

*   the code point U+FB00 represents the [ligature](https://developer.mozilla.org/en-US/docs/Glossary/Ligature)
     `"ﬀ"`. It is compatible with two consecutive U+0066 code points (`"ff"`).
*   the code point U+24B9 represents the symbol `"Ⓓ"`. It is compatible with the U+0044 code point (`"D"`).

In some respects (such as sorting) they should be treated as equivalent—and in some (such as visual appearance) they should not, so they are not canonically equivalent.

You can use `normalize()` using the `"NFKD"` or `"NFKC"` arguments to produce a form of the string that will be the same for all compatible strings:

When applying compatibility normalization it's important to consider what you intend to do with the strings, since the normalized form may not be appropriate for all applications. In the example above the normalization is appropriate for search, because it enables a user to find the string by searching for `"f"`. But it may not be appropriate for display, because the visual representation is different.

As with canonical normalization, you can ask for decomposed or composed compatible forms by passing `"NFKD"` or `"NFKC"`, respectively.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using normalize()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#using_normalize)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.normalize](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.normalize) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Unicode Standard Annex #15, Unicode Normalization Forms](https://www.unicode.org/reports/tr15/ "External link (opens in new tab)")
    
*   [Unicode equivalence](https://en.wikipedia.org/wiki/Unicode_equivalence "External link (opens in new tab)")
     on Wikipedia

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/normalize/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/normalize (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fnormalize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fnormalize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fnormalize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fnormalize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#mdn-search)
    

encodeURI()
===========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`encodeURI()`** function encodes a [URI](https://developer.mozilla.org/en-US/docs/Glossary/URI)
 by replacing each instance of certain characters by one, two, three, or four escape sequences representing the [UTF-8](https://developer.mozilla.org/en-US/docs/Glossary/UTF-8)
 encoding of the character (will only be four escape sequences for characters composed of two surrogate characters). Compared to [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
, this function encodes fewer characters, preserving those that are part of the URI syntax.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#syntax)

------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#parameters)

[`uri`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#uri)

A string to be encoded as a URI.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#return_value)

A new string representing the provided string encoded as a URI.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#exceptions)

[`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)

Thrown if `uri` contains a [lone surrogate](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#description)

----------------------------------------------------------------------------------------------------------------------

`encodeURI()` is a function property of the global object.

The `encodeURI()` function escapes characters by UTF-8 code units, with each octet encoded in the format `%XX`, left-padded with 0 if necessary. Because lone surrogates in UTF-16 do not encode any valid Unicode character, they cause `encodeURI()` to throw a [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
.

`encodeURI()` escapes all characters **except**:

A–Z a–z 0–9 - \_ . ! ~ \* ' ( )

; / ? : @ & = + $ , #

The characters on the second line are characters that may be part of the URI syntax, and are only escaped by `encodeURIComponent()`. Both `encodeURI()` and `encodeURIComponent()` do not encode the characters `-.!~*'()`, known as "unreserved marks", which do not have a reserved purpose but are allowed in a URI "as is". (See [RFC2396](https://datatracker.ietf.org/doc/html/rfc2396 "External link (opens in new tab)")
)

The `encodeURI()` function does not encode characters that have special meaning (reserved characters) for a URI. The following example shows all the parts that a URI can possibly contain. Note how certain characters are used to signify special meaning:

`encodeURI`, as the name implies, is used to encode a URL as a whole, assuming it is already well-formed. If you want to dynamically assemble string values into a URL, you probably want to use [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
 on each dynamic segment instead, to avoid URL syntax characters in unwanted places.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#examples)

----------------------------------------------------------------------------------------------------------------

### [encodeURI() vs. encodeURIComponent()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#encodeuri_vs._encodeuricomponent)

`encodeURI()` differs from [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
 as follows:

### [Encoding a lone surrogate throws](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#encoding_a_lone_surrogate_throws)

A [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
 will be thrown if one attempts to encode a surrogate which is not part of a high-low pair. For example:

You can use [`String.prototype.toWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toWellFormed)
, which replaces lone surrogates with the Unicode replacement character (U+FFFD), to avoid this error. You can also use [`String.prototype.isWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/isWellFormed)
 to check if a string contains lone surrogates before passing it to `encodeURI()`.

### [Encoding for RFC3986](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#encoding_for_rfc3986)

The more recent [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986 "External link (opens in new tab)")
 makes square brackets reserved (for [IPv6](https://developer.mozilla.org/en-US/docs/Glossary/IPv6)
) and thus not encoded when forming something which could be part of a URL (such as a host). It also reserves !, ', (, ), and \*, even though these characters have no formalized URI delimiting uses. The following function encodes a string for RFC3986-compliant URL format.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-encodeuri-uri](https://tc39.es/ecma262/multipage/global-object.html#sec-encodeuri-uri) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`decodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
    
*   [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
    
*   [`decodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/encodeuri/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/encodeuri (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FencodeURI&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fencodeuri%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FencodeURI%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fencodeuri%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d4628c5144f459ddb081a3e58d0e56f0c2db673%0A*+Document+last+modified%3A+2026-09-02T02%3A16%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#mdn-search)
    

encodeURIComponent()
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`encodeURIComponent()`** function encodes a [URI](https://developer.mozilla.org/en-US/docs/Glossary/URI)
 by replacing each instance of certain characters by one, two, three, or four escape sequences representing the [UTF-8](https://developer.mozilla.org/en-US/docs/Glossary/UTF-8)
 encoding of the character (will only be four escape sequences for characters composed of two surrogate characters). Compared to [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
, this function encodes more characters, including those that are part of the URI syntax.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#try_it)

---------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#syntax)

---------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#parameters)

[`uriComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#uricomponent)

A string to be encoded as a URI component (a path, query string, fragment, etc.). Other values are [converted to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#return_value)

A new string representing the provided `uriComponent` encoded as a URI component.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#exceptions)

[`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)

Thrown if `uriComponent` contains a [lone surrogate](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#description)

-------------------------------------------------------------------------------------------------------------------------------

`encodeURIComponent()` is a function property of the global object.

`encodeURIComponent()` uses the same encoding algorithm as described in [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
. It escapes all characters **except**:

A–Z a–z 0–9 - \_ . ! ~ \* ' ( )

Compared to [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
, `encodeURIComponent()` escapes a larger set of characters. Use `encodeURIComponent()` on user-entered fields from forms sent to the server — this will encode `&` symbols that may inadvertently be generated during data entry for [character references](https://developer.mozilla.org/en-US/docs/Glossary/Character_reference)
 or other characters that require encoding/decoding. For example, if a user writes `Jack & Jill`, without `encodeURIComponent()`, the ampersand could be interpreted on the server as the start of a new field and jeopardize the integrity of the data.

For [`application/x-www-form-urlencoded`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#application/x-www-form-urlencoded-encoding-algorithm "External link (opens in new tab)")
, spaces are to be replaced by `+`, so one may wish to follow an `encodeURIComponent()` replacement with an additional replacement of `%20` with `+`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Encoding for Content-Disposition and Link headers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#encoding_for_content-disposition_and_link_headers)

The following example provides the special encoding required within UTF-8 [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Disposition)
 and [`Link`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link)
 server response header parameters (e.g., UTF-8 filenames):

### [Encoding for RFC3986](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#encoding_for_rfc3986)

The more recent [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986 "External link (opens in new tab)")
 reserves `!`, `'`, `(`, `)`, and `*`, even though these characters have no formalized URI delimiting uses. The following function encodes a string for RFC3986-compliant URL component format. It also encodes `[` and `]`, which are part of the [IPv6](https://developer.mozilla.org/en-US/docs/Glossary/IPv6)
 URI syntax. An RFC3986-compliant `encodeURI` implementation should not escape them, which is demonstrated in the [`encodeURI()` example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI#encoding_for_rfc3986)
.

### [Encoding a lone surrogate throws](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#encoding_a_lone_surrogate_throws)

A [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
 will be thrown if one attempts to encode a surrogate which is not part of a high-low pair. For example:

You can use [`String.prototype.toWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toWellFormed)
, which replaces lone surrogates with the Unicode replacement character (U+FFFD), to avoid this error. You can also use [`String.prototype.isWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/isWellFormed)
 to check if a string contains lone surrogates before passing it to `encodeURIComponent()`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-encodeuricomponent-uricomponent](https://tc39.es/ecma262/multipage/global-object.html#sec-encodeuricomponent-uricomponent) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`decodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
    
*   [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
    
*   [`decodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/encodeuricomponent/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/encodeuricomponent (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FencodeURIComponent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fencodeuricomponent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FencodeURIComponent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fencodeuricomponent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
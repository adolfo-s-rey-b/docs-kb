*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#mdn-search)
    

Uint8Array.fromBase64()
=======================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Uint8Array.fromBase64()`** static method creates a new [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
 object from a [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64)
\-encoded string.

This method should be preferred over [`Window.atob()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/atob)
 because it results in a byte array, which is easier to work with than a string containing raw bytes, unless your decoded binary data is actually intended to be ASCII text. If you already have an array buffer allocated and you want to populate it, use the instance method [`Uint8Array.prototype.setFromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64)
 instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#syntax)

------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#parameters)

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#string)

A base64 string encoding bytes to convert to a `Uint8Array`. The string must only contain characters in the base64 alphabet, which includes A–Z, a–z, 0–9, and two special characters, which are either `+` and `/` (if using `alphabet: "base64"` in `options`) or `-` and `_` (if using `alphabet: "base64url"` in `options`). It may have padding `=` characters at the end. Any ASCII white space characters within the string are ignored.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#options)

An object customizing the base64 string interpretation process. It can contain the following properties:

[`alphabet` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#alphabet)

A string specifying the base64 alphabet to use. It can be one of the following:

[`"base64"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#base64)

Accept input encoded with the standard base64 alphabet, which uses `+` and `/`.

[`"base64url"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#base64url)

Accept input encoded with the URL-safe base64 alphabet, which uses `-` and `_`.

[`lastChunkHandling` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#lastchunkhandling)

A string specifying how to handle the last chunk of the base64 string. Because every 4 characters in base64 encodes 3 bytes, the string is separated into chunks of 4 characters. If the last chunk has fewer than 4 characters, it needs to be handled differently. It can be one of the following:

[`"loose"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#loose)

The last chunk can either be 2 or 3 base64 characters, or exactly 4 characters long with padding `=` characters. The last chunk is decoded and appended to the result.

[`"strict"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#strict)

The last chunk must be exactly 4 characters long with padding `=` characters. Furthermore, [overflow bits](https://developer.mozilla.org/en-US/docs/Glossary/Base64#last_chunk)
 (trailing bits from the last base64 character that don't represent any data) must be 0. The last chunk is decoded and appended to the result.

[`"stop-before-partial"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#stop-before-partial)

If the last chunk is exactly 4 characters long with padding `=` characters, then it's decoded and appended to the result. Otherwise, the last partial chunk is ignored (but if it contains one base64 character followed by `=`, then a syntax error is still thrown). This is useful if the string is coming from a stream and the last chunk is not yet complete. To know how many characters of the input were read, use [`Uint8Array.prototype.setFromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64)
 instead (the linked page also contains an example of stream decoding using `"stop-before-partial"`).

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#return_value)

A new `Uint8Array` object containing the decoded bytes from the base64-encoded string.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the input string contains characters outside the specified alphabet, or if the last chunk does not satisfy the `lastChunkHandling` option.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   The input string is not a string.
*   The `options` object is not an object or `undefined`.
*   The options are not of the expected values or `undefined`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Decoding a base64 string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#decoding_a_base64_string)

This example uses the default `alphabet` and `lastChunkHandling` options to decode a base64 string. Note that:

*   The whitespace in the space is ignored.
*   The string has 14 base64 characters, not a multiple of 4. This is only valid and decodable with `lastChunkHandling: "loose"`.
*   The last chunk, `Ph`, ends in the character `h` which is `0b100001` in base64, so the last `0001` bits are "overflow bits" and are ignored. This is only valid and decodable with `lastChunkHandling: "loose"`.

### [Decoding a URL-safe base64 string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#decoding_a_url-safe_base64_string)

This example uses the `alphabet` option to decode a URL-safe base64 string.

### [Decoding a base64 string with strict last chunk handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#decoding_a_base64_string_with_strict_last_chunk_handling)

This example uses the `lastChunkHandling` option to decode a base64 string, where the last chunk must be exactly 4 characters long with padding `=` characters, and the overflow bits must be 0.

### [Decoding a base64 string with partial last chunk handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#decoding_a_base64_string_with_partial_last_chunk_handling)

This example uses the `lastChunkHandling` option to decode a base64 string, ignoring any partial last chunk.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-uint8array.frombase64](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-uint8array.frombase64) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Uint8Array.fromBase64` in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [es-shims polyfill of `Uint8Array.fromBase64`](https://www.npmjs.com/package/es-arraybuffer-base64 "External link (opens in new tab)")
    
*   [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
    
*   [`Uint8Array.prototype.setFromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64)
    
*   [`Uint8Array.prototype.toBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/toBase64)
    
*   [`Window.atob()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/atob)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/uint8array/frombase64/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/uint8array/frombase64 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FfromBase64&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Ffrombase64%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FfromBase64%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Ffrombase64%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
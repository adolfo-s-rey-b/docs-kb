*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#mdn-search)
    

Uint8Array.prototype.setFromBase64()
====================================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`setFromBase64()`** method of [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
 instances populates this `Uint8Array` object with bytes from a [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64)
\-encoded string, returning an object indicating how many bytes were read and written.

This method is most suitable for populating a pre-allocated array buffer. If you just want to create a new `Uint8Array` object from a base64-encoded string, use the static method [`Uint8Array.fromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64)
 instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#syntax)

---------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#parameters)

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#string)

A base64 string encoding bytes to write into a `Uint8Array`. It has the same requirements as the [`string` parameter of `Uint8Array.fromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#string)
. Note that the string is only read up to the point where the array is filled, so any invalid base64 syntax after that point is ignored.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#options)

An object customizing the base64 string interpretation process. It has the same requirements as the [`options` parameter of `Uint8Array.fromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64#options)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#return_value)

An object containing the following properties:

[`read`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#read)

The number of base64 characters read from the input string. If the decoded data fits into the array, this is the length of the input string (including padding); otherwise, it is the length up to the last complete 4-character chunk that fits into the array. Chunks will never be split (because the remaining bits cannot be partially "put back" into the base64 without completely re-encoding it); if the next chunk cannot fit into the remainder of the array, it will be entirely unread, resulting in the last one or two bytes of the array not being written.

[`written`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#written)

The number of bytes written to the `Uint8Array`. Will never be greater than this `Uint8Array`'s [`byteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/byteLength)
.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the input string contains characters outside the specified alphabet, or if the last chunk does not satisfy the `lastChunkHandling` option.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   The input string is not a string.
*   The `options` object is not an object or `undefined`.
*   The options are not of the expected values or `undefined`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#examples)

-------------------------------------------------------------------------------------------------------------------------------

### [Decoding a base64 string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#decoding_a_base64_string)

This example uses the default `alphabet` and `lastChunkHandling` options to decode a base64 string into an existing `Uint8Array`.

### [Decoding a big string into a small array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#decoding_a_big_string_into_a_small_array)

If the string contains more data than the array can hold, the method will only write as many bytes as the array can hold, without discarding any bits.

Note how the last two bytes of the array are not written. To decode these two bytes, we need to read at least three more base64 characters, which represent 18 bits. These can't fit into the remaining two bytes of the array, so we can only write 2 chunks, or 6 bytes.

### [Setting data at a specific offset](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#setting_data_at_a_specific_offset)

The `setFromBase64()` method always starts writing at the beginning of the `Uint8Array`. If you want to write to the middle of the array, you can write to a [`TypedArray.prototype.subarray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/subarray)
 instead.

### [Stream decoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#stream_decoding)

This example is adapted from the [original proposal](https://github.com/tc39/proposal-arraybuffer-base64/blob/main/stream.mjs "External link (opens in new tab)")
. It mimics the [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)
 API with the `stream` option. Note the use of `lastChunkHandling: "stop-before-partial"` to handle incomplete chunks.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-uint8array.prototype.setfrombase64](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-uint8array.prototype.setfrombase64) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Uint8Array.prototype.setFromBase64` in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [es-shims polyfill of `Uint8Array.prototype.setFromBase64`](https://www.npmjs.com/package/es-arraybuffer-base64 "External link (opens in new tab)")
    
*   [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
    
*   [`Uint8Array.fromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromBase64)
    
*   [`Uint8Array.prototype.toBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/toBase64)
    
*   [`Window.atob()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/atob)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/uint8array/setfrombase64/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/uint8array/setfrombase64 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FsetFromBase64&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Fsetfrombase64%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FsetFromBase64%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Fsetfrombase64%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
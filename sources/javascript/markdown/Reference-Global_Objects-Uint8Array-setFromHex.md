*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#mdn-search)
    

Uint8Array.prototype.setFromHex()
=================================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`setFromHex()`** method of [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
 instances populates this `Uint8Array` object with bytes from a hex-encoded string, returning an object indicating how many bytes were read and written.

This method parses the string into a byte array. To convert the string into a single number, use the [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
 function with `radix` set to `16` instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#syntax)

------------------------------------------------------------------------------------------------------------------------

js

    setFromHex(string)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#parameters)

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#string)

A hexadecimal string encoding bytes to write into a `Uint8Array`. The string must:

*   Have an even number of characters because two characters encode one byte.
*   Only contain characters in the hexadecimal alphabet, which includes 0–9 and A–F (case-insensitive).
*   Not contain whitespace (unlike [`Uint8Array.prototype.setFromBase64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromBase64)
    ).

Note that the string is only read up to the point where the array is filled, so any invalid hex syntax after that point is ignored.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#return_value)

An object containing the following properties:

[`read`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#read)

The number of hex characters read from the input string. If the decoded data fits into the array, it is the length of the input string: otherwise, it is the number of complete hex characters that fit into the array.

[`written`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#written)

The number of bytes written to the `Uint8Array`. Will never be greater than this `Uint8Array`'s [`byteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/byteLength)
.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the input string contains characters outside the hex alphabet, or its length is odd.

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if the input string is not a string.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Decoding a hexadecimal string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#decoding_a_hexadecimal_string)

This example decodes a hexadecimal string into an existing `Uint8Array`.

js

    const uint8Array = new Uint8Array(8);
    const result = uint8Array.setFromHex("cafed00d");
    console.log(result); // { read: 8, written: 4 }
    console.log(uint8Array); // Uint8Array(8) [202, 254, 208, 13, 0, 0, 0, 0]
    

### [Decoding a big string into a small array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#decoding_a_big_string_into_a_small_array)

If the string contains more data than the array can hold, the method will only write as many bytes as the array can hold.

js

    const uint8Array = new Uint8Array(4);
    const result = uint8Array.setFromHex("cafed00d-some random stuff");
    console.log(result); // { read: 8, written: 4 }
    console.log(uint8Array); // Uint8Array(4) [202, 254, 208, 13]
    

Excess characters are ignored, even if they are invalid. However the total length of the input string must be even.

### [Setting data at a specific offset](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#setting_data_at_a_specific_offset)

The `setFromHex()` method always starts writing at the beginning of the `Uint8Array`. If you want to write to the middle of the array, you can write to a [`TypedArray.prototype.subarray()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/subarray)
 instead.

js

    const uint8Array = new Uint8Array(8);
    // Start writing at offset 2
    const result = uint8Array.subarray(2).setFromHex("cafed00d");
    console.log(result); // { read: 8, written: 4 }
    console.log(uint8Array);
    // Uint8Array(8) [0, 0, 202, 254, 208, 13, 0, 0]
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-uint8array.prototype.setfromhex](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-uint8array.prototype.setfromhex) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Uint8Array.prototype.setFromHex` in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [es-shims polyfill of `Uint8Array.prototype.setFromHex`](https://www.npmjs.com/package/es-arraybuffer-base64 "External link (opens in new tab)")
    
*   [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)
    
*   [`Uint8Array.fromHex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/fromHex)
    
*   [`Uint8Array.prototype.toHex()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/toHex)
    
*   [`parseInt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array/setFromHex/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/uint8array/setfromhex/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/uint8array/setfromhex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FsetFromHex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Fsetfromhex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FUint8Array%2FsetFromHex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fuint8array%2Fsetfromhex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
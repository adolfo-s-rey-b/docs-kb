*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#mdn-search)
    

DataView
========

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`DataView`** view provides a low-level interface for reading and writing multiple number types in a binary [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
, without having to care about the platform's [endianness](https://developer.mozilla.org/en-US/docs/Glossary/Endianness)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#description)

---------------------------------------------------------------------------------------------------------------------

### [Endianness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#endianness)

Multi-byte number formats are represented in memory differently depending on machine architecture — see [Endianness](https://developer.mozilla.org/en-US/docs/Glossary/Endianness)
 for an explanation. `DataView` accessors provide explicit control of how data is accessed, regardless of the executing computer's endianness. For example, [WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)
 memory is always little-endian, so you should use `DataView` instead of typed arrays to read and write multi-byte values. See [`WebAssembly.Memory`](https://developer.mozilla.org/en-US/docs/WebAssembly/Reference/JavaScript_interface/Memory)
 for an example.

**Note:** `DataView` defaults to big-endian read and write, but most platforms use little-endian.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#constructor)

---------------------------------------------------------------------------------------------------------------------

[`DataView()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/DataView)

Creates a new `DataView` object.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#instance_properties)

-------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `DataView.prototype` and shared by all `DataView` instances.

[`DataView.prototype.buffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/buffer)

Returns the [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
 referenced by the `DataView`.

[`DataView.prototype.byteLength`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/byteLength)

Returns the length (in bytes) of the `DataView`.

[`DataView.prototype.byteOffset`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/byteOffset)

Returns the offset (in bytes) of the `DataView` from the start of its [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
.

[`DataView.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `DataView` instances, the initial value is the [`DataView`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/DataView)
 constructor.

[`DataView.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#dataview.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"DataView"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#instance_methods)

-------------------------------------------------------------------------------------------------------------------------------

[`DataView.prototype.getBigInt64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getBigInt64)

Reads 8 bytes starting at the specified byte offset of this `DataView` and interprets them as a 64-bit signed integer.

[`DataView.prototype.getBigUint64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getBigUint64)

Reads 8 bytes starting at the specified byte offset of this `DataView` and interprets them as a 64-bit unsigned integer.

[`DataView.prototype.getFloat16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getFloat16)

Reads 2 bytes starting at the specified byte offset of this `DataView` and interprets them as a 16-bit floating point number.

[`DataView.prototype.getFloat32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getFloat32)

Reads 4 bytes starting at the specified byte offset of this `DataView` and interprets them as a 32-bit floating point number.

[`DataView.prototype.getFloat64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getFloat64)

Reads 8 bytes starting at the specified byte offset of this `DataView` and interprets them as a 64-bit floating point number.

[`DataView.prototype.getInt16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt16)

Reads 2 bytes starting at the specified byte offset of this `DataView` and interprets them as a 16-bit signed integer.

[`DataView.prototype.getInt32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt32)

Reads 4 bytes starting at the specified byte offset of this `DataView` and interprets them as a 32-bit signed integer.

[`DataView.prototype.getInt8()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt8)

Reads 1 byte at the specified byte offset of this `DataView` and interprets it as an 8-bit signed integer.

[`DataView.prototype.getUint16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint16)

Reads 2 bytes starting at the specified byte offset of this `DataView` and interprets them as a 16-bit unsigned integer.

[`DataView.prototype.getUint32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint32)

Reads 4 bytes starting at the specified byte offset of this `DataView` and interprets them as a 32-bit unsigned integer.

[`DataView.prototype.getUint8()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint8)

Reads 1 byte at the specified byte offset of this `DataView` and interprets it as an 8-bit unsigned integer.

[`DataView.prototype.setBigInt64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setBigInt64)

Takes a BigInt and stores it as a 64-bit signed integer in the 8 bytes starting at the specified byte offset of this `DataView`.

[`DataView.prototype.setBigUint64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setBigUint64)

Takes a BigInt and stores it as a 64-bit unsigned integer in the 8 bytes starting at the specified byte offset of this `DataView`.

[`DataView.prototype.setFloat16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setFloat16)

Takes a number and stores it as a 16-bit float in the 2 bytes starting at the specified byte offset of this `DataView`.

[`DataView.prototype.setFloat32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setFloat32)

Takes a number and stores it as a 32-bit float in the 4 bytes starting at the specified byte offset of this `DataView`.

[`DataView.prototype.setFloat64()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setFloat64)

Takes a number and stores it as a 64-bit float in the 8 bytes starting at the specified byte offset of this `DataView`.

[`DataView.prototype.setInt16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt16)

Takes a number and stores it as a 16-bit signed integer in the 2 bytes at the specified byte offset of this `DataView`.

[`DataView.prototype.setInt32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt32)

Takes a number and stores it as a 32-bit signed integer in the 4 bytes at the specified byte offset of this `DataView`.

[`DataView.prototype.setInt8()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt8)

Takes a number and stores it as an 8-bit signed integer in the byte at the specified byte offset of this `DataView`.

[`DataView.prototype.setUint16()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint16)

Takes a number and stores it as a 16-bit unsigned integer in the 2 bytes at the specified byte offset of this `DataView`.

[`DataView.prototype.setUint32()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint32)

Takes a number and stores it as a 32-bit unsigned integer in the 4 bytes at the specified byte offset of this `DataView`.

[`DataView.prototype.setUint8()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint8)

Takes a number and stores it as an 8-bit unsigned integer in the byte at the specified byte offset of this `DataView`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#examples)

---------------------------------------------------------------------------------------------------------------

### [Using DataView](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#using_dataview)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-dataview-objects](https://tc39.es/ecma262/multipage/structured-data.html#sec-dataview-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Polyfill of `DataView` in `core-js`](https://core-js.io/docs/features/ecmascript/typed-arrays "External link (opens in new tab)")
    
*   [`ArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)
    
*   [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/dataview/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/dataview (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDataView&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdataview%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDataView%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdataview%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
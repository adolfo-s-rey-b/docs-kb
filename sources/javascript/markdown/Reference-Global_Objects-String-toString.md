*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#mdn-search)
    

String.prototype.toString()
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`toString()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns this string value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#try_it)

------------------------------------------------------------------------------------------------------------------

    const stringObj = new String("foo");
    
    console.log(stringObj);
    // Expected output: String { "foo" }
    
    console.log(stringObj.toString());
    // Expected output: "foo"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#syntax)

------------------------------------------------------------------------------------------------------------------

js

    toString()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#return_value)

A string representing the specified string value.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#description)

----------------------------------------------------------------------------------------------------------------------------

The [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 object overrides the `toString` method of [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
; it does not inherit [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
. For `String` values, the `toString` method returns the string itself (if it's a primitive) or the string that the `String` object wraps. It has the exact same implementation as [`String.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/valueOf)
.

The `toString()` method requires its `this` value to be a `String` primitive or wrapper object. It throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 for other `this` values without attempting to coerce them to string values.

Because `String` doesn't have a [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
 method, JavaScript calls the `toString()` method automatically when a `String` _object_ is used in a context expecting a string, such as in a [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
. However, string _primitive_ values do not consult the `toString()` method to be [coerced to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
 — since they are already strings, no conversion is performed.

js

    String.prototype.toString = () => "Overridden";
    console.log(`${"foo"}`); // "foo"
    console.log(`${new String("foo")}`); // "Overridden"
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using toString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#using_tostring)

The following example displays the string value of a [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 object:

js

    const x = new String("Hello world");
    
    console.log(x.toString()); // "Hello world"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.tostring](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.tostring) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`String.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/valueOf)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/tostring/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/tostring (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FtoString&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ftostring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2FtoString%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Ftostring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F06e6e54baef7032c4e81ca93291fde0a0585de8b%0A*+Document+last+modified%3A+2026-01-25T19%3A35%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
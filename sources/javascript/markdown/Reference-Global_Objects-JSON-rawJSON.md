*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#mdn-search)
    

JSON.rawJSON()
==============

Baseline 2025

Newly available

Since March 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`JSON.rawJSON()`** static method creates a "raw JSON" object containing a piece of JSON text. When serialized to JSON, the raw JSON object is treated as if it is already a piece of JSON. This text is required to be valid JSON.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#syntax)

---------------------------------------------------------------------------------------------------------------

js

    JSON.rawJSON(string)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#parameters)

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#string)

The JSON text. Must be valid JSON **representing a primitive value**.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#return_value)

An object that can be used to create JSON text with the exact same content as the `string` provided, without quotes around the string itself. This object [has `null` prototype](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#null-prototype_objects)
 and [is frozen](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
 (so it never gets accidentally serialized as a regular object by any kind of primitive conversion), and the following property:

[`rawJSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#rawjson)

The original JSON `string` provided.

Furthermore, it has a [private field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 that marks itself as a raw JSON object. This allows it to be identified by [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 and [`JSON.isRawJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/isRawJSON)
.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the `string` is not valid JSON, or if it represents an object or array.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#description)

-------------------------------------------------------------------------------------------------------------------------

A raw JSON object can be seen as an immutable, atomic data structure like any kind of [primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_values)
. It is not a regular object and it contains no data other than the raw JSON text. It is used to "pre-serialize" data to formats that `JSON.stringify` itself cannot produce for various reasons. The most typical use case is the floating point number loss of precision problem. For example:

js

    JSON.stringify({ value: 12345678901234567890 });
    // {"value":12345678901234567000}
    

The value is not exactly equivalent to the original number any more! This is because JavaScript uses floating point representation for all numbers, so it cannot represent all integers exactly. The number literal `12345678901234567890` itself is already rounded to the nearest representable number when it is parsed by JavaScript.

Without `JSON.rawJSON`, there is no way to tell `JSON.stringify` to produce the number literal `12345678901234567890`, because there is simply no corresponding JavaScript number value. With raw JSON, you can directly tell `JSON.stringify()` what a particular value should be stringified as:

js

    const rawJSON = JSON.rawJSON("12345678901234567890");
    JSON.stringify({ value: rawJSON });
    // {"value":12345678901234567890}
    

For a more complete example of this, see [Lossless number serialization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON#using_json_numbers)
.

Note that although we passed a string to `JSON.rawJSON()`, it still becomes a number in the final JSON. This is because the string represents the verbatim JSON text. If you want to serialize a string, you should use `JSON.rawJSON()` with a quotes-enclosed string value:

js

    const rawJSON = JSON.rawJSON('"Hello world"');
    JSON.stringify({ value: rawJSON });
    // {"value":"Hello world"}
    

`JSON.rawJSON` allows you to insert arbitrary JSON text, but does not allow you to create invalid JSON. Anything that was not permitted by the JSON syntax is not permitted by `JSON.rawJSON()` either:

js

    const rawJSON = JSON.rawJSON('"Hello\nworld"'); // Syntax error, because line breaks are not allowed in JSON strings
    

Furthermore, you cannot use `JSON.rawJSON()` to create JSON objects or arrays.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#examples)

-------------------------------------------------------------------------------------------------------------------

### [Using JSON.rawJSON() to create JSON expressions of different types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#using_json.rawjson_to_create_json_expressions_of_different_types)

js

    const numJSON = JSON.rawJSON("123");
    const strJSON = JSON.rawJSON('"Hello world"');
    const boolJSON = JSON.rawJSON("true");
    const nullJSON = JSON.rawJSON("null");
    
    console.log(
      JSON.stringify({
        age: numJSON,
        message: strJSON,
        isActive: boolJSON,
        nothing: nullJSON,
      }),
    );
    
    // {"age":123,"message":"Hello world","isActive":true,"nothing":null}
    

However, you cannot use `JSON.rawJSON()` to create JSON objects or arrays:

js

    const arrJSON = JSON.rawJSON("[1, 2, 3]");
    const objJSON = JSON.rawJSON('{"a": 1, "b": 2}');
    // SyntaxError
    

### [Using JSON.rawJSON() to create escaped string literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#using_json.rawjson_to_create_escaped_string_literals)

Apart from numbers, there is only one other type that does not have a one-to-one correspondence between JavaScript values and JSON text: strings. When strings are serialized to JSON, all code points, other than those that are not legal inside JSON string literals (such as line breaks), are printed literally:

js

    console.log(JSON.stringify({ value: "\ud83d\ude04" })); // {"value":"😄"}
    

This may not be desirable, because the receiver of this string may handle Unicode differently. To improve interoperability, you can explicitly specify the string to be serialized with escape sequences:

js

    const rawJSON = JSON.rawJSON('"\\ud83d\\ude04"');
    const objStr = JSON.stringify({ value: rawJSON });
    console.log(objStr); // {"value":"\ud83d\ude04"}
    console.log(JSON.parse(objStr).value); // 😄
    

Note that the double backslashes in the `rawJSON` actually represents a single slash character.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-json.rawjson](https://tc39.es/ecma262/multipage/structured-data.html#sec-json.rawjson) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `JSON.rawJSON` in `core-js`](https://core-js.io/docs/features/ecmascript/json "External link (opens in new tab)")
    
*   [`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
    
*   [`JSON.isRawJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/isRawJSON)
    
*   [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/json/rawjson/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/json/rawjson (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2FrawJSON&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Frawjson%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2FrawJSON%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Frawjson%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
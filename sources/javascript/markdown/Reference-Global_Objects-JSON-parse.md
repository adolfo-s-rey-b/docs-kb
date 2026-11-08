*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#mdn-search)
    

JSON.parse()
============

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`JSON.parse()`** static method parses a JSON string, constructing the JavaScript value or object described by the string. An optional _reviver_ function can be provided to perform a transformation on the resulting object before it is returned.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#try_it)

-------------------------------------------------------------------------------------------------------------

    const json = '{"result":true, "count":42}';
    const obj = JSON.parse(json);
    
    console.log(obj.count);
    // Expected output: 42
    
    console.log(obj.result);
    // Expected output: true
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#syntax)

-------------------------------------------------------------------------------------------------------------

js

    JSON.parse(text)
    JSON.parse(text, reviver)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#parameters)

[`text`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#text)

The string to parse as JSON. See the [`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
 object for a description of JSON syntax.

[`reviver` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#reviver)

If a function, this prescribes how each value originally produced by parsing is transformed before being returned. Non-callable values are ignored. The function is called with the following arguments:

[`key`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#key)

The key associated with the value.

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#value)

The value produced by parsing.

[`context`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#context)

A context object that holds state relevant to the current expression being revived. It is a new object for each invocation of the reviver function.

[`source` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#source)

The original JSON string representing this value. This property is only present when reviving primitive values, but not when `value` is an object or array.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#return_value)

The [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
, [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
, string, number, boolean, or `null` value corresponding to the given JSON `text`.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#exceptions)

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

Thrown if the string to parse is not valid JSON.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#description)

-----------------------------------------------------------------------------------------------------------------------

`JSON.parse()` parses a JSON string according to the [JSON grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON#full_json_grammar)
, then evaluates the string as if it's a JavaScript expression. The only instance where a piece of JSON text represents a different value from the same JavaScript expression is when dealing with the `"__proto__"` key — see [Object literal syntax vs. JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#object_literal_syntax_vs._json)
.

### [The reviver parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#the_reviver_parameter)

If a `reviver` is specified, the value computed by parsing is _transformed_ before being returned. Specifically, the computed value and all its properties (in a [depth-first](https://en.wikipedia.org/wiki/Depth-first_search "External link (opens in new tab)")
 fashion, beginning with the most nested properties and proceeding to the original value itself) are individually run through the `reviver`.

The `reviver` is called with the object containing the property being processed as `this` (unless you define the `reviver` as an arrow function, in which case there's no separate `this` binding) and three arguments: `key`, `value`, and `context`. The key is a string even for arrays. For primitive values, the `context` argument has a field called `source` containing the source text of this value. If the `reviver` function returns [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 (or returns no value — for example, if execution falls off the end of the function), the property is deleted from the object. Otherwise, the property is redefined to be the return value. If the `reviver` only transforms some values and not others, be certain to return all untransformed values as-is — otherwise, they will be deleted from the resulting object.

Similar to the `replacer` parameter of [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
, for arrays and objects, `reviver` will be last called on the root value with an empty string as the `key` and the root object as the `value`. For other valid JSON values, `reviver` works similarly and is called once with an empty string as the `key` and the value itself as the `value`.

If you return another value from `reviver`, that value will completely replace the originally parsed value. This even applies to the root value. For example:

js

    const transformedObj = JSON.parse('[1,5,{"s":1}]', (key, value) =>
      typeof value === "object" ? undefined : value,
    );
    
    console.log(transformedObj); // undefined
    

There is no way to work around this generically. You cannot specially handle the case where `key` is an empty string, because JSON objects can also contain keys that are empty strings. You need to know very precisely what kind of transformation is needed for each key when implementing the reviver.

Note that `reviver` is run after the value is parsed. So, for example, numbers in JSON text will have already been converted to JavaScript numbers, and may lose precision in the process. One way to transfer large numbers without loss of precision is to serialize them as strings, and revive them to [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
, or other appropriate arbitrary precision formats.

You can also use the `context.source` property to access the original JSON source text representing the value, as shown below:

js

    const bigJSON = '{"gross_gdp": 12345678901234567890}';
    const bigObj = JSON.parse(bigJSON, (key, value, context) => {
      if (key === "gross_gdp") {
        // Ignore the value because it has already lost precision
        return BigInt(context.source);
      }
      return value;
    });
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using JSON.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#using_json.parse)

js

    JSON.parse("{}"); // {}
    JSON.parse("true"); // true
    JSON.parse('"foo"'); // "foo"
    JSON.parse('[1, 5, "false"]'); // [1, 5, "false"]
    JSON.parse("null"); // null
    

### [Using the reviver parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#using_the_reviver_parameter)

js

    JSON.parse(
      '{"p": 5}',
      (key, value) =>
        typeof value === "number"
          ? value * 2 // return value * 2 for numbers
          : value, // return everything else unchanged
    );
    // { p: 10 }
    
    JSON.parse('{"1": 1, "2": 2, "3": {"4": 4, "5": {"6": 6}}}', (key, value) => {
      console.log(key);
      return value;
    });
    // 1
    // 2
    // 4
    // 6
    // 5
    // 3
    // ""
    

### [Using reviver when paired with the replacer of JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#using_reviver_when_paired_with_the_replacer_of_json.stringify)

In order for a value to properly round-trip (that is, it gets deserialized to the same original object), the serialization process must preserve the type information. For example, you can use the `replacer` parameter of [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 for this purpose:

js

    // Maps are normally serialized as objects with no properties.
    // We can use the replacer to specify the entries to be serialized.
    const map = new Map([\
      [1, "one"],\
      [2, "two"],\
      [3, "three"],\
    ]);
    
    const jsonText = JSON.stringify(map, (key, value) =>
      value instanceof Map ? Array.from(value.entries()) : value,
    );
    
    console.log(jsonText);
    // [[1,"one"],[2,"two"],[3,"three"]]
    
    const map2 = JSON.parse(jsonText, (key, value) =>
      Array.isArray(value) && value.every(Array.isArray) ? new Map(value) : value,
    );
    
    console.log(map2);
    // Map { 1 => "one", 2 => "two", 3 => "three" }
    

Because JSON has no syntax space for annotating type metadata, in order to revive values that are not plain objects, you have to consider one of the following:

*   Serialize the entire object to a string and prefix it with a type tag.
*   "Guess" based on the structure of the data (for example, an array of two-member arrays)
*   If the shape of the payload is fixed, based on the property name (for example, all properties called `registry` hold `Map` objects).

### [Illegal JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#illegal_json)

When `JSON.parse` receives a string that does not conform to the JSON grammar, it throws a `SyntaxError`.

Arrays and objects cannot have [trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas)
 in JSON:

js

    JSON.parse("[1, 2, 3, 4, ]");
    // SyntaxError: Unexpected token ] in JSON at position 13
    
    JSON.parse('{"foo": 1, }');
    // SyntaxError: Unexpected token } in JSON at position 12
    

JSON strings must be delimited by double (not single) quotes:

js

    JSON.parse("{'foo': 1}");
    // SyntaxError: Unexpected token ' in JSON at position 1
    
    JSON.parse("'string'");
    // SyntaxError: Unexpected token ' in JSON at position 0
    

If you are writing JSON inside a JavaScript string literal, you should either use single quotes to delimit the JavaScript string literal, or escape the double quotes that delimit the JSON string:

js

    JSON.parse('{"foo": 1}'); // OK
    JSON.parse("{\"foo\": 1}"); // OK
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-json.parse](https://tc39.es/ecma262/multipage/structured-data.html#sec-json.parse) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of modern `JSON.parse` behavior (reviver's `context` parameter) in `core-js`](https://core-js.io/docs/features/ecmascript/json "External link (opens in new tab)")
    
*   [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/json/parse/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/json/parse (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2Fparse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Fparse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2Fparse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Fparse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
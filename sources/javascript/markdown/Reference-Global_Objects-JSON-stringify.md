*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#mdn-search)
    

JSON.stringify()
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`JSON.stringify()`** static method converts a JavaScript value to a JSON string, optionally replacing values if a replacer function is specified or optionally including only the specified properties if a replacer array is specified.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#try_it)

-----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#syntax)

-----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#parameters)

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#value)

The value to convert to a JSON string.

[`replacer` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#replacer)

A function that alters the behavior of the stringification process, or an array of strings and numbers that specifies properties of `value` to be included in the output. If `replacer` is an array, all elements in this array that are not strings or numbers (either primitives or wrapper objects), including [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
 values, are completely ignored. If `replacer` is anything other than a function or an array (e.g., [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or not provided), all string-keyed properties of the object are included in the resulting JSON string.

[`space` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#space)

A string or number that's used to insert white space (including indentation, line break characters, etc.) into the output JSON string for readability purposes.

If this is a number, it indicates the number of space characters to be used as indentation, clamped to 10 (that is, any number greater than `10` is treated as if it were `10`). Values less than 1 indicate that no space should be used.

If this is a string, the string (or the first 10 characters of the string, if it's longer than that) is inserted before every nested object or array.

If `space` is anything other than a string or number (can be either a primitive or a wrapper object) — for example, is [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or not provided — no white space is used.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#return_value)

A JSON string representing the given value, or undefined.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown in one of the following cases:

*   `value` contains a circular reference.
*   A [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     value is encountered.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#description)

---------------------------------------------------------------------------------------------------------------------------

`JSON.stringify()` converts a value to the JSON notation that the value represents. Values are stringified in the following manner:

*   [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
    , [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
    , [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
    , and [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     (obtainable via [`Object()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/Object)
    ) objects are converted to the corresponding primitive values during stringification, in accordance with the traditional conversion semantics. [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     objects (obtainable via [`Object()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/Object)
    ) are treated as plain objects.
*   Attempting to serialize [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     values will throw. However, if the BigInt has a `toJSON()` method (through monkey patching: `BigInt.prototype.toJSON = ...`), that method can provide the serialization result. This constraint ensures that a proper serialization (and, very likely, its accompanying deserialization) behavior is always explicitly provided by the user.
*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    , [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    , and [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     values are not valid JSON values. If any such values are encountered during conversion, they are either omitted (when found in an object) or changed to [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     (when found in an array). `JSON.stringify()` can return `undefined` when passing in "pure" values like `JSON.stringify(() => {})` or `JSON.stringify(undefined)`.
*   The numbers [`Infinity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity)
     and [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    , as well as the value [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    , are all considered `null`. (But unlike the values in the previous point, they would never be omitted.)
*   Arrays are serialized as arrays (enclosed by square brackets). Only array indices between 0 and `length - 1` (inclusive) are serialized; other properties are ignored.
*   The special raw JSON object created with [`JSON.rawJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON)
     is serialized as the raw JSON text it contains (by accessing its `rawJSON` property).
*   For other objects:
    *   All [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
        \-keyed properties will be completely ignored, even when using the [`replacer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter)
         parameter.
        
    *   If the value has a `toJSON()` method, it's responsible for defining what data will be serialized. Instead of the object being serialized, the value returned by the `toJSON()` method when called will be serialized. `JSON.stringify()` calls `toJSON` with one parameter, the `key`, which has the same semantic as the `key` parameter of the [`replacer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter)
         function:
        
        *   if this object is a property value, the property name
        *   if it is in an array, the index in the array, as a string
        *   if `JSON.stringify()` was directly called on this object, an empty string
        
        All [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
         objects implement the `toJSON()` method, which returns a string (the same as calling `toString()`). Thus, they will be serialized as strings. Similarly, [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
         objects implement `toJSON()`, which returns the same as [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
        .
        
    *   Only [enumerable own properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Enumerability_and_ownership_of_properties)
         are visited. This means [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
        , [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
        , etc. will become `"{}"`. You can use the [`replacer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter)
         parameter to serialize them to something more useful.
        
        Properties are visited using the same algorithm as [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
        , which has a well-defined order and is stable across implementations. For example, `JSON.stringify` on the same object will always produce the same string, and `JSON.parse(JSON.stringify(obj))` would produce an object with the same key ordering as the original (assuming the object is completely JSON-serializable).
        

### [The replacer parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter)

The `replacer` parameter can be either a function or an array.

As an array, its elements indicate the names of the properties in the object that should be included in the resulting JSON string. Only string and number values are taken into account; symbol keys are ignored.

As a function, it takes two parameters: the `key` and the `value` being stringified. The object in which the key was found is provided as the `replacer`'s `this` context.

The `replacer` function is called for the initial object being stringified as well, in which case the `key` is an empty string (`""`). It is then called for each property on the object or array being stringified. Array indices will be provided in its string form as `key`. The current property value will be replaced with the `replacer`'s return value for stringification. This means:

*   If you return a number, string, boolean, or `null`, that value is directly serialized and used as the property's value. (Returning a BigInt will throw as well.)
*   If you return a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
    , [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
    , or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    , the property is not included in the output.
*   If you return any other object, the object is recursively stringified, calling the `replacer` function on each property.

**Note:** When parsing JSON generated with `replacer` functions, you would likely want to use the [`reviver`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse#using_the_reviver_parameter)
 parameter to perform the reverse operation.

Typically, array elements' index would never shift (even when the element is an invalid value like a function, it will become `null` instead of omitted). Using the `replacer` function allows you to control the order of the array elements by returning a different array.

### [The space parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_space_parameter)

The `space` parameter may be used to control spacing in the final string.

*   If it is a number, successive levels in the stringification will each be indented by this many space characters.
*   If it is a string, successive levels will be indented by this string.

Each level of indentation will never be longer than 10. Number values of `space` are clamped to 10, and string values are truncated to 10 characters.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#examples)

---------------------------------------------------------------------------------------------------------------------

### [Using JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#using_json.stringify)

### [Using a function as replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#using_a_function_as_replacer)

If you wish the `replacer` to distinguish an initial object from a key with an empty string property (since both would give the empty string as key and potentially an object as value), you will have to keep track of the iteration count (if it is beyond the first iteration, it is a genuine empty string key).

### [Using an array as replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#using_an_array_as_replacer)

### [Using the space parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#using_the_space_parameter)

Indent the output with one space:

Using a tab character mimics standard pretty-print appearance:

### [toJSON() behavior](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#tojson_behavior)

Defining `toJSON()` for an object allows overriding its serialization behavior.

### [Issue with serializing circular references](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#issue_with_serializing_circular_references)

Since the [JSON format](https://www.json.org/ "External link (opens in new tab)")
 doesn't support object references (although an [IETF draft exists](https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03 "External link (opens in new tab)")
), a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 will be thrown if one attempts to encode an object with circular references.

To serialize circular references, you can use a library that supports them (e.g., [cycle.js](https://github.com/douglascrockford/JSON-js/blob/master/cycle.js "External link (opens in new tab)")
 by Douglas Crockford) or implement a solution yourself, which will require finding and replacing (or removing) the cyclic references by serializable values.

If you are using `JSON.stringify()` to deep-copy an object, you may instead want to use [`structuredClone()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone "structuredClone()")
, which supports circular references. JavaScript engine APIs for binary serialization, such as [`v8.serialize()`](https://nodejs.org/api/v8.html#v8serializevalue "External link (opens in new tab)")
, also support circular references.

### [Using JSON.stringify() with localStorage](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#using_json.stringify_with_localstorage)

In a case where you want to store an object created by your user and allow it to be restored even after the browser has been closed, the following example is a model for the applicability of `JSON.stringify()`:

### [Well-formed JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#well-formed_json.stringify)

Engines implementing the [well-formed JSON.stringify specification](https://github.com/tc39/proposal-well-formed-stringify "External link (opens in new tab)")
 will stringify lone surrogates (any code point from U+D800 to U+DFFF) using Unicode escape sequences rather than literally (outputting lone surrogates). Before this change, such strings could not be encoded in valid UTF-8 or UTF-16:

But with this change `JSON.stringify()` represents lone surrogates using JSON escape sequences that _can_ be encoded in valid UTF-8 or UTF-16:

This change should be backwards-compatible as long as you pass the result of `JSON.stringify()` to APIs such as `JSON.parse()` that will accept any valid JSON text, because they will treat Unicode escapes of lone surrogates as identical to the lone surrogates themselves. _Only_ if you are directly interpreting the result of `JSON.stringify()` do you need to carefully handle `JSON.stringify()`'s two possible encodings of these code points.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-json.stringify](https://tc39.es/ecma262/multipage/structured-data.html#sec-json.stringify) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Polyfill of modern `JSON.stringify` behavior (symbol, well-formed unicode, raw JSON) in `core-js`](https://core-js.io/docs/features/ecmascript/json "External link (opens in new tab)")
    
*   [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)
    
*   [`JSON.rawJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/json/stringify/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/json/stringify (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2Fstringify&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Fstringify%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FJSON%2Fstringify%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fjson%2Fstringify%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
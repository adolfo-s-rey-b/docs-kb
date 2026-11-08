*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#mdn-search)
    

Map
===

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Map`** object holds key-value pairs and remembers the original insertion order of the keys. Any value (both objects and [primitive values](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
) may be used as either a key or a value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#try_it)

------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#description)

----------------------------------------------------------------------------------------------------------------

`Map` objects are collections of key-value pairs. A key in the `Map` **may only occur once**; it is unique in the `Map`'s collection. A `Map` object is iterated by key-value pairs — a [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loop returns a 2-member array of `[key, value]` for each iteration. Iteration happens in _insertion order_, which corresponds to the order in which each key-value pair was first inserted into the map by the [`set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/set)
 method (that is, there wasn't a key with the same value already in the map when `set()` was called).

The specification requires maps to be implemented "that, on average, provide access times that are sublinear on the number of elements in the collection". Therefore, it could be represented internally as a hash table (with O(1) lookup), a search tree (with O(log(N)) lookup), or any other data structure, as long as the complexity is better than O(N).

### [Key equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#key_equality)

Value equality is based on the [SameValueZero](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#same-value-zero_equality)
 algorithm. (It used to use [SameValue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Equality_comparisons_and_sameness#same-value_equality_using_object.is)
, which treated `0` and `-0` as different. Check [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#browser_compatibility)
.) This means [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 is considered the same as `NaN` (even though `NaN !== NaN`) and all other values are considered equal according to the semantics of the `===` operator. Also, for object keys, equality is based on object identity. They are compared by reference, not by value. See [Using the Map object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#using_the_map_object)
 for examples.

### [Objects vs. Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#objects_vs._maps)

[`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
 is similar to `Map`—both let you set keys to values, retrieve those values, delete keys, and detect whether something is stored at a key. For this reason (and because there were no built-in alternatives), `Object` has been used as `Map` historically.

However, there are important differences that make `Map` preferable in some cases:

|     | Map | Object |
| --- | --- | --- |
| Accidental Keys | A `Map` does not contain any keys by default. It only contains what is explicitly put into it. | An `Object` has a prototype, so it contains default keys that could collide with your own keys if you're not careful.<br><br>**Note:** This can be bypassed by using [`Object.create(null)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)<br>, but this is seldom done. |
| Security | A `Map` is safe to use with user-provided keys and values. | Setting user-provided key-value pairs on an `Object` may allow an attacker to override the object's prototype, which can lead to [object injection attacks](https://github.com/eslint-community/eslint-plugin-security/blob/main/docs/the-dangers-of-square-bracket-notation.md "External link (opens in new tab)")<br> or [prototype pollution attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Prototype_pollution)<br>. Like the accidental keys issue, this can also be mitigated by using a `null`\-prototype object. |
| Key Types | A `Map`'s keys can be any value (including functions, objects, or any primitive). | The keys of an `Object` must be either a [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)<br> or a [`Symbol`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)<br>. |
| Key Order | The keys in `Map` are ordered in a straightforward way: A `Map` object iterates entries, keys, and values in the order of entry insertion. | Although the keys of an ordinary `Object` are ordered now, this was not always the case, and the order is complex. As a result, it's best not to rely on property order.<br><br>The order was first defined for own properties only in ECMAScript 2015; ECMAScript 2020 defines order for inherited properties as well. But note that no single mechanism iterates **all** of an object's properties; the various mechanisms each include different subsets of properties. ([`for-in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)<br> includes only enumerable string-keyed properties; [`Object.keys`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)<br> includes only own, enumerable, string-keyed properties; [`Object.getOwnPropertyNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)<br> includes own, string-keyed properties even if non-enumerable; [`Object.getOwnPropertySymbols`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols)<br> does the same for just `Symbol`\-keyed properties, etc.) |
| Size | The number of items in a `Map` is easily retrieved from its [`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size)<br> property. | Determining the number of items in an `Object` is more roundabout and less efficient. A common way to do it is through the [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)<br> of the array returned from [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)<br>. |
| Iteration | A `Map` is an [iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)<br>, so it can be directly iterated. | `Object` does not implement an [iteration protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)<br>, and so objects are not directly iterable using the JavaScript [for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)<br> statement (by default).<br><br>**Note:**<br><br>*   An object can implement the iteration protocol, or you can get an iterable for an object using [`Object.keys`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)<br>     or [`Object.entries`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)<br>    .<br>*   The [for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)<br>     statement allows you to iterate over the _enumerable_ properties of an object. |
| Performance | Performs better in scenarios involving frequent additions and removals of key-value pairs. | Not optimized for frequent additions and removals of key-value pairs. |
| Serialization and parsing | No native support for serialization or parsing.<br><br>(But you can build your own serialization and parsing support for `Map` by using [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)<br> with its _replacer_ argument, and by using [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)<br> with its _reviver_ argument. See the Stack Overflow question [How do you JSON.stringify an ES6 Map?](https://stackoverflow.com/q/29085197/ "External link (opens in new tab)")<br>). | Native support for serialization from [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)<br> to JSON, using [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)<br>.<br><br>Native support for parsing from JSON to [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)<br>, using [`JSON.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)<br>. |

### [Setting object properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#setting_object_properties)

Setting Object properties works for Map objects as well, and can cause considerable confusion.

Therefore, this appears to work in a way:

But that way of setting a property does not interact with the Map data structure. It uses the feature of the generic object. The value of 'bla' is not stored in the Map for queries. Other operations on the data fail:

The correct usage for storing data in the Map is through the `set(key, value)` method.

### [Map-like browser APIs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis)

**Browser `Map`\-like objects** (or "maplike objects") are [Web API](https://developer.mozilla.org/en-US/docs/Web/API)
 interfaces that behave in many ways like a `Map`.

Just like `Map`, entries can be iterated in the same order that they were added to the object. `Map`\-like objects and `Map` also have properties and methods that share the same name and behavior. However unlike `Map` they only allow specific predefined types for the keys and values of each entry.

The allowed types are set in the specification IDL definition. For example, [`RTCStatsReport`](https://developer.mozilla.org/en-US/docs/Web/API/RTCStatsReport)
 is a `Map`\-like object that must use strings for keys and objects for values. This is defined in the specification IDL below:

`Map`\-like objects are either read-only or read-writable (see the `readonly` keyword in the IDL above).

*   Read-only `Map`\-like objects have the property [`size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size)
    , and the methods: [`entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)
    , [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)
    , [`get()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get)
    , [`has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/has)
    , [`keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys)
    , [`values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values)
    , and [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Symbol.iterator)
    .
*   Writeable `Map`\-like objects additionally have the methods: [`clear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/clear)
    , [`delete()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/delete)
    , and [`set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/set)
    .

The methods and properties have the same behavior as the equivalent entities in `Map`, except for the restriction on the types of the keys and values.

The following are examples of read-only `Map`\-like browser objects:

*   [`AudioParamMap`](https://developer.mozilla.org/en-US/docs/Web/API/AudioParamMap)
    
*   [`CSSFontFeatureValuesMap`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontFeatureValuesMap)
    
*   [`EventCounts`](https://developer.mozilla.org/en-US/docs/Web/API/EventCounts)
    
*   [`KeyboardLayoutMap`](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardLayoutMap)
    
*   [`MIDIInputMap`](https://developer.mozilla.org/en-US/docs/Web/API/MIDIInputMap)
    
*   [`MIDIOutputMap`](https://developer.mozilla.org/en-US/docs/Web/API/MIDIOutputMap)
    
*   [`RTCStatsReport`](https://developer.mozilla.org/en-US/docs/Web/API/RTCStatsReport)
    

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#constructor)

----------------------------------------------------------------------------------------------------------------

[`Map()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)

Creates a new `Map` object.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#static_properties)

----------------------------------------------------------------------------------------------------------------------------

[`Map[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Symbol.species)

The constructor function that is used to create derived objects.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#static_methods)

----------------------------------------------------------------------------------------------------------------------

[`Map.groupBy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/groupBy)

Groups the elements of a given iterable using the values returned by a provided callback function. The final returned `Map` uses the unique values from the test function as keys, which can be used to get the array of elements in each group.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#instance_properties)

--------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Map.prototype` and shared by all `Map` instances.

[`Map.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Map` instances, the initial value is the [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
 constructor.

[`Map.prototype.size`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size)

Returns the number of key/value pairs in the `Map` object.

[`Map.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Map"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#instance_methods)

--------------------------------------------------------------------------------------------------------------------------

[`Map.prototype.clear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/clear)

Removes all key-value pairs from the `Map` object.

[`Map.prototype.delete()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/delete)

Removes the entry specified by the key from this `Map`.

[`Map.prototype.entries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)

Returns a new Iterator object that contains a two-member array of `[key, value]` for each element in the `Map` object in insertion order.

[`Map.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)

Calls `callbackFn` once for each key-value pair present in the `Map` object, in insertion order. If a `thisArg` parameter is provided to `forEach`, it will be used as the `this` value for each callback.

[`Map.prototype.get()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get)

Returns the value corresponding to the key in this `Map`, or `undefined` if there is none.

[`Map.prototype.getOrInsert()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/getOrInsert)

Returns the value corresponding to the specified key in this `Map`. If the key is not present, it inserts a new entry with the key and a given default value, and returns the inserted value.

[`Map.prototype.getOrInsertComputed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/getOrInsertComputed)

Returns the value corresponding to the specified key in this `Map`. If the key is not present, it inserts a new entry with the key and a default value computed from a given callback, and returns the inserted value.

[`Map.prototype.has()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/has)

Returns a boolean indicating whether an entry with the specified key exists in this `Map` or not.

[`Map.prototype.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys)

Returns a new Iterator object that contains the keys for each element in the `Map` object in insertion order.

[`Map.prototype.set()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/set)

Adds a new entry with a specified key and value to this `Map`, or updates an existing entry if the key already exists.

[`Map.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values)

Returns a new Iterator object that contains the values for each element in the `Map` object in insertion order.

[`Map.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Symbol.iterator)

Returns a new Iterator object that contains a two-member array of `[key, value]` for each element in the `Map` object in insertion order.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#examples)

----------------------------------------------------------------------------------------------------------

### [Using the Map object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#using_the_map_object)

### [Using NaN as Map keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#using_nan_as_map_keys)

[`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
 can also be used as a key. Even though every `NaN` is not equal to itself (`NaN !== NaN` is true), the following example works because `NaN`s are indistinguishable from each other:

### [Iterating Map with for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#iterating_map_with_for...of)

Maps can be iterated using a `for...of` loop:

### [Iterating Map with forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#iterating_map_with_foreach)

Maps can be iterated using the [`forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)
 method:

### [Relation with Array objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#relation_with_array_objects)

### [Cloning and merging Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#cloning_and_merging_maps)

Just like `Array`s, `Map`s can be cloned:

**Note:** Keep in mind that _the data itself_ is not cloned. In other words, it is only a [shallow copy](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy)
 of the `Map`.

Maps can be merged, maintaining key uniqueness:

Maps can be merged with Arrays, too:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-map-objects](https://tc39.es/ecma262/multipage/keyed-collections.html#sec-map-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#see_also)

----------------------------------------------------------------------------------------------------------

*   [Polyfill for `Map` in `core-js`](https://core-js.io/docs/features/ecmascript/collections#h-map "External link (opens in new tab)")
    
*   [es-shims polyfill of `Map`](https://www.npmjs.com/package/es-map "External link (opens in new tab)")
    
*   [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
    
*   [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
    
*   [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/map/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/map (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
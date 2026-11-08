*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#mdn-search)
    

String
======

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`String`** object is used to represent and manipulate a sequence of characters.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#description)

-------------------------------------------------------------------------------------------------------------------

Strings are useful for holding data that can be represented in text form. Some of the most-used operations on strings are to check their [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
, to build and concatenate them using the [`+` and `+=` string operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#string_operators)
, checking for the existence or location of substrings with the [`indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)
 method, or extracting substrings with the [`substring()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
 method.

### [Creating strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#creating_strings)

Strings can be created as primitives, from string literals, or as objects, using the [`String()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String)
 constructor:

String primitives and string objects share many behaviors, but have other important differences and caveats. See "[String primitives and String objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_primitives_and_string_objects)
" below.

String literals can be specified using single or double quotes, which are treated identically, or using the backtick character \`. This last form specifies a [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
: with this form you can interpolate expressions. For more information on the syntax of string literals, see [lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#string_literals)
.

### [Character access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#character_access)

There are two ways to access an individual character in a string. The first is the [`charAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
 method:

The other way is to treat the string as an array-like object, where individual characters correspond to a numerical index:

When using bracket notation for character access, attempting to delete or assign a value to these properties will not succeed. The properties involved are neither writable nor configurable. (See [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
 for more information.)

### [Comparing strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#comparing_strings)

Use the [less-than and greater-than operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
 to compare strings:

Note that all comparison operators, including [`===`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
 and [`==`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
, compare strings case-sensitively. A common way to compare strings case-insensitively is to convert both to the same case (upper or lower) before comparing them.

The choice of whether to transform by [`toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
 or [`toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
 is mostly arbitrary, and neither one is fully robust when extending beyond the Latin alphabet. For example, the German lowercase letter `ß` and `ss` are both transformed to `SS` by `toUpperCase()`, while the Turkish letter `ı` would be falsely reported as unequal to `I` by `toLowerCase()` unless specifically using [`toLocaleLowerCase("tr")`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleLowerCase)
.

A locale-aware and robust solution for testing case-insensitive equality is to use the [`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
 API or the string's [`localeCompare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
 method — they share the same interface — with the [`sensitivity`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator/Collator#sensitivity)
 option set to `"accent"` or `"base"`.

The `localeCompare()` method enables string comparison in a similar fashion as `strcmp()` — it allows sorting strings in a locale-aware manner.

### [String primitives and String objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_primitives_and_string_objects)

Note that JavaScript distinguishes between `String` objects and [primitive string](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
 values. (The same is true of [`Boolean`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
 and [`Numbers`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
.)

String literals (denoted by double or single quotes) and strings returned from `String` calls in a non-constructor context (that is, called without using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 keyword) are primitive strings. In contexts where a method is to be invoked on a primitive string or a property lookup occurs, JavaScript will automatically wrap the string primitive and call the method or perform the property lookup on the wrapper object instead.

**Warning:** You should rarely find yourself using `String` as a constructor.

String primitives and `String` objects also give different results when using [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
. Primitives passed to `eval` are treated as source code; `String` objects are treated as all other objects are, by returning the object. For example:

For these reasons, the code may break when it encounters `String` objects when it expects a primitive string instead, although generally, authors need not worry about the distinction.

A `String` object can always be converted to its primitive counterpart with the [`valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/valueOf)
 method.

### [String coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)

Many built-in operations that expect strings first coerce their arguments to strings (which is largely why `String` objects behave similarly to string primitives). [The operation](https://tc39.es/ecma262/multipage/abstract-operations.html#sec-tostring "External link (opens in new tab)")
 can be summarized as follows:

*   Strings are returned as-is.
*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
     turns into `"undefined"`.
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
     turns into `"null"`.
*   `true` turns into `"true"`; `false` turns into `"false"`.
*   Numbers are converted with the same algorithm as [`toString(10)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)
    .
*   [BigInts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
     are converted with the same algorithm as [`toString(10)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/toString)
    .
*   [Symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    .
*   Objects are first [converted to a primitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
     by calling its [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toPrimitive)
     (with `"string"` as hint), `toString()`, and `valueOf()` methods, in that order. The resulting primitive is then converted to a string.

There are several ways to achieve nearly the same effect in JavaScript.

*   [Template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
    : `` `${x}` `` does exactly the string coercion steps explained above for the embedded expression.
*   The [`String()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String)
     function: `String(x)` uses the same algorithm to convert `x`, except that [Symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
     don't throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    , but return `"Symbol(description)"`, where `description` is the [description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/description)
     of the Symbol.
*   Using the [`+` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
    : `"" + x` coerces its operand to a _primitive_ instead of a _string_, and, for some objects, has entirely different behaviors from normal string coercion. See its [reference page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
     for more details.

Depending on your use case, you may want to use `` `${x}` `` (to mimic built-in behavior) or `String(x)` (to handle symbol values without throwing an error), but you should not use `"" + x`.

### [UTF-16 characters, Unicode code points, and grapheme clusters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)

Strings are represented fundamentally as sequences of [UTF-16 code units](https://en.wikipedia.org/wiki/UTF-16 "External link (opens in new tab)")
. In UTF-16 encoding, every code unit is exact 16 bits long. This means there are a maximum of 216, or 65536 possible characters representable as single UTF-16 code units. This character set is called the [basic multilingual plane (BMP)](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane "External link (opens in new tab)")
, and includes the most common characters like the Latin, Greek, Cyrillic alphabets, as well as many East Asian characters. Each code unit can be written in a string with `\u` followed by exactly four hex digits.

However, the entire Unicode character set is much, much bigger than 65536. The extra characters are stored in UTF-16 as _surrogate pairs_, which are pairs of 16-bit code units that represent a single character. To avoid ambiguity, the two parts of the pair must be between `0xD800` and `0xDFFF`, and these code units are not used to encode single-code-unit characters. (More precisely, leading surrogates, also called high-surrogate code units, have values between `0xD800` and `0xDBFF`, inclusive, while trailing surrogates, also called low-surrogate code units, have values between `0xDC00` and `0xDFFF`, inclusive.) Each Unicode character, comprised of one or two UTF-16 code units, is also called a _Unicode code point_. Each Unicode code point can be written in a string with `\u{xxxxxx}` where `xxxxxx` represents 1–6 hex digits.

A "lone surrogate" is a 16-bit code unit satisfying one of the descriptions below:

*   It is in the range `0xD800`–`0xDBFF`, inclusive (i.e., is a leading surrogate), but it is the last code unit in the string, or the next code unit is not a trailing surrogate.
*   It is in the range `0xDC00`–`0xDFFF`, inclusive (i.e., is a trailing surrogate), but it is the first code unit in the string, or the previous code unit is not a leading surrogate.

Lone surrogates do not represent any Unicode character. Although most JavaScript built-in methods handle them correctly because they all work based on UTF-16 code units, lone surrogates are often not valid values when interacting with other systems — for example, [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
 will throw a [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
 for lone surrogates, because URI encoding uses UTF-8 encoding, which does not have any encoding for lone surrogates. Strings not containing any lone surrogates are called _well-formed_ strings, and are safe to be used with functions that do not deal with UTF-16 (such as `encodeURI()` or [`TextEncoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder)
). You can check if a string is well-formed with the [`isWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/isWellFormed)
 method, or sanitize lone surrogates with the [`toWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toWellFormed)
 method.

On top of Unicode characters, there are certain sequences of Unicode characters that should be treated as one visual unit, known as a _grapheme cluster_. The most common case is emojis: many emojis that have a range of variations are actually formed by multiple emojis, usually joined by the <ZWJ> (`U+200D`) character.

You must be careful which level of characters you are iterating on. For example, [`split("")`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
 will split by UTF-16 code units and will separate surrogate pairs. String indexes also refer to the index of each UTF-16 code unit. On the other hand, [`[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)
 iterates by Unicode code points. Iterating through grapheme clusters will require some custom code.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#constructor)

-------------------------------------------------------------------------------------------------------------------

[`String()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String)

Creates `String` objects. When called as a function, it returns primitive values of type String.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#static_methods)

-------------------------------------------------------------------------------------------------------------------------

[`String.fromCharCode()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode)

Returns a string created by using the specified sequence of Unicode values.

[`String.fromCodePoint()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint)

Returns a string created by using the specified sequence of code points.

[`String.raw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw)

Returns a string created from a raw template string.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#instance_properties)

-----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `String.prototype` and shared by all `String` instances.

[`String.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `String` instances, the initial value is the [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String)
 constructor.

These properties are own properties of each `String` instance.

[`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)

Reflects the `length` of the string. Read-only.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#instance_methods)

-----------------------------------------------------------------------------------------------------------------------------

[`String.prototype.at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/at)

Returns the character (exactly one UTF-16 code unit) at the specified `index`. Accepts negative integers, which count back from the last string character.

[`String.prototype.charAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)

Returns the character (exactly one UTF-16 code unit) at the specified `index`.

[`String.prototype.charCodeAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)

Returns a number that is the UTF-16 code unit value at the given `index`.

[`String.prototype.codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt)

Returns a nonnegative integer Number that is the code point value of the UTF-16 encoded code point starting at the specified `pos`.

[`String.prototype.concat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat)

Combines the text of two (or more) strings and returns a new string.

[`String.prototype.endsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)

Determines whether a string ends with the characters of the string `searchString`.

[`String.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)

Determines whether the calling string contains `searchString`.

[`String.prototype.indexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)

Returns the index within this string of the first occurrence of `searchValue`, or `-1` if not found.

[`String.prototype.isWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/isWellFormed)

Returns a boolean indicating whether this string contains any [lone surrogates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
.

[`String.prototype.lastIndexOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)

Returns the index within this string of the last occurrence of `searchValue`, or `-1` if not found.

[`String.prototype.localeCompare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)

Returns a number indicating whether the reference string `compareString` comes before, after, or is equivalent to the given string in sort order.

[`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)

Used to match regular expression `regexp` against a string.

[`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)

Returns an iterator of all `regexp`'s matches.

[`String.prototype.normalize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize)

Returns the Unicode Normalization Form of the calling string value.

[`String.prototype.padEnd()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padEnd)

Pads the current string from the end with a given string and returns a new string of the length `targetLength`.

[`String.prototype.padStart()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart)

Pads the current string from the start with a given string and returns a new string of the length `targetLength`.

[`String.prototype.repeat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)

Returns a string consisting of the elements of the object repeated `count` times.

[`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

Used to replace occurrences of `searchFor` using `replaceWith`. `searchFor` may be a string or Regular Expression, and `replaceWith` may be a string or function.

[`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)

Used to replace all occurrences of `searchFor` using `replaceWith`. `searchFor` may be a string or Regular Expression, and `replaceWith` may be a string or function.

[`String.prototype.search()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)

Search for a match between a regular expression `regexp` and the calling string.

[`String.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)

Extracts a section of a string and returns a new string.

[`String.prototype.split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)

Returns an array of strings populated by splitting the calling string at occurrences of the substring `sep`.

[`String.prototype.startsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith)

Determines whether the calling string begins with the characters of string `searchString`.

[`String.prototype.substr()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)

Returns a portion of the string, starting at the specified index and extending for a given number of characters afterwards.

[`String.prototype.substring()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)

Returns a new string containing characters of the calling string from (or between) the specified index (or indices).

[`String.prototype.toLocaleLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleLowerCase)

The characters within a string are converted to lowercase while respecting the current locale.

For most languages, this will return the same as [`toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
.

[`String.prototype.toLocaleUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase)

The characters within a string are converted to uppercase while respecting the current locale.

For most languages, this will return the same as [`toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
.

[`String.prototype.toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)

Returns the calling string value converted to lowercase.

[`String.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toString)

Returns a string representing the specified object. Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`String.prototype.toUpperCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)

Returns the calling string value converted to uppercase.

[`String.prototype.toWellFormed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toWellFormed)

Returns a string where all [lone surrogates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
 of this string are replaced with the Unicode replacement character U+FFFD.

[`String.prototype.trim()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)

Trims whitespace from the beginning and end of the string.

[`String.prototype.trimEnd()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimEnd)

Trims whitespace from the end of the string.

[`String.prototype.trimStart()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimStart)

Trims whitespace from the beginning of the string.

[`String.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/valueOf)

Returns the primitive value of the specified object. Overrides the [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 method.

[`String.prototype[Symbol.iterator]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/Symbol.iterator)

Returns a new iterator object that iterates over the code points of a String value, returning each code point as a String value.

### [HTML wrapper methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#html_wrapper_methods)

**Warning:** Deprecated. Avoid these methods.

They are of limited use, as they are based on a very old HTML standard and provide only a subset of the currently available HTML tags and attributes. Many of them create deprecated or non-standard markup today. In addition, they do string concatenation without any validation or sanitation, which makes them a potential security threat when directly inserted using [`innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)
. Use [DOM APIs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
 such as [`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
 instead.

[`String.prototype.anchor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor)

[`<a name="name">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#name)
 (hypertext target)

[`String.prototype.big()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/big)

[`<big>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big)

[`String.prototype.blink()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/blink)

`<blink>`

[`String.prototype.bold()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/bold)

[`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)

[`String.prototype.fixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fixed)

[`<tt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt)

[`String.prototype.fontcolor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontcolor)

[`<font color="color">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font#color)

[`String.prototype.fontsize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize)

[`<font size="size">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font#size)

[`String.prototype.italics()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/italics)

[`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)

[`String.prototype.link()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/link)

[`<a href="url">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 (link to URL)

[`String.prototype.small()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/small)

[`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)

[`String.prototype.strike()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/strike)

[`<strike>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strike)

[`String.prototype.sub()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/sub)

[`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)

[`String.prototype.sup()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/sup)

[`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)

Note that these methods do not check if the string itself contains HTML tags, so it's possible to create invalid HTML:

The only escaping they do is to replace `"` in the attribute value (for [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor)
, [`fontcolor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontcolor)
, [`fontsize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize)
, and [`link()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/link)
) with `&quot;`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#examples)

-------------------------------------------------------------------------------------------------------------

### [String conversion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_conversion)

The `String()` function is a more reliable way of converting values to strings than calling the `toString()` method of the value, as the former works when used on [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 and [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. For example:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string-objects](https://tc39.es/ecma262/multipage/text-processing.html#sec-string-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Numbers and strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings)
     guide
*   [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1ddd95504b4507beeda0f08bd772eb167922b86a%0A*+Document+last+modified%3A+2026-05-22T15%3A48%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
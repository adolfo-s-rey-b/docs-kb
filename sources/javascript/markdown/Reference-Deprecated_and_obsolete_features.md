*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#mdn-search)
    

Deprecated and obsolete features
================================

This page lists features of JavaScript that are deprecated (that is, still available but should not be used) and obsolete (that is, no longer usable).

[Deprecated features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#deprecated_features)

----------------------------------------------------------------------------------------------------------------------------------------------

These deprecated features can still be used, but should be used with caution because they are not required to be implemented by every JavaScript engine. You should work to remove their use from your code.

Some of these deprecated features are listed in the [Annex B](https://tc39.es/ecma262/multipage/additional-ecmascript-features-for-web-browsers.html "External link (opens in new tab)")
 section of the ECMAScript specification. This section is described as normative optional — that is, web browser hosts must implement these features, while non-web hosts may not. These features are likely stable because removing them will cause backward compatibility issues and break legacy websites. (JavaScript has the design goal of "don't break the web".) Still, they are not cross-platform portable and may not be supported by all analysis tools, so you are advised to not use them, as the introduction of Annex B states:

> … All of the language features and behaviors specified in this annex have one or more undesirable characteristics and in the absence of legacy usage would be removed from this specification. …
> 
> … Programmers should not use or assume the existence of these features and behaviors when writing new ECMAScript code. …

Some others, albeit in the main spec body, are also marked as normative optional and should not be depended on.

### [HTML comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#html_comments)

JavaScript source, if parsed as scripts, allows HTML-like comments, as if the script is part of a `<script>` tag.

The following is valid JavaScript when running in a web browser (or Node.js, which uses the V8 engine powering Chrome):

`<!--` and `-->` both act like `//`, i.e., starting line comments. `-->` is only valid at the start of a line (to avoid ambiguity with a postfix decrement followed by a greater than operator), while `<!--` can occur anywhere in the line.

### [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)

The following properties are deprecated. This does not affect their use in [replacement strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
:

[`$1–$9`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n)

Parenthesized substring matches, if any.

[`input`, `$_`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/input)

The string against which a regular expression is matched.

[`lastMatch`, `$&`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastMatch)

The last matched substring.

[`lastParen`, `$+`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastParen)

The last parenthesized substring match, if any.

[`leftContext`, `` $` ``](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/leftContext)

The substring preceding the most recent match.

[`rightContext`, `$'`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/rightContext)

The substring following the most recent match.

**Warning:** Avoid using these static properties, as they can cause [issues when interacting with external code](https://github.com/tc39/proposal-regexp-legacy-features/blob/master/subclass-restriction-motivation.md#legacy-static-properties-regexp1-etc "External link (opens in new tab)")
!

The [`compile()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/compile)
 method is deprecated. Construct a new `RegExp` instance instead.

The following regex syntaxes are deprecated and only available in [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
. In Unicode-aware mode, they are all syntax errors:

*   [Lookahead assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
     can have [quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
    .
*   [Backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
     that do not refer to an existing capturing group become [legacy octal escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#escape_sequences)
    .
*   In [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    , character ranges where one boundary is a character class make the `-` become a literal character.
*   An escape sequence that's not recognized becomes an ["identity escape"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    .
*   Escape sequences within [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
     of the form `\cX` where `X` is a number or `_` are decoded in the same way as those with [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
     letters: `\c0` is the same as `\cP` when taken modulo 32. In addition, if the form `\cX` is encountered anywhere where `X` is not one of the recognized characters, then the backslash is treated as a literal character.
*   The sequence `\k` within a regex that doesn't have any [named capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
     is treated as an identity escape.
*   The syntax characters `]`, `{`, and `}` may appear [literally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
     without escaping if they cannot be interpreted as the end of a character class or quantifier delimiters.

### [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#function)

*   The [`caller`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/caller)
     property of functions and the [`arguments.callee`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/callee)
     property are deprecated and unavailable in strict mode.
*   Instead of accessing `arguments` as a property of a function, you should use the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
     object inside function closures.

### [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#object)

*   The [`Object.prototype.__proto__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto)
     accessors are deprecated. Use [`Object.getPrototypeOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)
     and [`Object.setPrototypeOf`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
     instead. This does not apply to the `__proto__` literal key in object literals.
*   The [`Object.prototype.__defineGetter__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__defineGetter__)
    , [`Object.prototype.__defineSetter__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__defineSetter__)
    , [`Object.prototype.__lookupGetter__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__lookupGetter__)
    , and [`Object.prototype.__lookupSetter__`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__lookupSetter__)
     methods are deprecated. Use [`Object.getOwnPropertyDescriptor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor)
     and [`Object.defineProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
     instead.

### [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#string)

*   HTML wrapper methods like [`String.prototype.fontsize`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fontsize)
     and [`String.prototype.big`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/big)
    .
*   [`String.prototype.substr`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
     probably won't be removed anytime soon, but it's defined in Annex B and hence normative optional.
*   `String.prototype.trimLeft` and `String.prototype.trimRight` should be replaced with [`String.prototype.trimStart`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimStart)
     and [`String.prototype.trimEnd`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trimEnd)
    .

### [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#date)

*   The [`getYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear)
     and [`setYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setYear)
     methods are affected by the Year-2000-Problem and have been subsumed by [`getFullYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
     and [`setFullYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)
    .
*   The `toGMTString()` method is deprecated. Use [`toUTCString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)
     instead.

### [Escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#escape_sequences)

*   Octal escape sequences (\\ followed by one, two, or three octal digits) are deprecated in string and regular expression literals.
*   The [`escape()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/escape)
     and [`unescape()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/unescape)
     functions are deprecated. Use [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
    , [`encodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
    , [`decodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
    , or [`decodeURIComponent()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
     to encode and decode escape sequences for special characters.

### [Statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#statements)

The [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
 statement is deprecated and unavailable in strict mode.

Initializers in `var` declarations of [`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
 loop headers are deprecated and produce [syntax errors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_for-in_initializer)
 in strict mode. The initializer expression is evaluated and assigned to the variable, but the value would be immediately reassigned on the first iteration of the loop.

Normally, the `catch` block of a [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
 statement cannot contain any variable declaration with the same name as the variables bound in the `catch()`. An extension grammar allows the `catch` block to contain a [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
 declared variable with the same name as the `catch`\-bound identifier, but only if the `catch` binding is a simple identifier, not a [destructuring pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
. However, this variable's initialization and assignment would only act on the `catch`\-bound identifier, instead of the upper scope variable, and the behavior could be confusing.

This is listed in Annex B of the spec and hence may not be implemented everywhere. Avoid any name conflicts between the `catch`\-bound identifier and variables declared in the `catch` block.

[Obsolete features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#obsolete_features)

------------------------------------------------------------------------------------------------------------------------------------------

These obsolete features have been entirely removed from JavaScript and can no longer be used as of the indicated version of JavaScript.

### [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp_2)

The following are now properties of `RegExp` instances, no longer of the `RegExp` constructor:

| Property | Description |
| --- | --- |
| [`global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global) | Whether or not to test the regular expression against all possible matches in a string, or only against the first. |
| [`ignoreCase`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase) | Whether or not to ignore case while attempting a match in a string. |
| [`lastIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex) | The index at which to start the next match. |
| [`multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)<br> (also via `RegExp.$*`) | Whether or not to search in strings across multiple lines. |
| [`source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/source) | The text of the pattern. |

The `valueOf()` method is no longer specialized for `RegExp`. It uses [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
, which returns itself.

### [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#function_2)

*   Functions' `arity` property is obsolete. Use [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
     instead.

### [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#object_2)

| Property | Description | Alternative |
| --- | --- | --- |
| `__count__` | Returns the number of enumerable properties directly available on a user-defined object. | [`Object.keys()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) |
| `__parent__` | Points to an object's context. | No direct replacement |
| `__iterator__` | Used with [legacy iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#legacy_generator_and_iterator)<br>. | [`Symbol.iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator)<br> and the new [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) |
| `__noSuchMethod__` | A method called when a non-existent property is called as a method. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |
| `Object.prototype.eval()` | Evaluates a string of JavaScript code in the context of the specified object. | No direct replacement |
| `Object.observe()` | Asynchronously observing the changes to an object. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |
| `Object.unobserve()` | Remove observers. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |
| `Object.getNotifier()` | Create a notifier object that allows you to synthetically trigger a change observable with `Object.observe()`. | No direct replacement |
| `Object.prototype.watch()` | Attach a handler callback to a property that gets called when the property is assigned. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |
| `Object.prototype.unwatch()` | Remove watch handlers on a property. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |

### [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#string_2)

*   Non-standard String generic methods like `String.slice(myStr, 0, 12)`, `String.replace(myStr, /\./g, "!")`, etc. were introduced in Firefox 1.5 (JavaScript 1.6), deprecated in Firefox 53, and removed in Firefox 68. You can use methods on [`String.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#instance_methods)
     together with [`Function.call`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
     instead.
*   `String.prototype.quote` was removed in Firefox 37.
*   The non-standard `flags` parameter in [`String.prototype.search`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)
    , [`String.prototype.match`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
    , and [`String.prototype.replace`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
     is obsolete.

### [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#weakmap)

*   `WeakMap.prototype.clear()` was added in Firefox 20 and removed in Firefox 46. It is not possible to traverse all keys in a [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
    .

### [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#date_2)

*   `Date.prototype.toLocaleFormat()`, which used a format string in the same format expected by the `strftime()` function in C, is obsolete. Use [`toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)
     or [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
     instead.

### [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#array)

*   Non-standard Array generic methods like `Array.slice(myArr, 0, 12)`, `Array.forEach(myArr, myFn)`, etc. have been introduced in Firefox 1.5 (JavaScript 1.6), deprecated in Firefox 68, and removed in Firefox 71. You can use methods on [`Array.prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)
     together with [`Function.call`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
     instead.

| Property | Description | Alternative |
| --- | --- | --- |
| `Array.observe()` | Asynchronously observing changes to Arrays. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |
| `Array.unobserve()` | Remove observers. | [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) |

### [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#number)

*   `Number.toInteger()` is obsolete. Use [`Math.floor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)
    , [`Math.round`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)
    , or other methods instead.

### [Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#proxy)

*   `Proxy.create` and `Proxy.createFunction` are obsolete. Use the [`Proxy()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy)
     constructor instead.
*   The following traps are obsolete:
    *   `hasOwn` ([bug 980565](https://bugzil.la/980565 "External link (opens in new tab)")
        , Firefox 33).
    *   `getEnumerablePropertyKeys` ([bug 783829](https://bugzil.la/783829 "External link (opens in new tab)")
        , Firefox 37)
    *   `getOwnPropertyNames` ([bug 1007334](https://bugzil.la/1007334 "External link (opens in new tab)")
        , Firefox 33)
    *   `keys` ([bug 1007334](https://bugzil.la/1007334 "External link (opens in new tab)")
        , Firefox 33)

### [ParallelArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#parallelarray)

*   `ParallelArray` is obsolete.

### [Statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#statements_2)

*   `for each...in` is obsolete. Use [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
     instead.
*   let blocks and let expressions are obsolete.
*   Expression closures (`function () 1` as a shorthand of `function () { return 1; }`) are obsolete. Use regular [`functions`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)
     or [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
     instead.

### [Acquiring source text](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#acquiring_source_text)

The `toSource()` methods of arrays, numbers, strings, etc. and the `uneval()` global function are obsolete. Use [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
, or write your own serialization method instead.

### [Legacy generator and iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#legacy_generator_and_iterator)

Legacy generator function statements and legacy generator function expressions are removed. The legacy generator function syntax reuses the `function` keyword, which automatically becomes a generator function when there are one or more `yield` expressions in the body — this is now a syntax error. Use [`function*` statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)
 and [`function*` expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)
 instead.

Array comprehensions and generator comprehensions are removed.

Firefox, prior to version 26, implemented another iterator protocol that is similar to the standard [Iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
. An object is a legacy iterator when it implements a `next()` method, which produces a value on each call and throws a `StopIteration` object at the end of iteration. This legacy iterator protocol differs from the standard iterator protocol:

*   The value was returned directly as the return value of calls to `next()`, instead of the `value` property of the `IteratorResult` object.
*   Iteration termination was expressed by throwing a `StopIteration` object, instead of through the `done` property of the `IteratorResult` object.

This feature, along with the `StopIteration` global constructor, was removed in Firefox 58+. For future-facing usages, consider using [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
 loops and the [iterator protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)
.

### [Sharp variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#sharp_variables)

Sharp variables are obsolete. To create circular structures, use temporary variables instead.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/deprecated_and_obsolete_features/index.md?plain=1 "Folder: en-us/web/javascript/reference/deprecated_and_obsolete_features (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FDeprecated_and_obsolete_features&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fdeprecated_and_obsolete_features%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FDeprecated_and_obsolete_features%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fdeprecated_and_obsolete_features%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
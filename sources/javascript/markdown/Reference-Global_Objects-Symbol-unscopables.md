*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#mdn-search)
    

Symbol.unscopables
==================

Deprecated

Avoid using this feature in new projects. JavaScript strict mode prohibits the `with` statement. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring "The destructuring assignment syntax is a JavaScript expression that unpacks values from arrays, or properties from objects, into distinct variables.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Symbol.unscopables`** static data property represents the [well-known symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#well-known_symbols)
 `Symbol.unscopables`. The [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
 statement looks up this symbol on the scope object for a property containing a collection of properties that should not become bindings within the `with` environment.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#try_it)

---------------------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#value)

-------------------------------------------------------------------------------------------------------------------

The well-known symbol `Symbol.unscopables`.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#description)

-------------------------------------------------------------------------------------------------------------------------------

The `[Symbol.unscopables]` symbol (accessed via `Symbol.unscopables`) can be defined on any object to exclude property names from being exposed as lexical variables in [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
 environment bindings. Note that when using [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, `with` statements are not available, and this symbol is likely not needed.

Setting a property of the `[Symbol.unscopables]` object to `true` (or any [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
 value) will make the corresponding property of the `with` scope object _unscopable_ and therefore won't be introduced to the `with` body scope. Setting a property to `false` (or any [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 value) will make it _scopable_ and thus appear as lexical scope variables.

When deciding whether `x` is unscopable, the entire prototype chain of the `[Symbol.unscopables]` property is looked up for a property called `x`. This means if you declared `[Symbol.unscopables]` as a plain object, `Object.prototype` properties like [`toString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 would become unscopable as well, which may cause backward incompatibility for legacy code assuming those properties are normally scoped (see [an example below](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#avoid_using_a_non-null-prototype_object_as_symbol.unscopables)
). You are advised to make your custom `[Symbol.unscopables]` property have `null` as its prototype, like [`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)
 does.

This protocol is also utilized by DOM APIs, such as [`Element.prototype.append()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/append)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Scoping in with statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#scoping_in_with_statements)

The following code works fine in ES5 and below. However, in ECMAScript 2015, the [`Array.prototype.values()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
 method was introduced. That means that inside a `with` environment, "values" would now be the `Array.prototype.values()` method and not the variable outside the `with` statement.

The code containing `with (values)` caused some websites to malfunction in Firefox when `Array.prototype.values()` was added ([Firefox Bug 883914](https://bugzil.la/883914 "External link (opens in new tab)")
). Furthermore, this implies that any future array method addition may be breaking if it implicitly changes the `with` scope. Therefore, the `[Symbol.unscopables]` symbol was introduced and implemented on `Array` as [`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)
 to prevent some of the Array methods being scoped into the `with` statement.

### [Unscopables in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#unscopables_in_objects)

You can also set `[Symbol.unscopables]` for your own objects.

### [Avoid using a non-null-prototype object as `[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#avoid_using_a_non-null-prototype_object_as_symbol.unscopables)

Declaring `[Symbol.unscopables]` as a plain object without eliminating its prototype may cause subtle bugs. Consider the following code working before `[Symbol.unscopables]`:

To preserve backward compatibility, you decided to add a `[Symbol.unscopables]` property when adding more properties to `character`. You may naïvely do it like:

However, the code above now breaks:

This is because when looking up `character[Symbol.unscopables].toString`, it returns [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
, which is a truthy value, thus making the `toString()` call in the `with()` statement reference `globalThis.toString()` instead — and because it's called without a [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, `this` is `undefined`, making it return `[object Undefined]`.

Even when the method is not overridden by `character`, making it unscopable will change the value of `this`.

To fix this, always make sure `[Symbol.unscopables]` only contains properties you wish to be unscopable, without `Object.prototype` properties.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-symbol.unscopables](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-symbol.unscopables) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)
    
*   [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
    
*   [`Element.prototype.append()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/append)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/symbol/unscopables/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/symbol/unscopables (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSymbol%2Funscopables&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fsymbol%2Funscopables%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSymbol%2Funscopables%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fsymbol%2Funscopables%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4fcf79b60471db6f148fa4ba36f2cdeafbbeb70%0A*+Document+last+modified%3A+2025-10-30T21%3A49%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
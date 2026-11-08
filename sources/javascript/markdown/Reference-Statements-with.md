*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#mdn-search)
    

with
====

Deprecated

Avoid using this feature in new projects. JavaScript strict mode prohibits the `with` statement. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [Destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring "The destructuring assignment syntax is a JavaScript expression that unpacks values from arrays, or properties from objects, into distinct variables.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Note:** Use of the `with` statement is not recommended, as it may be the source of confusing bugs and compatibility issues, makes optimization impossible, and is forbidden in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
. The recommended alternative is to assign the object whose properties you want to access to a temporary variable.

The **`with`** statement extends the scope chain for a statement.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#syntax)

---------------------------------------------------------------------------------------------------

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#expression)

Adds the given expression to the scope chain used when evaluating the statement. The parentheses around the expression are required.

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#statement)

Any statement. To execute multiple statements, use a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 statement (`{ ... }`) to group those statements.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#description)

-------------------------------------------------------------------------------------------------------------

There are two types of identifiers: a _qualified_ identifier and an _unqualified_ identifier. An unqualified identifier is one that does not indicate where it comes from.

Normally, an unqualified identifier is resolved by searching the scope chain for a variable with that name, while a qualified identifier is resolved by searching the prototype chain of an object for a property with that name.

One exception to this is the [global object](https://developer.mozilla.org/en-US/docs/Glossary/Global_object)
, which sits on top of the scope chain, and whose properties automatically become global variables that can be referred to without qualifiers.

The `with` statement adds the given object to the head of this scope chain during the evaluation of its statement body. Every unqualified name would first be searched within the object (through an [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
 check) before searching in the upper scope chain.

Note that if the unqualified reference refers to a method of the object, the method is called with the object as its `this` value.

The object may have a [`[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables)
 property, which defines a list of properties that should not be added to the scope chain (for backward compatibility). See the [`Symbol.unscopables`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables)
 documentation for more information.

The reasons to use a `with` statement include saving one temporary variable and reducing file size by avoiding repeating a lengthy object reference. However, there are far more reasons why `with` statements are not desirable:

*   Performance: The `with` statement forces the specified object to be searched first for all name lookups. Therefore, all identifiers that aren't members of the specified object will be found more slowly in a `with` block. Moreover, the optimizer cannot make any assumptions about what each unqualified identifier refers to, so it must repeat the same property lookup every time the identifier is used.
    
*   Readability: The `with` statement makes it hard for a human reader or JavaScript compiler to decide whether an unqualified name will be found along the scope chain, and if so, in which object. For example:
    
    If you look just at the definition of `f`, it's impossible to tell what the `x` in the `with` body refers to. Only when `f` is called can `x` be determined to be `o.x` or `f`'s first formal parameter. If you forget to define `x` in the object you pass as the second parameter, you won't get an error — instead you'll just get unexpected results. It's also unclear what the actual intent of such code would be.
    
*   Forward compatibility: Code using `with` may not be forward compatible, especially when used with something other than a plain object, which may gain more properties in the future. Consider this example:
    
    If you call `f([1, 2, 3], obj)` in an ECMAScript 5 environment, the `values` reference inside the `with` statement will resolve to `obj`. However, ECMAScript 2015 introduces a [`values`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/values)
     property on `Array.prototype` (so it will be available on every array). So, after upgrading the environment, the `values` reference inside the `with` statement resolves to `[1, 2, 3].values` instead, and is likely to cause bugs.
    
    In this particular example, `values` is defined as unscopable through [`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)
    , so it still correctly resolves to the `values` parameter. If it were not defined as unscopable, one can see how this would be a difficult issue to debug.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#examples)

-------------------------------------------------------------------------------------------------------

### [Using the with statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#using_the_with_statement)

The following `with` statement specifies that the [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
 object is the default object. The statements following the `with` statement refer to the [`PI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI)
 property and the [`cos`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)
 and [`sin`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin)
 methods, without specifying an object. JavaScript assumes the `Math` object for these references.

### [Avoiding the with statement by destructuring properties into the current scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#avoiding_the_with_statement_by_destructuring_properties_into_the_current_scope)

You can usually avoid using `with` through [property destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)
. Here we create an extra block to mimic the behavior of `with` creating an extra scope — but in actual usage, this block can usually be omitted.

### [Avoiding the with statement by using an IIFE](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#avoiding_the_with_statement_by_using_an_iife)

If you're producing an expression that must reuse a long-named reference multiple times, and your goal is to eliminate that lengthy name within your expression, you can wrap the expression in an [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 and provide the long name as an argument.

### [Creating dynamic namespaces using the with statement and a proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#creating_dynamic_namespaces_using_the_with_statement_and_a_proxy)

`with` will transform every variable lookup to a property lookup, while [Proxies](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 allow trapping every property lookup call. You can create a dynamic namespace by combining them.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-with-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-with-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with#see_also)

-------------------------------------------------------------------------------------------------------

*   [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
    
*   [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    
*   [`Symbol.unscopables`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/unscopables)
    
*   [`Array.prototype[Symbol.unscopables]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Symbol.unscopables)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/with/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/with (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwith&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fwith%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwith%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fwith%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
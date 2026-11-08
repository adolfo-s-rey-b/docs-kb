*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#mdn-search)
    

new.target
==========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`new.target`** meta-property lets you detect whether a function or constructor was called using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator. In constructors and functions invoked using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator, `new.target` returns a reference to the constructor or function that `new` was called upon. In normal function calls, `new.target` is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#try_it)

--------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#syntax)

--------------------------------------------------------------------------------------------------------

### [Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#value)

`new.target` is guaranteed to be a constructable function value or `undefined`.

*   In class constructors, it refers to the class that `new` was called upon, which may be a subclass of the current constructor, because subclasses transitively call the superclass's constructor through [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    .
*   In ordinary functions, if the function is constructed directly with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    , `new.target` refers to the function itself. If the function is called without `new`, `new.target` is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    . Functions can be used as the base class for [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
    , in which case `new.target` may refer to the subclass.
*   If a constructor (class or function) is called via [`Reflect.construct()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/construct)
    , then `new.target` refers to the value passed as `newTarget` (which defaults to `target`).
*   In [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
    , `new.target` is inherited from the surrounding scope. If the arrow function is not defined within another class or function which has a `new.target` [binding](https://developer.mozilla.org/en-US/docs/Glossary/Binding)
    , then a syntax error is thrown.
*   In [static initialization blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks)
    , `new.target` is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    .

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#description)

------------------------------------------------------------------------------------------------------------------

The `new.target` syntax consists of the keyword `new`, a dot, and the identifier `target`. Because `new` is a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
, not an identifier, this is not a [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
, but a special expression syntax.

The `new.target` meta-property is available in all function/class bodies; using `new.target` outside of functions or classes is a syntax error.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#examples)

------------------------------------------------------------------------------------------------------------

### [new.target in function calls](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#new.target_in_function_calls)

In normal function calls (as opposed to constructor function calls), `new.target` is [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
. This lets you detect whether a function was called with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 as a constructor.

### [new.target in constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#new.target_in_constructors)

In class constructors, `new.target` refers to the constructor that was directly invoked by `new`. This is also the case if the constructor is in a parent class and was delegated from a child constructor. `new.target` points to the class that `new` was called upon. For example, when `b` was initialized using `new B()`, the name of `B` was printed; and similarly, in case of `a`, the name of class `A` was printed.

### [new.target using Reflect.construct()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#new.target_using_reflect.construct)

Before [`Reflect.construct()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/construct)
 or classes, it was common to implement inheritance by passing the value of [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
, and letting the base constructor mutate it.

However, [`call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
 and [`apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 actually _call_ the function instead of _constructing_ it, so `new.target` has value `undefined`. This means that if `Base()` checks whether it's constructed with `new`, an error will be thrown, or it may behave in other unexpected ways. For example, you can't extend [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/Map)
 this way, because the `Map()` constructor cannot be called without `new`.

All built-in constructors directly construct the entire prototype chain of the new instance by reading `new.target.prototype`. So to make sure that (1) `Base` is constructed with `new`, and (2) `new.target` points to the subclass instead of `Base` itself, we need to use [`Reflect.construct()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/construct)
.

**Note:** In fact, due to the lack of `Reflect.construct()`, it is not possible to properly subclass built-ins (like [`Error` subclassing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#custom_error_types)
) when transpiling to pre-ES6 code.

However, if you are writing ES6 code, prefer using classes and `extends` instead, as it's more readable and less error-prone.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-built-in-function-objects](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-built-in-function-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target#see_also)

------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    
*   [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/new.target/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/new.target (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnew.target&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnew.target%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnew.target%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnew.target%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
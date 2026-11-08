*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#mdn-search)
    

Function.prototype.bind()
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`bind()`** method of [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 instances creates a new function that, when called, calls this function with its `this` keyword set to the provided value, and a given sequence of arguments preceding any provided when the new function is called.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#try_it)

----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#syntax)

----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#parameters)

[`thisArg`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#thisarg)

The value to be passed as the `this` parameter to the target function `func` when the bound function is called. If the function is not in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 and [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 will be replaced with the global object, and primitive values will be converted to objects. The value is ignored if the bound function is constructed using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator.

[`arg1`, …, `argN` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#arg1)

Arguments to prepend to arguments provided to the bound function when invoking `func`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#return_value)

A copy of the given function with the specified `this` value, and initial arguments (if provided).

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#description)

--------------------------------------------------------------------------------------------------------------------------

The `bind()` function creates a new _bound function_. Calling the bound function generally results in the execution of the function it wraps, which is also called the _target function_. The bound function will store the parameters passed — which include the value of `this` and the first few arguments — as its internal state. These values are stored in advance, instead of being passed at call time. You can generally see `const boundFn = fn.bind(thisArg, arg1, arg2)` as being equivalent to `const boundFn = (...restArgs) => fn.call(thisArg, arg1, arg2, ...restArgs)` for the effect when it's called (but not when `boundFn` is constructed).

A bound function can be further bound by calling `boundFn.bind(thisArg, /* more args */)`, which creates another bound function `boundFn2`. The newly bound `thisArg` value is ignored, because the target function of `boundFn2`, which is `boundFn`, already has a bound `this`. When `boundFn2` is called, it would call `boundFn`, which in turn calls `fn`. The arguments that `fn` ultimately receives are, in order: the arguments bound by `boundFn`, arguments bound by `boundFn2`, and the arguments received by `boundFn2`.

A bound function may also be constructed using the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator if its target function is constructable. Doing so acts as though the target function had instead been constructed. The prepended arguments are provided to the target function as usual, while the provided `this` value is ignored (because construction prepares its own `this`, as seen by the parameters of [`Reflect.construct`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect/construct)
). If the bound function is directly constructed, [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
 will be the target function instead. (That is, the bound function is transparent to `new.target`.)

However, because a bound function does not have the [`prototype`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/prototype)
 property, it cannot be used as a base class for [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
.

When using a bound function as the right-hand side of [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
, `instanceof` would reach for the target function (which is stored internally in the bound function) and read its `prototype` instead.

The bound function has the following properties:

[`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)

The `length` of the target function minus the number of arguments being bound (not counting the `thisArg` parameter), with 0 being the minimum value.

[`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/name)

The `name` of the target function plus a `"bound "` prefix.

The bound function also inherits the [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 of the target function. However, it doesn't have other own properties of the target function (such as [static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 if the target function is a class).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#examples)

--------------------------------------------------------------------------------------------------------------------

### [Creating a bound function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#creating_a_bound_function)

The most common use of `bind()` is to make a function that, no matter how it is called, is called with a particular `this` value.

A common mistake for new JavaScript programmers is to extract a method from an object, then to later call that function and expect it to use the original object as its `this` (e.g., by using the method in callback-based code).

Without special care, however, the original object is usually lost. Creating a bound function from the function, using the original object, neatly solves this problem:

**Note:** If you run this example in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
, the `this` parameter of `retrieveX` will be bound to `undefined` instead of `globalThis`, causing the `retrieveX()` call to fail.

If you run this example in an ECMAScript module, top-level `this` will be bound to `undefined` instead of `globalThis`, causing the `this.x = 9` assignment to fail.

If you run this example in a Node CommonJS module, top-level `this` will be bound to `module.exports` instead of `globalThis`. However, the `this` parameter of `retrieveX` will still be bound to `globalThis` in non-strict mode and to `undefined` in strict mode. Therefore, in non-strict mode (the default), the `retrieveX()` call will return `undefined` because `this.x = 9` is writing to a different object (`module.exports`) from what `getX` is reading from (`globalThis`).

In fact, some built-in "methods" are also getters that return bound functions — one notable example being [`Intl.NumberFormat.prototype.format()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/format#using_format_with_map)
, which, when accessed, returns a bound function that you can directly pass as a callback.

### [Partially applied functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#partially_applied_functions)

Another use of `bind()` is to make a function with pre-specified initial arguments.

These arguments (if any) follow the provided `this` value and are then inserted at the start of the arguments passed to the target function, followed by whatever arguments are passed to the bound function at the time it is called.

### [With setTimeout()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#with_settimeout)

By default, within [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
, the `this` keyword will be set to [`globalThis`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis)
, which is [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 in browsers. When working with class methods that require `this` to refer to class instances, you may explicitly bind `this` to the callback function, in order to maintain the instance.

You can also use [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 for this purpose.

### [Bound functions used as constructors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#bound_functions_used_as_constructors)

Bound functions are automatically suitable for use with the [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 operator to construct new instances created by the target function. When a bound function is used to construct a value, the provided `this` is ignored. However, provided arguments are still prepended to the constructor call.

Note that you need not do anything special to create a bound function for use with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. [`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)
, [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 etc. all work as expected, as if the constructor was never bound. The only difference is that it can no longer be used for [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
.

The corollary is that you need not do anything special to create a bound function to be called plainly, even if you would rather require the bound function to only be called using [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. If you call it without `new`, the bound `this` is suddenly not ignored.

If you wish to restrict a bound function to only be callable with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, or only be callable without `new`, the target function must enforce that restriction, such as by checking `new.target !== undefined` or using a [class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
 instead.

### [Binding classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#binding_classes)

Using `bind()` on classes preserves most of the class's semantics, except that all static own properties of the current class are lost. However, because the prototype chain is preserved, you can still access static properties inherited from the parent class.

### [Transforming methods to utility functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#transforming_methods_to_utility_functions)

`bind()` is also helpful in cases where you want to transform a method which requires a specific `this` value to a plain utility function that accepts the previous `this` parameter as a normal parameter. This is similar to how general-purpose utility functions work: instead of calling `array.map(callback)`, you use `map(array, callback)`, which allows you to use `map` with array-like objects that are not arrays (for example, [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
) without mutating `Object.prototype`.

Take [`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
, for example, which you want to use for converting an array-like object to a real array. You could create a shortcut like this:

Note that you can't save `slice.call` and call it as a plain function, because the `call()` method also reads its `this` value, which is the function it should call. In this case, you can use `bind()` to bind the value of `this` for `call()`. In the following piece of code, `slice()` is a bound version of [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
, with the `this` value bound to [`Array.prototype.slice()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
. This means that additional `call()` calls can be eliminated:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function.prototype.bind](https://tc39.es/ecma262/multipage/fundamental-objects.html#sec-function.prototype.bind) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Function.prototype.bind` in `core-js`](https://core-js.io/docs/features/ecmascript/function "External link (opens in new tab)")
    
*   [`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
    
*   [`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)
    
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/function/bind/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/function/bind (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fbind&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fbind%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fbind%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ffunction%2Fbind%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#mdn-search)
    

null
====

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`null`** keyword refers to the [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#null_type)
 [primitive value](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
, which represents the intentional absence of any object value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#try_it)

--------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#syntax)

--------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#description)

------------------------------------------------------------------------------------------------------------

The keyword `null` is a literal for the `null` value. Unlike [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
, which is a global variable, `null` is not an identifier but a syntax keyword.

`null` has the following behaviors:

*   Like `undefined`, accessing any property on `null` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     instead of returning `undefined` or searching prototype chains.
*   Like `undefined`, `null` is treated as [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
     for boolean operations, and [nullish](https://developer.mozilla.org/en-US/docs/Glossary/Nullish)
     for [nullish coalescing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
     and [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
    .
*   The [`typeof null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null)
     result is `"object"`. This is a bug in JavaScript that cannot be fixed due to backward compatibility.
*   Unlike `undefined`, [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
     can represent `null` faithfully.

JavaScript is unique to have two nullish values: `null` and `undefined`. Semantically, their difference is very minor: `undefined` represents the absence of a value, while `null` represents the absence of an _object_. For example, the end of the [prototype chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain)
 is `null` because the prototype chain is composed of objects; [`document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
 returns `null` if it doesn't match, because had it matched, the result would be an object. If you are designing an API, you should likely accept `null` and `undefined` as equivalent inputs, because many codebases have stylistic rules about when to use `null` or `undefined` by default.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#examples)

------------------------------------------------------------------------------------------------------

### [Difference between `null` and `undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#difference_between_null_and_undefined)

When checking for `null` or `undefined`, beware of the [differences between equality (==) and identity (===) operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
, as the former performs type-conversion.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-null-value](https://tc39.es/ecma262/multipage/overview.html#sec-null-value) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#see_also)

------------------------------------------------------------------------------------------------------

*   [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
    
*   [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
    
*   [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 28, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/null/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/null (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnull&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnull%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnull%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Fnull%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb94841f0e5f0578297954ef4276a4e2d319a8720%0A*+Document+last+modified%3A+2025-10-28T20%3A03%3A18.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
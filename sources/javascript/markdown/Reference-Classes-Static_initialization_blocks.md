*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#mdn-search)
    

Static initialization blocks
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Static initialization blocks** are declared within a [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
. They contain statements to be evaluated during class initialization. This permits more flexible initialization logic than [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 properties, such as using `try...catch` or setting multiple fields from a single value. Initialization is performed in the context of the current class declaration, with access to private state, which allows the class to share information of its private elements with other classes or functions declared in the same scope (analogous to "friend" classes in C++).

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#try_it)

------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#syntax)

------------------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#description)

----------------------------------------------------------------------------------------------------------------------------------

Without static initialization blocks, complex static initialization might be achieved by calling a static method after the class declaration:

However, this approach exposes an implementation detail (the `init()` method) to the user of the class. On the other hand, any initialization logic declared outside the class does not have access to private static fields. Static initialization blocks allow arbitrary initialization logic to be declared within the class and executed during class evaluation.

A [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
 can have any number of `static {}` initialization blocks in its class body. These are [evaluated](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#evaluation_order)
, along with any interleaved static field initializers, in the order they are declared. Any static initialization of a super class is performed first, before that of its sub classes.

The scope of the variables declared inside the static block is local to the block. This includes `var`, `function`, `const`, and `let` declarations. `var` declarations will not be hoisted out of the static block.

The `this` inside a static block refers to the constructor object of the class. `super.property` can be used to access static properties of the super class. Note however that it is a syntax error to call [`super()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 in a class static initialization block, or to use the [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
 object.

The statements are evaluated synchronously. You cannot use [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 or [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 in this block. (Think of the initialization statements as being implicitly wrapped in a function.)

The scope of the static block is nested _within_ the lexical scope of the class body, and can access [private names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
 declared within the class without causing a syntax error.

[Static field](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
 initializers and static initialization blocks are evaluated one-by-one. The initialization block can refer to field values above it, but not below it. All static methods are added beforehand and can be accessed, although calling them may not behave as expected if they refer to fields below the current block.

**Note:** This is more important with [private static fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
, because accessing a non-initialized private field throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, even if the private field is declared below. (If the private field is not declared, it would be an early [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.)

A static initialization block may not have decorators (the class itself may).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Multiple blocks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#multiple_blocks)

The code below demonstrates a class with static initialization blocks and interleaved static field initializers. The output shows that the blocks and fields are evaluated in execution order.

Note that any static initialization of a super class is performed first, before that of its sub classes.

### [Using this and super](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#using_this_and_super)

The `this` inside a static block refers to the constructor object of the class. This code shows how to access a public static field.

The [`super.property`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 syntax can be used inside a `static` block to reference static properties of a super class.

### [Access to private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#access_to_private_elements)

This example below shows how access can be granted to a private instance field of a class from an object outside the class (example from the [v8.dev blog](https://v8.dev/features/class-static-initializer-blocks#access-to-private-fields "External link (opens in new tab)")
):

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ClassStaticBlock](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-ClassStaticBlock) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [Class static initialization blocks](https://v8.dev/features/class-static-initializer-blocks "External link (opens in new tab)")
     on v8.dev (2021)
*   [ES2022 feature: class static initialization blocks](https://2ality.com/2021/09/class-static-block.html "External link (opens in new tab)")
     by Dr. Axel Rauschmayer (2021)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Static_initialization_blocks/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/static_initialization_blocks/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/static_initialization_blocks (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FStatic_initialization_blocks&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fstatic_initialization_blocks%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FStatic_initialization_blocks%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fstatic_initialization_blocks%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
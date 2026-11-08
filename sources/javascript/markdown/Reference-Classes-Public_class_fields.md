*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#mdn-search)
    

Public class fields
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Public fields** are writable, enumerable, and configurable properties defined on each class instance or class constructor.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#syntax)

---------------------------------------------------------------------------------------------------------------

There are some additional syntax restrictions:

*   The name of a static property (field or method) cannot be `prototype`.
*   The name of a class field (static or instance) cannot be `constructor`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#description)

-------------------------------------------------------------------------------------------------------------------------

This page introduces public instance fields in detail.

*   For public static fields, see [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
    .
*   For private fields, see [private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    .
*   For public methods, see [method definitions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions)
    .
*   For public accessors, see [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
     and [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    .

Public instance fields exist on every created instance of a class. By declaring a public field, you can ensure the field is always present, and the class definition is more self-documenting.

Public instance fields are added to the instance either at construction time in the base class (before the constructor body runs), or just after `super()` returns in a subclass. Fields without initializers are initialized to `undefined`. Like properties, field names may be computed.

Computed field names are only evaluated once, at [class definition time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#evaluation_order)
. This means that each class always has a fixed set of field names, and two instances cannot have different field names via computed names. The `this` value in the computed expression is the `this` surrounding the class definition, and referring to the class's name is a [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
 because the class is not initialized yet. [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 and [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 work as expected in this expression.

In the field initializer, [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 refers to the class instance under construction, and [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
 refers to the `prototype` property of the base class, which contains the base class's instance methods, but not its instance fields.

The field initializer expression is evaluated each time a new instance is created. (Because the `this` value is different for each instance, the initializer expression can access instance-specific properties.)

The expression is evaluated synchronously. You cannot use [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 or [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 in the initializer expression. (Think of the initializer expression as being implicitly wrapped in a function.)

Because instance fields of a class are added before the respective constructor runs, you can access the fields' values within the constructor. However, because instance fields of a derived class are defined after `super()` returns, the base class's constructor does not have access to the derived class's fields.

Fields are added one-by-one. Field initializers can refer to field values above them, but not below them. All instance and static methods are added beforehand and can be accessed, although calling them may not behave as expected if they refer to fields below the one being initialized.

**Note:** This is more important with [private fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
, because accessing a non-initialized private field throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, even if the private field is declared below. (If the private field is not declared, it would be an early [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.)

Because class fields are added using the [`[[DefineOwnProperty]]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/Proxy/defineProperty)
 semantic (which is essentially [`Object.defineProperty()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
), field declarations in derived classes do not invoke setters in the base class. This behavior differs from using `this.field = …` in the constructor.

**Note:** Before the class fields specification was finalized with the `[[DefineOwnProperty]]` semantic, most transpilers, including [Babel](https://babeljs.io/ "External link (opens in new tab)")
 and [tsc](https://www.typescriptlang.org/ "External link (opens in new tab)")
, transformed class fields to the `DerivedWithConstructor` form, which has caused subtle bugs after class fields were standardized.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#examples)

-------------------------------------------------------------------------------------------------------------------

### [Using class fields](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#using_class_fields)

Class fields cannot depend on arguments of the constructor, so field initializers usually evaluate to the same value for each instance (unless the same expression can evaluate to different values each time, such as [`Math.random()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)
 or object initializers).

However, even declaring an empty class field is beneficial, because it indicates the existence of the field, which allows type checkers as well as human readers to statically analyze the shape of the class.

The code above seems repetitive, but consider the case where `this` is dynamically mutated: the explicit field declaration makes it clear which fields will definitely be present on the instance.

Because initializers are evaluated after the base class has executed, you can access properties created by the base class constructor.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-FieldDefinition](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-FieldDefinition) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
     guide
*   [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
    
*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [The semantics of all JS class elements](https://rfrn.org/~shu/2018/05/02/the-semantics-of-all-js-class-elements.html "External link (opens in new tab)")
     by Shu-yu Guo (2018)
*   [Public and private class fields](https://v8.dev/features/class-fields "External link (opens in new tab)")
     on v8.dev (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/classes/public_class_fields/index.md?plain=1 "Folder: en-us/web/javascript/reference/classes/public_class_fields (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FPublic_class_fields&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fpublic_class_fields%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2FPublic_class_fields%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fclasses%2Fpublic_class_fields%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
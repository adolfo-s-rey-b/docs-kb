*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#mdn-search)
    

Expressions and operators
=========================

This chapter documents all the JavaScript language operators, expressions and keywords.

[Expressions and operators by category](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#expressions_and_operators_by_category)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

For an alphabetical listing see the sidebar on the left.

### [Primary expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#primary_expressions)

Basic keywords and general expressions in JavaScript. These expressions have the highest precedence (higher than [operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
).

[`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

The `this` keyword refers to a special property of an execution context.

[Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#literals)

Basic `null`, boolean, number, and string literals.

[`[]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

Array initializer/literal syntax.

[`{}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)

Object initializer/literal syntax.

[`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function)

The `function` keyword defines a function expression.

[`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/class)

The `class` keyword defines a class expression.

[`function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function*)

The `function*` keyword defines a generator function expression.

[`async function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function)

The `async function` defines an async function expression.

[`async function*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/async_function*)

The `async function*` keywords define an async generator function expression.

[`/ab+c/i`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

Regular expression literal syntax.

[`` `string` ``](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

Template literal syntax.

[`( )`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)

Grouping operator.

### [Left-hand-side expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#left-hand-side_expressions)

Left values are the destination of an assignment.

[Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)

Member operators provide access to a property or method of an object (`object.property` and `object["property"]`).

[`?.`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

The optional chaining operator returns `undefined` instead of causing an error if a reference is [nullish](https://developer.mozilla.org/en-US/docs/Glossary/Nullish)
 ([`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
).

[`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

The `new` operator creates an instance of a constructor.

[`new.target`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new.target)

In constructors, `new.target` refers to the constructor that was invoked by [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
.

[`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta)

An object exposing context-specific metadata to a JavaScript module.

[`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)

The `super` keyword calls the parent constructor or allows accessing properties of the parent object.

[`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import)

The `import()` syntax allows loading a module asynchronously and dynamically into a potentially non-module environment.

[`import.defer()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/defer)

The `import.defer()` syntax loads a module dynamically, deferring synchronous evaluation until the returned namespace's properties are accessed.

[`import.source()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import/source)

The `import.source()` syntax results in an object representing the module's compiled source, without loading its dependencies, linking it, or evaluating it.

### [Increment and decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#increment_and_decrement)

Postfix/prefix increment and postfix/prefix decrement operators.

[`A++`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)

Postfix increment operator.

[`A--`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)

Postfix decrement operator.

[`++A`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)

Prefix increment operator.

[`--A`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)

Prefix decrement operator.

### [Unary operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#unary_operators)

A unary operation is an operation with only one operand.

[`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)

The `delete` operator deletes a property from an object.

[`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)

The `void` operator evaluates an expression and discards its return value.

[`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

The `typeof` operator determines the type of a given object.

[`+`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)

The unary plus operator converts its operand to Number type.

[`-`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)

The unary negation operator converts its operand to Number type and then negates it.

[`~`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT)

Bitwise NOT operator.

[`!`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)

Logical NOT operator.

[`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)

Pause and resume an async function and wait for the promise's fulfillment/rejection.

### [Arithmetic operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#arithmetic_operators)

Arithmetic operators take numerical values (either literals or variables) as their operands and return a single numerical value.

[`**`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)

Exponentiation operator.

[`*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)

Multiplication operator.

[`/`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)

Division operator.

[`%`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)

Remainder operator.

[`+`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
 (Plus)

Addition operator.

[`-`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)

Subtraction operator.

### [Relational operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#relational_operators)

A comparison operator compares its operands and returns a boolean value based on whether the comparison is true.

[`<`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)
 (Less than)

Less than operator.

[`>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than)
 (Greater than)

Greater than operator.

[`<=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)

Less than or equal operator.

[`>=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal)

Greater than or equal operator.

[`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)

The `instanceof` operator determines whether an object is an instance of another object.

[`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)

The `in` operator determines whether an object has a given property.

**Note:** `=>` is [not an operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#what_are_operators)
, but the notation for [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
.

### [Equality operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators)

The result of evaluating an equality operator is always of type boolean based on whether the comparison is true.

[`==`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)

Equality operator.

[`!=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)

Inequality operator.

[`===`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)

Strict equality operator.

[`!==`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)

Strict inequality operator.

### [Bitwise shift operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#bitwise_shift_operators)

Operations to shift all bits of the operand.

[`<<`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift)

Bitwise left shift operator.

[`>>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)

Bitwise right shift operator.

[`>>>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)

Bitwise unsigned right shift operator.

### [Binary bitwise operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_bitwise_operators)

Bitwise operators treat their operands as a set of 32 bits (zeros and ones) and return standard JavaScript numerical values.

[`&`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND)

Bitwise AND.

[`|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR)

Bitwise OR.

[`^`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR)

Bitwise XOR.

### [Binary logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators)

Logical operators implement boolean (logical) values and have [short-circuiting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#short-circuiting)
 behavior.

[`&&`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)

Logical AND.

[`||`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR)

Logical OR.

[`??`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)

Nullish Coalescing Operator.

### [Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#conditional_ternary_operator)

[`(condition ? ifTrue : ifFalse)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)

The conditional operator returns one of two values based on the logical value of the condition.

### [Assignment operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#assignment_operators)

An assignment operator assigns a value to its left operand based on the value of its right operand.

[`=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)

Assignment operator.

[`*=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication_assignment)

Multiplication assignment.

[`/=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division_assignment)

Division assignment.

[`%=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder_assignment)

Remainder assignment.

[`+=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition_assignment)

Addition assignment.

[`-=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction_assignment)

Subtraction assignment

[`<<=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift_assignment)

Left shift assignment.

[`>>=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift_assignment)

Right shift assignment.

[`>>>=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift_assignment)

Unsigned right shift assignment.

[`&=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND_assignment)

Bitwise AND assignment.

[`^=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR_assignment)

Bitwise XOR assignment.

[`|=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR_assignment)

Bitwise OR assignment.

[`**=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation_assignment)

Exponentiation assignment.

[`&&=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND_assignment)

Logical AND assignment.

[`||=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR_assignment)

Logical OR assignment.

[`??=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)

Nullish coalescing assignment.

[`[a, b] = arr`, `{ a, b } = obj`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring)

Destructuring allows you to assign the properties of an array or object to variables using syntax that looks similar to array or object literals.

### [Yield operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#yield_operators)

[`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)

Pause and resume a generator function.

[`yield*`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*)

Delegate to another generator function or iterable object.

### [Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#spread_syntax)

[`...obj`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)

Spread syntax allows an iterable, such as an array or string, to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected. In an object literal, the spread syntax enumerates the properties of an object and adds the key-value pairs to the object being created.

### [Comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#comma_operator)

[`,`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)

The comma operator allows multiple expressions to be evaluated in a single statement and returns the result of the last expression.

[What are operators?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#what_are_operators)

----------------------------------------------------------------------------------------------------------------------

As the [What are statements, declarations, and expressions?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
 section explains, an expression is a fundamental building block that evaluates to a value. Statements, declarations, and expressions can all define specific slots where expressions are accepted. Where an expression contains slots for further nested expressions, the part(s) that are not slots are known as operators.

For example, the syntax for an [addition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
 expression is `expression + expression` (if you read the spec, the operands are called _AdditiveExpression_ and _MultiplicativeExpression_, which are both subsets of _Expression_, but that's the spec's mechanism for defining [precedence and associativity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
 and is irrelevant for our purposes). Apart from the two expression slots, the code entity it introduces is just `+`: the _addition operator_. Similarly, the syntax for a [yield](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
 expression is `yield expression`, so `yield` is known as the operator. In other words, each operator corresponds to an expression.

MDN also regards expressions without slots such as [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 as operators per the definition above, although we nearly always just refer to them as "syntax" or "expression".

An expression does not need to take a fixed number of slots. For example, the array literal expression, `[expression, expression, expression]`, can take an arbitrary number of expression slots. The `[,,]` part might be called an "operator". MDN avoids this usage, but you may see it in functional programming languages like [Haskell](https://www.haskell.org/onlinereport/haskell2010/haskellch3.html "External link (opens in new tab)")
.

The definition of operators gets fuzzier with certain other code entities: what if an expression has a slot that's not an expression, or a code entity combined with an expression does not make an expression? Do we still refer to that code entity as an operator?

*   In the [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
     expression `foo?.bar`, `foo` is an expression, but `bar` must be an identifier and is not evaluated to a value. Do we still regard `?.` as an operator?
*   In the [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
     expression `arg => body`, `body` might be an expression (although it can also be a block body), and `arg` is just an argument list. Do we still regard `=>` as an operator?
*   In the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
     `...foo`, `foo` is an expression, but the whole thing is not an expression because it does not evaluate to a value—it only makes sense in certain other expressions like function calls, array literals, and object literals. Do we still regard `...` as an operator?

The term "operator" is not precisely defined in JavaScript, so MDN does not give a definitive answer. Our approach is to group all these constructs under "Operators" but avoid formally referring to them as operators. Many useful concepts about operators, such as [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
, still apply to them regardless of their exact nature.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-SpreadElement](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-SpreadElement) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-comma-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-comma-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-multiplicative-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-multiplicative-operators) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-LogicalANDExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-LogicalANDExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-relational-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-relational-operators) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-grouping-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-grouping-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-assignment-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-assignment-operators) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-generator-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-generator-function-definitions) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-subtraction-operator-minus](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-subtraction-operator-minus) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-async-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-async-function-definitions) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-generator-function-definitions-runtime-semantics-evaluation](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-generator-function-definitions-runtime-semantics-evaluation) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-this-keyword](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-this-keyword) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-null-value](https://tc39.es/ecma262/multipage/overview.html#sec-null-value) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ArgumentList](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ArgumentList) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-PropertyDefinition](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-PropertyDefinition) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-built-in-function-objects](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-built-in-function-objects) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-property-accessors](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-property-accessors) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-equality-operators](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-equality-operators) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-addition-operator-plus](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-addition-operator-plus) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-CoalesceExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-CoalesceExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-delete-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-delete-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-unary-plus-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-unary-plus-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-FormalParameters](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-FormalParameters) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-signed-right-shift-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-signed-right-shift-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-AssignmentRestProperty](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-AssignmentRestProperty) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-bitwise-not-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-bitwise-not-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ComputedPropertyName](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ComputedPropertyName) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-destructuring-assignment](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-destructuring-assignment) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-destructuring-binding-patterns](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-destructuring-binding-patterns) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-postfix-increment-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-postfix-increment-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-super-keyword](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-super-keyword) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-import-calls](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-import-calls) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-BitwiseORExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-BitwiseORExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-ImportMeta](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-ImportMeta) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-BitwiseANDExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-BitwiseANDExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-object-initializer](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-object-initializer) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-unsigned-right-shift-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-unsigned-right-shift-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-AssignmentRestElement](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-AssignmentRestElement) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-void-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-void-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-YieldExpression](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-YieldExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-function-definitions) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-async-generator-function-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-async-generator-function-definitions) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-logical-not-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-logical-not-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-new-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-new-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-MethodDefinition](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#prod-MethodDefinition) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-OptionalExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-OptionalExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-conditional-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-conditional-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-postfix-decrement-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-postfix-decrement-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-LogicalORExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-LogicalORExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-typeof-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-typeof-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# prod-BitwiseXORExpression](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#prod-BitwiseXORExpression) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-exp-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-exp-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-class-definitions](https://tc39.es/ecma262/multipage/ecmascript-language-functions-and-classes.html#sec-class-definitions) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-unary-minus-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-unary-minus-operator) |
| [ECMAScript® 2027 Language Specification  <br>\# sec-left-shift-operator](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-left-shift-operator) |
| [Source Phase Imports  <br>\# sec-left-hand-side-expressions](https://tc39.es/proposal-source-phase-imports/#sec-left-hand-side-expressions) |
| [HTML  <br>\# import-meta-resolve](https://html.spec.whatwg.org/multipage/webappapis.html#import-meta-resolve) |
| [HTML  <br>\# fetch-a-single-module-script](https://html.spec.whatwg.org/multipage/webappapis.html#fetch-a-single-module-script) |
| [HTML  <br>\# integration-with-the-javascript-module-system](https://html.spec.whatwg.org/multipage/webappapis.html#integration-with-the-javascript-module-system) |
| [Deferred Imports Evaluation  <br>\# sec-left-hand-side-expressions](https://tc39.es/proposal-defer-import-eval/#sec-left-hand-side-expressions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#see_also)

-------------------------------------------------------------------------------------------------

*   [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 15, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff693fdeb65be430fdf3b7fc5cdf44a10a13f2bbf%0A*+Document+last+modified%3A+2026-09-15T05%3A12%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
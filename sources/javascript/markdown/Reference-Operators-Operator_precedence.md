*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#mdn-search)
    

Operator precedence
===================

**Operator precedence** determines how operators are parsed concerning each other. Operators with higher precedence become the operands of operators with lower precedence.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#try_it)

-----------------------------------------------------------------------------------------------------------------

[Precedence and associativity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#precedence_and_associativity)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Consider an expression describable by the representation below, where both `OP1` and `OP2` are fill-in-the-blanks for OPerators.

a OP1 b OP2 c

The combination above has two possible interpretations:

(a OP1 b) OP2 c
a OP1 (b OP2 c)

Which one the language decides to adopt depends on the identity of `OP1` and `OP2`.

If `OP1` and `OP2` have different precedence levels (see the table below), the operator with the higher _precedence_ goes first and associativity does not matter. Observe how multiplication has higher precedence than addition and executed first, even though addition is written first in the code.

Within operators of the same precedence, the language groups them by _associativity_. _Left-associativity_ (left-to-right) means that it is interpreted as `(a OP1 b) OP2 c`, while _right-associativity_ (right-to-left) means it is interpreted as `a OP1 (b OP2 c)`. Assignment operators are right-associative, so you can write:

with the expected result that `a` and `b` get the value 5. This is because the assignment operator returns the value that is assigned. First, `b` is set to 5. Then the `a` is also set to 5 — the return value of `b = 5`, a.k.a. right operand of the assignment.

As another example, the unique exponentiation operator has right-associativity, whereas other arithmetic operators have left-associativity.

Operators are first grouped by precedence, and then, for adjacent operators that have the same precedence, by associativity. So, when mixing division and exponentiation, the exponentiation always comes before the division. For example, `2 ** 3 / 3 ** 2` results in 0.8888888888888888 because it is the same as `(2 ** 3) / (3 ** 2)`.

For prefix unary operators, suppose we have the following pattern:

OP1 a OP2 b

where `OP1` is a prefix unary operator and `OP2` is a binary operator. If `OP1` has higher precedence than `OP2`, then it would be grouped as `(OP1 a) OP2 b`; otherwise, it would be `OP1 (a OP2 b)`.

If the unary operator is on the second operand:

a OP2 OP1 b

Then the binary operator `OP2` must have lower precedence than the unary operator `OP1` for it to be grouped as `a OP2 (OP1 b)`. For example, the following is invalid:

Because `+` has higher precedence than [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
, this would become `(a + yield) 1` — but because `yield` is a [reserved word](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
 in generator functions, this would be a syntax error. Luckily, most unary operators have higher precedence than binary operators and do not suffer from this pitfall.

If we have two prefix unary operators:

OP1 OP2 a

Then the unary operator closer to the operand, `OP2`, must have higher precedence than `OP1` for it to be grouped as `OP1 (OP2 a)`. It's possible to get it the other way and end up with `(OP1 OP2) a`:

Because [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
 has higher precedence than [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
, this would become `(await yield) 1`, which is awaiting an identifier called `yield`, and a syntax error. Similarly, if you have `new !A;`, because `!` has lower precedence than `new`, this would become `(new !) A`, which is obviously invalid. (This code looks nonsensical to write anyway, since `!A` always produces a boolean, not a constructor function.)

For postfix unary operators (namely, `++` and `--`), the same rules apply. Luckily, both operators have higher precedence than any binary operator, so the grouping is always what you would expect. Moreover, because `++` evaluates to a _value_, not a _reference_, you can't chain multiple increments together either.

Operator precedence will be handled _recursively_. For example, consider this expression:

First, we group operators with different precedence by decreasing levels of precedence.

1.  The `**` operator has the highest precedence, so it's grouped first.
2.  Looking around the `**` expression, it has `*` on the right and `+` on the left. `*` has higher precedence, so it's grouped first. `*` and `/` have the same precedence, so we group them together for now.
3.  Looking around the `*`/`/` expression grouped in 2, because `+` has higher precedence than `>>`, the former is grouped.

Within the `*`/`/` group, because they are both left-associative, the left operand would be grouped.

Note that operator precedence and associativity only affect the order of evaluation of _operators_ (the implicit grouping), but not the order of evaluation of _operands_. The operands are always evaluated from left-to-right. The higher-precedence expressions are always evaluated first, and their results are then composed according to the order of operator precedence.

If you are familiar with binary trees, think about it as a [post-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#Post-order,_LRN "External link (opens in new tab)")
.

                /
       ┌────────┴────────┐
echo("left", 4)         \*\*
                ┌────────┴────────┐
        echo("middle", 3)  echo("right", 2)

After all operators have been properly grouped, the binary operators would form a binary tree. Evaluation starts from the outermost group — which is the operator with the lowest precedence (`/` in this case). The left operand of this operator is first evaluated, which may be composed of higher-precedence operators (such as a call expression `echo("left", 4)`). After the left operand has been evaluated, the right operand is evaluated in the same fashion. Therefore, all leaf nodes — the `echo()` calls — would be visited left-to-right, regardless of the precedence of operators joining them.

[Short-circuiting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#short-circuiting)

-------------------------------------------------------------------------------------------------------------------------------------

In the previous section, we said "the higher-precedence expressions are always evaluated first" — this is generally true, but it has to be amended with the acknowledgement of _short-circuiting_, in which case an operand may not be evaluated at all.

Short-circuiting is jargon for conditional evaluation. For example, in the expression `a && (b + c)`, if `a` is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
, then the sub-expression `(b + c)` will not even get evaluated, even if it is grouped and therefore has higher precedence than `&&`. We could say that the logical AND operator (`&&`) is "short-circuited". Along with logical AND, other short-circuited operators include logical OR (`||`), nullish coalescing (`??`), and optional chaining (`?.`).

When evaluating a short-circuited operator, the left operand is always evaluated. The right operand will only be evaluated if the left operand cannot determine the result of the operation.

**Note:** The behavior of short-circuiting is baked in these operators. Other operators would _always_ evaluate both operands, regardless if that's actually useful — for example, `NaN * foo()` will always call `foo`, even when the result would never be something other than `NaN`.

The previous model of a post-order traversal still stands. However, after the left subtree of a short-circuiting operator has been visited, the language will decide if the right operand needs to be evaluated. If not (for example, because the left operand of `||` is already truthy), the result is directly returned without visiting the right subtree.

Consider this case:

Only `C()` is evaluated, despite `&&` having higher precedence. This does not mean that `||` has higher precedence in this case — it's exactly _because_ `(B() && A())` has higher precedence that causes it to be neglected as a whole. If it's re-arranged as:

Then the short-circuiting effect of `&&` would only prevent `B()` from being evaluated, but because `A() && B()` as a whole is `false`, `C()` would still be evaluated.

However, note that short-circuiting does not change the final evaluation outcome. It only affects the evaluation of _operands_, not how _operators_ are grouped — if evaluation of operands doesn't have side effects (for example, logging to the console, assigning to variables, throwing an error), short-circuiting would not be observable at all.

The assignment counterparts of these operators ([`&&=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND_assignment)
, [`||=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR_assignment)
, [`??=`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)
) are short-circuited as well. They are short-circuited in a way that the assignment does not happen at all.

[Table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#table)

---------------------------------------------------------------------------------------------------------------

The following table lists operators in order from highest precedence (18) to lowest precedence (1).

Several general notes about the table:

1.  Not all syntax included here are ["operators" in the strict sense](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#what_are_operators)
    . For example, spread `...` and arrow `=>` are typically not regarded as operators. However, we still included them to show how tightly they bind compared to other operators/expressions.
2.  Some operators have certain operands that require expressions narrower than those produced by higher-precedence operators. For example, the right-hand side of member access `.` (precedence 17) must be an identifier instead of a grouped expression. The left-hand side of arrow `=>` (precedence 2) must be an arguments list or a single identifier instead of some random expression.
3.  Some operators have certain operands that accept expressions wider than those produced by higher-precedence operators. For example, the bracket-enclosed expression of bracket notation `[ … ]` (precedence 17) can be any expression, even comma (precedence 1) joined ones. These operators act as if that operand is "automatically grouped". In this case we will omit the associativity.

| Precedence | Associativity | Individual operators | Notes |
| --- | --- | --- | --- |
| 18: grouping | n/a | [Grouping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)<br>  <br>`(x)` | \[1\] |
| 17: access and call | left-to-right | [Member access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#dot_notation)<br>  <br>`x.y` | \[2\] |
| [Optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)<br>  <br>`x?.y` |
| n/a | [Computed member access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors#bracket_notation)<br>  <br>`x[y]` | \[3\] |
| [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)<br> with argument list  <br>`new x(y)` | \[4\] |
| [Function call](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)<br>  <br>`x(y)` |
| [`import(x)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import) |
| 16: new | n/a | [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)<br> without argument list  <br>`new x` |
| 15: postfix operators | n/a | [Postfix increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)<br>  <br>`x++` | \[5\] |
| [Postfix decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)<br>  <br>`x--` |
| 14: prefix operators | n/a | [Prefix increment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)<br>  <br>`++x` | \[6\] |
| [Prefix decrement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement)<br>  <br>`--x` |
| [Logical NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT)<br>  <br>`!x` |
| [Bitwise NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT)<br>  <br>`~x` |
| [Unary plus](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_plus)<br>  <br>`+x` |
| [Unary negation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unary_negation)<br>  <br>`-x` |
| [`typeof x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) |
| [`void x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void) |
| [`delete x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete) | \[7\] |
| [`await x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) |
| 13: exponentiation | right-to-left | [Exponentiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)<br>  <br>`x ** y` | \[8\] |
| 12: multiplicative operators | left-to-right | [Multiplication](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication)<br>  <br>`x * y` |
| [Division](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division)<br>  <br>`x / y` |
| [Remainder](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder)<br>  <br>`x % y` |
| 11: additive operators | left-to-right | [Addition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)<br>  <br>`x + y` |
| [Subtraction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction)<br>  <br>`x - y` |
| 10: bitwise shift | left-to-right | [Left shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift)<br>  <br>`x << y` |
| [Right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift)<br>  <br>`x >> y` |
| [Unsigned right shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)<br>  <br>`x >>> y` |
| 9: relational operators | left-to-right | [Less than](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than)<br>  <br>`x < y` |
| [Less than or equal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Less_than_or_equal)<br>  <br>`x <= y` |
| [Greater than](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than)<br>  <br>`x > y` |
| [Greater than or equal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Greater_than_or_equal)<br>  <br>`x >= y` |
| [`x in y`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in) |
| [`x instanceof y`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof) |
| 8: equality operators | left-to-right | [Equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)<br>  <br>`x == y` |
| [Inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality)<br>  <br>`x != y` |
| [Strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)<br>  <br>`x === y` |
| [Strict inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality)<br>  <br>`x !== y` |
| 7: bitwise AND | left-to-right | [Bitwise AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND)<br>  <br>`x & y` |
| 6: bitwise XOR | left-to-right | [Bitwise XOR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR)<br>  <br>`x ^ y` |
| 5: bitwise OR | left-to-right | [Bitwise OR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR)<br>  <br>`x \| y` |
| 4: logical AND | left-to-right | [Logical AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND)<br>  <br>`x && y` |
| 3: logical OR, nullish coalescing | left-to-right | [Logical OR](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR)<br>  <br>`x \| y` |
| [Nullish coalescing operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)<br>  <br>`x ?? y` | \[9\] |
| 2: assignment and miscellaneous | right-to-left | [Assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment)<br>  <br>`x = y` | \[10\] |
| [Addition assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition_assignment)<br>  <br>`x += y` |
| [Subtraction assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction_assignment)<br>  <br>`x -= y` |
| [Exponentiation assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation_assignment)<br>  <br>`x **= y` |
| [Multiplication assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Multiplication_assignment)<br>  <br>`x *= y` |
| [Division assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Division_assignment)<br>  <br>`x /= y` |
| [Remainder assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder_assignment)<br>  <br>`x %= y` |
| [Left shift assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift_assignment)<br>  <br>`x <<= y` |
| [Right shift assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift_assignment)<br>  <br>`x >>= y` |
| [Unsigned right shift assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift_assignment)<br>  <br>`x >>>= y` |
| [Bitwise AND assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_AND_assignment)<br>  <br>`x &= y` |
| [Bitwise XOR assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR_assignment)<br>  <br>`x ^= y` |
| [Bitwise OR assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR_assignment)<br>  <br>`x \|= y` |
| [Logical AND assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND_assignment)<br>  <br>`x &&= y` |
| [Logical OR assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR_assignment)<br>  <br>`x \|= y` |
| [Nullish coalescing assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_assignment)<br>  <br>`x ??= y` |
| right-to-left | [Conditional (ternary) operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator)<br>  <br>`x ? y : z` | \[11\] |
| right-to-left | [Arrow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)<br>  <br>`x => y` | \[12\] |
| n/a | [`yield x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield) |
| [`yield* x`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield*) |
| [Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)<br>  <br>`...x` | \[13\] |
| 1: comma | left-to-right | [Comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)<br>  <br>`x, y` |

Notes:

1.  The operand can be any expression.
2.  The "right-hand side" must be an identifier.
3.  The "right-hand side" can be any expression.
4.  The "right-hand side" is a comma-separated list of any expression with precedence > 1 (i.e., not comma expressions). The constructor of a `new` expression cannot be an optional chain.
5.  The operand must be a valid assignment target (identifier or property access). Its precedence means `new Foo++` is `(new Foo)++` (a syntax error) and not `new (Foo++)` (a TypeError: (Foo++) is not a constructor).
6.  The operand must be a valid assignment target (identifier or property access).
7.  The operand cannot be an identifier or a [private element](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
     access.
8.  The left-hand side cannot have precedence 14.
9.  The operands cannot be a logical OR `||` or logical AND `&&` operator without grouping.
10.  The "left-hand side" must be a valid assignment target (identifier or property access).
11.  The associativity means the two expressions after `?` are implicitly grouped.
12.  The "left-hand side" is a single identifier or a parenthesized parameter list.
13.  Only valid inside object literals, array literals, or argument lists.

The precedence of groups 17 and 16 may be a bit ambiguous. Here are a few examples to clarify.

*   Optional chaining is always substitutable for its respective syntax without optionality (barring a few special cases where optional chaining is forbidden). For example, any place that accepts `a?.b` also accepts `a.b` and vice versa, and similarly for `a?.()`, `a()`, etc.
*   Member expressions and computed member expressions are always substitutable for each other.
*   Call expressions and `import()` expressions are always substitutable for each other.
*   This leaves four classes of expressions: member access, `new` with arguments, function call, and `new` without arguments.
    *   The "left-hand side" of a member access can be: a member access (`a.b.c`), `new` with arguments (`new a().b`), and function call (`a().b`).
    *   The "left-hand side" of `new` with arguments can be: a member access (`new a.b()`) and `new` with arguments (`new new a()()`).
    *   The "left-hand side" of a function call can be: a member access (`a.b()`), `new` with arguments (`new a()()`), and function call (`a()()`).
    *   The operand of `new` without arguments can be: a member access (`new a.b`), `new` with arguments (`new new a()`), and `new` without arguments (`new new a`).

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/operators/operator_precedence/index.md?plain=1 "Folder: en-us/web/javascript/reference/operators/operator_precedence (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FOperator_precedence&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Foperator_precedence%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FOperator_precedence%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Foperators%2Foperator_precedence%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5c8d0ac21db572edebbd4ad428efca0af3ec1734%0A*+Document+last+modified%3A+2026-09-04T17%3A06%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
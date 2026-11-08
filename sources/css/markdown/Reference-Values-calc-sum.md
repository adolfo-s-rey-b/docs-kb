*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#mdn-search)
    

`<calc-sum>` CSS type
=====================

The **`<calc-sum>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents an expression which performs a calculation in any [CSS math function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
. The expression executes a basic arithmetic operation of addition and subtraction between two values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#syntax)

--------------------------------------------------------------------------------------------

The `<calc-sum>` type defines two numeric values and one of the following [arithmetic operators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Math#arithmetic_operators)
 between them.

[`+`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#sect)

Adds two numbers together.

[`-`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#-)

Subtracts the right number from the left.

### [Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#formal_syntax)

<calc-sum> =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( [<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#description)

------------------------------------------------------------------------------------------------------

The operands in the expression may be any [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 syntax value. You can use [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, or [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
.

The two operands' types must be consistent. For lengths, you can't use `0` to mean `0px` (or another length unit). Instead, you must add an explicit unit: `margin-top: calc(0px + 20px);` is valid, while `margin-top: calc(0 + 20px);` is invalid. Percentage value types are resolved based on the context. For example, `margin-top: calc(50% + 20px);` is valid because `margin-top` resolves percentages to lengths.

Including [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
 in `calc-sum` expressions is also allowed. The following code `calc(10px + var(--variable))`, is a valid expression.

The `+` and `-` operators **must be surrounded by [whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
**. For instance, `calc(50% -8px)` will be parsed as "a percentage followed by a negative length" — which is an invalid expression — while `calc(50% - 8px)` is "a percentage followed by a subtraction operator and a length". Likewise, `calc(8px + -50%)` is treated as "a length followed by an addition operator and a negative percentage".

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# typedef-calc-sum](https://drafts.csswg.org/css-values/#typedef-calc-sum) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum#see_also)

------------------------------------------------------------------------------------------------

*   `<calc-product>`
*   `<calc-value>`
*   [`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/calc-sum/index.md?plain=1 "Folder: en-us/web/css/reference/values/calc-sum (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-sum&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-sum%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-sum%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-sum%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
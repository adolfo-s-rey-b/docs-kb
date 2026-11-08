*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#mdn-search)
    

`exp()` CSS function
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`exp()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is an exponential function that takes a number as an argument and returns the mathematical constant `e` raised to the power of the given number.

The mathematical constant [`e`](https://en.wikipedia.org/wiki/E_(mathematical_constant) "External link (opens in new tab)")
 is the base of natural logarithms, and is approximately `2.718281828459045`.

The `exp(number)` function contains a calculation which returns the same value as [`pow(e, number)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#syntax)

---------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#parameters)

The `exp(number)` function accepts only one value as its parameter.

[`number`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#number)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Representing the value to be raised by a power of `e`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#return_value)

Returns a non-negative [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing enumber, which is the result of calculating `e` raised to the power of `number`.

*   If `number` is `-Infinity`, the result is `0`.
*   If `number` is `0`, the result is `1`.
*   If `number` is `1`, the result is `e` (i.e., `2.718281828459045`).
*   If `number` is `Infinity`, the result is `Infinity`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#formal_syntax)

-----------------------------------------------------------------------------------------------------

<exp()> =   
  exp( <calc-sum> )    
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
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
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#examples)

-------------------------------------------------------------------------------------------

### [Rotate elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#rotate_elements)

The `exp()` function can be used to [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
 elements as it returns a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
.

#### HTML

#### CSS

#### Result

### [Scale headings by fixed ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#scale_headings_by_fixed_ratio)

The `exp()` function can be useful for strategies like CSS modular scale, which relates all the font-sizes on a page to each other by a fixed ratio.

#### HTML

html

    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
    

#### CSS

css

    h1 {
      font-size: calc(1rem * exp(1.25)); /* 3.4903429574618414rem */
    }
    h2 {
      font-size: calc(1rem * exp(1)); /* 2.718281828459045rem */
    }
    h3 {
      font-size: calc(1rem * exp(0.75)); /* 2.117000016612675rem */
    }
    h4 {
      font-size: calc(1rem * exp(0.5)); /* 1.6487212707001282rem */
    }
    h5 {
      font-size: calc(1rem * exp(0.25)); /* 1.2840254166877414rem */
    }
    h6 {
      font-size: calc(1rem * exp(0)); /* 1rem */
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# exponent-funcs](https://drafts.csswg.org/css-values/#exponent-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp#see_also)

-------------------------------------------------------------------------------------------

*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
    
*   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/exp/index.md?plain=1 "Folder: en-us/web/css/reference/values/exp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fexp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fexp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fexp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fexp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdaa035392f8466e6d75f290d9ffa4317adca4070%0A*+Document+last+modified%3A+2026-09-02T11%3A38%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
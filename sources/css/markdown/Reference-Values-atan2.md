*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#mdn-search)
    

`atan2()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`atan2()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is a trigonometric function that returns the inverse tangent of two values between `-infinity` and `infinity`. The function accepts two arguments and returns an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 between `-180deg` and `180deg`, without implying any specific unit such as radians.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#syntax)

-----------------------------------------------------------------------------------------

css

    /* Two <number> values */
    transform: rotate(atan2(3, 2));
    
    /* Two <dimension> values */
    transform: rotate(atan2(1rem, -0.5rem));
    
    /* Two <percentage> values */
    transform: rotate(atan2(20%, -30%));
    
    /* Other values */
    transform: rotate(atan2(pi, 45));
    transform: rotate(atan2(e, 30));
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#parameters)

The `atan2(y, x)` function accepts two comma-separated values as its parameters. Each value can be a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, a [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. Both values must be of the same type, although if they are [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
 they can be of different units (example: `atan2(100px, 5vw)` is valid).

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#y)

The y-coordinate of the point. A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, a [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#x)

The x-coordinate of the point. A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, a [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#return_value)

Given two values `x` and `y`, the function `atan2(y, x)` calculates and returns the [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 between the positive x-axis and the ray from the origin to the point `(x, y)`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#formal_syntax)

-------------------------------------------------------------------------------------------------------

<atan2()> =   
  atan2( <calc-sum> , <calc-sum> )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#examples)

---------------------------------------------------------------------------------------------

### [Rotate elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#rotate_elements)

The `atan2()` function can be used to [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
 elements as it returns an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
.

#### HTML

html

    <div class="box box-1"></div>
    <div class="box box-2"></div>
    <div class="box box-3"></div>
    <div class="box box-4"></div>
    <div class="box box-5"></div>
    

#### CSS

    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 50px;
    }
    

css

    div.box {
      width: 100px;
      height: 100px;
      background: linear-gradient(orange, red);
    }
    div.box-1 {
      transform: rotate(atan2(3, 2));
    }
    div.box-2 {
      transform: rotate(atan2(3%, -2%));
    }
    div.box-3 {
      transform: rotate(atan2(-1, 0.5));
    }
    div.box-4 {
      transform: rotate(atan2(1, 0.5));
    }
    div.box-5 {
      transform: rotate(atan2(1rem, -0.5rem));
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# trig-funcs](https://drafts.csswg.org/css-values/#trig-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2#see_also)

---------------------------------------------------------------------------------------------

*   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [Using CSS typed arithmetic](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/atan2/index.md?plain=1 "Folder: en-us/web/css/reference/values/atan2 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fatan2&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fatan2%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fatan2%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fatan2%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdaa035392f8466e6d75f290d9ffa4317adca4070%0A*+Document+last+modified%3A+2026-09-02T11%3A38%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
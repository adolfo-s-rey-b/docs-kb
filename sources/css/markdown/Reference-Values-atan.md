*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#mdn-search)
    

`atan()` CSS function
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`atan()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is a trigonometric function that returns the inverse tangent of a number between `-∞` and `+∞`. The function contains a single calculation that returns an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 between `-90deg` and `90deg`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#syntax)

----------------------------------------------------------------------------------------

css

    /* Single <number> values */
    transform: rotate(atan(1));
    transform: rotate(atan(4 * 50));
    
    /* Other values */
    transform: rotate(atan(pi / 2));
    transform: rotate(atan(e * 3));
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#parameters)

The `atan(number)` function accepts only one value as its parameter.

[`number`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#number)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 between `-∞` and `+∞`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#return_value)

The inverse tangent of a `number` will always return an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 between `-90deg` and `90deg`.

*   If `number` is `0⁻`, the result is `0⁻`.
*   If `number` is `+∞` the result is `90deg`.
*   If `number` is `-∞` the result is `-90deg`.

That is:

*   `atan(-infinity)` representing `-90deg`.
*   `atan(-1)` representing `-45deg`
*   `atan(0)` representing `0deg`
*   `atan(1)` representing `45deg`
*   `atan(infinity)` representing `90deg`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#formal_syntax)

------------------------------------------------------------------------------------------------------

<atan()> =   
  atan( <calc-sum> )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#examples)

--------------------------------------------------------------------------------------------

### [Rotate elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#rotate_elements)

The `atan()` function can be used to [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
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
      transform: rotate(atan(-99999));
    }
    div.box-2 {
      transform: rotate(atan(-1));
    }
    div.box-3 {
      transform: rotate(atan(0));
    }
    div.box-4 {
      transform: rotate(atan(1));
    }
    div.box-5 {
      transform: rotate(atan(99999));
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# trig-funcs](https://drafts.csswg.org/css-values/#trig-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan#see_also)

--------------------------------------------------------------------------------------------

*   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/atan/index.md?plain=1 "Folder: en-us/web/css/reference/values/atan (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fatan&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fatan%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fatan%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fatan%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdaa035392f8466e6d75f290d9ffa4317adca4070%0A*+Document+last+modified%3A+2026-09-02T11%3A38%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#mdn-search)
    

`cos()` CSS function
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`cos()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is a trigonometric function that returns the cosine of a number, which is a value between `-1` and `1`. The function contains a single calculation that must resolve to either a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 by interpreting the result of the argument as radians. That is, `cos(45deg)`, `cos(0.125turn)`, and `cos(3.14159 / 4)` all represent the same value, approximately `0.707`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#try_it)

---------------------------------------------------------------------------------------

    transform: translateX(calc(cos(0deg) * 140px))
      translateY(calc(sin(0deg) * -140px));
    

    transform: translateX(calc(cos(90deg) * 140px))
      translateY(calc(sin(90deg) * -140px));
    

    transform: translateX(calc(cos(135deg) * 140px))
      translateY(calc(sin(135deg) * -140px));
    

    transform: translateX(calc(cos(180deg) * 140px))
      translateY(calc(sin(180deg) * -140px));
    

    transform: translateX(calc(cos(-45deg) * 140px))
      translateY(calc(sin(-45deg) * -140px));
    

    <div class="circle">
      <span class="dot" id="example-element"></span>
    </div>
    

    :root {
      --radius: 140px;
      --dot-size: 10px;
    }
    .circle {
      display: grid;
      place-content: center;
      margin: 0 auto;
      width: calc(var(--radius) * 2);
      aspect-ratio: 1;
      border-radius: 50%;
      border: 2px solid #666666;
      background-image:
        radial-gradient(black var(--dot-size), transparent var(--dot-size)),
        linear-gradient(135deg, blue, deepskyblue, lightgreen, lavender, honeydew);
    }
    .dot {
      display: block;
      width: var(--dot-size);
      aspect-ratio: 1;
      border-radius: 50%;
      border: 2px solid #666666;
      background-color: #ff6666;
      transform: translateX(calc(cos(0deg) * var(--radius)))
        translateY(calc(sin(0deg) * var(--radius) * -1));
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#syntax)

---------------------------------------------------------------------------------------

css

    /* Single <angle> values */
    width: calc(100px * cos(45deg));
    width: calc(100px * cos(0.125turn));
    width: calc(100px * cos(0.785398163rad));
    
    /* Single <number> values */
    width: calc(100px * cos(63.673));
    width: calc(100px * cos(2 * 0.125));
    
    /* Other values */
    width: calc(100px * cos(pi));
    width: calc(100px * cos(e / 2));
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#parameters)

The `cos(angle)` function accepts only one value as its parameter.

[`angle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#angle)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
. When specifying unitless numbers they are interpreted as a number of radians, representing an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#return_value)

The cosine of an `angle` will always return a number between `−1` and `1`.

*   If `angle` is `infinity`, `-infinity`, or `NaN`, the result is `NaN`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#formal_syntax)

-----------------------------------------------------------------------------------------------------

<cos()> =   
  cos( <calc-sum> )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#examples)

-------------------------------------------------------------------------------------------

### [Keep the size of a rotated box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#keep_the_size_of_a_rotated_box)

The `cos()` function can be used to keep the size of a rotated box.

When the element is rotated using [`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
, it goes beyond its initial size. To fix this, we will use `cos()` to update the element size.

For example, if you rotate a `100px`/`100px` square `45deg`, the diamond it creates will be wider and taller than the original square. To shrink the diamond into the box allotted for the original square, you would have to scale down the diamond using this formula: `width = height = 100px * cos(45deg) = 100px * 0.707 = 70.7px`. You need to also adjust the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 and add [`translate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
 to correct the position:

#### HTML

html

    <div class="original-square"></div>
    <div class="rotated-diamond"></div>
    <div class="rotated-scaled-diamond"></div>
    

#### CSS

    body {
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 50px;
    }
    

css

    div.original-square {
      width: 100px;
      height: 100px;
      background-color: blue;
    }
    div.rotated-diamond {
      width: 100px;
      height: 100px;
      background-color: red;
      transform: rotate(45deg);
    }
    div.rotated-scaled-diamond {
      width: calc(100px * cos(45deg));
      height: calc(100px * cos(45deg));
      margin: calc(100px / 4 * cos(45deg));
      transform: rotate(45deg);
      transform-origin: center;
      background-color: green;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# trig-funcs](https://drafts.csswg.org/css-values/#trig-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos#see_also)

-------------------------------------------------------------------------------------------

*   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/cos/index.md?plain=1 "Folder: en-us/web/css/reference/values/cos (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcos&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcos%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcos%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcos%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
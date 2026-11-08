*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#mdn-search)
    

`sin()` CSS function
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sin()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is a trigonometric function that returns the sine of a number, which is a value between `-1` and `1`. The function contains a single calculation that must resolve to either a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 by interpreting the result of the argument as radians. That is, `sin(45deg)`, `sin(0.125turn)`, and `sin(3.14159 / 4)` all represent the same value, approximately `0.707`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#try_it)

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#syntax)

---------------------------------------------------------------------------------------

css

    /* Single <angle> values */
    width: calc(100px * sin(45deg));
    width: calc(100px * sin(0.25turn));
    width: calc(100px * sin(1.0471967rad));
    
    /* Single <number> values */
    width: calc(100px * sin(63.673));
    width: calc(100px * sin(2 * 0.125));
    
    /* Other values */
    width: calc(100px * sin(pi / 2));
    width: calc(100px * sin(e / 4));
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#parameters)

The `sin(angle)` function accepts only one value as its parameter.

[`angle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#angle)

A calculation which resolves to a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
. When specifying unitless numbers they are interpreted as a number of radians, representing an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#return_value)

The sine of an `angle` will always return a number between `−1` and `1`.

*   If `angle` is `infinity`, `-infinity`, or `NaN`, the result is `NaN`.
*   If `angle` is `0⁻`, the result is `0⁻`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#formal_syntax)

-----------------------------------------------------------------------------------------------------

<sin()> =   
  sin( <calc-sum> )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#examples)

-------------------------------------------------------------------------------------------

### [Changing box sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#changing_box_sizes)

In this example, `sin(30deg)` will return `0.5`, making the box have a `50px` width and a `50px` height.

css

    div {
      background-color: red;
      width: calc(sin(30deg) * 100px);
      height: calc(sin(30deg) * 100px);
    }
    

### [Controlling animation duration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#controlling_animation_duration)

Another use case is to control the [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
, reducing the duration based on the sine value. In this case, the animation duration will be `1s`.

css

    div {
      animation-name: myAnimation;
      animation-duration: calc(sin(0.25turn) * 1s);
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# trig-funcs](https://drafts.csswg.org/css-values/#trig-funcs) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin#see_also)

-------------------------------------------------------------------------------------------

*   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/sin/index.md?plain=1 "Folder: en-us/web/css/reference/values/sin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
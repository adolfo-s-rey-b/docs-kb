*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#mdn-search)
    

`cubic-bezier()` CSS function
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`cubic-bezier()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 creates a smooth transition using a cubic [Bézier curve](https://developer.mozilla.org/en-US/docs/Glossary/Bezier_curve)
. As an [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
, it can be used to smooth out the start and end of the [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#syntax)

----------------------------------------------------------------------------------------------------------------

css

    cubic-bezier(0.25, 0.1, 0.25, 1)
    cubic-bezier(0.1, -0.6, 0.2, 0)
    cubic-bezier(0, 0, 1, 1)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#parameters)

The function accepts the following four parameters, which represent the coordinates of two control points:

[`<x1>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#x1)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the x-axis coordinate of the first control point. It must be in the `[0, 1]` range.

[`<y1>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#y1)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the y-axis coordinate of the first control point.

[`<x2>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#x2)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the x-axis coordinate of the second control point. It must be in the `[0, 1]` range.

[`<y2>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#y2)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the y-axis coordinate of the second control point.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#description)

--------------------------------------------------------------------------------------------------------------------------

The cubic Bézier functions, often called "smooth" easing functions, correlate an input progress to an output progress, both expressed as [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s, where `0.0` represents the initial state and `1.0` represents the final state. If the cubic Bézier curve is invalid, CSS ignores the whole property.

A cubic Bézier curve is defined by four points: P0, P1, P2, and P3. The points P0 and P3 represent the start and the end of the curve. In CSS, the start point P0 is fixed at `(0, 0)` and the end point P3 is fixed at `(1, 1)`, while intermediate points P1 and P2 are defined by the function parameters `(<x1>, <y1>)` and `(<x2>, <y2>)` respectively. The x-axis represents input progress and the y-axis represents output progress.

![Graph of Input progress to Output progress showing an S-shaped line curving from the origin to (1, 1) with the Bezier control points P1(0.1, 0.6) and P2(0.7, 0.2).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier/cubic-bezier.svg)

Not all cubic Bézier curves are suitable as easing functions because not all are [mathematical functions](https://en.wikipedia.org/wiki/Function_%28mathematics%29 "External link (opens in new tab)")
; i.e., curves that for a given x-axis coordinate have zero or one value. With P0 and P3 fixed as defined by CSS, a cubic Bézier curve is a function, and is valid when the x-axis coordinates of P1 and P2 are both in the \[0, 1\] range.

Cubic Bézier curves with the P1 or P2 ordinate outside the `[0, 1]` range can cause the value to go farther than the final state and then return. In animations, this creates a kind of "bouncing" effect.

![Graphs of the easing function cubic-bezier(0.3, 0.2, 0.2, 1.4), one of which shows the output progress going above 1 starting from a certain input progress, the other shows the output progress reaching and then staying at 1.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier/cubic-bezier_out_of_range.svg)

However, certain properties will restrict the output if it goes outside an allowable range. For example, a color component greater than `255` or smaller than `0` in [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 will be clipped to the closest allowed value (`255` and `0`, respectively). Some `cubic-bezier()` values exhibit this property.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

<cubic-bezier()> =   
  cubic-bezier( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,1\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#examples)

--------------------------------------------------------------------------------------------------------------------

### [Bouncing effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#bouncing_effect)

In this example, the red ball bounces out of the box when transitioned from its original position. This is because one of the P2 values, `2.3`, goes beyond the `[0, 1]` range.

    <div tabindex="0">
      <span></span>
    </div>
    

    div {
      margin: 8px auto;
      padding: 8px;
      width: 256px;
      border-radius: 40px;
      background-color: wheat;
    }
    
    span {
      display: block;
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: tomato;
    }
    
    div:hover span,
    div:focus span {
      translate: 192px 0;
    }
    

css

    span {
      transition: translate 0.3s cubic-bezier(0.3, 0.8, 0.3, 2.3);
    }
    

### [Using the cubic-bezier() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#using_the_cubic-bezier_function)

These cubic Bézier curves are valid for use in CSS:

css

    /* The canonical Bézier curve with four <number> in the [0,1] range */
    cubic-bezier(0.1, 0.7, 1.0, 0.1)
    
    /* Using <integer> is valid because any <integer> is also a <number> */
    cubic-bezier(0, 0, 1, 1)
    
    /* Negative values for ordinates are valid, leading to bouncing effects */
    cubic-bezier(0.1, -0.6, 0.2, 0)
    
    /* Values greater than 1.0 for ordinates are also valid */
    cubic-bezier(0, 1.1, 0.8, 4)
    

These cubic Bézier curve definitions are invalid:

css

    /* Parameters must be numbers */
    cubic-bezier(0.1, red, 1.0, green)
    
    /* X coordinates must be in the [0, 1] range */
    cubic-bezier(2.45, 0.6, 4, 0.1)
    
    /* There must be exactly four parameters */
    cubic-bezier(0.3, 2.1)
    
    /* X coordinates must be in the [0, 1] range */
    cubic-bezier(-1.9, 0.3, -0.2, 2.1)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Easing Functions Level 1  <br>\# cubic-bezier-easing-functions](https://drafts.csswg.org/css-easing/#cubic-bezier-easing-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier#see_also)

--------------------------------------------------------------------------------------------------------------------

*   Other easing functions: [`linear()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
     and [`steps()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   [cubic-bezier.com](https://cubic-bezier.com/ "External link (opens in new tab)")
     by Lea Verou

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/easing-function/cubic-bezier/index.md?plain=1 "Folder: en-us/web/css/reference/values/easing-function/cubic-bezier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Fcubic-bezier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Fcubic-bezier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Fcubic-bezier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Fcubic-bezier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
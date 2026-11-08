*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#mdn-search)
    

`<easing-function>` CSS type
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<easing-function>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a mathematical function that describes the rate at which a value changes.

This transition between two values may be applied in different situations. It may be used to describe how fast values change during animations. This lets you vary the animation's speed over the course of its duration. You can specify an easing function for CSS [transition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
 and [animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
 properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#values)

An `<easing-function>` can be one of the following types:

[`<linear-easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#linear-easing-function)

Creates transitions that progress at a constant rate. This function can be specified using one of the following:

[`linear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#linear)

Specifies a constant rate of interpolation, with no change in the rate of progress throughout the duration (that is, no acceleration or deceleration). This keyword value is equivalent to `linear(0, 1)`. It can also be represented as `cubic-bezier(0, 0, 1, 1)`.

![Graph of Input progress to Output progress showing a line extending from the origin to (1, 1).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear.svg)

**Note:** The `linear` keyword is always interpreted as `linear(0, 1)`, whereas the function `linear(0, 1)` is interpreted as `linear(0 0%, 1 100%)`.

[`linear()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)

Defines multiple points of progress using [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values, with optional [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values to control their timing.

[`<cubic-bezier-easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#cubic-bezier-easing-function)

Creates smooth transitions with variable rates of change. This function can be specified using one of the following:

[`ease`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#ease)

Represents the easing function `cubic-bezier(0.25, 0.1, 0.25, 1)`. It indicates that the interpolation starts slowly, accelerates sharply, and then slows gradually towards the end. It is similar to the `ease-in-out` keyword, though it accelerates more sharply at the beginning.

[`ease-in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#ease-in)

Represents the easing function `cubic-bezier(0.42, 0, 1, 1)`. It indicates that the interpolation starts slowly, then progressively speeds up until the end, at which point it stops abruptly.

[`ease-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#ease-out)

Represents the easing function `cubic-bezier(0, 0, 0.58, 1)`. It indicates that the interpolation starts abruptly and then progressively slows down towards the end.

[`ease-in-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#ease-in-out)

Represents the easing function `cubic-bezier(0.42, 0, 0.58, 1)`. It indicates that the interpolation starts slowly, speeds up, and then slows down towards the end. At the beginning, it behaves like the `ease-in` keyword; at the end, it is like the `ease-out` keyword.

![Graphs of Input progress to Output progress, of which ease shows a curved line quickly rising from the origin to (1, 1); ease-in shows a shallow curved line from the origin that straightens out as it approaches (1, 1); ease-out shows a straight diagonal line that slightly curves as it gets close to (1, 1); and ease-in-out shows a symmetrical, S-shaped line curving from the origin to (1, 1).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/ease.svg)

[`cubic-bezier()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)

Defines a custom curve using four [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values that specify the coordinates of two control points. The x-coordinates must be in the range `[0, 1]`.

[`<step-easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#step-easing-function)

Creates stepped transitions that divides the animation into a set number of equal-length intervals, causing the animation to jump from one step to the next rather than transitioning smoothly. This function can be specified using one of the following:

[`step-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#step-start)

Represents the easing function `steps(1, jump-start)` or `steps(1, start)`. It indicates that the interpolation jumps immediately to its final state, where it stays until the end.

[`step-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#step-end)

Represents the easing function `steps(1, jump-end)` or `steps(1, end)`. It indicates that the interpolation stays in its initial state until the end, at which point it jumps directly to its final state.

![Two graphs of Input progress to Output progress. In the step-start graph, an unfilled circle represents the origin point (0, 0), with a horizontal line extending from (0, 1) to (1, 1). In the step-end graph, a horizontal line extends from the origin to (1, 0), with an unfilled circle at (1,0) and a solid circle at (1, 1).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/step.svg)

[`steps()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)

Creates a stair-shaped curve using an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 to specify the number of intervals and an optional keyword to control the timing of jumps.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<easing-function> =   
  <linear-easing-function>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier-easing-function>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <step-easing-function>            
  
<linear-easing-function> =   
  linear      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <linear()>    
  
<cubic-bezier-easing-function> =   
  ease              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-out          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in-out       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier()>    
  
<step-easing-function> =   
  step-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  step-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <steps()>     
  
[<linear()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
 =   
  linear( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[{0,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cubic-bezier()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
 =   
  cubic-bezier( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,1\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<steps()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
 =   
  steps( <integer> , <step-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<step-position> =   
  jump-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-none   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-both   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#examples)

-------------------------------------------------------------------------------------------------------

### [Comparing the easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#comparing_the_easing_functions)

This example provides a comparison between the different easing functions using an animation. From the drop-down menu, you can select an easing function – there are a couple of keywords and some `cubic-bezier()` and `steps()` options. After selecting an option, you can start and stop the animation using the provided button.

#### HTML

#### CSS

#### JavaScript

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Easing Functions Level 1  <br>\# easing-functions](https://drafts.csswg.org/css-easing/#easing-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function#see_also)

-------------------------------------------------------------------------------------------------------

*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   [`linear()` easing generator](https://linear-easing-generator.netlify.app/ "External link (opens in new tab)")
     by Jake Archibald
*   [cubic-bezier.com](https://cubic-bezier.com/ "External link (opens in new tab)")
     by Lea Verou

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/easing-function/index.md?plain=1 "Folder: en-us/web/css/reference/values/easing-function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
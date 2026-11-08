*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#mdn-search)
    

`steps()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`steps()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transition that divides the input time into a specified number of intervals that are equal in length. This subclass of step functions are sometimes also called _staircase functions_.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#syntax)

---------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#parameters)

The function accepts the following parameters:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#integer)

Represents the number of equidistant intervals or 'steps'. It must be a positive integer greater than `0` unless the second parameter is `jump-none`, in which case, it must be a positive integer greater than `1`.

[`<step-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#step-position)

Specifies when the jump between values occurs. If omitted, it defaults to `end`. The possible keyword values include:

[`jump-start` or `start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#jump-start)

Indicates that the first step happens when the animation begins.

[`jump-end` or `end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#jump-end)

Indicates that the last step happens when the animation ends.

[`jump-none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#jump-none)

Indicates neither early nor late jumps happen.

[`jump-both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#jump-both)

Indicates both early and late jumps happen.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#description)

-------------------------------------------------------------------------------------------------------------------

The `steps()` function divides the animation duration into equal intervals. For example, `steps(4, end)` divides the animation into four equal intervals, with values changing at the end of each interval except the last change which occurs at the animation's end.

If an animation contains multiple segments, the specified number of steps applies to each segment. For example, if an animation has three segments and uses `steps(2)`, there will be six steps in total, with two steps per segment.

The following image shows the effect of different `<step-position>` values when the jumps occur:

![Graphs of Input progress to Output progress, of which steps(2, jump-start) shows horizontal lines extending 0.5 unit from (0, 0.5) and (0.5, 1), respectively, with empty circles at the origin and (0.5, 0.5); steps(4, jump-end) shows horizontal lines extending 0.25 unit from (0, 0), (0.25, 0.25), (0.5, 0.5), and (0.75, 0.75), respectively, with unfilled circles at (0.25, 0), (0.5, 0.25), and (0.75, 0.5), and a solid circle at (1, 1); steps(5, jump-none) shows horizontal lines extending 0.2 unit from (0, 0), (0.2, 0.25), (0.4, 0.5), (0.6, 0.75), and (0.8, 1), respectively, with unfilled circles at (0.2, 0), (0.4, 0.25), (0.6, 0.5), and (0.8, 0.75); steps(3, jump-both) shows horizontal lines extending 1/3 unit from (0, 0.25), (1/3, 0.5), and (2/3, 0.75), respectively, with a solid circle at (1, 1) and unfilled circles at the origin, (1/3, 0.25), (2/3, 0.5), and (1, 0.75).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps/jump.svg)

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

<steps()> =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#examples)

-------------------------------------------------------------------------------------------------------------

### [Using the steps() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#using_the_steps_function)

The following `steps()` functions are valid:

The following `steps()` functions are invalid:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Easing Functions Level 1  <br>\# step-easing-functions](https://drafts.csswg.org/css-easing/#step-easing-functions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps#see_also)

-------------------------------------------------------------------------------------------------------------

*   Other easing functions: [`cubic-bezier()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
     and [`linear()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   [Step function](https://en.wikipedia.org/wiki/Step_function "External link (opens in new tab)")
     on Wikipedia

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/easing-function/steps/index.md?plain=1 "Folder: en-us/web/css/reference/values/easing-function/steps (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Fsteps&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Fsteps%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Fsteps%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Fsteps%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
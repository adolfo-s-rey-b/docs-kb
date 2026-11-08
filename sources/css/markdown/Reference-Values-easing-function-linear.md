*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#mdn-search)
    

`linear()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`linear()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 creates a transition curve that progresses uniformly between points. As an [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
, it creates transitions where the [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 occurs at a constant rate from beginning to end.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#syntax)

----------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#parameters)

The function accepts two or more of the following values, which represent progress points in the animation timeline:

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

Represents a point in time along the duration of the animation or transition. At least two values must be specified. The value `0` represents the start of the transition, and `1` represents the end. Values outside the `0` to `1` range are also allowed.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

Indicates when the progress `<number>` is reached during the animation timeline. It can be specified after any `<number>` value except the first and last and can take up to two values. If two percentage values are specified, they define the length of the stop: the first percentage indicates the starting point and the second percentage indicates the ending point for that segment in the animation or transition. If no `<percentage>` value is specified, the progress values are distributed evenly along the timeline.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#description)

--------------------------------------------------------------------------------------------------------------------

The `linear()` function allows the approximation of complex animations and transitions by interpolating linearly between the specified points. A typical use of the `linear()` function is to provide many points to approximate any curve.

The `linear()` function creates transitions where progress occurs at a constant rate between specified points. For example, `linear(0, 0.25, 1)` has linear stops of `0`, `0.25`, and `1`. The animation starts at point `0`, moves linearly to `0.25`, and then continues linearly to point `1`. Since no percentage is specified, the same duration (`50%`) is used for each segment, that is, from `0` to `0.25` and from `0.25` to `1`.

![Graphs of Input progress to Output progress, of which linear(0, 0.25, 1) shows a broken line connecting the origin, (0.5, 0.25), and (1, 1); and linear(0, 0.25 75%, 1) shows a broken line connecting the origin, (0.75, 0.25), and (1, 1).](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear/linear_function.svg)

By default, the stops are equidistant. For example, if there are five stops, they will occur at 0%, 25%, 50%, 75%, and 100% of the duration. You can use optional percentage values to provide finer control, defining when each progress value should occur and allowing for a more controlled progression of the transition.

Consider an animation with a duration time of 100 seconds and a change of 100 pixels. Let's look at a scenario where the easing of the animation is specified as `linear(0, 0.25 75%, 1)`. In this case, the animation progresses to 25 pixels (25% of its total change) in the first 75 seconds (75% of the duration). The last 75 pixels are applied in the remaining 25 seconds of the animation.

For the same animation, suppose the easing function is specified as `linear(0, 0.5 25% 75%, 1)`. Here, the animation reaches 50 pixels (50% of its total change) in 25 seconds (25% of the duration) and remains there for 50 seconds (75% - 25% of the duration). Then the last 50 pixels are applied in the remaining 25 seconds of the duration. Note that `linear(0, 0.5 25% 75%, 1)` is equivalent to `linear(0, 0.5 25%, 0.5 75%, 1)`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

<linear()> =   
  linear( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[{0,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#examples)

--------------------------------------------------------------------------------------------------------------

### [Using the linear() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#using_the_linear_function)

The following `linear()` functions are valid for use in CSS:

The following `linear()` definitions are invalid:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Easing Functions Level 1  <br>\# the-linear-easing-function](https://drafts.csswg.org/css-easing/#the-linear-easing-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear#see_also)

--------------------------------------------------------------------------------------------------------------

*   Other easing functions: [`cubic-bezier()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
     and [`steps()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   [`linear()` easing generator](https://linear-easing-generator.netlify.app/ "External link (opens in new tab)")
     by Jake Archibald

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/easing-function/linear/index.md?plain=1 "Folder: en-us/web/css/reference/values/easing-function/linear (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Flinear&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Flinear%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Feasing-function%2Flinear%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Feasing-function%2Flinear%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
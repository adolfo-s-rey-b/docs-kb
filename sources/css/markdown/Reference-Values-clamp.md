*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#mdn-search)
    

`clamp()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`clamp()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 clamps a value within a range of values between a defined minimum bound and a maximum bound. The function takes three parameters: a minimum value, a preferred value, and a maximum allowed value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#try_it)

-----------------------------------------------------------------------------------------

Note that using `clamp()` for font sizes, as in these examples, allows you to set a font-size that grows with the size of the viewport, but doesn't go below a minimum font-size or above a maximum font-size. It has the same effect as the code in [Fluid Typography](https://css-tricks.com/snippets/css/fluid-typography/ "External link (opens in new tab)")
 but in one line, and without the use of media queries.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#syntax)

-----------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#parameters)

The `clamp(min, val, max)` function accepts three comma-separated expressions as its parameters.

[`min`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#min)

The minimum value is the smallest (most negative) value. This is the lower bound in the range of allowed values. If the preferred value is less than this value, the minimum value will be used.

[`val`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#val)

The preferred value is the expression whose value will be used as long as the result is between the minimum and maximum values.

[`max`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#max)

The maximum value is the largest (most positive) expression value to which the value of the property will be assigned if the preferred value is greater than this upper bound.

The expressions can be math functions (see [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 for more information), literal values, other expressions that evaluate to a valid argument type (like [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
), or nested [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
 and [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
 functions. For math expressions, you can use addition, subtraction, multiplication, and division without using the `calc()` function itself. You may also use parentheses to establish computation order when needed.

You can use different units for each value in your expressions and different units in any math function making up any of the arguments.

Keep the following aspects in mind while working with the function:

*   Math expressions involving percentages for widths and heights on table columns, table column groups, table rows, table row groups, and table cells in both auto and fixed layout tables _may_ be treated as if `auto` had been specified.
*   It is permitted to nest `max()` and `min()` functions as expression values, in which case the inner ones are treated as basic parentheses. The expressions are full math expressions, so you can use direct addition, subtraction, multiplication and division without using the `calc()` function itself.
*   The expression can be values combining the addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`) operators, using standard operator precedence rules. Make sure to put a space on each side of the `+` and `-` operands. You can use different units for each value in your expression. You may also use parentheses to establish computation order when needed.
*   Oftentimes you will want to use [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
     and [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
     within a `clamp()` function.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#return_value)

`clamp(MIN, VAL, MAX)` is resolved as `max(MIN, min(VAL, MAX))`.

Based on the provided parameters, the function returns [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
, [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, or [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#formal_syntax)

-------------------------------------------------------------------------------------------------------

<clamp()> =   
  clamp( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-sum> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , <calc-sum> , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-sum> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#examples)

---------------------------------------------------------------------------------------------

### [min(), max(), and clamp() comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#min_max_and_clamp_comparison)

In this example we have a web page that uses [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
, [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
, and `clamp()` to set sizes responsively.

The example adjusts the sizes of page elements in three ways:

*   the lengths of the lines of text
*   the font size of paragraph text
*   the font size of heading text

In all three cases, the page uses a combination of a viewport-relative units ([`vw`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vw)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
), to set a size that varies with the viewport width, and a value that is not viewport relative ([`rem`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rem)
 and [`px`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#px)
) to implement minimum and/or maximum sizes.

The example is at [https://mdn.github.io/css-examples/min-max-clamp/](https://mdn.github.io/css-examples/min-max-clamp/ "External link (opens in new tab)")
. Open it in a new window and try adjusting the window width.

The **line length** (controlled by the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 of the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element) will increase as the window width increases, but only up to a certain point (`1000px`), and beyond that point, it won't increase anymore. We're using `min()` to set a **maximum line length**: it can go under `1000px`, but won't go over. This is helpful because long lines are harder to read, so we often want to limit how long a line can be. To achieve this we use `min(1000px, calc(70% + 100px))`: when the result of the percentage-based calculation goes above `1000px`, we switch to the fixed `1000px` value.

The **size of the paragraph text**, controlled by the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element, decreases as the window gets narrower, but only up to a certain point, and beyond that point (the point where `1.2vw` is less than `1.2rem`) it doesn't get any smaller: it stays at `1.2rem`. We're using `max()` to set a **minimum font size**: the font can grow above `1.2rem` but will never go below it. This is helpful because really small text is hard to read. To achieve this we use `max(1.2rem, 1.2vw)`. This means that the `font-size` will be set at `1.2rem`, unless the computed value of `1.2vw` is greater than that of `1.2rem`, in which case it will be set to `1.2vw` instead.

The **size of the heading text**, controlled by the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 element, has a viewport-relative value with both a maximum and a minimum threshold. To achieve this we use `clamp(1.8rem, 2.5vw, 2.8rem)`. The viewport-relative value is `2.5vw` but it is clamped between `1.8rem` and `2.8rem`, so:

*   if the calculated value of `2.5vw` is less than `1.8rem`, then `1.8rem` will be used
*   if the calculated value of `2.5vw` is greater than `2.8rem`, then `2.8rem` will be used.

This prevents the heading text from getting too small in a very narrow window, or too big in a very wide window.

#### HTML

#### CSS

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#accessibility)

-------------------------------------------------------------------------------------------------------

When `clamp()` is used for controlling text size, make sure that the maximum allowed value is a [relative length unit](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units)
 that is no less than twice the minimum allowed value, for example:

This helps to ensure that text size can scale to at least 200% if the page is zoomed.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.4: Resize Text | WAI | W3C](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html "External link (opens in new tab)")
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# funcdef-clamp](https://drafts.csswg.org/css-values/#funcdef-clamp) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp#see_also)

---------------------------------------------------------------------------------------------

*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    
*   [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
    
*   [Learn: CSS Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/clamp/index.md?plain=1 "Folder: en-us/web/css/reference/values/clamp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fclamp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fclamp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fclamp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fclamp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11c522da37b7469cbce26bbe220936aec1d372d0%0A*+Document+last+modified%3A+2026-08-12T02%3A52%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
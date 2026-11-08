*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#mdn-search)
    

`minmax()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`minmax()`** [CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a size range greater than or equal to _min_ and less than or equal to _max_. It is used with [CSS grids](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#try_it)

------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#syntax)

------------------------------------------------------------------------------------------

A function taking two parameters, _min_ and _max_.

Each parameter can be a `<length>`, a `<percentage>` or one of the keyword values `max-content`, `min-content`, or `auto`.

The second parameter _max_ also accepts [`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
 values. (this `fr` units can only be used for _max_, and are invalid for _min_.)

If _max_ < _min_, then _max_ is ignored and `minmax(min,max)` is treated as _min_.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

A non-negative length.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A non-negative percentage relative to the inline size of the grid container in column grid tracks, and the block size of the grid container in row grid tracks. If the size of the grid container depends on the size of its tracks, then the `<percentage>` must be treated as `auto`. The [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may adjust the intrinsic size contributions of the track to the size of the grid container and increase the final size of the track by the minimum amount that would result in honoring the percentage.

[`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)

A non-negative dimension with the unit `fr` specifying the track's flex factor. Each `<flex>`\-sized track takes a share of the remaining space in proportion to its flex factor.

[`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)

Represents the largest max-content contribution of the grid items occupying the grid track.

[`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)

Represents the largest min-content contribution of the grid items occupying the grid track.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#auto)

As `min`, it represents the largest minimum size (as specified by [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
/[`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
) of the grid items occupying the grid track. As `max`, it is identical to `max-content`. However, unlike `max-content`, it allows expansion of the track by the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 property values like `normal` and `stretch`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#formal_syntax)

--------------------------------------------------------------------------------------------------------

<minmax()> =   
  minmax( min , max )    

### [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#css_properties)

`minmax()` function can be used within:

*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    
*   [`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#examples)

----------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#css)

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# funcdef-grid-template-columns-minmax](https://drafts.csswg.org/css-grid/#funcdef-grid-template-columns-minmax) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax#see_also)

----------------------------------------------------------------------------------------------

*   [Basic concepts of grid layout: track sizing with minmax()](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#track_sizing_and_minmax)
    
*   [CSS grids, logical values and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes)
    
*   Video: [Introducing minmax()](https://gridbyexample.com/video/series-minmax/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/minmax/index.md?plain=1 "Folder: en-us/web/css/reference/values/minmax (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fminmax&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fminmax%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fminmax%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fminmax%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
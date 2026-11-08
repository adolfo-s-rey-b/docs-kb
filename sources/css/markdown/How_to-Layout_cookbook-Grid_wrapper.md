*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#mdn-search)
    

Grid wrapper
============

The grid wrapper pattern is useful for aligning grid content within a central wrapper while also allowing items to break out and align to the edge of the containing element or page.

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#requirements)

------------------------------------------------------------------------------------------------------------------

Items placed on the grid should be able to align to a horizontally-centered max-width wrapper or the outer edges of the grid, or both.

[Recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#recipe)

------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#choices_made)

------------------------------------------------------------------------------------------------------------------

This recipe uses the CSS grid [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
 function to define the grid track sizes in the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property. For the central columns with a maximum width, we can set a minimum value of `0` or greater and a maximum value that specifies the maximum size the column tracks will grow to. Using [relative](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_font)
 or [absolute](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)
 [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 units (pixels, ems, rems) will create a fixed maximum size for the central wrapper, whereas using [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values or [viewport units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport)
 will cause the wrapper to grow or shrink in response to its context.

The outer two columns have a maximum size of `1fr`, meaning that they will each expand to fill the remaining available space in the grid container.

[Useful fallbacks or alternative methods](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#useful_fallbacks_or_alternative_methods)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To center the grid horizontally on the page you can set a `max-width` along with left and right `auto` [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
s:

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#accessibility_concerns)

--------------------------------------------------------------------------------------------------------------------------------------

Although CSS grid enables positioning items anywhere (within reason), ensuring that your underlying markup follows a logical order is important (see [CSS grid layout and accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Accessibility)
 for more details).

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper#see_also)

----------------------------------------------------------------------------------------------------------

*   [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
     property
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module
*   [CSS grid: More flexibility with `minmax()`](https://css-irl.info/more-flexibility-with-minmax/ "External link (opens in new tab)")
     (2018)
*   [Breaking out with CSS grid](https://rachelandrew.co.uk/archives/2017/06/01/breaking-out-with-css-grid-explained/ "External link (opens in new tab)")
     (2017)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Grid_wrapper/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/grid_wrapper/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/grid_wrapper (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FGrid_wrapper&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fgrid_wrapper%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FGrid_wrapper%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fgrid_wrapper%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0ab262675372b83fc870accf3dc46d6a367c451c%0A*+Document+last+modified%3A+2026-02-12T15%3A14%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#mdn-search)
    

`<flex>` CSS type
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<flex>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 denotes a flexible length within a grid container. It is used in [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
, [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
 and other related properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#syntax)

----------------------------------------------------------------------------------------------

The `<flex>` data type is specified as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by the unit `fr`. The `fr` unit represents a fraction of the leftover space in the grid container. As with all CSS dimensions, there is no space between the unit and the number.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#examples)

--------------------------------------------------------------------------------------------------

### [Examples of correct values for the fr data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#examples_of_correct_values_for_the_fr_data_type)

1fr    /\* Using an integer value \*/
2.5fr  /\* Using a float value \*/

### [Example of use in a track listing for CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#example_of_use_in_a_track_listing_for_css_grid_layout)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Grid Layout Module Level 2  <br>\# fr-unit](https://drafts.csswg.org/css-grid/#fr-unit) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value#see_also)

--------------------------------------------------------------------------------------------------

*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/flex_value/index.md?plain=1 "Folder: en-us/web/css/reference/values/flex_value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fflex_value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fflex_value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fflex_value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fflex_value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
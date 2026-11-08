*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#mdn-search)
    

Basic concepts of logical properties and values
===============================================

The [CSS logical properties and values module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values#properties)
 defines flow-relative mappings for many of the [physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
 and values in CSS. This article discusses this module, and explains [flow relative values](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
 and properties.

[Why are logical properties useful](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#why_are_logical_properties_useful)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS 2.1 and earlier had sized things according to the physical dimensions of the screen. Therefore we describe boxes as having a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, position items from the `top` and `left`, assign borders, margin, and padding to the `top`, `right`, `bottom`, `left`, etc. The Logical properties and values module defines mappings for these [physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
 and values to their logical, or flow relative, counterparts — e.g., `start` and `end` as opposed to `left` and `right`/`top` and `bottom`.

These mappings are very useful for sites that get translated into languages with a different writing mode than the original layout. For example, with a CSS grid layout, if the grid container has a width applied with the [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties used to align the grid items, as these properties are flow relative, the `justify-self: start` aligns the item to the start on the inline dimension, and `align-self: start` does the same on the block dimension.

![A grid in a horizontal writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/grid-horizontal-width-sm.png)

If the writing mode of this component is changed to `vertical-rl` using the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property, the alignment continues to work in the same way. The inline dimension will run vertically and the block dimension horizontally. The grid doesn't look the same, however, as the width assigned to the container is a horizontal measure, a measure tied to the physical and not the logical or flow relative running of the text.

![A grid in vertical writing mode.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/grid-vertical-width-sm.png)

If instead of the `width` property, the logical property [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 is used, the component will work the same way no matter which writing mode it is displayed using.

![A grid layout in vertical writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/grid-vertical-inline-size-small.png)

You can try this out in the live example below. Change `writing-mode` from `vertical-rl` to `horizontal-tb` on `.grid` to see how the different properties change the layout.

When working with a site in a writing mode other than a horizontal, top-to-bottom one, or when using writing modes for creative reasons, being able to relate to the flow of the content makes a lot of sense.

[Block and inline dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#block_and_inline_dimensions)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

A key concept of working with flow relative properties and values is the two dimensions of block and inline. CSS layout methods such as flexbox and grid layout use the concepts of `block` and `inline` rather than `right` and `left`/`top` and `bottom` when aligning items.

The `inline` dimension is the dimension along which a line of text runs in the writing mode in use. Therefore, in an English document with the text running horizontally left-to-right, or an Arabic document with the text running horizontally right-to-left, the inline dimension is _horizontal_. Switch to a vertical writing mode (e.g., a Japanese document) and the inline dimension is now _vertical_, as lines in that writing mode run vertically.

The block dimension is the other dimension, and the direction in which blocks — such as paragraphs — display one after the other. In English and Arabic, these run vertically, whereas in any vertical writing mode these run horizontally.

The below diagram shows the inline and block directions in a horizontal writing mode:

![diagram showing the inline axis running horizontally, block axis vertically.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/mdn-horizontal.png)

This diagram shows block and inline in a vertical writing mode:

![Diagram showing the block axis running horizontally the inline axis vertically.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/mdn-vertical.png)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [Box alignment in flex layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    
*   [Flow layout and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_writing_modes)
    
*   [Understanding logical properties and values](https://www.smashingmagazine.com/2018/03/understanding-logical-properties-values/ "External link (opens in new tab)")
     on Smashing Magazine (2018)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/logical_properties_and_values/basic_concepts/index.md?plain=1 "Folder: en-us/web/css/guides/logical_properties_and_values/basic_concepts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FBasic_concepts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fbasic_concepts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FBasic_concepts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fbasic_concepts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
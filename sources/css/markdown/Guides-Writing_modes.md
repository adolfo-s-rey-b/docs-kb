*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#mdn-search)
    

CSS writing modes
=================

The **CSS writing modes** module defines support for various international writing modes and their combinations, including left-to-right and right-to-left text ordering as well as horizontal and vertical orientations.

A _writing mode_ in CSS is determined by the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
 properties defined in this module. It is defined primarily in terms of its inline base direction and block flow direction.

Some horizontal languages are left-to-right, including Latin and Indic scripts. Other horizontal languages are written right-to-left, including Hebrew and Arabic scripts. Sometimes text needs to be bidirectional, such as when mixing left-to-right and right-to-left scripts. Some languages can be written with a vertical orientation, for example, Chinese, Japanese, and Korean (CJK) scripts.

The CSS writing modes module addresses the orientations of all writing modes. Other modules, such as the [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS)
 module, provide rendering models and formatting controls related to the display text annotations.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#reference)

---------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#properties)

*   [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    
*   `glyph-orientation-vertical`
*   [`text-combine-upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    
*   [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    
*   [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    

### [Glossary and terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#glossary_and_terms)

*   [Baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Typography)
    
*   [Internationalization](https://developer.mozilla.org/en-US/docs/Glossary/Internationalization)
    
*   [Localization](https://developer.mozilla.org/en-US/docs/Glossary/Localization)
    
*   [Leading](https://developer.mozilla.org/en-US/docs/Glossary/Leading)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#guides)

---------------------------------------------------------------------------------------

[Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)

The article explains how to use the CSS [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 properties to create and configure vertical form controls.

[Introduction to writing mode systems](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Writing_mode_systems)

A brief overview of writing mode systems and their directionalities.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#related_concepts)

-----------------------------------------------------------------------------------------------------------

[CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
 module

*   [`hanging-punctuation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    
*   [`line-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break)
    
*   [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    
*   [`text-align-last`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last)
    
*   [`text-indent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent)
    
*   [`text-justify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify)
    
*   [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
    

[CSS inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
 module

*   [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
    
*   [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
    
*   [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    
*   [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    
*   [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
    
*   [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
     shorthand
*   [`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
    

[CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module

*   [Flow relative values](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
    
*   [Inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
    
*   [Logical properties](https://developer.mozilla.org/en-US/docs/Glossary/Logical_properties)
    
*   [Physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
    

[CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
 module

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
    
*   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    

[CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)

*   [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
    

[SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)

*   [`glyph-orientation-horizontal`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/glyph-orientation-horizontal)
    
*   [`glyph-orientation-vertical`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/glyph-orientation-vertical)
    
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/writing-mode)
    

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

*   [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    
*   [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
    
*   [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    
*   [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
     attribute
*   [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
     attribute

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

*   [Internationalization guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Internationalization)
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
     object

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4](https://drafts.csswg.org/css-writing-modes/) |
| [CSS Writing Modes Level 3](https://drafts.csswg.org/css-writing-modes-3/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes#see_also)

-------------------------------------------------------------------------------------------

*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module
*   [CSS text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
     module: [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
     and [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module: [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
     and [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    
*   [CSS overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overscroll_behavior)
     module: [`overscroll-behavior-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-block)
     and [`overscroll-behavior-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/writing_modes/index.md?plain=1 "Folder: en-us/web/css/guides/writing_modes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWriting_modes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fwriting_modes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWriting_modes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fwriting_modes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa516a9818e8cef06c626d436ee1d73fc6d87ec51%0A*+Document+last+modified%3A+2026-05-11T22%3A57%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
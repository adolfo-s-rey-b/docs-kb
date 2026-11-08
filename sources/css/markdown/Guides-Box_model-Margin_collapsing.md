*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#mdn-search)
    

Mastering margin collapsing
===========================

The [top](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 and [bottom](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
 margins of blocks are sometimes combined (collapsed) into a single margin whose size is the largest of the individual margins (or just one of them, if they are equal), a behavior known as **margin collapsing**. Note that the margins of [floating](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 and [absolutely positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#types_of_positioning)
 elements never collapse.

Margin collapsing occurs in three basic cases:

[Adjacent siblings](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#adjacent_siblings)

The margins of adjacent siblings are collapsed (except when the latter sibling needs to be [cleared](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
 past floats).

[No content separating parent and descendants](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#no_content_separating_parent_and_descendants)

The vertical margins between a parent block and its descendants can collapse. This happens when there is no separating content between them. Specifically, this occurs in two main cases:

*   The [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
     of a parent collapses with the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
     of its first in-flow descendant unless the parent has a [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
     , [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
     , contains any inline content (such as text), or has _[clearance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
    _ applied.
*   The [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
     of a parent collapses with the [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
     of its last in-flow descendant unless the parent has a defined [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
     or [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    , a [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , or [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    .

In both cases, creating a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 on the parent will also prevent its margins from collapsing with its children.

[Empty blocks](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#empty_blocks)

If there is no border, padding, inline content, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, or [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
 to separate a block's [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 from its [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
, then its top and bottom margins collapse.

Some things to note:

*   More complex margin collapsing (of more than two margins) occurs when the above cases are combined.
*   These rules apply even to margins that are zero, so the margin of a descendant ends up outside its parent (according to the rules above) whether or not the parent's margin is zero.
*   When negative margins are involved, the size of the collapsed margin is the sum of the largest positive margin and the smallest (most negative) negative margin.
*   When all margins are negative, the size of the collapsed margin is the smallest (most negative) margin. This applies to both adjacent elements and nested elements.
*   Collapsing margins is only relevant in the vertical direction.
*   Margins don't collapse in a container with `display` set to `flex` or `grid`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#examples)

---------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#result)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing#see_also)

---------------------------------------------------------------------------------------------------------

*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module
*   [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    
*   CSS key concepts:
    *   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
        
    *   [At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
        
    *   [Comments](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments)
        
    *   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
        
    *   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
        
    *   [Layout modes](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
        
    *   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
        
    *   Values:
        *   [Initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
            
        *   [Computed values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
            
        *   [Used values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
            
        *   [Actual values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
            
    *   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
        
    *   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
        
    *   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_model/margin_collapsing/index.md?plain=1 "Folder: en-us/web/css/guides/box_model/margin_collapsing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_model%2FMargin_collapsing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_model%2Fmargin_collapsing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_model%2FMargin_collapsing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_model%2Fmargin_collapsing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#mdn-search)
    

Introduction to the CSS box model
=================================

When laying out a document, the browser's rendering engine represents each element as a rectangular box according to the standard **CSS basic box model**. CSS determines the size, position, and properties (color, background, border size, etc.) of these boxes.

Every box is composed of four parts (or _areas_), defined by their respective edges: the _content edge_, _padding edge_, _border edge_, and _margin edge_.

![CSS Box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction/boxmodel.png)

[Content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)

------------------------------------------------------------------------------------------------------------

The **content area**, bounded by the content edge, contains the "real" content of the element, such as text, an image, or a video player. Its dimensions are the _content width_ (or _content-box width_) and the _content height_ (or _content-box height_). It often has a background color or background image.

If the [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
 property is set to `content-box` (default) and if the element is a block element, the content area's size can be explicitly defined with the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
, and [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
 properties.

[Padding area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#padding_area)

------------------------------------------------------------------------------------------------------------

The **padding area**, bounded by the padding edge, extends the content area to include the element's padding. Its dimensions are the _padding-box width_ and the _padding-box height_.

The thickness of the padding is determined by the [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
, [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
, [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
, [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
, and shorthand [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 properties.

[Border area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#border_area)

----------------------------------------------------------------------------------------------------------

The **border area**, bounded by the border edge, extends the padding area to include the element's borders. Its dimensions are the _border-box width_ and the _border-box height_.

The thickness of the borders is determined by the [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
 and shorthand [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 properties. If the [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
 property is set to `border-box`, the border area's size can be explicitly defined with the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
, and [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
 properties. When there is a background ([`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 or [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
) set on a box, it extends to the outer edge of the border (i.e., extends underneath the border in z-ordering). This default behavior can be altered with the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 CSS property.

[Margin area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#margin_area)

----------------------------------------------------------------------------------------------------------

The **margin area**, bounded by the margin edge, extends the border area to include an empty area used to separate the element from its neighbors. Its dimensions are the _margin box width_ and the _margin box height_.

The size of the margin area is determined by the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
, [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
, [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
, [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
, and shorthand [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 properties. When [margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
 occurs, the margin area is not clearly defined since margins are shared between boxes.

Finally, note that for non-replaced inline elements, the amount of space taken up (the contribution to the height of the line) is determined by the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 property, even though the borders and padding are still displayed around the content.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#see_also)

----------------------------------------------------------------------------------------------------

*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module
*   [Layout and the containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    
*   [Introducing the CSS Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Learn: Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
    
*   CSS key concepts:
    *   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
        
    *   [At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
        
    *   [Comments](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments)
        
    *   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
        
    *   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
        
    *   [Layout modes](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
        
    *   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
        
    *   [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
        
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

This page was last modified on Sep 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_model/introduction/index.md?plain=1 "Folder: en-us/web/css/guides/box_model/introduction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_model%2FIntroduction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_model%2Fintroduction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_model%2FIntroduction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_model%2Fintroduction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F298079b550c76f20de6611c4ecdde4c30dc68b2b%0A*+Document+last+modified%3A+2026-09-22T10%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#mdn-search)
    

`justify-items` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2016.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`justify-items`** property defines the default [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 for all items of the box, giving them all a default way of justifying each box along the appropriate axis.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#try_it)

-----------------------------------------------------------------------------------------------------

The effect of this property is dependent of the layout mode we are in:

*   In block-level layouts, it aligns the items inside their containing block on the inline axis.
*   For absolutely-positioned elements, it aligns the items inside their containing block on the inline axis, accounting for the offset values of top, left, bottom, and right.
*   In table cell layouts, this property is _ignored_ (see [Box alignment for block, absolutely positioned, and table layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)
    )
*   In flexbox layouts, this property is _ignored_ (see [Box alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    )
*   In grid layouts, it aligns the items inside their grid areas on the inline axis (see [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    )

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#syntax)

-----------------------------------------------------------------------------------------------------

This property can take one of four different forms:

*   Basic keywords: one of the keyword values `normal` or `stretch`.
*   Baseline alignment: the `baseline` keyword, plus optionally one of `first` or `last`.
*   Positional alignment: one of: `center`, `start`, `end`, `flex-start`, `flex-end`, `self-start`, `self-end`, `left`, or `right`. Plus optionally `safe` or `unsafe`.
*   Legacy alignment: the `legacy` keyword, followed by one of `left`, `right`, or `center`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#normal)

The effect of this keyword is dependent of the layout mode we are in:

*   In block-level layouts, the keyword is a synonym of `start`.
*   In absolutely-positioned layouts, the keyword behaves like `start` on _replaced_ absolutely-positioned boxes, and as `stretch` on _all other_ absolutely-positioned boxes.
*   In table cell layouts, this keyword has no meaning as this property is _ignored_.
*   In flexbox layouts, this keyword has no meaning as this property is _ignored._
*   In grid layouts, this keyword leads to a behavior similar to the one of `stretch`, except for boxes with an aspect ratio or an intrinsic size where it behaves like `start`.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#start)

The item is packed flush to each other toward the start edge of the alignment container in the appropriate axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#end)

The item is packed flush to each other toward the end edge of the alignment container in the appropriate axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#flex-start)

For items that are not children of a flex container, this value is treated like `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#flex-end)

For items that are not children of a flex container, this value is treated like `end`.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#self-start)

The item is packed flush to the edge of the alignment container of the start side of the item, in the appropriate axis.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#self-end)

The item is packed flush to the edge of the alignment container of the end side of the item, in the appropriate axis.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#center)

The items are packed flush to each other toward the center of the alignment container.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#left)

The items are packed flush to each other toward the left edge of the alignment container. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#right)

The items are packed flush to each other toward the right edge of the alignment container in the appropriate axis. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group. The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#stretch)

If the combined size of the items is less than the size of the alignment container, any `auto`\-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size exactly fills the alignment container.

[`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#anchor-center)

In the case of [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 elements, aligns the items to the center of the associated anchor element in the inline direction. See [Centering on the anchor using `anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#safe)

If the size of the item overflows the alignment container, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#unsafe)

Regardless of the relative sizes of the item and alignment container, the given alignment value is honored.

[`legacy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#legacy)

Makes the value inherited by the box descendants. Note that if a descendant has a `justify-self: auto` value, the `legacy` keyword is not considered by the descend, only the `left`, `right`, or `center` value associated to it.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `legacy` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

justify-items =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <self-position> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  legacy                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  legacy [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
                   
  
[<baseline-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 last [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  baseline             
  
[<overflow-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
 =   
  unsafe  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  safe      
  
[<self-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
 =   
  center      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-end      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#examples)

---------------------------------------------------------------------------------------------------------

### [Basic demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#basic_demonstration)

In this example, we have a 2 x 2 grid layout. Initially the grid container is given a `justify-items` value of `stretch` (the default), which causes the grid items to stretch across the entire width of their cells.

If you hover or tab onto the grid container however, it is given a `justify-items` value of `center`, which causes the grid items to span only as wide as their content width, and align in the center of their cells.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# justify-items-property](https://drafts.csswg.org/css-align/#justify-items-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items#see_also)

---------------------------------------------------------------------------------------------------------

*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
     shorthand
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/justify-items/index.md?plain=1 "Folder: en-us/web/css/reference/properties/justify-items (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-items&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-items%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-items%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-items%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F07758d01509695fe45ccc3f7687f6597dc3d9e2a%0A*+Document+last+modified%3A+2026-09-02T04%3A34%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
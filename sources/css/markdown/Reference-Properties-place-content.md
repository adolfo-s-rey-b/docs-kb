*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#mdn-search)
    

`place-content` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`place-content`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property allows you to align content along both the block and inline directions at once (i.e., the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 properties) in a relevant layout system such as [Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 or [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#try_it)

-----------------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#syntax)

-----------------------------------------------------------------------------------------------------

The first value is the [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 property value, the second the [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 one.

**Note:** If the second value is not present, the first value is used for both, provided it is a valid value for both. If it is invalid for one or the other, the whole value will be invalid.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#values)

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#start)

The items are packed flush to each other toward the start edge of the alignment container in the appropriate axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#end)

The items are packed flush to each other toward the end edge of the alignment container in the appropriate axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#flex-start)

The items are packed flush to each other toward the edge of the alignment container depending on the flex container's main-start or cross-start side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#flex-end)

The items are packed flush to each other toward the edge of the alignment container depending on the flex container's main-end or cross-end side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `end`.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#center)

The items are packed flush to each other toward the center of the alignment container.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#left)

The items are packed flush to each other toward the left edge of the alignment container. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#right)

The items are packed flush to each other toward the right edge of the alignment container in the appropriate axis. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`space-between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#space-between)

The items are evenly distributed within the alignment container. The spacing between each pair of adjacent items is the same. The first item is flush with the main-start edge, and the last item is flush with the main-end edge.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group. The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`space-around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#space-around)

The items are evenly distributed within the alignment container. The spacing between each pair of adjacent items is the same. The empty space before the first and after the last item equals half of the space between each pair of adjacent items.

[`space-evenly`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#space-evenly)

The items are evenly distributed within the alignment container. The spacing between each pair of adjacent items, the main-start edge and the first item, and the main-end edge and the last item, are all exactly the same.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#stretch)

If the combined size of the items is less than the size of the alignment container, any `auto`\-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size exactly fills the alignment container

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#safe)

Used alongside an alignment keyword. If the chosen keyword means that the item overflows the alignment container causing data loss, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#unsafe)

Used alongside an alignment keyword. Regardless of the relative sizes of the item and alignment container, and regardless of whether overflow which causes data loss might happen, the given alignment value is honored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)<br>    : `normal`<br>*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)<br>    : `normal` |
| Applies to | multi-line flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)<br>    : as specified<br>*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

place-content =   
  [<'align-content'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 [<'justify-content'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<align-content>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 =   
  normal                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <content-distribution>                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <content-position>    
  
[<justify-content>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <content-distribution>                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <content-position> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<baseline-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 last [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  baseline             
  
[<content-distribution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
 =   
  space-between  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-around   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-evenly   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch          
  
[<overflow-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
 =   
  unsafe  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  safe      
  
[<content-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
 =   
  center      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex-end      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#examples)

---------------------------------------------------------------------------------------------------------

### [Placing content in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#placing_content_in_a_flex_container)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# place-content](https://drafts.csswg.org/css-align/#place-content) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content#see_also)

---------------------------------------------------------------------------------------------------------

*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/place-content/index.md?plain=1 "Folder: en-us/web/css/reference/properties/place-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
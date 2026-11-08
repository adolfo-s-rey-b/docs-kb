*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#mdn-search)
    

`place-self` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`place-self`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property allows you to align an individual item in both the block and inline directions at once (i.e., the [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties). This property applies to block-level boxes, absolutely-positioned boxes, and grid items. If the second value is not present, the first value is also used for it.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#try_it)

--------------------------------------------------------------------------------------------------

    place-self: stretch center;
    

    place-self: center start;
    

    place-self: start end;
    

    place-self: end center;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">One</div>
        <div>Two</div>
        <div>Three</div>
      </div>
    </section>
    

    .example-container {
      border: 1px solid #c5c5c5;
      display: grid;
      width: 220px;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 80px;
      grid-gap: 10px;
    }
    
    .example-container > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Positional alignment */
    place-self: auto center;
    place-self: normal start;
    place-self: center normal;
    place-self: start auto;
    place-self: end normal;
    place-self: self-start auto;
    place-self: self-end normal;
    place-self: flex-start auto;
    place-self: flex-end normal;
    place-self: anchor-center;
    
    /* Baseline alignment */
    place-self: baseline normal;
    place-self: first baseline auto;
    place-self: last baseline normal;
    place-self: stretch auto;
    
    /* Global values */
    place-self: inherit;
    place-self: initial;
    place-self: revert;
    place-self: revert-layer;
    place-self: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#values)

This property is specified as one or two of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#auto)

Computes to the parent's [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 value.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#normal)

The effect of this keyword is dependent of the layout mode we are in:

*   In absolutely-positioned layouts, the keyword behaves like `start` on _replaced_ absolutely-positioned boxes, and as `stretch` on _all other_ absolutely-positioned boxes.
*   In static position of absolutely-positioned layouts, the keyword behaves as `stretch`.
*   For flex items, the keyword behaves as `stretch`.
*   For grid items, this keyword leads to a behavior similar to the one of `stretch`, except for boxes with an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
     or an intrinsic size where it behaves like `start`.
*   The property doesn't apply to block-level boxes, and to table cells.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#self-start)

Aligns the items to be flush with the edge of the alignment container corresponding to the item's start side in the cross axis.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#self-end)

Aligns the items to be flush with the edge of the alignment container corresponding to the item's end side in the cross axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#flex-start)

The cross-start margin edge of the flex item is flushed with the cross-start edge of the line.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#flex-end)

The cross-end margin edge of the flex item is flushed with the cross-end edge of the line.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#center)

The flex item's margin box is centered within the line on the cross-axis. If the cross-size of the item is larger than the flex container, it will overflow equally in both directions.

[`baseline`, `first baseline`. `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group. The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#stretch)

If the combined size of the items along the cross axis is less than the size of the alignment container and the item is `auto`\-sized, its size is increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size of all `auto`\-sized items exactly fills the alignment container along the cross axis.

[`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#anchor-center)

In the case of [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 elements, aligns the item to the center of the associated anchor element in the block and inline direction. See [Centering on the anchor using `anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)<br>    : `auto`<br>*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)<br>    : `auto` |
| Applies to | block-level boxes, absolutely-positioned boxes, and grid items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)<br>    : `auto` computes to itself on absolutely-positioned elements, and to the computed value of [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)<br>     on the parent (minus any legacy keywords) on all other boxes, or `start` if the box has no parent. Its behavior depends on the layout model, as described for [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)<br>    . Otherwise the specified value.<br>*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#formal_syntax)

----------------------------------------------------------------------------------------------------------------

place-self =   
  [<'align-self'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 [<'justify-self'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<align-self>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 =   
  auto                                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <self-position> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  anchor-center                                        
  
[<justify-self>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 =   
  auto                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <self-position> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  anchor-center                                         
  
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
  
[<baseline-position>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 last [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  baseline             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#examples)

------------------------------------------------------------------------------------------------------

### [Basic demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#basic_demonstration)

In the following example we have a 2 x 2 grid layout. Initially the grid container has [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 and [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 values of `stretch` — the defaults — which causes the grid items to stretch across the entire width of their cells.

The second, third, and fourth grid items are then given different values of `place-self`, to show how these override the default placements. These values cause the grid items to span only as wide/tall as their content width/height, and align in different positions across their cells, in the block and inline directions.

#### HTML

html

    <article class="container">
      <span>First</span>
      <span>Second</span>
      <span>Third</span>
      <span>Fourth</span>
    </article>
    

#### CSS

css

    html {
      font-family: "Helvetica", "Arial", sans-serif;
      letter-spacing: 1px;
    }
    
    article {
      background-color: red;
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 80px;
      grid-gap: 10px;
      margin: 20px;
      width: 300px;
    }
    
    span:nth-child(2) {
      place-self: start center;
    }
    
    span:nth-child(3) {
      place-self: center start;
    }
    
    span:nth-child(4) {
      place-self: end;
    }
    
    article span {
      background-color: black;
      color: white;
      margin: 1px;
      text-align: center;
    }
    
    article,
    span {
      padding: 10px;
      border-radius: 7px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# place-self-property](https://drafts.csswg.org/css-align/#place-self-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self#see_also)

------------------------------------------------------------------------------------------------------

*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/place-self/index.md?plain=1 "Folder: en-us/web/css/reference/properties/place-self (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-self&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-self%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-self%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-self%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
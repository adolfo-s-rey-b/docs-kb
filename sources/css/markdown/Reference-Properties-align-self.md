*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#mdn-search)
    

`align-self` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`align-self`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property overrides a grid or flex item's [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 value. In grid, it aligns the item inside the [grid area](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
. In flexbox, it aligns the item on the [cross axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)
.

The property doesn't apply to block-level boxes, or to table cells. If a flexbox item's cross-axis margin is `auto`, then `align-self` is ignored.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#try_it)

--------------------------------------------------------------------------------------------------

    align-self: stretch;
    

    align-self: center;
    

    align-self: start;
    

    align-self: end;
    

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
      width: 200px;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 80px;
      grid-gap: 10px;
    }
    
    .example-container > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    align-self: auto;
    align-self: normal;
    
    /* Positional alignment */
    /* align-self does not take left and right values */
    align-self: center; /* Put the item around the center */
    align-self: start; /* Put the item at the start */
    align-self: end; /* Put the item at the end */
    align-self: self-start; /* Align the item flush at the start */
    align-self: self-end; /* Align the item flush at the end */
    align-self: flex-start; /* Put the flex item at the start */
    align-self: flex-end; /* Put the flex item at the end */
    align-self: anchor-center;
    
    /* Baseline alignment */
    align-self: baseline;
    align-self: first baseline;
    align-self: last baseline;
    align-self: stretch; /* Stretch 'auto'-sized items to fit the container */
    
    /* Overflow alignment */
    align-self: safe center;
    align-self: unsafe center;
    
    /* Global values */
    align-self: inherit;
    align-self: initial;
    align-self: revert;
    align-self: revert-layer;
    align-self: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#values)

This property is specified as one or two of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#auto)

Computes to the parent's [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 value.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#normal)

The effect of this keyword is dependent of the layout mode we are in:

*   In absolutely-positioned layouts, the keyword behaves like `start` on _replaced_ absolutely-positioned boxes, and as `stretch` on _all other_ absolutely-positioned boxes.
*   In static position of absolutely-positioned layouts, the keyword behaves as `stretch`.
*   For flex items, the keyword behaves as `stretch`.
*   For grid items, this keyword leads to a behavior similar to the one of `stretch`, except for boxes with an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
     or an intrinsic size where it behaves like `start`.
*   The property doesn't apply to block-level boxes, and to table cells.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#self-start)

Aligns the items to be flush with the edge of the alignment container corresponding to the item's start side in the cross axis.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#self-end)

Aligns the items to be flush with the edge of the alignment container corresponding to the item's end side in the cross axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#flex-start)

The cross-start margin edge of the flex item is flushed with the cross-start edge of the line.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#flex-end)

The cross-end margin edge of the flex item is flushed with the cross-end edge of the line.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#center)

The flex item's margin box is centered within the line on the cross-axis. If the cross-size of the item is larger than the flex container, it will overflow equally in both directions.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group. The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#stretch)

If the item's cross-size is `auto`, the used size is set to the length necessary to be as close to filling the container as possible, respecting the item's width and height limits. If the item is not auto-sized, this value falls back to `flex-start`, and to `self-start` or `self-end` if the container's [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 is `first baseline` (or `baseline`) or `last baseline`.

[`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#anchor-center)

In the case of [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 elements, aligns the item to the center of the associated anchor element in the block direction. See [Centering on the anchor using `anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#safe)

If the size of the item overflows the alignment container, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#unsafe)

Regardless of the relative sizes of the item and alignment container, the given alignment value is honored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | flex items, grid items, and absolutely-positioned boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `auto` computes to itself on absolutely-positioned elements, and to the computed value of [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)<br> on the parent (minus any legacy keywords) on all other boxes, or `start` if the box has no parent. Its behavior depends on the layout model, as described for [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)<br>. Otherwise the specified value. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#formal_syntax)

----------------------------------------------------------------------------------------------------------------

align-self =   
  auto                                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <self-position> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#examples)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#html)

html

    <section>
      <div>Item #1</div>
      <div>Item #2</div>
      <div>Item #3</div>
    </section>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#css)

css

    section {
      display: flex;
      align-items: center;
      height: 120px;
      background: beige;
    }
    
    div {
      height: 60px;
      background: cyan;
      margin: 5px;
    }
    
    div:nth-child(3) {
      align-self: flex-end;
      background: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# align-self-property](https://drafts.csswg.org/css-align/#align-self-property) |
| [CSS Flexible Box Layout Module Level 1  <br>\# align-items-property](https://drafts.csswg.org/css-flexbox/#align-items-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self#see_also)

------------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
    
*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/align-self/index.md?plain=1 "Folder: en-us/web/css/reference/properties/align-self (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-self&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-self%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-self%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-self%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
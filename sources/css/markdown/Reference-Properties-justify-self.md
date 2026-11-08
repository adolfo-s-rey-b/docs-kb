*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#mdn-search)
    

`justify-self` CSS property
===========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`justify-self`** property sets the way a box is justified inside its alignment container along the appropriate axis.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#try_it)

----------------------------------------------------------------------------------------------------

    justify-self: stretch;
    

    justify-self: center;
    

    justify-self: start;
    

    justify-self: end;
    

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
      grid-auto-rows: 40px;
      grid-gap: 10px;
    }
    
    .example-container > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

The effect of this property is dependent of the layout mode we are in:

*   In block-level layouts, it aligns an item inside its containing block on the inline axis.
*   For absolutely-positioned elements, it aligns an item inside its containing block on the inline axis, accounting for the offset values of top, left, bottom, and right.
*   In table cell layouts, this property is _ignored_. Read more about [alignment in block, absolute positioned and table layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)
    .
*   In flexbox layouts, this property is _ignored_. Read more about [alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    .
*   In grid layouts, it aligns an item inside its grid area on the inline axis. Read more about [alignment in grid layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    .

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Basic keywords */
    justify-self: auto;
    justify-self: normal;
    justify-self: stretch;
    
    /* Positional alignment */
    justify-self: center; /* Pack item around the center */
    justify-self: start; /* Pack item from the start */
    justify-self: end; /* Pack item from the end */
    justify-self: flex-start; /* Equivalent to 'start'. Note that justify-self is ignored in flexbox layouts. */
    justify-self: flex-end; /* Equivalent to 'end'. Note that justify-self is ignored in flexbox layouts. */
    justify-self: self-start;
    justify-self: self-end;
    justify-self: left; /* Pack item from the left */
    justify-self: right; /* Pack item from the right */
    justify-self: anchor-center;
    
    /* Baseline alignment */
    justify-self: baseline;
    justify-self: first baseline;
    justify-self: last baseline;
    
    /* Overflow alignment (for positional alignment only) */
    justify-self: safe center;
    justify-self: unsafe center;
    
    /* Global values */
    justify-self: inherit;
    justify-self: initial;
    justify-self: revert;
    justify-self: revert-layer;
    justify-self: unset;
    

This property can take one of three different forms:

*   Basic keywords: one of the keyword values `normal`, `auto`, or `stretch`.
*   Baseline alignment: the `baseline` keyword, plus optionally one of `first` or `last`.
*   Positional alignment:
    *   one of: `center`, `start`, `end`, `flex-start`, `flex-end`, `self-start`, `self-end`, `left`, or `right`.
    *   Plus optionally `safe` or `unsafe`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#auto)

The value used is the value of the `justify-items` property of the parents box, unless the box has no parent, or is absolutely positioned, in these cases, `auto` represents `normal`.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#normal)

The effect of this keyword is dependent of the layout mode we are in:

*   In block-level layouts, the keyword is a synonym of `start`.
*   In absolutely-positioned layouts, the keyword behaves like `start` on _replaced_ absolutely-positioned boxes, and as `stretch` on _all other_ absolutely-positioned boxes.
*   In table cell layouts, this keyword has no meaning as this property is _ignored_.
*   In flexbox layouts, this keyword has no meaning as this property is _ignored._
*   In grid layouts, this keyword leads to a behavior similar to the one of `stretch`, except for boxes with an aspect ratio or an intrinsic size where it behaves like `start`.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#start)

The item is packed flush to each other toward the start edge of the alignment container in the appropriate axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#end)

The item is packed flush to each other toward the end edge of the alignment container in the appropriate axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#flex-start)

For items that are not children of a flex container, this value is treated like `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#flex-end)

For items that are not children of a flex container, this value is treated like `end`.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#self-start)

The item is packed flush to the edge of the alignment container of the start side of the item, in the appropriate axis.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#self-end)

The item is packed flush to the edge of the alignment container of the end side of the item, in the appropriate axis.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#center)

The items are packed flush to each other toward the center of the alignment container.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#left)

The items are packed flush to each other toward the left edge of the alignment container. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#right)

The items are packed flush to each other toward the right edge of the alignment container in the appropriate axis. If the property's axis is not parallel with the inline axis, this value behaves like `start`.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group. The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#stretch)

If the combined size of the items is less than the size of the alignment container, any `auto`\-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size exactly fills the alignment container.

[`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#anchor-center)

In the case of [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 elements, aligns the item to the center of the associated anchor element in the inline direction. See [Centering on the anchor using `anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#safe)

If the size of the item overflows the alignment container, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#unsafe)

Regardless of the relative sizes of the item and alignment container, the given alignment value is honored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block-level boxes, absolutely-positioned boxes, and grid items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#formal_syntax)

------------------------------------------------------------------------------------------------------------------

justify-self =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#examples)

--------------------------------------------------------------------------------------------------------

### [Basic demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#basic_demonstration)

In the following example we have a 2 x 2 grid layout. Initially the grid container is given a `justify-items` value of `stretch` — the default — which causes the grid items to stretch across the entire width of their cells.

The second, third, and fourth grid items are then given different values of `justify-self`, to show how these override the `justify-items` value. These values cause the grid items to span only as wide as their content width, and align in different positions across their cells.

#### HTML

html

    <article class="container">
      <span>First child</span>
      <span>Second child</span>
      <span>Third child</span>
      <span>Fourth child</span>
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
      grid-auto-rows: 40px;
      grid-gap: 10px;
      margin: 20px;
      width: 300px;
      justify-items: stretch;
    }
    
    span:nth-child(2) {
      justify-self: start;
    }
    
    span:nth-child(3) {
      justify-self: center;
    }
    
    span:nth-child(4) {
      justify-self: end;
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

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# justify-self-property](https://drafts.csswg.org/css-align/#justify-self-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self#see_also)

--------------------------------------------------------------------------------------------------------

*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`place-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/justify-self/index.md?plain=1 "Folder: en-us/web/css/reference/properties/justify-self (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-self&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-self%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fjustify-self%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fjustify-self%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
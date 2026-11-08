*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#mdn-search)
    

`align-items` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`align-items`** property sets the [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 value on all direct children as a group. In flexbox, it controls the alignment of items on the [cross axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)
. In grid layout, it controls the alignment of items on the block axis within their [grid areas](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Areas)
.

The interactive example below uses grid layout to demonstrate some of the values of this property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#try_it)

---------------------------------------------------------------------------------------------------

    align-items: stretch;
    

    align-items: center;
    

    align-items: start;
    

    align-items: end;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One</div>
          <div>Two</div>
          <div>Three</div>
        </div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      display: grid;
      width: 200px;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 80px;
      grid-gap: 10px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Basic keywords */
    align-items: normal;
    align-items: stretch;
    
    /* Positional alignment */
    /* align-items does not take left and right values */
    align-items: center;
    align-items: start;
    align-items: end;
    align-items: flex-start;
    align-items: flex-end;
    align-items: self-start;
    align-items: self-end;
    align-items: anchor-center;
    
    /* Baseline alignment */
    align-items: baseline;
    align-items: first baseline;
    align-items: last baseline;
    
    /* Overflow alignment (for positional alignment only) */
    align-items: safe center;
    align-items: unsafe center;
    
    /* Global values */
    align-items: inherit;
    align-items: initial;
    align-items: revert;
    align-items: revert-layer;
    align-items: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#values)

This property is specified as one or two of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#normal)

The effect of this keyword is dependent of the layout mode we are in:

*   In absolutely-positioned layouts, the keyword behaves like `start` on _replaced_ absolutely-positioned boxes, and as `stretch` on _all other_ absolutely-positioned boxes.
*   In static position of absolutely-positioned layouts, the keyword behaves as `stretch`.
*   For flex items, the keyword behaves as `stretch`.
*   For grid items, this keyword leads to a behavior similar to the one of `stretch`, except for boxes with an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
     or an intrinsic size where it behaves like `start`.
*   The property doesn't apply to block-level boxes, and to table cells.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#center)

The flex items' margin boxes are centered within the line on the cross-axis. If the cross-size of an item is larger than the flex container, it will overflow equally in both directions.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#start)

The items are packed flush to each other toward the start edge of the alignment container in the appropriate axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#end)

The items are packed flush to each other toward the end edge of the alignment container in the appropriate axis.

[`self-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#self-start)

The items are packed flush to the edge of the alignment container's start side of the item, in the appropriate axis.

[`self-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#self-end)

The items are packed flush to the edge of the alignment container's end side of the item, in the appropriate axis.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#baseline)

All flex items are aligned such that their [flex container baselines](https://drafts.csswg.org/css-flexbox-1/#flex-baselines "External link (opens in new tab)")
 align. The item with the largest distance between its cross-start margin edge and its baseline is flushed with the cross-start edge of the line.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#stretch)

If the item's cross-size is `auto`, the used size is set to the length necessary to be as close to filling the container as possible, respecting the item's width and height limits. If the item is not auto-sized, this value falls back to `flex-start`, and to `self-start` or `self-end` if the container's [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
 is `first baseline` (or `baseline`) or `last baseline`.

[`anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#anchor-center)

In the case of [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 elements, aligns the items to the center of the associated anchor element in the block direction. See [Centering on the anchor using `anchor-center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#centering_on_the_anchor_using_anchor-center)
.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#safe)

Used alongside an alignment keyword. If the chosen keyword means that the item overflows the alignment container causing data loss, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#unsafe)

Used alongside an alignment keyword. Regardless of the relative sizes of the item and alignment container and whether overflow which causes data loss might happen, the given alignment value is honored.

There are also two values that were defined for flexbox, as they are base on [flex model axes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox#the_flex_model)
 concepts, that work in grid layouts as well:

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#flex-start)

Used in flex layout only, aligns the flex items flush against the flex container's main-start or cross-start side. When used outside of a flex formatting context, this value behaves as `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#flex-end)

Used in flex layout only, aligns the flex items flush against the flex container's main-end or cross-end side. When used outside of a flex formatting context, this value behaves as `end`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

align-items =   
  normal                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <self-position>    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#examples)

-------------------------------------------------------------------------------------------------------

In this example we have a container with six children. A [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 dropdown menu enables toggling the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 of the container between `grid` and `flex`. A second menu enables changing the value of the container's `align-items` property.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#css)

We style the container and items in a manner that ensures we have two lines or rows of items. We defined `.flex` and `.grid` classes, which will be applied to the container with JavaScript. They set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of the container, and change its background and border colors providing an additional indicator that the layout has changed. The six flex items each have a different background color, with the 4th item being two lines long and the 6th item having an enlarged font.

css

    .flex,
    .grid {
      height: 200px;
      width: 500px;
      align-items: initial; /* Change the value in the live sample */
      border: solid 5px transparent;
      gap: 3px;
    }
    
    .flex {
      display: flex;
      flex-wrap: wrap;
      background-color: #8c8c9f;
      border-color: magenta;
    }
    
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, 100px);
      background-color: #9f8c8c;
      border-color: slateblue;
    }
    
    #item1 {
      background-color: #8cffa0;
      min-height: 30px;
    }
    
    #item2 {
      background-color: #a0c8ff;
      min-height: 50px;
    }
    
    #item3 {
      background-color: #ffa08c;
      min-height: 40px;
    }
    
    #item4 {
      background-color: #ffff8c;
      min-height: 60px;
    }
    
    #item5 {
      background-color: #ff8cff;
      min-height: 70px;
    }
    
    #item6 {
      background-color: #8cffff;
      min-height: 50px;
      font-size: 30px;
    }
    

    select {
      font-size: 16px;
    }
    
    .row {
      margin-top: 10px;
    }
    
    div > div {
      box-sizing: border-box;
      border: 2px solid white;
      width: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#html)

We include a container [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 with six nested `<div>` children. The HTML for the form and the JavaScript that changes the container's class have been hidden for the sake of brevity.

html

    <div id="container" class="flex">
      <div id="item1">1</div>
      <div id="item2">2</div>
      <div id="item3">3</div>
      <div id="item4">4<br />line 2</div>
      <div id="item5">5</div>
      <div id="item6">6</div>
    </div>
    

    <div class="row">
      <label for="display">display: </label>
      <select id="display">
        <option value="flex">flex</option>
        <option value="grid">grid</option>
      </select>
    </div>
    
    <div class="row">
      <label for="values">align-items: </label>
      <select id="values">
        <option value="normal">normal</option>
        <option value="flex-start">flex-start</option>
        <option value="flex-end">flex-end</option>
        <option value="center" selected>center</option>
        <option value="baseline">baseline</option>
        <option value="stretch">stretch</option>
    
        <option value="start">start</option>
        <option value="end">end</option>
        <option value="self-start">self-start</option>
        <option value="self-end">self-end</option>
    
        <option value="first baseline">first baseline</option>
        <option value="last baseline">last baseline</option>
    
        <option value="safe center">safe center</option>
        <option value="unsafe center">unsafe center</option>
        <option value="safe right">safe right</option>
        <option value="unsafe right">unsafe right</option>
        <option value="safe end">safe end</option>
        <option value="unsafe end">unsafe end</option>
        <option value="safe self-end">safe self-end</option>
        <option value="unsafe self-end">unsafe self-end</option>
        <option value="safe flex-end">safe flex-end</option>
        <option value="unsafe flex-end">unsafe flex-end</option>
      </select>
    </div>
    

    const values = document.getElementById("values");
    const display = document.getElementById("display");
    const container = document.getElementById("container");
    
    values.addEventListener("change", (evt) => {
      container.style.alignItems = evt.target.value;
    });
    
    display.addEventListener("change", (evt) => {
      container.className = evt.target.value;
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# align-items-property](https://drafts.csswg.org/css-align/#align-items-property) |
| [CSS Flexible Box Layout Module Level 1  <br>\# align-items-property](https://drafts.csswg.org/css-flexbox/#align-items-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items#see_also)

-------------------------------------------------------------------------------------------------------

*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
     shorthand
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/align-items/index.md?plain=1 "Folder: en-us/web/css/reference/properties/align-items (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-items&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-items%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-items%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-items%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
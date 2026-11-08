*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#mdn-search)
    

`align-content` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **`align-content`** property sets the distribution of space between and around content items along a [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
's [cross axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)
, or a [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 or [block-level](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
 element's block axis.

This property has no effect on single line flex containers (i.e., ones with `flex-wrap: nowrap`).

The interactive example below uses grid layout to demonstrate some of the values of this property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#try_it)

-----------------------------------------------------------------------------------------------------

    align-content: start;
    

    align-content: center;
    

    align-content: space-between;
    

    align-content: space-around;
    

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
      grid-template-columns: 60px 60px;
      grid-auto-rows: 40px;
      column-gap: 10px;
      height: 180px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Normal alignment */
    align-content: normal;
    
    /* Basic positional alignment */
    /* align-content does not take left and right values */
    align-content: start;
    align-content: center;
    align-content: end;
    align-content: flex-start;
    align-content: flex-end;
    
    /* Baseline alignment */
    align-content: baseline;
    align-content: first baseline;
    align-content: last baseline;
    
    /* Distributed alignment */
    align-content: space-between;
    align-content: space-around;
    align-content: space-evenly;
    align-content: stretch;
    
    /* Overflow alignment */
    align-content: safe center;
    align-content: unsafe center;
    
    /* Global values */
    align-content: inherit;
    align-content: initial;
    align-content: revert;
    align-content: revert-layer;
    align-content: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#values)

This property is specified as one or two of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#normal)

The items are packed in their default position as if no `align-content` value was set.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#start)

The items are packed flush to each other against the start edge of the alignment container in the cross axis.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#center)

The items are packed flush to each other in the center of the alignment container along the cross axis.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#end)

The items are packed flush to each other against the end edge of the alignment container in the cross axis.

[`flex-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#flex-start)

The items are packed flush to each other against the edge of the alignment container depending on the flex container's cross-start side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `start`.

[`flex-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#flex-end)

The items are packed flush to each other against the edge of the alignment container depending on the flex container's cross-end side. This only applies to flex layout items. For items that are not children of a flex container, this value is treated like `end`.

[`baseline`, `first baseline`, `last baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#baseline)

Specifies participation in first- or last-baseline alignment: aligns the alignment baseline of the box's first or last baseline set with the corresponding baseline in the shared first or last baseline set of all the boxes in its baseline-sharing group.

![the baseline is the line upon which most letters "sit" and below which descenders extend.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content/410px-typography_line_terms.svg.png)

The fallback alignment for `first baseline` is `start`, the one for `last baseline` is `end`.

[`space-between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#space-between)

The items are evenly distributed within the alignment container along the cross axis. The spacing between each pair of adjacent items is the same. The first item is flush with the start edge of the alignment container in the cross axis, and the last item is flush with the end edge of the alignment container in the cross axis.

[`space-around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#space-around)

The items are evenly distributed within the alignment container along the cross axis. The spacing between each pair of adjacent items is the same. The empty space before the first and after the last item equals half of the space between each pair of adjacent items.

[`space-evenly`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#space-evenly)

The items are evenly distributed within the alignment container along the cross axis. The spacing between each pair of adjacent items, the start edge and the first item, and the end edge and the last item, are all exactly the same.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#stretch)

If the combined size of the items along the cross axis is less than the size of the alignment container, any `auto`\-sized items have their size increased equally (not proportionally), while still respecting the constraints imposed by [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
/[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 (or equivalent functionality), so that the combined size exactly fills the alignment container along the cross axis.

[`safe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#safe)

Used alongside an alignment keyword. If the chosen keyword means that the item overflows the alignment container causing data loss, the item is instead aligned as if the alignment mode were `start`.

[`unsafe`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#unsafe)

Used alongside an alignment keyword. Regardless of the relative sizes of the item and alignment container and whether overflow which causes data loss might happen, the given alignment value is honored.

**Note:** The `<content-distribution>` values (`space-between`, `space-around`, `space-evenly`, and `stretch`) have no effect in [block layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#align-content_and_justify-content)
 as all the content in that block is treated as a single [alignment-subject](https://developer.mozilla.org/en-US/docs/Glossary/Alignment_Subject)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | Block-containers, multi-column containers, flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

align-content =   
  normal                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <content-distribution>                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <content-position>    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#examples)

---------------------------------------------------------------------------------------------------------

### [Effects of different align-content values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#effects_of_different_align-content_values)

In this example, you can switch between three different [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property values, including `flex`, `grid`, and `block`. You can also switch between the different values for `align-content`.

#### HTML

html

    <section>
      <div class="olive">Olive</div>
      <div class="coral">Coral</div>
      <div class="deepskyblue">Deep<br />sky<br />blue</div>
      <div class="orchid">Orchid</div>
      <div class="slateblue">Slateblue</div>
      <div class="maroon">Maroon</div>
    </section>
    

    <fieldset class="controls">
      <legend>Controls</legend>
      <div class="row">
        <label for="display">display: </label>
        <select id="display">
          <option value="block" selected>block</option>
          <option value="flex">flex</option>
          <option value="grid">grid</option>
        </select>
      </div>
      <div class="row">
        <label for="alignContent">align-content: </label>
        <select id="alignContent">
          <option value="normal" selected>normal</option>
          <option value="start">start</option>
          <option value="center">center</option>
          <option value="end">end</option>
          <option value="flex-start">flex-start</option>
          <option value="flex-end">flex-end</option>
          <option value="space-between">space-between</option>
          <option value="space-around">space-around</option>
          <option value="space-evenly">space-evenly</option>
        </select>
      </div>
      <p>CSS applied</p>
      <pre>
    section {
      display: <span id="displayStyle">block</span>;
      align-content: <span id="align">normal</span>
    }
      </pre>
    </fieldset>
    

#### CSS

    body {
      font-size: 1.25rem;
      display: flex;
      gap: 1rem;
    }
    section div {
      font-family: monospace;
      padding: 3px;
    }
    

css

    section {
      border: solid 1.5px tomato;
      height: 300px;
      width: 300px;
      flex-wrap: wrap; /* used by flex only */
      gap: 0.2rem; /* not used by block */
    }
    .olive {
      background-color: olive;
    }
    .coral {
      background-color: coral;
    }
    .deepskyblue {
      background-color: deepskyblue;
    }
    .orchid {
      background-color: orchid;
    }
    .slateblue {
      background-color: slateblue;
      color: white;
    }
    .maroon {
      background-color: maroon;
      color: white;
    }
    

    const alignContent = document.querySelector("#alignContent");
    const display = document.querySelector("#display");
    const container = document.querySelector("section");
    const displayStyle = document.querySelector("#displayStyle");
    const alignStyle = document.querySelector("#align");
    
    alignContent.addEventListener("change", () => {
      updatePage();
    });
    display.addEventListener("change", () => {
      updatePage();
    });
    function updatePage() {
      const alVal = alignContent.value;
      const dVal = display.value;
      container.style.alignContent = alVal;
      container.style.display = dVal;
      alignStyle.innerText = alVal;
      displayStyle.innerText = dVal;
    }
    updatePage();
    

#### Result

Try changing the `display` value and the `align-content` value.

In [block layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables#align-content_and_justify-content)
, child elements are treated as a single element, meaning `space-between`, `space-around`, and `space-evenly` behave differently.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# align-justify-content](https://drafts.csswg.org/css-align/#align-justify-content) |
| [CSS Flexible Box Layout Module Level 1  <br>\# align-content-property](https://drafts.csswg.org/css-flexbox/#align-content-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content#see_also)

---------------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
    
*   [Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout)
    
*   [Block-level content](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
    
*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/align-content/index.md?plain=1 "Folder: en-us/web/css/reference/properties/align-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falign-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falign-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
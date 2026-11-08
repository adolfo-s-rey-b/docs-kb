*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#mdn-search)
    

`place-items` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`place-items`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property aligns items along both block and inline directions at the same time.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#try_it)

---------------------------------------------------------------------------------------------------

    place-items: center stretch;
    

    place-items: center start;
    

    place-items: start end;
    

    place-items: end center;
    

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
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 80px;
      grid-gap: 10px;
      width: 220px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Positional alignment */
    place-items: center;
    place-items: normal start;
    place-items: center normal;
    place-items: start legacy;
    place-items: end normal;
    place-items: self-start legacy;
    place-items: self-end normal;
    place-items: flex-start legacy;
    place-items: flex-end normal;
    place-items: anchor-center;
    
    /* Baseline alignment */
    place-items: baseline normal;
    place-items: first baseline legacy;
    place-items: last baseline normal;
    place-items: stretch legacy;
    
    /* Global values */
    place-items: inherit;
    place-items: initial;
    place-items: revert;
    place-items: revert-layer;
    place-items: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#values)

This property is specified as one or two space-separated values of the following types, in the order listed:

[`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)

Specifies the alignment in the block direction.

[`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 Optional

Specifies the alignment in the inline direction. If omitted, the `align-items` value is used.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#description)

-------------------------------------------------------------------------------------------------------------

The `place-items` shorthand property sets [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 and [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 in a single declaration, aligning items along both the block and inline directions.

If only one value is provided, the value is used to set alignment in both block and inline directions. If two values are provided, the first value is the [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 value, setting the alignment in the block direction, and the second value is the [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 value, setting alignment in the inline direction.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)<br>    : `normal`<br>*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)<br>    : `legacy` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)<br>    : as specified<br>*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

place-items =   
  [<'align-items'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 [<'justify-items'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<align-items>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 =   
  normal                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-position>                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <overflow-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 <self-position>    
  
[<justify-items>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#examples)

-------------------------------------------------------------------------------------------------------

### [Placing items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#placing_items_in_a_flex_container)

In flexbox [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 or [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
 do not apply, as on the main axis items are treated as a group. Therefore, the second value will be ignored.

    div > div {
      box-sizing: border-box;
      border: 2px solid #8c8c8c;
      width: 50px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    
    #item1 {
      background-color: #8cffa0;
      min-height: 30px;
      font-size: 2em;
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
    }
    
    select {
      font-size: 16px;
    }
    
    .row {
      margin-top: 10px;
    }
    

    <div id="container">
      <div id="item1">1</div>
      <div id="item2">2</div>
      <div id="item3">3</div>
    </div>
    
    <div class="row">
      <label for="values">place-items: </label>
      <select id="values">
        <option value="stretch">stretch</option>
        <option value="start">start</option>
        <option value="center">center</option>
        <option value="end">end</option>
        <option value="left">left</option>
        <option value="right">right</option>
        <option value="auto center">auto center</option>
        <option value="normal start">normal start</option>
        <option value="center normal">center normal</option>
        <option value="start auto">start auto</option>
        <option value="end normal">end normal</option>
        <option value="self-start auto">self-start auto</option>
        <option value="self-end normal">self-end normal</option>
        <option value="flex-start auto">flex-start auto</option>
        <option value="flex-end normal">flex-end normal</option>
        <option value="left auto">left auto</option>
        <option value="right normal">right normal</option>
        <option value="baseline normal">baseline normal</option>
        <option value="first baseline auto">first baseline auto</option>
        <option value="last baseline normal">last baseline normal</option>
        <option value="stretch auto">stretch auto</option>
      </select>
    </div>
    

    const values = document.getElementById("values");
    const container = document.getElementById("container");
    
    values.addEventListener("change", (evt) => {
      container.style.placeItems = evt.target.value;
    });
    

#### CSS

css

    #container {
      height: 200px;
      width: 240px;
      place-items: stretch; /* You can change this value by selecting another option in the list */
      background-color: #8c8c8c;
      display: flex;
    }
    

#### Result

### [Placing items in a grid container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#placing_items_in_a_grid_container)

The following grid container has items which are smaller than the grid areas they are placed in, therefore `place-items` will move them in the block and inline dimensions.

    div > div {
      box-sizing: border-box;
      border: 2px solid #8c8c8c;
    }
    
    #item1 {
      background-color: #8cffa0;
      min-height: 30px;
      font-size: 2em;
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
    }
    
    select {
      font-size: 16px;
    }
    
    .row {
      margin-top: 10px;
    }
    

    <div id="grid-container">
      <div id="item1">1</div>
      <div id="item2">2</div>
      <div id="item3">3</div>
      <div id="item4">4</div>
      <div id="item5">5</div>
    </div>
    
    <div class="row">
      <label for="grid-values">place-items: </label>
      <select id="grid-values">
        <option value="stretch">stretch</option>
        <option value="start">start</option>
        <option value="center">center</option>
        <option value="end">end</option>
        <option value="left">left</option>
        <option value="right">right</option>
        <option value="auto center">auto center</option>
        <option value="normal start">normal start</option>
        <option value="center normal">center normal</option>
        <option value="start auto">start auto</option>
        <option value="end normal">end normal</option>
        <option value="self-start auto">self-start auto</option>
        <option value="self-end normal">self-end normal</option>
        <option value="flex-start auto">flex-start auto</option>
        <option value="flex-end normal">flex-end normal</option>
        <option value="left auto">left auto</option>
        <option value="right normal">right normal</option>
        <option value="baseline normal">baseline normal</option>
        <option value="first baseline auto">first baseline auto</option>
        <option value="last baseline normal">last baseline normal</option>
        <option value="stretch auto">stretch auto</option>
      </select>
    </div>
    

    const values = document.getElementById("grid-values");
    const container = document.getElementById("grid-container");
    
    values.addEventListener("change", (evt) => {
      container.style.placeItems = evt.target.value;
    });
    

#### CSS

css

    #grid-container {
      height: 200px;
      width: 240px;
      place-items: stretch; /* You can change this value by selecting another option in the list */
      background-color: #8c8c8c;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
    }
    
    #grid-container > div {
      width: 50px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Alignment Module Level 3  <br>\# place-items-property](https://drafts.csswg.org/css-align/#place-items-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items#see_also)

-------------------------------------------------------------------------------------------------------

*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`justify-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Aligning items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Box alignment in grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/place-items/index.md?plain=1 "Folder: en-us/web/css/reference/properties/place-items (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-items&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-items%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fplace-items%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fplace-items%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6354422058e438a2599e4eab71eaec8eb40850fa%0A*+Document+last+modified%3A+2026-09-14T09%3A57%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
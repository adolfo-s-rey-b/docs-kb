*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#mdn-search)
    

`flex-wrap` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-wrap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether flex items are forced onto one line or can wrap onto multiple lines. If wrapping is allowed, it sets the direction that lines are stacked.

The [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 property shorthand can be used to set both the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 and `flex-wrap` properties, which define the flex container's main and cross axes, respectively.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#try_it)

-------------------------------------------------------------------------------------------------

    flex-wrap: nowrap;
    

    flex-wrap: wrap;
    

    flex-wrap: wrap-reverse;
    

    flex-wrap: wrap balance;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div>Item One</div>
        <div>Item Two</div>
        <div>Item Three</div>
        <div>Item Four</div>
        <div>Item Five</div>
        <div>Item Six</div>
        <div>Item Seven</div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      width: 80%;
      display: flex;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      width: 60px;
      margin: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    flex-wrap: nowrap;
    flex-wrap: wrap;
    flex-wrap: wrap-reverse;
    flex-wrap: balance;
    flex-wrap: wrap balance;
    flex-wrap: balance wrap-reverse;
    
    /* Global values */
    flex-wrap: inherit;
    flex-wrap: initial;
    flex-wrap: revert;
    flex-wrap: revert-layer;
    flex-wrap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#values)

This property is specified as a single value from the following list or as two space-separated values when using `balance`:

[`nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#nowrap)

The flex items are laid out in a single line which may cause the flex container to overflow. This is the initial value.

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#wrap)

The flex items can break into multiple lines.

[`wrap-reverse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#wrap-reverse)

Behaves the same as `wrap`, but with the lines laid out in reverse order.

[`balance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#balance)

Specifies that flex items broken across multiple lines are distributed so that the line lengths are as similar as possible. If `balance` is specified as the only keyword, the other keyword defaults to `wrap`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#description)

-----------------------------------------------------------------------------------------------------------

The `flex-wrap` property is used to specify whether the flex container's child flex items may wrap onto multiple flex lines or not and, if set to wrap, whether the children should be evenly distributed across flex lines.

The initial value of `nowrap` specifies that all items should be laid out on a single flex line, which means they may overflow the container. The `wrap` and `wrap-reverse` keywords prevent overflow by specifying that flex items can flow, or wrap, across multiple lines.

With `wrap`, cross-start is the equivalent of [inline-start or block-start](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
, depending on the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 value and the current [writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
. With `wrap-reverse`, cross-start is the equivalent of inline-end or block-end.

### [Balancing flex item distribution](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#balancing_flex_item_distribution)

By default, when `wrap` or `wrap-reverse` is specified, each flex line is filled with flex items before items are wrapped onto the next line. This can result in an uneven distribution of items, with the last flex line composed of fewer items. If those items' [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 values are non-zero, the extra available space is distributed across these fewer items, making them much larger than the items on filled flex lines.

The `balance` keyword can be used to distribute the items across lines in a more even manner. Optionally, the [`flex-line-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
 property can be used to define the minimum number of lines across which the balanced items should be distributed.

If `balance` is the only keyword specified, the other keyword defaults to `wrap`.

A balanced wrapping flex container can have a [`flex-line-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
 value applied to specify the minimum number of lines the flex items should be distributed over. The `flex-line-count` property has no effect if `balance` is not specified inside `flex-wrap`.

If `balance` is specified alongside `nowrap`, the property is invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `nowrap` |
| Applies to | flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#formal_syntax)

---------------------------------------------------------------------------------------------------------------

flex-wrap =   
  nowrap                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 wrap [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 wrap-reverse [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 balance    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#examples)

-----------------------------------------------------------------------------------------------------

### [Setting flex container wrap values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#setting_flex_container_wrap_values)

#### HTML

html

    <h4>This is an example for flex-wrap:wrap</h4>
    <div class="content">
      <div class="red">1</div>
      <div class="green">2</div>
      <div class="blue">3</div>
    </div>
    <h4>This is an example for flex-wrap:nowrap</h4>
    <div class="content1">
      <div class="red">1</div>
      <div class="green">2</div>
      <div class="blue">3</div>
    </div>
    <h4>This is an example for flex-wrap:wrap-reverse</h4>
    <div class="content2">
      <div class="red">1</div>
      <div class="green">2</div>
      <div class="blue">3</div>
    </div>
    

#### CSS

css

    /* Common Styles */
    .content,
    .content1,
    .content2 {
      color: white;
      font: 100 24px/100px sans-serif;
      height: 150px;
      width: 897px;
      text-align: center;
    }
    
    .content div,
    .content1 div,
    .content2 div {
      height: 50%;
      width: 300px;
    }
    .red {
      background: orangered;
    }
    .green {
      background: yellowgreen;
    }
    .blue {
      background: steelblue;
    }
    
    /* Flexbox Styles */
    .content {
      display: flex;
      flex-wrap: wrap;
    }
    .content1 {
      display: flex;
      flex-wrap: nowrap;
    }
    .content2 {
      display: flex;
      flex-wrap: wrap-reverse;
    }
    

#### Results

### [Demonstrating the `balance` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#demonstrating_the_balance_keyword)

This example demonstrates the effects of the `balance` keyword within the `flex-wrap` property and different `flex-line-count` values.

#### HTML

    <form>
      <div>
        <input type="checkbox" id="reverse" name="reverse" />
        <label for="reverse">Set <code>wrap-reverse</code>?</label>
      </div>
      <div>
        <input type="checkbox" id="balance" name="balance" checked />
        <label for="balance">Set <code>balance</code>?</label>
      </div>
      <div>
        <label for="line-count"><code>flex-line-count</code></label>
        <input
          type="range"
          id="line-count"
          name="line-count"
          min="1"
          max="12"
          value="3" />
        <output>3</output>
      </div>
    </form>
    
    <hr />
    
    <p>Currently set: <code>flex-wrap: wrap; flex-line-count: 3;</code></p>
    
    <hr />
    

We include a container [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 with a `class` of `box`, which has ten child `<div>`s.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
      <div>Eight</div>
      <div>Nine</div>
      <div>Ten</div>
    </div>
    

We also include controls to enable changing features of the flex container, including:

*   Toggling `flex-wrap` between the `wrap` and `wrap-reverse` values.
*   Toggling the `balance` keyword on and off.
*   Changing the `flex-line-count` value.

We've hidden the HTML and JavaScript for brevity.

#### CSS

We apply `display: flex` to the `.box` to turn it into a flex container, then set some `flex-wrap` and `flex-line-count` values to make the flex children wrap evenly over a minimum of three flex lines. You can change the values in the live demo. We also set a [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 value of `1 1 150px` on the flex children so they will have a base width of `150px`, with any remaining space distributed evenly between items on the same flex line.

css

    .box {
      display: flex;
      flex-wrap: wrap balance;
      flex-line-count: 3;
    }
    
    .box > * {
      flex: 1 1 150px;
    }
    

    .box {
      width: 100%;
      border: 2px dotted rgb(96 139 168);
      gap: 10px;
    }
    
    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
    }
    
    * {
      box-sizing: border-box;
    }
    
    body {
      padding: 10px 30px;
    }
    
    @supports not (flex-wrap: balance) {
      body::before {
        content: "Your browser does not support flex-wrap: balance.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

We've hidden the rest of the CSS for brevity.

    const boxElem = document.querySelector(".box");
    const outputElem = document.querySelector("output");
    const pCodeElem = document.querySelector("p code");
    const reverseInput = document.getElementById("reverse");
    const balanceInput = document.getElementById("balance");
    const lineCountInput = document.getElementById("line-count");
    
    let wrapValue = "wrap";
    let lineCountValue = "3";
    
    function updateCurrentlySet() {
      pCodeElem.textContent = `flex-wrap: ${wrapValue}; flex-line-count: ${lineCountValue};`;
    }
    
    function setFlexWrap() {
      wrapValue = "";
      if (reverseInput.checked) {
        wrapValue += "wrap-reverse";
      } else {
        wrapValue += "wrap";
      }
    
      if (balanceInput.checked) {
        wrapValue += " balance";
      }
    
      boxElem.style.flexWrap = wrapValue;
      updateCurrentlySet();
    }
    
    function setFlexLineCount() {
      lineCountValue = lineCountInput.value;
      boxElem.style.flexLineCount = lineCountValue;
      outputElem.textContent = lineCountValue;
      updateCurrentlySet();
    }
    
    reverseInput.addEventListener("change", setFlexWrap);
    balanceInput.addEventListener("change", setFlexWrap);
    lineCountInput.addEventListener("input", setFlexLineCount);
    

#### Results

Change the form control settings to see how they affect the output. Note how:

*   Toggling between `wrap` and `wrap-reverse` changes the direction in which the flex lines are laid out along the cross-axis.
*   Setting `balance` causes the flex items to be evenly distributed across the available flex lines.
*   Changing the `flex-line-count` value changes the minimum number of lines the items will be distributed across. The `flex-line-count` property, and therefore the slider, has no effect unless `balance` is checked.
*   As the flex items are distributed over four flex lines by default, changing the `flex-line-count` to a value of less than `5` has no effect. Values from `5` to `10` add an extra flex line.
*   As there are 10 flex items, `flex-line-count` values of `10` or greater will all have the same effect — one item will be placed on each of 10 flex lines.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-wrap-property](https://drafts.csswg.org/css-flexbox/#flex-wrap-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap#see_also)

-----------------------------------------------------------------------------------------------------

*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    
*   [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
     shorthand
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Mastering wrapping of flex items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Wrapping_items)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-wrap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-wrap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-wrap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-wrap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-wrap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-wrap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
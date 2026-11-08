*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#mdn-search)
    

`rule-inset-junction` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#browser_compatibility)
 carefully before using this in production.

The **`rule-inset-junction`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property can be used to offset the column and row rule segment [junction endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end#understanding_junction_endpoints)
 to the same value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#try_it)

-----------------------------------------------------------------------------------------------------------

    rule-inset-junction: 0;
    

    rule-inset-junction: 10px;
    

    rule-inset-junction: 0.5em -0.5em;
    

    rule-inset-junction: overlap-join;
    

    rule-inset-junction: overlap-join 10px;
    

    <section id="default-example">
      <div id="example-element">
        <i>A</i>
        <i>B</i>
        <i>C</i>
        <i>D</i>
        <i>E</i>
        <i>F</i>
        <i>G</i>
        <i>H</i>
        <i>I</i>
        <i>J</i>
        <i>K</i>
        <i>L</i>
      </div>
    </section>
    

    #example-element {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      rule: solid thick lightpink;
      column-rule-color: magenta;
      rule-break: intersection;
      gap: 1.5em;
      rule-overlap: column-over-row;
      border: 1px solid rebeccapurple;
      margin: auto;
      rule-visibility-items: around;
    }
    #example-element i {
      background-color: #efefef;
      color: #333333;
      padding: 1em;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
    
*   [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    rule-inset-junction: overlap-join;
    
    /* <length-percentage> values */
    rule-inset-junction: 0;
    rule-inset-junction: 1em;
    rule-inset-junction: -5px;
    rule-inset-junction: -25%;
    
    /* Two values */
    rule-inset-junction: 0 1em;
    rule-inset-junction: -5px -25%;
    rule-inset-junction: overlap-join 10px;
    
    /* Global values */
    rule-inset-junction: inherit;
    rule-inset-junction: initial;
    rule-inset-junction: revert;
    rule-inset-junction: revert-layer;
    rule-inset-junction: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#values)

This property is specified as one or two values from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#overlap-join)

Specifies that the junction segment should extend across the row-rule, resolving to half the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 value plus half the used [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the junction endpoint, which is the `row-gap` value for column segments and the `column-gap` value for row segments.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#description)

---------------------------------------------------------------------------------------------------------------------

The `rule-inset-junction` shorthand property can be used to set the [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
 and [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
 properties to the same value in a single declaration, insetting row and column junction segment endpoints by the specified values.

If one value is specified, both properties are set to that value. If two values are specified, `-start` is set to the first value and `-end` is set to the second. Positive values reduce (or inset) the segment size, while negative values and the [`overlap-join` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end#understanding_junction_endpoints)
 increase (or outset) it. The default value is `0`.

To inset both cap and junction segment endpoints, the `rule-inset-junction` shorthand property, along with the [`rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
 shorthand property, can be set using the `rule-inset` shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

rule-inset-junction =   
  [<'column-rule-inset-junction'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
    
  
[<column-rule-inset-junction>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
 =   
  <inset-value> <inset-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#basic_usage)

This example demonstrates setting `rule-inset-junction` to inset the edges of junction segments on flex containers.

#### HTML

The markup includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each containing seven children. The only difference between the two containers is that the second one has an added `column` class.

html

    <h1>Insetting junction column rule endpoints</h1>
    <article>
      <section>
        <h2>flex-direction: row</h2>
        <div class="flexbox">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </section>
      <section>
        <h2>flex-direction: column</h2>
        <div class="flexbox column">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
      </section>
    </article>
    

    <p>
      <label
        >Change the size of the inset.
        <input type="range" min="-40" max="16" value="16" id="inset"
      /></label>
      <output id="o">16px</output>
    </p>
    

#### CSS

We use the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to turn the `.flexbox` elements into flex containers. We balance the items into three flex lines using [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 and [`flex-line-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
. We define a [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 and set the `rule-inset-junction` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid blue;
    
      rule-inset-junction: 16px;
    }
    

We also set the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 on the `.column` container to `column`, changing the main axis of the flex container to run up and down the page and making the items flow in columns rather than rows.

css

    .column {
      flex-direction: column;
    }
    

The rest of the CSS is hidden for brevity.

    h1,
    article {
      font-family: sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 1.25em;
    }
    h2 {
      font-size: 1em;
    }
    article {
      display: flex;
      gap: 5vw;
      rule: 1px solid black;
      width: 100vw;
    }
    section {
      flex-basis: 45vw;
    }
    .flexbox > div {
      border: 1px solid green;
      background-color: lime;
      flex: 1 1 auto;
      height: 30px;
    }
    output {
      display: inline-block;
      width: 2em;
    }
    p {
      margin-top: 2.5em;
    }
    @layer no-support {
      @supports not (rule-inset-junction: 16px) {
        body::before {
          content: "Your browser doesn't support the rule-inset-junction property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const inset = document.getElementById("inset");
    const containers = document.querySelectorAll(".flexbox");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      const val = `${inset.value}px`;
      containers[0].style.ruleInsetJunction = val;
      containers[1].style.ruleInsetJunction = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset. Note that when a rule is a single segment spanning the entire width or height of the container, the segment has two cap endpoints and no junction endpoints, and is therefore not affected by changes to the `rule-inset-junction` value.

### [With grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#with_grid_layout)

This example demonstrates using the `rule-inset-junction` property to inset junction segment endpoints to two different values on a grid container.

#### HTML

We include the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 element as a container with several [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 children which will each be converted into a grid item.

html

    <ul id="ul">
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
      <li>6</li>
      <li>7</li>
      <li>8</li>
      <li>9</li>
      <li>10</li>
      <li>11</li>
      <li>12</li>
      <li>13</li>
      <li>15</li>
      <li>16</li>
      <li>17</li>
      <li>18</li>
      <li>19</li>
    </ul>
    

    <p>
      <label
        >Change the <code>-start</code> value.
        <input type="range" min="-40" max="40" value="16" id="start" data-unit="px"
      /></label>
      <output id="og">16px</output>
    </p>
    <p>
      <label
        >Change the <code>-end</code> value.
        <input type="range" min="-40" max="40" value="0" id="end" data-unit="px"
      /></label>
      <output id="ow">0px</output>
    </p>
    

#### CSS

We turn the `<ul>` into a grid container by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `grid`. The [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property specifies that the grid has five columns. We remove the bullets with the [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property and set the row and column gaps to `20px` with the [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand. We set the color, size, and line style of all the rules using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand, then change just the row rule color with the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
 property.

We break the rules at every intersection using the [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
 property. If the rules didn't break, there would be no junction segments to style!

Finally, we set the start of each column junction to be inset by `16px` and the end to not be inset using the `rule-inset-junction` property.

We also set the 6th grid item to span three columns.

css

    ul {
      display: grid;
      grid-template-columns: repeat(5, auto);
      list-style-type: "";
      gap: 20px;
      rule: 10px solid olive;
      row-rule-color: palegoldenrod;
      rule-break: intersection;
    
      rule-inset-junction: 16px 0;
    }
    
    li:nth-of-type(7) {
      grid-column-end: span 3;
    }
    

The rest of the CSS is hidden for brevity.

    ul {
      border: 1px solid;
      place-items: center;
      width: 95vw;
      padding: 0;
    }
    li {
      text-align: center;
      font-family: sans-serif;
      background-color: #ededed;
      padding: 2em 1em;
      width: 100%;
      box-sizing: border-box;
    }
    li code {
      display: block;
      margin: 0 auto;
      text-align: left;
      width: 30vw;
    }
    output {
      font-family: monospace;
    }
    input {
      accent-color: olive;
    }
    @layer no-support {
      @supports not (rule-inset-junction: 16px) {
        body::before {
          content: "Your browser doesn't support the rule-inset-junction property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const ul = document.querySelector("ul");
    const startSize = document.getElementById("start");
    const og = document.getElementById("og");
    const endSize = document.getElementById("end");
    const ow = document.getElementById("ow");
    const cell = document.querySelector("li:nth-of-type(7)");
    let text = "";
    function update() {
      ul.style.ruleInsetJunction = text = `${startSize.value}px ${endSize.value}px`;
      cell.innerHTML = `<code>rule-inset-cap: ${text};</code>`;
    }
    
    update();
    
    startSize.addEventListener("input", () => {
      og.innerText = `${startSize.value}px`;
      update();
    });
    
    endSize.addEventListener("input", () => {
      ow.innerText = `${endSize.value}px`;
      update();
    });
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-inset-junction](https://drafts.csswg.org/css-gaps-1/#propdef-rule-inset-junction) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
     shorthand
*   `rule-inset` shorthand
*   [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
     shorthand
*   [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-inset-junction/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-inset-junction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-inset-junction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-inset-junction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-inset-junction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-inset-junction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F068c46001316cf268128ab7a26b33fd5705cde1b%0A*+Document+last+modified%3A+2026-11-04T14%3A57%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
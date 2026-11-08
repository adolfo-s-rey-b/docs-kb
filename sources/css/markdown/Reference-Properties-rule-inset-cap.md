*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#mdn-search)
    

`rule-inset-cap` CSS property
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#browser_compatibility)
 carefully before using this in production.

The **`rule-inset-cap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property can be used to offset the column and row rule segment [cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap#understanding_cap_endpoints)
 to the same value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#try_it)

------------------------------------------------------------------------------------------------------

    rule-inset-cap: -20px;
    

    rule-inset-cap: 0;
    

    rule-inset-cap: 1em;
    

    rule-inset-cap: 100%;
    

    rule-inset-cap: overlap-join;
    

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
        <i>M</i>
        <i>N</i>
        <i>O</i>
        <i>P</i>
        <i>Q</i>
    
        <i id="y">Y</i>
        <i id="z">Z</i>
        <i id="bang">!</i>
      </div>
    </section>
    

    #example-element {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      rule: solid thick magenta;
      column-rule-color: rebeccapurple;
      gap: 1em;
      rule-overlap: column-over-row;
      rule-visibility-items: between;
      border: 1px solid rebeccapurple;
      overflow: visible;
      margin: 1em;
    }
    #example-element i {
      padding: 8px;
      border: 1px dashed;
    }
    #y {
      grid-column: 4 / 5;
      grid-row: 4 / 5;
    }
    #z {
      grid-column: 5 / 6;
      grid-row: 4 / 5;
    }
    #bang {
      grid-column: 6 / 7;
      grid-row: 4 / 5;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
    
*   [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    rule-inset-cap: overlap-join;
    
    /* A <length-percentage> value */
    rule-inset-cap: 0;
    rule-inset-cap: 1em;
    rule-inset-cap: -5px;
    rule-inset-cap: -25%;
    
    /* Two values */
    rule-inset-cap: 0 20px;
    rule-inset-cap: 1em -5px;
    rule-inset-cap: overlap-join -25%;
    
    /* Global values */
    rule-inset-cap: inherit;
    rule-inset-cap: initial;
    rule-inset-cap: revert;
    rule-inset-cap: revert-layer;
    rule-inset-cap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#values)

This property is specified as one or two values from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#overlap-join)

Resolves to `0`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values resolve to `0` for caps at the container's edge. For interior gaps, percentages are relative to the height of the adjacent `row-gap` for column segment caps, or the width of the adjacent `column-gap` for row segment caps.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#description)

----------------------------------------------------------------------------------------------------------------

The `rule-inset-cap` shorthand property can be used to set the [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
 and [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
 properties to the same value in a single declaration, insetting row and column cap segment endpoints by the specified values.

If you specify one value, both the start and end cap segment endpoints are set to that value. If you specify two values, the row and column cap start segment endpoints are set to the first value, and the row and column cap end segment endpoints are set to the second value.

The default value is `0`, which, in the case of cap endpoints, is the same as `overlap-join`. Positive values reduce the segment size, while negative values increase it.

The `rule-inset-cap` property, along with the [`rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction)
 property, can be set using the `rule-inset` shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

rule-inset-cap =   
  [<'column-rule-inset-cap'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
    
  
[<column-rule-inset-cap>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#examples)

----------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#basic_usage)

This example shows how to set `rule-inset-cap` to inset the endpoints of cap segments on flex containers.

#### HTML

The markup includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each containing seven children. The only difference between the two containers is that the second one has an added `column` class.

html

    <h1>Insetting cap endpoints</h1>
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
. We define a light blue [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 to paint in both row and column gaps, then override the [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
, setting darker `blue` vertical gap decorations. Finally, we set the `rule-inset-cap` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      column-rule-color: blue;
    
      rule-inset-cap: 16px;
    }
    

We also set the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 on the `.column` container to make its items flow in columns rather than rows. We've hidden the other CSS styles, and the code that make the form interactive, for brevity.

css

    .column {
      flex-direction: column;
    }
    

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
      width: 90vw;
      margin: auto;
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
      @supports not (rule-inset-cap: 16px) {
        body::before {
          content: "Your browser doesn't support the rule-inset-cap property";
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
      containers[0].style.ruleInsetCap = val;
      containers[1].style.ruleInsetCap = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset.

### [Setting two values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#setting_two_values)

#### HTML

    <p>
      <label
        >Change the <code>row-rule-inset-cap</code> value.
        <input type="range" min="-40" max="40" value="40" id="row" data-unit="px"
      /></label>
      <output id="og">40px</output>
    </p>
    <p>
      <label
        >Change the <code>column-rule-inset-cap</code> value.
        <input type="range" min="-40" max="40" value="-40" id="col" data-unit="px"
      /></label>
      <output id="ow">-40px</output>
    </p>
    

Our HTML includes an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) with nine list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
):

html

    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
      <li>6</li>
      <li>7</li>
      <li>8</li>
      <li>9</li>
    </ul>
    

The user interface for selecting different values and the JavaScript that enables the interactivity have been hidden for brevity.

#### CSS

We create a grid container by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to grid, creating 4 columns with [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
, and adding a `30px` [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
. We use the [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
 and [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 properties to define our rules. We then use the `rule-inset-cap` property to inset the start cap segment endpoints by `40px` and outset the end cap segment endpoints by `-40px`.

We also set the 6th grid item to span two columns.

css

    ul {
      display: grid;
      grid-template-columns: repeat(4, auto);
      gap: 30px;
      row-rule: 16px solid olive;
      column-rule: 10px solid palegoldenrod;
    
      rule-inset-cap: 40px -40px;
    }
    li:nth-of-type(6) {
      grid-column-end: span 2;
    }
    

    ul {
      width: calc(95vw - 80px);
      border: 1px solid;
      list-style-type: none;
      margin: auto;
      padding: 0;
      place-items: center;
    }
    li {
      place-content: center;
      text-align: center;
      font-family: sans-serif;
      background-color: #ededed;
      padding: 5vw;
      width: 100%;
      box-sizing: border-box;
    }
    li:nth-of-type(6) {
      padding: 2em 0;
    }
    li code {
      display: block;
      margin: 0 auto;
      text-align: left;
      background-color: #fcfcfc;
      width: calc(47.5vw - 40px);
    }
    output {
      font-family: monospace;
    }
    input {
      accent-color: olive;
    }
    @layer no-support {
      @supports not (rule-inset-cap: 16px) {
        body::before {
          content: "Your browser doesn't support the rule-inset-cap property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const ul = document.querySelector("ul");
    const rowSize = document.getElementById("row");
    const og = document.getElementById("og");
    const colSize = document.getElementById("col");
    const ow = document.getElementById("ow");
    const cell = document.querySelector("li:nth-of-type(6)");
    let text = "";
    function update() {
      ul.style.ruleInsetCap = text = `${rowSize.value}px ${colSize.value}px`;
      cell.innerHTML = `<code>rule-inset-cap: ${text};</code>`;
    }
    
    update();
    
    rowSize.addEventListener("input", () => {
      og.innerText = `${rowSize.value}px`;
      update();
    });
    
    colSize.addEventListener("input", () => {
      ow.innerText = `${colSize.value}px`;
      update();
    });
    

#### Result

Change the inset values for the starts and ends of the cap segment endpoints.

### [Inner cap segments](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#inner_cap_segments)

This example shows how to set `rule-inset-cap` to inset the endpoints of cap segments on a grid container, and how the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 property can turn inner endpoints into cap segment endpoints.

#### HTML

We include an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) as our container for several list items ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
).

We also include a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element with an [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 for each `rule-visibility-items` keyword, and an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of type [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
.

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
      <li>14</li>
      <li>15</li>
      <li>16</li>
      <li>17</li>
    </ul>
    
    <p>
      <label>
        <code>rule-visibility-items</code> value
        <select id="visibility">
          <option>all</option>
          <option>between</option>
          <option>around</option>
          <option selected>normal</option>
        </select>
      </label>
    </p>
    
    <p>
      <label
        >Change the inset size.
        <input type="range" min="-40" max="16" value="0" id="inset" data-unit="px"
      /></label>
      <output id="o"></output>
    </p>
    

#### CSS

We create a grid container by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to grid, creating 6 columns with [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
, and adding a `20px` [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
. We use the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 property to define our rules, overriding the row rule color with the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
 property. We set the [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
 property to break the rules at each intersection, making each rule segment distinct. We explicitly set [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 to the default value of `normal`. We then use the `rule-inset-cap` property to inset all the cap segment endpoints by `16px`.

We also set the seventh list item to span two columns using the [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
 property.

css

    ul {
      display: grid;
      grid-template-columns: repeat(6, auto);
      gap: 20px;
      rule: 10px solid olive;
      row-rule-color: palegoldenrod;
      rule-break: intersection;
      rule-visibility-items: normal;
    
      rule-inset-cap: 16px;
    }
    
    li:nth-of-type(7) {
      grid-column-end: span 2;
    }
    

We've hidden the other CSS styles, and the code that make the form interactive, for brevity.

    ul {
      place-items: center;
      padding: 0;
      list-style-type: none;
      border: 1px solid;
      margin: 40px;
    }
    li {
      text-align: center;
      font-family: sans-serif;
      background-color: #ededed;
      padding: 1em;
      width: 100%;
      box-sizing: border-box;
    }
    li:nth-of-type(n + 9) {
      grid-row: 3 / 4;
    }
    li:nth-of-type(n + 12) {
      grid-row: 4 / 5;
    }
    li:nth-of-type(10) {
      grid-column: 5/6;
    }
    li:nth-of-type(11) {
      grid-column: 6/7;
    }
    
    li:nth-of-type(15) {
      grid-area: 4 / 5 / 5 / 6;
    }
    li:nth-of-type(16) {
      grid-area: 4 / 6 / 5 / 7;
    }
    li:nth-of-type(17) {
      display: none;
      grid-area: 5 / 6 / 6 / 7;
    }
    @layer no-support {
      @supports not (rule-inset-cap: 16px) {
        body::before {
          content: "Your browser doesn't support the rule-inset-cap property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      output.innerText =
        ul.style.ruleInsetCap = `${inset.value}${inset.dataset["unit"]}`;
    });
    
    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
    });
    

#### Result

Select `between` from the dropdown to paint only rule segments when both adjacent grid areas contain a grid item, thereby creating interior cap segments. Now change the inset value to visualize which segment endpoints are cap segment endpoints.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-inset-cap](https://drafts.csswg.org/css-gaps-1/#propdef-rule-inset-cap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap#see_also)

----------------------------------------------------------------------------------------------------------

*   [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
     shorthand
*   [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
     shorthand
*   `column-rule-inset` shorthand
*   `row-rule-inset` shorthand
*   `rule-inset-start` shorthand
*   `rule-inset` shorthand
*   [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
     shorthand\\
*   [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-inset-cap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-inset-cap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-inset-cap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-inset-cap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-inset-cap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-inset-cap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
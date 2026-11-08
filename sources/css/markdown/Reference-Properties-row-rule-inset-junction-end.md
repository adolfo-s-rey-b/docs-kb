*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#mdn-search)
    

`row-rule-inset-junction-end` CSS property
==========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#browser_compatibility)
 carefully before using this in production.

The **`row-rule-inset-junction-end`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the end edge of row rule segments that are [junction endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#understanding_junction_end)
, that is, endpoints at gap junctions where rule segments intersect.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#try_it)

-------------------------------------------------------------------------------------------------------------------

    row-rule-inset-junction-end: 0;
    

    row-rule-inset-junction-end: 0.5em;
    

    row-rule-inset-junction-end: 5px;
    

    row-rule-inset-junction-end: -50%;
    

    row-rule-inset-junction-end: overlap-join;
    

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
        <i>R</i>
    
        <i id="u">U</i>
        <i id="x">X</i>
        <i id="y">Y</i>
        <i id="bang">!</i>
      </div>
    </section>
    

    #example-element {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      rule: solid thick lightpink;
      row-rule-color: magenta;
      row-rule-break: intersection;
      gap: 1.5em;
      rule-overlap: row-over-column;
      border: 1px solid rebeccapurple;
      margin: auto;
      rule-visibility-items: around;
    }
    #example-element i {
      padding: 8px;
      border: 1px dashed;
    }
    #u {
      grid-row: 3 / 4;
      grid-column: 7 / 8;
    }
    #y {
      grid-row: 4 / 5;
      grid-column: 4 / 5;
    }
    #x {
      grid-column: 3 / 4;
      grid-row: 4 / 5;
    }
    #bang {
      grid-column: 6 / 7;
      grid-row: 4 / 5;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#syntax)

-------------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    row-rule-inset-junction-end: overlap-join;
    
    /* <length-percentage> values */
    row-rule-inset-junction-end: 0;
    row-rule-inset-junction-end: 1em;
    row-rule-inset-junction-end: -5px;
    row-rule-inset-junction-end: -25%;
    
    /* Global values */
    row-rule-inset-junction-end: inherit;
    row-rule-inset-junction-end: initial;
    row-rule-inset-junction-end: revert;
    row-rule-inset-junction-end: revert-layer;
    row-rule-inset-junction-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#values)

This property is specified as a single value from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#overlap-join)

Specifies that the junction segment should extend across the column-rule, resolving to half the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 value plus half the used [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the junction endpoint, which is the `column-gap` value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#description)

-----------------------------------------------------------------------------------------------------------------------------

The `row-rule-inset-junction-end` property can be used to inset or outset [junction segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#understanding_junction_end)
 occurring at the end of row rule segments. The default value is `0`. Positive values reduce the segment size, while negative values and the [`overlap-join` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#the_overlap-join_value)
 increase it.

Row rules are painted within a row gap as one or more segments, with segments occurring between:

*   Adjacent rows in CSS grid layouts.
*   Adjacent flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Adjacent rows in multi-col layouts, which may exist when [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
     is set to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    .

Whether a row rule spans multiple columns or is broken into multiple segments is defined by the [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
 property. Interior breaks between row rule segments are the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
. A junction end occurs at the end of every row segment where the segment ends at a gap junction with other row or rule segments present.

The `row-rule-inset-junction-end` property is a constituent property of several [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset both the left and right row segment junction endpoints, the `row-rule-inset-junction-end` property, along with the [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
     property, can be set using the [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
     shorthand.
    
*   To inset all end row segment endpoints, the `row-rule-inset-junction-end` property, along with the [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
     property, can be set using the `row-rule-inset-end` shorthand.
    
*   To inset the top, bottom, left, and right segment junction endpoints the `row-rule-inset-junction` shorthand property, along with the [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
     shorthand property, can be set using the [`rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction)
     shorthand.
    

All segment endpoints, including this property's `-start`, `-cap`, and `column-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding junction endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#understanding_junction_endpoints)

A _junction segment endpoint_ is any segment endpoint at an interior gap that ends at a gap intersection where other column rule or row rule segments are present. The `row-rule-inset-junction-end` property controls the inset of the end edge of row junction segments, allowing the segments to be shrunk or extended.

Length `row-rule-inset-junction-end` values inset junction segments by the specified value. Percentage values are relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
. Negative values create an outset, extending the end of the junction segment. Setting `-50%` outsets the end of the junction segment half way through the adjacent column gap, no matter how wide the column gap is.

In the following demonstration, the row rule segments in all but the last column end in junction endpoints. With `row-rule-inset-junction-end: 16px` set, the right, or end, of these segments is inset by `16px`. Change the inset `<length>` value to better visualize which row segments end in junction segment endpoints.

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
      <li class="b">21</li>
      <li class="c">23</li>
    </ul>
    
    <p>
      <label
        ><code>rule-visibility-items</code> value <code>
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
        >Change the size of the inset.
        <input type="range" min="-20" max="16" value="16" id="inset" data-unit="px"
      /></label>
      <output id="o">16px</output>
    </p>
    

    <p>
      <label
        >Change the size of the inset.
        <input
          type="range"
          min="-200"
          max="100"
          value="50"
          id="inset"
          data-unit="%"
      /></label>
      <output id="o">50%</output>
    </p>
    

    ul {
      display: grid;
      grid-template-columns: repeat(6, auto);
      list-style-type: none;
      gap: 20px;
      row-rule: 10px solid olive;
      column-rule: 10px solid palegoldenrod;
      rule-overlap: row-over-column;
      rule-visibility-items: normal;
      rule-break: intersection;
      row-rule-inset-junction-end: 16px;
    
      border: 1px solid;
    }
    ul {
      place-items: center;
      width: 95vw;
      padding: 0;
    }
    li {
      text-align: center;
      font-family: sans-serif;
      background-color: #ededed;
      padding: 1em;
      width: 100%;
      box-sizing: border-box;
    }
    .b {
      grid-column: 3 / 4;
      grid-row: 4 / 5;
    }
    .c {
      grid-column: 5 / 6;
      grid-row: 4 / 5;
    }
    @layer no-support {
      @supports not (row-rule-inset-junction-end: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-junction-end property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      row-rule-inset-junction-end: 100%;
      row-rule-style: inset;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      o.innerText =
        ul.style.rowRuleInsetJunctionEnd = `${inset.value}${inset.dataset["unit"]}`;
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.rowRuleStyle = "repeat(3, solid), repeat(2, double)";
      } else if (visibility.value === "around") {
        ul.style.rowRuleStyle = "repeat(3, solid), repeat(2, double)";
      } else {
        ul.style.rowRuleStyle = "solid";
      }
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.rowRuleStyle = "repeat(2, inset), double, repeat(2, solid)";
      } else if (visibility.value === "around") {
        ul.style.rowRuleStyle = "repeat(3, inset), repeat(2, double)";
      } else {
        ul.style.rowRuleStyle = "solid";
      }
    });
    

The [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
 property is set to `intersection`, breaking all the row and column segments at every gap junction, with the end of each interior row segment abutting a column gap by default. The default value of the `row-rule-inset-junction-end` property is `0`.

Change the inset value. Note how only the right ends of the row segments in the middle of the grid change when the property value changes. The segment endpoints at the containers do not change: these are _cap endpoints_, and are not affected by the `row-rule-inset-junction-end` property.

Select `between` as the `rule-visibility-items` value. This value causes rules in gap segments to be painted only if items occupy both adjacent areas. The row rule segment between `17` and `23` now ends at an interior junction where no other rule segments are present: the end of this row segment is a _cap segment endpoint_ and isn't affected by the `row-rule-inset-junction-end` property. The `row-rule-inset-cap-end` property can be used to inset this segment endpoint.

The `around` value paints rules in gap segments if an item occupies at least one of the two adjacent areas. In this example, no junction segment endpoints became cap segment endpoints, but some cap segments were not drawn.

### [The `overlap-join` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#the_overlap-join_value)

The `overlap-join` value outsets the end of interior segments so they align with the far edge of the intersected column-rule. The value resolves to half the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 size (extending it to the middle of the gap) plus half the column rule width. When `row-rule-inset-junction-end` is set to the `overlap-join` keyword value, the junction end segments extend into the column gap to meet, or "join", the opposite edge of the column rule painted in that gap.

In the following live example, `row-rule-inset-junction-end` is set to `overlap-join`:

    <p>
      <label
        >Change the <code>column-gap</code>.
        <input type="range" min="10" max="40" value="40" id="gap" data-unit="px"
      /></label>
      <output id="og">40px</output>
    </p>
    <p>
      <label
        >Change the <code>column-rule-width</code>.
        <input type="range" min="0" max="40" value="16" id="rrw" data-unit="px"
      /></label>
      <output id="ow">16px</output>
    </p>
    
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
      <li>10</li>
    </ul>
    

    ul {
      display: grid;
      grid-template-columns: repeat(4, auto);
      list-style-type: none;
      gap: 30px;
      row-rule: 16px solid olive;
      column-rule: 10px solid palegoldenrod;
      rule-overlap: row-over-column;
      rule-visibility-items: around;
      row-rule-break: intersection;
      row-rule-inset-junction-end: overlap-join;
      border: 1px solid;
    }
    ul {
      place-items: center;
      margin: auto;
      padding: 0;
    }
    li {
      text-align: center;
      font-family: sans-serif;
      background-color: #ededed;
      padding: 2em;
      width: 100%;
      box-sizing: border-box;
    }
    @layer no-support {
      @supports not (row-rule-inset-junction-end: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-junction-end property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const ul = document.querySelector("ul");
    const gapSize = document.getElementById("gap");
    const og = document.getElementById("og");
    const ruleWidth = document.getElementById("rrw");
    const ow = document.getElementById("ow");
    
    gapSize.addEventListener("input", () => {
      og.innerText = ul.style.columnGap = `${gapSize.value}px`;
    });
    
    ruleWidth.addEventListener("input", () => {
      ow.innerText = ul.style.columnRuleWidth = `${ruleWidth.value}px`;
    });
    

Change the size of the [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
 and the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
. Notice how, no matter the size of the gap or column rule, the end of the row segment is always stretched across the column rule, with the endpoint aligned with the opposite edge of the column rule painted in the gap.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------------

row-rule-inset-junction-end =   
  <inset-value>    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#basic_usage)

This example demonstrates setting `row-rule-inset-junction-end` to inset the end edge of row junction segments on flex containers.

#### HTML

The markup includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each containing seven children. The only difference between the two containers is that the second one has an added `column` class.

html

    <h1>Insetting junction row rule endpoints</h1>
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
 to paint both column and row gaps, then overwrite the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
, setting darker `blue` row gap decorations. Finally, we set the `row-rule-inset-junction-end` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      row-rule-color: blue;
    
      row-rule-inset-junction-end: 16px;
    }
    

We also set the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 on the `.column` container to `column`, changing the main axis of the flex container, making the items flow in columns rather than rows.

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
      @supports not (row-rule-inset-junction-end: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-junction-end property";
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
      containers[0].style.rowRuleInsetJunctionEnd = val;
      containers[1].style.rowRuleInsetJunctionEnd = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset. Note that this property affects only row rules split into multiple segments. When a row rule is a single segment that spans the width of the container, the segment has two cap endpoints and no junction endpoints, and remains unaffected by changes to the `row-rule-inset-junction-end` value.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-row-rule-inset-junction-end](https://drafts.csswg.org/css-gaps-1/#propdef-row-rule-inset-junction-end) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
    
*   [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
     shorthand
*   `row-rule-inset` shorthand
*   `rule-inset` shorthand
*   [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
    
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

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule-inset-junction-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule-inset-junction-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-junction-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-junction-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-junction-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-junction-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2a563c927890794b513523649ccfbbe48d336465%0A*+Document+last+modified%3A+2026-11-05T23%3A07%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
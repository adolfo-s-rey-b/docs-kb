*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#mdn-search)
    

`column-rule-inset-junction-start` CSS property
===============================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#browser_compatibility)
 carefully before using this in production.

The **`column-rule-inset-junction-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the top endpoints of column rule segments that are [junction endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#understanding_junction_endpoints)
; that is, endpoints at gap junctions where rule segments intersect.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#try_it)

------------------------------------------------------------------------------------------------------------------------

    column-rule-inset-junction-start: 0;
    

    column-rule-inset-junction-start: 0.5em;
    

    column-rule-inset-junction-start: 10px;
    

    column-rule-inset-junction-start: -100%;
    

    column-rule-inset-junction-start: overlap-join;
    

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
      column-rule-break: intersection;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#syntax)

------------------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    column-rule-inset-junction-start: overlap-join;
    
    /* <length-percentage> values */
    column-rule-inset-junction-start: 0;
    column-rule-inset-junction-start: 1em;
    column-rule-inset-junction-start: -5px;
    column-rule-inset-junction-start: -25%;
    
    /* Global values */
    column-rule-inset-junction-start: inherit;
    column-rule-inset-junction-start: initial;
    column-rule-inset-junction-start: revert;
    column-rule-inset-junction-start: revert-layer;
    column-rule-inset-junction-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#values)

This property is specified as a single value from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#overlap-join)

Specifies that the junction segment should extend across the row-rule, resolving to half the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 value plus half the used [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the junction endpoint, which is the `row-gap` value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#description)

----------------------------------------------------------------------------------------------------------------------------------

The `column-rule-inset-junction-start` property can be used to inset or outset [junction segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#understanding_junction_endpoints)
 occurring at the top of column rule segments. The default value is `0`. Positive values reduce the segment size, while negative values and [the `overlap-join` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#the_overlap-join_value)
 increase it.

Column rules are painted within a column gap as one or more segments, with segments occurring between:

*   Adjacent columns in CSS grid layouts.
*   Adjacent flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Adjacent columns in multi-col layouts.

Whether a column rule spans multiple rows or is broken into multiple segments is defined by the [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
 property; interior breaks between column rule segments are the size of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
. A junction end occurs at the top of every column segment where the segment's top ends at a gap junction with other column or rule segments present.

The `column-rule-inset-junction-start` property is a constituent property of several [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset the top and bottom column segment junction endpoints, the `column-rule-inset-junction-start` property, along with the [`column-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end)
     property, can be set using the [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
     shorthand.
    
*   To inset all top column segment endpoints, the `column-rule-inset-junction-start` property, along with the [`column-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-start)
     property, can be set using the `column-rule-inset-start` shorthand.
    
*   To inset the top, bottom, left, and right segment junction endpoints the `column-rule-inset-junction` shorthand property, along with the [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
     shorthand property, can be set using the [`rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction)
     shorthand.
    

All segment endpoints, including this property's `-start`, `-cap`, and `row-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding junction endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#understanding_junction_endpoints)

A _junction segment endpoint_ is any segment endpoint at an interior gap that ends at a gap intersection where other rule or column segments are present. The `column-rule-inset-junction-start` property controls the inset of the top edge of column junction segments, allowing the segments to be shrunk or extended.

Length `column-rule-inset-junction-start` values inset segments by the specified value. Negative length values create an outset, extending the top end of the junction segment. Percentage values are relative to the size of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
. Setting `-50%` outsets the top of the junction segment half way through the row gap above the segment, no matter how wide the row gap is.

In the following demonstration, the column rule segments in the last two rows start in junction endpoints. With `column-rule-inset-junction-start: 16px` set, the top, or start, of these segments are inset by `16px`. Change the inset `<length>` value to better visualize which column segments start in junction segment endpoints.

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
        <input type="range" min="-40" max="16" value="16" id="inset" data-unit="px"
      /></label>
      <output id="o">16px</output>
    </p>
    

    <p>
      <label
        >Change the size of the inset.
        <input
          type="range"
          min="-450"
          max="100"
          value="100"
          id="inset"
          data-unit="%"
      /></label>
      <output id="o">100%</output>
    </p>
    

    ul {
      display: grid;
      grid-template-columns: repeat(6, auto);
      list-style-type: none;
      gap: 20px;
      column-rule: 10px solid olive;
      row-rule: 10px solid palegoldenrod;
      rule-overlap: column-over-row;
      rule-visibility-items: normal;
      rule-break: intersection;
      column-rule-inset-junction-start: 16px;
    
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
    @layer no-support {
      @supports not (column-rule-inset-junction-start: 16px) {
        body::before {
          content: "Your browser doesn't support the column-rule-inset-junction-start property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      column-rule-inset-junction-start: 100%;
      column-rule-style: inset;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      o.innerText =
        ul.style.columnRuleInsetJunctionStart = `${inset.value}${inset.dataset["unit"]}`;
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.columnRuleStyle = "repeat(3, solid), repeat(2, double)";
      } else if (visibility.value === "around") {
        ul.style.columnRuleStyle = "repeat(3, solid), repeat(2, double)";
      } else {
        ul.style.columnRuleStyle = "solid";
      }
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.columnRuleStyle = "repeat(2, inset), double, repeat(2, solid)";
      } else if (visibility.value === "around") {
        ul.style.columnRuleStyle = "repeat(3, inset), repeat(2, double)";
      } else {
        ul.style.columnRuleStyle = "solid";
      }
    });
    

If you set `0px` as the value, the start of the column rules will align with the start, or top, of the row, abutting the row gap. This is the default. Note how only the start ends of the segments in the middle of the grid change when the property value changes. The segments in the first row do not change: these are _cap endpoints_, and are not affected by the `column-rule-inset-junction-start` property.

Select `around` and `between` as the `rule-visibility-items` value. This `around` value paints rules in a gap segment if an item occupies at least one of the two adjacent areas. The `between` value paints rules in gap segments only if items occupy both adjacent areas. When a rule segment ends at an interior intersection where no other rule segments are present, the segment is a _cap segment endpoint_, and isn't affected by the `column-rule-inset-junction-start` property.

### [The `overlap-join` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#the_overlap-join_value)

The `overlap-join` value outsets the top end of interior segments so they align with the top of the intersected row-rule. The value resolves to half the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 size (extending it to the middle of the gap) plus half the row rule width.

When `column-rule-inset-junction-start` is set to the `overlap-join` keyword value, the junction end segments extend up into the row gap to meet, or "join", the top edge of the row rule painted in that gap.

In the following live example, `column-rule-inset-junction-start` is set to `overlap-join`:

    <p>
      <label
        >Change the <code>row-gap</code>.
        <input type="range" min="10" max="40" value="30" id="gap" data-unit="px"
      /></label>
      <output id="og">30px</output>
    </p>
    <p>
      <label
        >Change the <code>row-rule-width</code>.
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
      column-rule: 16px solid olive;
      row-rule: 10px solid palegoldenrod;
      rule-overlap: column-over-row;
      rule-visibility-items: around;
      column-rule-break: intersection;
      column-rule-inset-junction-start: overlap-join;
      border: 1px solid;
    }
    ul {
      place-items: center;
      width: 70vw;
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
      @supports not (column-rule-inset-junction-start: 16px) {
        body::before {
          content: "Your browser doesn't support the column-rule-inset-junction-start property";
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
      og.innerText = ul.style.rowGap = `${gapSize.value}px`;
    });
    
    ruleWidth.addEventListener("input", () => {
      ow.innerText = ul.style.rowRuleWidth = `${ruleWidth.value}px`;
    });
    

Change the size of the [`row-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
 and the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
. Notice how, no matter the size of the gap or row rule, the top end of the column segment is always stretched to align with the top of the row rule painted in the gap.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------------------

column-rule-inset-junction-start =   
  <inset-value>    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#basic_usage)

This example demonstrates setting `column-rule-inset-junction-start` to inset the start edge of column junction segments on flex containers.

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
. We define a light blue [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 to paint both row and column gaps, then overwrite the [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
, setting darker `blue` column gap decorations. We also set the [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
 property to `row-over-column` so the column segments are drawn under the row segments when the segments overlap. Finally, we set the `column-rule-inset-junction-start` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      column-rule-color: blue;
      rule-overlap: row-over-column;
    
      column-rule-inset-junction-start: 16px;
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
      @supports not (column-rule-inset-junction-start: 16px) {
        body::before {
          content: "Your browser doesn't support the column-rule-inset-junction-start property";
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
      containers[0].style.columnRuleInsetJunctionStart = val;
      containers[1].style.columnRuleInsetJunctionStart = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset. Note that in example, where the column rule is a single segment that goes from bottom to bottom, the segment has two cap endpoints and no junction endpoints. Therefore, changing the `column-rule-inset-junction-start` value does not affect this example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-column-rule-inset-junction-start](https://drafts.csswg.org/css-gaps-1/#propdef-column-rule-inset-junction-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [`column-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end)
    
*   [`column-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
     shorthand
*   `column-rule-inset` shorthand
*   `rule-inset` shorthand
*   [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
    
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

This page was last modified on Nov 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule-inset-junction-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule-inset-junction-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-inset-junction-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-inset-junction-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-inset-junction-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-inset-junction-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F068c46001316cf268128ab7a26b33fd5705cde1b%0A*+Document+last+modified%3A+2026-11-04T14%3A57%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
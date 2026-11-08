*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#mdn-search)
    

`row-rule-inset-cap-start` CSS property
=======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#browser_compatibility)
 carefully before using this in production.

The **`row-rule-inset-cap-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the start of row rule segment [cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap#understanding_cap_endpoints)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#try_it)

----------------------------------------------------------------------------------------------------------------

    row-rule-inset-cap-start: -20px;
    

    row-rule-inset-cap-start: 0;
    

    row-rule-inset-cap-start: 1em;
    

    row-rule-inset-cap-start: 100%;
    

    row-rule-inset-cap-start: overlap-join;
    

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
    
        <i id="r">R</i>
        <i id="z">Z</i>
        <i id="bang">!</i>
      </div>
    </section>
    

    #example-element {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      rule: solid thick magenta;
      row-rule-color: rebeccapurple;
      gap: 1em;
      rule-overlap: row-over-column;
      rule-visibility-items: between;
      border: 1px solid rebeccapurple;
      overflow: visible;
      margin: 1em;
    }
    #example-element i {
      padding: 8px;
      border: 1px dashed;
    }
    #r {
      grid-column: 5 / 6;
      grid-row: 3 / 4;
    }
    #z {
      grid-column: 5 / 6;
      grid-row: 4 / 5;
    }
    #bang {
      grid-column: 5 / 6;
      grid-row: 5 / 6;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#syntax)

----------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    row-rule-inset-cap-start: overlap-join;
    
    /* <length-percentage> values */
    row-rule-inset-cap-start: 0;
    row-rule-inset-cap-start: 1em;
    row-rule-inset-cap-start: -5px;
    row-rule-inset-cap-start: -25%;
    
    /* Global values */
    row-rule-inset-cap-start: inherit;
    row-rule-inset-cap-start: initial;
    row-rule-inset-cap-start: revert;
    row-rule-inset-cap-start: revert-layer;
    row-rule-inset-cap-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#values)

This property is specified as a single value from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#overlap-join)

Resolves to `0`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the cap endpoint, which is either the `column-gap` or `0`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#description)

--------------------------------------------------------------------------------------------------------------------------

The `row-rule-inset-cap-start` property insets the start of [cap segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap#understanding_cap_endpoints)
 at the container's start edge and at cap endpoints where no rule segments intersect. The default value is `0`, which is the same as `overlap-join`. Positive values reduce the segment size, while negative values increase it.

Row rules are painted within a row gap as one or more segments, with segments occurring between:

*   Adjacent rows in CSS grid layouts.
*   Adjacent flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Adjacent rows in multi-col layouts, which may exist when [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
     is set to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    .

Length `row-rule-inset-cap-start` values inset the start of both interior and start-edge cap segment endpoints by the specified value. Negative length values create an outset, with container-edge cap segments extending beyond the container's start edge.

[Percentage value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#understanding_percentage_values)
 insets for interior cap segments are relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
. For cap segments at the container start edge, percentage values are relative to `0`, so they are always `0px`.

The `row-rule-inset-cap-start` property is a constituent property of several [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset both the left and right ends of row cap segments, the `row-rule-inset-cap-start` property, along with the [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
     property, can be set using the [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
     shorthand.
    
*   To inset the start edge of all row segments, the `row-rule-inset-cap-start` property, along with the [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
     property, can be set using the `row-rule-inset-start` shorthand.
    

All segment endpoints, including this property's `-end`, `-junction`, and `column-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding cap start](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#understanding_cap_start)

A _cap segment endpoint_ is any segment endpoint that is not a junction segment endpoint. This includes endpoints at the container's content edges, as well as endpoints at a gap junction where no other rule segments are present.

The `row-rule-inset-cap-start` controls the start inset of row rules with cap endpoints. The property can shrink or extend the start of:

*   Row rule segments abutting the container start edge.
*   Row rule segments whose left side abuts an interior gap where no other row or column rule segments are present.

Row cap segments are impacted by the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 properties, which define whether row- and column-rule segments are painted in gaps adjacent to empty areas. Changing the value from `auto` to `between` or `around` can create additional interior cap segments.

In the following demonstration, the leftmost segments of the row rules abutting the container edge start in a cap endpoint. With `row-rule-inset-cap-start: -32px` set, these endpoints are all outset by `32px`. As row rules don't impact the box model, these protruding lines don't affect the content's layout. Change the inset `<length>` value to better visualize which segments start with cap segment endpoints.

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
        >Change the size of the inset.
        <input
          type="range"
          min="-40"
          max="16"
          value="-32"
          id="inset"
          data-unit="px"
      /></label>
      <output id="o">-32px</output>
    </p>
    

    <p>
      <label
        >Change the size of the inset.
        <input
          type="range"
          min="-200"
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
      row-rule: 10px solid olive;
      column-rule: 10px solid palegoldenrod;
      rule-overlap: column-over-row;
      rule-visibility-items: normal;
      rule-break: intersection;
      row-rule-inset-cap-start: -32px;
    
      border: 1px solid;
      margin: auto 40px;
    }
    ul {
      place-items: center;
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
    li:nth-of-type(n + 9) {
      grid-row: 3 / 4;
    }
    li:nth-of-type(n + 13) {
      grid-row: 4 / 5;
    }
    li:nth-of-type(12),
    li:nth-of-type(16) {
      grid-column: 5/6;
    }
    li:nth-of-type(17) {
      grid-column: 6/7;
    }
    
    @layer no-support {
      @supports not (row-rule-inset-cap-start: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap-start property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      row-rule-inset-cap-start: 100%;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      output.innerText =
        ul.style.rowRuleInsetCapStart = `${inset.value}${inset.dataset["unit"]}`;
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.rowRuleStyle = "repeat(2, solid), double";
      } else {
        ul.style.rowRuleStyle = "solid";
      }
    });
    

Change the inset. Setting `0px` aligns the start of the row rules with the start of the container. This is the default.

Select `between` as the `rule-visibility-items` value. This value paints rules in a gap segment only if the two adjacent areas are occupied by items. Again, we have row rule cap endpoints at the start edge of the container. The third row rule, denoted with a double line style, has an additional cap endpoint segment: the left side of the segment between items `12` and `16`. This does not meet any other rule segments and is therefore affected by the `row-rule-inset-cap-start` property.

In this case, the `around` value of the `rule-visibility-items` property, which paints rules in a gap segment as long as one adjacent area is occupied by an item, did not create additional cap segment endpoints. The rule start of the segment between `12` and `16` intersects with the column rule segments in the column-gap to the left of those items, creating junction, not cap, segment endpoints. Junction endpoints are inset using the [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
 property instead.

### [Understanding percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#understanding_percentage_values)

The length a percentage value is relative to depends on the endpoint location. Interior endpoint percentage values are relative to the width of the gap at the cap endpoint, so relative to the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 if abutting a rule gap, and `0` at the edge of the container.

This example isn't broken; all the cap segments start at the container's edge, so all the insets are `0` by default.

The slider only has an effect when the `rule-visibility-items` value is set to `between`, and then only on the single inner cap endpoint segment that this value creates — the segment between `12` and `16`. For this segment only, the percentage offset is relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 width, which in this case is `20px`. Setting `100%` insets the start of the cap segment by `20px`. Setting `-200%` outsets the segment by `40px`, with the rule segment drawn through the `20px` gap and into the previous column.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

row-rule-inset-cap-start =   
  <inset-value>    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#examples)

--------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#basic_usage)

This example demonstrates setting `row-rule-inset-cap-start` to inset the start edge of cap segments on flex containers.

#### HTML

The markup includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each containing seven children. The only difference between the two containers is that the second one has an added `column` class.

html

    <h1>Insetting cap row rule endpoints</h1>
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
 property to turn the `.flexbox` elements into flex containers. We balance the items into three flex lines using with [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 and [`flex-line-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
. We define a light blue [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 to be painted in both column and row gaps, then overwrite the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
, setting darker `blue` row gap decorations. Finally, we set the `row-rule-inset-cap-start` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      row-rule-color: blue;
    
      row-rule-inset-cap-start: 16px;
    }
    

We also set the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 on the `.column` container, to change the main axis of the flex container, and make the items flow in columns rather than rows.

css

    .column {
      flex-direction: column;
    }
    

The rest of the CSS is hidden for brevity.

    body {
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
      gap: 42px;
      rule: 1px solid black;
      width: 100vw;
      padding: 0 50px;
      box-sizing: border-box;
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
      @supports not (row-rule-inset-cap-start: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap-start property";
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
      containers[0].style.rowRuleInsetCapStart = val;
      containers[1].style.rowRuleInsetCapStart = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-column-rule-inset-cap-start](https://drafts.csswg.org/css-gaps-1/#propdef-column-rule-inset-cap-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`column-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-start)
    
*   [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
    
*   [`row-rule-inset-junction-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
    
*   `row-rule-inset-start` shorthand
*   [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
     shorthand
*   `row-rule-inset` shorthand
*   `rule-inset-start` shorthand
*   [`rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
    
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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule-inset-cap-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule-inset-cap-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
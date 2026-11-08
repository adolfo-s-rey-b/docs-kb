*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#mdn-search)
    

`column-rule-inset-cap-end` CSS property
========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#browser_compatibility)
 carefully before using this in production.

The **`column-rule-inset-cap-end`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the bottom of column rule segment [cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#understanding_cap_end)
 at the container's end edge, and cap endpoints where no rule segments intersect.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#try_it)

-----------------------------------------------------------------------------------------------------------------

    column-rule-inset-cap-end: -20px;
    

    column-rule-inset-cap-end: 0;
    

    column-rule-inset-cap-end: 1em;
    

    column-rule-inset-cap-end: 100%;
    

    column-rule-inset-cap-end: overlap-join;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    column-rule-inset-cap-end: overlap-join;
    
    /* <length-percentage> values */
    column-rule-inset-cap-end: 0;
    column-rule-inset-cap-end: 1em;
    column-rule-inset-cap-end: -5px;
    column-rule-inset-cap-end: -25%;
    
    /* Global values */
    column-rule-inset-cap-end: inherit;
    column-rule-inset-cap-end: initial;
    column-rule-inset-cap-end: revert;
    column-rule-inset-cap-end: revert-layer;
    column-rule-inset-cap-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#values)

This property is specified as a single value from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#overlap-join)

Resolves to `0`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the cap endpoint, which is either the width of the `row-gap` or `0`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#description)

---------------------------------------------------------------------------------------------------------------------------

The `column-rule-inset-cap-end` property can be used to inset the end edge of [cap segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#understanding_cap_end)
. The default value is `0`, which is the same as `overlap-join`. Positive values reduce the segment size, while negative values increase it.

Column rules are painted within a column gap as one or more segments, with segments occurring between:

*   Adjacent columns in CSS grid layouts.
*   Flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Columns in multi-col layouts.

Whether a column rule spans multiple rows or is broken into multiple segments is defined by the [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
 property, with interior breaks between column rule segments being the size of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
.

Length `column-rule-inset-cap-end` values inset segments by the specified value — for both interior and end edge cap segments. Negative length values create an outset, with end edge cap segments extending beyond the container's end edge.

[Percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#understanding_percentage_values)
 are relative to the size of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 for interior segments. For end edge cap segments, percentage values are relative to `0`, so percentage values never cause cap segment endpoints at the container's end edge to extend beyond the container.

The `column-rule-inset-cap-end` property is a constituent property of several [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset the start and end caps, the `column-rule-inset-cap-end` property, along with the [`column-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-start)
     property, can be set using the [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
     shorthand.
    
*   To inset the ends of all column segments, the `column-rule-inset-cap-end` property, along with the [`column-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end)
     property, can be set using the `column-rule-inset-end` shorthand.
    
*   To inset all row and column cap and junction endpoints, the `column-rule-inset-end` property, along with the `row-rule-inset-end` property, can be set using the `rule-inset-end` shorthand.
    

All segment endpoints, including this property's `-start`, `-junction`, and `row-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding cap end](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#understanding_cap_end)

A _cap segment endpoint_ is any segment endpoint that is not a junction segment endpoint. This includes endpoints at the container's content edges, as well as endpoints at a gap junction where no other rule or column segments are present.

The `column-rule-inset-cap-end` property controls the inset of the bottom edge of column cap segment endpoints, allowing the segments to be shrunk or extended.

Column cap segment endpoints are not affected by `column-rule-break` property value settings, which only control junction segment breaks. They are, however, affected by the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 properties, which define whether column- and row-rule segments are painted in gaps adjacent to empty areas.

Column cap segment endpoints only exist at the end edge of the container and at interior gaps where no other column or row rule segments are present. Therefore, whether segments are painted (or would otherwise be painted if the `rule` were set to a visible value) impacts which column segments are end cap segments.

In the following demonstration, the bottom of column rule segments end in cap endpoints. With `column-rule-inset-cap-end: 16px` set, all the column segments are inset by `16px`. Change the inset `<length>` value to better visualize which segments end in cap segment endpoints.

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
      column-rule-inset-cap-end: 16px;
    
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
      @supports not (column-rule-inset-cap-end: 16px) {
        body::before {
          content: "Your browser doesn't support the column-rule-inset-cap-end property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      column-rule-inset-cap-end: 100%;
      column-rule-style: inset;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      o.innerText =
        ul.style.columnRuleInsetCapEnd = `${inset.value}${inset.dataset["unit"]}`;
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.columnRuleStyle = "repeat(2, solid), double";
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
    

Change the inset. If `0px` is set, the end of the column rules will align with the end of the container. This is the default. Setting `-32px` outsets the segments by `32px`, with the lines being drawn `32px` past the end edge of the container. As column rules don't impact the box model, these lines have no impact on the layout of the container or the rest of the content.

Select `around` as the `rule-visibility-items` value. This value paints rules in a gap segment if at least one of the two adjacent areas is occupied by an item. The double line-style column rules, which appear when the `rule-visibility-items` property is set to `around` do not end in a cap endpoint. The last two column rules end at interior gaps where row rule segments are present, so these column segments are not cap segment endpoints. Therefore, the `column-rule-inset-cap-end` property does not affect those segment endpoints.

Select `between` as the `rule-visibility-items` value, which paints rules in gap segments only if both adjacent areas are occupied by an item. The last row rule in the second row gutter ends at the third column gap. The third column rule ends at an interior gap where a row rule segment is present, so this column segment is not a cap segment endpoint and is not affected by the `column-rule-inset-cap-end` property. The last two column rules, however, end at interior gaps where no other rule segments are present, so these column segments are cap segment endpoints and therefore are affected by the `column-rule-inset-cap-end` property.

### [Understanding percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#understanding_percentage_values)

The length a percentage value is relative to depends on the endpoint location. Interior endpoint percentage values are relative to the width of the gap at the cap endpoint, so relative to the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 if abutting a rule gap, and `0` at the bottom edge of the container.

In this demonstration, these endpoints are denoted by the inset, dark and light, line style. If the cap segment endpoint is at the container's edge, the percentage is relative to `0`, so it always computes to `0` (which is why only the `between` value has an effect).

Select `around` as the `rule-visibility-items` value. The first three columns end at the container edge, so any percentage value will resolve to `0`. The last two column rules end at interior gaps where row rule segments are present, so these column segments are not cap segment endpoints.

Select `between` as the `rule-visibility-items` value. The first two columns end at the container edge, so they have a `0` inset. The third column rule ends at an interior gap where a row rule segment is present, so this column segment is not a cap segment endpoint. The last two column rules end at interior gaps where no other rule segments are present, so the percentage offset is relative to the size of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 width, which in this case is `20px`.

Setting `100%` insets the end of the last two column rule segments by `20px`. Setting `-200%` will outset these segments by `40px`, with the lines being drawn through the `20px` gap and `20px` protruding into the last row of items. Negative percentage values that compute to a length larger than the combined height of the last row and row gap will cause the last two column rules to protrude below the container's end edge.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

column-rule-inset-cap-end =   
  <inset-value>    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#examples)

---------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#basic_usage)

This example demonstrates setting `column-rule-inset-cap-end` to inset the end edge of cap segments on flex containers.

#### HTML

The markup includes two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each containing seven children. The only difference between the two containers is that the second one has an added `column` class.

html

    <h1>Insetting cap column rule endpoints</h1>
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
, setting darker `blue` column gap decorations. Finally, we set the `column-rule-inset-cap-end` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      column-rule-color: blue;
    
      column-rule-inset-cap-end: 16px;
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
      @supports not (column-rule-inset-cap-end: 16px) {
        body::before {
          content: "Your browser doesn't support the column-rule-inset-cap-end property";
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
      containers[0].style.columnRuleInsetCapEnd = val;
      containers[1].style.columnRuleInsetCapEnd = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-column-rule-inset-cap-end](https://drafts.csswg.org/css-gaps-1/#propdef-column-rule-inset-cap-end) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end#see_also)

---------------------------------------------------------------------------------------------------------------------

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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule-inset-cap-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule-inset-cap-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-inset-cap-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-inset-cap-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-inset-cap-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-inset-cap-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
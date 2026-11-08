*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#mdn-search)
    

`row-rule-inset-cap` CSS property
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#browser_compatibility)
 carefully before using this in production.

The **`row-rule-inset-cap`** [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the row rule segment [cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_cap_endpoints)
 at the container's left and right edges, and endpoints where the segments don't intersect other column or row segments.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#try_it)

----------------------------------------------------------------------------------------------------------

    row-rule-inset-cap: -20px;
    

    row-rule-inset-cap: 0;
    

    row-rule-inset-cap: 1em;
    

    row-rule-inset-cap: 100%;
    

    row-rule-inset-cap: overlap-join;
    

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
      rule: solid thick rebeccapurple;
      row-rule-color: magenta;
      gap: 0.5em;
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
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
    
*   [`row-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    row-rule-inset-cap: overlap-join;
    
    /* <length-percentage> values */
    row-rule-inset-cap: 0;
    row-rule-inset-cap: 1em;
    row-rule-inset-cap: -5px;
    row-rule-inset-cap: -25%;
    
    /* Two values */
    row-rule-inset-cap: overlap-join 1em;
    row-rule-inset-cap: -5px -25%;
    
    /* Global values */
    row-rule-inset-cap: inherit;
    row-rule-inset-cap: initial;
    row-rule-inset-cap: revert;
    row-rule-inset-cap: revert-layer;
    row-rule-inset-cap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#values)

This property is specified as a one or two values from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#overlap-join)

Resolves to `0`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. [Percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_percentage_values)
 are relative to the crossing gap width, which is the width of the `column-gap` for segment endpoints at gap junctions and `0` for endpoints at the container's edge.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#description)

--------------------------------------------------------------------------------------------------------------------

The `row-rule-inset-cap` shorthand property can be used to set the [`row-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
 and [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
 properties, insetting or outsetting both the left and right edges of [cap segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_cap_endpoints)
 in a single declaration.

If one value is specified, both properties are set to that value. If two values are specified, `-start` is set to the first value and `-end` is set to the second. The default value is `0`, which in the case of cap endpoints, is the same as `overlap-join`. Positive values reduce, or inset, the segment size, while negative values increase, or outset, it.

Row rules are painted within a row gap as one or more segments, with segments occurring between:

*   Adjacent rows in CSS grid layouts.
*   Adjacent flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Adjacent rows in multi-col layouts, which may exist when [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
     is set to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    .

Whether a row rule spans multiple columns or is broken into multiple segments is defined by the [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
 property, with interior breaks between row rule segments generally being the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
.

Length `row-rule-inset-cap` values inset segments by the specified value. Negative length values create an outset, making the segment wider and causing cap segments on the left and right edges of the container to extend beyond the container's edge.

[Percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_percentage_values)
 are relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 for interior segments. Setting `-50%` will extend the segment to the middle of the gap, while `-100%` will extend the segment across the entire gap. For cap segments at the container's edge, percentage values are relative to `0`, so percentage values have no effect on cap segment endpoints at the container's edge.

The `row-rule-inset-cap` property is a constituent property of a few [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset the left and right sides of all row segments, the `row-rule-inset-cap` property, along with the [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
     property, can be set using the `row-rule-inset` shorthand.
    
*   To inset both row and column cap segment endpoints, the `row-rule-inset-cap` property, along with the [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
     property, can be set using the [`rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
     shorthand.
    

All segment endpoints, including this property's `-junction` and `column-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_cap_endpoints)

A _cap segment endpoint_ is any segment endpoint that is not a junction segment endpoint. This includes endpoints at the container's content edges, as well as endpoints at a gap junction where no other column or row segments are present.

The `row-rule-inset-cap` property can outset or inset the start and end of row rules at the container edge, and the start and end of interior row segments where no other segments are present.

Cap segments are impacted by the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 properties, which define whether row- and column-rule segments are painted in gaps adjacent to empty areas. Changing the value from `auto` to `between` or `around` can create additional interior cap segments.

In the following demonstration, the rows end in cap endpoints at the container's left and right edges. With `row-rule-inset-cap: -32px` set, these endpoints are outset by `32px`. Change the inset `<length>` value to better visualize which segments start or end with cap segment endpoints.

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
      row-rule-inset-cap: -32px;
    
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
      @supports not (row-rule-inset-cap: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      row-rule-inset-cap: 100%;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      o.innerText =
        ul.style.rowRuleInsetCap = `${inset.value}${inset.dataset["unit"]}`;
    });
    

    visibility.addEventListener("change", () => {
      ul.style.ruleVisibilityItems = `${visibility.value}`;
      if (visibility.value === "between") {
        ul.style.rowRuleStyle = "repeat(2, solid), double";
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
    

Setting `0px` aligns the row rule ends with the left and right container edges. This is the default.

Select `between` as the `rule-visibility-items` value. This value paints rules in gap segments only if the two adjacent areas are occupied by items. Again, we have row rule cap endpoints at the start edge of the container, but now we have none at the end edge. The third row rule, denoted with a double-line style, has two additional cap endpoints: the end-side of the segment between `11` and `15` and the start-side of the segment between `12` and `16`. These do not meet any other rule segments; therefore, they are affected by the `row-rule-inset-cap-start` property.

In this case, the `around` value of the `rule-visibility-items` property, which paints rules in a gap segment as long as one adjacent area is occupied by an item, did not create additional cap segment endpoints. All the interior segment endpoints end in junctions where there are column segments, thus creating junction, not cap, segment endpoints. Junction endpoints can be inset using the [`row-rule-inset-junction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
 shorthand property.

### [Understanding percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#understanding_percentage_values)

The length a percentage value is relative to depends on the endpoint location. Interior endpoint percentage values are relative to the width of the gap at the cap endpoint, so relative to the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 if abutting a rule gap, plus any additional spacing added due to [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 settings, and `0` at the edge of the container. For example, `row-rule-inset-cap: 50%` resolves to half the gap junction size at an interior cap (half the size of the `column-gap` value), and `0` at the container edges.

This example is not broken. When `rule-visibility-items` is set to `normal`, every row cap endpoint abuts the left or right edge of the container, so any percentage value set will be relative to `0`.

Select `around` as the `rule-visibility-items` value. The first three rows start and the first and last row end at the container edge. Any percentage values for these row cap segment endpoints will resolve to `0`. All the other segments end at interior gaps where column rule segments are present, so these row segments are not cap segment endpoints.

Select `between` as the `rule-visibility-items` value. As in the previous demonstration, this value creates two interior cap segment endpoints: the right side of the segment between items `11` and `15` and the left side of segment between items `12` and `16` again do not meet any other rule segments. For these two cap endpoints, the percentage offset is relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 width, which in this case is `20px`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

row-rule-inset-cap =   
  <inset-value> <inset-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#examples)

--------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#basic_usage)

This example demonstrates setting `row-rule-inset-cap` to inset the row rule cap segment endpoints on flex containers.

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
 property to turn the `.flexbox` elements into flex containers. We balance the items into three flex lines using [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 and [`flex-line-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
. We define a `lightblue` [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 to paint both column and row gaps, then overwrite the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
, setting darker `blue` row gap decorations. Finally, we set the `row-rule-inset-cap` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      row-rule-color: blue;
    
      row-rule-inset-cap: 16px;
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
      @supports not (row-rule-inset-cap: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap property";
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
      containers[0].style.rowRuleInsetCap = val;
      containers[1].style.rowRuleInsetCap = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset. Note how the row segments grow and shrink only at segment cap ends, either their left side, their right side, or both directions — the ends that don't intersect other row or column segments.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-row-rule-inset-cap](https://drafts.csswg.org/css-gaps-1/#propdef-row-rule-inset-cap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`row-rule-inset-cap-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
    
*   [`row-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
    
*   `row-rule-inset` shorthand
*   [`column-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
     shorthand
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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule-inset-cap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule-inset-cap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
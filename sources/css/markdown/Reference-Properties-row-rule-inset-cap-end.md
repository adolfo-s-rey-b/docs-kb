*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#mdn-search)
    

`row-rule-inset-cap-end` CSS property
=====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#browser_compatibility)
 carefully before using this in production.

The **`row-rule-inset-cap-end`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to offset the end of row rule segment [cap endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#understanding_cap_end)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#try_it)

--------------------------------------------------------------------------------------------------------------

    row-rule-inset-cap-end: -20px;
    

    row-rule-inset-cap-end: 1.25em;
    

    row-rule-inset-cap-end: 0;
    

    row-rule-inset-cap-end: 100%;
    

    row-rule-inset-cap-end: overlap-join;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    row-rule-inset-cap-end: overlap-join;
    
    /* <length-percentage> values */
    row-rule-inset-cap-end: 0;
    row-rule-inset-cap-end: 1rem;
    row-rule-inset-cap-end: -15px;
    row-rule-inset-cap-end: -50%;
    
    /* Global values */
    row-rule-inset-cap-end: inherit;
    row-rule-inset-cap-end: initial;
    row-rule-inset-cap-end: revert;
    row-rule-inset-cap-end: revert-layer;
    row-rule-inset-cap-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#values)

This property is specified as a single value from the following list:

[`overlap-join`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#overlap-join)

Resolves to `0`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the size of the inset. Percentage values are relative to the cap endpoint, which is either the height of the `column-gap` width or `0`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#description)

------------------------------------------------------------------------------------------------------------------------

The `row-rule-inset-cap-end` property can be used to inset the end edge of row rule [cap segment endpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#understanding_cap_end)
 at the container's end edge and cap endpoints where no rule segments intersect. The default value is `0`, which is the same as `overlap-join`. Positive values reduce the row rule segment size, while negative values increase it.

Row rules are painted within a row gap as one or more segments, with segments occurring between:

*   Adjacent rows in CSS grid layouts.
*   Adjacent flex items or flex lines in flex layouts, depending on the `flex-direction`.
*   Adjacent rows in multi-col layouts if the [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
     is set to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    .

Whether a row rule spans multiple columns or is broken into multiple segments is defined by the [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
 property, with interior breaks between row rule segments being the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
.

Length `row-rule-inset-cap-end` values are inset by the value specified for both interior and end edge cap segments. Negative length values create an outset, with end edge cap segments extending beyond the container's end edge.

[Percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#understanding_percentage_values)
 for interior cap segment endpoint insets are relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
. For end edge cap segments, percentage values are relative to `0`, so percentage values never inset or outset cap segment endpoints at the container's end edge.

The `row-rule-inset-cap-end` property is a constituent property of several [shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
:

*   To inset both the start and ends of row rule caps, the `row-rule-inset-cap-end` property, along with the [`row-rule-inset-cap-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
     property, can be set using the [`row-rule-inset-cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
     shorthand.
    
*   To inset the ends of all row segments, the `row-rule-inset-cap-end` property, along with the [`row-rule-inset-junction-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end)
     property, can be set using the `row-rule-inset-end` shorthand.
    

All segment endpoints, including this property's `-start`, `-junction`, and `column-` equivalents, can be set using the `rule-inset` shorthand.

### [Understanding cap end](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#understanding_cap_end)

A _cap segment endpoint_ is any segment endpoint that is not a junction segment endpoint. This includes endpoints at the container's content edges, as well as endpoints at a gap junction where no other column or row segments are present.

The `row-rule-inset-cap-end` controls the inset of cap segment endpoints occurring at the end of a row rule segment. Depending on the writing mode, the property can inset the right or left edge of row rule segments at interior gaps with no other row or column rule segments, or at the container's end edge.

This property is affected by the [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
 properties, which define whether row- and column-rule segments are painted in gaps adjacent to empty areas. As row cap segment endpoints only exist at the end edge of the container and at interior gaps where no other row or column rule segments are present, whether segments are painted (or would otherwise be painted if the `rule` were set to a visible value) impacts which row segments are end cap segments.

In the following demonstration, the end segments of row rules with a solid line style end in a cap endpoint. With `row-rule-inset-cap-end: 16px` set, these endpoints are all inset by `16px`. Change the inset `<length>` value to better visualize which segments end in cap segment endpoints.

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
      <li class="a">18</li>
      <li class="b">22</li>
      <li class="c">24</li>
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
      rule-overlap: row-over-column;
      rule-visibility-items: normal;
      rule-break: intersection;
      row-rule-inset-cap-end: -32px;
    
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
    .a {
      grid-column: 5 / 6;
      grid-row: 3 / 4;
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
      @supports not (row-rule-inset-cap-end: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap-end property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    ul {
      row-rule-inset-cap-end: 100%;
      row-rule-style: inset;
    }
    

    const inset = document.getElementById("inset");
    const visibility = document.getElementById("visibility");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    inset.addEventListener("input", () => {
      output.innerText =
        ul.style.rowRuleInsetCapEnd = `${inset.value}${inset.dataset["unit"]}`;
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
    

Setting `-32px` outsets the end of all the row rules by `32px`: the lines are drawn `32px` past the right edge of the container. As row rules don't impact the box model, these lines have no impact on the layout of the container or the rest of the content. If `0px` is set, the end of the row rules will align with the edge of the container. This is the default.

The double line-style row rule segments, which appear when the `rule-visibility-items` property is set to `between`, add a cap endpoint. The `between` value only paints rules in gap segments between two adjacent areas occupied by an item. Because the row rule segment above item `24` ends at an intersection with no other row or column rule segments present, this is a cap endpoint, and therefore is affected by the `row-rule-inset-cap-end` property. The segment above item `22` ends at a gap junction where a rule segment is present, so it is not a cap endpoint. There are fewer segments abutting the right edge of the container, but the remaining segment, between `6` and `12`, remains a cap endpoint.

Rule segments abutting the end edge of the container are always row-rule cap end segments affected by the value of the `row-rule-inset-cap-end` property.

### [Understanding percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#understanding_percentage_values)

The length a percentage value is relative to depends on the endpoint location. Interior endpoint percentage values are relative to the width of the gap at the cap endpoint, so relative to the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 if abutting a rule gap, and `0` at the top edge of the container.

This example isn't broken; all the cap segments end at the container's edge, so all the insets are `0` by default.

If you select `around` as the `rule-visibility-items` value, the only cap segment endpoints are at the edge of the container, so percentage value insets continue to resolve to `0`.

Select `between` as the `rule-visibility-items` value. We now have a row rule end cap affected by the inset — see the segment between grid items `18` and `24`! This segment ends at an interior gap where no other rule segments are present, so the percentage inset is relative to the size of the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 width, which in this case is `20px`. Setting `100%` insets the end by `20px`. Setting `-200%` will outset the segment by `40px`, with the lines drawn through the `20px` gap into the next column.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

row-rule-inset-cap-end =   
  <inset-value>    
  
<inset-value> =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlap-join           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#examples)

------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#basic_usage)

This example demonstrates setting `row-rule-inset-cap-end` to inset the end edge of cap segments on flex containers.

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
, setting darker `blue` vertical gap decorations. Finally, we set the `row-rule-inset-cap-end` to `16px`.

css

    .flexbox {
      display: flex;
      flex-wrap: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid lightblue;
      row-rule-color: blue;
    
      row-rule-inset-cap-end: 16px;
    }
    

We also set the [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 on the `.column` container, to change the main axis of the flex container, and make the items flow in columns rather than rows. The rest of the CSS is hidden for brevity.

css

    .column {
      flex-direction: column;
    }
    

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
      @supports not (row-rule-inset-cap-end: 16px) {
        body::before {
          content: "Your browser doesn't support the row-rule-inset-cap-end property";
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
      containers[0].style.rowRuleInsetCapEnd = val;
      containers[1].style.rowRuleInsetCapEnd = val;
      output.innerText = val;
    });
    

#### Result

Change the size of the inset.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-row-rule-inset-cap-end](https://drafts.csswg.org/css-gaps-1/#propdef-row-rule-inset-cap-end) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end#see_also)

------------------------------------------------------------------------------------------------------------------

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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-rule-inset-cap-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-rule-inset-cap-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-rule-inset-cap-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-rule-inset-cap-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
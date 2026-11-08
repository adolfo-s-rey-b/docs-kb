*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#mdn-search)
    

`column-rule-break` CSS property
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#browser_compatibility)
 carefully before using this in production.

The **`column-rule-break`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the behavior for breaking column rules into segments wherever column rules intersect row gaps.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#try_it)

---------------------------------------------------------------------------------------------------------

    column-rule-break: none;
    

    column-rule-break: normal;
    

    column-rule-break: intersection;
    

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
        <i>S</i>
        <i>T</i>
        <i>U</i>
        <i>V</i>
        <i>W</i>
        <i>X</i>
        <i>Y</i>
        <i>Z</i>
      </div>
    </section>
    

    #example-element {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      column-rule: solid thick orange;
      row-rule: solid thick lavender;
      gap: 15px;
      rule-overlap: column-over-row;
    }
    #example-element i {
      padding: 5px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-rule-break: none;
    column-rule-break: normal;
    column-rule-break: intersection;
    
    /* Global values */
    column-rule-break: inherit;
    column-rule-break: initial;
    column-rule-break: revert;
    column-rule-break: revert-layer;
    column-rule-break: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#values)

This property is specified as a single keyword from the following list:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#none)

There are no breaks in column rules when they intersect row gaps; rather, a continuous column rule is painted the whole height of the container, from edge to edge.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#normal)

In grid and flex containers, behaves as `none`. In multi-col, behaves as `intersection`. This is the default value.

[`intersection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#intersection)

Column rules always break when they intersect row gaps, with column rule segments starting and ending at container and gap edges.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#description)

-------------------------------------------------------------------------------------------------------------------

The `column-rule-break` property specifies whether or not to break column rules into segments when they cross row gaps.

Column rules are painted within a column gap as one or more segments, with segments occurring between adjacent grid items in separate columns, between flex items or flex lines in flex layouts depending on the `flex-direction`, or between columns in multi-col layouts.

The `column-rule-break` property only determines if the break occurs. By default, the break between column rule segments is the height of the row gap, as each segment starts and ends at the edge of the gap (or edge of the container). If the row gap is `0`, this break may not be visible. The end positions can be controlled with the `column-rule-inset` properties.

If `column-rule-break` is set to `none`, there are no breaks. In this case, the column rule line is continuous, and any `column-rule-inset` values only affect the left and right edges of the column rule at the container's edge. When there are breaks, the `column-rule-inset` properties affect the start and end of every column rule segment.

The `column-rule-break` property, along with the [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
 property, can be set using the [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
 shorthand.

Whether a column rule is by default a single continuous segment or segments that break at row gaps depends on the container type.

### [Grid containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#grid_containers)

In grid containers, by default, column rule segments continue through row gap intersections, equivalent to `column-rule-break: none`. Setting `column-rule-break: intersection` forces the segments to break at every row gap they would otherwise cross.

    <h1>Default rule breaks in grid</h1>
    <div class="grid">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    <p>
      <label
        ><input type="checkbox" /> Set
        <code>column-rule-break: intersection</code></label
      >
    </p>
    

    h1,
    div {
      font-family: sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 1.25em;
    }
    h2 {
      font-size: 1em;
    }
    
    :has(:checked) .grid {
      column-rule-break: intersection;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      rule: 5px solid blue;
      row-rule-color: lightblue;
      rule-overlap: column-over-row;
      width: 100%;
    }
    
    .grid > div {
      border: 1px solid green;
      background-color: lime;
      height: 30px;
    }
    
    @layer no-support {
      @supports not (column-rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the column-rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

By default, there are no column rule breaks. Check the checkbox to set the `column-rule-break` to `intersection`, which makes the otherwise continuous rules break at every "cross" intersection. By default, the break between segments is the height of the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
, which was set to `20px` in this case.

### [Flex containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#flex_containers)

In flexbox, whether the column rules break at every row gap by default depends on the `flex-direction`. In horizontal writing modes, when set to `row` or `row-reverse`, the column rule breaks at every row gap, equivalent to `column-rule-break: intersection`. When the `flex-direction` is `column` or `column-reverse`, the column rule is continuous by default, equivalent to `column-rule-break: none`.

    <h1>Default rule breaks in flexbox</h1>
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
        ><input type="checkbox" /> Set
        <code>column-rule-break: intersection</code></label
      >
    </p>
    

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
    
    :has(:checked) .flexbox {
      column-rule-break: intersection;
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
    .flexbox {
      display: flex;
      flex-flow: balance;
      flex-line-count: 3;
      gap: 20px;
      rule: 5px solid blue;
      row-rule-color: lightblue;
      width: 100%;
    }
    .column {
      flex-flow: column balance;
      gap: 20px;
    }
    
    .flexbox > div {
      border: 1px solid green;
      background-color: lime;
      flex: 1 1 auto;
      height: 30px;
    }
    
    @layer no-support {
      @supports not (column-rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the column-rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

In horizontal writing modes, setting the `column-rule-break` to `intersection` only impacts the column rules in the `column` and `column-reverse` scenarios.

### [Multi-col containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#multi-col_containers)

In multi-col containers, the default `normal` value behaves the same as `intersection`. While the row decorations are continuous by default, column rules break at every intersection. Column rules break into segments at every row gap, with each segment starting and ending at the edge of the gap. These start and end positions can be changed with the `column-rule-inset` properties.

    <h1>Default rule breaks in multi-col</h1>
    <ol>
      <li>One fish</li>
      <li>Two fish</li>
      <li>Red fish</li>
      <li>Blue fish</li>
      <li>Black fish</li>
      <li>Blue fish</li>
      <li>Old fish</li>
      <li>New fish.</li>
      <li>This one has a little star.</li>
      <li>This one has a little car.</li>
      <li>Say! What a lot</li>
      <li>Of fish there are.</li>
      <li>Yes. Some are blue.</li>
      <li>And some are blue.</li>
      <li>Some are old.</li>
      <li>And some are new.</li>
      <li>Some are sad.</li>
      <li>And some are glad.</li>
      <li>And some are very, very bad.</li>
      <li>Why are they</li>
      <li>Sad and glad and bad?</li>
      <li>I do not know.</li>
      <li>Go ask your dad.</li>
    </ol>
    <fieldset>
      <legend>Set <code>column-rule-break:</code></legend>
      <label
        ><input type="radio" name="break" value="none" /> <code>none</code></label
      >
      <label
        ><input type="radio" name="break" value="normal" checked />
        <code>normal</code></label
      >
      <label
        ><input type="radio" name="break" value="intersection" />
        <code>intersection</code></label
      >
    </fieldset>
    

    h1,
    ol,
    fieldset {
      font-family: sans-serif;
      text-align: center;
    }
    h1 {
      font-size: 1.25em;
    }
    ol {
      columns: 3 / 4em;
      gap: 20px;
      rule: 5px solid blue;
      row-rule-color: lightblue;
      rule-overlap: column-over-row;
    }
    li {
      border: 1px solid green;
      background-color: lime;
      list-style-type: none;
      margin-bottom: 5px;
    }
    :has([value="normal"]:checked) ol {
      column-rule-break: normal;
    }
    :has([value="intersection"]:checked) ol {
      column-rule-break: intersection;
    }
    :has([value="none"]:checked) ol {
      column-rule-break: none;
    }
    label {
      margin-right: 20px;
    }
    @layer no-support {
      @supports not (column-rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the column-rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

If you select `none`, the column rule will no longer break into segments; rather, it will continue from the top of the container, until it reaches the bottom edge. The `column-rule-inset` properties can be used to offset the ends of the column gap decorations.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

column-rule-break =   
  none          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  intersection    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#basic_usage)

In this example, we use the `column-rule-break` property to break each rule segment in a grid container, creating column rule segments between row gaps. Changing the `row-gap` property changes the segment size.

#### HTML

We create a list of 50 items and a slider to select the row gap width. Most of the HTML is hidden for brevity.

html

    <ul>
      <li>1</li>
      <li>2</li>
      ...
      <li>49</li>
      <li>50</li>
    </ul>
    

    <p>
      <label
        >Change the width of the row gap.
        <input type="range" min="0" max="32" value="16" id="gap"
      /></label>
      <output id="o"></output>
    </p>
    <ul id="ul">
      <li>1</li>
      <li>2</li>
      <li>3</li>
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
      <li>18</li>
      <li>19</li>
      <li>20</li>
      <li>21</li>
      <li>22</li>
      <li>23</li>
      <li>24</li>
      <li>25</li>
      <li>26</li>
      <li>27</li>
      <li>28</li>
      <li>29</li>
      <li>30</li>
      <li>31</li>
      <li>32</li>
      <li>33</li>
      <li>34</li>
      <li>35</li>
      <li>36</li>
      <li>37</li>
      <li>38</li>
      <li>39</li>
      <li>40</li>
      <li>41</li>
      <li>42</li>
      <li>43</li>
      <li>44</li>
      <li>45</li>
      <li>46</li>
      <li>47</li>
      <li>48</li>
      <li>49</li>
      <li>50</li>
    </ul>
    

#### CSS

We define the unordered list as an 8-column container, creating rows and columns with the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property and setting [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to `none` to remove the bullets. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `20px` to provide enough room between the rows and columns to fit our `20px` solid row and column rules. We include the [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
 property to paint the column decoration on top of any row decorations. Last, we set the column rules to break at every intersection.

css

    ul {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      list-style-type: none;
      gap: 20px;
    
      column-rule: 10px solid olive;
      row-rule: 10px solid palegoldenrod;
      rule-overlap: column-over-row;
    
      column-rule-break: intersection;
    }
    

The rest of the CSS is hidden for brevity.

    ol {
      place-items: center;
      width: 95vw;
    }
    li {
      text-align: center;
      font-family: sans-serif;
      line-height: 50px;
    }
    @layer no-support {
      @supports not (column-rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the column-rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

    const gap = document.getElementById("gap");
    const ul = document.getElementById("ul");
    const output = document.getElementById("o");
    
    gap.addEventListener("input", () => {
      output.innerText = ul.style.rowGap = `${gap.value}px`;
    });
    

#### Result

Make the row gaps wider and note how the breaks between column segments grow. Bring the row gap width down to `0px`, and notice how the column decoration appears continuous. It isn't! The `0px` gap between segments may not be visible, but the segments still start and end at the gap, so any offsets set with `column-rule-inset-*` properties still apply.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-column-rule-break](https://drafts.csswg.org/css-gaps-1/#propdef-column-rule-break) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
    
*   [`rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
     shorthand
*   `rule-inset` shorthand
*   [`rule-overlap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-rule-break/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-rule-break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-rule-break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-rule-break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd3a0fd9820ca27a3f17642841af8426735cb4ec3%0A*+Document+last+modified%3A+2026-10-08T09%3A49%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
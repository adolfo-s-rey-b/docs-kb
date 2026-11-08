*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#mdn-search)
    

`rule-break` CSS property
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#browser_compatibility)
 carefully before using this in production.

The **`rule-break`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the behavior for breaking column and row rules into segments where rows and column gaps intersect, setting [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
 and [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
 to the same value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#try_it)

--------------------------------------------------------------------------------------------------

    rule-break: none;
    

    rule-break: normal;
    

    rule-break: intersection;
    

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
      row-rule: solid thick orange;
      column-rule: solid thick purple;
      gap: 10px;
    }
    #example-element i {
      padding: 5px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
    
*   [`row-rule-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    rule-break: none;
    rule-break: normal;
    rule-break: intersection;
    
    /* Global values */
    rule-break: inherit;
    rule-break: initial;
    rule-break: revert;
    rule-break: revert-layer;
    rule-break: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#values)

This property is specified as a single keyword from the following list:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#none)

There are no breaks where row and column rules intersect; rather, a single continuous decoration is painted from one end of each gap to the other.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#normal)

In flex and grid containers, behaves as `none`. In multi-col, `column-rule-break` behaves as `intersection` and `row-rule-break` behaves as `none`. This is the default value.

[`intersection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#intersection)

Rules always break when they intersect a gap, with rule segments starting and ending at container and gap edges.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#description)

------------------------------------------------------------------------------------------------------------

The `rule-break` property is used to set the behavior for breaking rules into segments when they cross gaps.

Gap decorations are painted within a gap as one or more gap decoration segments, with segments occurring between any two adjacent items. Depending on the container type, by default, these segments may either end at the edge of a gap, or the column and row rule may extend the entire height and width of the container.

When there is a break in a rule, by default, the segments start and end at the edge of the gaps. If the gap size is `0`, the break may not be visible. The `rule-break` property determines if the break occurs. You can control the size of the break at the end of each segment with the `rule-inset` properties. When there are no breaks, and the line is continuous, `rule-inset` properties only affect the rule at the start and end edges of the container. When there are breaks, the `rule-inset` properties affect the start and end of every rule segment.

Whether a rule is by default composed of a single continuous segment or segments that break when intersecting gaps depends on the container type.

### [Grid containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#grid_containers)

In grid containers, by default, rule segments continue through visible "cross" intersections. Setting `rule-break: intersection` will force the segments to break where they would otherwise cross.

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
        ><input type="checkbox" /> Set <code>rule-break: intersection</code></label
      >
    </p>
    

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
    
    :has(:checked) .grid {
      rule-break: intersection;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      rule: 5px solid red;
      width: 100%;
    }
    
    .grid > div {
      border: 1px solid green;
      background-color: lime;
      height: 30px;
    }
    
    @layer no-support {
      @supports not (rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

Check the checkbox to set the `rule-break` to `intersection`, which makes the continuous rules break at every "cross" intersection.

### [Flex containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#flex_containers)

In flexbox, when the `flex-direction` is `row` or `row-reverse`, the row rule is continuous, with the column segments starting and ending at the edge of the row gaps. When the `flex-direction` is `column` or `column-reverse`, the column rule is continuous, with the row segments starting and ending at the edge of the column gaps.

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
        ><input type="checkbox" /> Set <code>rule-break: intersection</code></label
      >
    </p>
    

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
    
    :has(:checked) .flexbox {
      rule-break: intersection;
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
      rule: 5px solid red;
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
      @supports not (rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

Note how, depending on the `flex-direction`, the column or row rules are continuous by default. If you set the `rule-break` to `intersection`, those continuous rules break at every intersection.

### [Multi-col containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#multi-col_containers)

In multi-col containers, the default `normal` behavior differs between row rules and column rules. Column rule segments start and end when they intersect a row gap, behaving as `column-rule-break: intersection`, while row rules don't break when they intersect a column gap, behaving as `row-rule-break: none`.

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
      <li>Yes. Some are red.</li>
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
      <legend>Set <code>rule-break:</code></legend>
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
    ol {
      columns: 3 / 4em;
      gap: 20px;
      rule: 5px solid red;
    }
    li {
      border: 1px solid green;
      background-color: lime;
      list-style-type: none;
      margin-bottom: 5px;
    }
    :has([value="normal"]:checked) ol {
      rule-break: normal;
    }
    :has([value="intersection"]:checked) ol {
      rule-break: intersection;
    }
    :has([value="none"]:checked) ol {
      rule-break: none;
    }
    label {
      margin-right: 20px;
    }
    @layer no-support {
      @supports not (rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

Check the radio buttons for each value to see the value's effect.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#formal_definition)

------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#formal_syntax)

----------------------------------------------------------------------------------------------------------------

rule-break =   
  [<'column-rule-break'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
    
  
[<column-rule-break>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
 =   
  none          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  intersection    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#examples)

------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#basic_usage)

In this example, we use the `rule-break` property to break each rule segment in a grid container so no rules intersect.

#### HTML

We create a list of 50 items. Most of the HTML is hidden for brevity.

html

    <ul>
      <li>1</li>
      <li>2</li>
      ...
      <li>49</li>
      <li>50</li>
    </ul>
    

    <ul>
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

We define the unordered list as a 8-column container, creating columns and rows with the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property and setting [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to `none` to remove the bullets. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `20px` to provide enough room between the columns and rows to fit our `20px` solid column and row rules. Last, we set the rule segments to break instead of intersect.

css

    ul {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      list-style-type: none;
      gap: 20px;
    
      row-rule: 20px solid palegoldenrod;
      column-rule: 20px solid olive;
    
      rule-break: intersection;
    }
    

The rest of the CSS is hidden for brevity.

    ol {
      place-items: center;
    }
    li {
      text-align: center;
      aspect-ratio: 1;
      font-family: sans-serif;
      line-height: 50px;
    }
    @layer no-support {
      @supports not (rule-break: intersection) {
        body::before {
          content: "Your browser doesn't support the rule-break property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-break](https://drafts.csswg.org/css-gaps-1/#propdef-rule-break) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break#see_also)

------------------------------------------------------------------------------------------------------

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

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-break/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd3a0fd9820ca27a3f17642841af8426735cb4ec3%0A*+Document+last+modified%3A+2026-10-08T09%3A49%3A05.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
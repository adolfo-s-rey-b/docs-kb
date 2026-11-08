*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#mdn-search)
    

`rule-color` CSS property
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#browser_compatibility)
 carefully before using this in production.

The **`rule-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property defines the colors of the lines drawn between columns and rows in multi-column grid, flex, and multi-col layouts, setting the colors of the column and row rules to the same value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#try_it)

--------------------------------------------------------------------------------------------------

    rule-color: purple;
    

    rule-color: rgb(48 125 222), rgb(222 48 125);
    

    rule-color: rgb(48 125 222), repeat(3, rgb(222 48 125));
    

    rule-color: purple, repeat(auto, red, yellow);
    

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
      rule: solid thick;
    }
    #example-element i {
      padding: 5px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Single <color> value */
    rule-color: purple;
    rule-color: rgb(192 56 78);
    rule-color: transparent;
    rule-color: hsl(0 100% 50% / 60%);
    
    /* Multiple values */
    rule-color: purple, magenta;
    rule-color: repeat(3, purple), repeat(3, transparent);
    rule-color: repeat(3, purple), repeat(3, yellow, blue);
    rule-color: purple, repeat(auto, transparent), purple;
    rule-color: purple, repeat(auto, blue, yellow), purple;
    rule-color: repeat(3, purple), repeat(auto, transparent), repeat(3, purple);
    
    /* Global values */
    rule-color: inherit;
    rule-color: initial;
    rule-color: revert;
    rule-color: revert-layer;
    rule-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#values)

The `rule-color` property accepts a comma-separated list of values, including:

[`<line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#line-color)

A [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 representing the color of the line.

[`<repeat-line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#repeat-line-color)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more as the first argument and one or more `<color>` values as subsequent arguments. The `<integer>` specifies how many times the `<color>` values should be repeated.

[`<auto-repeat-line-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#auto-repeat-line-color)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<color>` values as subsequent arguments. The provided `<color>` values are repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#description)

------------------------------------------------------------------------------------------------------------

The `rule-color` property defines the colors of any lines drawn in the gaps between columns and rows in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one column or row. It is a shorthand property that sets both the [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
 and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
 properties to the same value.

The value is a comma-separated list of components, which can include `<line-color>`, `<repeat-line-color>`, and `<auto-repeat-line-color>` types. The `rule-color` property, along with the [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
 and [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
 properties, can be set using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand.

### [Line colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#line_colors)

A `<line-color>` can be declared as any valid CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value. If the property value consists of only one `<color>`, all the rule lines will be that color. For example, if we declare the following, the lines in the gutters between columns and rows will all be blue:

css

    rule-color: blue;
    

When multiple `<line-color>` values are declared, they will be applied to lines painted in the column and row gutters in the order specified. If there are more rules than `<line-color>` values, the list of colors is repeated until every column-rule has a color. If we declare the following, for example, every odd rule will be red, and every even rule will be yellow.

css

    rule-color: red, yellow;
    

### [Repeated line colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#repeated_line_colors)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values passed as subsequent arguments the specified number of times. This allows the color values to be repeated as many times as you need without having to list them individually. The following declarations are equivalent:

css

    rule-color: blue, yellow, red, yellow, red, yellow, red;
    rule-color: blue, repeat(3, yellow, red);
    

This creates a list of seven colors. If the number of colors in the `rule-color` value's color list exceeds the number of gaps between columns and rows, the excess color values are ignored. If there are fewer colors than gutters, the list of values is repeated until every rule has an associated color. For example, if the container has three columns and 18 rows, the rule in the first column gutter will be blue and the second yellow. For the row rules, the sequence repeats, with the first, eighth, and fifteenth row rules being blue.

### [Auto-repeating line colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#auto-repeating_line_colors)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the `<color>` values passed as subsequent arguments will be repeated as many times as needed to fill in values for any column and row rules that are not explicitly specified by other components of the property value.

css

    rule-color: blue, repeat(auto, yellow), red;
    

In this case, the first column and row rules will be blue, the last will be red, and all others will be yellow. As long as there are at least two rules in either direction, the first rule will always be blue and the last will always be red. All the other rules will be yellow, which means if there are only 2 or 3 columns and rows, there will be no yellow lines.

The `auto` keyword within the `repeat()` function creates an auto-repeater that fills in values for the rule line colors that would not otherwise receive values from other parts of the list, preventing the list from being cycled. A `rule-color` value can include, at most, one `repeat(auto, <color>)`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#formal_definition)

------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#formal_syntax)

----------------------------------------------------------------------------------------------------------------

rule-color =   
  [<'column-rule-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
  
[<column-rule-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
 =   
  <line-color-list>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <auto-line-color-list>    
  
<line-color-list> =   
  <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<auto-line-color-list> =   
  <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <auto-repeat-line-color> , <line-color-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<line-color-or-repeat> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <repeat-line-color>    
  
<auto-repeat-line-color> =   
  repeat( auto , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<repeat-line-color> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#basic_example)

In this example, we define a single `<color>` for the lines drawn between the columns and rows of items in a grid container.

#### HTML

We create a list of 75 items. Most of the HTML is hidden for brevity.

html

    <ul>
      <li>1</li>
      <li>2</li>
      ...
      <li>74</li>
      <li>75</li>
    </ul>
    

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
      <li>51</li>
      <li>52</li>
      <li>53</li>
      <li>54</li>
      <li>55</li>
      <li>56</li>
      <li>57</li>
      <li>58</li>
      <li>59</li>
      <li>60</li>
      <li>61</li>
      <li>62</li>
      <li>63</li>
      <li>64</li>
      <li>65</li>
      <li>66</li>
      <li>67</li>
      <li>68</li>
      <li>69</li>
      <li>70</li>
      <li>71</li>
      <li>72</li>
      <li>73</li>
      <li>74</li>
      <li>75</li>
    </ul>
    

#### CSS

We define the unordered list as a 10-column container, creating columns and rows with the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the columns and rows to fit our `3px` dashed rule, and set [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to `none` to remove the bullets.

We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the items to fit our medium dashed rule. We set the `rule-color` to `#22BB22`, a green [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
 value:

css

    ul {
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      list-style-type: none;
      gap: 5px;
      rule-style: dashed;
      rule-width: medium;
    
      rule-color: #22bb22;
    }
    li {
      text-align: center;
      aspect-ratio: 1;
    }
    

    @layer no-support {
      @supports not (rule-color: red) {
        body::before {
          content: "Your browser doesn't support the rule-color property";
          background-color: wheat;
          text-align: center;
          padding: 1rem 0;
    
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
        }
      }
    }
    

#### Result

### [Multiple color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#multiple_color_values)

This example demonstrates declaring more than one color, and how the values are repeated when there are fewer values in the list of colors than gutters between columns and rows.

Using the same HTML and CSS as in the previous example, we include three comma-separated colors as the `rule-color` value:

    @layer no-support {
      @supports not (rule-color: red, blue) {
        body::before {
          content: "Your browser doesn't support multiple values for the rule-color property";
          background-color: wheat;
          text-align: center;
          padding: 1rem 0;
    
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
        }
      }
    }
    

css

    ul {
      rule-color: blue, yellow, red;
    }
    

#### Result

There are nine column gutters and six row gutters, but only three colors in our color list, so the list gets repeated, with the first, fourth, and seventh lines being blue.

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `rule-color` property value and how this function can help prevent complex values from becoming unwieldy.

#### CSS

To demonstrate how values can become complicated and the utility of the `repeat()` function, we declare two custom properties, which we use in four [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
 color function declarations to create blue, redish, tealish, and yellow colors. The redish and tealish `color-mix()` colors are within a `repeat()` function, set to repeat 3 times.

We also added a border around each grid item so you can see how the line is rule in the middle of the gutter between the columns and rows.

css

    ul {
      --base: yellow;
      --mixin: blue;
    
      rule-color:
        color-mix(in lch decreasing hue, var(--base) 0%, var(--mixin)),
        repeat(
          3,
          color-mix(in lch decreasing hue, var(--base) 58%, var(--mixin)),
          color-mix(in lch increasing hue, var(--base) 58%, var(--mixin))
        ),
        color-mix(in lch decreasing hue, var(--base) 100%, var(--mixin));
    }
    

#### Result

The grid has 10 columns and 7 rows, creating 9 column and 6 row gutters. The `repeat()` function repeats the two contained mixed colors three times, creating a color list with eight colors in all. While there is a lot of CSS to create the four colors, at least we didn't have to write out all eight `color-mix()` functions. Since there are more column gutters than list colors, the colors are repeated for the column gutters. As there are fewer row gutters than colors, the last two colors in the list are not used for the row gutters.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#using_auto_within_repeat)

This example demonstrates using `auto`, instead of an integer, within the `repeat()` function.

We use the same HTML and CSS as in the previous examples, but override the `rule-color` value. Here, we use `repeat(auto, <color>)` to set all the lines to be almost transparent black (`#00000033`), except the first and last, which we set to a solid `black`.

css

    ul {
      rule-color: black, repeat(auto, #00000033), black;
    }
    

#### Result

Even though there are more column rule lines than row rule lines, the `<auto-repeat-line-color>` value enables the creation of this symmetric effect.

    @layer no-support {
      @supports not (rule-color: repeat(3, red)) {
        body::before {
          content: "Your browser doesn't support `repeat()` functions within a rule-color property value";
          background-color: wheat;
          text-align: center;
          padding: 1rem 0;
    
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-color](https://drafts.csswg.org/css-gaps-1/#propdef-rule-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color#see_also)

------------------------------------------------------------------------------------------------------

*   The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`row-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04dfe418f2942ae739d41592c22fafa3679fc03c%0A*+Document+last+modified%3A+2026-10-05T17%3A37%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
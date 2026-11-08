*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#mdn-search)
    

`rule-style` CSS property
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#browser_compatibility)
 carefully before using this in production.

The **`rule-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property defines the line style of the lines drawn between columns and rows in multi-column grid, flex, and multi-col layouts, setting the styles of the column and row rules to the same value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#try_it)

--------------------------------------------------------------------------------------------------

    rule-style: solid;
    

    rule-style: dashed, dotted;
    

    rule-style: repeat(2, inset, dashed, double);
    

    rule-style: solid, repeat(auto, double), solid;
    

    rule-style: hidden;
    

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
      rule: solid rebeccapurple 7px;
      gap: 7px;
    }
    #example-element i {
      padding: 5px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#syntax)

--------------------------------------------------------------------------------------------------

css

    /* One value */
    rule-style: none;
    rule-style: hidden;
    rule-style: dotted;
    rule-style: dashed;
    rule-style: solid;
    rule-style: double;
    rule-style: groove;
    rule-style: ridge;
    rule-style: inset;
    rule-style: outset;
    
    /* Multiple values */
    rule-style: groove, double, dashed;
    rule-style: solid, repeat(5, ridge), solid;
    rule-style: dotted, repeat(auto, inset, outset), dotted;
    
    /* Global values */
    rule-style: inherit;
    rule-style: initial;
    rule-style: revert;
    rule-style: revert-layer;
    rule-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#values)

The `rule-style` property accepts a comma-separated list of values, including:

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#line-style)

A [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
: one of `none`, `hidden`, `dotted`, `dashed`, `solid`, `double`, `groove`, `ridge`, `inset`, or `outset`. The default value is `none`.

[`<repeat-line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#repeat-line-style)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with the first argument being an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 of `1` or more, and subsequent arguments being [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 values. The integer specifies how many times the `<line-style>` values should be repeated.

[`<auto-repeat-line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#auto-repeat-line-style)

A [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
 function, with `auto` as the first argument and one or more `<line-style>` values as subsequent arguments. The provided `<line-style>` values are repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#description)

------------------------------------------------------------------------------------------------------------

The `rule-style` property defines the line style of any column and row rule lines drawn in the gaps between columns and rows in [multi-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
, [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
, and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 containers with more than one column or row.

The `rule-style` sets both the [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
 and [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
 properties to the same value. The `rule-style` property, along with the [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
 and [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
 properties, can also be set using the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand.

The value is a comma-separated list of components, which can include `<line-style>`, `<repeat-line-style>`, and `<auto-repeat-line-style>` types.

If the property value has only one `<line-style>`, all the column and row rules will be that style. If we declare the following, all column and row rules will be `double`:

css

    rule-style: double;
    

When multiple `<line-style>` values are declared, they will be applied to rules in the order specified. If there are more rules than `<line-style>` values, the list of line styles is repeated until every column and row rule has a style. For example, if we declare the following, every odd rule will be `double`, and every even rule will be `inset`.

css

    rule-style: double, inset;
    

### [Repeated line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#repeated_line_styles)

The `repeat()` function, with an integer of `1` or greater as the first argument, can be used to repeat a valid list of CSS [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 values passed as subsequent arguments the specified number of times. This allows the same style to be repeated a set number of times without repeating the same value. You can include `<line-style>` keyword values or custom properties that resolve to a valid `<line-style>`. Using `repeat()` can make values easier to write, enabling recurring patterns to be written using a single function, regardless of the number of columns or rows. The following declarations are equivalent:

css

    rule-style: solid, outset, inset, outset, inset, outset, inset;
    rule-style: solid, repeat(3, outset, inset);
    

This creates a list of seven styles. If the number of styles in the `rule-style` value's style list exceeds the number of gaps between columns or rows, the excess style values are ignored. If the container has three columns or rows, the rule in the first gutter will be `solid` and the second `outset`.

If there are more gutters than styles, the list of styles is repeated. If the container has 8, 15, 22, or 29 columns or rows, this sequence of styles will be repeated one, two, three, or four times, respectively, with the last rule being `inset`.

### [Auto-repeating line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#auto-repeating_line_styles)

The `repeat()` function also accepts `auto` as the first argument instead of a positive integer. With `auto` as the first argument, the `<line-style>` values passed as subsequent parameters will be repeated as many times as needed to fill in values for any rules that are not explicitly specified by other components of the property value.

The `auto` keyword within the `repeat()` function creates an auto repeater that fills in values for column and row rules that would not otherwise receive values from other parts of the list, preventing the list from being cycled. Only one `repeat(auto, <line-style>)` is allowed within a `rule-style` value.

css

    rule-style: solid, repeat(auto, dotted), solid;
    

In this case, it doesn't matter if the container has 8, 15, 22, or 29 columns or rows; the first and last rules will always be `solid`, and all the other rules will be `dotted`. If there are only 2 or 3 columns and rows, there will be no dotted rules.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#formal_definition)

------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#formal_syntax)

----------------------------------------------------------------------------------------------------------------

rule-style =   
  [<'column-rule-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
  
[<column-rule-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
 =   
  <line-style-list>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <auto-line-style-list>    
  
<line-style-list> =   
  <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<auto-line-style-list> =   
  <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <auto-repeat-line-style> , <line-style-or-repeat>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<line-style-or-repeat> =   
  <line-style>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <repeat-line-style>    
  
<auto-repeat-line-style> =   
  repeat( auto , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-style> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    
  
<repeat-line-style> =   
  repeat( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer \[1,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <line-style> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#examples)

------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#basic_usage)

In this example, we define a single `<line-style>` for the lines drawn between the columns and rows of items in a grid container.

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
 property; we then set [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to `none` to remove the bullets. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `5px` to provide enough room between the columns and rows to fit our `thick dashed orange` rule.

css

    ul {
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      list-style-type: none;
      gap: 5px;
      rule-width: thick;
      rule-color: orange;
    
      rule-style: dashed;
    }
    li {
      text-align: center;
      aspect-ratio: 1;
    }
    

    @layer no-support {
      @supports not (rule-style: solid) {
        body::before {
          content: "Your browser doesn't support the rule-style property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

### [Multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#multiple_values)

This example demonstrates using multiple `<line-style>` values as a property value, and what happens when more `<line-style>` values are specified than there are gutters to style.

We set the `rule-style` property to be a comma-separated list of all the possible `<line-style>` values.

css

    ul {
      rule-style:
        dotted, dashed, solid, double, groove, ridge, inset, outset, none, hidden;
    }
    

#### Result

There are more values than gutters for both the rows and columns; the last values are not used in each case.

### [Repeating values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#repeating_values)

This example demonstrates how, when there are fewer values in the list of styles than column and row rules, the values are repeated.

#### CSS

Using the same HTML and CSS as in the previous example, we include three comma-separated styles as the `rule-style` value:

css

    ul {
      rule-style: solid, groove, double;
    }
    

#### Result

### [Using the `repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#using_the_repeat_function)

This example demonstrates using the `repeat()` function within the `rule-style` property value.

#### CSS

We use the same HTML and CSS as in the previous examples. We include a `repeat()` function that sets a list of two `<line-style>` values to be repeated 3 times.

css

    ul {
      rule-style: solid, repeat(3, inset, outset), solid;
    }
    

#### Result

The `repeat()` function repeats two style values three times, creating a list of eight style values. The styles are repeated for the columns; however, the last values in the list are discarded for the rows.

### [Using `auto` within `repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#using_auto_within_repeat)

This example demonstrates using `auto` instead of an integer within the `repeat()` function.

#### CSS

Using `repeat(auto, <line-style>)`, we set all column and row rules to `groove`, except the first and last, which we set to `solid`.

css

    ul {
      rule-style: solid, repeat(auto, groove), solid;
    }
    

#### Result

Even though there are more column rule lines than row rule lines, the `<auto-repeat-line-color>` enables the creation of this symmetric effect.

    @layer no-support {
      @supports not (rule-style: solid, groove) {
        body::before {
          content: "Your browser doesn't support multiple values for the rule-style property";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-style](https://drafts.csswg.org/css-gaps-1/#propdef-rule-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style#see_also)

------------------------------------------------------------------------------------------------------

*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
     shorthand
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5fd3b03e9ad1ee4e8bc64d4f6888570690a7fbc8%0A*+Document+last+modified%3A+2026-10-06T14%3A57%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
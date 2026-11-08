*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#mdn-search)
    

`rule-overlap` CSS property
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/362)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#browser_compatibility)
 carefully before using this in production.

The **`rule-overlap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies which rule is painted on top when column rules and row rules intersect.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#try_it)

----------------------------------------------------------------------------------------------------

    rule-overlap: row-over-column;
    

    rule-overlap: column-over-row;
    

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
    }
    #example-element i {
      padding: 5px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keywords */
    rule-overlap: row-over-column;
    rule-overlap: column-over-row;
    
    /* Global values */
    rule-overlap: inherit;
    rule-overlap: initial;
    rule-overlap: revert;
    rule-overlap: revert-layer;
    rule-overlap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#values)

This property is specified as a single keyword from the following list:

[`row-over-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#row-over-column)

Specifies that row rules are painted over column rules. This is the default value.

[`column-over-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#column-over-row)

Specifies that column rules are painted over row rules.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#formal_syntax)

------------------------------------------------------------------------------------------------------------------

rule-overlap =   
  row-over-column  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column-over-row    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#basic_usage)

In this example, we use the `rule-overlap` property to paint column rules on top of row rules.

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
    <p>
      <label
        ><input type="checkbox" /> set to
        <code>rule-overlap: row-over-column;</code></label
      >
    </p>
    

#### CSS

We define the unordered list as a 10-column grid container using the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 property. We set [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 to an empty string to remove the bullets. We include a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `20px` to provide enough room between the columns and rows to fit our `20px` solid column and row rules. Finally, we use the `rule-overlap` property to draw the column rules on top of the row rules.

css

    ul {
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      list-style-type: "";
      gap: 20px;
    
      row-rule: 20px solid palegoldenrod;
      column-rule: 20px solid olive;
    
      rule-overlap: column-over-row;
    }
    

The rest of the CSS has been hidden for brevity.

    :has(:checked) ul {
      rule-overlap: row-over-column;
    }
    li {
      text-align: center;
      aspect-ratio: 1;
      line-height: 1.5em;
    }
    @layer no-support {
      @supports not (rule-overlap: row-over-column) {
        body::before {
          content: "Your browser doesn't support the rule-overlap property.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

Select the checkbox to toggle the value of the `rule-overlap` property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# propdef-rule-overlap](https://drafts.csswg.org/css-gaps-1/#propdef-rule-overlap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap#see_also)

--------------------------------------------------------------------------------------------------------

*   [`rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   [`rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
     shorthand
*   [`rule-visibility-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/rule-overlap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/rule-overlap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-overlap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-overlap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frule-overlap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frule-overlap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0cc2d00775016fc61ae0ac1256d65ed1b56a193a%0A*+Document+last+modified%3A+2026-10-07T11%3A04%3A09.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
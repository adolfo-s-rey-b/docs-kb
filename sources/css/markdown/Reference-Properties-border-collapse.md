*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#mdn-search)
    

`border-collapse` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-collapse`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether cells inside a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 have shared or separate borders.

When cells are collapsed, the [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 value of `inset` behaves like `ridge`, and `outset` behaves like `groove`.

When cells are separated, the distance between cells is defined by the [`border-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing)
 property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#try_it)

-------------------------------------------------------------------------------------------------------

    border-collapse: collapse;
    

    border-collapse: separate;
    

    <section class="default-example" id="default-example">
      <table class="transition-all" id="example-element">
        <tbody>
          <tr>
            <td>Cell 1.1</td>
            <td>Cell 1.2</td>
          </tr>
          <tr>
            <td>Cell 2.1</td>
            <td>Cell 2.2</td>
          </tr>
          <tr>
            <td>Cell 3.1</td>
            <td>Cell 3.2</td>
          </tr>
        </tbody>
      </table>
    </section>
    

    table {
      width: 15rem;
      table-layout: fixed;
    }
    
    td {
      border: 5px solid;
      border-color: crimson dodgerblue orange limegreen;
      padding: 0.75rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    border-collapse: collapse;
    border-collapse: separate;
    
    /* Global values */
    border-collapse: inherit;
    border-collapse: initial;
    border-collapse: revert;
    border-collapse: revert-layer;
    border-collapse: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#values)

This property is specified as one of the following keyword values:

[`collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#collapse)

Adjacent cells have shared borders (the collapsed-border table rendering model).

[`separate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#separate)

Adjacent cells have distinct borders (the separated-border table rendering model).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `separate` |
| Applies to | `table` and `inline-table` elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

border-collapse =   
  separate  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  collapse    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#examples)

-----------------------------------------------------------------------------------------------------------

### [A colorful table of browser engines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#a_colorful_table_of_browser_engines)

#### HTML

html

    <table class="separate">
      <caption>
        <code>border-collapse: separate</code>
      </caption>
      <tbody>
        <tr>
          <th>Browser</th>
          <th>Layout Engine</th>
        </tr>
        <tr>
          <td class="fx">Firefox</td>
          <td class="gk">Gecko</td>
        </tr>
        <tr>
          <td class="ed">Edge</td>
          <td class="tr">EdgeHTML</td>
        </tr>
        <tr>
          <td class="sa">Safari</td>
          <td class="wk">WebKit</td>
        </tr>
        <tr>
          <td class="ch">Chrome</td>
          <td class="bk">Blink</td>
        </tr>
        <tr>
          <td class="op">Opera</td>
          <td class="bk">Blink</td>
        </tr>
      </tbody>
    </table>
    <table class="collapse">
      <caption>
        <code>border-collapse: collapse</code>
      </caption>
      <tbody>
        <tr>
          <th>Browser</th>
          <th>Layout Engine</th>
        </tr>
        <tr>
          <td class="fx">Firefox</td>
          <td class="gk">Gecko</td>
        </tr>
        <tr>
          <td class="ed">Edge</td>
          <td class="tr">EdgeHTML</td>
        </tr>
        <tr>
          <td class="sa">Safari</td>
          <td class="wk">WebKit</td>
        </tr>
        <tr>
          <td class="ch">Chrome</td>
          <td class="bk">Blink</td>
        </tr>
        <tr>
          <td class="op">Opera</td>
          <td class="bk">Blink</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    .collapse {
      border-collapse: collapse;
    }
    
    .separate {
      border-collapse: separate;
    }
    
    table {
      display: inline-table;
      margin: 1em;
      border: dashed 5px;
    }
    
    table th,
    table td {
      border: solid 3px;
    }
    
    .fx {
      border-color: orange blue;
    }
    .gk {
      border-color: black red;
    }
    .ed {
      border-color: blue gold;
    }
    .tr {
      border-color: aqua;
    }
    .sa {
      border-color: silver blue;
    }
    .wk {
      border-color: gold blue;
    }
    .ch {
      border-color: red yellow green blue;
    }
    .bk {
      border-color: navy blue teal aqua;
    }
    .op {
      border-color: red;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# propdef-border-collapse](https://drafts.csswg.org/css2/#propdef-border-collapse) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`border-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing)
    , [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   The `border-collapse` property alters the appearance of the [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
     HTML element.
*   [CSS table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-collapse/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-collapse (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-collapse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-collapse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-collapse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-collapse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#mdn-search)
    

`empty-cells` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`empty-cells`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether borders and backgrounds appear around [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 cells that have no visible content.

This property has an effect only when the [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 property is `separate`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#try_it)

---------------------------------------------------------------------------------------------------

    empty-cells: show;
    

    empty-cells: hide;
    

    <section class="default-example" id="default-example">
      <table class="transition-all" id="example-element">
        <tbody>
          <tr>
            <th>Client Name</th>
            <th>Age</th>
          </tr>
          <tr>
            <td></td>
            <td>25</td>
          </tr>
          <tr>
            <td>Louise Q.</td>
            <td></td>
          </tr>
          <tr>
            <td>Owen B.</td>
            <td></td>
          </tr>
          <tr>
            <td>Stan L.</td>
            <td>71</td>
          </tr>
        </tbody>
      </table>
    </section>
    

    th,
    td {
      border: 2px solid #aa1199;
      padding: 0.25rem 0.5rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    empty-cells: show;
    empty-cells: hide;
    
    /* Global values */
    empty-cells: inherit;
    empty-cells: initial;
    empty-cells: revert;
    empty-cells: revert-layer;
    empty-cells: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#values)

This property is specified as one of the following keyword values:

[`show`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#show)

Borders and backgrounds are drawn like in normal cells.

[`hide`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#hide)

No borders or backgrounds are drawn.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `show` |
| Applies to | table-cell elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

empty-cells =   
  show  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hide    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#examples)

-------------------------------------------------------------------------------------------------------

### [Showing and hiding empty table cells](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#showing_and_hiding_empty_table_cells)

#### HTML

html

    <table class="table_1">
      <tbody>
        <tr>
          <td>Moe</td>
          <td>Larry</td>
        </tr>
        <tr>
          <td>Curly</td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <br />
    <table class="table_2">
      <tbody>
        <tr>
          <td>Moe</td>
          <td>Larry</td>
        </tr>
        <tr>
          <td>Curly</td>
          <td></td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    .table_1 {
      empty-cells: show;
    }
    
    .table_2 {
      empty-cells: hide;
    }
    
    td,
    th {
      border: 1px solid gray;
      padding: 0.5rem;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# empty-cells](https://drafts.csswg.org/css2/#empty-cells) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells#see_also)

-------------------------------------------------------------------------------------------------------

*   [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
    
*   [Learn: Styling tables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Tables)
    
*   [CSS table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/empty-cells/index.md?plain=1 "Folder: en-us/web/css/reference/properties/empty-cells (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fempty-cells&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fempty-cells%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fempty-cells%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fempty-cells%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
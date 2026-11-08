*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#mdn-search)
    

`table-layout` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`table-layout`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the algorithm used to lay out [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 cells, rows, and columns.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#try_it)

----------------------------------------------------------------------------------------------------

    table-layout: auto;
    width: 150px;
    

    table-layout: fixed;
    width: 150px;
    

    table-layout: auto;
    width: 100%;
    

    table-layout: fixed;
    width: 100%;
    

    <section class="default-example" id="default-example">
      <table class="transition-all" id="example-element">
        <tbody>
          <tr>
            <th>Name</th>
            <th>Location</th>
          </tr>
          <tr>
            <td>Lion</td>
            <td>Africa</td>
          </tr>
          <tr>
            <td>Norwegian Lemming</td>
            <td>Europe</td>
          </tr>
          <tr>
            <td>Seal</td>
            <td>Antarctica</td>
          </tr>
          <tr>
            <td>Tiger</td>
            <td>Asia</td>
          </tr>
        </tbody>
      </table>
    </section>
    

    table {
      border: 1px solid #113399;
    }
    
    th,
    td {
      border: 2px solid #aa1199;
      padding: 0.25rem 0.5rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    table-layout: auto;
    table-layout: fixed;
    
    /* Global values */
    table-layout: inherit;
    table-layout: initial;
    table-layout: revert;
    table-layout: revert-layer;
    table-layout: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#auto)

The automatic table layout algorithm is used. The widths of the table and its cells are adjusted to fit the content. Most browsers use this algorithm by default.

[`fixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#fixed)

The fixed table layout algorithm is used. When using this keyword, the table's width _needs to be specified explicitly_ using the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 property. If the value of the `width` property is set to `auto` or is not specified, the browser uses the automatic table layout algorithm, in which case the `fixed` value has no effect.  
The fixed table layout algorithm is faster than the automatic layout algorithm because the horizontal layout of the table depends only on the table's width, the width of the columns, and borders or cell spacing. The horizontal layout doesn't depend on the contents of the cells because it depends only on explicitly set widths.

In the fixed table layout algorithm, the width of each column is determined as follows:

*   A column element with explicit width sets the width for that column.
*   Otherwise, a cell in the first row with explicit width determines the width for that column.
*   Otherwise, the column gets the width from the shared remaining horizontal space.

With this algorithm the entire table can be rendered once the first table row has been downloaded and analyzed. This can speed up rendering time over the "automatic" layout method, but subsequent cell content might not fit in the column widths provided. Cells use the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property to determine whether to clip any overflowing content, but only if the table has a known width; otherwise, they won't overflow the cells.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | `table` and `inline-table` elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#formal_syntax)

------------------------------------------------------------------------------------------------------------------

table-layout =   
  auto   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#examples)

--------------------------------------------------------------------------------------------------------

### [Fixed-width tables with text-overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#fixed-width_tables_with_text-overflow)

This example uses a fixed table layout, combined with the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 property, to restrict the table's width. The [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
 property is used to apply an ellipsis to words that are too long to fit. If the table layout were `auto`, the table would grow to accommodate its contents, despite the specified `width`.

#### HTML

html

    <table>
      <tbody>
        <tr>
          <td>Ed</td>
          <td>Wood</td>
        </tr>
        <tr>
          <td>Albert</td>
          <td>Schweitzer</td>
        </tr>
        <tr>
          <td>Jane</td>
          <td>Fonda</td>
        </tr>
        <tr>
          <td>William</td>
          <td>Shakespeare</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    table {
      table-layout: fixed;
      width: 120px;
      border: 1px solid red;
    }
    
    td {
      border: 1px solid blue;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# width-layout](https://drafts.csswg.org/css2/#width-layout) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout#see_also)

--------------------------------------------------------------------------------------------------------

*   [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    
*   [CSS table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/table-layout/index.md?plain=1 "Folder: en-us/web/css/reference/properties/table-layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftable-layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftable-layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftable-layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftable-layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
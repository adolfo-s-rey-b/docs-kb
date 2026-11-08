*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#mdn-search)
    

`<tr>` HTML table row element
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<tr>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 (header cell) elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#try_it)

-----------------------------------------------------------------------------------------

    <table>
      <caption>
        Alien football stars
      </caption>
      <thead>
        <tr>
          <th scope="col">Player</th>
          <th scope="col">Gloobles</th>
          <th scope="col">Za'taak</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">TR-7</th>
          <td>7</td>
          <td>4,569</td>
        </tr>
        <tr>
          <th scope="row">Khiresh Odo</th>
          <td>7</td>
          <td>7,223</td>
        </tr>
        <tr>
          <th scope="row">Mia Oolong</th>
          <td>9</td>
          <td>6,219</td>
        </tr>
      </tbody>
    </table>
    

    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 10px;
    }
    
    th[scope="col"] {
      background-color: #505050;
      color: white;
    }
    
    th[scope="row"] {
      background-color: #d6ecd4;
    }
    
    td {
      text-align: center;
    }
    
    tr:nth-of-type(even) {
      background-color: #eeeeee;
    }
    
    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    caption {
      caption-side: bottom;
      padding: 10px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#attributes)

-------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#align)

Specifies the horizontal alignment of each row cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `center`, `right`, `justify`, and `char`. When supported, the `char` value aligns the textual content on the character defined in the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#char)
 attribute and on offset defined by the [`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#charoff)
 attribute. Use the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS property instead, as this attribute is deprecated.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#bgcolor)

Defines the background color of each row cell. The value is an HTML color; either a [6-digit hexadecimal RGB code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
, prefixed by a `#`, or a [color keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. Other CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values are not supported. Use the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 CSS property instead, as this attribute is deprecated.

[`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#char)

Specifies the alignment of the content to a character of each row cell. Typical values for this include a period (`.`) when attempting to align numbers or monetary values. If [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#align)
 is not set to `char`, this attribute is ignored.

[`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#charoff)

Specifies the number of characters to offset the row cell content from the alignment character specified by the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#char)
 attribute.

[`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#valign)

Specifies the vertical alignment of each row cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `baseline`, `bottom`, `middle`, and `top`. Use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 CSS property instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#usage_notes)

---------------------------------------------------------------------------------------------------

*   The `<tr>` element is valid as a child of a [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , or [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
     element only.
*   If the `<tr>` is placed as a direct child of its parent [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
     element, the `<tbody>` parent is implied and browsers will add the `<tbody>` to the markup.
*   The implied `<tbody>` parent is only supported if the `<table>` otherwise has no child `<tbody>` elements, and only if the `<tr>` is included after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , and `<thead>` elements.
*   The CSS pseudo-classes [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    , [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    , and [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
     are often useful for selecting the desired set of rows and their data and header cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
     and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
     elements).
*   When a `<tr>` is included as a direct child of the `<table>`, as the browser adds a `<tbody>` to the markup, CSS selectors such as `table > tr` may not work as expected or at all.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#examples)

---------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

### [Basic row setup](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#basic_row_setup)

This example demonstrates a table with four rows and three columns, where the first column contains headers for the row data cells.

#### HTML

Four `<tr>` elements are used to create four table rows. Each row contains three cells - one header cell ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
) and two data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
) - creating three columns. The [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute set on each header cell specifies which cells they relate to, which in this example is all data cells within the `row`.

html

    <table>
      <tbody>
        <tr>
          <th scope="row">A</th>
          <td>Alfa</td>
          <td>AL fah</td>
        </tr>
        <tr>
          <th scope="row">B</th>
          <td>Bravo</td>
          <td>BRAH voh</td>
        </tr>
        <tr>
          <th scope="row">C</th>
          <td>Charlie</td>
          <td>CHAR lee</td>
        </tr>
        <tr>
          <th scope="row">D</th>
          <td>Delta</td>
          <td>DELL tah</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

The CSS [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
 pseudo-class is used to select every `odd` row and set the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 of those rows to a slightly darker tone, creating a so-called "zebra stripe" effect. This alternating background makes the rows of data in the table easier to parse and read—imagine having many rows and columns and trying to find some data in a particular row. In addition, the row header cells ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements) are highlighted with a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 to distinguish them from the data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements).

css

    tr:nth-of-type(odd) {
      background-color: #eeeeee;
    }
    
    tr th[scope="row"] {
      background-color: #d6ecd4;
    }
    

    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 10px;
    }
    

#### Result

### [Header row](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#header_row)

This example extends the basic table from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#basic_row_setup)
 by adding a header row as the first row of the table.

#### HTML

An additional table row (`<tr>`) is added as the first row of the table with column header cells ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
) providing a header for each column. We put this row in a [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
 grouping element to indicate this is the header of the table. The [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute is added to each header cell (`<th>`) within this head row to explicitly specify that each header cell relates to all the cells within its own column, even though those cells are in the [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
.

html

    <table>
      <thead>
        <tr>
          <th scope="col">Symbol</th>
          <th scope="col">Code word</th>
          <th scope="col">Pronunciation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">A</th>
          <td>Alfa</td>
          <td>AL fah</td>
        </tr>
        <tr>
          <th scope="row">B</th>
          <td>Bravo</td>
          <td>BRAH voh</td>
        </tr>
        <tr>
          <th scope="row">C</th>
          <td>Charlie</td>
          <td>CHAR lee</td>
        </tr>
        <tr>
          <th scope="row">D</th>
          <td>Delta</td>
          <td>DELL tah</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

The CSS is nearly unchanged from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#basic_row_setup)
, except for some additional styling to highlight the "header row" so that the headers of the columns stand out from the other cells.

css

    tr:nth-of-type(odd) {
      background-color: #eeeeee;
    }
    
    tr th[scope="col"] {
      background-color: #505050;
      color: white;
    }
    
    tr th[scope="row"] {
      background-color: #d6ecd4;
    }
    

    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 10px;
    }
    

#### Result

### [Sorting rows](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#sorting_rows)

There are no native methods for sorting the rows (`<tr>` elements) of a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
. But using [`Array.prototype.sort()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
, [`Node.removeChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild)
, and [`Node.appendChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
, a custom `sort()` function can be implemented in JavaScript to sort an [`HTMLCollection`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection)
 of `<tr>` elements.

#### HTML

A [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 element is used in this basic table to mark the body section of the table and to include three rows (`<tr>` elements) with data ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements), creating one column with numbers in descending order.

html

    <table>
      <tbody>
        <tr>
          <td>3</td>
        </tr>
        <tr>
          <td>2</td>
        </tr>
        <tr>
          <td>1</td>
        </tr>
      </tbody>
    </table>
    

#### JavaScript

In the JavaScript code below, the created `sort()` function is attached to the [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 element so that it sorts the table cells in order of increasing value and updates the display accordingly.

js

    HTMLTableSectionElement.prototype.sort = function (cb) {
      Array.from(this.rows)
        .sort(cb)
        .forEach((e) => this.appendChild(this.removeChild(e)));
    };
    
    document
      .querySelector("table")
      .tBodies[0].sort((a, b) => a.textContent.localeCompare(b.textContent));
    

    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    td {
      border: 1px solid rgb(160 160 160);
      padding: 4px 8px;
    }
    

#### Result

### [Sorting rows with a click on header cells](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#sorting_rows_with_a_click_on_header_cells)

This example extends the basic table from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#sorting_rows)
 by making the sorting interactive and independent for multiple columns.

#### HTML

An additional data cell ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 element) is added to each row (`<tr>` element) within the table body ([`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 element) to create a second column with letters in ascending order. Using the [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
 element, a head section is added before the body section to introduce a head row with table header cells ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 element). These header cells are used in the JavaScript code below to make them clickable and then to perform the corresponding sorting when activated per click.

html

    <table>
      <thead>
        <tr>
          <th>Numbers</th>
          <th>Letters</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>3</td>
          <td>A</td>
        </tr>
        <tr>
          <td>2</td>
          <td>B</td>
        </tr>
        <tr>
          <td>1</td>
          <td>C</td>
        </tr>
      </tbody>
    </table>
    

#### JavaScript

A click event handler is added to each table header ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 element) of each [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 in the [`document`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDocument "document")
; it sorts all the rows (`<tr>` elements) of the [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 based on the contents of the data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements) contained in the rows.

**Note:** This solution assumes that the [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements are populated by raw text with no descendant elements.

js

    const allTables = document.querySelectorAll("table");
    
    for (const table of allTables) {
      const tBody = table.tBodies[0];
      const rows = Array.from(tBody.rows);
      const headerCells = table.tHead.rows[0].cells;
    
      for (const th of headerCells) {
        const cellIndex = th.cellIndex;
    
        th.addEventListener("click", () => {
          rows.sort((tr1, tr2) => {
            const tr1Text = tr1.cells[cellIndex].textContent;
            const tr2Text = tr2.cells[cellIndex].textContent;
            return tr1Text.localeCompare(tr2Text);
          });
    
          tBody.append(...rows);
        });
      }
    }
    

    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 4px 8px;
    }
    
    th {
      background-color: #505050;
      color: white;
      cursor: pointer;
    }
    

#### Result

**Note:** To be usable and accessible, the header cell of each sortable column must be identifiable as a sorting button and each must define whether the column is currently sorted in ascending or descending order visually and with the [`aria-sort`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-sort)
 attribute. See the [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/ "External link (opens in new tab)")
's [sortable table example](https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/ "External link (opens in new tab)")
 for more information.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None |
| Permitted content | Zero or more [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)<br> and/or [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)<br> elements; [script-supporting elements](https://developer.mozilla.org/en-US/docs/Glossary/Script-supporting_element)<br> ([`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br>) are also allowed. |
| Tag omission | Start tag is mandatory. End tag may be omitted if the `<tr>` element is immediately followed by a `<tr>` element, or if the row is the last element in its parent table group ([`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)<br>, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br> or [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)<br>) element. |
| Permitted parents | [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> (only if the table has no child [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br> element, and even then only after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)<br>, [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br>, and [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)<br> elements); otherwise, the parent must be a [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)<br>, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br> or [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)<br> element. |
| Implicit ARIA role | `[row](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/row_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLTableRowElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableRowElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-tr-element](https://html.spec.whatwg.org/multipage/tables.html#the-tr-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr#see_also)

---------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    : Other table-related elements
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    : CSS property to set the background color of each row cell
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    : CSS property to control borders of row cells
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align each row cell content
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    : CSS property to vertically align each row cell content
*   [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    , [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    , [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    : CSS pseudo-classes to select the desired row cells

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/tr/index.md?plain=1 "Folder: en-us/web/html/reference/elements/tr (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
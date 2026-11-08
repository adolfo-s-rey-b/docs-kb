*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#mdn-search)
    

`<thead>` HTML table head element
=================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<thead>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#try_it)

--------------------------------------------------------------------------------------------

    <table>
      <caption>
        Council budget (in £) 2018
      </caption>
      <thead>
        <tr>
          <th scope="col">Items</th>
          <th scope="col">Expenditure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Donuts</th>
          <td>3,000</td>
        </tr>
        <tr>
          <th scope="row">Stationery</th>
          <td>18,000</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th scope="row">Totals</th>
          <td>21,000</td>
        </tr>
      </tfoot>
    </table>
    

    thead,
    tfoot {
      background-color: #2c5e77;
      color: white;
    }
    
    tbody {
      background-color: #e4f0f5;
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
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 10px;
    }
    
    td {
      text-align: center;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#align)

Specifies the horizontal alignment of each head cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `center`, `right`, `justify`, and `char`. When supported, the `char` value aligns the textual content on the character defined in the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#char)
 attribute and the offset defined by the [`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#charoff)
 attribute. Use the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS property instead, as this attribute is deprecated.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#bgcolor)

Defines the background color of each head cell. The value is an HTML color; either a [6-digit hexadecimal RGB code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
, prefixed by a `#`, or a [color keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. Other CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values are not supported. Use the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 CSS property instead, as this attribute is deprecated.

[`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#char)

Does nothing. It was originally intended to specify the alignment of the content to a character of each head cell. If [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#align)
 is not set to `char`, this attribute is ignored.

[`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#charoff)

Does nothing. It was originally intended to specify the number of characters to offset the head cell content from the alignment character specified by the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#char)
 attribute.

[`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#valign)

Specifies the vertical alignment of each head cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `baseline`, `bottom`, `middle`, and `top`. Use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 CSS property instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#usage_notes)

------------------------------------------------------------------------------------------------------

*   The `<thead>` is placed after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
     and [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
     elements, but before any [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
     elements.
*   Along with its related [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
     and [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
     elements, the `<thead>` element provides useful [semantic](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
     information and can be used when rendering for either screen or print. Specifying such table content groups also provides valuable contextual information for assistive technologies, including screen readers and search engines.
*   When printing a document, in the case of a multipage table, the table head usually specifies information that remains the same on each page.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#examples)

------------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

### [Basic head structure](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#basic_head_structure)

This example demonstrates a table divided into a head section with column headers and a body section with the table's main data.

#### HTML

The `<thead>` and [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 elements are used to structure the table rows into [semantic](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
 sections. The `<thead>` element represents the head section of the table, which contains a row ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
) of column headers cells ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
).

html

    <table>
      <thead>
        <tr>
          <th>Student ID</th>
          <th>Name</th>
          <th>Major</th>
          <th>Credits</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>3741255</td>
          <td>Jones, Martha</td>
          <td>Computer Science</td>
          <td>240</td>
        </tr>
        <tr>
          <td>3971244</td>
          <td>Nim, Victor</td>
          <td>Russian Literature</td>
          <td>220</td>
        </tr>
        <tr>
          <td>4100332</td>
          <td>Petrov, Alexandra</td>
          <td>Astrophysics</td>
          <td>260</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

Some basic CSS is used to style and highlight the table head so that the headings of the columns stand out from the data in the table body.

css

    thead {
      border-bottom: 2px solid rgb(160 160 160);
      text-align: center;
      background-color: #2c5e77;
      color: white;
    }
    
    tbody {
      background-color: #e4f0f5;
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
    
    tbody > tr > td:last-of-type {
      text-align: center;
    }
    

#### Result

### [Multiple head rows](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#multiple_head_rows)

This example demonstrates a table head section with two rows.

#### HTML

We extend the markup the table from the [basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#basic_head_structure)
 in this example by including two table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
) within the `<thead>` element creating a multi-row table head. We included an additional column, splitting the student names into first and last names.

html

    <table>
      <thead>
        <tr>
          <th rowspan="2">Student ID</th>
          <th colspan="2">Student</th>
          <th rowspan="2">Major</th>
          <th rowspan="2">Credits</th>
        </tr>
        <tr>
          <th>First name</th>
          <th>Last name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>3741255</td>
          <td>Martha</td>
          <td>Jones</td>
          <td>Computer Science</td>
          <td>240</td>
        </tr>
        <tr>
          <td>3971244</td>
          <td>Victor</td>
          <td>Nim</td>
          <td>Russian Literature</td>
          <td>220</td>
        </tr>
        <tr>
          <td>4100332</td>
          <td>Alexandra</td>
          <td>Petrov</td>
          <td>Astrophysics</td>
          <td>260</td>
        </tr>
      </tbody>
    </table>
    

#### Cell spanning

In order to associate and line up the header cells with the correct columns and rows, the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
 and [`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)
 attributes are used on the [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements. The values set in these attributes specify how many cells each header cell ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
) spans. Due to the way these attributes are set, the two second-row header cells are lined up with the columns they head. These each span one row and one column as the default values for the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
 and [`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)
 attributes are both `1`.

The column and row spanning demonstrated by this example are illustrated in the following figure:

![Illustration demonstrating column and row spanning of table cells: cells 1, 3, and 4 spanning one column and two rows each; cell 2 spanning two columns and one row; cells 5 and 6 span a single row and column each, fitting into the available cells that are the second and third columns in the second row](https://developer.mozilla.org/shared-assets/images/diagrams/html/table/column-row-span.png)

#### CSS

The CSS is unchanged from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#basic_head_structure)
.

    thead {
      border-bottom: 2px solid rgb(160 160 160);
      background-color: #2c5e77;
      color: white;
    }
    
    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    
    tbody {
      background-color: #e4f0f5;
    }
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 10px;
    }
    
    tbody > tr > td:last-of-type {
      text-align: center;
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | Zero or more [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. |
| Tag omission | The start tag is mandatory. The end tag may be omitted if the `<thead>` element is immediately followed by a [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br> or [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)<br> element. |
| Permitted parents | A [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> element. The `<thead>` must appear after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)<br> and [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br> elements, even implicitly defined, but before any [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br>, [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)<br>, and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. |
| Implicit ARIA role | `[rowgroup](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/rowgroup_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLTableSectionElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableSectionElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-thead-element](https://html.spec.whatwg.org/multipage/tables.html#the-thead-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead#see_also)

------------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    , [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    : Other table-related elements
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    : CSS property to set the background color of each head cell
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    : CSS property to control borders of head cells
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align each head cell content
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    : CSS property to vertically align each head cell content

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/thead/index.md?plain=1 "Folder: en-us/web/html/reference/elements/thead (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fthead&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fthead%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fthead%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fthead%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44a5fa2aace490e0114349d9d683675b2f5cacce%0A*+Document+last+modified%3A+2026-05-09T06%3A32%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
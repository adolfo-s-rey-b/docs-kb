*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#mdn-search)
    

`<tfoot>` HTML table foot element
=================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<tfoot>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#try_it)

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
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#align)

Specifies the horizontal alignment of each foot cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `center`, `right`, `justify`, and `char`. When supported, the `char` value aligns the textual content on the character defined in the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#char)
 attribute and on offset defined by the [`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#charoff)
 attribute. Use the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS property instead, as this attribute is deprecated.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#bgcolor)

Defines the background color of each foot cell. The value is an HTML color; either a [6-digit hexadecimal RGB code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
, prefixed by a `#`, or a [color keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. Other CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values are not supported. Use the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 CSS property instead, as this attribute is deprecated.

[`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#char)

Does nothing. It was originally intended to specify the alignment of the content to a character of each foot cell. Typical values for this include a period (`.`) when attempting to align numbers or monetary values. If [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#align)
 is not set to `char`, this attribute is ignored.

[`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#charoff)

Does nothing. It was originally intended to specify the number of characters to offset the foot cell content from the alignment character specified by the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#char)
 attribute.

[`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#valign)

Specifies the vertical alignment of each foot cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `baseline`, `bottom`, `middle`, and `top`. Use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 CSS property instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#usage_notes)

------------------------------------------------------------------------------------------------------

*   The `<tfoot>` is placed after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
     elements.
*   Along with its related [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
     and [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
     elements, the `<tfoot>` element provides useful [semantic](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
     information and can be used when rendering for either screen or print. Specifying such table content groups also provides valuable contextual information for assistive technologies, including screen readers and search engines.
*   When printing a document, in the case of a multipage table, the table foot usually specifies information that is output as an intermediate summary on each page.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#example)

----------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

### [Table with footer](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#table_with_footer)

This example demonstrates a table divided into a head section with column headers, a body section with the table's main data, and a foot section summarizing data of one column.

#### HTML

The [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
, and `<tfoot>` elements are used to structure a basic table into [semantic](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
 sections. The `<tfoot>` element represents the foot section of the table, which contains a row ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
) representing the calculated average of the values in the "Credits" column.

To allocate the cells in the foot to the correct columns, the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
 attribute is used on the [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 element to span row header cell across the first three table columns. The single data cell ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
) in the foot is automatically placed in the correct location, i.e., the fourth column, with the omitted [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td#colspan)
 attribute value defaulting to `1`. Additionally, the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute is set to `row` on the header cell ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
) in the foot to explicitly define that this foot header cell relates to the table cells within the same row, which in our example is the one data cell in the foot row that contains the calculated average.

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
      <tfoot>
        <tr>
          <th colspan="3" scope="row">Average Credits</th>
          <td>240</td>
        </tr>
      </tfoot>
    </table>
    

#### CSS

Some basic CSS is used to style and highlight the table foot so that the foot cells stand out from the data in the table body.

css

    tfoot {
      border-top: 3px dotted rgb(160 160 160);
      background-color: #2c5e77;
      color: white;
    }
    
    tfoot th {
      text-align: right;
    }
    
    tfoot td {
      font-weight: bold;
    }
    
    thead {
      border-bottom: 2px solid rgb(160 160 160);
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
    
    tr > td:last-of-type {
      text-align: center;
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | Zero or more [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. |
| Tag omission | The start tag is mandatory. The end tag may be omitted if there is no more content in the parent [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> element. |
| Permitted parents | A [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> element. The `<tfoot>` must appear after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)<br>, [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br>, [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)<br>, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br>, and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. Note that this is the requirement in HTML.  <br>Originally, in HTML4, the opposite was true: the `<tfoot>` element could not be placed after any [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br> and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. |
| Implicit ARIA role | `[rowgroup](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/rowgroup_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLTableSectionElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableSectionElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-tfoot-element](https://html.spec.whatwg.org/multipage/tables.html#the-tfoot-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot#see_also)

------------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    : Other table-related elements
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    : CSS property to set the background color of each foot cell
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    : CSS property to control borders of foot cells
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align each foot cell content
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    : CSS property to vertically align each foot cell content

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/tfoot/index.md?plain=1 "Folder: en-us/web/html/reference/elements/tfoot (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftfoot&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftfoot%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftfoot%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftfoot%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44a5fa2aace490e0114349d9d683675b2f5cacce%0A*+Document+last+modified%3A+2026-05-09T06%3A32%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
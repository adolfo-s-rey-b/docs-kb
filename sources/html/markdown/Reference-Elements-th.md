*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#mdn-search)
    

`<th>` HTML table header element
================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<th>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines a cell as the header of a group of table cells and may be used as a child of the [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 element. The exact nature of this group is defined by the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 and [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)
 attributes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#try_it)

-----------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#attributes)

-------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`abbr`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#abbr)

A short, abbreviated description of the header cell's content provided as an alternative label to use for the header cell when referencing the cell in other contexts. Some user-agents, such as screen readers, may present this description before the content itself.

[`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)

A non-negative integer value indicating how many columns the header cell spans or extends. The default value is `1`. Values higher than `1000` are clipped to `1000`.

[`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)

A list of space-separated strings corresponding to the `id` attributes of the `<th>` elements that provide the headers for this header cell.

[`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)

A non-negative integer value indicating how many rows the header cell spans or extends. The default value is `1`; if its value is set to `0`, the header cell will extend to the end of the table grouping section ([`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
, [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
, even if implicitly defined), that the `<th>` belongs to. Values higher than `65534` are clipped at `65534`.

[`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)

Defines the cells that the header (defined in the `<th>`) element relates to. Possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are:

*   `row`: the header relates to all cells of the row it belongs to;
*   `col`: the header relates to all cells of the column it belongs to;
*   `rowgroup`: the header belongs to a rowgroup and relates to all of its cells;
*   `colgroup`: the header belongs to a colgroup and relates to all of its cells.

If the `scope` attribute is not specified, or its value is not `row`, `col`, `rowgroup`, or `colgroup`, then browsers automatically select the set of cells to which the header cell applies.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#align)

Specifies the horizontal alignment of the header cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `center`, `right`, `justify`, and `char`. When supported, the `char` value aligns the textual content on the character defined in the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#char)
 attribute and the offset defined by the [`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#charoff)
 attribute. Use the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS property instead, as this attribute is deprecated.

[`axis`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#axis)

Contains a list of space-separated strings, each corresponding to the `id` attribute of a group of cells that the header cell applies to. Use the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute instead, as this attribute is deprecated.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#bgcolor)

Defines the background color of the header cell. The value is an HTML color; either a [6-digit hexadecimal RGB code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
, prefixed by a `#`, or a [color keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. Other CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values are not supported. Use the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 CSS property instead, as this attribute is deprecated.

[`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#char)

Does nothing. It was originally intended to specify the alignment of the content to a character of the header cell. Typical values for this include a period (`.`) when attempting to align numbers or monetary values. If [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#align)
 is not set to `char`, this attribute is ignored.

[`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#charoff)

Does nothing. It was originally intended to specify the number of characters to offset the header cell content from the alignment character specified by the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#char)
 attribute.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#height)

Defines a recommended header cell height. Use the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 CSS property instead, as this attribute is deprecated.

[`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#valign)

Specifies the vertical alignment of the header cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `baseline`, `bottom`, `middle`, and `top`. Use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 CSS property instead, as this attribute is deprecated.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#width)

Defines a recommended header cell width. Use the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 CSS property instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#usage_notes)

---------------------------------------------------------------------------------------------------

*   The `<th>` may only be used within a [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
     element.
    
*   In simple contexts, using the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
     attribute on header cells (`<th>` elements) is redundant because [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
     is inferred. However, certain assistive technologies may fail to infer correctly, so specifying header scope may improve user experiences.
    
*   When using the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
     and [`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)
     attributes to span header cells across multiple columns and rows, cells without these attributes defined (with a default value of `1`) are automatically fitted into free available spaces in the table structure that span 1x1 cells, as illustrated in the following figure:
    
    ![Illustration demonstrating column and row spanning of table cells: cells 1, 3, and 4 spanning two rows; cell 2 spanning two columns; cells 5 and 6 fitting into the available cells that are the second and third columns in the second row](https://developer.mozilla.org/shared-assets/images/diagrams/html/table/column-row-span.png)
    
    **Note:** These attributes must not be used to overlap cells.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#examples)

---------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

### [Basic column and row headers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#basic_column_and_row_headers)

This example uses `<th>` elements to introduce column and row headers in a basic table structure.

#### HTML

The first row ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 element) contains the column headers (`<th>` elements), which act as "titles" for the columns to make it easier to understand the information in the columns and identify the data. To indicate that each column header relates to all cells in the corresponding column, the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute is set to `col` (column).

The remaining rows contain the main data of the table. Each of these rows has a row header (`<th>` element) introduced as the first cell. This creates a column with row headers as the first column of the table. Similar to the column headers, the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute is set to `row` to specify which cells each row header relates to, which in the example below are all data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements) in each `row`.

**Note:** Normally, the grouping elements [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
 and [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 are used to group rows with headers into the respective table head and body sections. These elements are omitted in this example to reduce complexity and enable focusing on the use of header cells.

#### CSS

Some basic CSS is used to style the table and its cells. We use CSS [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
 to target header cells based on their [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute values, highlighting column and row headers (`<th>` elements) and differentiating them each other and from the data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
).

#### Result

### [Column and row spanning](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#column_and_row_spanning)

This example extends and enhances the basic table from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#basic_column_and_row_headers)
 by adding a second row for additional column headers.

#### HTML

An additional table row ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 element) is added as the second header row of the table with two additional column headers (`<th>` elements). In this way, the "Pronunciation" column is split into two columns, one for the IPA (International Phonetic Alphabet) notation and one for the respelling (the original pronunciation column). The corresponding data cells ([`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements) are added to each subsequent row.

As shown in the [usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#usage_notes)
, the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
 and [`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)
 attributes can be used for the `<th>` elements to allocate the header cells to the correct columns and rows. To achieve a "two-row" header in the table structure, the first two header cells within the first [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 element are spanned across two rows. The third header cell is spanned two columns wide (remaining in the first row). This setup leaves two available areas in the third and fourth columns in the second row, where the two headers within the second [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 element are automatically placed, with the default value being `1` for the [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#colspan)
 and [`rowspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#rowspan)
 attributes.

**Note:** Normally, [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
 and [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 elements are used to group rows with headers into the respective table head and body sections. This is not implemented in this example to focus on the headers and spanning and reduce the example's complexity.

html

    <table>
      <tr>
        <th scope="col" rowspan="2">Symbol</th>
        <th scope="col" rowspan="2">Code word</th>
        <th scope="col" colspan="2">Pronunciation</th>
      </tr>
      <tr>
        <th scope="col">IPA</th>
        <th scope="col">Respelling</th>
      </tr>
      <tr>
        <th scope="row">A</th>
        <td>Alfa</td>
        <td>ˈælfa</td>
        <td>AL fah</td>
      </tr>
      <tr>
        <th scope="row">B</th>
        <td>Bravo</td>
        <td>ˈbraːˈvo</td>
        <td>BRAH voh</td>
      </tr>
      <tr>
        <th scope="row">C</th>
        <td>Charlie</td>
        <td>ˈtʃɑːli</td>
        <td>CHAR lee</td>
      </tr>
      <tr>
        <th scope="row">D</th>
        <td>Delta</td>
        <td>ˈdeltɑ</td>
        <td>DELL tah</td>
      </tr>
    </table>
    

#### CSS

The CSS is unchanged from the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#basic_column_and_row_headers)
.

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
    
    th[scope="col"] {
      background-color: #505050;
      color: white;
    }
    
    th[scope="row"] {
      background-color: #d6ecd4;
    }
    
    tr:nth-of-type(odd) td {
      background-color: #eeeeee;
    }
    

#### Result

### [Associate header cells with other header cells](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#associate_header_cells_with_other_header_cells)

For more complex relationships between header cells, using `th` elements with the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)
 attribute alone may not be sufficient for assistive technologies, especially screen readers.

#### HTML

To improve the [accessibility](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility)
 of the [previous example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#column_and_row_spanning)
 and to allow screen readers, for example, to speak the headers associated with each header cell, the [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)
 attribute can be introduced along with [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attributes. Because of the way the "Pronunciation" column is split into two columns in the example, introducing a "two row" header, assistive technologies such as screen readers may not be able to identify which additional header cells (`th` elements) the "Pronunciation" header cell is related to and vice versa. Therefore, the [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)
 attribute is used on the "Pronunciation", "IPA", and "Respelling" header cells to associate the related header cells based on the values of the unique identifiers from the added [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attributes in the form of a space-separated list.

**Note:** It's recommended to use more descriptive and useful values for the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute. Each `id` in a document must be unique to that document. In this example, the `id` values are single characters to maintain focus on the concept of the [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)
 attribute.

#### Result

The [visual result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#result_2)
 is unchanged from the [previous example table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#column_and_row_spanning)
.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but with no header, footer, sectioning content, or heading content descendants. |
| Tag omission | The start tag is mandatory.  <br>The end tag may be omitted, if it is immediately followed by a `<th>` or [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)<br> element or if there are no more data in its parent element. |
| Permitted parents | A [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> element. |
| Implicit ARIA role | [`columnheader`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/columnheader_role)<br> or [`rowheader`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/rowheader_role) |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLTableCellElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableCellElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-th-element](https://html.spec.whatwg.org/multipage/tables.html#the-th-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#see_also)

---------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    : Other table-related elements
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    : CSS property to set the background color of each header cell
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    : CSS property to control borders of header cells
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    : CSS property to control the recommended header cell height
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align each header cell content
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    : CSS property to vertically align each header cell content
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    : CSS property to control the recommended header cell width
*   [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    , [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    , [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    : CSS pseudo-classes to select the desired header cells

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/th/index.md?plain=1 "Folder: en-us/web/html/reference/elements/th (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3871111d7fb958626f9d926d8809222d318b8c72%0A*+Document+last+modified%3A+2026-07-14T15%3A32%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#mdn-search)
    

`<colgroup>` HTML table column group element
============================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<colgroup>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element defines a group of columns within a table.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#try_it)

-----------------------------------------------------------------------------------------------

    <table>
      <caption>
        Superheros and sidekicks
      </caption>
      <colgroup>
        <col />
        <col span="2" class="batman" />
        <col span="2" class="flash" />
      </colgroup>
      <thead>
        <tr>
          <td></td>
          <th scope="col">Batman</th>
          <th scope="col">Robin</th>
          <th scope="col">The Flash</th>
          <th scope="col">Kid Flash</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Skill</th>
          <td>Smarts, strong</td>
          <td>Dex, acrobat</td>
          <td>Super speed</td>
          <td>Super speed</td>
        </tr>
      </tbody>
    </table>
    

    .batman {
      background-color: #d7d9f2;
    }
    
    .flash {
      background-color: #ffe8d4;
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
      padding: 8px 6px;
    }
    
    td {
      text-align: center;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#span)

Specifies the number of consecutive columns the `<colgroup>` element spans. The value must be a positive integer greater than zero. If not present, its default value is `1`.

**Note:** The `span` attribute is not permitted if there are one or more [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 elements within the `<colgroup>`.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#align)

Specifies the horizontal alignment of each column group cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `center`, `right`, `justify`, and `char`. When supported, the `char` value aligns the textual content on the character defined in the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#char)
 attribute and the offset defined by the [`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#charoff)
 attribute. Note that the descendant [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 elements may override this value using their own [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col#align)
 attribute. Use the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS property on the [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements instead, as this attribute is deprecated.

**Note:** Setting `text-align` on the `<colgroup>` element has no effect as [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements are not descendants of the `<colgroup>` element, and therefore they do not inherit from it.

If the table does not use a [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td#colspan)
 attribute, use the `td:nth-of-type(an+b)` CSS selector per column, where `a` is the total number of the columns in the table and `b` is the ordinal position of the column in the table, e.g., `td:nth-of-type(7n+2) { text-align: right; }` to right-align the second column cells.

If the table does use a [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td#colspan)
 attribute, the effect can be achieved by combining adequate CSS attribute selectors like `[colspan=n]`, though this is not trivial.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#bgcolor)

Defines the background color of each column group cell. The value is an HTML color; either a [6-digit hexadecimal RGB code](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
, prefixed by a `#`, or a [color keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. Other CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values are not supported. Use the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 CSS property instead, as this attribute is deprecated.

[`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#char)

Does nothing. It was originally intended to specify the alignment of the content to a character of each column group cell. Typical values for this include a period (`.`) when attempting to align numbers or monetary values. If [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#align)
 is not set to `char`, this attribute is ignored, though it will still be used as the default value for the [`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col#align)
 of the [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 elements which are members of this column group.

[`charoff`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#charoff)

Does nothing. It was originally intended to specify the number of characters to offset the column group cell content from the alignment character specified by the [`char`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#char)
 attribute.

[`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#valign)

Specifies the vertical alignment of each column group cell. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `baseline`, `bottom`, `middle`, and `top`. Note that the descendant [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 elements may override this value using their own [`valign`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col#valign)
 attribute. Use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 CSS property on the [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements instead, as this attribute is deprecated.

**Note:** Setting `vertical-align` on the `<colgroup>` element has no effect as [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements are not descendants of the `<colgroup>` element, and therefore they do not inherit from it.

If the table does not use a [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td#colspan)
 attribute, use the [`td:nth-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
 CSS selector per column, e.g., `td:nth-of-type(2) { vertical-align: middle; }` to center the second column cells vertically.

If the table does use a [`colspan`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td#colspan)
 attribute, the effect can be achieved by combining adequate CSS attribute selectors like `[colspan=n]`, though this is not trivial.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#width)

Specifies a default width for each column in the current column group. In addition to the standard pixel and percentage values, this attribute can take the special form `0*`, which means that the width of each column spanned should be the minimum width necessary to hold the column's contents. Relative widths such as `5*` can also be used. Note that the descendant [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 elements may override this value using their own [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col#width)
 attribute. Use the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 CSS property instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#usage_notes)

---------------------------------------------------------------------------------------------------------

*   The `<colgroup>` should appear within a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
     element (if used), but before any [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
     elements.
*   Only a limited number of CSS properties affect `<colgroup>`:
    *   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
         : The various `background` properties will set the background for cells within the column group. As the column group background color is painted on top of the table, but behind background colors applied to the columns ([`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
        ), the row groups ([`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
        , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
        , and [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
        ), the rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
        ), and the individual cells ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
         and [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
        ), backgrounds applied to table column groups are only visible if every layer painted on top of them has a transparent background.
    *   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
        : The various `border` properties apply, but only if the `<table>` has [`border-collapse: collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
         set.
    *   [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
        : The value `collapse` for a column group results in all cells of the columns in that column group not being rendered, and cells spanning into other columns being clipped. The space these columns in the column group would have occupied is removed. However, the size of other columns is still calculated as though the cells in the collapsed column(s) in the column group are present. Other values for `visibility` have no effect.
    *   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
        : The `width` property defines a minimum width for the columns within the column group, as if [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
         were set.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#example)

-------------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

This example demonstrates a seven-column table divided into two `<colgroup>` elements that span multiple columns.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#html)

Two `<colgroup>` elements are used to structure a basic table by creating column groups. The number of columns in each column group is specified by the [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#span)
 attribute.

html

    <table>
      <caption>
        Personal weekly activities
      </caption>
      <colgroup span="5" class="weekdays"></colgroup>
      <colgroup span="2" class="weekend"></colgroup>
      <thead>
        <tr>
          <th>Mon</th>
          <th>Tue</th>
          <th>Wed</th>
          <th>Thu</th>
          <th>Fri</th>
          <th>Sat</th>
          <th>Sun</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Clean room</td>
          <td>Football training</td>
          <td>Dance Course</td>
          <td>History Class</td>
          <td>Buy drinks</td>
          <td>Study hour</td>
          <td>Free time</td>
        </tr>
        <tr>
          <td>Yoga</td>
          <td>Chess Club</td>
          <td>Meet friends</td>
          <td>Gymnastics</td>
          <td>Birthday party</td>
          <td>Fishing trip</td>
          <td>Free time</td>
        </tr>
      </tbody>
    </table>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#css)

Grouped columns can be used to visually highlight the structure using CSS:

css

    table {
      border-collapse: collapse;
      border: 2px solid rgb(140 140 140);
    }
    
    caption {
      caption-side: bottom;
      padding: 10px;
    }
    
    th,
    td {
      border: 1px solid rgb(160 160 160);
      padding: 8px 6px;
      text-align: center;
    }
    
    .weekdays {
      background-color: #d7d9f2;
    }
    
    .weekend {
      background-color: #ffe8d4;
    }
    

    table {
      font-family: sans-serif;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | If the [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#span)<br> attribute is present: none.  <br>If the attribute is not present: zero or more [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)<br> element |
| Tag omission | The start tag may be omitted, if it has a [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)<br> element as its first child and if it is not preceded by a `<colgroup>` whose end tag has been omitted.  <br>The end tag may be omitted, if it is not followed by a space or a comment. |
| Permitted parents | A [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> element. The `<colgroup>` must appear after any [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)<br> element, but before any [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)<br>, [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)<br>, [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)<br>, and [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLTableColElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableColElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-colgroup-element](https://html.spec.whatwg.org/multipage/tables.html#the-colgroup-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#see_also)

---------------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
    , [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    : Other table-related elements
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    : CSS property to set the background color of each column group cell
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    : CSS property to control borders of column group cells
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align each column group cell content
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    : CSS property to vertically align each column group cell content
*   [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
    : CSS property to hide (or show) cells of a column group
*   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    : CSS property to control the default width for each column in a column group
*   [`:nth-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    , [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    , [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    : CSS pseudo-classes to select the desired column cells

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/colgroup/index.md?plain=1 "Folder: en-us/web/html/reference/elements/colgroup (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcolgroup&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcolgroup%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcolgroup%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcolgroup%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
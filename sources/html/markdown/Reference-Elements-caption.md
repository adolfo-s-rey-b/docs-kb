*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#mdn-search)
    

`<caption>` HTML table caption element
======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<caption>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies the caption (or title) of a table, providing the table an [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
 or [accessible description](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_description)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#try_it)

----------------------------------------------------------------------------------------------

    <table>
      <caption>
        He-Man and Skeletor facts
      </caption>
      <tbody>
        <tr>
          <td></td>
          <th scope="col" class="heman">He-Man</th>
          <th scope="col" class="skeletor">Skeletor</th>
        </tr>
        <tr>
          <th scope="row">Role</th>
          <td>Hero</td>
          <td>Villain</td>
        </tr>
        <tr>
          <th scope="row">Weapon</th>
          <td>Power Sword</td>
          <td>Havoc Staff</td>
        </tr>
        <tr>
          <th scope="row">Dark secret</th>
          <td>Expert florist</td>
          <td>Cries at romcoms</td>
        </tr>
      </tbody>
    </table>
    

    caption {
      caption-side: bottom;
      padding: 10px;
      font-weight: bold;
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
    
    th {
      background-color: rgb(230 230 230);
    }
    
    td {
      text-align: center;
    }
    
    tr:nth-child(even) td {
      background-color: rgb(250 250 250);
    }
    
    tr:nth-child(odd) td {
      background-color: rgb(240 240 240);
    }
    
    .heman {
      font:
        1.4rem "molot",
        sans-serif;
      text-shadow:
        1px 1px 1px white,
        2px 2px 1px black;
    }
    
    .skeletor {
      font:
        1.7rem "rapscallion",
        fantasy;
      letter-spacing: 3px;
      text-shadow:
        1px 1px 0 white,
        0 0 9px black;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#attributes)

------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#deprecated_attributes)

The following attributes are deprecated and should not be used. They are documented below for reference when updating existing code and for historical interest only.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#align)

Specifies on which side of the table the caption should be displayed. The possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are `left`, `top`, `right`, or `bottom`. Use the [`caption-side`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side)
 and [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 CSS properties instead, as this attribute is deprecated.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#usage_notes)

--------------------------------------------------------------------------------------------------------

*   If included, the `<caption>` element must be the first child of its parent [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
     element.
*   When a `<table>` is nested within a [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
     as the figure's only content, it should be captioned via a [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
     for the `<figure>` instead of as a `<caption>` nested within the `<table>`.
*   Any [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
     applied to a table will not be applied to its caption. Add a `background-color` to the `<caption>` element as well if you want the same color to be behind both.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#example)

------------------------------------------------------------------------------------------------

See [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 for a complete table example introducing common standards and best practices.

### [Table with caption](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#table_with_caption)

This example demonstrates a basic table that includes a caption describing the data presented.

Such a "title" is helpful for users who are quickly scanning the page, and it is especially beneficial for visually impaired users, allowing them to determine the table's relevance quickly without the need to have a screen reader read the contents of many cells just to find out what the table is about.

#### HTML

A `<caption>` element is used as the first child of the [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
, with text content similar to a title to describe the table data. Three rows, the first being a header row, with two columns are created using the [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
, [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 and [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 elements after the `<caption>`.

html

    <table>
      <caption>
        User login email addresses
      </caption>
      <thead>
        <tr>
          <th>Login</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>user1</td>
          <td>user1@example.com</td>
        </tr>
        <tr>
          <td>user2</td>
          <td>user2@example.com</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

Some basic CSS is used to align and highlight the `<caption>`.

css

    caption {
      caption-side: top;
      text-align: left;
      padding-bottom: 10px;
      font-weight: bold;
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
    
    th {
      background-color: rgb(230 230 230);
    }
    
    td {
      text-align: center;
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | The end tag can be omitted if the element is not immediately followed by ASCII whitespace or a comment. |
| Permitted parents | A [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br> element, as its first descendant. |
| Implicit ARIA role | `[caption](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLTableCaptionElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableCaptionElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-caption-element](https://html.spec.whatwg.org/multipage/tables.html#the-caption-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption#see_also)

--------------------------------------------------------------------------------------------------

*   [Learn: HTML table basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
    
*   [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
    , [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
    , [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    , [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
    , [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
    , [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
    , [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
    , [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
    , [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
    : Other table-related elements
*   [`caption-side`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side)
    : CSS property to position the `<caption>` relative to its parent [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
    
*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    : CSS property to horizontally align the text content of the `<caption>`

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/caption/index.md?plain=1 "Folder: en-us/web/html/reference/elements/caption (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcaption&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcaption%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcaption%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcaption%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
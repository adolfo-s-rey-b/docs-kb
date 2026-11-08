*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#mdn-search)
    

`<ol>` HTML ordered list element
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<ol>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents an ordered list of items — typically rendered as a numbered list.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#try_it)

-----------------------------------------------------------------------------------------

    <ol>
      <li>Mix flour, baking powder, sugar, and salt.</li>
      <li>In another bowl, mix eggs, milk, and oil.</li>
      <li>Stir both mixtures together.</li>
      <li>Fill muffin tray 3/4 full.</li>
      <li>Bake for 20 minutes.</li>
    </ol>
    

    li {
      font:
        1rem "Fira Sans",
        sans-serif;
      margin-bottom: 0.5rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#attributes)

-------------------------------------------------------------------------------------------------

This element also accepts the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#compact)

This Boolean attribute hints that the list should be rendered in a compact style. The interpretation of this attribute is browser-specific. Use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 instead: to give a similar effect as the `compact` attribute, the CSS property [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 can be used with a value of `80%`.

[`reversed`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#reversed)

This Boolean attribute specifies that the list's items are in reverse order. Items will be numbered from high to low.

[`start`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#start)

An integer to start counting from for the list items. Always an Arabic numeral (1, 2, 3, etc.), even when the numbering `type` is letters or Roman numerals. For example, to start numbering elements from the letter "d" or the Roman numeral "iv," use `start="4"`.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#type)

Sets the numbering type:

*   `a` for lowercase letters
*   `A` for uppercase letters
*   `i` for lowercase Roman numerals
*   `I` for uppercase Roman numerals
*   `1` for numbers (default)

The specified type is used for the entire list unless a different [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#type)
 attribute is used on an enclosed [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 element.

**Note:** Unless the type of the list number matters (like legal or technical documents where items are referenced by their number/letter), use the CSS [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property instead.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#usage_notes)

---------------------------------------------------------------------------------------------------

Typically, ordered list items display with a preceding [marker](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
, such as a number or letter.

The `<ol>` and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 (or the synonym [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
) elements may nest as deeply as desired, alternating between `<ol>`, `<ul>` (or `<menu>`) as needed. To nest a list, place it inside an [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 element of the parent list; a list element can not be a direct child of another `<ul>` or `<ol>`.

The `<ol>` and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 elements both represent a list of items. The difference is with the `<ol>` element, the order is meaningful. For example:

*   Steps in a recipe
*   Turn-by-turn directions
*   The list of ingredients in decreasing proportion on nutrition information labels

To determine which list to use, try changing the order of the list items; if the meaning changes, use the `<ol>` element — otherwise you can use [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 otherwise, or [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
 if your list is a menu.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#examples)

---------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#basic_example)

html

    <ol>
      <li>Fee</li>
      <li>Fi</li>
      <li>Fo</li>
      <li>Fum</li>
    </ol>
    

#### Result

### [Using Roman Numeral type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#using_roman_numeral_type)

html

    <ol type="i">
      <li>Introduction</li>
      <li>List of Grievances</li>
      <li>Conclusion</li>
    </ol>
    

#### Result

### [Using the start attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#using_the_start_attribute)

html

    <p>Finishing places of contestants not in the winners' circle:</p>
    
    <ol start="4">
      <li>Speedwalk Stu</li>
      <li>Saunterin' Sam</li>
      <li>Slowpoke Rodriguez</li>
    </ol>
    

#### Result

### [Nesting lists](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#nesting_lists)

html

    <ol>
      <li>first item</li>
      <li>
        second item
        <!-- closing </li> tag is not here! -->
        <ol>
          <li>second item first subitem</li>
          <li>second item second subitem</li>
          <li>second item third subitem</li>
        </ol>
      </li>
      <!-- Here's the closing </li> tag -->
      <li>third item</li>
    </ol>
    

#### Result

### [Unordered list inside ordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#unordered_list_inside_ordered_list)

html

    <ol>
      <li>first item</li>
      <li>
        second item
        <!-- closing </li> tag is not here! -->
        <ul>
          <li>second item first subitem</li>
          <li>second item second subitem</li>
          <li>second item third subitem</li>
        </ul>
      </li>
      <!-- Here's the closing </li> tag -->
      <li>third item</li>
    </ol>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, and if the `<ol>` element's children include at least one [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br> element, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | Zero or more [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br>, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[list](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role) ` |
| Permitted ARIA roles | [`directory`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/directory_role)<br>, [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, [`listbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)<br>, [`menu`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)<br>, [`menubar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menubar_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`radiogroup`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radiogroup_role)<br>, [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)<br>, [`toolbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/toolbar_role)<br>, [`tree`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role) |
| DOM interface | [`HTMLOListElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOListElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-ol-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ol-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol#see_also)

---------------------------------------------------------------------------------------------

*   Other list-related HTML Elements: [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
    , [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
    , [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
    
*   CSS properties that may be specially useful to style the `<ol>` element:
    *   the [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
         property, to choose the way the ordinal displays
    *   [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
        , to handle complex nested lists
    *   the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
         property, to simulate the deprecated `compact` attribute
    *   the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
         property, to control the list indentation

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/ol/index.md?plain=1 "Folder: en-us/web/html/reference/elements/ol (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fol&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fol%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fol%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fol%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F51c7af056884cf4b990052e492c21cc8508eef5c%0A*+Document+last+modified%3A+2026-10-06T08%3A51%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
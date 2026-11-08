*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#mdn-search)
    

`<ul>` HTML unordered list element
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<ul>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents an unordered list of items, typically rendered as a bulleted list.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#try_it)

-----------------------------------------------------------------------------------------

    <ul>
      <li>Milk</li>
      <li>
        Cheese
        <ul>
          <li>Blue cheese</li>
          <li>Feta</li>
        </ul>
      </li>
    </ul>
    

    li {
      list-style-type: circle;
    }
    
    li li {
      list-style-type: square;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#attributes)

-------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#compact)

This Boolean attribute hints that the list should be rendered in a compact style. The interpretation of this attribute is browser-specific. Use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 instead: to give a similar effect as the `compact` attribute, the CSS property [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 can be used with a value of `80%`.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#type)

This attribute sets the bullet style for the list. The values defined under HTML3.2 and the transitional version of HTML 4.0/4.01 are:

*   `circle`
*   `disc`
*   `square`

A fourth bullet type has been defined in the WebTV interface, but not all browsers support it: `triangle`.

If not present and if no [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property applies to the element, the user agent selects a bullet type depending on the nesting level of the list.

**Warning:** Do not use this attribute, as it has been deprecated; use the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property instead.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#usage_notes)

---------------------------------------------------------------------------------------------------

*   The `<ul>` element is for grouping a collection of items that do not have a numerical ordering, and their order in the list is meaningless. Typically, unordered-list items are displayed with a bullet, which can be of several forms, like a dot, a circle, or a square. The bullet style is not defined in the HTML description of the page, but in its associated CSS, using the [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
     property.
*   The `<ul>` and [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     elements may be nested as deeply as desired. Moreover, the nested lists may alternate between `<ol>` and `<ul>` without restriction. To nest a list, place it inside an [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
     element of the parent list; a `<ul>` or `<ol>` can't be a direct child of another `<ul>` or `<ol>`.
*   The [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     and `<ul>` elements both represent a list of items. They differ in that, with the [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     element, the order is meaningful. To determine which one to use, try changing the order of the list items; if the meaning is changed, the [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     element should be used, otherwise you can use `<ul>`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#examples)

---------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#basic_example)

html

    <ul>
      <li>first item</li>
      <li>second item</li>
      <li>third item</li>
    </ul>
    

#### Result

### [Nesting a list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#nesting_a_list)

html

    <ul>
      <li>first item</li>
      <li>
        second item
        <!-- Look, the closing </li> tag is not placed here! -->
        <ul>
          <li>second item first subitem</li>
          <li>
            second item second subitem
            <!-- Same for the second nested unordered list! -->
            <ul>
              <li>second item second subitem first sub-subitem</li>
              <li>second item second subitem second sub-subitem</li>
              <li>second item second subitem third sub-subitem</li>
            </ul>
          </li>
          <!-- Closing </li> tag for the li that
                      contains the third unordered list -->
          <li>second item third subitem</li>
        </ul>
        <!-- Here is the closing </li> tag -->
      </li>
      <li>third item</li>
    </ul>
    

#### Result

### [Ordered list inside unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#ordered_list_inside_unordered_list)

html

    <ul>
      <li>first item</li>
      <li>
        second item
        <!-- Look, the closing </li> tag is not placed here! -->
        <ol>
          <li>second item first subitem</li>
          <li>second item second subitem</li>
          <li>second item third subitem</li>
        </ol>
        <!-- Here is the closing </li> tag -->
      </li>
      <li>third item</li>
    </ul>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, and if the `<ul>` element's children include at least one [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br> element, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | Zero or more [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br>, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[list](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role) ` |
| Permitted ARIA roles | [`directory`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/directory_role)<br>, [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, [`listbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)<br>, [`menu`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)<br>, [`menubar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menubar_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`radiogroup`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radiogroup_role)<br>, [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)<br>, [`toolbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/toolbar_role)<br>, [`tree`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role) |
| DOM Interface | [`HTMLUListElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLUListElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-ul-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#see_also)

---------------------------------------------------------------------------------------------

*   Other list-related HTML Elements: [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
    , [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
    , [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
    
*   CSS properties that may be specially useful to style the `<ul>` element:
    *   the [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
         property, to choose the way the ordinal displays.
    *   [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
        , to handle complex nested lists.
    *   the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
         property, to simulate the deprecated [`compact`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul#compact)
         attribute.
    *   the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
         property, to control the list indentation.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/ul/index.md?plain=1 "Folder: en-us/web/html/reference/elements/ul (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ful&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ful%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ful%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ful%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F51c7af056884cf4b990052e492c21cc8508eef5c%0A*+Document+last+modified%3A+2026-10-06T08%3A51%3A49.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
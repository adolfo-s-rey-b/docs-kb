*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#mdn-search)
    

`<menu>` HTML menu element
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<menu>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is described in the HTML specification as a semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
, but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
. It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#try_it)

-------------------------------------------------------------------------------------------

    <div class="news">
      <a href="#">NASA's Webb Delivers Deepest Infrared Image of Universe Yet</a>
      <menu>
        <li><button id="save">Save for later</button></li>
        <li><button id="share">Share this news</button></li>
      </menu>
    </div>
    

    .news {
      background-color: bisque;
      padding: 1em;
      border: solid thin black;
    }
    
    menu {
      list-style-type: none;
      display: flex;
      padding: 0;
      margin-bottom: 0;
      gap: 1em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#attributes)

---------------------------------------------------------------------------------------------------

This element also accepts the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#compact)

This Boolean attribute hints that the list should be rendered in a compact style. The interpretation of this attribute is browser-specific. Use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 instead: to give a similar effect as the `compact` attribute, the CSS property [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 can be used with a value of `80%`.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#usage_notes)

-----------------------------------------------------------------------------------------------------

The `<menu>` and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 elements both represent an unordered list of items. The key difference is that [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 primarily contains items for display, while `<menu>` represents a toolbar containing commands that the user can perform or activate.

**Note:** In early versions of the HTML specification, the `<menu>` element had an additional use case as a context menu. This functionality is considered obsolete and is not in the specification.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#examples)

-----------------------------------------------------------------------------------------------

### [Toolbar](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#toolbar)

In this example, a `<menu>` is used to create a toolbar for an editing application.

#### HTML

html

    <menu>
      <li><button onclick="copy()">Copy</button></li>
      <li><button onclick="cut()">Cut</button></li>
      <li><button onclick="paste()">Paste</button></li>
    </menu>
    

Note that this is functionally no different from:

html

    <ul>
      <li><button onclick="copy()">Copy</button></li>
      <li><button onclick="cut()">Cut</button></li>
      <li><button onclick="paste()">Paste</button></li>
    </ul>
    

#### CSS

css

    menu,
    ul {
      display: flex;
      list-style: none;
      padding: 0;
      width: 400px;
    }
    
    li {
      flex-grow: 1;
    }
    
    button {
      width: 100%;
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. If the element's children include at least one [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br> element: [Palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | Zero or more occurrences of [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br>, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br>, and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[list](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role) ` |
| Permitted ARIA roles | [`directory`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/directory_role)<br>, [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, `[listbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role) `, [`menu`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)<br>, [`menubar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menubar_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`radiogroup`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radiogroup_role)<br>, [`tablist`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tablist_role)<br>, [`toolbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/toolbar_role)<br> or [`tree`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tree_role) |
| DOM interface | [`HTMLMenuElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMenuElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-menu-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-menu-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu#see_also)

-----------------------------------------------------------------------------------------------

*   Other list-related HTML Elements: [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
    , [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
    , and [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/menu/index.md?plain=1 "Folder: en-us/web/html/reference/elements/menu (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmenu&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmenu%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmenu%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmenu%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
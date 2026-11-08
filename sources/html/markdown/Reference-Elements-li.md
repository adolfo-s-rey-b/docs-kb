*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#mdn-search)
    

`<li>` HTML list item element
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<li>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to represent an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#try_it)

-----------------------------------------------------------------------------------------

    <p>Apollo astronauts:</p>
    
    <ul>
      <li>Neil Armstrong</li>
      <li>Alan Bean</li>
      <li>Peter Conrad</li>
      <li>Edgar Mitchell</li>
      <li>Alan Shepard</li>
    </ul>
    

    p,
    li {
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    p {
      font-weight: bold;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#attributes)

-------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#value)

This integer attribute indicates the current ordinal value of the list item as defined by the [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 element. The only allowed value for this attribute is a number, even if the list is displayed with Roman numerals or letters. List items that follow this one continue numbering from the value set. This attribute has no meaning for unordered lists ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) or for menus ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
).

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#type)

This character attribute indicates the numbering type:

*   `a`: lowercase letters
*   `A`: uppercase letters
*   `i`: lowercase Roman numerals
*   `I`: uppercase Roman numerals
*   `1`: numbers

This type overrides the one used by its parent [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 element, if any.

**Note:** This attribute has been deprecated; use the CSS [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 property instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#examples)

---------------------------------------------------------------------------------------------

For more detailed examples, see the [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 and [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 pages.

### [Ordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#ordered_list)

html

    <ol>
      <li>first item</li>
      <li>second item</li>
      <li>third item</li>
    </ol>
    

#### Result

### [Ordered list with a custom value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#ordered_list_with_a_custom_value)

html

    <ol type="I">
      <li value="3">third item</li>
      <li>fourth item</li>
      <li>fifth item</li>
    </ol>
    

#### Result

### [Unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#unordered_list)

html

    <ul>
      <li>first item</li>
      <li>second item</li>
      <li>third item</li>
    </ul>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | The end tag can be omitted if the list item is immediately followed by another `<li>` element, or if there is no more content in its parent element. |
| Permitted parents | An [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br>, [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)<br>, or [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)<br> element. Though not a conforming usage, the obsolete [`<dir>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dir)<br> can also be a parent. |
| Implicit ARIA role | `[listitem](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listitem_role) ` when child of an `[ol](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol) `, `[ul](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul) ` or `[menu](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu) ` |
| Permitted ARIA roles | [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>, [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>, [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>, [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>, [`separator`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/separator_role)<br>, [`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)<br>, [`treeitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/treeitem_role) |
| DOM interface | [`HTMLLIElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLIElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-li-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-li-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li#see_also)

---------------------------------------------------------------------------------------------

*   Other list-related HTML Elements: [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
    , [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
    , [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
    , and the obsolete [`<dir>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dir)
    ;
*   CSS properties that may be specially useful to style the `<li>` element:
    *   the [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
         property, to choose the way the ordinal is displayed,
    *   [CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
        , to handle complex nested lists,
    *   the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
         property, to control the indent of the list item.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/li/index.md?plain=1 "Folder: en-us/web/html/reference/elements/li (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fli&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fli%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fli%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fli%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
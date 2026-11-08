*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#mdn-search)
    

`<hr>` HTML thematic break (horizontal rule) element
====================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<hr>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a thematic break between elements: for example, a change of scene in a story, or a shift of topic within a section.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#try_it)

-----------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#attributes)

-------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`align`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#align)

Sets the alignment of the rule on the page. If no value is specified, the default value is `left`.

[`color`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#color)

Sets the color of the rule through color name or hexadecimal value.

[`noshade`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#noshade)

Sets the rule to have no shading.

[`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#size)

Sets the height, in pixels, of the rule.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#width)

Sets the length of the rule on the page through a pixel or percentage value.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#usage_notes)

---------------------------------------------------------------------------------------------------

Historically, the `<hr>` element has always been presented as a horizontal rule or line. While it may still be displayed as a horizontal rule in visual browsers, this element is now defined in semantic terms, rather than presentational terms. Therefore, if you wish to draw a horizontal line, you should do so by adding a border to an existing element using CSS.

The `border-*` properties (for example, [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 and [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
) allow you to significantly customize a line's appearance, whether you are customizing an `<hr>` element or a border drawn on a different element.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#example)

-------------------------------------------------------------------------------------------

### [Thematic break between paragraphs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#thematic_break_between_paragraphs)

The following example adds a thematic break between paragraph-level elements.

#### HTML

#### Result

### [Thematic break between list items](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#thematic_break_between_list_items)

The `<hr>` tag can be placed within a list item for visual separation, to create a separator between sections of a list.

#### HTML

#### Result

### [Thematic break between select options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#thematic_break_between_select_options)

The `<hr>` element is allowed inside a `<select>` element to create a visual separator between `<option>` elements.

#### HTML

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | *   Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>    <br>*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br>     element |
| Implicit ARIA role | [`separator`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/separator_role) |
| Permitted ARIA roles | [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br> or [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role) |
| DOM interface | [`HTMLHRElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLHRElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-hr-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-hr-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr#see_also)

---------------------------------------------------------------------------------------------

*   [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
    
*   [`<hr>` in `<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#select_with_grouping_options)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/hr/index.md?plain=1 "Folder: en-us/web/html/reference/elements/hr (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fhr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fhr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#mdn-search)
    

`<datalist>` HTML data list element
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/51)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<datalist>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 elements that represent the permissible or recommended options available to choose from within other controls.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#try_it)

-----------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#attributes)

-------------------------------------------------------------------------------------------------------

This element has no other attributes than the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, common to all elements.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#usage_notes)

---------------------------------------------------------------------------------------------------------

To bind the `<datalist>` element to the control, we give it a unique identifier in the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute, and then add the [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
 attribute to the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element with the same identifier as value. Only certain types of [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 support this behavior, and it can also vary from browser to browser.

Each `<option>` element should have a `value` attribute, which represents a suggestion to be entered into the input. It can also have a `label` attribute, or, missing that, some text content, which may be displayed by the browser instead of `value` (Firefox), or in addition to `value` (Chrome and Safari, as supplemental text). The exact content of the drop-down menu depends on the browser, but when clicked, content entered into control field will always come from the `value` attribute.

**Note:** `<datalist>` is not a replacement for [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
. A `<datalist>` does not represent an input itself; it is a list of suggested values for an associated control. The control can still accept any value that passes validation, even if it is not in this suggestion list.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#accessibility)

-------------------------------------------------------------------------------------------------------------

When deciding to use the `<datalist>` element, here are some accessibility issues to be mindful of:

*   The font size of the data list's options does not zoom, always remaining the same size. The contents of the autosuggest do not grow or shrink when the rest of the contents are zoomed in or out.
*   As targeting the list of options with CSS is very limited to non-existent, rendering cannot be styled for high-contrast mode.
*   Some screen reader/browser combinations, including NVDA and Firefox, do not announce the contents of the autosuggest popup.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#examples)

---------------------------------------------------------------------------------------------------

### [Textual types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#textual_types)

Recommended values in types [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, [search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
, [url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
, [tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
, [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 and [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
, are displayed in a drop-down menu when user clicks or double-clicks on the control. Typically the right side of a control will also have an arrow pointing to the presence of predefined values.

### [Date and Time types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#date_and_time_types)

The types [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
, [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
, [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
, [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
 and [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
 can show an interface that allows a convenient selection of a date and time. Predefined values can be shown there, allowing the user to quickly fill the control value.

**Note:** When these types are not supported, a basic `text` type will be rendered instead, creating a text field. That field will correctly recognize recommended values and display them to the user in a drop-down menu.

### [Range type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#range_type)

When `value` attributes are included on `<option>` elements provided for a datalist associated with a [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 input type, they will be shown as a series of tick marks that the user can easily select.

**Note:** The `label` attribute is intended to provide labels for tick marks, as defined in the [HTML Standard](https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range) "External link (opens in new tab)")
. However, current browser support varies; labels might not be displayed visually or as tooltips.

### [Color type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#color_type)

The [color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)
 type can show predefined colors in a browser-provided interface.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | Either [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br> or zero or more [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [listbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLDataListElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDataListElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-datalist-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-datalist-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#see_also)

---------------------------------------------------------------------------------------------------

*   The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element, and more specifically its [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
     attribute;
*   The [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
     element.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/datalist/index.md?plain=1 "Folder: en-us/web/html/reference/elements/datalist (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdatalist&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdatalist%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdatalist%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdatalist%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
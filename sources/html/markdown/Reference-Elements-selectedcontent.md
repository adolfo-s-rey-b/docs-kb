*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#mdn-search)
    

`<selectedcontent>` HTML selected option display element
========================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/278)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<selectedcontent>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 is used inside a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element to display the contents of its currently selected [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 within its first child [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
. This enables you to style all parts of a `<select>` element, referred to as "[customizable selects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
".

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#attributes)

--------------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#description)

----------------------------------------------------------------------------------------------------------------

You use the `<selectedcontent>` element as the only child of a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element, which must be the first child of the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element. Any [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element, the only other valid child of `<select>`, must come after the `<button>` and nested `<selectedcontent>` pair.

### [How `<selectedcontent>` works behind the scenes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#how_selectedcontent_works_behind_the_scenes)

The `<selectedcontent>` element contains a clone of the content of the currently selected [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
. The browser renders this clone using [`cloneNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode "cloneNode()")
. When the selected `<option>` changes, such as during a [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
 event, the contents of `<selectedcontent>` are replaced with a clone of the newly selected `<option>`. Being aware of this behavior is important, especially when working with dynamic content.

**Warning:** Since the browser updates `<selectedcontent>` only when the selected `<option>` changes, any dynamic modifications to the content of the selected `<option>` after the `<select>` is rendered won't be cloned to `<selectedcontent>`. You'll need to update `<selectedcontent>` manually. Watch out if you're using any of the popular front-end JavaScript frameworks where `<option>` elements are updated dynamically after the initial render–the result may not match what you expect in `<selectedcontent>`.

### [`<selectedcontent>` inertness](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#selectedcontent_inertness)

By default, any `<button>` inside a `<select>` element is [inert](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert)
. As a result, all content inside that button—including `<selectedcontent>`—is also inert. This means users can't interact with or focus on content inside `<selectedcontent>`.

### [Styling the selected option's content with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#styling_the_selected_options_content_with_css)

You can target the content of the currently selected `<option>` element and style how it appears inside the select button. Styling the button doesn't affect the styling of the content of the `<option>` that was cloned. This lets you customize how the selected option appears in the button, separately from how it appears in the drop-down list.

For example, your `<option>` elements may contain icons, images, or even videos that render nicely inside the drop-down, but could cause the select `<button>` to increase in size, look untidy, and affect the surrounding layout. By targeting the content inside `<selectedcontent>`, you can hide elements such as images in the button, without affecting how they appear in the drop-down, as shown in the following snippet:

**Note:** If the `<button>` and/or `<selectedcontent>` elements are not included inside `<select>`, the browser creates an implicit `<button>` to display the contents of the selected `<option>`. This fallback button cannot be targeted with CSS using the `button` or `selectedcontent` type selector.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#examples)

----------------------------------------------------------------------------------------------------------

You can see a full example that includes the `<selectedcontent>` element in our [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 guide.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#technical_summary)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None |
| Permitted content | Mirrors content from the selected [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | A [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)<br> element that is the first child of a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br> element. |
| Implicit ARIA role | None |
| Permitted ARIA roles | None |
| DOM interface | [`HTMLSelectedContentElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectedContentElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-selectedcontent-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-selectedcontent-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent#see_also)

----------------------------------------------------------------------------------------------------------

*   The [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     element
*   The [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
     element
*   The [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
     element
*   [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/selectedcontent/index.md?plain=1 "Folder: en-us/web/html/reference/elements/selectedcontent (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fselectedcontent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fselectedcontent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fselectedcontent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fselectedcontent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F513146a616213fee548fdcf72dc1359030eb3395%0A*+Document+last+modified%3A+2026-07-04T09%3A59%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
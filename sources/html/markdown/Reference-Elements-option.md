*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#mdn-search)
    

`<option>` HTML option element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<option>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to define an item contained in a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
, or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#try_it)

---------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#attributes)

-----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

If this Boolean attribute is set, this option is not checkable. Often browsers gray out such control and it won't receive any browsing event, like mouse clicks or focus-related ones. If this attribute is not set, the element can still be disabled if one of its ancestors is a disabled [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
 element.

[`label`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#label)

This attribute is text for the label indicating the meaning of the option. If the `label` attribute isn't defined, its value is that of the element text content.

[`selected`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#selected)

If present, this Boolean attribute indicates that the option is initially selected. If the `<option>` element is the descendant of a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element whose [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#multiple)
 attribute is not set, only one single `<option>` of this [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element may have the `selected` attribute.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#value)

The content of this attribute represents the value to be submitted with the form, should this option be selected. If this attribute is omitted, the value is taken from the text content of the option element.

[Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#styling_with_css)

-----------------------------------------------------------------------------------------------------------------

Styling `<option>` elements has historically been highly limited. [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 explains newer features that enable their full customization, just like any regular DOM element.

### [Legacy option styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#legacy_option_styling)

In browsers that don't support the modern customization features (or legacy codebases where they can't be used), the styling available on `<option>` elements depends on the browser and operating system. Depending on the operating system, the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the owning `<select>` is respected in Firefox and Chromium. Chromium may additionally allow [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
, [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
, [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
, and [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 to be set.

You can find more details about legacy `<option>` styling in [our guide to advanced form styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#examples)

-------------------------------------------------------------------------------------------------

See [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 for examples.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | In traditional `<select>` elements, only text content is permitted, possibly with escaped characters (like `&eacute;`). In [customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)<br>, `<option>` elements can have any arbitrary content. |
| Tag omission | The start tag is mandatory. The end tag is optional if this element is immediately followed by another `<option>` element or an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)<br>, or if the parent element has no more content. |
| Permitted parents | A [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br>, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)<br> or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)<br> element. |
| Implicit ARIA role | [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLOptionElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptionElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-option-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-option-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#see_also)

-------------------------------------------------------------------------------------------------

*   Other form-related elements: [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    , [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
    , [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    , [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
    , [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
    , [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
    , [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    , [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
    , [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
     and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    .
*   [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/option/index.md?plain=1 "Folder: en-us/web/html/reference/elements/option (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foption&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Foption%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foption%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Foption%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
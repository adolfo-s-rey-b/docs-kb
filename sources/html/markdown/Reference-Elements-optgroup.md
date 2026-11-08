*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#mdn-search)
    

`<optgroup>` HTML option group element
======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<optgroup>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#try_it)

-----------------------------------------------------------------------------------------------

    <label for="dino-select">Choose a dinosaur:</label>
    <select id="dino-select">
      <optgroup label="Theropods">
        <option>Tyrannosaurus</option>
        <option>Velociraptor</option>
        <option>Deinonychus</option>
      </optgroup>
      <optgroup label="Sauropods">
        <option>Diplodocus</option>
        <option>Saltasaurus</option>
        <option>Apatosaurus</option>
      </optgroup>
    </select>
    

    label {
      display: block;
      margin-bottom: 10px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

If this Boolean attribute is set, none of the items in this option group is selectable. Often browsers gray out such control and it won't receive any browsing events, like mouse clicks or focus-related ones.

[`label`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#label)

The name of the group of options, which the browser can use when labeling the options in the user interface. This attribute is mandatory if this element is used.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#usage_notes)

---------------------------------------------------------------------------------------------------------

Optgroup elements may not be nested.

In [customizable `<select>` elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
, the [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 element is allowed as a child of `<optgroup>`, to provide a label that is easy to target and style. This replaces any text set in the `<optgroup>` element's `label` attribute, and it has the same semantics.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#examples)

---------------------------------------------------------------------------------------------------

html

    <select>
      <optgroup label="Group 1">
        <option>Option 1.1</option>
      </optgroup>
      <optgroup label="Group 2">
        <option>Option 2.1</option>
        <option>Option 2.2</option>
      </optgroup>
      <optgroup label="Group 3" disabled>
        <option>Option 3.1</option>
        <option>Option 3.2</option>
        <option>Option 3.3</option>
      </optgroup>
    </select>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | Zero or more [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br> elements. In [customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)<br>, a [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)<br> element is permitted as a child of `<optgroup>`. |
| Tag omission | The start tag is mandatory. The end tag is optional if this element is immediately followed by another `<optgroup>` element, or if the parent element has no more content. |
| Permitted parents | A [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br> element. |
| Implicit ARIA role | [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLOptGroupElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOptGroupElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-optgroup-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-optgroup-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup#see_also)

---------------------------------------------------------------------------------------------------

*   Other form-related elements: [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
    , [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
    , [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    , [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
    , [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
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

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/optgroup/index.md?plain=1 "Folder: en-us/web/html/reference/elements/optgroup (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foptgroup&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Foptgroup%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foptgroup%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Foptgroup%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
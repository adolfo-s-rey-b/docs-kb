*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#mdn-search)
    

`<output>` HTML output element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<output>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is a container element into which a site or app can inject the results of a calculation or the outcome of a user action.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#attributes)

-----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/for)

A space-separated list of other elements' [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
s, indicating that those elements contributed input values to (or otherwise affected) the calculation.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

The [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element to associate the output with (its _form owner_). The value of this attribute must be the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of a `<form>` in the same document. (If this attribute is not set, the `<output>` is associated with its ancestor `<form>` element, if any.)

This attribute lets you associate `<output>` elements to `<form>`s anywhere in the document, not just inside a `<form>`. It can also override an ancestor `<form>` element. The `<output>` element's name and content are not submitted when the form is submitted.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#name)

The element's name. Used in the [`form.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements "form.elements")
 API.

The `<output>` value, name, and contents are NOT submitted during form submission.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#accessibility)

-----------------------------------------------------------------------------------------------------------

Many browsers implement this element as an [`aria-live`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)
 region. Assistive technology will thereby announce the results of UI interactions posted inside it without requiring that focus is switched away from the controls that produce those results.

Live-region updates are generally announced as plain text, so links, buttons, and other semantics nested inside `<output>` may not be conveyed in the announcement.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#examples)

-------------------------------------------------------------------------------------------------

In the following example, we provide a slider whose value can range between `0` and `100`, and an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element into which you can enter a second number. The two numbers are added together, and the result is displayed in the `<output>` element each time the value of any of the controls changes.

html

    <input type="range" id="b" name="b" value="50" /> +
    <input type="number" id="a" name="a" value="10" /> =
    <output id="result" for="a b">60</output>
    

js

    const a = document.getElementById("a");
    const b = document.getElementById("b");
    const result = document.getElementById("result");
    
    function updateResult() {
      const aValue = a.valueAsNumber;
      const bValue = b.valueAsNumber;
      result.value = aValue + bValue;
    }
    
    a.addEventListener("input", updateResult);
    b.addEventListener("input", updateResult);
    
    updateResult();
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)<br>, [resettable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#resettable)<br> [form-associated element](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [`status`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/status_role) |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLOutputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOutputElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-output-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-output-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/output/index.md?plain=1 "Folder: en-us/web/html/reference/elements/output (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foutput&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Foutput%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Foutput%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Foutput%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
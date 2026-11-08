*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#mdn-search)
    

`<label>` HTML label element
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<label>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a caption for an item in a user interface.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#try_it)

--------------------------------------------------------------------------------------------

    <div class="preference">
      <label for="cheese">I like cheese.</label>
      <input type="checkbox" name="cheese" id="cheese" />
    </div>
    
    <div class="preference">
      <label for="peas">I like peas.</label>
      <input type="checkbox" name="peas" id="peas" />
    </div>
    

    .preference {
      display: flex;
      justify-content: space-between;
      width: 60%;
      margin: 0.5rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/for)

The value is the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of the [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)
 form control in the same document, [associating the `<label>` with that form control](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#associating_a_label_with_a_form_control)
. Note that its JavaScript reflection property is [`htmlFor`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/htmlFor)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#usage_notes)

------------------------------------------------------------------------------------------------------

### [Associating a label with a form control](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#associating_a_label_with_a_form_control)

The first element in the document with an `id` attribute matching the value of the `for` attribute is the _labeled control_ for this `label` element — if the element with that `id` is actually a [labelable element](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)
. If it is _not_ a labelable element, then the `for` attribute has no effect. If there are other elements that also match the `id` value, later in the document, they are not considered.

Multiple `<label>` elements can be associated with the same form control by having multiple `<label>` elements with the same `for` attribute value, which gives the form control multiple labels.

Associating a `<label>` with a form control, such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 offers some major advantages:

*   The label text is not only visually associated with its corresponding text input; it is programmatically associated with it too. This means that, for example, a screen reader will read out the label when the user is focused on the form input, making it easier for an assistive technology user to understand what data should be entered.
*   When a user clicks or touches/taps a label, the browser passes the focus to its associated input (the resulting event is also raised for the input). That increased hit area for focusing the input provides an advantage to anyone trying to activate it — including those using a touch-screen device.

There are two ways to associate a `<label>` with a form control, commonly referred to as _explicit_ and _implicit_ association.

To explicitly associate a `<label>` element with an `<input>` element, you first need to add the `id` attribute to the `<input>` element. Next, you add the `for` attribute to the `<label>` element, where the value of `for` is the same as the `id` in the `<input>` element.

html

    <label for="peas">I like peas.</label>
    <input type="checkbox" name="peas" id="peas" />
    

Alternatively, you can nest the `<input>` directly inside the `<label>`, in which case the `for` and `id` attributes are not needed because the association is implicit:

html

    <label>
      I like peas.
      <input type="checkbox" name="peas" />
    </label>
    

**Note:** A `<label>` element can have both a `for` attribute and a contained control element, as long as the `for` attribute points to the contained control element.

These two methods are equivalent, but there are a few considerations:

*   While common browser and [screen reader](https://developer.mozilla.org/en-US/docs/Glossary/Screen_reader)
     combinations support implicit association, not all assistive technologies do.
*   Depending on your design, the type of association may impact stylability. Making the `<label>` and form control sibling elements instead of parent-child means they are separate, adjacent boxes, enabling more customizable layout such as lining them up with grid or flex layout methods.
*   Explicit association requires the form control to have an `id`, which must be unique in the whole document. This is hard especially in a componentized application. Frameworks often provide their own solutions, such as React's [`useId()`](https://react.dev/reference/react/useId "External link (opens in new tab)")
    , but it still requires extra orchestration to get right.

Generally, we recommend using explicit association with the `for` attribute, to ensure compatibility with external tools and assistive technologies. In fact, you can simultaneously nest _and_ provide `id`/`for` for maximum compatibility.

The form control that a label is labeling is called the _labeled control_ of the label element. Multiple labels can be associated with the same form control:

html

    <label for="username">Enter your username:</label>
    <input id="username" name="username" type="text" />
    <label for="username">Forgot your username?</label>
    

Elements that can be associated with a `<label>` element include [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 (except for `type="hidden"`), [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
, [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
, [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#accessibility)

----------------------------------------------------------------------------------------------------------

### [Interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#interactive_content)

Other than the [implicitly associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#associating_a_label_with_a_form_control)
 form control, don't place additional interactive elements such as [anchors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 inside a `<label>`. Doing so makes it difficult for people to activate the form input associated with the `label`.

**Don't do this:**

html

    <label for="tac">
      <input id="tac" type="checkbox" name="terms-and-conditions" />
      I agree to the <a href="terms-and-conditions.html">Terms and Conditions</a>
    </label>
    

**Prefer this:**

html

    <p>
      <a href="terms-and-conditions.html">Read our Terms and Conditions</a>
    </p>
    <label for="tac">
      <input id="tac" type="checkbox" name="terms-and-conditions" />
      I agree to the Terms and Conditions
    </label>
    

**Note:** It is a good practice to place any necessary context, such as the link to the terms and conditions, before the form control, so that the user can read it before they interact with the control.

### [Headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#headings)

Placing [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 within a `<label>` interferes with many kinds of assistive technology, because headings are commonly used as [a navigation aid](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#navigation)
. If the label's text needs to be adjusted visually, use CSS classes applied to the `<label>` element instead.

If a [form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
, or a section of a form needs a title, use the [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 element placed within a [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
.

**Don't do this:**

html

    <label for="your-name">
      <h3>Your name</h3>
      <input id="your-name" name="your-name" type="text" />
    </label>
    

**Prefer this:**

html

    <label class="large-label" for="your-name">
      Your name
      <input id="your-name" name="your-name" type="text" />
    </label>
    

### [Buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#buttons)

An [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element with a `type="button"` declaration and a valid `value` attribute does not need a label associated with it. Doing so may actually interfere with how assistive technology parses the button input. The same applies for the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#examples)

------------------------------------------------------------------------------------------------

### [Defining an implicit label](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#defining_an_implicit_label)

html

    <label>Click me <input type="text" /></label>
    

### [Defining an explicit label with the "for" attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#defining_an_explicit_label_with_the_for_attribute)

html

    <label for="username">Click me to focus on the input field</label>
    <input type="text" id="username" />
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>, [form-associated element](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, but no descendant `label` elements. No [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)<br> elements other than the labeled control are allowed. |
| Tag omission | None, both the starting and ending tags are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLLabelElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-label-element](https://html.spec.whatwg.org/multipage/forms.html#the-label-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/label/index.md?plain=1 "Folder: en-us/web/html/reference/elements/label (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Flabel&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Flabel%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Flabel%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Flabel%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
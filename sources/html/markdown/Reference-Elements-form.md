*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#mdn-search)
    

`<form>` HTML form element
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<form>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a document section containing interactive controls for submitting information.

It is possible to use the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 to style a `<form>` element based on whether the [`elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements "elements")
 inside the form are valid.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#try_it)

-------------------------------------------------------------------------------------------

    <form action="" method="get" class="form-example">
      <div class="form-example">
        <label for="name">Enter your name: </label>
        <input type="text" name="name" id="name" required />
      </div>
      <div class="form-example">
        <label for="email">Enter your email: </label>
        <input type="email" name="email" id="email" required />
      </div>
      <div class="form-example">
        <input type="submit" value="Subscribe!" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    form.form-example {
      display: table;
    }
    
    div.form-example {
      display: table-row;
    }
    
    label,
    input {
      display: table-cell;
      margin-bottom: 10px;
    }
    
    label {
      padding-right: 10px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#accept)

Comma-separated [content types](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Content_type)
 the server accepts.

**Note:** **This attribute has been deprecated and should not be used.** Instead, use the [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#accept)
 attribute on `<input type=file>` elements.

[`accept-charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#accept-charset)

The [character encoding](https://developer.mozilla.org/en-US/docs/Glossary/Character_encoding)
 accepted by the server. The specification allows a single case-insensitive value of `"UTF-8"`, reflecting the ubiquity of this encoding (historically multiple character encodings could be specified as a comma-separated or space-separated list).

[`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#autocapitalize)

Controls whether inputted text is automatically capitalized and, if so, in what manner. See the [`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize)
 global attribute page for more information.

[`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)

Indicates whether input elements can by default have their values automatically completed by the browser. `autocomplete` attributes on form elements override it on `<form>`. Possible values:

*   `off`: The browser may not automatically complete entries. (Browsers tend to ignore this for suspected login forms; see [Managing autofill for login fields](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Turning_off_form_autocompletion#managing_autofill_for_login_fields)
    .)
*   `on`: The browser may automatically complete entries.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#name)

The name of the form. The value must not be the empty string, and must be unique among the `form` elements in the forms collection that it is in, if any. The name becomes a property of the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
, [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
, and [`document.forms`](https://developer.mozilla.org/en-US/docs/Web/API/Document/forms)
 objects, containing a reference to the form element.

[`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)

Controls the annotations and what kinds of links the form creates. Annotations include [`external`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#external)
, [`nofollow`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#nofollow)
, [`opener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#opener)
, [`noopener`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#noopener)
, and [`noreferrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#noreferrer)
. Link types include [`help`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#help)
, [`prev`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#prev)
, [`next`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#next)
, [`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#search)
, and [`license`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel#license)
. The [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
 value is a space-separated list of these enumerated values.

### [Attributes for form submission](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#attributes_for_form_submission)

The following attributes control behavior during form submission.

[`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)

The URL that processes the form submission. This value can be overridden by a [`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formaction)
 attribute on a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, or [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 element. This attribute is ignored when `method="dialog"` is set.

[`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)

If the value of the `method` attribute is `post`, `enctype` is the [MIME type](https://en.wikipedia.org/wiki/Mime_type "External link (opens in new tab)")
 of the form submission. Possible values:

*   `application/x-www-form-urlencoded`: The default value.
*   `multipart/form-data`: Use this if the form contains [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements with `type=file`.
*   `text/plain`: Useful for debugging purposes.

This value can be overridden by [`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formenctype)
 attributes on [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, or [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 elements.

[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#method)

The [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
 method to submit the form with. The only allowed methods/values are (case insensitive):

*   `post`: The [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
     method; form data sent as the [request body](https://developer.mozilla.org/en-US/docs/Web/API/Request/body)
    .
*   `get` (default): The [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET)
    ; form data appended to the `action` URL with a `?` separator. Use this method when the form [has no side effects](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)
    .
*   `dialog`: When the form is inside a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
    , closes the dialog and causes a `submit` event to be fired on submission, without submitting data or clearing the form.

This value is overridden by [`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formmethod)
 attributes on [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, or [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 elements.

[`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)

This Boolean attribute indicates that the form shouldn't be validated when submitted. If this attribute is not set (and therefore the form **_is_** validated), it can be overridden by a [`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formnovalidate)
 attribute on a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, or [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 element belonging to the form.

[`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#target)

Indicates where to display the response after submitting the form. It is a name/keyword for a _browsing context_ (for example, tab, window, or iframe). The following keywords have special meanings:

*   `_self` (default): Load into the same browsing context as the current one.
*   `_blank`: Load into a new unnamed browsing context. This provides the same behavior as setting [`rel="noopener"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#rel)
     which does not set [`window.opener`](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
    .
*   `_parent`: Load into the parent browsing context of the current one. If no parent, behaves the same as `_self`.
*   `_top`: Load into the top-level browsing context (i.e., the browsing context that is an ancestor of the current one and has no parent). If no parent, behaves the same as `_self`.
*   `_unfencedTop`: Load the response from a form inside an embedded [fenced frame](https://developer.mozilla.org/en-US/docs/Web/API/Fenced_frame_API)
     into the top-level frame (i.e., traversing beyond the root of the fenced frame, unlike other reserved destinations). Only available inside fenced frames.

This value can be overridden by a [`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formtarget)
 attribute on a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, or [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#examples)

-----------------------------------------------------------------------------------------------

html

    <!-- Form which will send a GET request to the current URL -->
    <form method="get">
      <label>
        Name:
        <input name="submitted-name" autocomplete="name" />
      </label>
      <button>Save</button>
    </form>
    
    <!-- Form which will send a POST request to the current URL -->
    <form method="post">
      <label>
        Name:
        <input name="submitted-name" autocomplete="name" />
      </label>
      <button>Save</button>
    </form>
    
    <!-- Form with fieldset, legend, and label -->
    <form method="post">
      <fieldset>
        <legend>Do you agree to the terms?</legend>
        <label><input type="radio" name="radio" value="yes" /> Yes</label>
        <label><input type="radio" name="radio" value="no" /> No</label>
      </fieldset>
    </form>
    

    document.querySelectorAll("form").forEach((form) => {
      form.addEventListener("submit", (event) => {
        event.preventDefault();
      });
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content) |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, but not containing `<form>` elements |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content) |
| Implicit ARIA role | `[form](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/form_role) ` |
| Permitted ARIA roles | `[search](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role) `, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br> or [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLFormElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-form-element](https://html.spec.whatwg.org/multipage/forms.html#the-form-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#see_also)

-----------------------------------------------------------------------------------------------

*   [HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   Other elements that are used when creating forms: [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
    , [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
    , [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    , [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
    , [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    , [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
    , [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
    , [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
    , [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    .
*   Getting a list of the elements in the form: [`HTMLFormElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
    
*   [ARIA: Form role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/form_role)
    
*   [ARIA: Search role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/form/index.md?plain=1 "Folder: en-us/web/html/reference/elements/form (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#mdn-search)
    

`<textarea>` HTML textarea element
==================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<textarea>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#try_it)

-----------------------------------------------------------------------------------------------

The above example demonstrates a number of features of `<textarea>`:

*   An `id` attribute to allow the `<textarea>` to be associated with a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
     element for accessibility purposes
*   A `name` attribute to set the name of the associated data point submitted to the server when the form is submitted.
*   `rows` and `cols` attributes to allow you to specify an exact size for the `<textarea>` to take. Setting these is a good idea for consistency, as browser defaults can differ.
*   The `<textarea>` element specifies its content differently in HTML and JavaScript contexts:
    *   In HTML, the initial content of a `<textarea>` is specified between its opening and closing tags, not as a `value` attribute.
    *   In JavaScript, `<textarea>` elements have a [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement/value)
         property that can be used to get or set the current content, and [`defaultValue`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement/defaultValue)
         to get and set its initial value (equivalent to accessing the HTML element's text content).

The `<textarea>` element also accepts several attributes common to form `<input>`s, such as `autocapitalize`, `autocomplete`, `autofocus`, `disabled`, `placeholder`, `readonly`, and `required`.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize)

Controls whether inputted text is automatically capitalized and, if so, in what manner.

[`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)

Controls whether entered text can be automatically completed by the browser. Possible values are:

*   `off`: The user must explicitly enter a value into this field for every use, or the document provides its own auto-completion method; the browser does not automatically complete the entry.
*   `on`: The browser can automatically complete the value based on values that the user has entered during previous uses.
*   [`<token-list>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#token_list_tokens)
    : An ordered set of space-separated autofill detail tokens, optionally preceded by a sectioning token, a billing or shipping grouping token, and/or a token identifying the type of recipient.

`<textarea>` elements that don't specify the `autocomplete` attribute inherit the `autocomplete` `on` or `off` status set on the `<textarea>`'s form owner. The form owner is either the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element that this `<textarea>` element is a descendant of or the form element whose `id` is specified by the `form` attribute of the input element. For more information, see the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#autocomplete)
 attribute in [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
.

[`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)

Controls whether automatic spelling correction and processing of text is enabled while the user is editing this `textarea`. Permitted values are:

[`on`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#on)

Enable automatic spelling correction and text substitutions.

[`off`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#off)

Disable automatic spelling correction and text substitutions.

[`autofocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autofocus)

This Boolean attribute lets you specify that a form control should have input focus when the page loads. Only one form-associated element in a document can have this attribute specified.

[`cols`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#cols)

The visible width of the text control, in average character widths. If it is specified, it must be a positive integer. If it is not specified, the default value is `20`.

[`dirname`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname)

This attribute is used to indicate the text directionality of the element contents. For more information, see the [`dirname` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

This Boolean attribute indicates that the user cannot interact with the control. If this attribute is not specified, the control inherits its setting from the containing element, for example [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
; if there is no containing element when the `disabled` attribute is set, the control is enabled.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

The form element that the `<textarea>` element is associated with (its "form owner"). The value of the attribute must be the `id` of a form element in the same document. If this attribute is not specified, the `<textarea>` element must be a descendant of a form element. This attribute enables you to place `<textarea>` elements anywhere within a document, not just as descendants of form elements.

[`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter. If this value isn't specified, the user can enter an unlimited number of characters.

[`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) required that the user should enter.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#name)

The name of the control.

[`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder)

A hint to the user of what can be entered in the control. Carriage returns or line-feeds within the placeholder text must be treated as line breaks when rendering the hint.

**Note:** Placeholders should only be used to show an example of the type of data that should be entered into a form; they are _not_ a substitute for a proper [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element tied to the input. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for a full explanation.

[`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)

This Boolean attribute indicates that the user cannot modify the value of the control. Unlike the `disabled` attribute, the `readonly` attribute does not prevent the user from clicking or selecting in the control. The value of a read-only control is still submitted with the form.

[`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)

This attribute specifies that the user must fill in a value before submitting a form.

[`rows`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#rows)

The number of visible text lines for the control. If it is specified, it must be a positive integer. If it is not specified, the default value is 2.

[`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)

Specifies whether the `<textarea>` is subject to spell-checking by the underlying browser/OS. The value can be:

*   `true`: Indicates that the element needs to have its spelling and grammar checked.
*   `default` : Indicates that the element is to act according to a default behavior, possibly based on the parent element's own `spellcheck` value.
*   `false` : Indicates that the element should not be spell-checked.

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#wrap)

Indicates how the control should wrap the value for form submission. Possible values are:

*   `hard`: The browser automatically inserts line breaks (CR+LF) so that each line is no longer than the width of the control; the [`cols`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#cols)
     attribute must be specified for this to take effect
*   `soft`: The browser ensures that all line breaks in the entered value are a `CR+LF` pair, but no additional line breaks are added to the value.
*   `off` : Like `soft` but changes appearance to `white-space: pre` so line segments exceeding `cols` are not wrapped and the `<textarea>` becomes horizontally scrollable.

If this attribute is not specified, `soft` is its default value.

[Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#styling_with_css)

-------------------------------------------------------------------------------------------------------------------

`<textarea>` is a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
 — it has intrinsic dimensions, like a raster image. By default, its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value is `inline-block`. Compared to other form elements it is relatively easy to style, with its box model, fonts, color scheme, etc. being easily manipulable using regular CSS.

[Styling HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
 provides some useful tips on styling `<textarea>`s.

### [Baseline inconsistency](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#baseline_inconsistency)

The HTML specification doesn't define where the baseline of a `<textarea>` is, so different browsers set it to different positions. For Gecko, the `<textarea>` baseline is set on the baseline of the first line of the textarea, on another browser it may be set on the bottom of the `<textarea>` box. Don't use [`vertical-align: baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 on it; the behavior is unpredictable.

### [Controlling whether a textarea is resizable](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#controlling_whether_a_textarea_is_resizable)

In most browsers, `<textarea>`s are resizable — you'll notice the drag handle in the right-hand corner, which can be used to alter the size of the element on the page. This is controlled by the [`resize`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize)
 CSS property — resizing is enabled by default, but you can explicitly disable it using a `resize` value of `none`:

### [Styling valid and invalid values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#styling_valid_and_invalid_values)

Valid and invalid values of a `<textarea>` element (e.g., those within, and outside the bounds set by `minlength`, `maxlength`, or `required`) can be highlighted using the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 pseudo-classes. For example, to give your textarea a different border depending on whether it is valid or invalid:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#examples)

---------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#basic_example)

The following example shows a textarea with a set number of rows and columns, some default content, and CSS styles that prevent users from resizing the element more than 500px wide and 130px high:

#### Result

### [Example using "minlength" and "maxlength"](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#example_using_minlength_and_maxlength)

This example has a minimum and maximum number of characters — of 10 and 20 respectively. Try it and see.

#### Result

Note that `minlength` doesn't stop the user from removing characters so that the number entered goes past the minimum, but it does make the value entered into the `<textarea>` invalid. Also note that even if you have a `minlength` value set (3, for example), an empty `<textarea>` is still considered valid unless you also have the `required` attribute set.

### [Example using "placeholder"](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#example_using_placeholder)

This example has a placeholder set. Notice how it disappears when you start typing into the box.

#### Result

**Note:** Placeholders should only be used to show an example of the type of data that should be entered into a form; they are _not_ a substitute for a proper [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element tied to the input. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for a full explanation.

### [Disabled and readonly text areas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#disabled_and_readonly_text_areas)

This example shows two `<textarea>`s — one is [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 and one is [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)
. You cannot edit the contents of either element, but the `readonly` element is focusable and its value is submitted in forms. The `disabled` element's value is not submitted and it's not focusable.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [Interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>, [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)<br>, [resettable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#resettable)<br>, and [submittable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#submittable)<br> [form-associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br> element. |
| Permitted content | Text |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLTextAreaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-textarea-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#see_also)

---------------------------------------------------------------------------------------------------

*   Other form-related elements:
    *   [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
        
    *   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
        
    *   [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
        
    *   [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
        
    *   [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
        
    *   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
        
    *   [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
        
    *   [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
        
    *   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
        
    *   [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
        
    *   [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
        
    *   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
        
    *   [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/textarea/index.md?plain=1 "Folder: en-us/web/html/reference/elements/textarea (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftextarea&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftextarea%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftextarea%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftextarea%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#mdn-search)
    

`<button>` HTML button element
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<button>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is an interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it then performs an action, such as submitting a [form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
 or opening a dialog.

By default, HTML buttons are presented in a style resembling the platform the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 runs on, but you can change buttons' appearance with [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#try_it)

---------------------------------------------------------------------------------------------

    <button class="favorite styled" type="button">Add to favorites</button>
    

    .styled {
      border: 0;
      line-height: 2.5;
      padding: 0 20px;
      font-size: 1rem;
      text-align: center;
      color: white;
      text-shadow: 1px 1px 1px black;
      border-radius: 10px;
      background-color: tomato;
      background-image: linear-gradient(
        to top left,
        rgb(0 0 0 / 0.2),
        rgb(0 0 0 / 0.2) 30%,
        transparent
      );
      box-shadow:
        inset 2px 2px 3px rgb(255 255 255 / 0.6),
        inset -2px -2px 3px rgb(0 0 0 / 0.6);
    }
    
    .styled:hover {
      background-color: red;
    }
    
    .styled:active {
      box-shadow:
        inset -2px -2px 3px rgb(255 255 255 / 0.6),
        inset 2px 2px 3px rgb(0 0 0 / 0.6);
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#attributes)

-----------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`autofocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#autofocus)

This Boolean attribute specifies that the button should have input [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus)
 when the page loads. **Only one element in a document can have this attribute.**

[`command`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#command)

Specifies the action to be performed on an element being controlled by a control `<button>` specified via the `commandfor` attribute. The possible values are:

[`"show-modal"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#show-modal)

The button will show a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 as modal. If the dialog is already modal, no action will be taken. This is a declarative equivalent of calling the [`HTMLDialogElement.showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal)
 method on the `<dialog>` element.

[`"close"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#close)

The button will close a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element. If the dialog is already closed, no action will be taken. This is a declarative equivalent of calling the [`HTMLDialogElement.close()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close)
 method on the `<dialog>` element. When used with the `value` attribute, the button's value will be passed as the dialog's [`returnValue`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/returnValue "returnValue")
 property.

[`"request-close"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#request-close)

The button will trigger a [`cancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/cancel_event "cancel")
 event on a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element to request that the browser dismiss it, followed by a [`close`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event "close")
 event. This differs from the `close` command in that authors can call [`Event.preventDefault()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
 on the `cancel` event to prevent the `<dialog>` from closing. If the dialog is already closed, no action will be taken. This is a declarative equivalent of calling the [`HTMLDialogElement.requestClose()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/requestClose)
 method on the `<dialog>` element. When used with the button's `value` attribute, the value will be passed as the dialog's `returnValue` property.

[`"show-popover"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#show-popover)

The button will show a hidden popover. If you try to show an already showing popover, no action will be taken. See [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
 for more details. This is equivalent to setting a value of `show` for the [`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)
 attribute, and also provides a declarative equivalent to calling the [`HTMLElement.showPopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover)
 method on the popover element.

[`"hide-popover"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#hide-popover)

The button will hide a showing popover. If you try to hide an already hidden popover, no action will be taken. See [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
 for more details. This is equivalent to setting a value of `hide` for the [`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)
 attribute, and also provides a declarative equivalent to calling the [`HTMLElement.hidePopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidePopover)
 method on the popover element.

[`"toggle-popover"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#toggle-popover)

The button will toggle a popover between showing and hidden. If the popover is hidden, it will be shown; if the popover is showing, it will be hidden. See [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
 for more details. This is equivalent to setting a value of `toggle` for the [`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)
 attribute, and also provides a declarative equivalent to calling the [`HTMLElement.togglePopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/togglePopover)
 method on the popover element.

[Custom values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#custom_values)

This attribute can represent custom values that are prefixed with a two hyphen characters (`--`). Buttons with a custom value will dispatch the [`CommandEvent`](https://developer.mozilla.org/en-US/docs/Web/API/CommandEvent)
 on the controlled element.

[`commandfor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#commandfor)

Turns a `<button>` element into a command button, controlling a given interactive element by issuing the command specified in the button's [`command`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#command)
 attribute. The `commandfor` attribute takes the ID of the element to control as its value. This is a more general version of [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

This Boolean attribute prevents the user from interacting with the button: it cannot be pressed or focused.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

The [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element to associate the button with (its _form owner_). The value of this attribute must be the `id` of a `<form>` in the same document. (If this attribute is not set, the `<button>` is associated with its ancestor `<form>` element, if any.)

This attribute lets you associate `<button>` elements to `<form>`s anywhere in the document, not just inside a `<form>`. It can also override an ancestor `<form>` element.

[`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formaction)

The URL that processes the information submitted by the button. Overrides the [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute of the button's form owner. Does nothing if there is no form owner.

[`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formenctype)

If the button is a submit button (it's inside/associated with a `<form>` and doesn't have `type="button"`), specifies how to encode the form data that is submitted. Possible values:

*   `application/x-www-form-urlencoded`: The default if the attribute is not used.
*   `multipart/form-data`: Used to submit [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements with their [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
     attributes set to `file`.
*   `text/plain`: Specified as a debugging aid; shouldn't be used for real form submission.

If this attribute is specified, it overrides the [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute of the button's form owner.

[`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formmethod)

If the button is a submit button (it's inside/associated with a `<form>` and doesn't have `type="button"`), this attribute specifies the [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
 used to submit the form. Possible values:

*   `post`: The data from the form are included in the body of the HTTP request when sent to the server. Use when the form contains information that shouldn't be public, like login credentials.
*   `get`: The form data are appended to the form's `action` URL, with a `?` as a separator, and the resulting URL is sent to the server. Use this method when the form [has no side effects](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)
    , like search forms.
*   `dialog`: This method is used to indicate that the button closes the [dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     with which it is associated, and does not transmit the form data at all.

If specified, this attribute overrides the [`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#method)
 attribute of the button's form owner.

[`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formnovalidate)

If the button is a submit button, this Boolean attribute specifies that the form is not to be [validated](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
 when it is submitted. If this attribute is specified, it overrides the [`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)
 attribute of the button's form owner.

This attribute is also available on [`<input type="image">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 and [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 elements.

[`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#formtarget)

If the button is a submit button, this attribute is an author-defined name or standardized, underscore-prefixed keyword indicating where to display the response from submitting the form. This is the `name` of, or keyword for, a _browsing context_ (a tab, window, or [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
). If this attribute is specified, it overrides the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#target)
 attribute of the button's form owner. The following keywords have special meanings:

*   `_self`: Load the response into the same browsing context as the current one. This is the default if the attribute is not specified.
*   `_blank`: Load the response into a new unnamed browsing context — usually a new tab or window, depending on the user's browser settings.
*   `_parent`: Load the response into the parent browsing context of the current one. If there is no parent, this option behaves the same way as `_self`.
*   `_top`: Load the response into the top-level browsing context (that is, the browsing context that is an ancestor of the current one, and has no parent). If there is no parent, this option behaves the same way as `_self`.

[`interestfor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#interestfor)

Defines the `<button>` element as an **interest invoker**. Its value is the `id` of a target element, which will be affected in some way (normally shown or hidden) when interest is shown or lost on the invoker element (for example, by hovering/unhovering or focusing/blurring it). See [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 for more details and examples.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#name)

The name of the button, submitted as a pair with the button's `value` as part of the form data, when that button is used to submit the form.

[`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)

Turns a `<button>` element into a popover control button; takes the ID of the popover element to control as its value. Establishing a relationship between a popover and its invoker button using the `popovertarget` attribute has two additional useful effects:

*   The browser creates an implicit [`aria-details`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-details)
     and [`aria-expanded`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-expanded)
     relationship between popover and invoker, and places the popover in a logical position in the keyboard focus navigation order when shown. This makes the popover more accessible to keyboard and assistive technology (AT) users (see also [Popover accessibility features](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_accessibility_features)
    ).
*   The browser creates an implicit anchor reference between the two, making it very convenient to position popovers relative to their controls using [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
    . See [Popover anchor positioning](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_anchor_positioning)
     for more details.

[`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertargetaction)

Specifies the action to be performed on a popover element being controlled by a control `<button>`. Possible values are:

[`"hide"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#hide)

The button will hide a shown popover. If you try to hide an already hidden popover, no action will be taken.

[`"show"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#show)

The button will show a hidden popover. If you try to show an already showing popover, no action will be taken.

[`"toggle"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#toggle)

The button will toggle a popover between showing and hidden. If the popover is hidden, it will be shown; if the popover is showing, it will be hidden. If `popovertargetaction` is omitted, `"toggle"` is the default action that will be performed by the control button.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#type)

The default behavior of the button. Possible values are:

*   `submit`: The button submits the form data to the server. This is the default if the attribute is not specified for buttons associated with a `<form>`, or if the attribute is an empty or invalid value.
*   `reset`: The button resets all the controls to their initial values, like [<input type="reset">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
    . (This behavior tends to annoy users.)
*   `button`: The button has no default behavior, and does nothing when pressed by default. It can have client-side scripts listen to the element's events, which are triggered when the events occur.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#value)

Defines the value associated with the button's `name` when it's submitted with the form data. This value is passed to the server in params when the form is submitted using this button. When used with the `close` or `request-close` commands, the `value` attribute sets the [`returnValue`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/returnValue "returnValue")
 of the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element being controlled.

[Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#notes)

-------------------------------------------------------------------------------------------

A submit button with the attribute `formaction` set, but without an associated form does nothing. You have to set a form owner, either by wrapping it in a `<form>` or set the attribute `form` to the id of the form.

`<button>` elements are much easier to style than [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. You can add inner HTML content (think `<i>`, `<br>`, or even `<img>`), and use [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 and [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-elements for complex rendering.

If your buttons are not for submitting form data to a server, be sure to set their `type` attribute to `button`. Otherwise, they will try to submit form data and to load the (nonexistent) response, possibly destroying the current state of the document.

While `<button type="button">` has no default behavior, event handlers can be scripted to trigger behaviors. An activated button can perform programmable actions using [JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)
, such as removing an item from a list.

By default, user agents style buttons as `display: flow-root`, which establishes a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 and centers the button's children both horizontally and vertically as long as they do not overflow. If the button is defined as a flex or grid container, the children will behave as flex or grid items. A button set to `display: inline` will be styled as if the value were set to `display: inline-block`.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#accessibility)

-----------------------------------------------------------------------------------------------------------

### [Icon buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#icon_buttons)

Buttons that only display an icon do not have an _[accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
_. Accessible names provide information for assistive technology, such as screen readers, to access when they parse the document and generate [an accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
. Assistive technology then uses the accessibility tree to navigate and manipulate page content.

To give an icon button an accessible name, put text in the `<button>` element that concisely describes the button's functionality.

#### Examples

html

    <button name="favorite">
      <svg fill="black" viewBox="0 0 42 42">
        <path
          d="M21,1c1.081,0,5.141,12.315,6.201,13.126s13.461,1.053,13.791,2.137 c0.34,1.087-9.561,8.938-9.961,10.252c-0.409,1.307,
          3.202,13.769,2.331,14.442c-0.879,0.673-11.05-6.79-12.361-6.79 c-1.311,0-11.481,7.463-12.36,6.79c-0.871-0.674,2.739-13.136,
          2.329-14.442c-0.399-1.313-10.3-9.165-9.96-10.252 c0.33-1.084,12.731-1.326,13.791-2.137S19.91,1,21,1z"></path>
      </svg>
      Add to favorites
    </button>
    

##### Result

If you want to visually hide the button's text, an accessible way to do so is to use [a combination of CSS properties](https://www.a11yproject.com/posts/how-to-hide-content/ "External link (opens in new tab)")
 to remove it visually from the screen, but keep it parsable by assistive technology.

However, it is worth noting that leaving the button text visible can help people who may not be familiar with the icon's meaning or understand the button's purpose. This is especially important for people who are not technologically sophisticated or who may have different cultural interpretations of the icon the button uses.

*   [What is an accessible name? | Vispero](https://vispero.com/resources/what-is-an-accessible-name/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 4.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Robust#guideline_4.1_%E2%80%94_compatible_maximize_compatibility_with_current_and_future_user_agents_including_assistive_technologies)
    
*   [Understanding Success Criterion 4.1.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/ensure-compat-rsv.html "External link (opens in new tab)")
    

### [Size and Proximity](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#size_and_proximity)

#### Size

Interactive elements such as buttons should have an area large enough to be easy to activate. This helps a variety of people, including people with motor control issues and people using non-precise forms of input such as a stylus or fingers. A minimum interactive size of 44×44 [CSS pixels](https://developer.mozilla.org/en-US/docs/Glossary/CSS_pixel)
 is recommended.

*   [Understanding Success Criterion 2.5.5: Target Size | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html "External link (opens in new tab)")
    
*   [Target Size and 2.5.5 | Adrian Roselli](https://adrianroselli.com/2019/06/target-size-and-2-5-5.html "External link (opens in new tab)")
    
*   [Quick test: Large touch targets - The A11Y Project](https://www.a11yproject.com/posts/large-touch-targets/ "External link (opens in new tab)")
    

#### Proximity

Large amounts of interactive content — including buttons — placed in close visual proximity to each other should have space separating them. This spacing is beneficial for people who are experiencing motor control issues, who may accidentally activate the wrong interactive content.

Spacing may be created using CSS properties such as [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
.

*   [Hand tremors and the giant-button-problem - Axess Lab](https://axesslab.com/hand-tremors/ "External link (opens in new tab)")
    

### [ARIA state information](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#aria_state_information)

To describe the state of a button the correct ARIA attribute to use is [`aria-pressed`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-pressed)
 and not [`aria-checked`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-checked)
 or [`aria-selected`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-selected)
. To find out more read the information about the [ARIA button role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role)
.

### [Button styles](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#button_styles)

It is best not to override the default focus ring for elements that have focus. If the button styles are overridden, it is important to **ensure that the focus state has enough contrast** so that people experiencing low vision conditions can perceive it and people with cognitive differences will understand it.

The [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
 pseudo-class can be used to apply styles to an element that has [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 only when the user agent's heuristics determine that the focus should be highlighted, such as when a `<button>` receives keyboard focus. See [:focus vs :focus-visible](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible#focus_vs_focus-visible)
 for more information.

Color contrast ratio is determined by comparing the luminosity of the button text and background color values to the background the button is placed on. To meet current [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, a ratio of 4.5:1 is required for text content and 3:1 for large text. (Large text is defined as 18.66px and [`bold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 or larger, or 24px or larger.)

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.3 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    

### [Clicking and focus](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#clicking_and_focus)

Whether clicking on a `<button>` or [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 button types causes it to (by default) become focused varies by browser and OS. Most browsers do give focus to a button being clicked, but [Safari does not, by design](https://webkit.org/b/22261#c68 "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#examples_2)

---------------------------------------------------------------------------------------------------

### [Creating a basic button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#creating_a_basic_button)

This example creates a clickable button. The `type="button"` attribute ensures the button has no default behavior. You can make this button interactive using JavaScript or attributes such as `command` and `commandfor`.

html

    <button type="button" name="button">I'm a button</button>
    

### [Using the `request-close` value for the `command` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#using_the_request-close_value_for_the_command_attribute)

The dialog in this example has two radio buttons that control whether or not the dialog can be closed. Select **Yes** or **No**, and then click **Request to Close** to try to close the dialog. If **Yes** is selected, the dialog closes; if **No** is selected, the dialog stays open and shows a message instead.

html

    <button type="button" commandfor="mydialog" command="show-modal">
      Open Dialog
    </button>
    <dialog id="mydialog">
      <div class="wrapper">
        <form>
          <fieldset>
            <legend>Allow this dialog to close when requested?</legend>
            <div>
              <input type="radio" id="no" name="close" value="no" checked />
              <label for="no">No</label>
            </div>
            <div>
              <input type="radio" id="yes" name="close" value="yes" />
              <label for="yes">Yes</label>
            </div>
          </fieldset>
        </form>
        <button commandfor="mydialog" command="request-close">
          Request to Close
        </button>
        <p class="warning" hidden>You must choose "Yes" to close this dialog.</p>
      </div>
    </dialog>
    

    .warning {
      color: tomato;
    }
    

js

    const dialog = document.querySelector("dialog");
    const radio = document.querySelector("form").elements["close"];
    const warning = document.querySelector(".warning");
    
    dialog.addEventListener("cancel", (e) => {
      if (!e.cancelable) return;
      if (radio.value === "no") {
        warning.hidden = false;
        e.preventDefault();
      } else {
        warning.hidden = true;
      }
    });
    

The **Open Dialog** button opens the `<dialog>` element using `command="show-modal"`.

The **Request to Close** button has `command="request-close"`, which targets the `<dialog>` element using the `commandfor="mydialog"` attribute. When it's clicked, it asks the `<dialog>` if it can be closed (unlike the `command="close"` attribute, which would close the `<dialog>` immediately). This checks if the `<dialog>` is [`cancelable`](https://developer.mozilla.org/en-US/docs/Web/API/Event/cancelable)
 using a `cancel` event.

When the event is `cancelable`, the value of the radio buttons is checked:

*   If set to `yes`, the dialog is closed.
*   If set to `no`, the `hidden` attribute is turned off on the warning and the [`preventDefault()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)
     method is called, which prevents the default `<dialog>` closing behavior.

### [Using the `value` attribute with dialog `close` command](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#using_the_value_attribute_with_dialog_close_command)

This example demonstrates how to use the button `value` attribute with `close` command to populate the value of a dialog's [`returnValue`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/returnValue "returnValue")
 property.

When either the **Cancel** or **Delete** button is clicked, the dialog closes and sets its `returnValue` to the button's `value` attribute. The `close` event listener checks `dialog.returnValue` to determine which action the user chose and logs the result to the screen.

#### HTML

The HTML first defines a **Delete Record** button that uses the `commandfor` attribute to specify the dialog to be opened.

Within the dialog **Cancel** and **Delete** buttons use the `commandfor` attribute to indicate that they apply to the current dialog. They also set the `command` attribute to "close" and set the `value` attribute to "cancel" and "delete" respectively — the value of the selected button is automatically copied to the dialog `returnValue` when the button is clicked.

html

    <button commandfor="confirm-dialog" command="show-modal">Delete Record</button>
    <dialog id="confirm-dialog">
      <header>
        <h1>Delete Record?</h1>
      </header>
      <p>Are you sure? This action cannot be undone</p>
      <footer>
        <button commandfor="confirm-dialog" command="close" value="cancel">
          Cancel
        </button>
        <button commandfor="confirm-dialog" command="close" value="delete">
          Delete
        </button>
      </footer>
    </dialog>
    

html

    <pre id="log"></pre>
    

    #log {
      height: 20px;
    }
    

    const logElement = document.querySelector("#log");
    function log(text) {
      logElement.innerText = text;
    }
    

#### JavaScript

The code uses a `close` event listener to log the dialog's `returnValue`.

js

    const dialog = document.getElementById("confirm-dialog");
    
    dialog.addEventListener("close", () => {
      switch (dialog.returnValue) {
        case "cancel":
          log("Cancel was clicked");
          break;
        case "delete":
          log("Delete was clicked");
          break;
        default:
          log("Closed with value:", dialog.returnValue);
      }
    });
    

#### Results

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [Interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>, [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)<br>, and [submittable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#submittable)<br> [form-associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br> element, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br> but there must be no [Interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>. If the `<button>` is the first child of a [customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)<br>, then it may also contain zero or one [`<selectedcontent>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent)<br> element. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) ` |
| Permitted ARIA roles | [`checkbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role)<br>, [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>, [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br>, [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>, [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>, [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>, [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>, [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>, [`switch`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role)<br>, [`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role) |
| DOM interface | [`HTMLButtonElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-button-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-button-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/button/index.md?plain=1 "Folder: en-us/web/html/reference/elements/button (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbutton&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbutton%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbutton%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbutton%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
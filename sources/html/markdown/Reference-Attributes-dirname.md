*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#mdn-search)
    

`dirname` HTML attribute
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`dirname`** attribute can be used on the [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element and several [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types and describes the directionality of the element's text content during form submission. The browser uses this attribute's value to determine whether text the user has entered is left-to-right or right-to-left oriented. When used, the element's text directionality value is included in form submission data along with the `dirname` attribute's value as the name of the field.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#usage_notes)

----------------------------------------------------------------------------------------------------------

The `dirname` attribute can be used on any [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element, or any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element with [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
, [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, [search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
, [tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
, [url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
, [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
, [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
, [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
 or [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
 type.

The format of the submitted data is `{dirname_value}={direction}` where `{dirname_value}` is the value of the `dirname` attribute and `{direction}` is the directionality of the text. For example, if the user enters "Hello" in an element with the attributes `name="comment"` and `dirname="comment-direction"`, the URL-encoded form submission data for `GET` requests will be `comment=Hello&comment-direction=ltr`. The directionality is one of the following:

[`rtl`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#rtl)

The text entered by the user is in a right-to-left writing direction.

[`ltr`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#ltr)

The text entered by the user is in a left-to-right writing direction.

If no text directionality is specified, the user agent will use the directionality of the parent element containing the form, and if that is not specified, the default directionality of the user agent.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#examples)

----------------------------------------------------------------------------------------------------

### [Textarea element directionality](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#textarea_element_directionality)

In this example, the `dir="auto"` attribute on the textarea element allows the text directionality to be determined automatically based on the text entered by the user:

When the user submits the form, the user agent includes two fields, one called `comment` with the value "سيب", and one called `comment-direction` with the value "rtl". The URL-encoded submission body looks like this:

### [Input element directionality](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#input_element_directionality)

In this example, the `dir="auto"` attribute on the input element allows the text directionality to be determined automatically based on the text entered by the user:

When the user submits the form, the user agent includes two fields, one called `comment-input` with the value "Hello", and one called `comment-direction` with the value "ltr":

### [Inheriting directionality](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#inheriting_directionality)

The following `<input>` and `<textarea>` elements do not have a `dir` attribute, so they inherit the explicit directionality of their parent element, which is `rtl`:

The URL-encoded submission body looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-fe-dirname](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-dirname) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

### [html.elements.textarea.dirname](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#html.elements.textarea.dirname)

### [html.elements.input.dirname](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#html.elements.input.dirname)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname#see_also)

----------------------------------------------------------------------------------------------------

*   [`dir` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/dirname/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/dirname (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fdirname&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fdirname%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fdirname%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fdirname%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
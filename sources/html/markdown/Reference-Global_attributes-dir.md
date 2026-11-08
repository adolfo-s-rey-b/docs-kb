*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#mdn-search)
    

`dir` HTML global attribute
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`dir`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that sets the element's _base text direction_ and directionally isolates its contents from surrounding text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#try_it)

---------------------------------------------------------------------------------------------------

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#values)

---------------------------------------------------------------------------------------------------

It can have the following values:

*   `ltr`, which sets a _left-to-right_ base direction;
*   `rtl`, which sets a _right-to-left_ base direction;
*   `auto`, which lets the user agent determine the base direction from the text, generally using the first character with a strong directionality (skipping `<bdi>`, `<script>`, `<style>`, `<textarea>`, and elements with valid `dir` attributes). For [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     and [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
    , the rendering direction is determined separately for each paragraph of text.

**Note:** The `auto` value should be used for data with an unknown directionality, like data coming from user input or external data.

If the [`dirname`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname)
 attribute is used when users submit input, it may be possible to render the data with a specified directionality instead of relying on automatic detection.

If unspecified or invalid, the direction is generally [inherited](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#inheritance)
 from the parent element. Omitting `dir` does not enable automatic direction detection.

### [Inheritance](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#inheritance)

If an element has no `dir` attribute, it generally inherits the direction of its [parent element](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement)
, or the [`host`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/host "host")
 if the parent node is a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
. If no ancestor sets a direction, the default is left-to-right.

There are exceptions:

*   A [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
     element determines its direction from its content, as if `dir="auto"` were set.
*   An [`<input type="tel">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
     element uses left-to-right direction.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#usage_notes)

-------------------------------------------------------------------------------------------------------------

The base direction is used by the Unicode Bidirectional Algorithm ([BiDi](https://developer.mozilla.org/en-US/docs/Glossary/BiDi)
). While characters strongly typed as LTR or RTL (such as Latin, Hebrew, or Arabic letters) establish directionality for themselves and all neutral characters in between (creating "runs" of text), the base direction is necessary in two scenarios:

*   It is assumed by neutral characters (like spaces or punctuation) at the boundaries of runs of text with different directionalities, often including at the very beginnings or ends.
*   It is used to order runs of text.

For example, consider the first English paragraph in the [Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#try_it)
 demo. There are two runs of text: the English text (LTR due to the Latin characters) and the final period (which is at the end of the `p` element, so assumes the base direction RTL). These runs of text are laid out right-to-left, so the text appears first on the right edge, followed to its left by the period. Similarly, the first Arabic paragraph inherits the LTR base direction from the HTML document, so the RTL Arabic text appears on the left edge, followed to its right by the period (with LTR direction). Both paragraphs are typographically incorrect.

Even for documents in a single script, it is recommended to explicitly set `dir` on the root element, which is especially important for RTL scripts, because the default LTR base direction is wrong. The [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute declares the language, but does not imply the base direction.

This attribute can be overridden by the CSS properties [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 and [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
, if a CSS page is active and the element supports these properties.

As the directionality of the text is semantically related to its content and not to its presentation, it is recommended that web developers use this attribute instead of the related CSS properties when possible. That way, the text will display correctly even on a browser that doesn't support CSS or has the CSS deactivated.

An image can have its `dir` property set to `"rtl"` in which case the HTML attributes `title` and `alt` will be formatted and defined as `"rtl"`.

When a table has its `dir` set to `"rtl"`, the column order is arranged from right to left.

The [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
 element requires `dir="ltr"` or `dir="rtl"`. On this element, the attribute overrides the characters' intrinsic directionality instead of only setting a base direction.

Browsers might allow users to change the directionality of [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements in order to assist with authoring content. Chrome and Safari provide a directionality option in the contextual menu of input fields. Firefox uses Ctrl (Windows)/Cmd (macOS) + Shift + X inside a `<textarea>` to toggle text direction. These features toggle the `dir` attribute value between `ltr` and `rtl`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#examples)

-------------------------------------------------------------------------------------------------------

### [Setting document-level direction](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#setting_document-level_direction)

Set `dir="rtl"` on the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element when the page is predominantly written in a right-to-left script, such as Arabic or Hebrew. Use `dir` on a block within the page when that block needs a different base direction.

In this Arabic document, the English paragraph needs both `dir="ltr"` and `lang="en"`.

### [Setting text direction explicitly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#setting_text_direction_explicitly)

This example explicitly sets the base direction of two paragraphs. The base direction affects the default alignment and the placement of punctuation.

### [Inline bidirectional text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#inline_bidirectional_text)

When an inline phrase has a different base direction from the surrounding text, tightly wrap the whole phrase in an element with the appropriate `dir` value. This also isolates the phrase's direction from its surroundings, so punctuation and numbers outside it are not treated as part of the phrase. Use an existing semantic element, such as [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
 for a book title, or a [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
 if no other element is appropriate.

Note that the exclamation mark, a part of the title, is inside the `<cite>` element. If outside, it will adopt the base direction and therefore appear on the left edge of the title.

### [Using dir="auto" for user-generated content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#using_dirauto_for_user-generated_content)

When the direction of text is not known in advance, such as for user comments, use `dir="auto"`. The browser uses the first strongly directional character to determine the element's base direction. This is a heuristic, not language detection: a comment that starts with an English name and continues in Arabic will get a left-to-right base direction. Use an explicit direction when it is known.

Here, the paragraphs represent two possible comments. The comments are written by users, so the site is not aware of their languages during rendering.

The [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
 element offers the same effect, and is terser for inline isolation, especially when no semantic element is appropriate.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-dir-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir#see_also)

-------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`HTMLElement.dir`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dir)
     that reflects this attribute.
*   [Handling different text directions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions)
    
*   [Creating HTML pages in Arabic, Hebrew and other right-to-left scripts](https://www.w3.org/International/tutorials/bidi-xhtml/index.en.html "External link (opens in new tab)")
     on w3.org

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/dir/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/dir (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdir&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdir%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fdir%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fdir%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ed465762d06fa17f7cc6adb3e2be9b57df03e9b%0A*+Document+last+modified%3A+2026-09-08T07%3A38%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
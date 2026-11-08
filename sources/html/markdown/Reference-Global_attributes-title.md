*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#mdn-search)
    

`title` HTML global attribute
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`title`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 contains text representing advisory information related to the element it belongs to.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#try_it)

-----------------------------------------------------------------------------------------------------

    <p>
      Use the <code>title</code> attribute on an <code>iframe</code> to clearly
      identify the content of the <code>iframe</code> to screen readers.
    </p>
    
    <iframe
      title="Wikipedia page for the HTML language"
      src="https://en.m.wikipedia.org/wiki/HTML"></iframe>
    <iframe
      title="Wikipedia page for the CSS language"
      src="https://en.m.wikipedia.org/wiki/CSS"></iframe>
    

    iframe {
      height: 200px;
      margin-bottom: 24px;
      width: 100%;
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#description)

---------------------------------------------------------------------------------------------------------------

The main use of the `title` attribute is to label [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 elements for assistive technology.

The `title` attribute may also be used to label controls in [data tables](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
.

The `title` attribute, when added to [`<link rel="stylesheet">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
, creates an alternate stylesheet. When defining an alternative style sheet with `<link rel="alternate">` the attribute is required and must be set to a non-empty string.

If included on the [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
 opening tag, the `title` must be a full expansion of the abbreviation or acronym. Instead of using `title`, when possible, provide an expansion of the abbreviation or acronym in plain text on first use, using the `<abbr>` to mark up the abbreviation. This enables all users know what name or term the abbreviation or acronym shortens while providing a hint to user agents on how to announce the content.

While `title` can be used to provide a programmatically associated label for an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element, this is not good practice. Use a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 instead.

[Multiline titles](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#multiline_titles)

-------------------------------------------------------------------------------------------------------------------------

The `title` attribute may contain several lines. Each `U+000A LINE FEED` (`LF`) character represents a line break. Some caution must be taken, as this means the following renders across two lines:

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#html)

html

    <p>
      Newlines in <code>title</code> should be taken into account. This
      <span
        title="This is a
    multiline title">
        example span
      </span>
      has a title attribute with a newline.
    </p>
    <hr />
    <pre id="output"></pre>
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#javascript)

We can query the `title` attribute and display it in the empty `<pre>` element as follows:

js

    const span = document.querySelector("span");
    const output = document.querySelector("#output");
    output.textContent = span.title;
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#result)

[Title attribute inheritance](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#title_attribute_inheritance)

-----------------------------------------------------------------------------------------------------------------------------------------------

If an element has no `title` attribute, then it inherits it from its parent node, which in turn may inherit it from its parent, and so on.

If this attribute is set to the empty string, it means its ancestors' `title`s are irrelevant and shouldn't be used in the tooltip for this element.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#html_2)

html

    <div title="CoolTip">
      <p>Hovering here will show "CoolTip".</p>
      <p title="">Hovering here will show nothing.</p>
    </div>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#result_2)

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#accessibility_concerns)

-------------------------------------------------------------------------------------------------------------------------------------

Use of the `title` attribute is highly problematic for:

*   People using touch-only devices
*   People navigating with keyboards
*   People navigating with assistive technology such as screen readers or magnifiers
*   People experiencing fine motor control impairment
*   People with cognitive concerns

This is due to inconsistent browser support, compounded by the additional assistive technology parsing of the browser-rendered page. If a tooltip effect is desired, it is better to [use a more accessible technique](https://inclusive-components.design/tooltips-toggletips/ "External link (opens in new tab)")
 that can be accessed with the above browsing methods.

*   [3.2.5.1. The title attribute | W3C HTML 5.2: 3. Semantics, structure, and APIs of HTML documents](https://html.spec.whatwg.org/multipage/dom.html#the-title-attribute "External link (opens in new tab)")
    
*   [Using the HTML title attribute – updated | Vispero](https://vispero.com/resources/using-the-html-title-attribute-updated/ "External link (opens in new tab)")
    
*   [Tooltips & Toggletips - Inclusive Components](https://inclusive-components.design/tooltips-toggletips/ "External link (opens in new tab)")
    
*   [The Trials and Tribulations of the Title Attribute - 24 Accessibility](https://www.24a11y.com/2017/the-trials-and-tribulations-of-the-title-attribute/ "External link (opens in new tab)")
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-title-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-title-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title#see_also)

---------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`HTMLElement.title`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/title)
     that reflects this attribute.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/title/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/title (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Ftitle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Ftitle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Ftitle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Ftitle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcb7d4dde9f0a43664c64587d9d70b8835286eb7%0A*+Document+last+modified%3A+2026-10-01T19%3A41%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
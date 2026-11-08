*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#mdn-search)
    

`<center>` HTML centered text element
=====================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<center>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is a [block-level element](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
 that displays its block-level or inline contents centered horizontally within its containing element. The container is usually, but isn't required to be, [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
.

This tag has been deprecated in HTML 4 (and XHTML 1) in favor of the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 property, which can be applied to the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element or to an individual [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
. For centering blocks, use other CSS properties like [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 and [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
 and set them to `auto` (or set [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 to `0 auto`).

[DOM interface](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#dom_interface)

-----------------------------------------------------------------------------------------------------------

This element implements the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface.

[Example 1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#example_1)

---------------------------------------------------------------------------------------------------

html

    <center>
      This text will be centered.
      <p>So will this paragraph.</p>
    </center>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#result)

[Example 2 (CSS alternative)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#example_2_css_alternative)

-------------------------------------------------------------------------------------------------------------------------------------

html

    <div class="center">
      This text will be centered.
      <p>So will this paragraph.</p>
    </div>
    

css

    .center {
      text-align: center;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#result_2)

[Example 3 (CSS alternative)](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#example_3_css_alternative)

-------------------------------------------------------------------------------------------------------------------------------------

html

    <p class="center">
      This line will be centered.<br />
      And so will this line.
    </p>
    

css

    .center {
      text-align: center;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#result_3)

**Note:** Applying [`text-align: center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 to a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 or [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element centers the _contents_ of those elements while leaving their overall dimensions unchanged.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# center](https://html.spec.whatwg.org/multipage/obsolete.html#center) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center#see_also)

-------------------------------------------------------------------------------------------------

*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    
*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/center/index.md?plain=1 "Folder: en-us/web/html/reference/elements/center (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcenter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcenter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcenter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcenter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
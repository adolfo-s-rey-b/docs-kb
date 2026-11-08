*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#mdn-search)
    

`<big>` HTML bigger text element
================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<big>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 deprecated element renders the enclosed text at a font size one level larger than the surrounding text (`medium` becomes `large`, for example). The size is capped at the browser's maximum permitted font size.

**Warning:** This element has been removed from the specification and shouldn't be used anymore. Use the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 property to adjust the font size.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#attributes)

--------------------------------------------------------------------------------------------------

This element has no other attributes than the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, common to all elements.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#examples)

----------------------------------------------------------------------------------------------

Here we see examples showing the use of `<big>` followed by an example showing how to accomplish the same results using modern CSS syntax instead.

### [Using big](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#using_big)

This example uses the obsolete `<big>` element to increase the size of some text.

#### HTML

#### Result

### [Using CSS `font-size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#using_css_font-size)

This example uses the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 property to increase the font size by one level.

#### CSS

css

    .bigger {
      font-size: larger;
    }
    

#### HTML

html

    <p>
      This is the first sentence.
      <span class="bigger">This whole sentence is in bigger letters.</span>
    </p>
    

#### Result

[DOM interface](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#dom_interface)

--------------------------------------------------------------------------------------------------------

This element implements the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# big](https://html.spec.whatwg.org/multipage/obsolete.html#big) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big#see_also)

----------------------------------------------------------------------------------------------

*   CSS: [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    , [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   HTML: [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small)
    , [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font)
    , [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/big/index.md?plain=1 "Folder: en-us/web/html/reference/elements/big (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbig&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbig%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbig%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbig%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
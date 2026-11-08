*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#mdn-search)
    

`::-moz-color-swatch` CSS pseudo-element
========================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`::-moz-color-swatch`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that represents the color selected in an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of `type="color"`.

**Note:** Using `::-moz-color-swatch` with anything but an `<input type="color">` doesn't match anything and has no effect.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#syntax)

----------------------------------------------------------------------------------------------------------

css

    ::-moz-color-swatch {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#examples)

--------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#html)

html

    <input type="color" value="#de2020" />
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#css)

css

    input[type="color"]::-moz-color-swatch {
      border-radius: 10px;
      border-style: none;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#specifications)

--------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch#see_also)

--------------------------------------------------------------------------------------------------------------

*   Similar pseudo-elements used by other browsers:
    *   `::-webkit-color-swatch`, pseudo-element supported by WebKit and Blink (Safari, Chrome, and Opera)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_-moz-color-swatch/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_-moz-color-swatch (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-moz-color-swatch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-moz-color-swatch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-moz-color-swatch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-moz-color-swatch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
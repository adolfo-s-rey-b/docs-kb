*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#mdn-search)
    

`::-moz-focus-inner` CSS pseudo-element
=======================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`::-moz-focus-inner`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that represents an inner focus ring of the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element as well as the [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
, [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
, and [color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)
 types of the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element.

**Note:** Using `::-moz-focus-inner` with anything than the buttons that support it doesn't match anything and has no effect.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#syntax)

---------------------------------------------------------------------------------------------------------

css

    ::-moz-focus-inner {
      /* ... */
    }
    

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#example)

-----------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#html)

html

    <input type="submit" value="Input" /> <button type="submit">Button</button>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#css)

css

    button::-moz-focus-inner,
    input[type="color"]::-moz-focus-inner,
    input[type="reset"]::-moz-focus-inner,
    input[type="button"]::-moz-focus-inner,
    input[type="submit"]::-moz-focus-inner {
      padding-block-start: 0px;
      padding-inline-end: 2px;
      padding-block-end: 0px;
      padding-inline-start: 2px;
      border: 2px dotted red;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#specifications)

-------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Mozilla CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
    
*   Related CSS properties:
    
    *   [`-moz-user-focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus)
        
*   Related CSS selectors:
    
    *   [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
        
    *   [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
        
    *   [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_-moz-focus-inner/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_-moz-focus-inner (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-moz-focus-inner&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-moz-focus-inner%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-moz-focus-inner%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-moz-focus-inner%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
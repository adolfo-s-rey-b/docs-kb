*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#mdn-search)
    

`:-moz-last-node` CSS pseudo-class
==================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#browser_compatibility)
 carefully before using this in production.

The **`:-moz-last-node`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that represents any element that is the last child node of some other element. It differs from [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
 because it does not match a last-child element with (non-whitespace) text after it.

**Note:** Any whitespace at the end of an element is ignored for the determination of `:-moz-last-node`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#syntax)

------------------------------------------------------------------------------------------------------

css

    :-moz-last-node {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#examples)

----------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#css)

css

    span:-moz-last-node {
      background-color: lime;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#html)

html

    <p>
      <span>This does not match.</span>
      <span>This matches!</span>
    </p>
    
    <p>
      <span>This doesn't match because it's followed by text.</span>
      Blahblah.
    </p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#specifications)

----------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node#see_also)

----------------------------------------------------------------------------------------------------------

*   [`:-moz-first-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-first-node)
    
*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_-moz-last-node/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_-moz-last-node (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-last-node&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-last-node%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-last-node%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-last-node%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
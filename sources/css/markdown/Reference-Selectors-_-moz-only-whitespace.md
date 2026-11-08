*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#mdn-search)
    

`:-moz-only-whitespace` CSS pseudo-class
========================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Note:** In [Selectors Level 4](https://drafts.csswg.org/selectors-4/#the-empty-pseudo "External link (opens in new tab)")
, the [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
 selector was changed to act like `:-moz-only-whitespace`, but no browser currently supports this yet.

The **`:-moz-only-whitespace`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements that only contain text nodes that only contain [whitespace](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
. (This includes elements with empty text nodes and elements with no child nodes.)

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#syntax)

------------------------------------------------------------------------------------------------------------

css

    :-moz-only-whitespace {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#examples)

----------------------------------------------------------------------------------------------------------------

### [Basic :-moz-only-whitespace example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#basic_-moz-only-whitespace_example)

#### HTML

html

    <div> </div>
    

#### CSS

css

    div {
      border: 4px solid red;
    }
    
    :-moz-only-whitespace {
      border-color: lime;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#specifications)

----------------------------------------------------------------------------------------------------------------------------

Briefly defined as `:blank` in [Selectors Level 4](https://drafts.csswg.org/selectors-4/#changes-2018-02 "External link (opens in new tab)")
, but then the functionality was merged into [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
 and [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
 redefined to mean empty [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    
*   [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_-moz-only-whitespace/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_-moz-only-whitespace (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-only-whitespace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-only-whitespace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-only-whitespace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-only-whitespace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
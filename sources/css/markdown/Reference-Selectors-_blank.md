*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#mdn-search)
    

`:blank` CSS pseudo-class
=========================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#browser_compatibility)
 carefully before using this in production.

**Note:** The `:blank` selector is considered at risk, as the CSSWG keeps changing it.

See [CSSWG issue #1967](https://github.com/w3c/csswg-drafts/issues/1967 "External link (opens in new tab)")
.

The **`:blank`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selects empty user input elements (e.g., [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#syntax)

---------------------------------------------------------------------------------------------

css

    :blank {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#examples)

-------------------------------------------------------------------------------------------------

### [Basic :blank example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#basic_blank_example)

In eventual supporting browsers, the `:blank` pseudo-class will enable developers to highlight in some way input controls that are not required, but still have no content filled in, perhaps as a reminder to users.

#### HTML

html

    <textarea></textarea>
    

#### CSS

css

    textarea:blank {
      border: 3px solid red;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# blank-pseudo](https://drafts.csswg.org/selectors/#blank-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank#see_also)

-------------------------------------------------------------------------------------------------

*   [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_blank/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_blank (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ablank&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_blank%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ablank%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_blank%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#mdn-search)
    

`:left` CSS pseudo-class
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/24)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:left`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
, used with the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
, represents all left-hand pages of a printed document.

Whether a given page is "left" or "right" is determined by the major writing direction of the document. For example, if the first page has a major writing direction of left-to-right then it will be a [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
 page; if it has a major writing direction of right-to-left then it will be a `:left` page.

**Note:** This pseudo-class can be used to change only the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, and [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 properties of the _page box_. All other properties will be ignored, and only the page box, not the document content on the page, will be affected.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#syntax)

--------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#examples)

------------------------------------------------------------------------------------------------

### [Setting a margin for left-hand pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#setting_a_margin_for_left-hand_pages)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# spread-pseudos](https://drafts.csswg.org/css-page/#spread-pseudos) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left#see_also)

------------------------------------------------------------------------------------------------

*   [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
    
*   Other page-related pseudo-classes: [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    , [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_left/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_left (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aleft&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_left%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aleft%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_left%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
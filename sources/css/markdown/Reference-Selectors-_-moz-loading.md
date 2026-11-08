*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#mdn-search)
    

`:-moz-loading` CSS pseudo-class
================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`:-moz-loading`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that matches elements that can't be displayed because they have not started loading, such as images that haven't started to arrive yet. Note that images that are _in the process_ of loading _are not_ matched by this pseudo-class.

**Note:** This selector is mainly intended to be used by theme developers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#syntax)

----------------------------------------------------------------------------------------------------

css

    :-moz-loading {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#examples)

--------------------------------------------------------------------------------------------------------

### [Setting a background for images that are loading](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#setting_a_background_for_images_that_are_loading)

css

    :-moz-loading {
      background: url("loading-animation.gif") center no-repeat;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#specifications)

--------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:-moz-broken`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-broken)
    , [`:-moz-suppressed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-suppressed)
    , [`:-moz-user-disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-user-disabled)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_-moz-loading/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_-moz-loading (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-loading&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-loading%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-loading%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-loading%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
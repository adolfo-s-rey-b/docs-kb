*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#mdn-search)
    

`:-moz-locale-dir(rtl)` CSS pseudo-class
========================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`:-moz-locale-dir(rtl)`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 is a [Mozilla extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
 that matches an element if the user interface is being displayed right-to-left. This is determined by the preference `intl.uidirection.locale` (where `locale` is the current locale) being set to "rtl".

**Note:** This selector is mainly used by extensions and themes to adapt the user interface based on the user's locale. (This can vary from window to window, and even from tab to tab.) It also allows extensions to work even when they don't support the user's default locale, since they can support both left-to-right and right-to-left layouts regardless of locale specifics.

**Warning:** This selector does not work properly from HTML; it never matches, no matter whether the UI locale is left-to-right or right-to-left.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#syntax)

-----------------------------------------------------------------------------------------------------------

css

    :-moz-locale-dir(rtl) {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#examples)

---------------------------------------------------------------------------------------------------------------

This example will not work if you're not using Firefox, and might not work properly even in Firefox due to an issue with using this selector in HTML.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#html)

html

    <p>If you're using a right-to-left interface, this should be red.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#css)

css

    p:-moz-locale-dir(rtl) {
      color: red;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#specifications)

---------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`:dir(…)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)
    
*   [`:-moz-locale-dir(ltr)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_ltr)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_-moz-locale-dir_rtl/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_-moz-locale-dir_rtl (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-locale-dir_rtl&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-locale-dir_rtl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A-moz-locale-dir_rtl%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_-moz-locale-dir_rtl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
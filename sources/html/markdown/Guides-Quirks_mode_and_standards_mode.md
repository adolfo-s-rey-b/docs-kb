*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode#mdn-search)
    

Understanding quirks and standards modes
========================================

In the old days of the web, pages were typically written in two versions: One for Netscape Navigator, and one for Microsoft Internet Explorer. When the web standards were made at W3C, browsers could not just start using them, as doing so would break most existing sites on the web. Browsers therefore introduced two modes to treat new standards compliant sites differently from old legacy sites.

There are now three modes used by the layout engines in web browsers: quirks mode, limited-quirks mode, and no-quirks mode. In **quirks mode**, layout emulates behavior in Navigator 4 and Internet Explorer 5. This is essential in order to support websites that were built before the widespread adoption of web standards. In **no-quirks mode**, the behavior is (hopefully) the desired behavior described by the modern HTML and CSS specifications. In **limited-quirks mode**, there are only a very small number of quirks implemented.

The limited-quirks and no-quirks modes used to be called "almost-standards" mode and "full standards" mode, respectively. These names have been changed as the behavior is now standardized.

[How do browsers determine which mode to use?](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode#how_do_browsers_determine_which_mode_to_use)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 documents, browsers use a doctype in the beginning of the document to decide whether to handle it in quirks mode or no-quirks mode. To ensure that your page uses no-quirks mode, make sure that your page has a doctype like in this example:

The doctype shown in the example, `<!doctype html>`, is the simplest possible, and the one recommended by current HTML standards. Earlier versions of the HTML standard recommended other variants, but all existing browsers today will use no-quirks mode for this doctype. There are no valid reasons to use a more complicated doctype. If you do use another doctype, you may risk choosing one which triggers limited-quirks mode or quirks mode.

Put the doctype right at the beginning of your HTML document, before any other content.

The only purpose of `<!doctype html>` is to activate no-quirks mode. Older versions of HTML standard doctypes provided additional meaning, but no browser ever used the doctype for anything other than switching between render modes.

See also a detailed description of [when different browsers choose various modes](https://hsivonen.fi/doctype/ "External link (opens in new tab)")
.

### [XHTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode#xhtml)

If you serve your page as [XHTML](https://developer.mozilla.org/en-US/docs/Glossary/XHTML)
 using the `application/xhtml+xml` MIME type in the `Content-Type` HTTP header, you do not need a doctype to enable no-quirks mode, as such documents always use no-quirks mode.

If you serve XHTML-like content using the `text/html` MIME type, browsers will read it as HTML, and you will need the doctype to use no-quirks mode.

[How do I see which mode is used?](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode#how_do_i_see_which_mode_is_used)

------------------------------------------------------------------------------------------------------------------------------------------------------------

If the page is rendered in quirks or limited-quirks mode, Firefox will log a warning to the console tab in the developer tools. If this warning is not shown, Firefox is using no-quirks mode.

The value of `document.compatMode` in JavaScript will show whether or not the document is in quirks mode. If its value is `"BackCompat"`, the document is in quirks mode. If it isn't, it will have value `"CSS1Compat"`.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 9, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/quirks_mode_and_standards_mode/index.md?plain=1 "Folder: en-us/web/html/guides/quirks_mode_and_standards_mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FQuirks_mode_and_standards_mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fquirks_mode_and_standards_mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FQuirks_mode_and_standards_mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fquirks_mode_and_standards_mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0754cd805a8e010d2e3a2a065f634a3bcf358252%0A*+Document+last+modified%3A+2025-07-09T21%3A49%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
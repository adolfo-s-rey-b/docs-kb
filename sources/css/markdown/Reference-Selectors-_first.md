*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#mdn-search)
    

`:first` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since August 2023.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/24)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:first`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
, used with the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
, represents the first page of a printed document. (See [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
 for general first element of a node.)

css

    /* Selects the first page when printing */
    @page :first {
      margin-left: 50%;
      margin-top: 50%;
    }
    

**Note:** You can't change all CSS properties with this pseudo-class. You can only change the margins, [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
, [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
, and page breaks of the document. Furthermore, you may only use [absolute-length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)
 units when defining the margins. All other properties will be ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#syntax)

---------------------------------------------------------------------------------------------

css

    :first {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#examples)

-------------------------------------------------------------------------------------------------

### [Using `:first` for page print styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#using_first_for_page_print_styles)

Press the "Print!" button to print the example. The words on the first page should be somewhere around the center, while other pages will have their contents at the default position:

html

    <p>First Page.</p>
    <p>Second Page.</p>
    <button>Print!</button>
    

css

    @page :first {
      size: 8.5in 11in;
      margin-left: 3in;
      margin-top: 5in;
    }
    
    p {
      page-break-after: always;
      font: 1.2em sans-serif;
    }
    

js

    document.querySelector("button").addEventListener("click", () => {
      window.print();
    });
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# first-pseudo](https://drafts.csswg.org/css-page/#first-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first#see_also)

-------------------------------------------------------------------------------------------------

*   [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
    
*   Other page-related pseudo-classes: [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    , [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_first/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_first (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
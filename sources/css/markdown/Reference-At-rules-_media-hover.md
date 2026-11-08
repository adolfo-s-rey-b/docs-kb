*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#mdn-search)
    

`hover` CSS media feature
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hover`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test whether the user's _primary_ input mechanism can hover over elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#syntax)

--------------------------------------------------------------------------------------------------

The `hover` feature is specified as a keyword value chosen from the list below.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#none)

The primary input mechanism cannot hover at all or cannot conveniently hover (e.g., many mobile devices emulate hovering when the user performs an inconvenient long tap), or there is no primary pointing input mechanism.

[`hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#hover)

The primary input mechanism can conveniently hover over elements.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#examples)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#html)

html

    <a href="#">Try hovering over me!</a>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#css)

css

    /* default hover effect */
    a:hover {
      color: black;
      background: yellow;
    }
    
    @media (hover: hover) {
      /* when hover is supported */
      a:hover {
        color: white;
        background: black;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# hover](https://drafts.csswg.org/mediaqueries/#hover) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover#see_also)

------------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/hover/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/hover (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fhover&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fhover%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fhover%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fhover%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
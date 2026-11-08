*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#mdn-search)
    

`grid` CSS media feature
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`grid`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test whether the output device uses a grid-based screen.

Most modern computers and smartphones have bitmap-based screens. Examples of grid-based devices include text-only terminals and basic phones with only one fixed font.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#syntax)

-------------------------------------------------------------------------------------------------

The `grid` feature is specified as a value representing whether the output device is grid-based — `1` if it is, and `0` if not.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#examples)

-----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#html)

html

    <p class="unknown">I don't know if you're using a grid device. :-(</p>
    <p class="bitmap">You are using a bitmap device.</p>
    <p class="grid">You are using a grid device! Neato!</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#css)

css

    :not(.unknown) {
      color: lightgray;
    }
    
    @media (grid: 0) {
      .unknown {
        color: lightgray;
      }
    
      .bitmap {
        color: red;
        text-transform: uppercase;
      }
    }
    
    @media (grid: 1) {
      .unknown {
        color: lightgray;
      }
    
      .grid {
        color: black;
        text-transform: uppercase;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# grid](https://drafts.csswg.org/mediaqueries/#grid) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid#see_also)

-----------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/grid/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/grid (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fgrid&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fgrid%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fgrid%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fgrid%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fddf85bfec1b6e43cdacb404de0c38a801c561640%0A*+Document+last+modified%3A+2026-05-12T10%3A30%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
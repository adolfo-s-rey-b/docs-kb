*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#mdn-search)
    

`-webkit-transform-3d` CSS media feature
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`-webkit-transform-3d`** Boolean [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is a [WebKit extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
 whose value is `true` if vendor-prefixed CSS 3D [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
s are supported.

**Note:** While this media feature is currently [supported by most browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#browser_compatibility)
. If possible, use an [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#syntax)

-----------------------------------------------------------------------------------------------------------------

`-webkit-transform-3d` is a Boolean [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 whose value is `true` if the browser supports `-webkit` prefixed CSS 3D [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
s.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#values)

[`true`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#true)

The browser supports the 3D CSS transforms with the `-webkit` prefix and supports non-standard, prefixed media queries.

[`false`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#false)

The 3D CSS transforms prefixed with `-webkit` are not supported by the browser.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#examples)

---------------------------------------------------------------------------------------------------------------------

### [Examples of media queries with -webkit-transform-3d](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#examples_of_media_queries_with_-webkit-transform-3d)

css

    @media (-webkit-transform-3d) {
      .foo {
        transform-style: preserve-3d;
      }
    }
    

A better method for checking for browser support is using a feature query:

css

    @supports (transform-style) {
      .foo {
        transform-style: preserve-3d;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compatibility  <br>\# css-media-queries-webkit-transform-3d](https://compat.spec.whatwg.org/#css-media-queries-webkit-transform-3d) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`-webkit-transform-2d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-2d)
    
*   [`-webkit-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition)
    
*   [`-webkit-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-animation)
    
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     and [using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     and [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
     and [using feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/-webkit-transform-3d/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/-webkit-transform-3d (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-transform-3d&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-transform-3d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-transform-3d%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-transform-3d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
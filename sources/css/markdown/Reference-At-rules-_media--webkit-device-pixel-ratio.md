*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#mdn-search)
    

`-webkit-device-pixel-ratio` CSS media feature
==============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`-webkit-device-pixel-ratio`** is a non-standard Boolean [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 which is an alternative to the standard [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
 media feature.

**Note:** If possible, use the [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
 media feature query instead, which is a standard media feature. While this prefixed media feature is a WebKit feature, other browser engines may support it. See [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#browser_compatibility)
 below.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#syntax)

-----------------------------------------------------------------------------------------------------------------------

The `-webkit-device-pixel-ratio` feature is specified as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 value. It is a range feature, meaning that you can also use the prefixed **`-webkit-min-device-pixel-ratio`** and **`-webkit-max-device-pixel-ratio`** variants to query minimum and maximum values, respectively.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#values)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The number of device pixels used to represent each CSS [`px`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)
. Although the value is a `<number>`, and thus doesn't syntactically allow units, its implicit unit is [`dppx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution#units)
.

[Implementation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#implementation)

---------------------------------------------------------------------------------------------------------------------------------------

css

    /* A unit of "dppx" is implied: */
    @media (-webkit-min-device-pixel-ratio: 2) {
      /* … */
    }
    /* It is equivalent to: */
    @media (min-resolution: 2dppx) {
      /* … */
    }
    
    /* Similarly: */
    @media (-webkit-max-device-pixel-ratio: 2) {
      /* … */
    }
    /* It is equivalent to: */
    @media (max-resolution: 2dppx) {
      /* … */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#examples)

---------------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#html)

html

    <p>This is a test of your device's pixel density.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#css)

css

    /* Exact resolution */
    @media (-webkit-device-pixel-ratio: 1) {
      p {
        color: red;
      }
    }
    
    /* Minimum resolution */
    @media (-webkit-min-device-pixel-ratio: 1.1) {
      p {
        font-size: 1.5em;
      }
    }
    
    /* Maximum resolution */
    @media (-webkit-max-device-pixel-ratio: 3) {
      p {
        background: yellow;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compatibility  <br>\# css-media-queries-webkit-device-pixel-ratio](https://compat.spec.whatwg.org/#css-media-queries-webkit-device-pixel-ratio) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    
*   [`-webkit-transform-2d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-2d)
    
*   [`-webkit-transform-3d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d)
    
*   [`-webkit-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition)
    
*   [`-webkit-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-animation)
    
*   [W3C Suggested Method to UnPrefix](https://www.w3.org/blog/CSS/2012/06/14/unprefix-webkit-device-pixel-ratio/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/-webkit-device-pixel-ratio/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/-webkit-device-pixel-ratio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-device-pixel-ratio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-device-pixel-ratio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-device-pixel-ratio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-device-pixel-ratio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
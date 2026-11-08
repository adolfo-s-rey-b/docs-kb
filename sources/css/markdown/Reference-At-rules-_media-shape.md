*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#mdn-search)
    

`shape` CSS media feature
=========================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#browser_compatibility)
 carefully before using this in production.

The `shape` [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the shape of the device to distinguish rectangular and round displays.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#syntax)

--------------------------------------------------------------------------------------------------

The `shape` discrete feature is specified as one of two acceptable strings, either `rect` representing a rectangular screen or `round` representing a circular, oval or elliptical screen.

[`rect`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#rect)

The shape is an axis aligned rectangle or square, or a similar shape such as rounded rectangle for which the traditional designs are appropriate.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#round)

The shape is rounded or a similar shape to the circle such as an oval, an ellipse for which distinctively rounded designs are appropriate.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#basic_example)

#### HTML

html

    <h1>Hello World!</h1>
    

#### CSS

css

    h1 {
      text-align: left;
    }
    
    @media (shape: rect) {
      h1 {
        text-align: left;
      }
    }
    
    @media (shape: round) {
      h1 {
        text-align: center;
      }
    }
    

### [Custom stylesheet](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#custom_stylesheet)

This HTML will apply a special stylesheet for devices that have round screens.

html

    <head>
      <link rel="stylesheet" href="default.css" />
      <link
        media="screen and (shape: rect)"
        rel="stylesheet"
        href="rectangle.css" />
      <link media="screen and (shape: round)" rel="stylesheet" href="round.css" />
    </head>
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Round Display Level 1  <br>\# shape-media-feature](https://drafts.csswg.org/css-round-display/#shape-media-feature) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape#see_also)

------------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [CSS round display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Round_display)
     module
*   [Using environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables/Using)
    
*   [CSS environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/shape/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fshape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fshape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fshape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fshape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
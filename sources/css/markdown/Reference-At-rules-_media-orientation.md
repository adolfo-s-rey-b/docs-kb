*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#mdn-search)
    

`orientation` CSS media feature
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`orientation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the orientation of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 (or the page box, for [paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
).

**Note:** This feature does not correspond to _device_ orientation. Opening the soft keyboard on many devices in portrait orientation will cause the viewport to become wider than it is tall, thereby causing the browser to use landscape styles instead of portrait.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#syntax)

--------------------------------------------------------------------------------------------------------

The `orientation` feature is specified as a keyword value chosen from the list below.

### [Keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#keyword_values)

[`portrait`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#portrait)

The viewport is in a portrait orientation, i.e., the height is greater than or equal to the width.

[`landscape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#landscape)

The viewport is in a landscape orientation, i.e., the width is greater than the height.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#examples)

------------------------------------------------------------------------------------------------------------

### [Portrait orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#portrait_orientation)

In this example we have three boxes in the HTML, and use the `orientation` media feature to switch between a row layout (in landscape) and a column layout (in portrait).

The example output is embedded in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 whose height is greater than its width, so the boxes get a column layout.

#### HTML

html

    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>
    

#### CSS

css

    body {
      display: flex;
    }
    
    div {
      background: yellow;
      width: 200px;
      height: 200px;
      margin: 0.5rem;
      padding: 0.5rem;
    }
    
    @media (orientation: landscape) {
      body {
        flex-direction: row;
      }
    }
    
    @media (orientation: portrait) {
      body {
        flex-direction: column;
      }
    }
    

#### Result

### [Landscape orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#landscape_orientation)

This example has exactly the same code as the previous example: it has three boxes in the HTML, and uses the `orientation` media feature to switch between a row layout (in landscape) and a column layout (in portrait).

However, in this example, the example output is embedded in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 whose height is less than its width, so the boxes get a row layout.

#### HTML

html

    <div>Box 1</div>
    <div>Box 2</div>
    <div>Box 3</div>
    

#### CSS

css

    body {
      display: flex;
    }
    
    div {
      background: yellow;
      width: 200px;
      height: 200px;
      margin: 0.5rem;
      padding: 0.5rem;
    }
    
    @media (orientation: landscape) {
      body {
        flex-direction: row;
      }
    }
    
    @media (orientation: portrait) {
      body {
        flex-direction: column;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# orientation](https://drafts.csswg.org/mediaqueries/#orientation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/orientation/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/orientation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Forientation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Forientation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Forientation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Forientation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
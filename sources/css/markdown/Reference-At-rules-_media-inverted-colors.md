*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#mdn-search)
    

`inverted-colors` CSS media feature
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/54)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inverted-colors`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is used to test if the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 or the underlying operating system has inverted all colors.

Inversion of colors can have unpleasant side effects, such as shadows turning into highlights, which can reduce the readability of the content. Using this media feature, you can detect if inversion is happening and style the content accordingly while respecting user preference.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#syntax)

------------------------------------------------------------------------------------------------------------

The `inverted-colors` feature is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#none)

Indicates that the colors are displayed normally and no inversion of colors has happened. This keyword value evaluates as false.

[`inverted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#inverted)

Indicates that all pixels within the displayed area have been inverted. This keyword value evaluates as true.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#examples)

----------------------------------------------------------------------------------------------------------------

### [Applying styles if color inversion is detected](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#applying_styles_if_color_inversion_is_detected)

This example demonstrates the effects of both `inverted-colors` media feature keyword values and when the `inverted-colors` media feature is not supported.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# inverted](https://drafts.csswg.org/mediaqueries-5/#inverted) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors#see_also)

----------------------------------------------------------------------------------------------------------------

*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
*   [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/inverted-colors/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/inverted-colors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Finverted-colors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Finverted-colors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Finverted-colors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Finverted-colors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
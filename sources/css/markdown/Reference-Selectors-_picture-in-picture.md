*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#mdn-search)
    

`:picture-in-picture` CSS pseudo-class
======================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/90)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:picture-in-picture`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches the element which is currently in picture-in-picture mode.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#syntax)

----------------------------------------------------------------------------------------------------------

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#usage_notes)

--------------------------------------------------------------------------------------------------------------------

The `:picture-in-picture` pseudo-class lets you configure your stylesheets to automatically adjust the size, style, or layout of content when a video switches back and forth between picture-in-picture and traditional presentation modes.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#examples)

--------------------------------------------------------------------------------------------------------------

In this example, a video has a box shadow when it is displayed in the floating window.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#html)

The page's HTML looks like this:

The [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 with the ID `"pip-video"` will change between having a red box shadow or not, depending on whether or not it is displayed in the picture-in-picture floating window.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#css)

The magic happens in the CSS.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# pip-state](https://drafts.csswg.org/selectors/#pip-state) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Picture-in-picture API](https://developer.mozilla.org/en-US/docs/Web/API/Picture-in-Picture_API)
    
*   [`HTMLVideoElement.requestPictureInPicture()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/requestPictureInPicture)
    
*   [`HTMLVideoElement.disablePictureInPicture`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/disablePictureInPicture)
    
*   [`Document.pictureInPictureEnabled`](https://developer.mozilla.org/en-US/docs/Web/API/Document/pictureInPictureEnabled)
    
*   [`Document.exitPictureInPicture()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/exitPictureInPicture)
    
*   [`Document.pictureInPictureElement`](https://developer.mozilla.org/en-US/docs/Web/API/Document/pictureInPictureElement)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_picture-in-picture/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_picture-in-picture (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Apicture-in-picture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_picture-in-picture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Apicture-in-picture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_picture-in-picture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
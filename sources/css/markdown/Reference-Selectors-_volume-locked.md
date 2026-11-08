*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#mdn-search)
    

`:volume-locked` CSS pseudo-class
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/166)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:volume-locked`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents an element that is capable of making sound, such as [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
, but the audio volume of the media element is currently "locked" by the user.

User agents may set media [`muted`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/muted)
 or [`volume`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volume)
 values according to user preferences (e.g., remembering the last set value across sessions, on a per-site basis, or otherwise). An element that is `:volume-locked` cannot be muted, un-muted, or have its volume changed via JavaScript. The locked status is an operating system or user agent preference.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#syntax)

-----------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#examples)

---------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#css)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# selectordef-volume-locked](https://drafts.csswg.org/selectors/#selectordef-volume-locked) |
| [HTML  <br>\# selector-volume-locked](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-volume-locked) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked#see_also)

---------------------------------------------------------------------------------------------------------

*   [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    
*   [`:muted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)
    
*   [`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`:stalled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [`volume`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volume)
     property of [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
     objects

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_volume-locked/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_volume-locked (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avolume-locked&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_volume-locked%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Avolume-locked%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_volume-locked%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
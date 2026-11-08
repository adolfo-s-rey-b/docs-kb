*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#mdn-search)
    

`:past` CSS pseudo-class
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/25)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:past`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector is a time-dimensional pseudo-class that will match for any element which appears entirely before an element that matches [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
. For example in a video with captions which are being displayed by [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
.

css

    :past(p, span) {
      display: none;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#syntax)

--------------------------------------------------------------------------------------------

css

    :past {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#examples)

------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#css)

css

    :past(p, span) {
      display: none;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#html)

html

    <video controls preload="metadata">
      <source src="video.mp4" type="video/mp4" />
      <source src="video.webm" type="video/webm" />
      <track
        label="English"
        kind="subtitles"
        srclang="en"
        src="subtitles.vtt"
        default />
    </video>
    

### [WebVTT](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#webvtt)

WEBVTT FILE

1
00:00:03.500 --> 00:00:05.000
This is the first caption

2
00:00:06.000 --> 00:00:09.000
This is the second caption

3
00:00:11.000 --> 00:00:19.000
This is the third caption

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 5  <br>\# the-past-pseudo](https://drafts.csswg.org/selectors-5/#the-past-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past#see_also)

------------------------------------------------------------------------------------------------

*   [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
    
*   [`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_past/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_past (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Apast&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_past%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Apast%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_past%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
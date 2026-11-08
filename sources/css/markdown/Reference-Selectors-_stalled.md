*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#mdn-search)
    

`:stalled` CSS pseudo-class
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/166)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:stalled`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents an element that is playable, such as [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
, when playback is stalled. A resource is considered to be stalled if the user has requested playback of a specific position in the media resource, but it has failed to receive any data for some amount of time. This is different from [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
 in that the media element is unexpectedly not loading data when stalled (e.g., due to a network error) for around 3 seconds (the exact time is [user agent dependent](https://html.spec.whatwg.org/multipage/media.html#stall-timeout "External link (opens in new tab)")
).

**Note:** Like with the [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
 pseudo-class, the element is still considered to be "playing" when it is "stalled". If `:stalled` matches an element, [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
 will also match that element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#syntax)

-----------------------------------------------------------------------------------------------

css

    :stalled {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#examples)

---------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#css)

css

    :stalled {
      outline: 5px solid red;
    }
    
    audio:stalled {
      background-color: red;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# selectordef-stalled](https://drafts.csswg.org/selectors/#selectordef-stalled) |
| [HTML  <br>\# selector-stalled](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-stalled) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled#see_also)

---------------------------------------------------------------------------------------------------

*   [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    
*   [`:muted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)
    
*   [`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [`stalled`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/stalled_event)
     event

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_stalled/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_stalled (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Astalled&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_stalled%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Astalled%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_stalled%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
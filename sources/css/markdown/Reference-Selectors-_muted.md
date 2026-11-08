*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#mdn-search)
    

`:muted` CSS pseudo-class
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/166)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:muted`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents an element that is capable of making sound, such as [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
, but is muted (forced silent).

Muted is different from [`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
 in that the page author has control over whether a media element can be muted or un-muted. User agents may set media `muted` value according to use preferences (e.g., remembering the last set value across sessions, on a per-site basis, or otherwise). An element that is `:volume-locked` cannot be muted, un-muted, or have its volume changed via JavaScript because of an operating system or user agent preference.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#syntax)

---------------------------------------------------------------------------------------------

css

    :muted {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#examples)

-------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#html)

The `muted` attribute is added to the [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 element so that the sound is muted, this works the same for [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 elements.

html

    <!-- 'Big Buck Bunny' licensed under CC 3.0 by the Blender foundation. Hosted by archive.org -->
    <!-- Poster from peach.blender.org -->
    <video
      controls
      muted
      src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
      poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
      width="620">
      Sorry, your browser doesn't support embedded videos, but don't worry, you can
      <a href="https://archive.org/details/BigBuckBunny_124">download it</a>
      and watch it with your favorite video player!
    </video>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#css)

If the `<video>` element is `muted` then a red outline is drawn around it, when it is not muted then it has a green outline. Try toggling the mute icon in the controls to see the state change.

    video {
      margin: 5px;
    }
    

css

    video:muted {
      outline: 5px solid red;
    }
    
    video:not(:muted) {
      outline: 5px solid green;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# selectordef-muted](https://drafts.csswg.org/selectors/#selectordef-muted) |
| [HTML  <br>\# selector-muted](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-muted) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted#see_also)

-------------------------------------------------------------------------------------------------

*   [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    
*   [`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`:stalled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
    
*   [`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [`muted`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/muted)
     property of [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
     objects

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_muted/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_muted (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Amuted&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_muted%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Amuted%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_muted%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1aa0dbd7441564e6ce8f6706c2022a2e1912d8c%0A*+Document+last+modified%3A+2026-07-16T11%3A25%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
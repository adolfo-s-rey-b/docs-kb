*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#mdn-search)
    

`::cue` CSS pseudo-element
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::cue`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 matches [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
 cues within a selected element. This can be used to [style captions and other cues](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API#styling_webvtt_in_html_or_a_stylesheet)
 in media with VTT tracks.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#try_it)

--------------------------------------------------------------------------------------------

    video {
      width: 100%;
    }
    
    video::cue {
      font-size: 1rem;
      color: yellow;
    }
    
    ::cue(u) {
      color: red;
    }
    

    <video controls src="/shared-assets/videos/friday.mp4">
      <track
        default
        kind="captions"
        srclang="en"
        src="/shared-assets/misc/friday.vtt" />
      Sorry, your browser doesn't support embedded videos.
    </video>
    

The properties are applied to the entire set of cues as if they were a single unit. The only exception is that `background` and its longhand properties apply to each cue individually, to avoid creating boxes and obscuring unexpectedly large areas of the media.

In the example above, the `::cue(u)` selector selects all the [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u)
 elements inside [the cue text](https://github.com/mdn/shared-assets/blob/main/misc/friday.vtt "External link (opens in new tab)")
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#syntax)

--------------------------------------------------------------------------------------------

css

    ::cue | ::cue(<selector>) {
      /* ... */
    }
    

[Permitted properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#permitted_properties)

------------------------------------------------------------------------------------------------------------------------

Rules whose selectors include this element may only use the following CSS properties:

*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    
*   [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    
*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    
*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
    
*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
    
*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    
*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`ruby-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position)
    
*   [`text-combine-upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    
*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    
*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    
*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
    
*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#examples)

------------------------------------------------------------------------------------------------

### [Styling WebVTT cues as white-on-black](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#styling_webvtt_cues_as_white-on-black)

The following CSS sets the cue style so that the text is white and the background is a translucent black box.

css

    ::cue {
      color: white;
      background-color: rgb(0 0 0 / 60%);
    }
    

### [Styling WebVTT internal node objects](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#styling_webvtt_internal_node_objects)

Cue text can include _internal node objects_ as the tags (similar to HTML elements) `<c>`, `<i>`, `<b>`, `<u>`, `<ruby>`, `<rt>`, `<v>`, and `<lang>`. The `::cue()` selector can be used to apply styles to content inside these tags to customize how the WebVTT track is displayed. Consider the following cue text that uses the `<u>` tag to underline some text:

00:00:01.500 --> 00:00:02.999 line:80%
Tell me, is the <u>lord of the universe</u> in?

The following CSS rule customizes the text inside the `<u>` tag with a color and a [text-decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
:

css

    ::cue(u) {
      color: red;
      text-decoration: wavy overline lime;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [WebVTT: The Web Video Text Tracks Format  <br>\# the-cue-pseudo-element](https://w3c.github.io/webvtt/#the-cue-pseudo-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue#see_also)

------------------------------------------------------------------------------------------------

*   [Web Video Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)
    , [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_cue/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_cue (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Acue&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_cue%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Acue%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_cue%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
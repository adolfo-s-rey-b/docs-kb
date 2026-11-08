*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#mdn-search)
    

`<track>` HTML embed text track element
=======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<track>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used as a child of the media elements, [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 and [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
. Each track element lets you specify a timed text track (or time-based data) that can be displayed in parallel with the media element, for example to overlay subtitles or closed captions on top of a video or alongside audio tracks.

Multiple tracks can be specified for a media element, containing different kinds of timed text data, or timed text data that has been translated for different locales. The data that is used will either be the track that has been set to be the default, or a kind and translation based on user preferences.

The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
 (`.vtt` files) — Web Video Text Tracks.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#try_it)

--------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`default`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#default)

This attribute indicates that the track should be enabled unless the user's preferences indicate that another track is more appropriate. This may only be used on one `track` element per media element.

[`kind`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#kind)

How the text track is meant to be used. If omitted the default kind is `subtitles`. If the attribute contains an invalid value, it will use `metadata`. The following keywords are allowed:

[`subtitles`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#subtitles)

Subtitles provide transcription or translation of the dialog. They are suitable for when the sound is available but not understood, such as speech or text that is not English in an English language film. Subtitles may contain additional content, usually extra background information. For example the text at the beginning of the Star Wars films, or the date, time, and location of a scene. Subtitles' information complements the audio and video. It is often embedded in the video itself, but can also be provided separately, especially for whole-film translations.

[`captions`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#captions)

Closed captions provide transcription or translation of the dialog, sound effects, relevant musical cues, and other relevant audio information, such as the cue's source (e.g., character, environment). They are suitable for when sound is unavailable or not clearly audible (e.g., because it is muted, drowned-out by ambient noise, or because the user is deaf).

[`descriptions`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#descriptions)

Descriptions summarize the _video_ component of the media resource. They are intended to be synthesized as audio when the visual component is obscured, unavailable, or not usable (e.g., because the user is interacting with the application without a screen while driving, or because the user is blind).

[`chapters`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#chapters)

Chapter titles are intended to be used when the user is navigating the media resource.

[`metadata`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#metadata)

Tracks used by scripts. Not visible to the user.

[`label`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#label)

A user-readable title of the text track which is used by the browser when listing available text tracks.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#src)

Address of the track (`.vtt` file). Must be a valid URL. This attribute must be specified and its URL value must have the same origin as the document — unless the [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 parent element of the `track` element has a [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 attribute.

[`srclang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#srclang)

Language of the track text data. It must be a valid [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
. If the `kind` attribute is set to `subtitles`, then `srclang` must be defined.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#usage_notes)

------------------------------------------------------------------------------------------------------

### [Track data types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#track_data_types)

The type of data that `track` adds to the media is set in the `kind` attribute, which can take values of `subtitles`, `captions`, `chapters` or `metadata`. The element points to a source file containing timed text that the browser exposes when the user requests additional data.

A media element cannot have more than one `track` with the same `kind`, `srclang`, and `label`.

### [Detecting cue changes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#detecting_cue_changes)

The underlying [`TextTrack`](https://developer.mozilla.org/en-US/docs/Web/API/TextTrack)
, indicated by the [`track`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement/track "track")
 property, receives a `cuechange` event every time the currently-presented cue is changed. This happens even if the track isn't associated with a media element.

If the track _is_ associated with a media element, using the `<track>` element as a child of the [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 element, the `cuechange` event is also sent to the [`HTMLTrackElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement)
.

### [Adding text tracks programmatically](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#adding_text_tracks_programmatically)

The JavaScript interface that represents the `<track>` element is [`HTMLTrackElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement)
. The text track associated with an element can be obtained from the [`HTMLTrackElement.track`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement/track)
 property, and is of type [`TextTrack`](https://developer.mozilla.org/en-US/docs/Web/API/TextTrack)
.

`TextTrack` objects also can be added to a [`HTMLVideoElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement)
 or [`HTMLAudioElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement)
 elements using the [`HTMLMediaElement.addTextTrack()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/addTextTrack)
 method. The `TextTrack` objects associated with a media element stored in a [`TextTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/TextTrackList)
, which can be retrieved using the [`HTMLMediaElement.textTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/textTracks)
 property.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#examples)

------------------------------------------------------------------------------------------------

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | A media element, [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)<br> or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLTrackElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-track-element](https://html.spec.whatwg.org/multipage/media.html#the-track-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track#see_also)

------------------------------------------------------------------------------------------------

*   [WebVTT text track format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [`HTMLMediaElement.textTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/textTracks)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/track/index.md?plain=1 "Folder: en-us/web/html/reference/elements/track (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftrack&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftrack%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftrack%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftrack%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
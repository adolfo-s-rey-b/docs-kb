*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#mdn-search)
    

`<audio>` HTML embed audio element
==================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<audio>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#try_it)

--------------------------------------------------------------------------------------------

The above example shows basic usage of the `<audio>` element. In a similar manner to the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, we include a path to the media we want to embed inside the `src` attribute; we can include other attributes to specify information such as whether we want it to autoplay and loop, whether we want to show the browser's default audio controls, etc.

The content inside the opening and closing `<audio></audio>` tags is shown as a fallback in browsers that don't support the element.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#attributes)

----------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`autoplay`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#autoplay)

A Boolean attribute: if specified, the audio will automatically begin playback as soon as it can do so, without waiting for the entire audio file to finish downloading.

**Note:** Sites that automatically play audio (or videos with an audio track) can be an unpleasant experience for users, so should be avoided when possible. If you must offer autoplay functionality, you should make it opt-in (requiring a user to specifically enable it). However, this can be useful when creating media elements whose source will be set at a later time, under user control. See our [autoplay guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)
 for additional information about how to properly use autoplay.

**Note:** Audio with the [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#loading)
 attribute set will not start downloading and autoplaying until the controls for the media are near or within the viewport. Lazy-loaded audio without the `controls` attribute will not autoplay.

[`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#controls)

If this attribute is present, the browser will offer controls to allow the user to control audio playback, including volume, seeking, and pause/resume playback.

[`controlslist`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#controlslist)

The [`controlslist`](https://wicg.github.io/controls-list/explainer.html "External link (opens in new tab)")
 attribute, when specified, helps the browser select what controls to show for the `audio` element whenever the browser shows its own set of controls (that is, when the `controls` attribute is specified).

The allowed values are `nodownload`, `nofullscreen` and `noremoteplayback`.

[`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)

This [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicates whether to use CORS to fetch the related audio file. [CORS-enabled resources](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)
 can be reused in the [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element without being _tainted_. The allowed values are:

[`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#anonymous)

Sends a cross-origin request without a credential. In other words, it sends the `Origin:` HTTP header without a cookie, X.509 certificate, or performing HTTP Basic authentication. If the server does not give credentials to the origin site (by not setting the `Access-Control-Allow-Origin:` HTTP header), the resource will be _tainted_, and its usage restricted.

[`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#use-credentials)

Sends a cross-origin request with a credential. In other words, it sends the `Origin:` HTTP header with a cookie, a certificate, or performing HTTP Basic authentication. If the server does not give credentials to the origin site (through `Access-Control-Allow-Credentials:` HTTP header), the resource will be _tainted_ and its usage restricted.

When not present, the resource is fetched without a CORS request (i.e., without sending the `Origin:` HTTP header), preventing its non-tainted use in [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 elements. If invalid, it is handled as if the enumerated keyword **anonymous** was used. See [CORS settings attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 for additional information.

[`disableremoteplayback`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#disableremoteplayback)

A Boolean attribute used to disable the capability of remote playback in devices that are attached using wired (HDMI, DVI, etc.) and wireless technologies (Miracast, Chromecast, DLNA, AirPlay, etc.). See the proposed [Remote Playback API specification](https://w3c.github.io/remote-playback/#the-disableremoteplayback-attribute "External link (opens in new tab)")
 for more information.

In Safari, you can use [`x-webkit-airplay="deny"`](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/OptingInorOutofAirPlay/OptingInorOutofAirPlay.html "External link (opens in new tab)")
 as a fallback.

[`loading`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#loading)

Indicates how the browser should load the audio:

[`eager`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#eager)

Loads the audio immediately, regardless of whether or not the audio is currently within the visible viewport (this is the default value).

[`lazy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#lazy)

Defers loading the audio until the controls reach a calculated distance from the viewport, as defined by the browser.

**Note:** In order for audio elements to intersect visibly with the viewport, they need to be visible. Browsers use the `controls` attribute to make audio elements visible, so it's needed for lazy loading. Lazy-loaded audio without the `controls` attribute will not load.

Lazy loading avoids the network and storage bandwidth required to handle the audio until it's reasonably certain that it will be needed. This improves the performance in most typical use cases.

Lazy-loaded audio located in the visual viewport may not yet be downloaded when the Window [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event "load")
 event is fired. This is because the event is fired based on eager-loaded audio only — lazy-loaded audio is not considered even if it is located within the visual viewport upon initial page load.

Loading is only deferred when JavaScript is enabled. This is an anti-tracking measure, because if a user agent supported lazy loading when scripting is disabled, it would still be possible for a site to track a user's approximate scroll position throughout a session, by strategically placing audio in a page's markup such that a server can track how many audio requests are made and when.

**Note:** The `loading="lazy"` attribute also impacts the [`autoplay`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#autoplay)
 attribute as described in that section of this page.

[`loop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#loop)

A Boolean attribute: if specified, the audio player will automatically seek back to the start upon reaching the end of the audio.

[`muted`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#muted)

A Boolean attribute that indicates the default audio mute setting contained in the audio. If set, the audio will be initially silenced. Its default value is `false`, meaning the audio will be heard when the audio is played.

**Note:** To unmute, setting `muted="false"` will not work; the audio will be muted if the attribute is present at all. To unmute, the attribute must be removed entirely.

[`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#preload)

This [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute is intended to provide a hint to the browser about what the author thinks will lead to the best user experience. It may have one of the following values:

*   `none`: Indicates that the audio should not be preloaded.
*   `metadata`: Indicates that only audio metadata (e.g., length) is fetched.
*   `auto`: Indicates that the whole audio file can be downloaded, even if the user is not expected to use it.
*   _empty string_: A synonym of the `auto` value.

The default value is different for each browser. The spec advises it to be set to `metadata`.

**Note:**

*   Audio with the [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#loading)
     attribute set will only apply the `preload` behavior once the audio controls are near or within the viewport.
*   The `autoplay` attribute has precedence over `preload`. If `autoplay` is specified, the browser would obviously need to start downloading the audio for playback.
*   The browser is not forced by the specification to follow the value of this attribute; it is a mere hint.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#src)

The URL of the audio to embed. This is subject to [HTTP access controls](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
. This is optional; you may instead use the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element within the audio block to specify the audio to embed.

[Events](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#events)

--------------------------------------------------------------------------------------------

[`audioprocess`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode/audioprocess_event "audioprocess")

The input buffer of a [`ScriptProcessorNode`](https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode)
 is ready to be processed.

[`canplay`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplay_event "canplay")

The browser can play the media, but estimates that not enough data has been loaded to play the media up to its end without having to stop for further buffering of content.

[`canplaythrough`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event "canplaythrough")

The browser estimates it can play the media up to its end without stopping for content buffering.

[`complete`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/complete_event "complete")

The rendering of an [`OfflineAudioContext`](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext)
 is terminated.

[`durationchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/durationchange_event "durationchange")

The `duration` attribute has been updated.

[`emptied`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/emptied_event "emptied")

The media has become empty; for example, this event is sent if the media has already been loaded (or partially loaded), and the [`HTMLMediaElement.load`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/load)
 method is called to reload it.

[`ended`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ended_event "ended")

Playback has stopped because the end of the media was reached.

[`loadeddata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event "loadeddata")

The first frame of the media has finished loading.

[`loadedmetadata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event "loadedmetadata")

The metadata has been loaded.

[`loadstart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadstart_event "loadstart")

Fired when the browser has started to load the resource.

[`pause`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/pause_event "pause")

Playback has been paused.

[`play`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play_event "play")

Playback has begun.

[`playing`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/playing_event "playing")

Playback is ready to start after having been paused or delayed due to lack of data.

[`ratechange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event "ratechange")

The playback rate has changed.

[`seeked`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeked_event "seeked")

A _seek_ operation completed.

[`seeking`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeking_event "seeking")

A _seek_ operation began.

[`stalled`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/stalled_event "stalled")

The user agent is trying to fetch media data, but data is unexpectedly not forthcoming.

[`suspend`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/suspend_event "suspend")

Media data loading has been suspended.

[`timeupdate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event "timeupdate")

The time indicated by the `currentTime` attribute has been updated.

[`volumechange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volumechange_event "volumechange")

The volume has changed.

[`waiting`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/waiting_event "waiting")

Playback has stopped because of a temporary lack of data.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#usage_notes)

------------------------------------------------------------------------------------------------------

Browsers don't all support the same [file types](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers)
 and [audio codecs](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs)
; you can provide multiple sources inside nested [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 elements, and the browser will then use the first one it understands:

The audio source can be set to any valid [URL](https://developer.mozilla.org/en-US/docs/Web/URI)
, including HTTP(S) URLs and [Data URLs](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
. When using HTTP(S) URLs, be aware that the browser's caching behavior will affect how often the file is requested from the server. Data URLs embed the audio data directly in the HTML, which can be useful for small audio files but isn't recommended for larger files as it increases the HTML file size.

When using [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 elements, the browser attempts to load each source sequentially. If a source fails (e.g., due to an invalid URL or unsupported format), the next source is attempted, and so on. An `error` event fires on the `<audio>` element after all sources have failed; `error` events are not fired on each individual `<source>` element.

You can also use the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
 to directly generate and manipulate audio streams from JavaScript code rather than streaming pre-existing audio files. You can set the [`srcObject`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/srcObject)
 in JavaScript to a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)
 object. This is commonly used for live audio streams or real-time audio processing.

Note that `MediaStream` sources have limitations: they are not seekable and only support a limited set of codecs.

We offer a substantive and thorough [guide to media file types](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
 and the [audio codecs that can be used within them](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs)
. Also available is [a guide to the codecs supported for video](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs)
.

Other usage notes:

*   If you don't specify the `controls` attribute, the audio player won't include the browser's default controls. You can, however, create your own custom controls using JavaScript and the [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
     API.
*   To allow precise control over your audio content, `HTMLMediaElement`s fire many different [events](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement#events)
    . This also provides a way to monitor the audio's fetching process so you can watch for errors or detect when enough is available to begin to play or manipulate it.
*   `<audio>` elements can't have subtitles or captions associated with them in the same way that `<video>` elements can. See [WebVTT and Audio](https://www.iandevlin.com/blog/2015/12/html5/webvtt-and-audio/ "External link (opens in new tab)")
     by Ian Devlin for some useful information and workarounds.
*   To test the fallback content on browsers that support the element, you can replace `<audio>` with a non-existing element like `<notanaudio>`.

A good general source of information on using HTML `<audio>` is the [HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
 beginner's tutorial.

### [Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#styling_with_css)

The `<audio>` element has no intrinsic visual output of its own unless the `controls` attribute is specified, in which case the browser's default controls are shown.

The default controls have a [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of `inline` by default, and it is often a good idea to set the value to `block` to improve control over positioning and layout, unless you want it to sit within a text block or similar.

You can style the default controls with properties that affect the block as a single unit, so for example you can give it a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 and [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, etc. You can't however style the individual components inside the audio player (e.g., change the button size or icons, change the font, etc.), and the controls are different across the different browsers.

To get a consistent look and feel across browsers, you'll need to create custom controls; these can be marked up and styled in whatever way you want, and then JavaScript can be used along with the [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
 API to wire up their functionality.

[Video player styling basics](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Video_player_styling_basics)
 provides some useful styling techniques — it is written in the context of `<video>`, but much of it is equally applicable to `<audio>`.

### [Detecting addition and removal of tracks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#detecting_addition_and_removal_of_tracks)

You can detect when tracks are added to and removed from an `<audio>` element using the [`addtrack`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList/addtrack_event "addtrack")
 and [`removetrack`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList/removetrack_event "removetrack")
 events. However, these events aren't sent directly to the `<audio>` element itself. Instead, they're sent to the track list object within the `<audio>` element's [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
 that corresponds to the type of track that was added to the element:

[`HTMLMediaElement.audioTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/audioTracks)

An [`AudioTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList)
 containing all of the media element's audio tracks. You can add a listener for `addtrack` to this object to be alerted when new audio tracks are added to the element.

[`HTMLMediaElement.videoTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/videoTracks)

Add an `addtrack` listener to this [`VideoTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList)
 object to be informed when video tracks are added to the element.

[`HTMLMediaElement.textTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/textTracks)

Add an `addtrack` event listener to this [`TextTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/TextTrackList)
 to be notified when new text tracks are added to the element.

**Note:** Even though it's an `<audio>` element, it still has video and text track lists, and can in fact be used to present video, although the user interface implications can be odd.

For example, to detect when audio tracks are added to or removed from an `<audio>` element, you can use code like this:

This code watches for audio tracks to be added to and removed from the element, and calls a hypothetical function on a track editor to register and remove the track from the editor's list of available tracks.

You can also use [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener "addEventListener()")
 to listen for the [`addtrack`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList/addtrack_event "addtrack")
 and [`removetrack`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList/removetrack_event "removetrack")
 events.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#accessibility)

----------------------------------------------------------------------------------------------------------

Audio with spoken dialog should provide both captions and transcripts that accurately describe its content. Captions, which are specified using [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
, allow people who are hearing impaired to understand an audio recording's content as the recording is being played, while transcripts allow people who need additional time to be able to review the recording's content at a pace and format that is comfortable for them.

If automatic captioning services are used, it is important to review the generated content to ensure it accurately represents the source audio.

The `<audio>` element doesn't directly support WebVTT. You will have to find a library or framework that provides the capability for you, or write the code to display captions yourself. One option is to play your audio using a [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
 element, which does support WebVTT.

In addition to spoken dialog, subtitles and transcripts should also identify music and sound effects that communicate important information. This includes emotion and tone. For example, in the WebVTT below, note the use of square brackets to provide tone and emotional insight to the viewer; this can help establish the mood otherwise provided using music, nonverbal sounds and crucial sound effects, and so forth.

1
00:00:00 --> 00:00:45
\[Energetic techno music\]

2
00:00:46 --> 00:00:51
Welcome to the Time Keeper's podcast! In this episode we're discussing which Swisswatch is a wrist switchwatch?

16
00:00:52 --> 00:01:02
\[Laughing\] Sorry! I mean, which wristwatch is a Swiss wristwatch?

Also it's a good practice to provide some content (such as the direct download link) as a fallback for viewers who use a browser in which the `<audio>` element is not supported:

*   [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [WebAIM: Captions, Transcripts, and Audio Descriptions](https://webaim.org/techniques/captions/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.2 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.2_%E2%80%94_providing_text_alternatives_for_time-based_media)
    
*   [Understanding Success Criterion 1.2.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/media-equiv-av-only-alt.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 1.2.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/media-equiv-captions.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#examples)

------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#basic_usage)

The following example shows basic usage of the `<audio>` element to play an OGG file. It will autoplay due to the `autoplay` attribute—if the page has permission to do so—and also includes fallback content.

For details on when autoplay works, how to get permission to use autoplay, and how and when it's appropriate to use autoplay, see our [autoplay guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)
.

### [<audio> element with <source> element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#audio_element_with_source_element)

This example specifies which audio track to embed using the `src` attribute on a nested `<source>` element rather than directly on the `<audio>` element. It is always useful to include the file's MIME type inside the `type` attribute, as the browser is able to instantly tell if it can play that file, and not waste time on it if not.

### [<audio> with multiple <source> elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#audio_with_multiple_source_elements)

This example includes multiple `<source>` elements. The browser tries to load the first source element (Opus) if it is able to play it; if not it falls back to the second (Vorbis) and finally back to MP3:

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, phrasing content, embedded content. If it has a [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#controls)<br> attribute: interactive content and palpable content. |
| Permitted content | If the element has a [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#src)<br> attribute: zero or more [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)<br> elements followed by transparent content that contains no `<audio>` or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)<br> media elements.  <br>Else: zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)<br> elements followed by zero or more [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)<br> elements followed by transparent content that contains no `<audio>` or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)<br> media elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role) |
| DOM interface | [`HTMLAudioElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-audio-element](https://html.spec.whatwg.org/multipage/media.html#the-audio-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio#see_also)

------------------------------------------------------------------------------------------------

*   [Web media technologies](https://developer.mozilla.org/en-US/docs/Web/Media)
    
    *   [Media container formats (file types)](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers)
        
    *   [Guide to audio codecs used on the web](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs)
        
*   [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
    
*   [`HTMLAudioElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement)
    
*   [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
    
*   [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)
    
*   [Learning area: HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
    
*   [Cross-browser audio basics](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Cross-browser_audio_basics)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/audio/index.md?plain=1 "Folder: en-us/web/html/reference/elements/audio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Faudio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Faudio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Faudio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Faudio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1aa0dbd7441564e6ce8f6706c2022a2e1912d8c%0A*+Document+last+modified%3A+2026-07-16T11%3A25%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
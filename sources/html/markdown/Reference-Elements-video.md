*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#mdn-search)
    

`<video>` HTML video embed element
==================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<video>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element embeds a media player which supports video playback into the document. You can use `<video>` for audio content as well, but the [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
 element may provide a more appropriate user experience.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#try_it)

--------------------------------------------------------------------------------------------

    <video controls width="250">
      <source src="/shared-assets/videos/flower.webm" type="video/webm" />
    
      <source src="/shared-assets/videos/flower.mp4" type="video/mp4" />
    
      Download the
      <a href="/shared-assets/videos/flower.webm">WEBM</a>
      or
      <a href="/shared-assets/videos/flower.mp4">MP4</a>
      video.
    </video>
    

The above example shows how to use the `<video>` element. Similar to the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, we include a path to the media we want to display inside the `src` attribute; we can include other attributes to specify information such as video width and height, whether we want it to autoplay and loop, or to show the browser's default video controls, and so on.

The content inside the opening and closing `<video></video>` tags is shown as a fallback in browsers that don't support the element.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#attributes)

----------------------------------------------------------------------------------------------------

Like all other HTML elements, this element supports the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`autoplay`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#autoplay)

A Boolean attribute; if specified, the video automatically begins to play back as soon as it can without stopping to finish loading the data.

**Note:** Modern browsers block audio (or videos with an unmuted audio track) from autoplaying, as sites that automatically play audio can be an unpleasant experience for users. See our [autoplay guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay)
 for additional information about how to properly use autoplay.

To disable video autoplay, `autoplay="false"` will not work; the video will autoplay if the attribute is there in the `<video>` tag at all. To remove autoplay, the attribute needs to be removed altogether.

**Note:** Videos with the [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#loading)
 attribute set will not start downloading and autoplaying until the element is near or within the viewport.

[`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#controls)

If this attribute is present, the browser will offer controls to allow the user to control video playback, including volume, seeking, and pause/resume playback.

[`controlslist`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#controlslist)

The [`controlslist`](https://wicg.github.io/controls-list/explainer.html "External link (opens in new tab)")
 attribute, when specified, helps the browser select what controls to show for the `video` element whenever the browser shows its own set of controls (that is, when the `controls` attribute is specified).

The allowed values are `nodownload`, `nofullscreen` and `noremoteplayback`.

Use the [`disablepictureinpicture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#disablepictureinpicture)
 attribute if you want to disable the Picture-In-Picture mode (and the control).

[`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)

This [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicates whether to use CORS to fetch the related video. [CORS-enabled resources](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)
 can be reused in the [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element without being _tainted_. The allowed values are:

[`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#anonymous)

Sends a cross-origin request without a credential. In other words, it sends the `Origin:` HTTP header without a cookie, X.509 certificate, or performing HTTP Basic authentication. If the server does not give credentials to the origin site (by not setting the `Access-Control-Allow-Origin:` HTTP header), the resource will be _tainted_, and its usage restricted.

[`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#use-credentials)

Sends a cross-origin request with a credential. In other words, it sends the `Origin:` HTTP header with a cookie, a certificate, or performing HTTP Basic authentication. If the server does not give credentials to the origin site (through `Access-Control-Allow-Credentials:` HTTP header), the resource will be _tainted_ and its usage restricted.

When not present, the resource is fetched without a CORS request (i.e., without sending the `Origin:` HTTP header), preventing its non-tainted use in [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 elements. If invalid, it is handled as if the enumerated keyword `anonymous` was used. See [CORS settings attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 for additional information.

[`disablepictureinpicture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#disablepictureinpicture)

Prevents the browser from suggesting a Picture-in-Picture context menu or to request Picture-in-Picture automatically in some cases.

[`disableremoteplayback`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#disableremoteplayback)

A Boolean attribute used to disable the capability of remote playback in devices that are attached using wired (HDMI, DVI, etc.) and wireless technologies (Miracast, Chromecast, DLNA, AirPlay, etc.).

In Safari, you can use [`x-webkit-airplay="deny"`](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/OptingInorOutofAirPlay/OptingInorOutofAirPlay.html "External link (opens in new tab)")
 as a fallback.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#height)

The height of the video's display area, in [CSS pixels](https://drafts.csswg.org/css-values/#px "External link (opens in new tab)")
 (absolute values only; [no percentages](https://html.spec.whatwg.org/multipage/embedded-content.html#dimension-attributes "External link (opens in new tab)")
).

[`loading`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#loading)

Indicates how the browser should load the video (including any poster image):

[`eager`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#eager)

Loads the video immediately, regardless of whether or not the video is currently within the visible viewport (this is the default value).

[`lazy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#lazy)

Defers loading the video until it reaches a calculated distance from the viewport, as defined by the browser.

Lazy loading avoids the network and storage bandwidth required to handle the video until it's reasonably certain that it will be needed. This improves the performance in most typical use cases.

While explicit [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#height)
 attributes are recommended for all videos to avoid layout shift, they are especially important for lazy-loaded ones. Lazy-loaded videos will never be loaded if they do not intersect a visible part of an element, even if loading them would change that, because unloaded videos have a `width` and `height` of `0`. It creates an even more disruptive user experience when the content visible in the viewport reflows in the middle of reading it.

Lazy-loaded videos located in the visual viewport may not yet be visible when the Window [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event "load")
 event is fired. This is because the event is fired based on eager-loaded videos — lazy-loaded videos are not considered even if they are located within the visual viewport upon initial page load.

Loading is only deferred when JavaScript is enabled. This is an anti-tracking measure, because if a user agent supported lazy loading when scripting is disabled, it would still be possible for a site to track a user's approximate scroll position throughout a session, by strategically placing videos in a page's markup such that a server can track how many videos are requested and when.

**Note:** The `loading="lazy"` attribute also impacts the [`autoplay`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#autoplay)
, [`poster`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#poster)
, and [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#preload)
 attributes, as described in each of those sections of the page.

[`loop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#loop)

A Boolean attribute; if specified, the browser will automatically seek back to the start upon reaching the end of the video.

[`muted`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#muted)

A Boolean attribute that indicates the default audio mute setting contained in the video. If set, the audio will be initially silenced. Its default value is `false`, meaning the audio will be heard when the video is played.

**Note:** To unmute, setting `muted="false"` will not work; the audio will be muted if the attribute is present at all. To unmute, the attribute must be removed entirely.

[`playsinline`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#playsinline)

A Boolean attribute indicating that the video is to be played "inline", that is, within the element's playback area. Note that the absence of this attribute _does not_ imply that the video will always be played in fullscreen.

[`poster`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#poster)

A URL for an image to be shown while the video is downloading. If this attribute isn't specified, nothing is displayed until the first frame is available, then the first frame is shown as the poster frame.

**Note:** Videos with the [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#loading)
 attribute set will only download the `poster` resource once the video is near or within the viewport.

[`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#preload)

This [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute is intended to provide a hint to the browser about what the author thinks will lead to the best user experience regarding what content is loaded before the video is played. It may have one of the following values:

*   `none`: Indicates that the video should not be preloaded.
*   `metadata`: Indicates that only video metadata (e.g., length) is fetched.
*   `auto`: Indicates that the whole video file can be downloaded, even if the user is not expected to use it.
*   _empty string_: A synonym of the `auto` value.

The default value is different for each browser. The spec advises it to be set to `metadata`.

**Note:**

*   Videos with the [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#loading)
     attribute set will only apply the `preload` behavior once the video is near or within the viewport.
*   The `autoplay` attribute has precedence over `preload`. If `autoplay` is specified, the browser would obviously need to start downloading the video for playback.
*   The specification does not force the browser to follow the value of this attribute; it is a mere hint.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#src)

The URL of the video to embed. This is optional; you may instead use the [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 element within the video block to specify the video to embed.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#width)

The width of the video's display area, in [CSS pixels](https://drafts.csswg.org/css-values/#px "External link (opens in new tab)")
 (absolute values only; [no percentages](https://html.spec.whatwg.org/multipage/embedded-content.html#dimension-attributes "External link (opens in new tab)")
).

[Events](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#events)

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

The media has become empty; for example, this event is sent if the media has already been loaded (or partially loaded), and the [`load()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/load)
 method is called to reload it.

[`ended`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ended_event "ended")

Playback has stopped because the end of the media was reached.

[`error`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/error_event "error")

An error occurred while fetching the media data, or the type of the resource is not a supported media format.

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

[`progress`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/progress_event "progress")

Fired periodically as the browser loads a resource.

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

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#usage_notes)

------------------------------------------------------------------------------------------------------

Browsers don't all support the same video formats; you can provide multiple sources inside nested [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 elements, and the browser will then use the first one it understands.

html

    <video controls>
      <source src="myVideo.webm" type="video/webm" />
      <source src="myVideo.mp4" type="video/mp4" />
      <p>
        Your browser doesn't support HTML video. Here is a
        <a href="myVideo.mp4" download="myVideo.mp4">link to the video</a> instead.
      </p>
    </video>
    

When using [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
 elements, the browser attempts to load each source sequentially. If a source fails (e.g., due to an invalid URL or unsupported format), the next source is attempted, and so on. An `error` event fires on the `<video>` element after all sources have failed; `error` events are not fired on each individual `<source>` element.

We offer a substantive and thorough [guide to media file types](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
 and the [guide to the codecs supported for video](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs)
. Also available is a guide to [audio codecs that can be used with them](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs)
.

Other usage notes:

*   If you don't specify the `controls` attribute, the video won't include the browser's default controls; you can create your own custom controls using JavaScript and the [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
     API. See [Creating a cross-browser video player](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/cross_browser_video_player)
     for more details.
*   To allow precise control over your video (and audio) content, `HTMLMediaElement`s fire many different [events](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement#events)
    . In addition to providing controllability, these events let you monitor the progress of both download and playback of the media, as well as the playback state and position.
*   You can use the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
     property to adjust the positioning of the video within the element's frame, and the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
     property to control how the video's size is adjusted to fit within the frame.
*   To show subtitles/captions along with your video, you can use some JavaScript along with the [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)
     element and the [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
     format. See [Adding captions and subtitles to HTML video](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video)
     for more information.
*   You can play audio files using a `<video>` element. This can be useful if, for example, you need to perform audio with a [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
     transcript, since the [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
     element doesn't allow captions using WebVTT.
*   To test the fallback content on browsers that support the element, you can replace `<video>` with a non-existing element like `<notavideo>`.

A good general source of information on using HTML `<video>` is the [HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
 beginner's tutorial.

### [Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#styling_with_css)

The `<video>` element is a replaced element — its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value is `inline` by default — but its default width and height in the viewport is defined by the video being embedded.

There are no special considerations for styling `<video>`; a common strategy is to give it a `display` value of `block` to make it easier to position, size, etc., and then provide styling and layout information as required. [Video player styling basics](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Video_player_styling_basics)
 provides some useful styling techniques.

### [Adding subtitles and other timed text tracks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#adding_subtitles_and_other_timed_text_tracks)

Timed text tracks for subtitles, closed captions, chapter headings, and so on, can be added declaratively by nesting the [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)
 element. The tracks are specified in [Web Video Text Tracks File Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format)
 (`.vtt` files).

For example, the HTML below includes the file "captions.vtt", which will be used to overlay closed captions on the video if captions are enabled by the user.

html

    <video controls src="video.webm">
      <track default kind="captions" src="captions.vtt" />
    </video>
    

Timed text tracks can also be added programmatically using the [WebVTT API](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
.

### [Detecting track addition and removal](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#detecting_track_addition_and_removal)

You can detect when tracks are added to and removed from a `<video>` element using the [`addtrack`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList/addtrack_event "addtrack")
 and [`removetrack`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList/removetrack_event "removetrack")
 events. However, these events aren't sent directly to the `<video>` element itself. Instead, they're sent to the track list object within the `<video>` element's [`HTMLMediaElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement)
 that corresponds to the type of track that was added to the element:

[`HTMLMediaElement.audioTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/audioTracks)

An [`AudioTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/AudioTrackList)
 containing all of the media element's audio tracks. Add a listener for `addtrack` to this object to be notified when new audio tracks are added to the element.

[`HTMLMediaElement.videoTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/videoTracks)

A [`VideoTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList)
 containing all of the media element's video tracks. Add an `addtrack` listener to this object to be notified when video tracks are added to the element.

[`HTMLMediaElement.textTracks`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/textTracks)

A [`TextTrackList`](https://developer.mozilla.org/en-US/docs/Web/API/TextTrackList)
 containing all of the media element's text tracks (which are used for subtitles, closed captions, and so on). Add an `addtrack` listener to this object to be notified when text tracks are added to the element.

For example, to detect when audio tracks are added to or removed from a `<video>` element, you can use code like this:

js

    const elem = document.querySelector("video");
    
    elem.audioTracks.onaddtrack = (event) => {
      trackEditor.addTrack(event.track);
    };
    
    elem.audioTracks.onremovetrack = (event) => {
      trackEditor.removeTrack(event.track);
    };
    

This code watches for audio tracks to be added to and removed from the element, and calls a hypothetical function on a track editor to register and remove the track from the editor's list of available tracks.

You can also use [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener "addEventListener()")
 to listen for the [`addtrack`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList/addtrack_event "addtrack")
 and [`removetrack`](https://developer.mozilla.org/en-US/docs/Web/API/VideoTrackList/removetrack_event "removetrack")
 events.

### [Server support for video](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#server_support_for_video)

If the MIME type for the video is not set correctly on the server, the video may not show or show a gray box containing an X (if JavaScript is enabled).

If you use Apache Web Server to serve WebM videos, you can fix this problem by adding the video file type extensions to the `video/webm` MIME type (the most common WebM file extension is `.webm`). To do this, edit the `mime.types` file in `/etc/apache` or use the `AddType` configuration directive in `httpd.conf`:

AddType video/webm .webm

Your web host may provide an easy interface to MIME type configuration changes for new technologies until a global update naturally occurs.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#accessibility)

----------------------------------------------------------------------------------------------------------

Videos should provide both captions and transcripts that accurately describe their content (see [Adding captions and subtitles to HTML video](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video)
 for more information on how to implement these). Captions allow people who are experiencing hearing loss to understand a video's audio content as the video is being played, while transcripts allow people who need additional time to be able to review audio content at a pace and format that is comfortable for them.

It's worth noting that while you can caption audio-only media, you can only do so when playing audio in a `<video>` element since the video region of the element is used to present the captions. This is one of the special scenarios in which it's useful to play audio in a video element.

If automatic captioning services are used, it is important to review the generated content to ensure it accurately represents the source video.

In addition to spoken dialog, subtitles and transcripts should also identify music and sound effects that communicate important information. This includes emotion and tone:

14
00:03:14 --> 00:03:18
\[Dramatic rock music\]

15
00:03:19 --> 00:03:21
\[whispering\] What's that off in the distance?

16
00:03:22 --> 00:03:24
It's… it's a…

16 00:03:25 --> 00:03:32
\[Loud thumping\]
\[Dishes clattering\]

Captions should not obstruct the main subject of the video. They can be positioned using [the `align` VTT cue setting](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format#cue_settings)
.

*   [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [WebAIM: Captions, Transcripts, and Audio Descriptions](https://webaim.org/techniques/captions/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.2 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.2_%E2%80%94_providing_text_alternatives_for_time-based_media)
    
*   [Understanding Success Criterion 1.2.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/media-equiv-av-only-alt.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 1.2.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/media-equiv-captions.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#examples)

------------------------------------------------------------------------------------------------

### [Single source](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#single_source)

This example plays a video when activated, providing the user with the browser's default video controls to control playback.

#### HTML

html

    <!-- Basic video example -->
    <!-- 'Big Buck Bunny' licensed under CC 3.0 by the Blender foundation. Hosted by archive.org -->
    <!-- Poster from peach.blender.org -->
    <video
      controls
      src="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4"
      poster="https://peach.blender.org/wp-content/uploads/title_anouncement.jpg?x11217"
      width="620">
      Sorry, your browser doesn't support embedded videos, but don't worry, you can
      <a href="https://archive.org/details/BigBuckBunny_124">download it</a>
      and watch it with your favorite video player!
    </video>
    

#### Result

Until the video starts playing, the image provided in the `poster` attribute is displayed in its place. If the browser doesn't support video playback, it displays the fallback text.

### [Multiple sources](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#multiple_sources)

This example builds on the last one, offering three different sources for the media; this allows the video to be watched regardless of which video codecs are supported by the browser.

#### HTML

html

    <!-- Using multiple sources as fallbacks for a video tag -->
    <!-- 'Elephants Dream' by Orange Open Movie Project Studio, licensed under CC-3.0, hosted by archive.org -->
    <!-- Poster hosted by Wikimedia -->
    <video
      width="620"
      controls
      poster="https://upload.wikimedia.org/wikipedia/commons/e/e8/Elephants_Dream_s5_both.jpg">
      <source
        src="https://archive.org/download/ElephantsDream/ed_hd.avi"
        type="video/avi" />
      <source
        src="https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"
        type="video/mp4" />
    
      Sorry, your browser doesn't support embedded videos, but don't worry, you can
      <a
        href="https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"
        download="ed_1024_512kb.mp4">
        download the MP4
      </a>
      and watch it with your favorite video player!
    </video>
    

#### Result

First AVI is tried. If that can't be played, [MP4](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers#mpeg-4_mp4)
 is tried. A fallback message is displayed if the video element isn't supported, but not if all sources fail.

Some media file types let you provide more specific information using the [`codecs`](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/codecs_parameter)
 parameter as part of the file's type string. For example, `video/webm; codecs="vp8, vorbis"` says that the file is a [WebM](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers#webm)
 video using [VP8](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs#vp8)
 for its video and [Vorbis](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs#vorbis)
 for audio.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, phrasing content, embedded content. If it has a [`controls`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#controls)<br> attribute: interactive content and palpable content. |
| Permitted content | If the element has a [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#src)<br> attribute: zero or more [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)<br> elements, followed by transparent content that contains no media elements–that is no [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)<br> or `<video>`.<br><br>Else: zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)<br> elements, followed by zero or more [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track)<br> elements, followed by transparent content that contains no media elements–that is no [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)<br> or `<video>`. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts embedded content. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role) |
| DOM interface | [`HTMLVideoElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-video-element](https://html.spec.whatwg.org/multipage/media.html#the-video-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video#see_also)

------------------------------------------------------------------------------------------------

*   [Guide to media types and formats on the web](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)
    
    *   [Media container formats (file types)](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers)
        
    *   [Web video codec guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Video_codecs)
        
    *   [Web audio codec guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs)
        
*   Positioning and sizing the picture within its frame: [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
     and [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    
*   [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
    
*   [HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
    
*   [Manipulating video using canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Manipulating_video_using_canvas)
    
*   [Configuring servers for Ogg media](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Configuring_servers_for_Ogg_media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/video/index.md?plain=1 "Folder: en-us/web/html/reference/elements/video (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fvideo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fvideo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fvideo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fvideo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1aa0dbd7441564e6ce8f6706c2022a2e1912d8c%0A*+Document+last+modified%3A+2026-07-16T11%3A25%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
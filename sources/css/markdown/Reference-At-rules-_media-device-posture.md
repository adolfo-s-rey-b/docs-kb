*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#mdn-search)
    

`device-posture` CSS media feature
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/270)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#browser_compatibility)
 carefully before using this in production.

The **`device-posture`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to detect the device's [current posture](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)
, that is, whether the viewport is in a flat (`continuous`) or folded state (`folded`).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#syntax)

-----------------------------------------------------------------------------------------------------------

The `device-posture` feature is specified as a keyword value chosen from the list below:

[`continuous`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#continuous)

Indicates a flat screen state. Foldable devices are `continuous` while they are flat; either fully opened or fully closed. Non-foldable devices are considered flat and therefore always `continuous` — this includes seamless curved displays and standard desktop, laptop, tablet, and mobile screens.

[`folded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#folded)

Indicates a folded screen state. Foldable devices are `folded` while used in a book or laptop posture.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#examples)

---------------------------------------------------------------------------------------------------------------

In this example, the `device-posture` media feature detects when a device is in a folded posture, adding a margin based on its [`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
 to create a larger gutter between the application's two panels for easier reading.

css

    @media (device-posture: folded) and (orientation: landscape) {
      .list-view {
        margin-inline-end: 60px;
      }
    }
    
    @media (device-posture: folded) and (orientation: portrait) {
      .list-view {
        margin-block-end: 60px;
      }
    }
    

To see the above code in action, view the [Device Posture API demo](https://mdn.github.io/dom-examples/device-posture-api/ "External link (opens in new tab)")
 on a foldable device if possible. Current browser developer tools enable emulating foldable devices, but don't include emulation of partially folded devices — only fully open or closed devices — so they will always return `continuous`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Device Posture API  <br>\# the-device-posture-media-feature](https://w3c.github.io/device-posture/#the-device-posture-media-feature) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`DevicePosture`](https://developer.mozilla.org/en-US/docs/Web/API/DevicePosture)
    
*   [Device Posture API](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)
    
*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/device-posture/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/device-posture (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-posture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-posture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdevice-posture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdevice-posture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
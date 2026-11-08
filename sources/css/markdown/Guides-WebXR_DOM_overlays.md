*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#mdn-search)
    

WebXR DOM overlays
==================

The **WebXR DOM overlays** module, an immersive web specification, expands the [WebXR Device API](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API)
 to allow HTML content — such as text and controls — to be displayed during an immersive virtual reality (VR) or augmented reality (AR) session.

In a typical WebXR session, content is rendered to a WebGL canvas superimposed on the real-world camera feed (in AR) or displayed as the full immersive view (in VR), with the device tracking the user's position and orientation. The DOM overlay renders a single DOM element and its descendants as a transparent-background 2D rectangle on top of this view, enabling interactive, stylable elements such as menus and dialogs to appear within the immersive experience.

The [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
 pseudo-class matches the DOM overlay element when a web page is being viewed in an immersive AR or VR environment, allowing it to be styled appropriately for its underlying content.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#reference)

--------------------------------------------------------------------------------------------------

### [Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#pseudo-classes)

*   [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
    

### [Events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#events)

*   [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
     events
    *   [`beforexrselect`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforexrselect_event "beforexrselect")
        

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#interfaces)

*   [`XRSession`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession)
    *   [`domOverlayState`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession/domOverlayState "domOverlayState")
         property

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#guides)

--------------------------------------------------------------------------------------------

[Fundamentals of WebXR](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API/Fundamentals)

Introduction to WebXR device API fundamentals.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#related_concepts)

----------------------------------------------------------------------------------------------------------------

*   [CSS pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    
    *   [`:modal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
        
    *   [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
        
    *   [`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
        
*   [WebXR Device API](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API)
    
    *   [`XRWebGLLayer`](https://developer.mozilla.org/en-US/docs/Web/API/XRWebGLLayer)
         interface

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Unknown specification](https://immersive-web.github.io/dom-overlays) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays#see_also)

------------------------------------------------------------------------------------------------

*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [CSSOM view module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view)
    
*   [CSSOM View API](https://developer.mozilla.org/en-US/docs/Web/API/CSSOM_view_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/webxr_dom_overlays/index.md?plain=1 "Folder: en-us/web/css/guides/webxr_dom_overlays (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWebXR_DOM_overlays&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fwebxr_dom_overlays%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWebXR_DOM_overlays%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fwebxr_dom_overlays%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F52a247932646cc4cb4b3a9bb50d7bd66d1fdc713%0A*+Document+last+modified%3A+2026-06-10T02%3A50%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
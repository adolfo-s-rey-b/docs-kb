*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#mdn-search)
    

`:xr-overlay` CSS pseudo-class
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/119)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#browser_compatibility)
 carefully before using this in production.

The **`:xr-overlay`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
, defined in the [WebXR DOM overlays](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays)
 module, matches the DOM overlay element when a web page is being viewed in an immersive AR or VR environment.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#syntax)

--------------------------------------------------------------------------------------------------

css

    :xr-overlay {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#description)

------------------------------------------------------------------------------------------------------------

The `:xr-overlay` pseudo-class matches the overlay element for the duration of an immersive session using a DOM overlay.

The overlay element is a [backdrop root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter#backdrop_root)
. Any [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 effects on the DOM overlay element or its descendants do not modify the AR camera image (if applicable) or the rendered content drawn to the immersive session's [`XRWebGLLayer`](https://developer.mozilla.org/en-US/docs/Web/API/XRWebGLLayer)
.

The overlay element itself is a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
 due to its fixed [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
. The stacking contexts for ancestors of the overlay element, if any, do not paint to the immersive session's display.

**Note:** On a multi-display system, the stacking contexts for ancestors or sibling trees of the overlay element may be displayed on separate displays.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#examples)

------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#basic_usage)

In this example, we define the overlay to be semi-transparent black, enabling content behind the overlay to be partially visible. To ensure enough contrast between content and its background, we set the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 to `white`.

css

    :xr-overlay {
      background-color: rgb(0 0 0 / 0.5);
      color: white;
    }
    

### [Targeting an overlay's contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#targeting_an_overlays_contents)

In this example, we use the `:xr-overlay` selector to style the [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements within an XR DOM overlay.

css

    :xr-overlay button {
      background-color: white;
      color: black;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [WebXR DOM Overlays Module  <br>\# selectordef-xr-overlay](https://immersive-web.github.io/dom-overlays/#selectordef-xr-overlay) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay#see_also)

------------------------------------------------------------------------------------------------------

*   [`:modal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
    
*   [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    
*   [`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
    
*   [CSS pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    
*   [WebXR DOM overlays](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/WebXR_DOM_overlays)
     module
*   [WebXR device API fundamentals](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API/Fundamentals)
    
*   [`XRSession.domOverlayState`](https://developer.mozilla.org/en-US/docs/Web/API/XRSession/domOverlayState)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_xr-overlay/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_xr-overlay (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Axr-overlay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_xr-overlay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Axr-overlay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_xr-overlay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff18c76e518179f2facc688464c5d382bf5a9b536%0A*+Document+last+modified%3A+2026-06-05T00%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
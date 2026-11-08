*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#mdn-search)
    

`display-mode` CSS media feature
================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/508)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`display-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test whether a web app is being displayed in a normal browser tab or in some alternative way, such as a standalone app or fullscreen mode.

For example:

*   A [progressive web app](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
     [can set its display mode](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Create_a_standalone_app)
     by setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display)
     member in its manifest. In this case, the value of `display-mode` identifies the value that was set (but note that this may not be the same as the value requested in the manifest, since a browser may not support the requested mode).
    
*   Any web app can use the [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
     or the [Document Picture-in-Picture API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Picture-in-Picture_API)
     to set the display mode, and in this case the value of `display-mode` identifies the mode that was set.
    

The `display-mode` value applies to the top-level browsing context and any child browsing contexts.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#syntax)

---------------------------------------------------------------------------------------------------------

The `display-mode` feature is specified as a keyword value chosen from the list below.

[`browser`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#browser)

The application opens in a conventional browser tab or new window, depending on the browser and platform.

[`fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#fullscreen)

All of the available display area is used and no user agent [chrome](https://developer.mozilla.org/en-US/docs/Glossary/Chrome)
 is shown. This can be used to apply CSS only when the app has been put in fullscreen mode by the [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)
 or by using the `fullscreen` value of the [`display`](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/display)
 member of the Wep App Manifest.

[`minimal-ui`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#minimal-ui)

The application will look and feel like a standalone application, but will have a minimal set of UI elements for controlling navigation. The elements will vary by browser.

[`picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#picture-in-picture)

This mode allows users to continue consuming specific content while they interact with other sites or applications on their device. The app is displayed in a floating and always-on-top window. This can be used to apply CSS only when the app has been put in Picture-in-Picture mode by the [Document Picture-in-Picture API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Picture-in-Picture_API)
.

[`standalone`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#standalone)

The application will look and feel like a standalone application. This can include the application having a different window, its own icon in the application launcher, etc. In this mode, the user agent will exclude UI elements for controlling navigation, but can include other UI elements such as a status bar.

[`window-controls-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#window-controls-overlay)

In this mode, the application looks and feels like a standalone desktop application, and the [Window Controls Overlay](https://developer.mozilla.org/en-US/docs/Web/API/Window_Controls_Overlay_API)
 feature is enabled.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#examples)

-------------------------------------------------------------------------------------------------------------

### [Apply CSS if the application is in fullscreen mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#apply_css_if_the_application_is_in_fullscreen_mode)

css

    @media (display-mode: fullscreen) {
      body {
        margin: 0;
        border: 5px solid black;
      }
    }
    

### [Provide a light and dark color scheme to Picture-in-Picture content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#provide_a_light_and_dark_color_scheme_to_picture-in-picture_content)

In this example, we combine the `display-mode: picture-in-picture` value with the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 media feature to create light and dark color schemes that are applied based on the user's color scheme preference, only when the app is being shown in Picture-in-Picture mode.

css

    @media (display-mode: picture-in-picture) and (prefers-color-scheme: light) {
      body {
        background: antiquewhite;
      }
    }
    
    @media (display-mode: picture-in-picture) and (prefers-color-scheme: dark) {
      body {
        background: #333333;
      }
    
      a {
        color: antiquewhite;
      }
    }
    

See [Using the Document Picture-in-Picture API](https://developer.mozilla.org/en-US/docs/Web/API/Document_Picture-in-Picture_API/Using)
 for more information and a full example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# display-modes](https://drafts.csswg.org/mediaqueries-5/#display-modes) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/display-mode/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/display-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdisplay-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdisplay-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fdisplay-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fdisplay-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#mdn-search)
    

CSS viewport
============

The **CSS viewport** module enables specifying the size, zoom factor, and orientation of the user-agent's initial containing block, or _viewport_.

Content designed for large viewports may exhibit a variety of bugs when viewed in smaller viewports, including unintended wrapping, clipped content, and incorrectly sized [scroll containers](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. HTML provides a [viewport meta tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
, `<meta name="viewport">`, to provide hints about the initial size of the viewport. If the site isn't designed to work well on small viewports and this tag is omitted, some mobile browsers render the site using a fixed initial containing block width, typically `980px`. The content is then scaled down, making the CSS pixel size smaller than an actual pixel. The resulting page fits into the available screen space but is illegible, requiring the user to zoom and pan to view the content.

The [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 initial containing block for continuous media has the dimensions of the viewport. Since the viewport is generally no larger than the display, devices with smaller displays, such as phones or tablets, typically present a smaller viewport than larger devices like desktops or laptops.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#reference)

----------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#properties)

*   [`zoom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/zoom)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#interfaces)

*   [`Window.Viewport`](https://developer.mozilla.org/en-US/docs/Web/API/Window/viewport)
    
*   [`Viewport`](https://developer.mozilla.org/en-US/docs/Web/API/Viewport)
    *   [`Viewport.segments`](https://developer.mozilla.org/en-US/docs/Web/API/Viewport/segments)
        

### [Glossary terms and definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#glossary_terms_and_definitions)

*   [Viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
    
*   [Actual viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#actual_viewport)
    
*   [Initial viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#initial_viewport)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#guides)

----------------------------------------------------------------------------------

[Viewport concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts)

The concept of the viewport — what it is, its impact in terms of CSS, SVG, and mobile devices — and the difference between the visual viewport and the layout viewport.

[Using environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables/Using)

An overview of what environment variables are, browser-defined environment variables, and how to use the `env()` function.

[Using the Viewport Segments API](https://developer.mozilla.org/en-US/docs/Web/API/Viewport_segments_API/Using)

Create responsive designs optimized for different viewport segment sizes and arrangements with the API and environment variables.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#related_concepts)

------------------------------------------------------------------------------------------------------

*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
    
    *   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
        
    *   [`horizontal-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)
         descriptor
    *   [`vertical-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments)
         descriptor
*   [CSS environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables)
    
    *   [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
        
    *   [`<environment-variable-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables/Using#browser-defined_environment_variables)
        
*   [Device Posture API](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#specifications)

--------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Viewport Module Level 1](https://drafts.csswg.org/css-viewport/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport#see_also)

--------------------------------------------------------------------------------------

*   [CSSOM view](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/viewport/index.md?plain=1 "Folder: en-us/web/css/guides/viewport (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FViewport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fviewport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FViewport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fviewport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
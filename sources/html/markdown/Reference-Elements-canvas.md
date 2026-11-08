*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#mdn-search)
    

`<canvas>` HTML graphics canvas element
=======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

Use the **HTML `<canvas>` element** with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
 or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)
 to draw graphics and animations.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#attributes)

-----------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#height)

The height of the coordinate space in CSS pixels. Defaults to 150.

[`moz-opaque`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#moz-opaque)

Lets the canvas know whether translucency will be a factor. If the canvas knows there's no translucency, painting performance can be optimized. This is only supported by Mozilla-based browsers; use the standardized [`canvas.getContext('2d', { alpha: false })`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext "canvas.getContext('2d', { alpha: false })")
 instead.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#width)

The width of the coordinate space in CSS pixels. Defaults to 300.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#usage_notes)

-------------------------------------------------------------------------------------------------------

### [Alternative content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#alternative_content)

You should provide alternate content inside the `<canvas>` block. That content will be rendered both on older browsers that don't support canvas and in browsers with JavaScript disabled.

### [Closing `</canvas>` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#closing_canvas_tag)

Unlike the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, the `<canvas>` element **requires** the closing tag (`</canvas>`).

### [Sizing the canvas using CSS versus HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#sizing_the_canvas_using_css_versus_html)

The displayed size of the canvas can be changed using CSS, but if you do this the image is scaled during rendering to fit the styled size, which can make the final graphics rendering end up being distorted.

It is better to specify your canvas dimensions by setting the `width` and `height` attributes directly on the `<canvas>` elements, either directly in the HTML or by using JavaScript.

### [Maximum canvas size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#maximum_canvas_size)

The exact maximum size of a `<canvas>` element depends on the browser and environment. While in most cases the maximum dimensions exceed 10,000 x 10,000 pixels, notably iOS devices limit the canvas size to only 4,096 x 4,096 pixels. See [canvas size limits in different browsers and devices](https://jhildenbiddle.github.io/canvas-size/#/?id=test-results "External link (opens in new tab)")
.

**Note:** Exceeding the maximum dimensions or area renders the canvas unusable — drawing commands will not work.

### [Using an offscreen canvas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#using_an_offscreen_canvas)

A canvas can be rendered using the [`OffscreenCanvas`](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas)
 API where the document and canvas are decoupled. The benefit is that a [worker thread](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
 can handle canvas rendering and the main thread of your web application is not blocked by canvas operations. By parallelizing work, other UI elements of your web application will remain responsive even if you are running complex graphics on an offscreen canvas. For more information, see the [`OffscreenCanvas`](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas)
 API documentation.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#accessibility)

-----------------------------------------------------------------------------------------------------------

### [Alternative content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#alternative_content_2)

The `<canvas>` element on its own is just a bitmap and does not provide information about any drawn objects. Canvas content is not exposed to accessibility tools as semantic HTML is. In general, you should avoid using canvas in an accessible website or app. The following guides can help to make it more accessible.

*   [Canvas accessibility use cases](https://www.w3.org/WAI/PF/HTML/wiki/Canvas_Accessibility_Use_Cases "External link (opens in new tab)")
    
*   [Canvas element accessibility issues](https://www.w3.org/html/wg/wiki/AddedElementCanvas "External link (opens in new tab)")
    
*   [Best practices for interactive canvas elements](https://html.spec.whatwg.org/multipage/scripting.html#best-practices "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#examples)

-------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#html)

This code snippet adds a canvas element to your HTML document. A fallback text is provided if a browser is unable to read or render the canvas.

html

    <canvas width="120" height="120">
      An alternative text describing what your canvas displays.
    </canvas>
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#javascript)

Then in the JavaScript code, call [`HTMLCanvasElement.getContext()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext)
 to get a drawing context and start drawing onto the canvas:

js

    const canvas = document.querySelector("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "green";
    // Add a rectangle at (10, 10) with size 100x100 pixels
    ctx.fillRect(10, 10, 100, 100);
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)<br>, palpable content. |
| Permitted content | Transparent but with no [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br> descendants except for [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)<br> elements, [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)<br> elements, [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)<br> elements whose [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)<br> attribute is `checkbox`, `radio`, or `button`. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLCanvasElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-canvas-element](https://html.spec.whatwg.org/multipage/canvas.html#the-canvas-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas#see_also)

-------------------------------------------------------------------------------------------------

*   [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
    
*   [Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
    
*   [OffscreenCanvas](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas)
    
*   [Canvas cheat sheet](https://simon.html5.org/dump/html5-canvas-cheat-sheet.html "External link (opens in new tab)")
     (2009)
*   [Canvas cheat sheet](https://websitesetup.org/wp-content/uploads/2015/11/Infopgraphic-CanvasCheatSheet-Final2.pdf "External link (opens in new tab)")
     (pdf) (2015)
*   [Safari HTML canvas guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/Introduction/Introduction.html "External link (opens in new tab)")
     via Apple (2013)
*   [`CanvasRenderingContext2D` 2D drawing context for a canvas element](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d "External link (opens in new tab)")
     via Apple.com
*   [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)
     API
*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
    
*   [HTML video and audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/canvas/index.md?plain=1 "Folder: en-us/web/html/reference/elements/canvas (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcanvas&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcanvas%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcanvas%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcanvas%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
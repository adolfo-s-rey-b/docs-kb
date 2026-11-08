*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#mdn-search)
    

Viewport concepts
=================

This article explains the concept of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 — what it is and its impact in terms of CSS, SVG, and mobile devices. This article defines the initial viewport and actual viewport, and differentiates between the [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport)
 and the [layout viewport](https://developer.mozilla.org/en-US/docs/Glossary/Layout_viewport)
.

[What is a viewport?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#what_is_a_viewport)

-------------------------------------------------------------------------------------------------------------------------------

A **viewport** is a user agent feature used to establish the initial containing block for continuous media.

The generic _viewport_ term generally refers to the area in computer graphics being currently viewed. In web browser terms, that is generally the same as the browser window, excluding the UI, menu bar, etc. That is the part of the document you are viewing.

As a document loads, the viewport goes through two stages:

[**Initial viewport**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#initial_viewport)

The _initial viewport_ refers to the window or viewing area of the UA before user agent styles, HTML [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 tags, or CSS styles have overridden its size. The initial viewport size is based on the size of the window or viewing area, and not the content. The size of a full-screen user agent's initial viewport will differ between orientations and devices, but will always be the same for the same device in the same orientation.

[**Actual viewport**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#actual_viewport)

The _actual viewport_ is the viewport you get after processing the [viewport `<meta>` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
. Content designed for large viewports may exhibit a variety of bugs when viewed in smaller viewports, including unintended wrapping, clipped content, and incorrectly sized [scroll containers](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. The viewport meta tag provides hints about the initial size of the viewport. The actual viewport is the size defined by its [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute. If this tag is omitted, some mobile browsers render content using a fixed initial containing block width, typically `980px`. They set the width of the actual viewport to this value, then scale the content down to fit it, making the CSS pixel size smaller than an actual pixel.

Documents, like this article, may be very long. Your viewport is everything that is currently visible; notably, the "what is a viewport" section, and perhaps some of the navigation menu. The size of the viewport depends on the size of the screen, whether the browser is in fullscreen mode or not, and whether or not the browser is zoomed in. Content outside the viewport, such as the _See Also_ section in this document, is likely to not be visible onscreen until scrolled into view.

*   On larger monitors where applications aren't necessarily full screen, the viewport is the size of the browser window.
*   On most mobile devices and when the browser is in fullscreen mode, the viewport is the entire screen.
*   In fullscreen mode, the viewport is the device screen, the window is the browser window, which can be as big as the viewport or smaller, and the document is the website, which can be much taller or wider than the viewport.

For [paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
, the initial containing block is based on the page area. The page area can be set through [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 rules.

To recap, the viewport is basically the part of the document that is currently visible.

### [Viewport sizes are mutable](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#viewport_sizes_are_mutable)

The width of the viewport is not always the width of the window. If you query the width or height of the window and document in Chrome or Firefox, you may get:

There are several DOM properties that can help you query viewport size, and other similar lengths:

*   The document element's [`Element.clientWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Element/clientWidth)
     is the inner width of a document in [CSS pixels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#screen_density)
    , including padding (but not borders, margins, or vertical scrollbars, if present). **This is the viewport width**.
*   The [`Window.innerWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth)
     is the width, in CSS pixels, of the browser window viewport including, if rendered, the vertical scrollbar.
*   The [`Window.outerWidth`](https://developer.mozilla.org/en-US/docs/Web/API/Window/outerWidth)
     is the width of the outside of the browser window including all the window [chrome](https://developer.mozilla.org/en-US/docs/Glossary/Chrome)
    .

In an experiment with these, the `innerWidth` and `outerWidth` was seen to be the same, but the `outerHeight` was 100px taller than the `innerHeight`. This is because the `outerHeight` includes the browser chrome: measurements were taken on a browser with an address bar and bookmarks bar totaling 100px in height, but no chrome on the left or right of the window.

The area within the `innerHeight` and `innerWidth` is generally considered the **[layout viewport](https://developer.mozilla.org/en-US/docs/Glossary/Layout_viewport)
**. The browser chrome is not considered part of the viewport.

When zoomed in, both Firefox and Chrome report the new [CSS pixel](https://developer.mozilla.org/en-US/docs/Glossary/CSS_pixel)
 size for `innerWidth` and `clientWidth`. The values returned for the `outerWidth` and `outerHeight` depend on the browser: Firefox reports the new value in CSS pixels, but Chrome returns the length in the default pixel size. When zoomed in you may get:

The viewport was originally 1200 x 800 pixels. Upon zooming in, the viewport became 800 x 533 pixels. This is the _layout viewport_. Sticky headers or footers, with the following styles, will stick to the top and bottom of the _layout viewport_ respectively.

We got the 800 x 533 measurement when we zoomed in using the keyboard. The header and footer stayed flush against the top and bottom of the window. But what if we had pinched-zoomed on a tablet? What if a dynamic keyboard pops open on a phone?

### [Layout and visual viewports](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#layout_and_visual_viewports)

The web contains two viewports, the **layout viewport** and the **visual viewport**. The visual viewport is the part of the web page that is currently visible in the browser and can change. When the user pinch-zooms the page, pops open a dynamic keyboard, or when a previously hidden address bar becomes visible, the visual viewport shrinks but the layout viewport is unchanged.

[Fixed](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#fixed_positioning)
 sticky headers or footers, as discussed above, stick to the top and bottom of the _layout viewport_, and therefore remain in view when we zoom in with the keyboard. If you pinch-zoom, the layout viewport may not be fully visible. If you magnify from the middle of the layout viewport, the content will expand in all four directions. If you have a sticky header or footer, they will still be stuck to the top or bottom of the layout viewport, but they may not be visible at the top and bottom of the device's screen — which is the visual viewport. The visual viewport is the currently visible portion of the layout viewport. If you scroll down, you are changing the contents of the visual viewport and bringing the bottom of the layout viewport into view, displaying the sticky footer, which will then stay stuck at the bottom.

The visual viewport is the visual portion of a screen not including on-screen keyboards, areas outside of a pinch-zoom area, or other feature that doesn't scale with the dimensions of a page. The visual viewport is the same size as the layout viewport or smaller.

For a page containing iframes, objects, or external SVG, both the containing pages and each included file has their own unique window object. Only the top-level window has a visual viewport that may be distinct from the layout viewport. For included documents, the visual viewport and layout viewport are the same.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#css)

The layout viewport and visual viewport described above are not the only viewports you will encounter. Any sub-viewport that is fully or partially displayed within the layout viewport is considered a visual viewport.

We generally think of [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/height)
 media queries as being relative to the width and height of the browser window. They are actually relative to the viewport, which is the window in the main document but is the intrinsic size of the element's parent in a nested browsing context like objects, iframes and SVG. In CSS, we also have [length units based on the viewport size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#viewport_units)
. A `vh` unit is 1% of the layout viewport's height. Similarly, the `vw` unit is 1% of the layout viewport's width.

#### `<iframe>`

Inside an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
, the visual viewport is the size of the inner width and height of the iframe, rather than the parent document. You can set any height and width on an iframe, but the whole document may not be visible.

If you use [viewport length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#viewport_units)
 in your CSS within the iframe document, `1vh` will be 1% of the height of the iframe, and `1vw` will be 1% of the width of the document.

If the iframe is set to 50vw, it will be 50% of the width of the `1200px` parent document in our example above, or `600px`, with `1vw` being `6px`. When zoomed in, the iframe shrinks to `400px` and `1vw` becomes `4px`.

A width-based media query within the iframe document is relative to the iframe's viewport.

If the above CSS is included in the iframe, the paragraphs will become red when the user has zoomed in, but this style does not apply in the non-zoomed-in state.

#### SVG

In an [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 document, the viewport is the visible area of the SVG image. You can set any height and width on an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
, but the whole image might not be visible. The area that is visible is called the viewport. The size of the viewport can be defined using the width and height attributes of the `<svg>` element.

In this example, the viewport has an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of 3:4 and is, by default, 400 by 300 units, with a unit generally being a CSS pixel.

SVG also has an internal [coordinate system](https://developer.mozilla.org/en-US/docs/Web/API/CSSOM_view_API/Coordinate_systems)
 defined via the [viewBox](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute, which is not related to this viewport discussion.

If you include an SVG file in your HTML, the viewport of the SVG is the initial containing block, or the width and height of the SVG container. Using the [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 query in your SVG's CSS is relative to that container, not the browser.

Generally, when you write the above media query, the styles are applied if the viewport, generally the browser window, is between 400px and 500px, inclusive. The width media query in the SVG is based on the element in which the SVG is contained — the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 if the source is an SVG file, the SVG itself if the SVG is included directly into the HTML, or the parent if the parent element has a width assigned and — not the viewport's width. With the above media query being in our SVG file, the CSS is applied if the SVG container is between 400px and 500px.

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#javascript)

The [`VisualViewport`](https://developer.mozilla.org/en-US/docs/Web/API/VisualViewport#examples)
 interface provides a mechanism for querying and modifying the properties of the visual viewport.

The [`Viewport`](https://developer.mozilla.org/en-US/docs/Web/API/Viewport)
 interface provides a mechanism for querying and modifying the properties of the visual viewport.

[Mobile viewports](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#mobile_viewports)

--------------------------------------------------------------------------------------------------------------------------

Mobile devices come in all shapes and sizes, with screens of differing [device pixel](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel)
 ratios. The mobile browser's viewport is the area of the window in which web content can be seen, which is not necessarily the same size as the rendered page. Mobile browsers render pages in a virtual window or viewport, generally at 980px, which is usually wider than the screen, and then shrink the rendered result down so it can all be seen at once. Users can then pan and zoom to see different areas of the page. For example, if a mobile screen has a width of 320px, a website might be rendered with a virtual viewport of 980px, and then it will be shrunk down to fit into the 320px space, which, depending on the design, is illegible for many if not everyone. To tell a mobile browser to use the viewport width instead of the default 980px as the width of the screen, developers can include a viewport meta tag, like the following:

The `width` property controls the size of the viewport. It should preferably be set to `device-width`, which is the width of the screen in CSS pixels at a scale of 100%. There are other properties, including `maximum-scale`, `minimum-scale`, and `user-scalable`, which control whether users can zoom the page in or out, but the default values are the best for accessibility and user experience, so these can be omitted.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSSOM view](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view)
     module
*   [CSSOM view API](https://developer.mozilla.org/en-US/docs/Web/API/CSSOM_view_API)
    
*   [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
    , specifically [`<meta name="viewport">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
    
*   [CSS viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Viewport)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cssom_view/viewport_concepts/index.md?plain=1 "Folder: en-us/web/css/guides/cssom_view/viewport_concepts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCSSOM_view%2FViewport_concepts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcssom_view%2Fviewport_concepts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCSSOM_view%2FViewport_concepts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcssom_view%2Fviewport_concepts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd00cd7171957c1510c2e7ff855196df01530a09c%0A*+Document+last+modified%3A+2026-10-11T18%3A49%3A39.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
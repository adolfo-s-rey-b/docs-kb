*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#mdn-search)
    

`<meta name="viewport">` HTML attribute value
=============================================

The **`viewport`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of a [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element gives hints about how the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 should be sized.

If specified, you define viewport-related behaviors using a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute in the `<meta>` element as a comma-separated list of one or more values.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#usage_notes)

-------------------------------------------------------------------------------------------------------------------

A `<meta name="viewport">` element has the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

The `content` attribute must be defined, and its value sets various viewport-related behaviors. Its value is a comma-separated list of one or more key-value pairs specified as `key=value`. The following keys are defined:

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#width)

Controls the (minimum) pixel width of the viewport (see [viewport width and screen width](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#viewport_width_and_screen_width)
). It can be set to a positive whole number of pixels between 1 and 10000 (like `width=600`) or to the special value `device-width`, which is the physical size of the device screen in CSS pixels. This value establishes the value of the [`vw`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport)
 unit.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#height)

Controls the (minimum) pixel height of the viewport (see [viewport width and screen width](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#viewport_width_and_screen_width)
). It can be set to a positive whole number of pixels between 1 and 10000 (like `height=400`) or to the special value `device-height`, which is the physical size of the device screen in CSS pixels. This value establishes the value of the [`vh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport)
 unit.

[`initial-scale`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#initial-scale)

Defines the ratio between the device width (`device-width` in portrait mode or `device-height` in landscape mode) and the viewport size. It can be a number between `0.0` and `10.0`.

[`maximum-scale`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#maximum-scale)

Defines the maximum amount to zoom in. It must be greater or equal to the `minimum-scale` or the behavior is undefined. Browser settings can ignore this rule, and iOS10+ ignores it by default. It can be a number between `0.0` and `10.0`.

[`minimum-scale`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#minimum-scale)

Defines the minimum zoom level. It must be smaller or equal to the `maximum-scale` or the behavior is undefined. Browser settings can ignore this rule, and iOS10+ ignores it by default. It can be a number between `0.0` and `10.0`.

[`user-scalable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#user-scalable)

A boolean indicating if the user can zoom the web page. Browser settings can ignore this rule, and iOS10+ ignores it by default. It can be either `yes` or `no`, defaulting to `yes`.

**Warning:** Disabling zooming capabilities by setting `user-scalable` to a value of `no` prevents people experiencing low vision conditions from being able to read and understand page content. Additionally, WCAG requires a minimum of 2× scaling; however, the best practice is to enable a 5× zoom. For more information, see:

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.4 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-scale.html "External link (opens in new tab)")
    

[`interactive-widget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#interactive-widget)

Specifies the effect that interactive UI widgets, such as virtual keyboards, have on a page's viewport. It can be the keyword `resizes-visual`, `resizes-content`, or `overlays-content`.

*   `resizes-visual`: The [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport)
     gets resized by the interactive widget. This is the default.
*   `resizes-content`: The [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
     gets resized by the interactive widget.
*   `overlays-content`: Neither the viewport nor the visual viewport gets resized by the interactive widget.

When the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 gets resized, the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 also gets resized, thereby affecting the computed size of [viewport units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport)
.

[`viewport-fit`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#viewport-fit)

Defines the viewable portions of the web page. It can be one of the keywords `auto`, `contain`, or `cover`.

*   `auto`: Doesn't affect the initial layout viewport, and the whole web page is viewable.
*   `contain`: The viewport is scaled to fit the largest rectangle inscribed within the display.
*   `cover`: The viewport is scaled to fill the device display. It's highly recommended to use the [safe area inset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
     variables to ensure that important content doesn't end up outside the display.

### [Viewport width and screen width](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#viewport_width_and_screen_width)

The browser's [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 is the area of the window in which web content can be seen. The viewport size needs to be computed before the page's content can be laid out—the page can overflow the viewport, in which case the browser provides scrollbars for the user to scroll around and access all the content, but the viewport size is the guideline for how much space, especially horizontally, the content should fit into.

Some mobile devices and other narrow screens render pages in a virtual window or viewport that is wider than the screen, and then shrink the rendered result down to fit the screen size. Users can then zoom and pan to look more closely at different areas of the page. For example, if a mobile screen has a width of 640px, pages might be rendered with a virtual viewport of 980px, and then it will be shrunk down to fit into the 640px space. This is done because not all pages are optimized for mobile and break (or at least look bad) when rendered at a small viewport width. This virtual viewport is a way to make non-mobile-optimized sites in general look better on narrow screen devices. However, this mechanism is not so good for pages that are optimized for narrow screens using [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
 — if the virtual viewport is 980px for example, media queries that kick in at 640px or 480px or less will never be used, limiting the effectiveness of such responsive design techniques. The viewport `<meta>` element mitigates this problem of virtual viewport on narrow screen devices.

The recommended setting is the following, which sets the viewport to match the device's width:

**Note:** This example omits `initial-scale=1`, a common practice that's usually unnecessary. When it is omitted, the browser determines the initial zoom level automatically and may zoom out when content overflows the viewport. The amount of scaling is browser-dependent and may depend on both the content's width and height. Add `initial-scale=1` if overflowing content causes unwanted shrinking and you want the page to start at 100% zoom instead; however, you should usually avoid overflowing content horizontally.

Sites can set their viewport to a specific size. For example, the definition `"width=320, initial-scale=1"` can be used to fit precisely onto a small phone display in portrait mode. This can cause problems when the browser renders a page at a larger size. To fix this, browsers will expand the viewport width if necessary to fill the screen at the requested scale. This is especially useful on large-screen devices.

For pages that set an initial or maximum scale, this means the `width` property actually translates into a _minimum_ viewport width. For example, if your layout needs at least 500 pixels of width then you can use the following markup. When the screen is more than 500 pixels wide, the browser will expand the viewport (rather than zoom in) to fit the screen:

### [Screen density](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#screen_density)

Screen resolutions have risen to the size that individual pixels are indistinguishable by the human eye. For example, smartphones often have small screens with resolutions upwards of 1920–1080 pixels (≈400dpi). Because of this, many browsers can display their pages in a smaller physical size by translating multiple hardware pixels for each CSS "pixel". Initially, this caused usability and readability problems on many touch-optimized websites.

On high dpi screens, pages with `initial-scale=1` will effectively be zoomed by browsers. Their text will be smooth and crisp, but their bitmap images may not take advantage of the full screen resolution. To get sharper images on these screens, web developers may want to design images – or whole layouts – at a higher scale than their final size and then scale them down using CSS or viewport properties.

The default pixel ratio depends on the display density. On a display with density less than 200dpi, the ratio is 1.0. On displays with density between 200 and 300dpi, the ratio is 1.5. For displays with density over 300dpi, the ratio is the integer floor (_density_/150dpi). Note that the default ratio is true only when the viewport scale equals 1. Otherwise, the relationship between CSS pixels and [device pixels](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel)
 depends on the current zoom level.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#examples)

-------------------------------------------------------------------------------------------------------------

### [Using a meta viewport size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#using_a_meta_viewport_size)

The following example indicates to the browser that the page should be rendered at the device width:

### [Using a media query with a viewport meta](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#using_a_media_query_with_a_viewport_meta)

The following `content` value uses multiple keywords that hint to the browser to use fullscreen mode, along with `viewport-fit`, which helps avoid display cutouts such as mobile device notches:

### [The effect of interactive UI widgets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#the_effect_of_interactive_ui_widgets)

Interactive UI widgets of the browser can influence the size of the page's viewports. The most common such UI widget is a virtual keyboard. To control which resize behavior the browser should use, set the `interactive-widget` property.

By default, the virtual keyboard only resizes the visual viewport, which doesn't affect the layout of the page. You can make the page's layout adapt to the presence of the virtual keyboard by setting the `interactive-widget` property to `resizes-content`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Viewport Module Level 1  <br>\# viewport-meta](https://drafts.csswg.org/css-viewport/#viewport-meta) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport#see_also)

-------------------------------------------------------------------------------------------------------------

*   [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
     glossary term
*   [Prepare for viewport resize behavior changes coming to Chrome on Android](https://developer.chrome.com/blog/viewport-resize-behavior/ "External link (opens in new tab)")
     on developer.chrome.com
*   [Mobile viewports for responsive experiences](https://experienceleague.adobe.com/en/docs/target/using/experiences/vec/mobile-viewports "External link (opens in new tab)")
     on Adobe Experience League

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 23, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/viewport/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/viewport (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Fviewport&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Fviewport%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Fviewport%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Fviewport%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1402df2877308c09ea2aa1460f1c97c634bd7624%0A*+Document+last+modified%3A+2026-09-23T21%3A11%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
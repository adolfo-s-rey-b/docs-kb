*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#mdn-search)
    

`@media` CSS at-rule
====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@media`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 can be used to apply part of a style sheet based on the result of one or more [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
. With it, you specify a media query and a block of CSS to apply to the document if and only if the media query matches the device on which the content is being used.

**Note:** In JavaScript, the rules created using `@media` can be accessed with the [`CSSMediaRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSMediaRule)
 CSS object model interface.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#try_it)

--------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#syntax)

--------------------------------------------------------------------------------------------

The `@media` at-rule may be placed at the top level of your code or nested inside any other conditional group at-rule.

For a discussion of media query syntax, please see [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#syntax)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#description)

------------------------------------------------------------------------------------------------------

A media query's `<media-query-list>` includes [`<media-type>`s](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
, [`<media-feature>s`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
, and [logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#logical_operators)
.

### [Media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)

A _`<media-type>`_ describes the general category of a device. Except when using the `only` logical operator, the media type is optional and the `all` type is implied.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#all)

Suitable for all devices.

[`print`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#print)

Intended for paged material and documents viewed on a screen in print preview mode. (Please see [paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
 for information about formatting issues that are specific to these formats.)

[`screen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#screen)

Intended primarily for screens.

**Note:** CSS2.1 and [Media Queries 3](https://drafts.csswg.org/mediaqueries-3/#background "External link (opens in new tab)")
 defined several additional media types (`tty`, `tv`, `projection`, `handheld`, `braille`, `embossed`, and `aural`, but they were deprecated in [Media Queries 4](https://drafts.csswg.org/mediaqueries/#media-types "External link (opens in new tab)")
 and shouldn't be used.

### [Media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)

A _`<media feature>`_ describes specific characteristics of the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
, output device, or environment. Media feature expressions test for their presence, value, or range of values, and are entirely optional. Each media feature expression must be surrounded by parentheses.

[`any-hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-hover)

Does any available input mechanism allow the user to hover over elements?

[`any-pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer)

Is any available input mechanism a pointing device, and if so, how accurate is it?

[`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio)

Width-to-height [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of the viewport.

[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color)

Number of bits per color component of the output device, or zero if the device isn't color.

[`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)

Approximate range of colors that are supported by the user agent and output device.

[`color-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-index)

Number of entries in the output device's color lookup table, or zero if the device does not use such a table.

[`device-aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio)

Width-to-height aspect ratio of the output device. Deprecated in Media Queries Level 4.

[`device-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-height)

Height of the rendering surface of the output device. Deprecated in Media Queries Level 4.

[`device-posture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture)

Detects the device's current posture, that is, whether the viewport is in a flat or folded state. Defined in the [Device Posture API](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)
.

[`device-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width)

Width of the rendering surface of the output device. Deprecated in Media Queries Level 4.

[`display-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode)

The mode in which an application is being displayed: for example, [fullscreen](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#fullscreen)
 or [picture-in-picture](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode#picture-in-picture)
 mode. Added in Media Queries Level 5.

[`dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range)

Combination of brightness, contrast ratio, and color depth that are supported by the user agent and the output device. Added in Media Queries Level 5.

[`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)

Detect whether user agent restricts color palette. Added in Media Queries Level 5.

[`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid)

Does the device use a grid or bitmap screen?

[`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/height)

Height of the viewport.

[`horizontal-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)

Detects whether the device has a specified number of viewport segments laid out horizontally.

[`hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover)

Does the primary input mechanism allow the user to hover over elements?

[`inverted-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors)

Is the user agent or underlying OS inverting colors? Added in Media Queries Level 5.

[`monochrome`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/monochrome)

Bits per pixel in the output device's monochrome frame buffer, or zero if the device isn't monochrome.

[`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)

Orientation of the viewport.

[`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-block)

How does the output device handle content that overflows the viewport along the block axis?

[`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline)

Can content that overflows the viewport along the inline axis be scrolled?

[`pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer)

Is the primary input mechanism a pointing device, and if so, how accurate is it?

[`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)

Detect if the user prefers a light or dark color scheme. Added in Media Queries Level 5.

[`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)

Detects if the user has requested the system increase or decrease the amount of contrast between adjacent colors. Added in Media Queries Level 5.

[`prefers-reduced-data`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-data)

Detects if the user has requested the web content that consumes less internet traffic.

[`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)

The user prefers less motion on the page. Added in Media Queries Level 5.

[`prefers-reduced-transparency`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency)

Detects if a user has enabled a setting on their device to reduce the transparent or translucent layer effects used on the device.

[`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)

Pixel density of the output device.

[`scan`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan)

Whether display output is progressive or interlaced.

[`scripting`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scripting)

Detects whether scripting (i.e., JavaScript) is available. Added in Media Queries Level 5.

[`shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/shape)

Detects the shape of the device to distinguish rectangular and round displays.

[`update`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/update)

How frequently the output device can modify the appearance of content.

[`vertical-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments)

Detects whether the device has a specified number of viewport segments laid out vertically. Added in Media Queries Level 5.

[`video-dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/video-dynamic-range)

Combination of brightness, contrast ratio, and color depth that are supported by the video plane of user agent and the output device. Added in Media Queries Level 5.

[`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)

Width of the viewport including width of scrollbar.

[`-moz-device-pixel-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-moz-device-pixel-ratio)

The number of device pixels per CSS pixel. Use the [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
 feature with the `dppx` unit instead.

[`-webkit-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-animation)

The browser supports `-webkit` prefixed CSS [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
. Use the [`@supports (animation)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

[`-webkit-device-pixel-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-device-pixel-ratio)

The number of device pixels per CSS pixel. Use the [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
 feature with the `dppx` unit instead.

[`-webkit-transform-2d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-2d)

The browser supports `-webkit` prefixed 2D CSS [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
. Use the [`@supports (transform)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

[`-webkit-transform-3d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d)

The browser supports `-webkit` prefixed 3D CSS [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
. Use the [`@supports (transform)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

[`-webkit-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition)

The browser supports `-webkit` prefixed CSS [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
. Use the [`@supports (transition)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

### [Logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#logical_operators)

The _logical operators_ `not`, `and`, `only`, and `or` can be used to compose a complex media query. You can also combine multiple media queries into a single rule by separating them with commas.

[`and`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#and)

Used for combining multiple media features together into a single media query, requiring each chained feature to return `true` for the query to be `true`. It is also used for joining media features with media types.

[`not`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#not)

Used to negate a media query, returning `true` if the query would otherwise return `false`. If present in a comma-separated list of queries, it will only negate the specific query to which it is applied.

**Note:** In Level 3, the `not` keyword can't be used to negate an individual media feature expression, only an entire media query.

[`only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#only)

Applies a style only if an entire query matches. It is useful for preventing older browsers from applying selected styles. When not using `only`, older browsers would interpret the query `screen and (width <= 500px)` as `screen`, ignoring the remainder of the query, and applying its styles on all screens. If you use the `only` operator, you _must also_ specify a media type.

[`,` (comma)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#sect)

Commas are used to combine multiple media queries into a single rule. Each query in a comma-separated list is treated separately from the others. Thus, if any of the queries in a list is `true`, the entire media statement returns `true`. In other words, lists behave like a logical `or` operator.

[`or`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#or)

Equivalent to the `,` operator. Added in Media Queries Level 4.

### [User agent client hints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#user_agent_client_hints)

Some media queries have corresponding [user agent client hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Client_hints)
. These are HTTP headers that request content that is pre-optimized for the particular media requirement. They include [`Sec-CH-Prefers-Color-Scheme`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Color-Scheme)
 and [`Sec-CH-Prefers-Reduced-Motion`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Reduced-Motion)
.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#formal_syntax)

----------------------------------------------------------------------------------------------------------

@media =   
  @media <media-query-list> { [<rule-list>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
 }    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#accessibility)

----------------------------------------------------------------------------------------------------------

To best accommodate people who adjust a site's text size, use [`em`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types)
s when you need a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 for your [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
.

Both [`em`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types)
 and [`px`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types)
 are valid units, but [`em`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types)
 works better if the user changes the browser text size.

Also consider media queries or [HTTP user agent client hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints)
 to improve the user's experience. For example, the media query [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 or the equivalent HTTP header [`Sec-CH-Prefers-Reduced-Motion`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Reduced-Motion)
 can be used to minimize the amount of animation or motion used based on user preferences.

[Security](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#security)

------------------------------------------------------------------------------------------------

Because media queries provide insights into the capabilities—and by extension, the features and design—of the device the user is working with, there is the potential that they could be abused to construct a ["fingerprint"](https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting)
 which identifies the device, or at least categorizes it to some degree of detail that may be undesirable to users.

Because of this potential, a browser may opt to fudge the returned values in some manner in order to prevent them from being used to precisely identify a computer. A browser might also offer additional measures in this area; for example, if Firefox's "Resist Fingerprinting" setting is enabled, many media queries report default values rather than values representing the actual device state.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#examples)

------------------------------------------------------------------------------------------------

### [Testing for print and screen media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#testing_for_print_and_screen_media_types)

The range syntax allows for less verbose media queries when testing for any feature accepting a range, as shown in the below examples:

For more examples, please see [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# media-descriptor-table](https://drafts.csswg.org/mediaqueries/#media-descriptor-table) |
| [CSS Conditional Rules Module Level 3  <br>\# at-media](https://drafts.csswg.org/css-conditional-3/#at-media) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#see_also)

------------------------------------------------------------------------------------------------

*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
*   [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [`CSSMediaRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSMediaRule)
     interface
*   CSS [`@custom-media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media)
     at-rule
*   [Extended Mozilla media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#media_features)
    
*   [Extended WebKit media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions#media_features)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
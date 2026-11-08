*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#mdn-search)
    

Using media queries
===================

**Media queries** allow you to apply CSS styles depending on a device's media type (such as print vs. screen) or other features or characteristics such as screen resolution or orientation, [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
, browser [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 width or height, user preferences such as preferring reduced motion, data usage, or transparency.

Media queries are used for the following:

*   To conditionally apply styles with the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
     [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    , [`@custom-media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media)
     and [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
     [at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    .
*   To target specific media for the [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    , [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
    , [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)
    , and other [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
     elements with the `media=` or `sizes="` attributes.
*   To [test and monitor media states](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing)
     using the [`Window.matchMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)
     and [`EventTarget.addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
     methods.

**Note:** The examples on this page use CSS's `@media` for illustrative purposes, but the basic syntax remains the same for all types of media queries.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#syntax)

---------------------------------------------------------------------------------------------

A media query is composed of an optional _media type_ and any number of _media feature_ expressions, which may optionally be combined in various ways using _logical operators_. Media queries are case-insensitive.

*   [Media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
     define the broad category of device for which the media query applies: `all`, `print`, `screen`.
    
    The type is optional (assumed to be `all`) except when using the `only` logical operator.
    
*   [Media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
     describe a specific characteristic of the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
    , output device, or environment:
    
    *   [`any-hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-hover)
        
    *   [`any-pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer)
        
    *   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio)
        
    *   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color)
        
    *   [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
        
    *   [`color-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-index)
        
    *   [`device-aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio)
        
    *   [`device-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-height)
        
    *   [`device-posture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture)
        
    *   [`device-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width)
        
    *   [`display-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode)
        
    *   [`dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range)
        
    *   [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
        
    *   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid)
        
    *   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/height)
        
    *   [`hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover)
        
    *   [`inverted-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors)
        
    *   [`monochrome`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/monochrome)
        
    *   [`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
        
    *   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-block)
        
    *   [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline)
        
    *   [`pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer)
        
    *   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
        
    *   [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
        
    *   [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
        
    *   [`prefers-reduced-transparency`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency)
        
    *   [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
        
    *   [`scripting`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scripting)
        
    *   [`update`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/update)
        
    *   [`video-dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/video-dynamic-range)
        
    *   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)
        
    
    For example, the [`hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover)
     feature allows a query to check whether the device supports hovering over elements. Media feature expressions test for their presence or value, and are entirely optional. Each media feature expression must be surrounded by parentheses.
    
*   [Logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#logical_operators)
     can be used to compose a complex media query: `not`, `and`, and `only`. You can also combine multiple media queries into a single rule by separating them with commas.
    

A media query computes to `true` when the media type (if specified) matches the device on which a document is being displayed _and_ all media feature expressions compute as true. Queries involving unknown media types are always false.

**Note:** A style sheet with a media query attached to its [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 tag [will still download](https://scottjehl.github.io/CSS-Download-Tests/ "External link (opens in new tab)")
 even if the query returns `false`, the download will happen but the priority of downloading will be much lower. Nevertheless, its contents will not apply unless and until the result of the query changes to `true`. You can read why this happens in Tomayac's blog [Why Browsers Download Stylesheets With Non-Matching Media Queries](https://medium.com/@tomayac/why-browsers-download-stylesheets-with-non-matching-media-queries-eb61b91b85a2 "External link (opens in new tab)")
.

[Targeting media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#targeting_media_types)

---------------------------------------------------------------------------------------------------------------------------

Media types describe the general category of a given device. Although websites are commonly designed with screens in mind, you may want to create styles that target special devices such as printers or audio-based screen readers. For example, this CSS targets printers:

You can also target multiple devices. For instance, this `@media` rule uses two media queries to target both screen and print devices:

See [media types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
 for the list of available media types. Because media types describe devices in very broad terms, most of the originally-defined media types were deprecated, with just `screen`, `print`, and `all` remaining. To target more specific attributes, use _media features_ instead.

[Targeting media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#targeting_media_features)

---------------------------------------------------------------------------------------------------------------------------------

Media features describe the specific characteristics of a given [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
, output device, or environment. For instance, you can apply specific styles to widescreen monitors, computers that use mice, or devices that are being used in low-light conditions. This example applies styles when the user's _primary_ input mechanism (such as a mouse) can hover over elements:

Media features are either range or discrete.

_Discrete features_ take their value from an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 set of possible keyword values. For example, the discrete `orientation` feature accepts either `landscape` or `portrait`.

Many _range features_ can be prefixed with "min-" or "max-" to express "minimum condition" or "maximum condition" constraints. For example, this CSS will apply styles only if your browser's [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 width is equal to or narrower than 1250px:

The following media queries are equivalent to the above example:

With media query range features, you can either use the inclusive `min-` and `max-` prefixes or the more concise range syntax operators `<=` and `>=`.

The following media queries are equivalent:

The range comparisons above are inclusive. To exclude the comparison value, use `<` and/or `>`.

If you create a media feature query without specifying a value, the nested styles will be used as long as the feature's value is not `0` or `none`. For example, this CSS will apply to any device with a color screen:

If a feature doesn't apply to the device on which the browser is running, expressions involving that media feature are always false.

For more [Media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 examples, please see the reference page for each specific feature.

[Creating complex media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#creating_complex_media_queries)

---------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to create a media query that depends on multiple conditions. This is where the _logical operators_ come in: `not`, `and`, and `only`. Furthermore, you can combine multiple media queries into a comma-separated list; this allows you to apply the same styles in different situations, with the contained media queries evaluated as a logical `or` composition: interpreted as if each media query were within parentheses with an `or` between them.

In the previous example, we saw the `and` operator used to group a media _type_ with a media _feature_. The `and` operator can also combine multiple media features within a single media query. The `not` operator negates a media query, or a media feature when used with brackets, basically reversing their normal meanings. The `or` operator can, under certain conditions, be used to combine multiple media features within a single media query. Lastly, the `only` operator was used to prevent older browsers from applying the styles without evaluating the media feature expressions but it has no effect in modern browsers.

**Note:** In most cases, the `all` media type is used by default when no other type is specified. However, if you use the `only` operator, you must explicitly specify a media type. You can see `only screen` or `only print` as a whole.

### [Combining multiple types or features](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#combining_multiple_types_or_features)

The `and` keyword combines a media feature with a media type _or_ other media features. This example combines two media features to restrict styles to landscape-oriented devices with a width of at least 30 ems:

To limit the styles to devices with a screen, you can chain the media features to the `screen` media type:

### [Testing for multiple queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#testing_for_multiple_queries)

You can use a comma-separated list of media queries to apply styles when the user's device matches any one of various media types, features, or states.

The following rule contains two media queries. The block's styles will apply if either the user's device has a height of 680px or more _or_ if the browser viewport is in portrait mode (the viewport height is greater than the viewport width):

In this example, if the user is printing to a PDF and the page height is 800px, the media query returns true because the first query component — which tests whether the viewport has a height of `680px` or more — is true. Likewise, if a user is on a smartphone in portrait mode with a viewport height of 480px, the media query returns true because the second query component is true.

In a comma-separated list of media queries, the individual media queries end at the comma or, in the case of the last media query in the list, at the opening bracket (`{`).

### [Inverting a query's meaning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#inverting_a_querys_meaning)

The `not` keyword inverts the meaning of a single media query. For example, the CSS styles in this media query will apply to everything _except_ printed media:

The `not` negates only the media query it is applied to. The `not`, without parenthesis, negates all the features within the media query in which it is contained. This means, in a comma-separated list of media queries, each `not` applies to the single query it is contained within, applying to _all_ the features within that single query. In this example, the `not` applies to the first media query `screen and (color)`, which concludes at the first comma:

Because the query starts with a media type `screen`, you _cannot_ wrap `screen and (color)` with parentheses. On the other hand, if your media query consists of features only, then you _must_ parenthesize the query:

Parentheses limit the components of the query that get negated. For example, to negate the `(width > 1000px)` query only:

`not` only negates the query to its right. In this example, we negate the `hover` media feature but not the `screen` media type:

The `not (hover)` matches if the device has no hover capability. In this case, because of its ordering, the `not` applies to `hover` but not to `screen`.

### [Improving compatibility with older browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#improving_compatibility_with_older_browsers)

The `only` keyword prevents older browsers that do not support media queries with media features from applying the given styles. _It has no effect on modern browsers._

### [Testing for multiple features with `or`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#testing_for_multiple_features_with_or)

You can use `or` to test for a match among more than one feature, resolving to `true` if any of the features are true. For example, the following query tests for devices that have a monochrome display or hover capability:

Note that you cannot use the `or` operator on the same level as the `and` and `not` operators. You can either separate the media features with a comma or use parenthesis to group sub-expressions of media features to clarify the order of evaluation.

For example, the following queries are both valid:

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#see_also)

-------------------------------------------------------------------------------------------------

*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Testing media queries programmatically](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing)
    
*   [CSS Animations Between Media Queries](https://davidwalsh.name/animate-media-queries "External link (opens in new tab)")
    
*   [Extended Mozilla media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#media_features)
    
*   [Extended WebKit media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions#media_features)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/media_queries/using/index.md?plain=1 "Folder: en-us/web/css/guides/media_queries/using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FUsing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fusing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FUsing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fusing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F44eeeccd6f2799db65aedaf2d23290d20057ce9e%0A*+Document+last+modified%3A+2026-09-08T00%3A03%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
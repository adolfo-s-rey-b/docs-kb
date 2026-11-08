*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#mdn-search)
    

CSS media queries
=================

The **CSS media queries** module enables testing and querying of viewport values and browser or device features, to conditionally apply CSS styles based on the current user environment. Media queries are used in the CSS `@media` rule and other contexts and languages such as HTML and JavaScript.

Media queries are a key component of [responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
. They enable conditional setting of CSS styles depending on the presence or value of device characteristics. It's common to use a media query based on [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 size to set appropriate layouts on devices with different screen sizes — for example three columns on a wide screen or a single column on a narrow screen.

Other common examples include increasing the font size and hiding navigation menus when printing a page, adjusting the padding between paragraphs when a page is viewed in portrait or landscape mode, or increasing the size of buttons to provide a larger hit area on touchscreens.

In [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
, use the [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 to conditionally apply part of a style sheet based on the result of a media query. To conditionally apply an entire style sheet, use [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
.

When designing reusable HTML components, you may also use [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
, which allow you to apply styles based on the size of a containing element rather than the viewport or other device characteristics.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#reference)

---------------------------------------------------------------------------------------------

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#at-rules_and_descriptors)

*   [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
    
*   [`@custom-media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media)
    
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    *   [`any-hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-hover)
        
    *   [`any-pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer)
        
    *   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio)
        
    *   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color)
        
    *   [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
        
    *   [`color-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-index)
        
    *   [`device-aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio)
        
    *   [`device-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-height)
        
    *   [`device-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width)
        
    *   [`display-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/display-mode)
        
    *   [`dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range)
        
    *   [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
        
    *   [`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/grid)
        
    *   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/height)
        
    *   [`horizontal-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/horizontal-viewport-segments)
        
    *   [`hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover)
        
    *   [`inverted-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors)
        
    *   [`monochrome`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/monochrome)
        
    *   [`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
        
    *   [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-block)
        
    *   [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline)
        
    *   [`pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer)
        
    *   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
        
    *   [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
        
    *   [`prefers-reduced-data`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-data)
        
    *   [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
        
    *   [`prefers-reduced-transparency`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency)
        
    *   [`resolution`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/resolution)
        
    *   [`scan`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scan)
        
    *   [`scripting`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/scripting)
        
    *   [`update`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/update)
        
    *   [`vertical-viewport-segments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/vertical-viewport-segments)
        
    *   [`video-dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/video-dynamic-range)
        
    *   [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/width)
        

The CSS media queries level 5 module also introduces the `environment-blending`, `nav-controls`, and `video-color-gamut` `@media` descriptors. Currently, no browsers support these features.

**Note:** CSS media queries level 4 deprecated three `@media` descriptors: [`device-aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-aspect-ratio)
, [`device-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-height)
, and [`device-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-width)
.

### [Data types and operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#data_types_and_operators)

*   [`<media-types>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
    
*   [`<media-features>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
    
*   [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    
*   [Logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#logical_operators)
    

### [Glossary terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#glossary_terms)

*   [media](https://developer.mozilla.org/en-US/docs/Glossary/Media/CSS)
    
*   [media query](https://developer.mozilla.org/en-US/docs/Glossary/Media_query)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#guides)

---------------------------------------------------------------------------------------

[Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)

Introduces media queries, their syntax, and the operators and media features used to construct media query expressions.

[Learn: Media query fundamentals](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Media_queries)

Introduction to media queries and approaches for using them to create responsive designs.

[Testing media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing)

Describes how to use media queries in your JavaScript code to determine the state of a device, and to set up listeners that notify your code when the results of media queries change (such as when the user rotates the screen or resizes the browser).

[Using media queries for accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility)

Learn how media queries can help users understand your website better.

[Printing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing)

Tips and techniques for helping improve web content printer output.

[Responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)

Learn how to use media queries with `sizes` to implement responsive image solutions on websites.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#related_concepts)

-----------------------------------------------------------------------------------------------------------

*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
     module
    *   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
         at-rule
    *   [Using container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
        
    *   [Using size and style container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
        
*   [CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
     module
    *   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
         at-rule
    *   [Using feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
        
*   [CSS environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Environment_variables)
    *   [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
         function
*   [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
     module
    *   [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
         at-rule
*   [CSS object model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model)
     module
    *   [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
         interface
        *   [`matches`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/matches "matches")
             property
        *   [`media`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/media "media")
             property
        *   [`change`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/change_event "change")
             event
    *   [`MediaList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaList)
         interface
        *   [`mediaText`](https://developer.mozilla.org/en-US/docs/Web/API/MediaList/mediaText "mediaText")
             property
    *   [`MediaQueryListEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryListEvent)
         object
*   [Device Posture API](https://developer.mozilla.org/en-US/docs/Web/API/Device_Posture_API)
    *   [`device-posture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/device-posture)
         descriptor
*   HTML
    *   `sizes` attribute for [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#sizes)
        , [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#sizes)
        , and [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#sizes)
         for [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture)
        
    *   `media` attribute for [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#media)
        , [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source#media)
        , and [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#media)
         [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
        
    *   [`<meta name="viewport">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
        
*   SVG [`media`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/media)
     attribute

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#specifications)

-------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 3](https://drafts.csswg.org/mediaqueries-3/) |
| [Media Queries Level 4](https://drafts.csswg.org/mediaqueries/) |
| [Media Queries Level 5](https://drafts.csswg.org/mediaqueries-5/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries#see_also)

-------------------------------------------------------------------------------------------

*   [Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Using the `srcset` and `sizes` attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#using_the_srcset_and_sizes_attributes)
    
*   [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
    
*   Use [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
     to apply styles that depend on browser support for various CSS technologies.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/media_queries/index.md?plain=1 "Folder: en-us/web/css/guides/media_queries (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
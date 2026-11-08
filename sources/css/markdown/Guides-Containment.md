*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#mdn-search)
    

CSS containment
===============

The **CSS containment** module defines containment and container queries.

Containment enables the isolation of page subtrees from the rest of the DOM. The browser can then improve performance by optimizing the rendering of these independent parts.

Container queries are similar to dimension [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
, except that the queries are based on the dimensions of a specific container element defined as a [containment context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#naming_containment_contexts)
, rather than on the dimensions of the viewport. Container queries enable querying a container's size, properties, property values, or even just its assigned [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 to conditionally apply CSS styles. When applying these conditional styles, you can use container query length units, which specify lengths relative to the dimensions of the query container. Additional properties are defined to enable establishing a specific element as a query container and giving it a specific name.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#reference)

-------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#properties)

*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
    

### [Events](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#events)

*   [`contentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event "contentvisibilityautostatechange")
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#interfaces)

*   [`ContentVisibilityAutoStateChangeEvent`](https://developer.mozilla.org/en-US/docs/Web/API/ContentVisibilityAutoStateChangeEvent)
    *   [`skipped`](https://developer.mozilla.org/en-US/docs/Web/API/ContentVisibilityAutoStateChangeEvent/skipped "skipped")
         property
*   [`CSSContainerRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSContainerRule)
    *   [`CSSContainerRule.containerName`](https://developer.mozilla.org/en-US/docs/Web/API/CSSContainerRule/containerName)
        
    *   [`CSSContainerRule.containerQuery`](https://developer.mozilla.org/en-US/docs/Web/API/CSSContainerRule/containerQuery)
        

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#guides)

-------------------------------------------------------------------------------------

[CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)

A guide to using container queries with `@container`, including naming containment contexts.

[Using CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using)

Describes the basic aims of CSS containment and how to leverage `contain` and `content-visibility` for a better user experience.

[Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)

A guide to writing container size and style queries with `@container`, including style queries for custom properties, query syntax and names, and nesting container queries.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#related_concepts)

---------------------------------------------------------------------------------------------------------

*   [Layout and the containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    
*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    
*   [CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
     module
    
    *   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
         at-rule
    *   [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
         property
    *   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
         property
    *   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
         property
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
    
    *   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
         at-rule
    *   [CSS logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#logical_operators)
         (`not`, `or`, and `and`)
*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
    
    *   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
         at-rule
    *   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
         property
*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module
    
    *   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
         property
    *   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
         shorthand property
    *   [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
         property
    *   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
         property
    *   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
         property
    *   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
         property
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
    
    *   [Using CSS counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)
         guide
*   [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module
    
    *   [CSS nesting at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules)
         guide

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#specifications)

-----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Containment Module Level 2](https://drafts.csswg.org/css-contain-2/) |
| [CSS Containment Module Level 3](https://drafts.csswg.org/css-contain-3/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment#see_also)

-----------------------------------------------------------------------------------------

*   [Using feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
    
*   [Using CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
     at-rule

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/containment/index.md?plain=1 "Folder: en-us/web/css/guides/containment (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcontainment%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcontainment%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2ce88199869b63f8da3bbeafd899400f7579cce9%0A*+Document+last+modified%3A+2026-06-08T16%3A09%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
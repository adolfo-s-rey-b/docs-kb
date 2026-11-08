*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#mdn-search)
    

CSS lists and counters
======================

The **CSS lists and counters** module enables styling and positioning of list item bullets and manipulating their values with a combination of strings, counters, and other features.

A list item's marker, whether a bullet symbol or ordinal counter, is its defining feature. List items are not limited to [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements nested within [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 or [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 elements. Rather, list items are any element with `display: list-item` set.

This module defines CSS features to set and reset a list's counters, set which [counter-styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
 or symbols to use as its markers, and position those markers. It also provides developers with the ability to create customized markers.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#reference)

-------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#properties)

*   [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
    
*   [`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
    
*   [`counter-set`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
    
*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    
*   [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
    
*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     shorthand

There is also a `marker-side` property, which is yet to be fully defined or implemented.

### [Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#pseudo-elements)

*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#functions)

*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    
*   [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
    

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#data_types)

*   [`<counter>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content#counter)
    
*   [`<counter-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter#counter-name)
    
*   [`<counter-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter#counter-style)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#guides)

-------------------------------------------------------------------------------

[Consistent list indentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting)

Explains how to achieve consistent list indentation across different browsers.

[Using CSS Counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles/Using_counters)

Explains how to use the CSS counter properties to control list counters.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#related_concepts)

---------------------------------------------------------------------------------------------------

*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
    
    *   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
         at-rule
    *   [`<counter-style-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style#counter-style-name)
         data type
    *   [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols#values)
         data type
    *   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
         function
*   [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
     `start`, `reversed`, and `type` attributes
    
*   [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
     `type` attribute
    
*   [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
     `type` and `value` attributes
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#specifications)

-----------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3](https://drafts.csswg.org/css-lists/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists#see_also)

-----------------------------------------------------------------------------------

*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/lists/index.md?plain=1 "Folder: en-us/web/css/guides/lists (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLists&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flists%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLists%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flists%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
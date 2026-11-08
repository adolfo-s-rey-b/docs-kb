*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#mdn-search)
    

CSS custom highlight API
========================

The **CSS custom highlight API** module provides a programmatic way to target specific ranges of text defined by range objects, without affecting the underlying DOM structure. The range objects can then be selected via `::highlight()` pseudo-elements, and have highlight styles added and removed. The features of this module can create highlight effects similar to how text editors highlight spelling or grammar errors, and code editors highlight syntax errors.

The CSS Custom Highlight API extends the concept of other highlight pseudo-elements such as [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
, [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
, [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
, and [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
 by providing a way to create arbitrary text ranges (defined as [`Range`](https://developer.mozilla.org/en-US/docs/Web/API/Range)
 objects in JavaScript) and style them via CSS, rather than being limited to browser-defined ranges.

[Custom highlight API in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#custom_highlight_api_in_action)

----------------------------------------------------------------------------------------------------------------------------------------------

To enable styling text ranges on a webpage using the CSS Custom Highlight API, you create a [`Range`](https://developer.mozilla.org/en-US/docs/Web/API/Range)
 object, then a [`Highlight`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight)
 object for the range. After registering the highlight using the [`HighlightRegistry.set()`](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry/set)
 method, you can then select the range using the [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
 pseudo-element. The name defined in the `set()` method is used as the parameter of the `::highlight()` pseudo-element selector to select that range. The range selected by the `::highlight()` pseudo-element can be styled using a [limited number of properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#allowable_properties)
.

This example uses the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 property to strike through the `steps` highlight range defined by our JavaScript:

We create a `Range` with a start and end node (which is the same node in this case). We then set this range as the `Highlight` using the `set()` method of the CSS `HighlightRegistry` interface.

An event listener updates the end of the highlighted range when the number of completed steps changes:

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#reference)

----------------------------------------------------------------------------------------------------

### [Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#pseudo-elements)

*   [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#interfaces)

*   [`Highlight`](https://developer.mozilla.org/en-US/docs/Web/API/Highlight)
    
*   [`HighlightRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry)
    

### [Interface extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#interface_extensions)

This module adds properties and methods to interfaces defined in other specifications.

*   [`CSS`](https://developer.mozilla.org/en-US/docs/Web/API/CSS)
    *   [`CSS.highlights`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/highlights_static)
        

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#guides)

----------------------------------------------------------------------------------------------

[CSS custom highlight API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API#concepts_and_usage)

The concepts and usage of the CSS custom highlight API, including creating `Range` and `Highlight` objects, registering the highlights using the `HighlightRegistry`, and styling the highlights using the `::highlight()` pseudo-element.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#related_concepts)

------------------------------------------------------------------------------------------------------------------

*   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    
*   [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
    
*   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    
*   [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
    
*   [`AbstractRange`](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange)
     interface
*   [`Range`](https://developer.mozilla.org/en-US/docs/Web/API/Range)
     interface and [`Range()`](https://developer.mozilla.org/en-US/docs/Web/API/Range/Range "Range()")
     constructor
*   [Text fragments](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
    
*   [`FragmentDirective`](https://developer.mozilla.org/en-US/docs/Web/API/FragmentDirective)
     interface

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Custom Highlight API Module Level 1](https://drafts.csswg.org/css-highlight-api-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API#see_also)

--------------------------------------------------------------------------------------------------

*   [CSS pseudo-element module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
    
*   [CSS Object Model (CSSOM)](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model)
     APIs

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/custom_highlight_api/index.md?plain=1 "Folder: en-us/web/css/guides/custom_highlight_api (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_highlight_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcustom_highlight_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_highlight_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcustom_highlight_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc26d4cc8e9b10c504587531c49fa82b7b646be18%0A*+Document+last+modified%3A+2026-09-04T19%3A00%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#mdn-search)
    

`::highlight()` CSS pseudo-element
==================================

Baseline 2026

Newly available

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::highlight()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 applies styles to a custom highlight.

A custom highlight is a collection of [`AbstractRange`](https://developer.mozilla.org/en-US/docs/Web/API/AbstractRange)
 objects and is registered on a webpage using the [`HighlightRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/HighlightRegistry)
.

The `::highlight()` pseudo-element follows a special inheritance model common to all highlight pseudo-elements. For more details on how this inheritance works, see the [Highlight pseudo-elements inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements_inheritance)
 section.

[Allowable properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#allowable_properties)

------------------------------------------------------------------------------------------------------------------------------

Only certain CSS properties can be used with `::highlight()`:

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     and its associated properties
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`-webkit-text-stroke-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
    , [`-webkit-text-fill-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-fill-color)
     and [`-webkit-text-stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width)
    

In particular, [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 is ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#syntax)

--------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#examples)

------------------------------------------------------------------------------------------------------

### [Highlighting characters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#highlighting_characters)

#### HTML

#### CSS

#### JavaScript

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Custom Highlight API Module Level 1  <br>\# custom-highlight-pseudo](https://drafts.csswg.org/css-highlight-api/#custom-highlight-pseudo) |
| [CSS Pseudo-Elements Module Level 4  <br>\# selectordef-highlight-highlight-name-selector](https://drafts.csswg.org/css-pseudo/#selectordef-highlight-highlight-name-selector) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS custom highlight API](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_highlight_API)
     module
*   [CSS custom highlight](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)
     API
*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_highlight/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_highlight (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ahighlight&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_highlight%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Ahighlight%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_highlight%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
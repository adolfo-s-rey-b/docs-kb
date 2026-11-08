*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#mdn-search)
    

CSS pseudo-elements
===================

The **CSS pseudo-element** module defines abstract elements that are not directly present in the document tree. These abstract elements, called pseudo-elements, represent portions of the render tree that can be selected and styled. Pseudo-elements are used to create abstractions about the document tree beyond those provided by the document tree.

**Note:** This page introduces a CSS module. To find an exhaustive list of all pseudo-elements defined by CSS specifications, see the [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 reference page.

Pseudo-elements are prefixed with a double colon (`::`). You add pseudo-elements to selectors (as in `p::first-line`) to target and style these faux elements.

Pseudo-elements enable targeting entities not included in HTML and sections of content that cannot be targeted otherwise without adding extra markup. Consider the placeholder of an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element. This is an abstract element and not a distinct node in the document tree. You can select this placeholder by using the [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
 pseudo-element. As another example, the [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
 pseudo-element matches the content currently highlighted by a user, allowing you to style what is matched as the user interacts with the content and changes the selection. Similarly, the [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
 pseudo-element targets the first line of an element, updating automatically if the character count of the first line changes, without having to query the element's line length.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#reference)

-----------------------------------------------------------------------------------------------

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#selectors)

*   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
    
*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    
*   [`::file-selector-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
    
*   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
    
*   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    
*   [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
    
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
    
*   [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
    
*   [`::search-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text)
    
*   [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
    
*   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    
*   [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
    

The specification also defines the `::details-content` pseudo-element and the `::postfix` and `::prefix` sub-pseudo elements. These are not yet supported by any browser. The [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
 pseudo-element is included within this module, but most details are provided in the [CSS custom highlight API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)
.

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#interfaces)

*   [`CSSPseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPseudoElement)
     interface
    *   [`CSSPseudoElement.element`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPseudoElement/element)
         property
    *   [`CSSPseudoElement.parent`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPseudoElement/parent)
         property
    *   [`CSSPseudoElement.type`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPseudoElement/type)
         property
    *   [`pseudo()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPseudoElement/pseudo "pseudo()")
         method

### [Terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#terms)

*   [Pseudo-element](https://developer.mozilla.org/en-US/docs/Glossary/Pseudo-element)
     glossary term

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#guides)

-----------------------------------------------------------------------------------------

[CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)

Alphabetical list of pseudo-elements defined by all the CSS specifications and WebVTT.

[Learn: Pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)

Part of CSS building blocks section on selectors. This article defines what a pseudo-element is and how it can be combined with pseudo-classes and be used for generating content with `::before` and `::after` pseudo-elements.

[How to create fancy boxes using pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Solve_CSS_problems/Create_fancy_boxes#pseudo-elements)

Example of styling generated content using `::before` and `::after` pseudo-elements for visual effects.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#related_concepts)

-------------------------------------------------------------------------------------------------------------

*   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    
*   Web Video Text Tracks Format (WebVTT) cues:
    
    *   [`::cue`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
        
    *   [`::cue()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
        
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module
    
    *   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
        
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
    
    *   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
        
    *   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
        
    *   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
        
    *   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
        
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
    
    *   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
        
    *   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
        
    *   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
        
    *   [`::slotted()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
        
*   [CSS shadow parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
     module
    
    *   [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
        
*   [CSS view transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/View_transitions)
     module
    
    *   [`::view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
        
    *   [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
        
    *   [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
        
    *   [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
        
    *   [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
        
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
    *   [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
        
    *   [Combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selectors_and_combinators#combinators)
        
    *   [Class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
        
    *   [ID selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)
        
    *   [Type selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
        
    *   [Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
        
    *   [Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
        
*   [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
     attribute of the `<input>` element
    
*   [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
     selector
    
*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
    
    *   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
         property
    *   [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
         property
*   [Text fragments](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment/Text_fragments)
    
*   [`AnimationEvent.pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent/pseudoElement)
     property
    
*   [`KeyframeEffect.pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/KeyframeEffect/pseudoElement)
     property
    
*   [`TransitionEvent.pseudoElement`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent/pseudoElement)
     property
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4](https://drafts.csswg.org/css-pseudo/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements#see_also)

---------------------------------------------------------------------------------------------

*   [List of pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [CSS shadow-parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
     module
*   [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
     module
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module
*   [CSS custom highlight API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/pseudo-elements/index.md?plain=1 "Folder: en-us/web/css/guides/pseudo-elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPseudo-elements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpseudo-elements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPseudo-elements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpseudo-elements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55fa0e2b797b1358464b42ceb32167675a03ca8d%0A*+Document+last+modified%3A+2026-06-08T16%3A51%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#mdn-search)
    

CSS selectors
=============

The **CSS selectors** module defines the patterns to select elements to which a set of CSS rules are then applied along with their [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
. The CSS selectors module provides us with more than 60 selectors and five combinators. [Other modules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#related_concepts)
 provide additional pseudo-class selectors and pseudo-elements.

**Note:** This page introduces a CSS module. To find an exhaustive list of all selectors defined by CSS specifications, see the [selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors)
 reference page.

In CSS, selectors are patterns used to match, or select, the elements you want to style. Selectors are also used in JavaScript to enable selecting the DOM nodes to return as a [`NodeList`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList)
.

Selectors, whether used in CSS or JavaScript, enable targeting HTML elements based on their type, attributes, current states, and even position in the DOM. Combinators allow you to be more precise when selecting elements by enabling selecting elements based on their relationship to other elements.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#reference)

-----------------------------------------------------------------------------------------

### [Combinators and separators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#combinators_and_separators)

*   `+` ([Next-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator)
    )
*   `>` ([Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)
    )
*   `~` ([Subsequent sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)
    )
*   " " ([Descendant combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator)
    )
*   `|` ([Namespace separator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator)
    )
*   `,` ([Selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
    )

The CSS selectors module also introduces the [column combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Column_combinator)
 (`||`). Currently, no browsers support this feature.

### [Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#selectors)

*   [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
    
*   [`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
    
*   [`:autofill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill)
    
*   [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    
*   [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
    
*   [`:default`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default)
    
*   [`:defined`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined)
    
*   [`:dir()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)
    
*   [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
    
*   [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
    
*   [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
    
*   [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    
*   [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    
*   [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
    
*   [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
    
*   [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
    
*   [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    
*   [`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)
    
*   [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
    
*   [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    
*   [`:in-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range)
    
*   [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
    
*   [`:interest-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
    
*   [`:interest-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target)
    
*   [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    
*   [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
    
*   [`:lang()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
    
*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    
*   [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    
*   [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
    
*   `:matches()` (obsolete legacy selector alias for [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
    )
*   [`:modal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
    
*   [`:muted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)
    
*   [`:not()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)
    
*   [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    
*   [`:nth-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    
*   [`:nth-last-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
    
*   [`:nth-last-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    
*   [`:only-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child)
    
*   [`:only-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)
    
*   [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
    
*   [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    
*   [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
    
*   [`:past`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past)
    
*   [`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
    
*   [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
    
*   [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
    
*   [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
    
*   [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    
*   [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    
*   [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
    
*   [`:scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
    
*   [`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`:stalled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
    
*   [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
    
*   [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    
*   [`:user-valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)
    
*   [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
    
*   [`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
    
*   [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
    
*   [`:-webkit-` pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions#pseudo-classes)
    
*   [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
    
*   [Class selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
    
*   [ID selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)
    
*   [Type selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
    
*   [Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
    

The CSS selectors module also introduces the [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
, [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
, and [`:local-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:local-link)
 pseudo-classes. Currently, no browsers support these features.

[Terms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#terms)

---------------------------------------------------------------------------------

*   [Pseudo-class](https://developer.mozilla.org/en-US/docs/Glossary/Pseudo-class)
     glossary term
*   [Functional pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#functional_pseudo-classes)
    
*   [Combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selectors_and_combinators#combinators)
    
*   [Simple selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#simple_selector)
    
*   [Compound selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#compound_selector)
    
*   [Complex selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#complex_selector)
    
*   [Relative selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#relative_selector)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#guides)

-----------------------------------------------------------------------------------

[CSS selectors and combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selectors_and_combinators)

Overview of the different types of simple selectors and various combinators defined in the CSS selectors and the CSS pseudo modules.

[CSS selector structure](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure)

Explanation of the structure of CSS selectors and the terminologies introduced in the CSS selectors module, ranging from "simple selector" to "forgiving relative selector list".

[Pseudo classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)

Lists the pseudo-classes, selectors that allow the selection of elements based on state information that is not contained in the document tree, defined in the various CSS modules and HTML.

[Using the `:target` pseudo-class in selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target)

Learn how to use the [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
 pseudo-class to style the target element a URL's fragment identifier.

[Privacy and the `:visited` selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited)

Explores the style limitations set on the `:visited` class for user privacy.

[CSS building blocks: CSS selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)

Introduction to basic CSS selectors, including tutorials on [Type, class, and ID selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
, [Attribute selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Attribute_selectors)
, [Pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)
, and [Combinators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Combinators)
.

[Learn: UI pseudo-classes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/UI_pseudo-classes)

Learn the different UI pseudo-classes available for styling forms in different states.

[Selection and traversal on the DOM tree](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Selection_and_traversal_on_the_DOM_tree)

The selectors API enables using selectors in JavaScript to retrieve element nodes from the DOM.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#related_concepts)

-------------------------------------------------------------------------------------------------------

*   [`state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
     pseudo-class
    
*   [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
     pseudo-class
    
*   [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module
    
    *   [`&` nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
        
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
    
    *   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
         pseudo-class
    *   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
         pseudo-class
    *   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
         pseudo-class
    *   [`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
         pseudo-class
    *   [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
         pseudo-element
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
    
    *   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
        
    *   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
        
    *   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
        
    *   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
        
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module
    
    *   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
        
*   [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
     module
    
    *   [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
         pseudo-class
    *   [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
         pseudo-class
    *   [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
         pseudo-class
    *   `:blank` pseudo-class
*   [CSS pseudo-element module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     (representing entities not included in HTML)
    
    *   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
        
    *   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
        
    *   [`::file-selector-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
        
    *   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
        
    *   [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
        
    *   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
        
    *   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
        
    *   [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
        
    *   [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
        
    *   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
        
    *   [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
        
*   [CSS shadow parts module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
    
    *   [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
         pseudo-element
*   [CSS positioned layout module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
    
    *   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
        
*   Other [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
    
    *   [`::cue`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
        
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
    
    *   [`<keyframe-selector>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
        
*   [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
     at-rule
    
*   [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [`Document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
     method
    
*   [`Document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)
     method
    
*   [`NodeList.forEach()`](https://developer.mozilla.org/en-US/docs/Web/API/NodeList/forEach)
     method
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#specifications)

---------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4](https://drafts.csswg.org/selectors/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors#see_also)

---------------------------------------------------------------------------------------

*   [CSS pseudo-element module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
    
*   [CSS cascading and inheritance module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
    
*   [CSS nesting module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
    
*   [Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/selectors/index.md?plain=1 "Folder: en-us/web/css/guides/selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fselectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fselectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa75edf682e5e346b4f97582db6cbccaae800ef73%0A*+Document+last+modified%3A+2026-04-14T21%3A25%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
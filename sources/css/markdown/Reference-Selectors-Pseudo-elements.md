*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#mdn-search)
    

Pseudo-elements
===============

A CSS **pseudo-element** is a keyword added to a selector that lets you style a specific part of the selected element(s).

**Note:** This page is an index of all pseudo-elements in CSS. The [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
 page introduces the module that defines some, but not all, of these pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#syntax)

------------------------------------------------------------------------------------------------------

For example, [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
 can be used to change the font of the first line of a paragraph.

Double colons (`::`) are used for pseudo-elements. This distinguishes pseudo-elements from [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 that use a single colon (`:`) in their notation. Note, browsers support single colon syntax for the original four pseudo-elements: `::before`, `::after`, `::first-line`, and `::first-letter`.

Pseudo-elements do not exist independently. The element of which a pseudo-element is a part is called its _originating element_. A pseudo-element must appear after all the other components in the [complex](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#complex_selector)
 or [compound](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#compound_selector)
 selector. The last element in the selector is the originating element of the pseudo-element. For example, you can select a paragraph's first line using `p::first-line` but not the first-line's children. So `p::first-line > *` is invalid.

A pseudo-element can be selected based on the current state of the originating element. For example, `p:hover::first-line` selects the first line (pseudo-element) of a paragraph when the paragraph itself is being hovered (pseudo-class).

The specifications allow some pseudo-elements to be selected based on the current state of the originating element. In these cases, the pseudo-element is selected only when it is in the same state. For example, `::picker(select):hover` selects the currently hovered descendant of a customizable [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element, excluding the first [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 child, which is not selected by the [`::picker()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
 pseudo-element. Note, however, that when a [selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#selector_list)
 contains an invalid selector, the entire style block is ignored, so make sure the state you're including is supported on the pseudo-element to which it is attached.

[Typographic pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#typographic_pseudo-elements)

------------------------------------------------------------------------------------------------------------------------------------------------

[`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)

The first line-box of the originating element.

[`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)

The first letter, number, or symbol character on the first line of its originating element.

[`::cue`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)

The [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
 cues within a selected element. This can be used to [style captions and other cues](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API#styling_webvtt_in_html_or_a_stylesheet)
 in media with VTT tracks. The [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
 module also defines the `::postfix` and `::prefix` sub-pseudo elements. These are not yet supported by any browser.

[Highlight pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements)

--------------------------------------------------------------------------------------------------------------------------------------------

Selects document sections based on content and document status, enabling those areas to be styled differently to indicate that status to the user.

[`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)

A portion of text that the browser thinks is grammatically incorrect.

[`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)

The elements in the [highlight registry](https://developer.mozilla.org/en-US/docs/Web/API/CSS/highlights_static)
. It is used to create custom highlights.

[`::search-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text)

Search results identified by the user agent's "Find" or "Find in page" text search feature.

[`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)

The portion of a document that has been selected.

[`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)

A portion of text that the browser thinks is misspelled.

[`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)

The document's target element. The target element is identified using the [URL's fragment](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment)
 identifier.

[Tree-Abiding pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#tree-abiding_pseudo-elements)

--------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-elements behave like regular elements, fitting seamlessly within the box model. They act as a child element that can be styled directly within the originating element hierarchy.

[`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)

Creates a pseudo-element that is the first child of the selected element.

[`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)

Creates a pseudo-element that is the last child of the selected element.

[`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)

Each column fragment of a [multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
.

[`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)

The automatically generated marker box of a list item.

[`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)

The backdrop of the originating element rendered in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
.

[`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)

Creates a button that can control the scrolling of the [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 to which it is applied.

[`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)

Creates a pseudo-element that is a scroll marker — a scroll target button for its originating element nested in a scroll-marker group.

[`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)

Generates a container before or after a scroll container to contain the [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-elements generated on the element or its descendants.

[Element-backed pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#element-backed_pseudo-elements)

------------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-elements are real elements that are not otherwise selectable.

[`::details-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content)

The expandable/collapsible contents of a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element.

[`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)

Any element within a [shadow tree](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 that has a matching [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute.

[`::slotted()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)

Any element placed into a slot inside an HTML template.

[Form-related pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#form-related_pseudo-elements)

--------------------------------------------------------------------------------------------------------------------------------------------------

The pseudo-elements are related to form controls.

[`::checkmark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::checkmark)

Targets the checkmark placed inside the currently-selected `<option>` element of a [customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 to provide a visual indication of which one is selected.

[`::file-selector-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)

The button of an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of [`type="file"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
.

[`::picker()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)

The picker part of an element, for example the drop-down picker of a [customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
.

[`::picker-icon`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker-icon)

The picker icon inside form controls that have an icon associated with them. In the case of a [customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
, it selects the arrow that points down when the select is closed.

[`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)

The placeholder text in an input field.

[Alphabetical index](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#alphabetical_index)

------------------------------------------------------------------------------------------------------------------------------

Pseudo-elements defined by a set of CSS specifications include the following:

A

*   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
    

B

*   [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    
*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    

C

*   [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    
*   [`::checkmark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::checkmark)
    
*   [`::cue`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
     (and [`::cue()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
    )

D

*   [`::details-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content)
    

F

*   [`::file-selector-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
    
*   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
    

G

*   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    

H

*   [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
    

M

*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
    

P

*   [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
    
*   [`::picker()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
    
*   [`::picker-icon`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker-icon)
    
*   [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
    

S

*   [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`::scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
    
*   [`::slotted()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
    
*   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    

T

*   [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
    

V

*   [`::view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
    
*   [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
    
*   [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
    
*   [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
    
*   [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
    

### [Non-standard pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#non-standard_pseudo-elements)

Non-standard vendor-prefixed pseudo-elements include:

#### `-moz-` prefix

*   [`::-moz-color-swatch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch)
    
*   [`::-moz-focus-inner`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner)
    
*   [`::-moz-list-bullet`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-bullet)
    
*   [`::-moz-list-number`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-number)
    
*   [`::-moz-meter-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-meter-bar)
    
*   [`::-moz-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-progress-bar)
    
*   [`::-moz-range-progress`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-progress)
    
*   [`::-moz-range-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-thumb)
    
*   [`::-moz-range-track`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-track)
    

#### `-webkit-` prefix

*   [`::-webkit-inner-spin-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-inner-spin-button)
    
*   [`::-webkit-meter-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-bar)
    
*   [`::-webkit-meter-even-less-good-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-even-less-good-value)
    
*   [`::-webkit-meter-inner-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-inner-element)
    
*   [`::-webkit-meter-optimum-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-optimum-value)
    
*   [`::-webkit-meter-suboptimum-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-suboptimum-value)
    
*   [`::-webkit-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-bar)
    
*   [`::-webkit-progress-inner-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element)
    
*   [`::-webkit-progress-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-value)
    
*   [`::-webkit-scrollbar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar)
    
*   [`::-webkit-search-cancel-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-search-cancel-button)
    
*   [`::-webkit-search-results-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-search-results-button)
    
*   [`::-webkit-slider-runnable-track`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-runnable-track)
    
*   [`::-webkit-slider-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-thumb)
    

[Nesting pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#nesting_pseudo-elements)

----------------------------------------------------------------------------------------------------------------------------------------

You can chain some pseudo-element selectors together to style pseudo-elements nested inside other pseudo-elements. The following nested pseudo-element combinations are supported:

*   [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
    *   `::after::marker`: Selects the [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
         pseudo-element of an `::after` pseudo-element, when `::after` is styled as a list item, with [`display: list-item`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
        .
*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    *   `::before::marker`: Selects the [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
         pseudo-element of a `::before` pseudo-element, when `::before` is styled as a list item, with [`display: list-item`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
        .

Check out the individual pseudo-element reference pages for examples and browser compatibility information.

[Highlight pseudo-elements inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements_inheritance)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Highlight pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements)
, such as [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
, [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
, [`::highlight()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
, [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
, and [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
, follow a consistent inheritance model that differs from [regular element inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
.

When you apply styles to highlight pseudo-elements, they inherit from both:

1.  Their parent elements (following normal inheritance).
2.  The highlight pseudo-elements of their parent elements (following highlight inheritance).

This means that if you style both a parent element's highlight pseudo-element and a child element's highlight pseudo-element, the child's highlighted text will combine properties from both sources.

Here is a concrete example.

First, we have some HTML that includes two nested [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements. Some of the included text content is contained directly inside the parent `<div>`, and some is nested inside the child `<div>`.

Next we include some CSS, which selects the parent and child `<div>` elements separately and gives them different [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 values, and selects the parent and child's selected text ([`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
). This gives each `<div>` a different [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and sets a different text `color` on the parent selection.

The example renders as follows:

Try selecting the text in both the parent and child elements. Notice that:

1.  When you select the parent text, it uses the yellow background and red text color defined in `.parent::selection`.
2.  When you select the child text, it uses:
    *   The orange background from `.child::selection`.
    *   The red text color inherited from the parent's `::selection` pseudo-element.

This demonstrates how the child's highlight pseudo-element inherits from both its parent element and the parent's highlight pseudo-element.

[CSS custom properties (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 in highlight pseudo-elements inherit from their originating element (the element they're being applied to), not through the highlight inheritance chain. For example:

When using the universal selector with highlight pseudo-elements, it prevents highlight inheritance. For example:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4](https://drafts.csswg.org/css-pseudo/) |
| [CSS Positioned Layout Module Level 4](https://drafts.csswg.org/css-position-4/) |
| [Unknown specification](https://drafts.csswg.org/css-shadow-parts/) |
| [WebVTT: The Web Video Text Tracks Format](https://w3c.github.io/webvtt/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module
*   [Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module
*   [Learn: Pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)
    
*   [Inheritance changes for CSS selection styling](https://developer.chrome.com/blog/selection-styling "External link (opens in new tab)")
     - Detailed explanation of the highlight pseudo-elements inheritance model changes in Chrome 134

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/pseudo-elements/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/pseudo-elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FPseudo-elements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fpseudo-elements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FPseudo-elements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fpseudo-elements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbc294cca926abf68e1cbf8026f0bae1bf6a95325%0A*+Document+last+modified%3A+2026-06-08T17%3A12%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
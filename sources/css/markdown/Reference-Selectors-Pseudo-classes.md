*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#mdn-search)
    

Pseudo-classes
==============

A [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **_pseudo-class_** is a keyword added to a selector that lets you select elements based on information that lies outside of the document tree, such as a specific state of the selected element(s). For example, the pseudo-class [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 can be used to style a button when a user's pointer hovers over it.

A pseudo-class consists of a colon (`:`) followed by the pseudo-class name (e.g., `:hover`). A functional pseudo-class also contains a pair of parentheses to define the arguments (e.g., `:dir()`). The element that a pseudo-class is attached to is defined as an _anchor element_ (e.g., `button` in case `button:hover`).

Pseudo-classes let you apply a style to an element not only in relation to the content of the document tree, but also in relation to external factors like the history of the navigator ([`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
, for example), the status of its content (like [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
 on certain form elements), or the position of the mouse (like [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
, which lets you know if the mouse is over an element or not).

**Note:** In contrast to pseudo-classes, [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 can be used to style a _specific part_ of an element.

[Elemental pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#elemental_pseudo-classes)

-----------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to the core identity of elements.

[`:defined`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined)

Matches any element that is defined.

[`:heading`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading)

Matches any heading element (`<h1>`\-`<h6>`).

[Element display state pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#element_display_state_pseudo-classes)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes enable the selection of elements based on their display states.

[`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)

Matches an element that can either be open or closed that is currently open.

[`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)

Matches a popover element that is currently in the showing state.

Matches an element that is in a state in which it excludes all interaction with elements outside it until the interaction has been dismissed.

[`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)

Matches an element that is currently in fullscreen mode.

[`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)

Matches an element that is currently in picture-in-picture mode.

[`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)

Matches the DOM overlay element during an immersive AR or VR session.

[Input pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#input_pseudo-classes)

---------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to form elements, and enable selecting elements based on HTML attributes and the state that the field is in before and after interaction.

[`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)

Represents a user interface element that is in an enabled state.

[`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)

Represents a user interface element that is in a disabled state.

[`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)

Represents any element that cannot be changed by the user.

[`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)

Represents any element that is user-editable.

[`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)

Matches an input element that is displaying placeholder text. For example, it will match the `placeholder` attribute in the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements.

[`:autofill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill)

Matches when an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 has been autofilled by the browser.

[`:default`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default)

Matches one or more UI elements that are the default among a set of elements.

[`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)

Matches when elements such as checkboxes and radio buttons are toggled on.

[`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)

Matches UI elements when they are in an indeterminate state.

[`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)

Matches a user-input element which is empty, containing an empty string or other null input.

[`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)

Matches an element with valid contents. For example, an input element with the type 'email' that contains a validly formed email address or an empty value if the control is not required.

[`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)

Matches an element with invalid contents. For example, an input element with type 'email' with a name entered.

[`:in-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range)

Applies to elements with range limitations. For example, a slider control when the selected value is in the allowed range.

[`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)

Applies to elements with range limitations. For example, a slider control when the selected value is outside the allowed range.

[`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)

Matches when a form element is required.

[`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)

Matches when a form element is optional.

[`:user-valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)

Represents an element with correct input, but only when the user has interacted with it.

[`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)

Represents an element with incorrect input, but only when the user has interacted with it.

[Linguistic pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#linguistic_pseudo-classes)

-------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes reflect the document language and enable the selection of elements based on language or script direction.

[`:dir()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)

The directionality pseudo-class selects an element based on its directionality as determined by the document language.

[`:lang()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)

Select an element based on its content language.

[Location pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#location_pseudo-classes)

---------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to links, and to targeted elements within the current document.

[`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)

Matches an element if the element would match either [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
 or [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
.

[`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)

Matches links that have not yet been visited.

[`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)

Matches links that have been visited.

[`:local-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:local-link)

Matches links whose absolute URL is the same as the target URL. For example, anchor links to the same page.

[`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)

Matches the element which is the target of the document URL.

[`:scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)

Represents elements that are a reference point for selectors to match against.

**Note:** A `:target-within` pseudo-class, to match elements that are or have a descendant which is the target of the document URL, was defined but removed from the specification. Use `:has(:target)` for this purpose.

[Resource state pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#resource_state_pseudo-classes)

---------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes apply to media that is capable of being in a state where it would be described as playing, such as a video.

[`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)

Represents a playable element that is playing.

[`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)

Represents a playable element that is paused.

[`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)

Represents a playable element that is currently seeking a playback position in the media resource.

[`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)

Represents a playable element that is playing but is temporarily stalled because it is downloading the media resource.

[`:stalled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)

Represents a playable element that is playing but is stalled because it cannot download the media resource.

[`:muted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)

Represents a sound-producing element that is muted.

[`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)

Represents a sound-producing element that has its volume level locked by the browser.

[Time-dimensional pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#time-dimensional_pseudo-classes)

-------------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes apply when viewing something which has timing, such as a [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
 caption track.

[`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)

Represents the element or ancestor of the element that is being displayed.

[`:past`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past)

Represents an element that occurs entirely before the [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
 element.

[`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)

Represents an element that occurs entirely after the [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
 element.

[Tree-structural pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#tree-structural_pseudo-classes)

-----------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to the location of an element within the document tree.

[`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)

Represents an element that is the root of the document. In HTML this is usually the `<html>` element.

[`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)

Represents an element with no children other than white-space characters.

[`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)

Uses `An+B` notation to select elements from a list of sibling elements.

[`:nth-last-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)

Uses `An+B` notation to select elements from a list of sibling elements, counting backwards from the end of the list.

[`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)

Matches an element that is the first of its siblings.

[`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)

Matches an element that is the last of its siblings.

[`:only-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child)

Matches an element that has no siblings. For example, a list item with no other list items in that list.

[`:heading()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function)

Uses `An+B` notation to select heading elements (`<h1>`\-`<h6>`).

[`:nth-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)

Uses `An+B` notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements.

[`:nth-last-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)

Uses `An+B` notation to select elements from a list of sibling elements that match a certain type from a list of sibling elements counting backwards from the end of the list.

[`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)

Matches an element that is the first of its siblings, and also matches a certain type selector.

[`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)

Matches an element that is the last of its siblings, and also matches a certain type selector.

[`:only-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)

Matches an element that has no siblings of the chosen type selector.

[Shadow-structural pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#shadow-structural_pseudo-classes)

---------------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to the shadow DOM.

[`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)

Matches the shadow tree's shadow host.

[`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)

Matches an element that matches [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
 and matches any of the selectors in the list provided.

[`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)

Selects elements outside of the shadow tree in the context of the shadow host.

[`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)

Matches slot elements that have been assigned content.

[User action pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#user_action_pseudo-classes)

---------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes require some interaction by the user in order for them to apply, such as holding a mouse pointer over an element.

[`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)

Matches when a user designates an item with a pointing device, such as holding the mouse pointer over the item.

[`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)

Matches when an item is being activated by the user. For example, when the item is clicked on.

[`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)

Matches when an element has focus.

[`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)

Matches when an element has focus and the user agent identifies that the element should be visibly focused.

[`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)

Matches an element to which [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 applies, plus any element that has a descendant to which [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 applies.

[`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)

Matches the [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
 pseudo-element of a [`scroll-marker-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
 that is currently scrolled to, in other words, the **active** scroll marker.

### [Top-layer ancestor matching boundary](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#top-layer_ancestor_matching_boundary)

When setting styles using a `:hover`, `:active`, or `:focus-within` pseudo-class selector, the selector matches a nested set of elements up the DOM tree. If the hierarchy includes an element in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 (for example, a [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 or [customizable `<select>`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 picker), the matching stops at that top-layer element.

For example, the following code features a customizable `<select>` element and a popover. We've set every element in the page to have a thick blue dashed [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 on hover.

Note that when you hover over the `<select>` element or the popover toggle button, all ancestors of those elements get the border. However, once the select picker or the popover is open, hovering over one of its descendants applies the border only up to the top-layer element itself (the select picker or the popover), that is, the matching stops at this element.

This behavior stops the pseudo-class matching from spilling out of a top-layer component into the surrounding page, which can otherwise cause a user interface to look broken.

[Functional pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#functional_pseudo-classes)

-------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes accept a [selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
 or [forgiving selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#forgiving_selector_list)
 as a parameter.

[`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)

The matches-any pseudo-class matches any element that matches any of the selectors in the list provided. The list is forgiving.

[`:not()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)

The negation, or matches-none, pseudo-class represents any element that is not represented by its argument.

[`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)

The specificity-adjustment pseudo-class matches any element that matches any of the selectors in the list provided without adding any specificity weight. The list is forgiving.

[`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)

The relational pseudo-class represents an element if any of the relative selectors match when anchored against the attached element.

[Custom state pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#custom_state_pseudo-classes)

-----------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes apply to custom elements.

[`:state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)

Matches custom elements that have the specified custom state.

[Page pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#page_pseudo-classes)

-------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to pages in a printed document and are used with the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 at-rule.

[`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)

Represents all left-hand pages of a printed document.

[`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)

Represents all right-hand pages of a printed document.

[`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)

Represents the first page of a printed document.

[`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#blank_2)

Represents a blank page in a printed document.

[View transition pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#view_transition_pseudo-classes)

-----------------------------------------------------------------------------------------------------------------------------------------------------

These pseudo-classes relate to elements involved in a [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
.

[`:active-view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)

Matches the root element of a document when a [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API#concepts_and_usage)
 is in progress (_active_) and stops matching once the transition has completed.

[`:active-view-transition-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)

Matches the root element of a document when a specified [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API#concepts_and_usage)
 is in progress (_active_) and stops matching once the transition has completed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#syntax)

-----------------------------------------------------------------------------------------------------

Like regular classes, you can chain together as many pseudo-classes as you want in a selector.

[Alphabetical index](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#alphabetical_index)

-----------------------------------------------------------------------------------------------------------------------------

Pseudo-classes defined by a set of CSS specifications include the following:

A

*   [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
    
*   [`:active-view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)
    
*   [`:active-view-transition-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)
    
*   [`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
    
*   [`:autofill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill)
    

B

*   [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
     (input)
*   `:blank` (page)
*   [`:buffering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    

C

*   [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
    
*   [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
    

D

*   [`:default`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default)
    
*   [`:defined`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined)
    
*   [`:dir()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)
    
*   [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
    

E

*   [`:empty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
    
*   [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
    

F

*   [`:first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    
*   [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    
*   [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    
*   [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
    
*   [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
    
*   [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
    
*   [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    
*   [`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)
    

H

*   [`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
    
*   [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
    
*   [`:heading`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading)
    
*   [`:heading()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function)
    
*   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    
*   [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
    
*   [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
    
*   [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    

I

*   [`:in-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range)
    
*   [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
    
*   [`:interest-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
    
*   [`:interest-target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target)
    
*   [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    
*   [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
    

L

*   [`:lang()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
    
*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    
*   [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    
*   [`:left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    
*   [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
    
*   [`:local-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:local-link)
    

M

*   [`:modal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
    
*   [`:muted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)
    

N

*   [`:not()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)
    
*   [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    
*   [`:nth-last-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
    
*   [`:nth-last-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    
*   [`:nth-of-type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    

O

*   [`:only-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child)
    
*   [`:only-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)
    
*   [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
    
*   [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    
*   [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
    

P

*   [`:past`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past)
    
*   [`:paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`:picture-in-picture`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
    
*   [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
    
*   [`:playing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
    

R

*   [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
    
*   [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    
*   [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    
*   [`:right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    
*   [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
    

S

*   [`:scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
    
*   [`:seeking`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`:stalled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
    
*   [`:state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
    

T

*   [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
    
*   [`:target-after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
    
*   [`:target-current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [`:target-before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    

U

*   [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    
*   [`:user-valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)
    

V

*   [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
    
*   [`:volume-locked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
    

W

*   [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
    

X

*   [`:xr-overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
    

### [Non-standard pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#non-standard_pseudo-classes)

Non-standard vendor-prefixed pseudo-classes include:

#### `-moz-` prefix

*   [`:-moz-broken`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-broken)
    
*   [`:-moz-drag-over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over)
    
*   [`:-moz-first-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-first-node)
    
*   [`:-moz-handler-blocked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-blocked)
    
*   [`:-moz-handler-crashed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-crashed)
    
*   [`:-moz-handler-disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-disabled)
    
*   [`:-moz-last-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node)
    
*   [`:-moz-loading`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading)
    
*   [`:-moz-locale-dir(ltr)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_ltr)
    
*   [`:-moz-locale-dir(rtl)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl)
    
*   [`:-moz-only-whitespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace)
    
*   [`:-moz-submit-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-submit-invalid)
    
*   [`:-moz-suppressed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-suppressed)
    
*   [`:-moz-user-disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-user-disabled)
    
*   [`:-moz-window-inactive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-window-inactive)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# pseudo-classes](https://html.spec.whatwg.org/multipage/semantics-other.html#pseudo-classes) |
| [Selectors Level 4](https://drafts.csswg.org/selectors/) |
| [CSS Scope](https://drafts.csswg.org/css-scoping/) |
| [CSS Paged Media Module Level 3](https://drafts.csswg.org/css-page/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#see_also)

---------------------------------------------------------------------------------------------------------

*   [Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/pseudo-classes/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/pseudo-classes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FPseudo-classes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fpseudo-classes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FPseudo-classes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fpseudo-classes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc62181855c91ac0435dea5fa759a250e1dea4f8b%0A*+Document+last+modified%3A+2026-08-12T07%3A36%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#mdn-search)
    

`overlay` CSS property
======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/211)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#browser_compatibility)
 carefully before using this in production.

The **`overlay`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether an element appearing in the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 (for example, a shown [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 or modal [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 element) is actually rendered in the top layer. This property is only relevant within a list of [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 values, and only if `allow-discrete` is set as the [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
.

It is important to note that `overlay` can _only_ be set by the browser — author styles cannot change the `overlay` value of any element. You can, however, add `overlay` to the [list of transition properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 set on an element. This causes its removal from the top layer to be deferred so it can be animated instead of disappearing immediately.

**Note:** When transitioning `overlay`, you need to set [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
 on the transition so that it will animate. `overlay` animations differ from normal [discrete animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
 in that the visible (i.e., `auto`) state will always be shown for the full duration of the transition, regardless of whether it is the start or end state.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#syntax)

-----------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#auto)

The element is rendered in the top layer if it is promoted to the top layer.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#none)

The element is not rendered in the top layer.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Discrete behavior except when animating to or from `none` is visible for the entire duration |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#formal_syntax)

-------------------------------------------------------------------------------------------------------------

overlay =   
  none  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#examples)

---------------------------------------------------------------------------------------------------

### [Transitioning a popover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#transitioning_a_popover)

In this example, a [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 is animated as it [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 from hidden to shown and back again.

#### HTML

The HTML contains a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element declared as a popover using the [popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute, and a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element designated as the popover's display control using its [popovertarget](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute.

#### CSS

The `overlay` property is only present in the list of transitioned properties. As `overlay` is a user-agent controlled property, it is not declared in the pre-transition or post-transition states.

The two properties we want to animate are [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
: we want the popover to fade in and out while growing and shrinking in the horizontal direction. We set a starting state for these properties on the default hidden state of the popover element (selected via `[popover]`), and an end state on the open state of the popover (selected via the [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
 pseudo-class). We then set a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 property to animate between the two.

Because the animated element is being promoted to the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 when shown and removed from the top layer when hidden, `overlay` is added to the list of transitioned elements. This ensures that the removal of the element from the top layer is deferred until the animation has ended. This doesn't make a huge difference for basic animations such as this one, but in more complex cases not doing this can result in the element being removed from the overlay too quickly, meaning the animation is not smooth or effective. Note that the [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
 value is also set in the shorthand to enable discrete transitions.

The following steps are also required to get the animation working in both directions:

*   A starting state for the animation is set inside the [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
     at-rule. This is needed to avoid unexpected behavior. By default transitions are not triggered on elements' first style updates, or when the `display` type changes from `none` to another type. `@starting-style` allows you to override that default in a specific controlled fashion. Without this, the entry animation would not occur and the popover would just appear.
*   `display` is also added to the list of transitioned elements so that the animated element is visible (set to `display: block`) throughout both the entry and exit animation. Without this, the exit animation would not be visible; in effect, the popover would just disappear. Again, `transition-behavior: allow-discrete` is required in this case for the animation to occur.

You'll note that we've also included a transition on the [`::backdrop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
 that appears behind the popover when it opens, to provide a nice darkening animation. `[popover]:popover-open::backdrop` is needed to select the backdrop when the popover is open.

#### Result

The code renders as follows:

**Note:** Because popovers change from `display: none` to `display: block` each time they are shown, the popover transitions from its `@starting-style` styles to its `[popover]:popover-open` styles every time the entry transition occurs. When the popover closes, it transitions from its `[popover]:popover-open` state to the default `[popover]` state.

It is possible for the style transition on entry and exit to be different in such cases. See our [Demonstration of when starting styles are used](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#demonstration_of_when_starting_styles_are_used)
 example for a proof of this.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Positioned Layout Module Level 4  <br>\# overlay](https://drafts.csswg.org/css-position-4/#overlay) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay#see_also)

---------------------------------------------------------------------------------------------------

*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    
*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [Four new CSS features for smooth entry and exit animations](https://developer.chrome.com/blog/entry-exit-animations/ "External link (opens in new tab)")
     on developer.chrome.com (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overlay/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overlay (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverlay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverlay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverlay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverlay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
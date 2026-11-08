*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#mdn-search)
    

`transition-behavior` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition-behavior`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether transitions will be started for properties whose animation behavior is [discrete](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    transition-behavior: allow-discrete;
    transition-behavior: normal;
    
    /* Global values */
    transition-behavior: inherit;
    transition-behavior: initial;
    transition-behavior: revert;
    transition-behavior: revert-layer;
    transition-behavior: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#values)

[`allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#allow-discrete)

Transitions will be started on the element for discrete animated properties.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#normal)

Transitions will _not_ be started on the element for discrete animated properties.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#description)

---------------------------------------------------------------------------------------------------------------------

The `transition-behavior` property is only relevant when used in conjunction with other transition properties, notably [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 and [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
, as no transition occurs if no properties are animated over a non-zero duration of time.

css

    .card {
      transition-property: opacity, display;
      transition-duration: 0.25s;
      transition-behavior: allow-discrete;
    }
    
    .card.fade-out {
      opacity: 0;
      display: none;
    }
    

The `transition-behavior` value can be included as part of a shorthand [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 declaration. When included in the shorthand, when using or defaulting to all properties, the `allow-discrete` value has no impact on regular animatable properties. The following CSS is equivalent to the longhand declarations above:

css

    .card {
      transition: all 0.25s;
      transition: all 0.25s allow-discrete;
    }
    
    .card.fade-out {
      opacity: 0;
      display: none;
    }
    

In the above snippet we include the `transition` property twice. The first instance does not include the `allow-discrete` value — this provides cross-browser support, ensuring the card's other properties still transition in browsers that don't support `transition-behavior`.

### [Discrete animation behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#discrete_animation_behavior)

Discrete-animated properties generally flip between two values 50% through animating between the two.

There is an exception, however, which is when animating to or from `display: none` or `content-visibility: hidden`. In this case, the browser will flip between the two values so that the transitioned content is shown for the entire animation duration.

So for example:

*   When animating `display` from `none` to `block` (or another visible `display` value), the value will flip to `block` at `0%` of the animation duration so it is visible throughout.
*   When animating `display` from `block` (or another visible `display` value) to `none`, the value will flip to `none` at `100%` of the animation duration so it is visible throughout.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

transition-behavior =   
  <transition-behavior-value>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<transition-behavior-value> =   
  normal          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  allow-discrete    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#examples)

---------------------------------------------------------------------------------------------------------------

### [Transitioning a popover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#transitioning_a_popover)

In this example, a [popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
 is animated as it [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 from hidden to shown and back again.

#### HTML

The HTML contains a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element declared as a popover using the [popover](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute, and a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 element designated as the popover's display control using its [popovertarget](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute.

html

    <button popovertarget="mypopover">Show the popover</button>
    <div popover="auto" id="mypopover">I'm a Popover! I should animate.</div>
    

#### CSS

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    [popover] {
      font-size: 1.2rem;
      padding: 10px;
    }
    

css

    [popover]:popover-open {
      opacity: 1;
      transform: scaleX(1);
    }
    
    [popover] {
      /* Final state of the exit animation */
      opacity: 0;
      transform: scaleX(0);
    
      transition-property: opacity, transform, overlay, display;
      transition-duration: 0.7s;
      transition-behavior: allow-discrete;
      /* Using the shorthand transition property, we could write:
        transition: 
          opacity 0.7s,
          transform 0.7s,
          overlay 0.7s allow-discrete,
          display 0.7s allow-discrete;
    
        or even:
        transition: all 0.7s allow-discrete;
      */
    }
    
    /* Needs to be included after the previous [popover]:popover-open 
       rule to take effect, as the specificity is the same */
    @starting-style {
      [popover]:popover-open {
        opacity: 0;
        transform: scaleX(0);
      }
    }
    

The two properties we want to animate are [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
: we want the popover to fade in and out while growing and shrinking in the horizontal direction. We set a starting state for these properties on the default hidden state of the popover element (selected via `[popover]`), and an end state on the open state of the popover (selected via the [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
 pseudo-class). We then set a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 property to animate between the two.

Because the animated element is being promoted to the [top layer](https://developer.mozilla.org/en-US/docs/Glossary/Top_layer)
 when shown and removed from the top layer when hidden — which also means that its hidden state has [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 set on it — the following properties are added to the list of transitioned elements to get the animation working in both directions. In both cases, `transition-behavior: allow-discrete` is set in the shorthand to enable discrete animation.

*   `display`: Required so that the animated element is visible (set to `display: block`) throughout both the entry and exit animation. Without this, the exit animation would not be visible; in effect, the popover would just disappear.
*   [`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
    : Required to make sure that the removal of the element from the top layer is deferred until the animation has been completed. This doesn't make a huge difference for basic animations such as this one, but in more complex cases not doing this can result in the element being removed from the overlay too quickly, meaning the animation is not smooth or effective.

In addition, a starting state for the animation is set inside the [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
 at-rule. This is needed to avoid unexpected behavior. By default transitions are not triggered on elements' first style updates, or when the `display` type changes from `none` to another type. `@starting-style` allows you to override that default in a specific controlled fashion. Without this, the entry animation would not occur and the popover would just appear.

#### Result

The code renders as follows:

**Note:** Because popovers change from `display: none` to `display: block` each time they are shown, the popover transitions from its `@starting-style` styles to its `[popover]:popover-open` styles every time the entry transition occurs. When the popover closes, it transitions from its `[popover]:popover-open` state to the default `[popover]` state.

It is possible for the style transition on entry and exit to be different in such cases. See our [Demonstration of when starting styles are used](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style#demonstration_of_when_starting_styles_are_used)
 example for a proof of this.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 2  <br>\# transition-behavior-property](https://drafts.csswg.org/css-transitions-2/#transition-behavior-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`overlay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
    
*   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    
*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   [Four new CSS features for smooth entry and exit animations](https://developer.chrome.com/blog/entry-exit-animations/ "External link (opens in new tab)")
     on developer.chrome.com (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition-behavior/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition-behavior (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-behavior&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-behavior%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-behavior%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-behavior%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
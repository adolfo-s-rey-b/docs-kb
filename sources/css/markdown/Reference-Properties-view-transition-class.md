*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#mdn-search)
    

`view-transition-class` CSS property
====================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view-transition-class`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property provides the selected elements with one or more identifying classes ([`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
s), providing an additional method of styling the view transitions for those elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#syntax)

-------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#values)

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

An identifying name used to select view transition pseudo-elements for styling. Unlike `view-transition-name`, a class does not need to be unique and does not cause the element to participate in a separate view transition group.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#none)

No class would apply to the named view transition pseudo-elements generated for this element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#description)

-----------------------------------------------------------------------------------------------------------------------

The `view-transition-class` value provides a styling hook, similar to a CSS class name, which can be used to apply the same styles to multiple view transition pseudo-elements. It does not mark an element for capturing. Each individual element still needs its own unique [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
; the `view-transition-class` is only used as an additional way to style elements that already have a `view-transition-name`. Support for determining the `view-transition-name` automatically is being discussed in the [CSS View Transitions Module Level 2](https://drafts.csswg.org/css-view-transitions-2/#auto-vt-name "External link (opens in new tab)")
 spec.

The `view-transition-class` applies styles using the view transition pseudo-elements, including [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
, [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
, [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
, and [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
. This is different from the `view-transition-name`, which matches view transitions between the element in the old state with its corresponding element in the new state.

Until the `view-transition-class` property is fully supported in all browsers supporting view transitions, include a custom `::view-transition-group()` for each element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

view-transition-class =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#examples)

-----------------------------------------------------------------------------------------------------------------

### [Styling a shared class across multiple elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#styling_a_shared_class_across_multiple_elements)

In this example, three cards each have a unique [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
 (required for pairing old and new states), but they all share the same `view-transition-class`. This lets you write a single rule that styles all their transitions at once, rather than repeating styles for each name individually. Unlike `view-transition-name`, a `view-transition-class` does not need to be unique.

### [Using multiple classes on a single element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#using_multiple_classes_on_a_single_element)

A `view-transition-class` value can be a space-separated list of identifiers, letting you compose several "atomic" styles on the same element and target each one independently of your view transition pseudo-elements. In this example, both cards share the same two classes — `slide` controls the animation, and `fast-transition` controls its duration — while each card still has its own unique [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 2  <br>\# view-transition-class-prop](https://drafts.csswg.org/css-view-transitions-2/#view-transition-class-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
    
*   [Using the View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using)
     guide
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-transition-class/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-transition-class (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-class&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-class%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-class%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-class%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7447816a276e95c5b4c2ab2f6a1f80b081371de2%0A*+Document+last+modified%3A+2026-05-07T12%3A13%3A48.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
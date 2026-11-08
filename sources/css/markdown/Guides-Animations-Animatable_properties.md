*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#mdn-search)
    

Animatable CSS properties
=========================

[CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 and [Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 rely on the concept of **animatable** properties, and all CSS properties are animatable unless otherwise specified. Each property's _animation type_ determines how values [combine](https://drafts.csswg.org/css-values/#combining-values "External link (opens in new tab)")
 - interpolate, add, or accumulate - for this property. Transitions only involve interpolation, whereas animations may use all three combination methods.

**Note:** The animation type for each CSS property is listed in its "Formal definition" table (E.g., [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#formal_definition)
).

**Note:** The interpolation method for each CSS data type is described in its "Interpolation" section (E.g., [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation)
).

[Animation types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#animation_types)

----------------------------------------------------------------------------------------------------------------------------

There are mainly four animation types as defined in the [Web Animations](https://drafts.csswg.org/web-animations-1/#animating-properties "External link (opens in new tab)")
 specification:

[Not animatable](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#not_animatable)

The property is not animatable. It is not processed when listed in an animation keyframe and is unaffected by transitions.

**Note:** An animation effect targeting only properties that are not animatable will still exhibit the usual behavior for an animation effect (E.g., firing the [`animationstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event "animationstart")
 event).

[Discrete](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)

The property's values are not additive, and interpolation swaps from the start value to the end value at `50%`. Specifically, denoting by `p` the progress value:

*   If `p < 0.5`, then `V_result = V_start`;
*   If `p ≥ 0.5`, then `V_result = V_end`.

[By computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#by_computed_value)

Corresponding individual components of the computed values are combined using the indicated procedure for that value type. If the number of components or the types of corresponding components do not match, or if any component value uses discrete animation and the two corresponding values do not match, then the property values combine as discrete.

[Repeatable list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#repeatable_list)

Same as by computed value except that if the two lists have differing numbers of items, they are first repeated to the least common multiple numbers of items. Each item is then combined by computed value. If a pair of values cannot be combined or any component value uses discrete animation, then the property values combine as discrete.

Some properties have specific interpolation behavior not covered by these four types. In this case, refer to the property's "Interpolation" section (E.g., [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility#interpolation)
).

[Animating custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#animating_custom_properties)

----------------------------------------------------------------------------------------------------------------------------------------------------

For custom properties registered using the [`registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "registerProperty()")
 method, the animation type is by computed value, with the computed value type [determined](https://drafts.css-houdini.org/css-properties-values-api/#calculation-of-computed-values "External link (opens in new tab)")
 by the property's syntax definition.

For unregistered custom properties, the animation type is discrete.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [Using CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [Using CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/animations/animatable_properties/index.md?plain=1 "Folder: en-us/web/css/guides/animations/animatable_properties (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimations%2FAnimatable_properties&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fanimations%2Fanimatable_properties%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FAnimations%2FAnimatable_properties%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fanimations%2Fanimatable_properties%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
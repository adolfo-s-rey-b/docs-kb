*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#mdn-search)
    

`view-timeline-inset` CSS property
==================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view-timeline-inset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to specify one or two values representing an adjustment to the position of the scrollport (see [Scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 for more details) in which the subject element of a _named view progress timeline_ animation is deemed to be visible. Put another way, this allows you to specify start and/or end inset (or outset) values that offset the position of the timeline.

This can be combined with or used instead of [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 and its longhand properties, which can be used to set the attachment range of an animation along its timeline. See [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 for more details.

**Note:** If the scroller element does not overflow its container in the axis dimension or if the overflow is hidden or clipped, no scroll progress timeline will be created.

The `view-timeline-inset`, [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
, and [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
 properties can also be set using the [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
 shorthand property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#syntax)

-----------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#values)

Allowed values for `view-timeline-inset` are:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#auto)

If set, the corresponding [`scroll-padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
 (or equivalent longhand value) for that edge of the scrollport is used. If this is not set (or set to `auto`), the value will usually be 0, although some user agents may use heuristics to determine a different default value if appropriate.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Any valid `<length-percentage>` value is accepted as an inset/outset value.

*   If the value is positive, the position of the animation's start/end will be moved inside the scrollport by the specified length or percentage.
*   If the value is negative, the position of the animation's start/end will be moved outside the scrollport by the specified length or percentage, i.e., it will start animating before it appears in the scrollport, or finish animating after it leaves the scrollport.

If two values are provided, the first value represents the start inset/outset in the relevant axis (where the animation begins) and the second value represents the end inset/outset (where the animation ends). If only one value is provided, the start and end inset/outset are both set to the same value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the corresponding dimension of the relevant scrollport |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list where each item may be either 'auto' or a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

view-timeline-inset =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#examples)

---------------------------------------------------------------------------------------------------------------

### [Creating a named view progress timeline with inset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#creating_a_named_view_progress_timeline_with_inset)

A view progress timeline named `--subject-reveal` is defined using the `view-timeline` property on a subject element with a `class` of `animation`. This is then set as the timeline for the same element using `animation-timeline: --subject-reveal;`. The result is that the subject element animates as it moves upwards through the document as it is scrolled.

A `view-timeline-inset` declaration is also set to make the animation begin later than expected, and finish earlier.

#### HTML

The HTML for the example is shown below.

#### CSS

The `subject` element and its containing `content` element are styled minimally, and the text content is given some basic font settings:

The `<div>` with the class of `subject` is also given a class of `animation` — this is where `view-timeline` is set to define a named view progress timeline. We also give it a `view-timeline-inset` declaration to make the animation begin later than expected, and finish earlier. It is also given an `animation-timeline` name with the same value to declare that this will be the element animated as the view progress timeline is progressed.

Last, an animation is specified on the element that animates its opacity and scale, causing it to fade in and size up as it moves up the scroller.

#### Result

Scroll to see the subject element being animated.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# view-timeline-inset](https://drafts.csswg.org/scroll-animations/#view-timeline-inset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`timeline-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    , [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    , [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-timeline-inset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-timeline-inset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline-inset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline-inset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline-inset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline-inset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
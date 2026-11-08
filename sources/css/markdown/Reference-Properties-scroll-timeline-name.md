*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#mdn-search)
    

`scroll-timeline-name` CSS property
===================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll-timeline-name`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to define the name of a [named scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_scroll_progress_timelines)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#syntax)

------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#values)

This property is specified as one of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#none)

The timeline has no name.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#dashed-ident)

An arbitrary custom identifier defining a name for a scroll progress timeline, which can then be referenced in an [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#description)

----------------------------------------------------------------------------------------------------------------------

The `scroll-timeline-name` property is used to define the name of a _named scroll progress timeline_, which is progressed through by scrolling a scrollable element (_scroller_) between top and bottom (or left and right).

Set the `scroll-timeline-name` property on the scroller that provides the timeline. The name is then referenced in an [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 declaration to indicate the container's element that is used to drive the progress of the animation through the scrolling action.

If the element does not overflow its container in the axis dimension or if the overflow is hidden or clipped, no timeline will be created.

The `scroll-timeline-name`, along with the [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
 property, can also be set using the [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | scroll containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `none` or an ordered list of identifiers |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

scroll-timeline-name =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#examples)

----------------------------------------------------------------------------------------------------------------

### [Creating a named scroll progress timeline animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#creating_a_named_scroll_progress_timeline_animation)

In this example, a scroll timeline named `--square-timeline` is defined using the `scroll-timeline-name` property on the element with the ID `container`. This is then applied to the animation on the `#square` element using `animation-timeline: --square-timeline`.

#### HTML

The HTML for the example is shown below.

#### CSS

The CSS for the container sets it as the source of a scroll timeline named `--square-timeline` using the `scroll-timeline-name` property. No [scrollbar axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
 is defined here because the vertical axis will be used by default.

The height of the container is set to `300px`, and the container is also set to create a vertical scrollbar if it overflows (the CSS `height` rule on the `stretcher` element below does make the content overflow its container).

The CSS below defines a square that rotates according to the timeline provided by the `animation-timeline` property, which is set to the `--square-timeline` timeline named above.

The `stretcher` CSS rule sets the block height to `600px`, which creates content that overflows the container element, thereby creating scroll bars. Without this element, the content would not overflow the container, there would be no scrollbar, and hence no scroll timeline to associate with the animation timeline.

#### Result

Scroll the vertical bar to see the square animate as you scroll.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# scroll-timeline-name](https://drafts.csswg.org/scroll-animations/#scroll-timeline-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    , [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
    
*   [`timeline-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
    
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scroll-timeline-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scroll-timeline-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-timeline-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-timeline-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscroll-timeline-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscroll-timeline-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
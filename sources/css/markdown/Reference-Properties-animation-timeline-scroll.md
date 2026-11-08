*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#mdn-search)
    

`scroll()` CSS function
=======================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scroll()`** [CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 can be used with the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property to create an [anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_scroll_progress_timelines)
, defining the scroller and axis of the timeline.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#syntax)

-----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#parameters)

[`<scroller>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#scroller)

The scroller element that will provide the scroll progress timeline. Valid values include:

[`nearest`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#nearest)

The nearest ancestor of the current element that has scrollbars on either axis. This is the default value.

[`root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#root)

The root element of the document.

[`self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#self)

The current element itself.

[`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#axis)

An [`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 keyword value describing the direction, or axis, of the scrollport that controls the scroll-driven animation. The default value is `block`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#description)

---------------------------------------------------------------------------------------------------------------------------

The `scroll()` CSS function can be used as a single value within the comma-separated [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property to specify a scroll progress timeline for a [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animation. It defines the scrollable element (_scroller_) and scrollbar axis that will provide the animation timeline.

By default, `scroll()` references the `block` axis of the `nearest` ancestor scroll container. The scroller and axis values can be specified in any order.

The following five declarations are equivalent:

The scroll progress timeline is progressed through by scrolling the scroller horizontally or vertically, depending on the `<axis>` and [writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Writing_mode_systems)
. If the indicated axis does not contain a scrollbar, then the animation timeline will be inactive.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

<scroll()> =   
  scroll( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <scroller> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <axis> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<scroller> =   
  root     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nearest  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self       
  
[<axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#examples)

---------------------------------------------------------------------------------------------------------------------

### [Setting an anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#setting_an_anonymous_scroll_progress_timeline)

In this example, the `#square` element is animated using an anonymous scroll progress timeline, which is applied to the element to be animated using the `scroll()` function. The timeline in this particular example is provided by the nearest parent element that has (any) scrollbar, from the scrollbar in the block direction.

#### HTML

The HTML for the example is shown below.

#### CSS

The CSS below defines a square that rotates in alternate directions according to the timeline provided by the `animation-timeline` property. In this case, the timeline is provided by `scroll(block nearest)`, which means that it will select the scrollbar in the block direction of the nearest ancestor element that has scrollbars; in this case the vertical scrollbar of the "container" element.

**Note:** `block` and `nearest` are actually the default parameter values, so we could have used just `scroll()`.

The CSS for the container sets its height to 300px and we also set the container to create a vertical scrollbar if it overflows. The "stretcher" CSS sets the block height to 600px, which forces the container element to overflow. These two together ensure that the container has a vertical scrollbar, which allows it to be used as the source of the anonymous scroll progress timeline.

#### Result

Scroll to see the square element being animated.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# scroll-notation](https://drafts.csswg.org/scroll-animations/#scroll-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [`ScrollTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ScrollTimeline)
    
*   [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-timeline/scroll/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-timeline/scroll (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline%2Fscroll&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%2Fscroll%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline%2Fscroll%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%2Fscroll%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
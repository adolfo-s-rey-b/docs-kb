*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#mdn-search)
    

`view()` CSS function
=====================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view()`** [CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 is used with the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property to create an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
 based on when an element comes into view inside its nearest [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. You can adjust the tracking axis and the optional insets to control when the element is considered "in view".

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#syntax)

---------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#parameters)

[`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#axis)

Specifies the scroll direction used by the view progress timeline. The value can be one of the [`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 keywords: `block`, `inline`, `x`, or `y`. The default value is `block`.

[`<view-timeline-inset>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#view-timeline-inset)

Specifies the inset area that defines when an element is considered "in view". The value can be the keyword `auto` or up to two [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#description)

-------------------------------------------------------------------------------------------------------------------------

A view progress timeline progresses based on changes in the visibility of a subject element inside its nearest scroll container. The `view()` function is used with the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property to create such a view progress timeline.

The function's parameters can specify the scrollbar axis along which timeline progress is tracked and insets that adjust the position of the box in which the subject is considered visible.

*   **Axis**: By default, `view()` uses the block axis. You can change this by providing an explicit `<axis>` value. If the chosen axis does not contain a scrollbar, then the animation timeline will be inactive (zero progress).
*   **Inset**: By default, the timeline is at `0%` (the `from` keyframe in the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
     animation) when the subject is first visible at one edge of the scroller, and at `100%` (the `to` keyframe) when the subject's outer border edge reaches the opposite edge of the scroller. You can control these points with the `<view-timeline-inset>` parameters. The animation lasts as long as the element is in the inset-adjusted view. The inset is used to determine whether the element is in view, which in turn determines the length of the animation timeline. The inset consists of up to two values, each of which can be either `auto` or a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    .
    *   The first value defines the start, an inward offset from the scrollport's beginning.
    *   The second value, if present, specifies the end, an inward offset from the scrollport's end. If the value is greater than `0`, it specifies an inset (positive). A negative value defines an outset adjustment to the [scrollport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container#scrollport)
        .

The axis and inset components can be specified in any order. Within the inset component, the first value defines the start inset, and the second value defines the end inset.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

<view()> =   
  view( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <axis> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'view-timeline-inset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         
  
[<view-timeline-inset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
 =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#examples)

-------------------------------------------------------------------------------------------------------------------

### [Creating an anonymous view progress timeline using `view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#creating_an_anonymous_view_progress_timeline_using_view)

In this example, we create an anonymous view progress timeline for the element with the `subject` and `animation` classes using `animation-timeline: view()`. The result is that as you scroll the document, this element animates as it moves upward through the document.

#### HTML

In the middle of the text, we include the following (note that the HTML includes a lot of content that we've hidden for brevity):

We also include two overlays to enable visualizing the animation range:

#### CSS

The styles for the `subject` and `subject-container` include:

The `subject-container` class shows the bounds of the animation. We define `top` and `bottom` overlays to mark the inset-adjusted scrollport.

The `<div>` element with the `subject` class is also given a class of `animation`. The `grow` animation causes the `subject` element to grow or shrink. The `animation-timeline: view(block 50% 10%)` rule sets the element to be animated as it progresses through the view progress timeline created by its nearest scroll container (in this case, the document's root element).

While scrolling down, note how the inset values `50% 10%` cause the animation to start when the element is 10% from the bottom of the scrollport and to finish when it is 50% from the top. As the animation progresses along the timeline, the `subject` grows. When scrolling up the animation proceeds in the reverse direction, starting at 50% from the top, moving backward through the keyframes, and ending at 10% from the bottom. So, as the animation runs backward, the `subject` shrinks.

An important point to remember is that the animation lasts only as long as the `subject` element is within view, which is defined here by `50% 10%` inset values.

The rest of the CSS is hidden for brevity.

#### Result

Scroll to see the element with the `subject` class animate as it enters and leaves the adjusted inset view.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# view-notation](https://drafts.csswg.org/scroll-animations/#view-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [`ViewTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline)
    
*   [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-timeline/view/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-timeline/view (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline%2Fview&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%2Fview%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline%2Fview%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%2Fview%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3142e11b227fb3e7c6de298ea9049aa1999d6f%0A*+Document+last+modified%3A+2026-04-27T02%3A18%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
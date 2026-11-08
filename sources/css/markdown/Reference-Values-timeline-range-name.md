*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#mdn-search)
    

`<timeline-range-name>` CSS type
================================

The **`<timeline-range-name>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 data type is a CSS identifier representing one of the predefined named timeline ranges inside a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
.

The `<timeline-range-name>` keyword values are used in [keyframe selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
 and the following longhand and shorthand properties:

*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    
*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
     shorthand
*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
    
*   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
    
*   [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     shorthand
*   [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
    
*   [`timeline-trigger-active-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
    
*   [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     shorthand

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#syntax)

-------------------------------------------------------------------------------------------------------

Valid `<timeline-range-name>` values:

[`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#cover)

Represents the full range of a view progress timeline, from the point where the subject element's start border edge first enters the scrollport's view progress visibility range (`0%` progress) to the point where the end border edge has completely left it (`100%` progress). This is the default range for [view progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
.

[`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#contain)

Represents the range of a view progress timeline where the subject element is fully contained by, or fully contains, the view progress visibility range within the [scrollport](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container#scrollport)

*   If the subject element is smaller than the scrollport, it ranges from the point where the subject element is first completely contained by the scroll port (`0%` progress), to the point where it is no longer completely contained by the scroll port (`100%` progress).
*   If the subject element is larger than the scrollport, it ranges from the point where the subject element first completely covers the scroll port (`0%` progress), to the point where it no longer completely covers the scrollport (`100%` progress).

[`entry`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#entry)

Represents the range of a view progress timeline from the point where the subject element first starts to enter the scroll port, to the point where it has completely entered the scrollport. `0%` is equivalent to `0%` of the `cover` range. `100%` is equivalent to `0%` of the `contain` range.

[`exit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#exit)

Represents the range of a view progress timeline from the point where the subject element first starts to exit the scroll port, to the point where it has completely exited the scrollport. `0%` is equivalent to `100%` of the `contain` range. `100%` is equivalent to `100%` of the `cover` range.

[`entry-crossing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#entry-crossing)

Represents the range during which the principal box crosses the end border edge. The start (0% progress) of the range occurs when the start border edge of the element's principal box coincides with the end edge of its view progress visibility range. The end (100%) of the range is the point at which the end border edge of the element's principal box coincides with the end edge of its view progress visibility range. The size of the range is the size of the element's principal box in the scroll direction.

[`exit-crossing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#exit-crossing)

Represents the range where the principal box crosses the start border edge. The range start (0% progress) occurs when the start border edge of the element's principal box coincides with the start edge of its view progress visibility range. The range end (100% progress) is the point at which the end border edge of the element's principal box coincides with the start edge of its view progress visibility range. The size of the range is the size of the element's principal box in the scroll direction.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#scroll)

Represents the full range of the [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 on which the view progress timeline is defined. The range start (0% progress) and end (100% progress) occur at the very start and end positions of the scroll container underlying the view progress timeline. This is the default range for [scroll progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

<timeline-range-name> =   
  cover           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  entry           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exit            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  entry-crossing  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exit-crossing   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll            

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#examples)

-----------------------------------------------------------------------------------------------------------

See the [View timeline range visualizer](https://scroll-driven-animations.style/tools/view-timeline/ranges/ "External link (opens in new tab)")
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# typedef-timeline-range-name](https://drafts.csswg.org/scroll-animations/#typedef-timeline-range-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    , [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    , [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    
*   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
    , [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    
*   [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
    
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [View timeline range visualizer](https://scroll-driven-animations.style/tools/view-timeline/ranges/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/timeline-range-name/index.md?plain=1 "Folder: en-us/web/css/reference/values/timeline-range-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftimeline-range-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftimeline-range-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftimeline-range-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftimeline-range-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4aba58b4ad2745a73054f60b6d649d8e29b7b44d%0A*+Document+last+modified%3A+2026-10-05T11%3A36%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
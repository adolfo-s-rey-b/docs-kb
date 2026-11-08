*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#mdn-search)
    

`<axis>` CSS type
=================

The **`<axis>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 data type specifies the scrolling direction of the [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 controlling a [scroll timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
.

The `<axis>` keyword values are used in the following [CSS functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 and properties:

*   [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
     shorthand
*   [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
    
*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
     shorthand
*   [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#syntax)

----------------------------------------------------------------------------------------

Valid `<axis>` values:

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#block)

The block axis of the scroller element, which is the axis in the direction perpendicular to the flow of text within a line. For horizontal writing modes, such as standard English, this is the same as `y`, while for vertical writing modes, it is the same as `x`.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#inline)

The inline axis of the scroller element, which is the axis in the direction parallel to the flow of text in a line. For horizontal writing modes, this is the same as `x`, while for vertical writing modes, this is the same as `y`.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#x)

The horizontal axis of the scroller element.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#y)

The vertical axis of the scroller element.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#formal_syntax)

------------------------------------------------------------------------------------------------------

<axis> =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# typedef-axis](https://drafts.csswg.org/scroll-animations/#typedef-axis) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis#see_also)

--------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
     guide
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/axis/index.md?plain=1 "Folder: en-us/web/css/reference/values/axis (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Faxis&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Faxis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Faxis%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Faxis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
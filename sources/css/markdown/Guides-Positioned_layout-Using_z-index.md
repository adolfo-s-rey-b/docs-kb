*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#mdn-search)
    

Using z-index
=============

The first article of this guide, [Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
, explains how stacking is arranged by default. If you want to create a custom stacking order, you can use the [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
 property on a [positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#types_of_positioning)
 element.

The `z-index` property can be specified with an integer value (positive, zero, or negative), which represents the position of the element along an imaginary z-axis. If you are not familiar with the term 'z-axis', imagine the page as a stack of layers, each one having a number. Layers are rendered in numerical order, with larger numbers above smaller numbers (_X_ represents an arbitrary positive integer):

| Layer | Description |
| --- | --- |
| Bottom layer | Farthest from the observer |
| Layer -X | Layers with negative `z-index` values |
| Layer 0 | Default rendering layer |
| Layer X | Layers with positive `z-index` values |
| Top layer | Closest to the observer |

**Note:**

*   When no `z-index` property is specified, elements are rendered on the default rendering layer (Layer 0).
*   If several elements share the same `z-index` value (i.e., they are placed on the same layer), stacking rules explained in the section [Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
     apply.

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#example)

-----------------------------------------------------------------------------------------------------------

In this example, the layers' stacking order is rearranged using `z-index`. The `z-index` of DIV #5 has no effect since it is not a positioned element.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#css)

[Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#result)

---------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Understanding z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Understanding_z-index)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [Stacking floating elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements)
    
*   [Stacking without `z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/using_z-index/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout/using_z-index (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FUsing_z-index&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fusing_z-index%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FUsing_z-index%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fusing_z-index%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
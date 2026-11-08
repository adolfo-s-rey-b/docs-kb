*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#mdn-search)
    

Stacking context example 3
==========================

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#description)

--------------------------------------------------------------------------------------------------------------------------------

This example shows problems that arise when mixing several positioned elements in a multi-level HTML hierarchy and when `z-index` values are assigned using class selectors.

The example has a three-level hierarchical menu made from several positioned `div` elements. Second-level and third-level `div` elements appear when a user hovers or clicks on their parents. Usually this kind of menu is script-generated either client-side or server-side, so style rules are assigned with a class selector instead of the id selector.

If the three menu levels partially overlap, then managing stacking could become a problem.

The first-level menu is relatively positioned, creating a stacking context.

The second-level menu is absolutely positioned inside the parent element. In order to put it above all first-level menus, the `z-index` property is used. The problem is that for each second-level menu, a stacking context is created and each third-level menu belongs to the context of its parent.

So a third-level menu will be stacked under the following second-level menus, because all second-level menus share the same z-index value and the default stacking rules apply.

To better understand the situation, here is the stacking context hierarchy (the three dots "..." represent multiple repetition of the previous line):

*   Root stacking context
    *   LEVEL #1
        
        *   LEVEL #2 (`z-index`: 1)
            
            *   LEVEL #3
            *   …
            *   LEVEL #3
        *   LEVEL #2 (`z-index`: 1)
            
        *   …
            
        *   LEVEL #2 (`z-index`: 1)
            
    *   LEVEL #1
        
    *   …
        
    *   LEVEL #1
        

This problem can be avoided by removing overlapping between different level menus, or by using individual (and different) z-index values assigned through the id selector instead of class selector, or by flattening the HTML hierarchy.

**Note:** In the source code you will see that second-level and third level menus are made of several `div` elements contained in an absolutely positioned container. This is useful to group and position all of them at once.

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#example)

------------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#css)

[Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#result)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
    : The stacking rules that apply when `z-index` is not used.
*   [Stacking floating elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements)
    : How floating elements are handled with stacking.
*   [Using z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index)
    : How to use `z-index` to change default stacking.
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    : Notes on the stacking context.
*   [Stacking context example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1)
    : 2-level HTML hierarchy, `z-index` on the last level
*   [Stacking context example 2](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_2)
    : 2-level HTML hierarchy, `z-index` on all levels

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/stacking_context/example_3/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout/stacking_context/example_3 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context%2FExample_3&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%2Fexample_3%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context%2FExample_3%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%2Fexample_3%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
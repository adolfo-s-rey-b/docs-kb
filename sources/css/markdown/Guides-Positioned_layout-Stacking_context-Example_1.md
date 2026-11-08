*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#mdn-search)
    

Stacking context example 1
==========================

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#description)

--------------------------------------------------------------------------------------------------------------------------------

Let's start with a basic example. In the root stacking context, there are two relatively positioned `<div>` elements (DIV #1 and DIV #3) without `z-index` properties. Inside DIV #1, there is an absolutely positioned DIV #2, while in DIV #3, there is an absolutely positioned DIV #4, both without `z-index` properties.

The only stacking context is the root context. Without `z-index` values, elements are stacked in order of occurrence.

![Stacking context example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1/understanding_zindex_05a.png)

If DIV #2 is assigned a positive (non-zero and non-auto) z-index value, it is rendered above all the other DIVs.

![Stacking context example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1/understanding_zindex_05b.png)

Then if DIV #4 is also assigned a positive z-index greater than DIV #2's z-index, it is rendered above all the other DIVs including DIV #2.

![Stacking context example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1/understanding_zindex_05c.png)

In this last example you can see that DIV #2 and DIV #4 are not siblings, because they belong to different parents in the HTML elements' hierarchy. Even so, stacking of DIV #4 with respect of DIV #2 can be controlled through `z-index`. It happens that, since DIV #1 and DIV #3 are not assigned any `z-index` value, or any other [features that create a stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context#features_creating_stacking_contexts)
, they do not create a stacking context. This means that all their content, including DIV #2 and DIV #4, belongs to the same root stacking context.

In terms of stacking contexts, DIV #1 and DIV #3 are assimilated into the root element, and the resulting hierarchy is the following:

*   Root stacking context
    *   DIV #2 (`z-index`: 1)
    *   DIV #4 (`z-index`: 2)

**Note:** DIV #1 and DIV #3 are not translucent. It is important to remember that assigning an opacity value of less than `1` to an element implicitly creates a stacking context, as does adding a `z-index` value to a positioned element. This example also shows what happens when a parent element doesn't create a stacking context.

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#example)

------------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#css)

[Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#result)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Example: 2-level HTML hierarchy, `z-index` on all levels](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_2)
    
*   [Example: 3-level HTML hierarchy, `z-index` on the second level](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_3)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context/Example_1/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/stacking_context/example_1/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout/stacking_context/example_1 (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context%2FExample_1&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%2Fexample_1%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_context%2FExample_1%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_context%2Fexample_1%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc1bbbf977b4fd477104265cd87f74cdf42616b0d%0A*+Document+last+modified%3A+2026-02-05T16%3A58%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
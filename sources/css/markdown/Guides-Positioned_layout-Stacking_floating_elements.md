*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#mdn-search)
    

Stacking floating elements
==========================

For floating elements, the stacking order is a bit different. Floating elements are placed between non-positioned elements and positioned elements:

1.  The background and borders of the root element.
2.  Descendant non-positioned elements, in order of appearance in the HTML.
3.  _Floating elements_.
4.  Descendant positioned elements, in order of appearance in the HTML.

See [types of positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position#types_of_positioning)
 for an explanation of positioned and non-positioned elements.

**Note:** If an `opacity` value is applied to a non-positioned element (i.e., DIV #4 in the example below), something strange happens: the background and border of that block pop up above the floating blocks and the positioned blocks. This is due to a peculiar part of the specification: applying an `opacity` value creates a new stacking context (see [What No One Told You About Z-Index](https://philipwalton.com/articles/what-no-one-told-you-about-z-index/ "External link (opens in new tab)")
).

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#example)

------------------------------------------------------------------------------------------------------------------------

You can see in this example that the background and border of the non-positioned element (DIV #4) is completely unaffected by floating elements, but the content is affected. This happens according to standard float behavior which can be shown with a rule added to the above list:

1.  The background and borders of the root element.
2.  Descendant non-positioned elements, in order of appearance in the HTML.
3.  Floating elements.
4.  _Descendant non-positioned inline elements_.
5.  Descendant positioned elements, in order of appearance in the HTML.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#css)

[Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#result)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Understanding z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Understanding_z-index)
    
*   [Stacking without the `z-index` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_without_z-index)
    
*   [Using z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Using_z-index)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [CSS positioned layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_floating_elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/positioned_layout/stacking_floating_elements/index.md?plain=1 "Folder: en-us/web/css/guides/positioned_layout/stacking_floating_elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_floating_elements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_floating_elements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FPositioned_layout%2FStacking_floating_elements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fpositioned_layout%2Fstacking_floating_elements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#mdn-search)
    

Split navigation
================

The **split navigation** is a navigation pattern where one or more elements are separated from the rest of the navigation items.

![Items separated into two groups.](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation/split-navigation.png)

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#requirements)

----------------------------------------------------------------------------------------------------------------------

A common navigation pattern is to have one element pushed away from the others. We can use flexbox to achieve this, without needing to make the two sets of items into two separate flex containers.

[Recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#recipe)

----------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

html

    <nav>
      <ul class="main-nav">
        <li><a href="">About</a></li>
        <li><a href="">Products</a></li>
        <li><a href="">Our Team</a></li>
        <li class="push"><a href="">Contact</a></li>
      </ul>
    </nav>
    

css

    .main-nav {
      margin: 0;
      padding: 0;
      list-style: none;
      font: 1.2em sans-serif;
    
      display: flex;
    }
    
    .main-nav a {
      padding: 0.5em 1em;
      display: block;
    }
    
    .push {
      margin-left: auto;
    }
    

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#choices_made)

----------------------------------------------------------------------------------------------------------------------

This pattern combines auto margins with flexbox to split the items.

An auto margin absorbs all available space in the direction it is applied. This is how centering a block with auto margins works — you have a margin on each side of the block trying to take up all of the space, thus pushing the block into the middle.

In this case the left auto margin takes up any available space and pushes the item over to the right. You could apply the class `push` to any item in the list.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation#see_also)

--------------------------------------------------------------------------------------------------------------

*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module
*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     property
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Split_navigation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/split_navigation/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/split_navigation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FSplit_navigation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fsplit_navigation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FSplit_navigation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fsplit_navigation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
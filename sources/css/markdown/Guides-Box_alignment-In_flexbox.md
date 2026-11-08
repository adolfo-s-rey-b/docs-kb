*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#mdn-search)
    

Box alignment in flexbox
========================

The [box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module details how alignment works in various layout methods. In this guide, we explore how box alignment works in the context of [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
. As this guide aims to detail things which are specific to flexbox and box alignment, it should be read in conjunction with the [box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
 guide, which details the common features of box alignment across layout methods.

[Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#basic_example)

----------------------------------------------------------------------------------------------------------------

In this flexbox example, three flex items are aligned on the main axis using [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 and on the cross axis using [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
. The first item overrides the `align-items` values set on the group by setting [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 to `center`.

    body {
      font-family: sans-serif;
    }
    .box > * {
      padding: 20px;
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
    }
    

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three <br />has <br />extra <br />text</div>
    </div>
    

css

    .box {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      border: 2px dotted rgb(96 139 168);
    }
    
    .box :first-child {
      align-self: center;
    }
    

[The axes and flex-direction](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#the_axes_and_flex-direction)

--------------------------------------------------------------------------------------------------------------------------------------------

Flexbox respects the writing mode of the document, therefore if you are working in English and set [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 to `flex-end` this will align the items to the end of the flex container. If you are working with [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 set to `row`, this alignment will be in the inline direction.

However, in flexbox you can change the main axis by setting `flex-direction` to `column`. In this case, `justify-content` will align items in the block direction. Therefore it is easiest to think about the main and cross axis when working in flexbox like so:

*   The main axis = direction set by `flex-direction` = alignment via `justify-content`
*   The cross axis = runs across the main axis = alignment via [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    , [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    /[`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    

### [Main Axis Alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#main_axis_alignment)

*   [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    

### [Cross Axis Alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#cross_axis_alignment)

*   [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    

### [There is no justify-self in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#there_is_no_justify-self_in_flexbox)

On the main axis, Flexbox deals with the flex items as a group. The amount of space required to lay out the items is calculated, and the leftover space is then available for distribution. The `justify-content` property controls how that leftover space is used. Set `justify-content: flex-end` and the extra space is placed before the items, `justify-content: space-around` and it is placed either side of the item in that dimension, etc.

This means that a `justify-self` property does not make sense in flexbox as we are always dealing with moving the entire group of items around.

On the cross axis `align-self` makes sense as we potentially have additional space in the flex container in that dimension, in which a single item can be moved to the start and end.

[Alignment and auto margins](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#alignment_and_auto_margins)

------------------------------------------------------------------------------------------------------------------------------------------

There is a specific use case in flexbox where we might think that a `justify-self` property is what we need, and this is when we want to split a set of flex items, perhaps to create a split navigation pattern. For this use case, we can use an `auto` margin. A margin set to `auto` will absorb all available space in its dimension. This is how centering a block with auto margins works. By setting the left and right margin to `auto`, both sides of our block try to take up all of the available space and so push the box into the center.

By setting a [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 of `auto` on one item in a set of flex items all aligned to start, we can create a split navigation. This works well with flexbox and the alignment properties. As soon as there is no space available for the auto margin, the item behaves in the same way as all the other flex items and shrinks to try to fit into space.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div class="push">Four</div>
      <div>Five</div>
    </div>
    

css

    .box {
      display: flex;
      border: 2px dotted rgb(96 139 168);
    }
    .push {
      margin-left: auto;
    }
    

[The `gap` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#the_gap_properties)

----------------------------------------------------------------------------------------------------------------------------

*   [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
    
*   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    

### [Creating fixed size gaps between items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#creating_fixed_size_gaps_between_items)

On the main axis, the `column-gap` property creates fixed size gaps between adjacent items.

On the cross axis the `row-gap` property creates spacing between adjacent flex lines, therefore [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 must also be set to `wrap` for this to have any effect.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
    </div>
    

css

    .box {
      width: 450px;
      display: flex;
      flex-wrap: wrap;
      row-gap: 10px;
      column-gap: 2em;
      border: 2px dotted rgb(96 139 168);
    }
    
    .box > * {
      flex: 1;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module
*   [Box alignment overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/Overview)
    
*   [Box alignment in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_grid_layout)
    
*   [Box alignment in multiple-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_multi-column_layout)
    
*   [Box alignment for block, absolutely positioned, and table layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_block_abspos_tables)
    
*   [Aligning items in flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items)
    
*   [Cross axis](https://developer.mozilla.org/en-US/docs/Glossary/Cross_Axis)
    
*   [Main axis](https://developer.mozilla.org/en-US/docs/Glossary/Main_Axis)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/box_alignment/in_flexbox/index.md?plain=1 "Folder: en-us/web/css/guides/box_alignment/in_flexbox (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_flexbox&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_flexbox%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBox_alignment%2FIn_flexbox%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbox_alignment%2Fin_flexbox%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
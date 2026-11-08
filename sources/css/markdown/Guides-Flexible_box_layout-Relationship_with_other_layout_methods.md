*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#mdn-search)
    

Relationship of flexbox to other layout methods
===============================================

In this article, we will take a look at how flexbox fits in with all the other CSS modules. We'll find out which specifications you also need to take notice of if you want to learn flexbox, and find out why flexbox is different to some other modules.

[The box alignment module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#the_box_alignment_module)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many people first look at flexbox when they want to properly align flex items inside a flex container. Flexbox provides access to properties that allow the alignment of items on their cross axis and justification of items on the main axis.

Flexbox was originally defined in its own [flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 module, but the properties and values that are common to other layout methods are defined in the [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
 module. This module details how alignment, justification, gaps, and gutters work in all layout systems — not just flexbox. When a feature is defined in both specifications, note that the box alignment module supersedes the flexible box layout module.

[Writing Modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#writing_modes)

--------------------------------------------------------------------------------------------------------------------------------------------------

In the [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 article, it is noted that flexbox is **writing mode aware**. Writing modes are fully detailed in the [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
 module, which details how CSS supports the different writing modes that exist internationally. We need to be aware of how this will impact our flex layouts as the writing mode changes the direction that blocks are laid out in our document. Understanding **block** and **inline** directions is key to new layout methods.

It is worth noting that we might want to change the writing mode of our document for reasons other than publishing content in a language that uses a different writing mode. The CSS writing modes module defines how text can be written horizontally, left-to-right and right-to-left, and vertically, top-to-bottom. This is important for internationalization and translations, but these feature can also be used for creative designs.

### [The writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#the_writing_modes)

The writing modes specification defines the following values of the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property, which serve to change the direction that blocks are laid out on the page, to match the direction that blocks lay out when content is formatted in that particular writing mode. You can change the live example below to these modes in order to see what happens to the flex layout.

*   `horizontal-tb`
*   `vertical-rl`
*   `vertical-lr`
*   `sideways-rl`
*   `sideways-lr`

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
    </div>
    

css

    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
    }
    
    .box {
      width: 500px;
      border: 2px dotted rgb(96 139 168);
      display: flex;
      writing-mode: horizontal-tb;
    }
    

Note that you would not normally use CSS and the `writing-mode` property to change an entire document to another writing mode. This would be done via HTML, by adding a [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 and [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute to the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element to indicate the document language and default text direction. This would mean that the document would display correctly even if CSS did not load.

[Flexbox and other layout methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#flexbox_and_other_layout_methods)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some properties were designed assuming that content is laid out using the standard block layout system, and don't apply in the context of flex layout. An element set to `display: flex` behaves in most ways like any other block-level container that establishes a containing block. It establishes a new [flex formatting context](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Container)
, so floats will not intrude and the containers' margins will not collapse.

With regard to flex items, if an item was floated or cleared and then becomes a flex item due to the parent having `display: flex` applied, the floating and clearing will no longer happen, and the item will not be taken out of normal flow in the way that floats are. If you have used the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 property, as used with `inline-block` or table layout for alignment, this will no longer affect the item and you can use the alignment properties of flexbox instead.

In this next live example the child elements have been floated, and then their container has had `display: flex` added. If you remove `display: flex`, you should see that the `.box` element collapses as we have no clearing applied. This demonstrates that the float is happening. Re-apply `display: flex` and the collapsing does not happen. This is because the items no longer have a float applied, as they have been transformed into flex items.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
    </div>
    

css

    .box {
      width: 500px;
      border: 2px dotted rgb(96 139 168);
      display: flex;
    }
    
    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      float: left;
    }
    

[Flexbox and grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#flexbox_and_grid_layout)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 and flexbox share many properties and values. For divergent properties, if a flex item becomes a grid item, any `flex` values assigned to the child elements, such as `flex-end`, will be ignored. As noted above, values defined in the box alignment module that work across both layout methods supersede those defined in flexbox only.

### [Flex and grid — what's the difference?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#flex_and_grid_%E2%80%94_whats_the_difference)

A common question is to ask what the difference is between flexbox and CSS grid layout — why do we have two specifications that sometimes appear to be doing the same thing?

The most straightforward answer to this question is defined in the specifications themselves. Flexbox is a one-dimensional layout method whereas grid layout is a two-dimensional layout method. The example below has a flex layout. As already described in the [Basic concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 article, flex items can be allowed to wrap but, once they do, each line behaves as if it were a flex container of its own. When space is distributed, flexbox does not look at the placement of items in other rows and tries to line things up with each other.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
    </div>
    

css

    .box {
      border: 2px dotted rgb(96 139 168);
      display: flex;
      flex-wrap: wrap;
      padding: 1em;
    }
    
    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      padding: 1em;
      flex: 1 1 200px;
    }
    

If we create a very similar layout using grid, we can control the layout in both rows and columns.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div>Three</div>
      <div>Four</div>
      <div>Five</div>
      <div>Six</div>
      <div>Seven</div>
    </div>
    

css

    .box {
      border: 2px dotted rgb(96 139 168);
      padding: 1em;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, auto));
    }
    
    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      padding: 1em;
      background-color: rgb(96 139 168 / 0.2);
    }
    

These examples point to another key difference between these layout methods. In grid layout, you do the majority of sizing specification on the container, setting up tracks and then placing items into them. In flexbox, while you create a flex container and set the direction at that level, any control over item sizing needs to happen on the items themselves.

In some cases, you could use either layout method. As you become confident with both, you will find each one is better suited to specific layout needs, and you'll end up with both methods in your CSS. There is rarely a right or wrong answer.

As a general rule, if you are setting widths on flex items to make items in one row of a wrapped flex container line up with the items above them, you should instead opt for a two-dimensional grid layout.

There are no set rules like "you should use flexbox for small components and grid layout for larger ones." A tiny component can be two dimensional, and a large layout can be represented better with layout in one dimension. Try things out — you have a choice of layout methods, so take advantage of it.

For more comparisons of grid and flexbox see the article [Relationship of grid layout to other layout methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Relationship_with_other_layout_methods)
. This article details many of the ways that grid layout differs from flex layout and demonstrates some of the extra functionality you get when using grid layout such as layering of items on the grid. This may also help you decide which layout method to use.

[Flexbox and display: contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods#flexbox_and_display_contents)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `contents` value of the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property is described in the spec as follows:

> "The element itself does not generate any boxes, but its children and pseudo-elements still generate boxes as normal. For the purposes of box generation and layout, the element must be treated as if it had been replaced with its children and pseudo-elements in the document tree."

This value of `display` controls box generation, and whether the element should generate a box that we can style and see on the page, or whether instead the box it would normally create should be removed and the child elements essentially moved up to participate in whatever layout method the parent would have been part of. This is easier to see with an example.

In the following live example, we have a flex container containing three flex items. One has two elements nested inside it, which would not ordinarily participate in flex layout. Flex layout only applies to the direct children of a flex container.

By adding `display: contents` to the wrapper around the nested elements, you can see that the item has disappeared from the layout, allowing the two sub-children to be laid out as if they were direct children of the flex container. You can try removing the `display: contents` line to see it return.

Note that this only removes the box from the layout; the sub-children don't become direct children in any other way. We used a direct child selector to add the background and borders to the flex items; it has not been applied to our nested children. They have been laid out as flex items, but as they are not direct children they do not get the other styling.

As the box is removed, you cannot then use it to — for example — add a background color behind the nested sub children. If you remove `display: contents` in this live example you will see that the direct child we are removing has an orange background color. This also disappears when the box disappears.

html

    <div class="box">
      <div>One</div>
      <div>Two</div>
      <div class="nested">
        <div>Sub-item 1</div>
        <div>Sub-item 2</div>
      </div>
    </div>
    

css

    .box > * {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      padding: 1em;
      background-color: rgb(96 139 168 / 0.2);
    }
    
    .box {
      border: 2px dotted rgb(96 139 168);
      padding: 1em;
      display: flex;
    }
    
    .nested {
      background-color: orange;
      display: contents;
    }
    

**Warning:** Some browsers incorrectly remove some elements with `display: contents` from the accessibility tree (but descendants will remain), removing those elements' semantics while maintaining their child content. This means the element itself may not be announced by screen readers. See [`display: contents`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#display_contents)
 and [`display: contents` considered harmful](https://ericwbailey.website/published/display-contents-considered-harmful/ "External link (opens in new tab)")
.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Relationship_with_other_layout_methods/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/flexible_box_layout/relationship_with_other_layout_methods/index.md?plain=1 "Folder: en-us/web/css/guides/flexible_box_layout/relationship_with_other_layout_methods (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFlexible_box_layout%2FRelationship_with_other_layout_methods&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fflexible_box_layout%2Frelationship_with_other_layout_methods%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFlexible_box_layout%2FRelationship_with_other_layout_methods%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fflexible_box_layout%2Frelationship_with_other_layout_methods%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cc5111618cee56a288f3c4354acd2330f893434%0A*+Document+last+modified%3A+2026-11-05T12%3A43%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
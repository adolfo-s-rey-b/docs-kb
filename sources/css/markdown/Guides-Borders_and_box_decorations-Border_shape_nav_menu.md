*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#mdn-search)
    

Creating an irregular nav menu with border-shape
================================================

The CSS [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
 property can be applied to elements to create precisely-shaped containers such as speech bubbles, abstract tooltip designs, and more, enabling many new creative ideas to be put into production without the need for workarounds or hacks. You can learn all about the property and see basic examples in action on the property reference page.

In this guide, we show you how to use `border-shape` to create an irregular animated navigation menu with each nav item shaped like a jigsaw piece.

[Defining the nav menu markup](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#defining_the_nav_menu_markup)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Our HTML is fairly typical for a navigation menu — a list of links.

[Setting the basic page styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#setting_the_basic_page_styles)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The basic page setup styles are as follows. We apply some rudimentary font styles, use [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 to cause the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 to fill the viewport, and use [flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
 to place the nav menu in the center of the screen.

[Applying the general nav styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#applying_the_general_nav_styles)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we style the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 by removing the default [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
 and [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 and setting a [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of `flex` to lay out the contained [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements in a row. We then set a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 value of `0` and apply a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
, so that when the `<ul>` state changes, a change in the `gap` value animates smoothly.

Next, we style the `<li>` elements. We want each nav item to be square, so we set an equal [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
.

Next, we style the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements inside the list items. We start by removing the default [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 and setting the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 to `black`. We then set a `width` and `height` of `100%` to make the `<a>` elements fill the full area of the `<li>` elements, then use [flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
 to center their text horizontally and vertically.

We then set [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 and [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
 properties on the links, plus a `transition` so that any property value changes are animated smoothly when the element's state changes.

We then give each jigsaw piece a different color:

[Handling the border shape](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#handling_the_border_shape)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Now it's time to set the `border-shape` for each nav item to get the jigsaw piece look we are after. For variety, we've shaped each odd-numbered `<a>` element like a downwards-pointing jigsaw-piece, and each even-numbered `<a>` element like an upwards-pointing jigsaw-piece:

This immediately creates an issue — the notches on the jigsaw pieces that extend out from the original `<a>` area aren't filled by the `<a>` elements' background colors.

There is a solution to this problem. We've deliberately included the `content-box` `<geometry-box>` value after each `shape()` function in the previous two rules. This means the shapes will be drawn relative to the elements' content boxes, and any applied `padding` won't be set inside the shape. Instead, the padding will be placed outside the shape, causing it to get smaller and forcing the background color to fill up the notches.

The required `padding` is set like so:

**Note:** You can see what the background problem looks like by inspecting the [live example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#result)
 in your browser's developer tools and disabling the `padding` applied to the `<a>` elements.

The `padding` causes the jigsaw pieces to get smaller, so there are gaps between them. We want them to touch initially, so we set a large negative [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
 value on each list item to bring them together:

A side-effect of this `margin-right` setting is that all of the `<li>` items are moved to the right, so the nav menu is no longer horizontally centered. To fix this, we use [relative positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#relative_positioning)
 to move the `<ul>` back to the left:

Finally, we apply some style updates on `:hover` and `:focus` that, when combined with the `transition` properties we set earlier, produce some animated effects on interaction with the nav items. We increase the `gap` set on the `<ul>` flexbox layout when it is hovered over or focused. To handle the focus state, we use the [`:has`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
 pseudo-class to select the entire `<ul>` when any `<a>` inside it is focused.

We then set an increased `brightness` [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
, [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
 factor, and outer `box-shadow` on the `<a>` elements themselves when they are hovered over or focused, making them appear brighter and raised up on interaction.

[Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#result)

---------------------------------------------------------------------------------------------------------------------------

Hover over or focus the nav items to see the animated effects. Note how naturally the different applied effects work with the `border-shape` values.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [border-shape: the future of the non-rectangular web](https://una.im/border-shape "External link (opens in new tab)")
     by Una Kravets (2026)
*   [Get Ready For the Powerful CSS border-shape Property!](https://css-tricks.com/get-ready-for-the-powerful-css-border-shape-property/ "External link (opens in new tab)")
     on CSS Tricks (2026)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations/Border_shape_nav_menu/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/borders_and_box_decorations/border_shape_nav_menu/index.md?plain=1 "Folder: en-us/web/css/guides/borders_and_box_decorations/border_shape_nav_menu (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBorders_and_box_decorations%2FBorder_shape_nav_menu&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fborders_and_box_decorations%2Fborder_shape_nav_menu%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBorders_and_box_decorations%2FBorder_shape_nav_menu%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fborders_and_box_decorations%2Fborder_shape_nav_menu%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc655f38c10ba17b853b0e66b43cf4cf2b176e424%0A*+Document+last+modified%3A+2026-08-04T23%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
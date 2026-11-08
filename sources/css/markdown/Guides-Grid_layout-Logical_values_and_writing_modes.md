*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#mdn-search)
    

Grids, logical values, and writing modes
========================================

One of the most important features of CSS grid layout is the support for different writing modes built into the specification. In this guide, we look at this feature of CSS grid layout and other modern layout methods, learning a little about writing modes and logical vs. physical properties as we do so.

[Logical and physical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#logical_and_physical_properties_and_values)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS is full of **physical** positioning properties and keywords – `left` and `right`, `top` and `bottom`. In the code snippet below, we position an item using absolute positioning and use the physical [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 as offset values to push the item around. The item is placed 20 pixels from the top and 30 pixels from the left of the container:

This example uses the [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 and [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
 properties; these are just two of the many **[physical properties](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
** in CSS. We can also add margins, padding, and borders using physical properties, for example [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 and [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
. You might also see physical keywords in use, such as when using `text-align: right` to align text to the right.

We call these keywords and properties _physical_ because they relate to the screen you are looking at. Left is always left, no matter what direction your text is running.

### [Issues with physical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#issues_with_physical_properties)

Physical properties can cause issues when developing a site that has to work in multiple languages, including languages where the text flows from right to left, or top to bottom. Browsers are designed to correctly display content regardless of the language. Some CSS features can override browser defaults and cause content to display less than optimally.

In this example, the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property has been set to [rtl](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
, which switches the writing mode from the default for an English language document of `ltr`. We have two paragraphs. These should both flow from right to left because of the `direction` value set on an ancestor element (`<body>`). The first paragraph has [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 set to `left`, so it aligns with the left of its container. The second paragraph aligns with the right and flows from right to left.

This is a basic demonstration of the problems that can arise when using physical values and properties in CSS. If we write CSS using physical properties and keywords, we tell the browser our assumption as to how the text will flow and prevent it from handling alternative writing modes.

### [Logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#logical_properties_and_values)

**[Logical properties](https://developer.mozilla.org/en-US/docs/Glossary/Logical_properties)
 and values** do not assume a text direction. This is why we use the keyword `start` in CSS grid layout to align something with the start of a container. When working with English content, `start` will be on the left, however, it doesn't have to be. The word `start` infers no physical location, which enables websites to start the content on the right when right-to-left languages, such as Arabic, are used.

[Block and Inline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#block_and_inline)

------------------------------------------------------------------------------------------------------------------------------------------

When using logical rather than physical properties, we don't see the world as left to right, and top to bottom. We have a different reference point. This is where understanding the _block_ and _inline_ axes, introduced in the [grid alignment guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Box_alignment)
, becomes very useful. If you think about layout in terms of block and inline, the way things work in CSS grid layout makes a lot of sense.

![An image showing the default direction of the block and inline axes.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes/8-horizontal-tb.png)

[CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#css_writing_modes)

--------------------------------------------------------------------------------------------------------------------------------------------

The [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
 module specifies how writing modes work in CSS. These features are not just for supporting languages with a different writing mode to English; they can also be used for creative purposes. The examples in this section make use of the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property to make changes to the writing mode applied to our grid, demonstrating how logical values work in the process.

### [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#writing-mode)

Writing modes are more than just left to right and right to left text, and the `writing-mode` property helps us display text running in other directions. The [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property can have values of:

*   `horizontal-tb`
*   `vertical-rl`
*   `vertical-lr`
*   `sideways-rl`
*   `sideways-lr`

The value `horizontal-tb`, which stands for "horizontal, top to bottom", is the default for text on the web. It is the direction in which you are reading this guide. The other values change how text flows in our document, matching the different writing modes found worldwide.

As an example, we have two paragraphs below. The first uses the default `horizontal-tb` value, and the second uses `vertical-rl`. In the second writing mode, text still runs left to right, however the direction of the text is vertical — inline text now runs down the page, from top to bottom.

[Writing modes in grid layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#writing_modes_in_grid_layouts)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Applying this to a grid layout example, we can see how changing the writing mode means changing our idea of where the block and inline axes are.

### [Default writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#default_writing_mode)

In this example, the grid has three columns and two row tracks. This means there are three tracks running down the block axis. In default writing mode, grid auto-places items starting at the top left, moving along to the right, filling up the three cells on the inline axis. It then moves to the next line, creating a new row track, and fills in more items:

### [Setting writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#setting_writing_mode)

If we add `writing-mode: vertical-lr` to the grid container in the previous example, we can see that the block and inline axes now run in a different direction. The block or _column_ axis now runs across the page from left to right, while the inline axis runs down the page, creating rows from top to bottom.

[Logical values for alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#logical_values_for_alignment)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

With the block and inline axis able to change direction, the logical values for the alignment properties start to make more sense.

In this example, we use alignment (the [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 and [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties) to align items inside a grid that is set to `writing-mode: vertical-lr`. The `start` and `end` properties work in exactly the same way that they do in the default writing mode, and remain logical in a way that using left and right, top and bottom to align items would not do. This occurs once we've flipped the grid onto the side, like this:

If you want to see how these work, with a right to left as well as top to bottom writing mode, switch `vertical-lr` to `vertical-rl`, which is a vertical writing mode running from right to left.

[Auto-placement and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#auto-placement_and_writing_modes)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As we've seen in the previous examples, writing mode can change the visual direction in which items place themselves onto the grid. Items will, by default, place themselves along the inline axis, adding new rows in the block direction. We've now seen that the inline axis does not always run from left to right, and the block axis does not always run from top to bottom.

[Line-based placement and Writing Modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#line-based_placement_and_writing_modes)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The key thing to remember when placing items by line number, is that line 1 is the start line and line -1 is the end line, no matter which writing mode you are in.

### [Line-based placement with left to right text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#line-based_placement_with_left_to_right_text)

In this example, we have a grid laid out in the default `ltr` direction, with three items positioned using line-based placement.

*   Item 1 starts at column line 1, spanning one track.
*   Item 2 starts at column line -1, spanning to -3.
*   Item 3 starts at column line 1, spanning to column line 3.

### [Line-based placement with right to left text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#line-based_placement_with_right_to_left_text)

If we add the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property with a value of `rtl` to the grid container in the previous example, line 1 is placed on the right-hand side of the grid, and line -1 on the left.

If you are switching the direction of your text, either for entire pages or for parts of pages, and are using lines, you may want to [name your lines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Named_grid_lines)
 to avoid the layout completely switching direction. For some things, for example, where a grid contains text content, this switching may be exactly what you want. For other uses it may not.

### [The strange order of values in the `grid-area` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#the_strange_order_of_values_in_the_grid-area_property)

You can use the [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
 property to specify all four lines of a grid area as one value. When people first encounter this, they are often surprised that the values do not follow the same order as the shorthand for [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 – which runs clockwise: top, right, bottom, left.

The order of `grid-area` values is:

*   `grid-row-start`
*   `grid-column-start`
*   `grid-row-end`
*   `grid-column-end`

Which for English, in left-to-right means the order is:

*   `top`
*   `left`
*   `bottom`
*   `right`

This is counter-clockwise! It's the reverse of what we do for margins and padding. If we remember that `grid-area` sees the world as "block and inline", you'll notice we are setting the two starts, then the two ends, which is much more logical once you know!

[Mixed writing modes and grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#mixed_writing_modes_and_grid_layout)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to displaying documents using the correct writing mode for the language, writing modes can be used creatively within documents that are otherwise `ltr`. In this example, we have a grid layout with a set of links down one side. We use writing modes (`writing-mode: vertical-lr`) to turn these on their side in the column track:

[Physical values and logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes#physical_values_and_logical_properties)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you combine logical grid properties with physical properties, remember that physical properties will not change according to writing mode. In our [Aligning items in CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Box_alignment)
 guide, we use auto margins to push one item away from the others; this employs physical properties. There are logical property equivalents for most physical properties, which respect writing modes in the same way as grid placement and alignment properties and values.

Similarly, when using absolute positioning within a grid area, you can use logical [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 to place items inside the grid area. When mixing logical and physical properties or values, be aware of the tension between them. For example, you may need to change your CSS to cope with a switch from `ltr` to `rtl`. Your understanding of block and inline through grid will help you to understand [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Logical_values_and_writing_modes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/grid_layout/logical_values_and_writing_modes/index.md?plain=1 "Folder: en-us/web/css/guides/grid_layout/logical_values_and_writing_modes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FLogical_values_and_writing_modes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Flogical_values_and_writing_modes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FGrid_layout%2FLogical_values_and_writing_modes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fgrid_layout%2Flogical_values_and_writing_modes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#mdn-search)
    

Block and inline layout in normal flow
======================================

In this guide, we will explore the basics of how Block and Inline elements behave when they are part of the normal flow.

Normal Flow is defined in the [CSS 2.1 specification](https://www.w3.org/TR/CSS2/visuren.html#normal-flow "External link (opens in new tab)")
, which explains that any boxes in normal flow will be part of a _formatting context_. They can be either block or inline, but not both at once. We describe block-level boxes as participating in a _block formatting context_, and inline-level boxes as participating in an _inline formatting context_.

The behavior of elements which have a block or inline formatting context is also defined in this specification. For elements with a block formatting context, the spec says:

> "In a block formatting context, boxes are laid out one after the other, vertically, beginning at the top of a containing block. The vertical distance between two sibling boxes is determined by the 'margin' properties. Vertical margins between adjacent block-level boxes in a block formatting context collapse.  
> In a block formatting context, each box's left outer edge touches the left edge of the containing block (for right-to-left formatting, right edges touch)." - 9.4.1

For elements with an inline formatting context:

> "In an inline formatting context, boxes are laid out horizontally, one after the other, beginning at the top of a containing block. Horizontal margins, borders, and padding are respected between these boxes. The boxes may be aligned vertically in different ways: their bottoms or tops may be aligned, or the baselines of text within them may be aligned. The rectangular area that contains the boxes that form a line is called a line box." - 9.4.2

Note that the CSS 2.1 specification describes documents as being in a horizontal, top-to-bottom writing mode. For example, by describing the vertical distance between block boxes. The behavior on block and inline elements is the same when working in a vertical writing mode; we explore this in our [Flow layout and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_writing_modes)
 guide.

[Elements participating in a block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#elements_participating_in_a_block_formatting_context)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Block elements in a horizontal writing mode such as English, lay out vertically, one below the other.

![Inline direction is horizontal. Block direction is vertical.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout/mdn-horizontal.png)

In a vertical writing mode they would lay out horizontally.

![Inline direction is vertical. Block direction is horizontal.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout/mdn-vertical.png)

In this guide, we will be working in English and therefore a horizontal writing mode. However, everything described should work in the same way if your document is in a vertical writing mode.

As defined in the specification, the margins between two block boxes are what creates separation between the elements. We can see this with the layout of two paragraphs, to which I have added a border. The default browser stylesheet adds spacing between the paragraphs by way of adding a margin to the top and bottom.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery.
      </p>
      <p>
        Before that night—a memorable night, as it was to prove—hundreds of millions
        of people had watched the rising smoke-wreaths of their fires without
        drawing any special inspiration from the fact.
      </p>
    </div>
    

css

    p {
      border: 2px solid green;
    }
    

If we set margins on the paragraph element to `0` then the borders will touch.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery.
      </p>
      <p>
        Before that night—a memorable night, as it was to prove—hundreds of millions
        of people had watched the rising smoke-wreaths of their fires without
        drawing any special inspiration from the fact.
      </p>
    </div>
    

css

    p {
      border: 2px solid green;
      margin: 0;
    }
    

By default block elements will consume all of the space in the inline direction, so our paragraphs spread out and get as big as they can inside their containing block. If we give them a width, they will continue to lay out one below the other - even if there would be space for them to be side by side. Each will start against the start edge of the containing block, so the place at which sentences would begin in that writing mode.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery.
      </p>
      <p>
        Before that night—a memorable night, as it was to prove—hundreds of millions
        of people had watched the rising smoke-wreaths of their fires without
        drawing any special inspiration from the fact.
      </p>
    </div>
    

css

    p {
      border: 2px solid green;
      width: 40%;
    }
    

### [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#margin_collapsing)

The spec explains that margins between block elements _collapse_. This means that if you have an element with a top margin immediately after an element with a bottom margin, rather than the total space being the sum of these two margins, the margin collapses, and so will essentially become as large as the larger of the two margins.

In the example below, the paragraphs have a top margin of `20px` and a bottom margin of `40px`. The size of the margin between the paragraphs is `40px` as the smaller top margin on the second paragraph has collapsed with the larger bottom margin of the first.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery.
      </p>
      <p>
        Before that night—a memorable night, as it was to prove—hundreds of millions
        of people had watched the rising smoke-wreaths of their fires without
        drawing any special inspiration from the fact.
      </p>
    </div>
    

css

    p {
      border: 2px solid green;
      margin: 20px 0 40px 0;
    }
    

You can read more about margin collapsing in our article [Mastering Margin Collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
.

**Note:** If you are not sure whether margins are collapsing, check the Box Model values in your browser DevTools. This will give you the actual size of the margin which can help you to identify what is happening.

![Screen shot box model panel in browser dev tools which shows the four values for margin, border, and padding along with height and width in a graphic at top and lists box-sizing, display, float, line-height, position, and z-index below the graphic.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout/box-model.png)

[Elements participating in an inline formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#elements_participating_in_an_inline_formatting_context)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Inline elements display one after the other in the direction that sentences run in that particular writing mode. While we don't tend to think of inline elements as having a box, as with everything in CSS they do. These inline boxes are arranged one after the other. If there is not enough space in the containing block for all of the boxes a box can break onto a new line. The lines created are known as line boxes.

In the following example, we have three inline boxes created by a paragraph with a [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 element inside it.

html

    <p>
      Before that night—<strong>a memorable night</strong>, as it was to
      prove—hundreds of millions of people had watched the rising smoke-wreaths of
      their fires without drawing any special inspiration from the fact.
    </p>
    

The boxes around the words before the `<strong>` element and after the `</strong>` element are referred to as anonymous boxes, boxes introduced to ensure that everything is wrapped in a box, but ones that we cannot target directly.

The line box size in the block direction (so the height when working in English) is defined by the tallest box inside it. In the next example, the `<strong>` element is 300%; since that content spans two lines, it now defines the height of the line boxes of those two lines.

html

    <p>
      Before that night—<strong>a memorable night</strong>, as it was to
      prove—hundreds of millions of people had watched the rising smoke-wreaths of
      their fires without drawing any special inspiration from the fact.
    </p>
    

css

    strong {
      font-size: 300%;
    }
    

Find out more about how block and inline boxes behave in our guide to the [visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
.

[The display property and flow layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#the_display_property_and_flow_layout)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to the rules existing in CSS2.1, new levels of CSS further describe the behavior of block and inline boxes. The [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property defines how a box and any boxes inside it behave. In the CSS Display Model Level 3, we can learn more about how the `display` property changes the behavior of boxes and the boxes they generate.

The display type of an element defines the outer display type; this dictates how the box displays alongside other elements in the same formatting context. It also defines the inner display type, which dictates how boxes inside this element behave. We can see this very clearly when considering a flex layout. In the example below I have a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
, which I have given `display: flex`. The flex container behaves like a block element: it displays on a new line and takes up all of the space it can in the inline direction. This is the outer display type of `block`.

The flex items however are participating in a flex formatting context, because their parent is the element with `display: flex`, which has an inner display type of `flex`, establishing the flex formatting context for the direct children.

html

    <div class="container">
      <div>Flex Item</div>
      <div>Flex Item</div>
      <div>
        <div>Children</div>
        <div>are in</div>
        <div>normal flow</div>
      </div>
    </div>
    

css

    .container {
      display: flex;
    }
    
    .container > * {
      border: 1px solid green;
    }
    

Therefore you can think of every box in CSS working in this way. The box itself has an outer display type, so it knows how to behave alongside other boxes. It then has an inner display type which changes the way its children behave. Those children then have an outer and inner display type too. The flex items in the previous example become flex level boxes, so their outer display type is dictated by way of them being part of the flex formatting context. They have an inner display type of _flow_ however, meaning that their children participate in normal flow. Items nested inside our flex item lay themselves out as block and inline elements unless something changes their display type.

This concept of the outer and inner display type is important as this tells us that a container using a layout method such as flexbox (`display: flex`) and grid layout (`display: grid`) is still participating in block and inline layout, due to the outer display type of those methods being `block`.

### [Changing the Formatting Context an element participates in](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#changing_the_formatting_context_an_element_participates_in)

Browsers display items in block or inline formatting contexts based on what normally makes sense for that element. For example, a [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 element is used to strongly emphasize a span of content and is displayed in bold in browsers by default. It would not generally make sense for that `<strong>` element to be displayed as a block-level element, breaking onto a new line. If you did want all `<strong>` elements to display as block boxes, you could do so by setting `strong { display: block; }`. The ability to style content with CSS means you can always use the most appropriate semantic HTML elements to mark up your content and then change how they are displayed with CSS.

html

    <p>
      Before that night—<strong>a memorable night</strong>, as it was to
      prove—hundreds of millions of people had watched the rising smoke-wreaths of
      their fires without drawing any special inspiration from the fact.
    </p>
    

css

    strong {
      display: block;
    }
    

[Summary](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#summary)

-----------------------------------------------------------------------------------------------------------

In this guide, we have looked at how elements display in normal flow, as block and inline elements. An HTML document with no CSS styling at all will display in a readable way due to this default behavior. Understanding how normal flow works is an important starting point for understanding CSS layout as a whole.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout#see_also)

-------------------------------------------------------------------------------------------------------------

*   [CSS Basic Box Model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
    
*   [Learn: Normal Flow](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction#normal_layout_flow)
    
*   [Inline-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)
    
*   [Block-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/block_and_inline_layout/index.md?plain=1 "Folder: en-us/web/css/guides/display/block_and_inline_layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FBlock_and_inline_layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fblock_and_inline_layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FBlock_and_inline_layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fblock_and_inline_layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2c6196c0352ac439f13adc6a0a83d79993ef5a1e%0A*+Document+last+modified%3A+2026-08-24T01%3A37%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
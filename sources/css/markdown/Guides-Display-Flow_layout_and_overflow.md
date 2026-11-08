*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#mdn-search)
    

Flow layout and overflow
========================

When there is more content than can fit into a container, an overflow situation occurs. Understanding how overflow behaves is important in dealing with any element with a constrained size in CSS. This guide explains how overflow works when working with normal flow. The HTML is the same in each example, so it's visible in the first section, and hidden in others for brevity.

[What is overflow?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#what_is_overflow)

-------------------------------------------------------------------------------------------------------------------------------

Giving an element a fixed height and width, then adding significant content to the box, creates a basic overflow example:

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    </div>
    <p>
      Their names were Stephen and Joseph Montgolfier. They were papermakers by
      trade, and were noted as possessing thoughtful minds and a deep interest in
      all scientific knowledge and new discovery.
    </p>
    <p>
      Before that night—a memorable night, as it was to prove—hundreds of millions
      of people had watched the rising smoke-wreaths of their fires without drawing
      any special inspiration from the fact.
    </p>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .box {
      width: 300px;
      height: 100px;
      border: 5px solid rebeccapurple;
      padding: 10px;
    }
    

The content goes into the box. Once it fills the box, it continues to overflow in a visible way, displaying content outside the box, potentially displaying under subsequent content. The property that controls how overflow behaves is the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property which has an initial value of `visible`. This is why we can see the overflow content.

[Controlling overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#controlling_overflow)

--------------------------------------------------------------------------------------------------------------------------------------

There are other values that control how overflow content behaves. To hide overflowing content use a value of `hidden`. This may cause some of your content to not be visible.

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    </div>
    <p>
      Their names were Stephen and Joseph Montgolfier. They were papermakers by
      trade, and were noted as possessing thoughtful minds and a deep interest in
      all scientific knowledge and new discovery.
    </p>
    <p>
      Before that night—a memorable night, as it was to prove—hundreds of millions
      of people had watched the rising smoke-wreaths of their fires without drawing
      any special inspiration from the fact.
    </p>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      width: 300px;
      height: 100px;
      border: 5px solid rebeccapurple;
      padding: 10px;
      overflow: hidden;
    }
    

Using a value of `scroll` contains the content in its box and add scrollbars to enable viewing it. Scrollbars will be added even if the content fits in the box.

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    </div>
    <p>
      Their names were Stephen and Joseph Montgolfier; they were papermakers by
      trade and were noted as possessing thoughtful minds and a deep interest in all
      scientific knowledge and new discoveries.
    </p>
    <p>
      Before that night—a memorable night, as it was to prove—hundreds of millions
      of people had watched the rising smoke-wreaths of their fires without drawing
      any special inspiration from the fact.
    </p>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      width: 300px;
      height: 100px;
      border: 5px solid rebeccapurple;
      padding: 10px;
      overflow: scroll;
    }
    

Using a value of `auto` will display the content with no scrollbars if the content fits inside the box. If it doesn't fit then scrollbars will be added. Comparing the next example, you should see `overflow: scroll` example above has horizontal and vertical scrollbars even though it only needs vertical scrolling. The `auto` example below only adds the scrollbar in the direction we need to scroll.

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    </div>
    <p>
      Their names were Stephen and Joseph Montgolfier, they were papermakers by
      trade, and were noted as possessing thoughtful minds and a deep interest in
      all scientific knowledge and new discovery.
    </p>
    <p>
      Before that night—a memorable night, as it was to prove—hundreds of millions
      of people had watched the rising smoke-wreaths of their fires without drawing
      any special inspiration from the fact.
    </p>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      width: 300px;
      height: 100px;
      border: 5px solid rebeccapurple;
      padding: 10px;
      overflow: auto;
    }
    

As we have already learned, using any of these values, other than the default of `visible`, will create a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
.

`overflow: clip` acts like `overflow: hidden`, but it does not allow programmatic scrolling; the box becomes non-scrollable. It also does not create a block formatting context.

The overflow property is in reality a shorthand for the [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 and [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 properties. If you specify only one value for overflow, this value is used for both axes. However, you can specify both values in which case the first is used for `overflow-x` and therefore the horizontal direction, and the second for `overflow-y` and the vertical direction. In the below example, I have only specified `overflow-y: scroll` so we do not get the unwanted horizontal scrollbar.

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    </div>
    <p>
      Their names were Stephen and Joseph Montgolfier, they were papermakers by
      trade, and were noted as possessing thoughtful minds and a deep interest in
      all scientific knowledge and new discovery.
    </p>
    <p>
      Before that night—a memorable night, as it was to prove—hundreds of millions
      of people had watched the rising smoke-wreaths of their fires without drawing
      any special inspiration from the fact.
    </p>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      width: 300px;
      height: 100px;
      border: 5px solid rebeccapurple;
      padding: 10px;
      overflow-y: scroll;
    }
    

[Flow Relative Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#flow_relative_properties)

----------------------------------------------------------------------------------------------------------------------------------------------

In the guide to [Writing Modes and Flow Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_writing_modes)
, we looked at the `block-size` and `inline-size` properties, which make more sense when working with different writing modes than tying our layout to the physical dimensions of the screen. The [CSS overflow module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
 also includes flow relative properties for overflow - [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-block)
 and [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline)
. These correspond to `overflow-x` and `overflow-y` but the mapping depends on the writing mode of the document.

[Indicating Overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#indicating_overflow)

------------------------------------------------------------------------------------------------------------------------------------

In the CSS overflow module, there are some properties that can help improve the way content looks in an overflow situation.

### [Inline-Axis Overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#inline-axis_overflow)

The [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
 property deals with text overflowing in the inline direction. It takes one of two values `clip`, in which case content is clipped when it overflows, this is the initial value and therefore the default behavior. We also have `ellipsis` which renders an ellipsis, which may be replaced with a better character for the language or writing mode in use.

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    
      <p>
        Their names were Stephen and Joseph Montgolfier, they were papermakers by
        trade, and were noted as possessing thoughtful minds and a deep interest in
        all scientific knowledge and new discovery.
      </p>
      <p>
        Before that night—a memorable night, as it was to prove—hundreds of millions
        of people had watched the rising smoke-wreaths of their fires without
        drawing any special inspiration from the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      width: 300px;
      border: 5px solid rebeccapurple;
      padding: 10px;
    }
    
    .box p {
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }
    

### [Block-Axis Overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#block-axis_overflow)

The [Overflow Module Level 4](https://drafts.csswg.org/css-overflow-4/#propdef-block-ellipsis "External link (opens in new tab)")
 specification adds a `block-ellipsis` property ([previously called `block-overflow`](https://github.com/w3c/csswg-drafts/commit/20b15b4d66b0fdfa8406f1ce28604128f02ee7bb "External link (opens in new tab)")
). This property enables adding an ellipsis (or custom strings) when text overflows in the block dimension, although there is no browser support for this at the time of writing.

This is useful in the situation where you have a listing of articles, for example, and you display the listings in fixed height boxes which only take a limited amount of text. It may not be obvious to the reader that there is more content to click through to when clicking the box or the title. An ellipsis indicates clearly the fact there is more content. The specification would allow a string of content or a regular ellipsis to be inserted.

[Summary](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#summary)

------------------------------------------------------------------------------------------------------------

Whether you are in continuous media on the web or in a Paged Media format such as print or EPUB, understanding how content overflows is useful when dealing with any layout method. Understanding how overflow works in normal flow enables a greater understanding of the implications of overflow content in layout methods such as grid and flexbox.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)
     guide
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 15, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/flow_layout_and_overflow/index.md?plain=1 "Folder: en-us/web/css/guides/display/flow_layout_and_overflow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FFlow_layout_and_overflow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fflow_layout_and_overflow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FFlow_layout_and_overflow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fflow_layout_and_overflow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32bdfdb82cf91ce9942b694286dec62be2cc20aa%0A*+Document+last+modified%3A+2025-12-15T12%3A04%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
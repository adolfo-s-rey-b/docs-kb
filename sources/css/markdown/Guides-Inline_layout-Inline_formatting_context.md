*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#mdn-search)
    

Inline formatting context
=========================

This guide explains the inline formatting context.

[Core concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#core_concepts)

-------------------------------------------------------------------------------------------------------------------------------

The inline formatting context is part of the visual rendering of a web page. Inline boxes are laid out one after the other, in the direction sentences run in the writing mode in use:

*   In a horizontal writing mode, boxes are laid out horizontally, starting on the left.
*   In a vertical writing mode they would be laid out vertically starting at the top.

In the example below, the two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with the black borders are part of a [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
, while inside each box, the words participate in an inline formatting context. The words in the horizontal writing mode run horizontally, while words in the vertical writing mode run vertically.

Boxes forming a line are contained by a rectangular area called a line box. This box will be large enough to contain all of the inline boxes in that line; when there is no more room in the inline direction another line will be created. Therefore, a paragraph is a set of inline line boxes, stacked in the block direction.

When an inline box is split, margins, borders, and padding have no visual effect where the split occurs. In the next example there is a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element wrapping a set of words wrapping onto two lines. The border on the `<span>` breaks at the wrapping point.

html

    <div class="example">
      Before that night—
      <span
        >a memorable night, as it was to prove— hundreds of millions of people</span
      >
      had watched the rising smoke-wreaths of their fires without drawing any
      special inspiration from the fact.
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    .example {
      border: 5px solid black;
      margin: 20px;
    }
    
    span {
      border: 5px solid rebeccapurple;
    }
    

Margins, borders, and padding in the inline direction are respected. In the example below you can see how the margin, border, and padding on the inline `<span>` element are added.

html

    <div class="example horizontal">One <span>Two</span> Three</div>
    <div class="example vertical">Four <span>Five</span> Six</div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .example {
      border: 5px solid black;
      margin: 20px;
    }
    
    span {
      border: 5px solid rebeccapurple;
      padding-inline-start: 20px;
      padding-inline-end: 40px;
      margin-inline-start: 30px;
      margin-inline-end: 10px;
    }
    .horizontal {
      writing-mode: horizontal-tb;
    }
    
    .vertical {
      writing-mode: vertical-rl;
    }
    

**Note:** I am using the logical, flow-relative properties — [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
 rather than [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
 — so that they work in the inline dimension whether the text is horizontal or vertical. Read more about these properties in [Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
.

[Alignment in the block direction](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#alignment_in_the_block_direction)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Inline boxes may be aligned in the block direction in different ways, using the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 property, which will align on the block axis in vertical writing modes (therefore not vertically at all!). In the example below the large text is making the line box of the first sentence larger, therefore the `vertical-align` property can be used to align the inline boxes either side of it. I have used the value `top`, try changing it to `middle`, `bottom`, or `baseline`.

html

    <div class="example horizontal">
      Before that night—<span>a memorable night</span>, as it was to prove—hundreds
      of millions of people had watched the rising smoke-wreaths of their fires
      without drawing any special inspiration from the fact.
    </div>
    
    <div class="example vertical">
      Before that night—<span>a memorable night</span>, as it was to prove—hundreds
      of millions of people had watched the rising smoke-wreaths of their fires
      without drawing any special inspiration from the fact.
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    span {
      font-size: 200%;
      vertical-align: top;
    }
    
    .example {
      border: 5px solid black;
      margin: 20px;
      inline-size: 400px;
    }
    
    .horizontal {
      writing-mode: horizontal-tb;
    }
    
    .vertical {
      writing-mode: vertical-rl;
    }
    

[Alignment in the inline direction](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#alignment_in_the_inline_direction)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If there is additional space in the inline direction, the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 property can be used to align the inline boxes within their line box. Try changing the value of `text-align` below to `end`.

html

    <div class="example horizontal">One Two Three</div>
    <div class="example vertical">Four Five Six</div>
    

    body {
      font: 1.2em sans-serif;
    }
    
    .example {
      border: 5px solid black;
      margin: 20px;
    }
    
    .horizontal {
      writing-mode: horizontal-tb;
    }
    
    .vertical {
      writing-mode: vertical-rl;
    }
    

css

    .example {
      text-align: center;
      inline-size: 250px;
    }
    

[Effect of floats](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#effect_of_floats)

-------------------------------------------------------------------------------------------------------------------------------------

Line boxes usually have the same size in the inline direction, therefore the same width if working in a horizontal writing mode, or height if working in a vertical writing mode. If there is a [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 within the same block formatting context however, the float will cause the line boxes that wrap the float to become shorter.

html

    <div class="box">
      <div class="float">I am a floated box!</div>
      <p>I am content inside the container.</p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .box {
      background-color: rgb(224 206 247);
      border: 5px solid rebeccapurple;
    }
    
    .float {
      float: left;
      width: 250px;
      height: 150px;
      background-color: white;
      border: 1px solid black;
      padding: 10px;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    
*   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/inline_layout/inline_formatting_context/index.md?plain=1 "Folder: en-us/web/css/guides/inline_layout/inline_formatting_context (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FInline_layout%2FInline_formatting_context&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Finline_layout%2Finline_formatting_context%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FInline_layout%2FInline_formatting_context%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Finline_layout%2Finline_formatting_context%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
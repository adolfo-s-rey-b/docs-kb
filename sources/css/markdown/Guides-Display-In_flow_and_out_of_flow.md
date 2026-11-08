*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#mdn-search)
    

In flow and out of flow
=======================

The [previous guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout)
 explained block and inline layout in normal flow. All elements that are in flow will be laid out using this method.

[Example of elements in flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#example_of_elements_in_flow)

---------------------------------------------------------------------------------------------------------------------------------------------------

The following example contains a heading, a paragraph, a list, and a final paragraph that contains a `strong` element. The heading and paragraphs are block level, the `strong` element inline. The list, which is displayed using flexbox to arrange the items into a row, is also participating in block and inline layout - the container has an outside `display` type of `block`.

html

    <div class="box">
      <h1>A heading</h1>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
    
      <ul>
        <li>One</li>
        <li>Two</li>
        <li>Three</li>
      </ul>
      <p>
        Their names were <strong>Stephen and Joseph Montgolfier</strong>, they were
        papermakers by trade, and were noted as possessing thoughtful minds and a
        deep interest in all scientific knowledge and new discovery.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    .box > * {
      border: 1px solid green;
    }
    
    ul {
      display: flex;
      justify-content: space-around;
      list-style: none;
      margin: 0;
    }
    

All of the elements are considered "in flow"; they appear on the page in the order that they are in the source.

[Taking an item out of flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#taking_an_item_out_of_flow)

-------------------------------------------------------------------------------------------------------------------------------------------------

All elements are in-flow apart from:

*   floated items
*   items with `position: absolute` (including `position: fixed` which acts in the same way)
*   the root element (`html`)

Out-of-flow items create a new [Block Formatting Context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 (BFC), and therefore, everything inside them can be seen as a mini layout, separate from the rest of the page. The root element, therefore, is out of flow, as the container for everything in our document, and establishes the Block Formatting Context for the document.

### [Floated items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#floated_items)

In this example, there is a `div` and then two paragraphs. A background color has been added to the paragraphs, and the `div` is floated left. The `div` is now out of flow.

As a float it is first laid out according to where it would be in normal flow, then taken out of flow and moved to the left as far as possible.

html

    <div class="box">
      <div class="float">I am a floated box!</div>
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

    body {
      font: 1.2em sans-serif;
    }
    p {
      background-color: #cccccc;
    }
    
    .float {
      float: left;
      font-weight: bold;
      width: 200px;
      border: 2px dotted black;
      padding: 10px;
    }
    

You can see the background color of the following paragraph running underneath, it is only the line boxes of that paragraph that have been shortened to cause the effect of wrapping content around the float. The box of our paragraph is still displaying according to the rules of normal flow. This is why, to make space around a floated item, you must add a margin to the item, in order to push the line boxes away from it. You cannot apply anything to the following in-flow content to achieve that.

### [Absolute positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#absolute_positioning)

Giving an item `position: absolute` or `position: fixed` removes it from flow, and any space that it would have taken up is removed. In the next example I have three paragraph elements, the second element has `position: absolute`, with offset values of `top: 30px` and `right: 30px`. It has been removed from document flow.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
      <p class="abspos">
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
      font: 1.2em sans-serif;
    }
    .box {
      width: 70%;
    }
    p {
      border: 2px solid green;
    }
    
    .abspos {
      position: absolute;
      background-color: green;
      color: white;
      top: 30px;
      right: 30px;
      width: 400px;
    }
    

Using `position: fixed` also removes the item from flow, however the offsets are based on the viewport rather than the containing block.

When taking an item out of flow with positioning, you will need to manage the possibility of content overlapping. Out of flow essentially means that the other elements on your page no longer know that element exists so will not respond to it.

### [Relative positioning and flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#relative_positioning_and_flow)

If you give an item relative positioning with `position: relative`, it remains in flow. However, you are then able to use the offset values to push it around. The space that it would have been placed in normal flow is reserved however, as you can see in the example below.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney.
      </p>
      <p class="relative">
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
      font: 1.2em sans-serif;
    }
    .box {
      width: 70%;
    }
    p {
      border: 2px solid green;
    }
    
    .relative {
      position: relative;
      background-color: green;
      color: white;
      bottom: 50px;
      left: 50px;
      width: 400px;
    }
    

When you do anything to remove or shift an item from where it would be placed in normal flow, you can expect to need to do some managing of the content and the content around it to prevent overlaps. Whether that involves clearing floats, or ensuring that an element with `position: absolute` does not sit on top of some other content. For this reason methods which remove elements from being in-flow should be used with understanding of the effect that they have.

[Summary](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#summary)

-----------------------------------------------------------------------------------------------------------

In this guide, we have explained how to take an element out of flow to achieve some very specific types of positioning. In the next guide we will look at a related issue, that of creating a [Block Formatting Context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
, in [Introduction to formatting contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Formatting_contexts)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Learn: Positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/in_flow_and_out_of_flow/index.md?plain=1 "Folder: en-us/web/css/guides/display/in_flow_and_out_of_flow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FIn_flow_and_out_of_flow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fin_flow_and_out_of_flow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FIn_flow_and_out_of_flow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fin_flow_and_out_of_flow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
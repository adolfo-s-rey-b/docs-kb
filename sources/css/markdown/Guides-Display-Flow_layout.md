*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout#mdn-search)
    

CSS flow layout
===============

_Normal Flow_, or Flow Layout, is the way that block and inline elements are displayed on a page before any changes are made to their layout. The flow is essentially a set of things that are all working together and know about each other in your layout. Once something is taken _out of flow_ it works independently.

In normal flow, **[inline](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)
** elements display in the inline direction, that is in the direction words are displayed in a sentence according to the [Writing Mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
 of the document. **[block](https://developer.mozilla.org/en-US/docs/Glossary/Block/CSS)
** elements display one after the other, as paragraphs do in the Writing Mode of that document. In English therefore, inline elements display one after the other, starting on the left, and block elements start at the top and move down the page.

[Basic Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout#basic_example)

-----------------------------------------------------------------------------------------------------------

The following example demonstrates Block and Inline Level boxes. The two paragraph elements with a green border are Block Level, displaying one under the other.

The first sentence also includes a span element with a blue background. This is inline level and therefore displays in place in the sentence.

    <div class="box">
      <p>
        One <span>November</span> night in the year 1782, so the story runs, two
        brothers sat over their winter fire in the little French town of Annonay,
        watching the grey smoke-wreaths from the hearth curl up the wide chimney.
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
    

    body {
      font: 1.2em sans-serif;
    }
    
    p {
      border: 2px solid green;
    }
    span {
      background-color: lightblue;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout#see_also)

-------------------------------------------------------------------------------------------------

*   [Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout)
    
*   [In flow and out of flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/In_flow_and_out_of_flow)
    
*   [Formatting contexts explained](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Formatting_contexts)
    
*   [Flow layout and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_writing_modes)
    
*   [Flow layout and overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout_and_overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Flow_layout/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/display/flow_layout/index.md?plain=1 "Folder: en-us/web/css/guides/display/flow_layout (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FFlow_layout&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fflow_layout%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FDisplay%2FFlow_layout%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fdisplay%2Fflow_layout%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
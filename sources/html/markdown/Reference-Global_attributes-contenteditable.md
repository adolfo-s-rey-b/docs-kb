*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#mdn-search)
    

`contenteditable` HTML global attribute
=======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contenteditable`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an enumerated attribute indicating if the element should be editable by the user. If so, the browser modifies its widget to allow editing.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#try_it)

---------------------------------------------------------------------------------------------------------------

    <blockquote contenteditable="true">
      <p>Edit this content to add your own quote</p>
    </blockquote>
    
    <cite contenteditable="true">-- Write your own name here</cite>
    

    blockquote {
      background: #eeeeee;
      border-radius: 5px;
      margin: 16px 0;
    }
    
    blockquote p {
      padding: 15px;
    }
    
    cite {
      margin: 16px 32px;
      font-weight: bold;
    }
    
    blockquote p::before {
      content: "\201C";
    }
    
    blockquote p::after {
      content: "\201D";
    }
    
    [contenteditable="true"] {
      caret-color: red;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#value)

-------------------------------------------------------------------------------------------------------------

The attribute must take one of the following values:

*   `true` or an _empty string_, which indicates that the element is editable.
*   `false`, which indicates that the element is not editable.
*   `plaintext-only`, which indicates that the element's raw text is editable, but rich text formatting is disabled.

If the attribute is given without a value, like `<label contenteditable>Example Label</label>`, its value is treated as an empty string.

If this attribute is missing or its value is invalid, its value is _inherited_ from its parent element: so the element is editable if its parent is editable.

Note that although its allowed values include `true` and `false`, this attribute is an _[enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
_ one and not a _Boolean_ one.

You can set the color used to draw the text insertion [caret](https://developer.mozilla.org/en-US/docs/Glossary/Caret)
 with the CSS [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 property.

Elements that are made editable, and therefore interactive, by using the `contenteditable` attribute can be focused. They participate in sequential keyboard navigation. However, elements with the `contenteditable` attribute nested within other `contenteditable` elements are not added to the tabbing sequence by default. You can add the nested `contenteditable` elements to the keyboard navigation sequence by specifying the `tabindex` value ([`tabindex="0"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
).

If content is pasted into an element with `contenteditable="true"`, all formatting is retained. If content is pasted into an element with `contenteditable="plaintext-only"`, all formatting is removed.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#examples)

-------------------------------------------------------------------------------------------------------------------

### [Pasting content into contenteditable](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#pasting_content_into_contenteditable)

This example has two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements with `contenteditable`, the first with the value `true` and the second with the value `plaintext-only`. Copy the content below and paste it into each `div` to see their effects.

#### HTML

    <h2>Content to copy</h2>
    <p class="instructions">
      Copy all the text in the block below and paste it into each of the
      contenteditable blocks to compare the results.
    </p>
    <section class="copying">
      <div class="copy">
        <p>
          This is a paragraph containing <strong>Bold</strong>, <em>Italic</em>, and
          <span class="red">red</span> text, followed by an ordered list:
        </p>
        <ol>
          <li>Step one</li>
          <li>Step two</li>
          <li>Step three</li>
        </ol>
      </div>
    </section>
    

html

    <h2>Pasting areas</h2>
    <section class="pasting">
      <div class="wrapper">
        <h3>contenteditable="true"</h3>
        <div contenteditable="true"></div>
      </div>
      <div class="wrapper">
        <h3>contenteditable="plaintext-only"</h3>
        <div contenteditable="plaintext-only"></div>
      </div>
    </section>
    

    h2 {
      margin-bottom: 0;
    }
    .copying {
      font-family: "Georgia", serif;
      margin: 1rem;
      padding: 1rem;
      border: solid black 1px;
    }
    .red {
      color: red;
    }
    .pasting {
      display: flex;
      flex-direction: row;
      gap: 1rem;
      width: 100%;
      .wrapper {
        flex: 1 1;
        margin: 0;
        padding: 0;
      }
      h3 {
        font-family: monospace;
      }
      [contenteditable] {
        min-height: 3rem;
        border: solid 1px;
        padding: 0.5rem;
        background-color: whitesmoke;
      }
      [contenteditable="true"] {
        caret-color: blue;
      }
      [contenteditable="plaintext-only"] {
        caret-color: red;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-contenteditable](https://html.spec.whatwg.org/multipage/interaction.html#attr-contenteditable) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable#see_also)

-------------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   [`HTMLElement.contentEditable`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/contentEditable)
     and [`HTMLElement.isContentEditable`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/isContentEditable)
    
*   The CSS [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
     property
*   [HTMLElement `input` event](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/contenteditable/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/contenteditable (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontenteditable&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontenteditable%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fcontenteditable%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fcontenteditable%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
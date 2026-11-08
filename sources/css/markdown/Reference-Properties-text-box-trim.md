*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#mdn-search)
    

`text-box-trim` CSS property
============================

Baseline 2026

Newly available

Since August 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/265)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-box-trim`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies which of the over and under edges of text content to trim from a text element's block container.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#syntax)

-----------------------------------------------------------------------------------------------------

### [Value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#value)

The `text-box-trim` property value may be specified as one of the following keywords:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#none)

The default value. No space is trimmed from the text.

[`trim-both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#trim-both)

The start (over) and end (under) edges are both trimmed.

[`trim-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#trim-start)

The start (over) edge is trimmed.

[`trim-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#trim-end)

The end (under) edge is trimmed.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#description)

---------------------------------------------------------------------------------------------------------------

The `text-box-trim` property specifies which of the over and under edges of text content to trim from a text element's block container.

Vertical spacing differs between fonts, making consistent typesetting historically challenging on the web. The `text-box-trim` property — along with its counterpart property [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
, which specifies how much space to trim — makes consistent vertical spacing of text easier to achieve.

The height of text-only content is relative to the height of the font. In digital font files, the height contains all characters, including capital letters, ascenders, descenders, etc. Different fonts have different base line-heights, meaning that lines of text with the same `font-size` will produce line boxes of differing heights, affecting the appearance of spacing between lines.

The `text-box-trim` property allows you to trim the over and under edge of the text's block container, making it easier to control text spacing in the block direction.

The actual amount of space trimmed is specified using the [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 property. For example, you can choose to trim the over edge in line with a font's capital letters or lower-case letters, and the under edge flush with the font's baseline.

The `text-box-trim` property, along with the [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 property, can also be set by using the [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | Block containers and inline boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

text-box-trim =   
  none        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-both     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#examples)

---------------------------------------------------------------------------------------------------------

### [Basic `text-box-trim` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#basic_text-box-trim_usage)

In the following example we set `text-box-edge: cap alphabetic` on two paragraphs, which trims the over edge of the text elements' block containers to the top of the capital letters and the under edge flush with the text baseline.

We then set `text-box-trim` values of `trim-end` on the first one, and `trim-both` on the second one. This results in the first paragraph only having its under edge trimmed, whereas the second one has both the over _and_ under edge trimmed.

#### Result

The output is as follows. Note how we've included a top and bottom border on each paragraph, so that you can see how the space has been trimmed in each case.

### [Interactive `text-box-trim` and `text-box-edge` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#interactive_text-box-trim_and_text-box-edge_value_comparison)

In this example we provide a user interface that allows you to choose the `text-box-trim` and `text-box-edge` values applied to a paragraph of text.

#### HTML

In our HTML, we include three main items:

*   Three [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     elements allowing you to set which edges of the paragraph should be trimmed (the `text-box-trim` value) and how much space to trim from the block-start and block-end edges of the paragraph (the [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
     value).
*   A [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
     element containing text, which the `text-box-*` values are applied to. This paragraph has [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     set on it so you can edit the text.
*   An [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
     element that displays the `text-box-*` declarations applied to the paragraph. This is updated when a selection is made.

We also import a font from the Google Fonts service to apply to our demo's text.

We have hidden the exact HTML code for brevity.

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap"
      rel="stylesheet" />
    <section>
      <div>
        <label for="box-trim">Select edge(s) to trim:</label>
        <select id="box-trim">
          <option>none</option>
          <option>trim-start</option>
          <option>trim-end</option>
          <option selected>trim-both</option>
        </select>
      </div>
      <div>
        <label for="trim-over">Select trim over (start) value:</label>
        <select id="trim-over">
          <option>text</option>
          <option selected>cap</option>
          <option>ex</option>
        </select>
      </div>
    </section>
    <p class="display" contenteditable>Holly Golightly</p>
    <section>
      <div>
        <label for="trim-under">Select trim under (end) value:</label>
        <select id="trim-under">
          <option>text</option>
          <option selected>alphabetic</option>
        </select>
      </div>
    </section>
    <output></output>
    

#### CSS

In our CSS, we apply the imported font to the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element and lay out the UI using [flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
. We have hidden most of the CSS code for brevity, but below we show the rules styling the paragraph the `text-box-*` effects are applied to and the `<output>` that shows the `text-box-*` rules being applied:

    html {
      font-family: "Roboto", sans-serif;
      height: 100%;
    }
    
    body {
      height: inherit;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 30px;
    }
    
    section {
      display: flex;
      justify-content: space-between;
    }
    
    section:nth-of-type(2) {
      justify-content: flex-end;
      padding-bottom: 30px;
    }
    
    select {
      width: 6rem;
    }
    

css

    p {
      margin: 0;
      font-size: 6rem;
      font-weight: bold;
      border-top: 5px solid magenta;
      border-bottom: 5px solid magenta;
    }
    
    output {
      border: 2px solid gray;
      border-radius: 10px;
      padding: 10px;
      margin: 0;
      width: fit-content;
    }
    

Again, note how we've included a top and bottom border on the `.display` paragraph, so that you can see how the space being trimmed changes when different `text-box-*` values are selected.

#### JavaScript

In the JavaScript, we start by grabbing references to the three `<select>` elements and two `<p>` elements:

js

    const boxTrimSelect = document.getElementById("box-trim");
    const trimOverSelect = document.getElementById("trim-over");
    const trimUnderSelect = document.getElementById("trim-under");
    
    const displayElem = document.querySelector("p");
    const codeElem = document.querySelector("output");
    

Next, we define a function called `setEdgeTrim()`. This applies a [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
 value to the paragraph based on the values of the `<select>` elements, and also prints the applied declarations to the output (both the longhand and shorthand equivalents):

js

    function setEdgeTrim() {
      const textBoxTrimValue = boxTrimSelect.value;
      const textBoxEdgeValue = `${trimOverSelect.value} ${trimUnderSelect.value}`;
      displayElem.style.textBox = `${textBoxTrimValue} ${textBoxEdgeValue}`;
    
      codeElem.innerHTML = `
        <span><code>text-box-trim: ${textBoxTrimValue}</code></span>
        <br>
        <span><code>text-box-edge: ${textBoxEdgeValue}</code></span>
        <br><br>
        <span>Shorthand equivalent:</span>
        <br><br>
        <span><code>text-box: ${textBoxTrimValue} ${textBoxEdgeValue}</code></span>
      `;
    }
    

In the last part of the JavaScript we run the `setEdgeTrim()` function once to set an initial state for the UI. We then apply [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
 event listeners to all of the `<select>` elements (via [`addEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
) so that `setEdgeTrim()` is run whenever one of the `<select>` values changes to update the UI accordingly:

js

    setEdgeTrim();
    
    boxTrimSelect.addEventListener("change", setEdgeTrim);
    trimOverSelect.addEventListener("change", setEdgeTrim);
    trimUnderSelect.addEventListener("change", setEdgeTrim);
    

#### Result

The output is as follows:

`text-box-trim` is initially set to `trim-both`, meaning that the over _and_ under edges of the paragraph are trimmed. `text-box-edge` is initially set to `cap alphabetic`, meaning that the text is trimmed flush with the top of capital letters at the start edge, and flush with the baseline at the end edge.

Try changing the `<select>` values to see the effect they have on the display text.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# text-box-trim](https://drafts.csswg.org/css-inline-3/#text-box-trim) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#see_also)

---------------------------------------------------------------------------------------------------------

*   [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
    , [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    
*   [CSS inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
     module
*   [CSS text-box-trim](https://developer.chrome.com/blog/css-text-box-trim "External link (opens in new tab)")
     on developer.chrome.com (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-box-trim/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-box-trim (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box-trim&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box-trim%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box-trim%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box-trim%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
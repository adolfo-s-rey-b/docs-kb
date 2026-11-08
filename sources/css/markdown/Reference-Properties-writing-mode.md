*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#mdn-search)
    

`writing-mode` CSS property
===========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`writing-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether lines of text are laid out horizontally or vertically, as well as the direction in which text flows.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#try_it)

----------------------------------------------------------------------------------------------------

    writing-mode: horizontal-tb;
    

    writing-mode: vertical-lr;
    

    writing-mode: vertical-rl;
    

    writing-mode: sideways-rl;
    

    writing-mode: sideways-lr;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div>1</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      padding: 0.75em;
      width: 80%;
      max-height: 300px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
      margin: 10px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    writing-mode: horizontal-tb;
    writing-mode: vertical-rl;
    writing-mode: vertical-lr;
    writing-mode: sideways-rl;
    writing-mode: sideways-lr;
    
    /* Global values */
    writing-mode: inherit;
    writing-mode: initial;
    writing-mode: revert;
    writing-mode: revert-layer;
    writing-mode: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#values)

This property is specified as one of the following keywords:

[`horizontal-tb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#horizontal-tb)

For `ltr` scripts, content flows horizontally from left to right. For `rtl` scripts, content flows horizontally from right to left. The next horizontal line is positioned below the previous line.

[`vertical-rl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#vertical-rl)

For `ltr` scripts, content flows vertically from top to bottom, and the next vertical line is positioned to the left of the previous line. For `rtl` scripts, content flows vertically from bottom to top, and the next vertical line is positioned to the left of the previous line.

[`vertical-lr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#vertical-lr)

For `ltr` scripts, content flows vertically from top to bottom, and the next vertical line is positioned to the right of the previous line. For `rtl` scripts, content flows vertically from bottom to top, and the next vertical line is positioned to the right of the previous line.

[`sideways-rl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#sideways-rl)

For `ltr` scripts, content flows vertically from top to bottom. For `rtl` scripts, content flows vertically from bottom to top. All the glyphs, even those in vertical scripts, are set sideways toward the right.

[`sideways-lr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#sideways-lr)

For `ltr` scripts, content flows vertically from bottom to top. For `rtl` scripts, content flows vertically from top to bottom. All the glyphs, even those in vertical scripts, are set sideways toward the left.

[`lr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#lr)

Deprecated except for SVG1 documents. For CSS, use `horizontal-tb` instead.

[`lr-tb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#lr-tb)

Deprecated except for SVG1 documents. For CSS, use `horizontal-tb` instead.

[`rl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#rl)

Deprecated except for SVG1 documents. For CSS, use `horizontal-tb` instead.

[`tb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#tb)

Deprecated except for SVG1 documents. For CSS, use `vertical-lr` instead.

[`tb-lr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#tb-lr)

Deprecated except for SVG1 documents. For CSS, use `vertical-lr` instead.

[`tb-rl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#tb-rl)

Deprecated except for SVG1 documents. For CSS, use `vertical-rl` instead.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#description)

--------------------------------------------------------------------------------------------------------------

The `writing-mode` property sets whether lines of text are laid out horizontally or vertically. It specifies the _block flow direction_, which is the direction in which block-level containers are stacked, and the direction in which inline-level content flows within a block container. Thus, it also determines the ordering of block-level content.

The flow direction in horizontal scripts is also affected by the [directionality of that script](https://www.w3.org/International/questions/qa-scripts.en "External link (opens in new tab)")
, either left-to-right (`ltr`, like English and most other languages) or right-to-left (`rtl`, like Hebrew or Arabic).

When set for an entire document, it should be set on the root element (`html` element for HTML documents).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `horizontal-tb` |
| Applies to | all elements except table row groups, table column groups, table rows, and table columns |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#formal_syntax)

------------------------------------------------------------------------------------------------------------------

writing-mode =   
  horizontal-tb  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  vertical-rl    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  vertical-lr    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sideways-rl    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sideways-lr      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#examples)

--------------------------------------------------------------------------------------------------------

### [Using multiple writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#using_multiple_writing_modes)

This example demonstrates all of the writing modes, showing each with text in various languages.

#### HTML

The HTML is a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 with each writing mode in a row with a column showing text in various scripts using that writing mode.

html

    <table>
      <caption>
        Using multiple writing modes
      </caption>
      <thead>
        <tr>
          <th>Value</th>
          <th>Vertical script</th>
          <th>Horizontal (LTR) script</th>
          <th>Horizontal (RTL) script</th>
          <th>Mixed script</th>
        </tr>
      </thead>
      <tbody>
        <tr class="text1">
          <th>horizontal-tb</th>
          <td>我家没有电脑。</td>
          <td>Example text</td>
          <td>מלל ארוך לדוגמא</td>
          <td>1994年に至っては</td>
        </tr>
        <tr class="text2">
          <th>vertical-lr</th>
          <td>我家没有电脑。</td>
          <td>Example text</td>
          <td>מלל ארוך לדוגמא</td>
          <td>1994年に至っては</td>
        </tr>
        <tr class="text3">
          <th>vertical-rl</th>
          <td>我家没有电脑。</td>
          <td>Example text</td>
          <td>מלל ארוך לדוגמא</td>
          <td>1994年に至っては</td>
        </tr>
        <tr class="experimental text4">
          <th>sideways-lr</th>
          <td>我家没有电脑。</td>
          <td>Example text</td>
          <td>מלל ארוך לדוגמא</td>
          <td>1994年に至っては</td>
        </tr>
        <tr class="experimental text5">
          <th>sideways-rl</th>
          <td>我家没有电脑。</td>
          <td>Example text</td>
          <td>מלל ארוך לדוגמא</td>
          <td>1994年に至っては</td>
        </tr>
      </tbody>
    </table>
    <p class="notice">
      Your browser does not support the <code>sideways-lr</code> or
      <code>sideways-rl</code> values.
    </p>
    

#### CSS

    table {
      border-collapse: collapse;
    }
    td,
    th {
      border: 2px black solid;
      padding: 4px;
    }
    th {
      background-color: lightgray;
    }
    
    .experimental {
      display: none;
    }
    
    .notice {
      display: table-row;
      font-weight: bold;
      text-align: center;
    }
    
    @supports (writing-mode: sideways-lr) {
      .experimental {
        display: table-row;
      }
      .notice {
        display: none;
      }
    }
    

The CSS that adjusts the directionality of the content looks like this:

css

    .text1 td {
      writing-mode: horizontal-tb;
    }
    
    .text2 td {
      writing-mode: vertical-lr;
    }
    
    .text3 td {
      writing-mode: vertical-rl;
    }
    
    .text4 td {
      writing-mode: sideways-lr;
    }
    
    .text5 td {
      writing-mode: sideways-rl;
    }
    

#### Result

### [Using writing-mode with transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#using_writing-mode_with_transforms)

If your browser doesn't support `sideways-lr`, a workaround is to use [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 to achieve a similar effect depending on the script direction. The effect of `vertical-rl` is the same as with `sideways-lr`, so no transformation is required for left-to-right scripts. In some cases, rotating the text 180 degrees is sufficient to achieve the effect of `sideways-lr`, but font glyphs may not be designed to be rotated, so this may produce unexpected positioning or rendering.

#### HTML

html

    <table>
      <caption>
        Using writing-mode with transforms
      </caption>
      <thead>
        <tr>
          <th>Vertical LR</th>
          <th>Vertical LR with transform</th>
          <th>Sideways LR</th>
          <th>Only rotate</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="vertical-lr">我家没有电脑。</span>
            <span class="vertical-lr">Example text</span>
          </td>
          <td>
            <span class="vertical-lr rotated">我家没有电脑。</span>
            <span class="vertical-lr rotated">Example text</span>
          </td>
          <td>
            <span class="sideways-lr">我家没有电脑。</span>
            <span class="sideways-lr">Example text</span>
          </td>
          <td>
            <span class="only-rotate">我家没有电脑。</span>
            <span class="only-rotate">Example text</span>
          </td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    .vertical-lr {
      writing-mode: vertical-lr;
    }
    
    .rotated {
      transform: rotate(180deg);
    }
    
    .sideways-lr {
      writing-mode: sideways-lr;
    }
    
    .only-rotate {
      inline-size: fit-content;
      transform: rotate(-90deg);
    }
    

    table {
      border-collapse: collapse;
    }
    td,
    th {
      border: 2px black solid;
      padding: 4px;
    }
    th {
      background-color: lightgray;
    }
    span {
      display: inline-block;
      width: 1.5em;
      text-align: center;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4  <br>\# block-flow](https://drafts.csswg.org/css-writing-modes/#block-flow) |
| [Scalable Vector Graphics (SVG) 2  <br>\# WritingModeProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#WritingModeProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode#see_also)

--------------------------------------------------------------------------------------------------------

*   [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    
*   [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    
*   [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    
*   [`text-combine-upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    
*   [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
     module
*   SVG [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/writing-mode)
     attribute
*   [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
    
*   [Handling different text directions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions)
    
*   [Styling vertical text (Chinese, Japanese, Korean and Mongolian)](https://www.w3.org/International/articles/vertical-text/ "External link (opens in new tab)")
     on W3.org (2022)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/writing-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/writing-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwriting-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwriting-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwriting-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwriting-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe57e3fdd4ab6fb372ddc3d78e5b428f318202426%0A*+Document+last+modified%3A+2026-08-04T08%3A08%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
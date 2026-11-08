*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#mdn-search)
    

`text-spacing-trim` CSS property
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/236)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#browser_compatibility)
 carefully before using this in production.

The **`text-spacing-trim`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the internal spacing set on Chinese/Japanese/Korean (CJK) punctuation characters between adjacent characters (kerning) and at the start or end of text lines.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-spacing-trim: normal;
    text-spacing-trim: space-all;
    text-spacing-trim: space-first;
    text-spacing-trim: trim-start;
    
    /* Global values */
    text-spacing-trim: inherit;
    text-spacing-trim: initial;
    text-spacing-trim: revert;
    text-spacing-trim: revert-layer;
    text-spacing-trim: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#values)

[`<spacing-trim>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#spacing-trim)

Defines the different spacing trim options. Available values are:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#normal)

Sets CJK full-width opening punctuation characters to be full-width at the start of each line. Sets CJK full-width closing punctuation characters to be full-width at the end of each line, or half-width if they do not fit on the line before justification. [Collapses spacing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#full-width_punctuation_collapsing)
 between punctuation characters.

[`space-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#space-all)

All CJK full-width punctuation characters are set to be full-width.

[`space-first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#space-first)

Behaves as `normal`, except that CJK full-width opening punctuation characters are set to be full-width at the start of the first line of the text's block container, and the start of every subsequent line coming after an explicit line break such as a newline character.

[`trim-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#trim-start)

Behaves as `normal`, except that CJK full-width opening punctuation characters are set to be half-width at the start of each line.

**Note:** The [CSS Text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
 module also defines `trim-both`, `trim-all`, and `auto` values. However, these are not currently implemented in any browser.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#description)

-------------------------------------------------------------------------------------------------------------------

The `text-spacing-trim` property applies spacing/kerning to CJK punctuation characters to produce visually pleasing typography as defined by the [Requirements for Japanese text layout](https://w3c.github.io/jlreq/ "External link (opens in new tab)")
 (JLREQ) and the [Requirements for Chinese text layout](https://www.w3.org/International/clreq/ "External link (opens in new tab)")
 (CLREQ).

Many CJK punctuation characters include glyph-internal spacing. For example, the CJK full stop and the CJK close parenthesis usually have glyph-internal spacing on their right-hand side, to give them a constant [advance measure](https://developer.mozilla.org/en-US/docs/Glossary/Advance_measure)
 consistent with other ideographic characters. However, when they appear in a row, the glyph-internal spacing can become excessive.

`text-spacing-trim` can be used to adjust such excessive spacing between adjacent characters (kerning) and at the start or end of text lines. Generally speaking:

*   If a full-width punctuation character is set to be full-width, it has internal spacing set on both sides and is the full width of an ideograph.
*   If a full-width punctuation character is set to be half-width, it has internal spacing set on one side only, and its other side is flush to the start (in the case of opening punctuation characters) or end (in the case of closing punctuation characters). Half-width characters are typically half the width of an ideograph.

**Note:** To avoid the risk of excessive kerning, fonts must have the OpenType Alternate Half Widths (`halt`) feature, the Contextual Half-width Spacing (`chws`) feature, or both. If the font doesn't have either feature, `text-spacing-trim` is disabled.

### [Full-width punctuation collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#full-width_punctuation_collapsing)

When pairs of punctuation characters are adjacent to one another, the space between them is collapsed according to the following rules:

*   Set a full-width opening punctuation character to half-width if the previous character is a fullwidth opening punctuation character, a fullwidth middle dot, an ideographic space (U+3000), a fullwidth closing punctuation character of an equivalent or larger font size, or a character belonging to [Unicode general category "Open punctuation" Ps](https://www.compart.com/en/unicode/category/Ps "External link (opens in new tab)")
    . Otherwise, set it to full-width.
*   Set a full-width closing punctuation character to half-width if the next character is a fullwidth closing punctuation character, a fullwidth middle dot, an ideographic space (U+3000), a fullwidth opening punctuation character with larger font size, or a character belonging to [Unicode general category "Close punctuation" (Pe)](https://www.compart.com/en/unicode/category/Pe "External link (opens in new tab)")
    . Otherwise, set it to full-width.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | text elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

text-spacing-trim =   
  <spacing-trim>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto              
  
<spacing-trim> =   
  space-all    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-first  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-start   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-both    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-all       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#examples)

-------------------------------------------------------------------------------------------------------------

### [`text-spacing-trim` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#text-spacing-trim_value_comparison)

This example compares the effect of four different `text-spacing-trim` properties, applying them to four identical paragraphs so you can see the visual differences between each one.

#### HTML

html

    <main>
      <div id="normal">
        <h2>normal</h2>
        <p>
          （東）、【「（東）」】。<br />
          「東」「東」「東」東東東「東」。
        </p>
      </div>
      <div id="space-all">
        <h2>space-all</h2>
        <p>
          （東）、【「（東）」】。<br />
          「東」「東」「東」東東東「東」。
        </p>
      </div>
      <div id="space-first">
        <h2>space-first</h2>
        <p>
          （東）、【「（東）」】。<br />
          「東」「東」「東」東東東「東」。
        </p>
      </div>
      <div id="trim-start">
        <h2>trim-start</h2>
        <p>
          （東）、【「（東）」】。<br />
          「東」「東」「東」東東東「東」。
        </p>
      </div>
    </main>
    

#### CSS

css

    main {
      font-family:
        "Yu Gothic", "YuGothic", "Noto Sans JP", "Hiragino Sans",
        "Hiragino Kaku Gothic ProN", sans-serif;
      display: grid;
      gap: 0.5em;
      grid-template-columns: 1fr 1fr;
      width: 70%;
      margin: 0 auto;
    }
    h2 {
      font-size: 80%;
      margin: 0;
    }
    p {
      font-size: 20px;
      border: 1px solid blue;
      margin: 0;
    }
    #normal {
      text-spacing-trim: normal;
      grid-column: 1;
      grid-row: 1;
    }
    #space-all {
      text-spacing-trim: space-all;
      grid-column: 2;
      grid-row: 1;
    }
    #space-first {
      text-spacing-trim: space-first;
      grid-column: 1;
      grid-row: 2;
    }
    #trim-start {
      text-spacing-trim: trim-start;
      grid-column: 2;
      grid-row: 2;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# text-spacing-trim-property](https://drafts.csswg.org/css-text-4/#text-spacing-trim-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`text-autospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace)
    
*   [`ic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#local_font-relative_lengths)
     and [`ric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#root_font-relative_lengths)
     units
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-spacing-trim/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-spacing-trim (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-spacing-trim&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-spacing-trim%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-spacing-trim%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-spacing-trim%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
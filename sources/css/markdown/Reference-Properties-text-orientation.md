*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#mdn-search)
    

`text-orientation` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-orientation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the orientation of the text characters in a line. It only affects text in vertical mode (when [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 is not `horizontal-tb`). It is useful for controlling the display of languages that use vertical script, and also for making vertical table headers.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#try_it)

--------------------------------------------------------------------------------------------------------

    writing-mode: vertical-rl;
    text-orientation: mixed;
    

    writing-mode: vertical-rl;
    text-orientation: upright;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <p>
          In another moment down went Alice after it, never once considering how in
          the world she was to get out again.
        </p>
      </div>
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-orientation: mixed;
    text-orientation: upright;
    text-orientation: sideways-right;
    text-orientation: sideways;
    text-orientation: use-glyph-orientation;
    
    /* Global values */
    text-orientation: inherit;
    text-orientation: initial;
    text-orientation: revert;
    text-orientation: revert-layer;
    text-orientation: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#values)

This property is specified as one of the following keyword values:

[`mixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#mixed)

Rotates the characters of horizontal scripts 90° clockwise. Lays out the characters of vertical scripts naturally. Default value.

[`upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#upright)

Lays out the characters of horizontal scripts naturally (upright), as well as the glyphs for vertical scripts. Note that this keyword causes all characters to be considered as left-to-right: the used value of [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 is forced to be `ltr`.

[`sideways`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#sideways)

Causes characters to be laid out as they would be horizontally, but with the whole line rotated 90° clockwise.

[`sideways-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#sideways-right)

An alias to `sideways` that is kept for compatibility purposes.

[`use-glyph-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#use-glyph-orientation)

On SVG elements, this keyword leads to use the value of the deprecated SVG properties `glyph-orientation-vertical` and `glyph-orientation-horizontal`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `mixed` |
| Applies to | all elements, except table row groups, rows, column groups, and columns |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

text-orientation =   
  mixed     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  upright   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sideways    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#examples)

------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#html)

html

    <p>Lorem ipsum dolet semper quisquam.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#css)

css

    p {
      writing-mode: vertical-rl;
      text-orientation: upright;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4  <br>\# text-orientation](https://drafts.csswg.org/css-writing-modes/#text-orientation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation#see_also)

------------------------------------------------------------------------------------------------------------

*   The other vertical-script related CSS properties: [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`text-combine-upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    , and [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    .
*   [CSS Logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   [Styling vertical text (Chinese, Japanese, Korean and Mongolian)](https://www.w3.org/International/articles/vertical-text/ "External link (opens in new tab)")
    
*   Extensive browsers support test results: [https://w3c.github.io/i18n-tests/results/horizontal-in-vertical.html#text\_orientation](https://w3c.github.io/i18n-tests/results/horizontal-in-vertical.html#text_orientation "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-orientation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-orientation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-orientation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-orientation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-orientation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-orientation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
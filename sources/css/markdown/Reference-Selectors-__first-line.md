*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#mdn-search)
    

`::first-line` CSS pseudo-element
=================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::first-line`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 applies styles to the first line of a [block container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model#block_containers)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#try_it)

---------------------------------------------------------------------------------------------------

    p::first-line {
      font-size: 1.2rem;
      font-weight: bold;
      text-decoration: underline;
    }
    

    <p>
      In warm ocean waters around the world, you may see a strange sight: A fish
      leaping from the water and soaring dozens of meters before returning to the
      ocean's depths. Early Mediterranean sailors thought these flying fish returned
      to the shore at night to sleep, and therefore called this family of marine
      fish Exocoetidae.
    </p>
    

The effects of `::first-line` are limited by the length and content of the first line of text in the element. The length of the first line depends on many factors, including the width of the element, the width of the document, and the font size of the text. `::first-line` has no effect when the first child of the element, which would be the first part of the first line, is an inline block-level element, such as an inline table.

**Note:** [Selectors Level 3](https://drafts.csswg.org/selectors-3/#first-line "External link (opens in new tab)")
 introduced the double-colon notation (`::`) to distinguish [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 from the single-colon (`:`) [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
. Browsers accept both `::first-line` and `:first-line`, which was introduced in CSS2.

For the purposes of CSS [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
, the `::first-line` pseudo-element is like an inline-level element meaning that in a left-justified first line, the background may not extend all the way to the right margin.

[Allowable properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#allowable_properties)

-------------------------------------------------------------------------------------------------------------------------------

Only a small subset of CSS properties can be used with the `::first-line` pseudo-element:

*   All font-related properties: [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    , [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    , [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    , [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    , [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    , [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    , [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    , [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    , [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    , [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    , [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    , [`font-language-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    , [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    , [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
    , [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
    , and [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   All background-related properties: [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    , [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    , [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
    , [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    , [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    , and [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    
*   The [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     property
*   [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
    , [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    , [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    , [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    , and [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    , [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    , and [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    .

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#syntax)

---------------------------------------------------------------------------------------------------

css

    ::first-line {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#examples)

-------------------------------------------------------------------------------------------------------

### [Styling first line of a paragraph](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#styling_first_line_of_a_paragraph)

#### HTML

html

    <p>
      Styles will only be applied to the first line of this paragraph. After that,
      all text will be styled like normal. See what I mean?
    </p>
    
    <span>
      The first line of this text will not receive special styling because it is not
      a block-level element.
    </span>
    

#### CSS

    * {
      font-size: 20px;
      font-family: sans-serif;
    }
    

css

    ::first-line {
      color: blue;
      font-weight: bold;
    
      /* WARNING: DO NOT USE THESE */
      /* Many properties are invalid in ::first-line pseudo-elements */
      margin-left: 20px;
      text-indent: 20px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#result)

### [Styling the first line of an SVG text element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#styling_the_first_line_of_an_svg_text_element)

In this example, we style the first line of an SVG [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 element using the `::first-line` pseudo-element.

**Note:** At time of writing this feature has [limited support](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#browser_compatibility)
.

#### HTML

html

    <svg viewBox="0 0 320 150">
      <text y="20">Here is an English paragraph
    that is broken into multiple lines
    in the source code so that it can
    be more easily read and edited
    in a text editor.
      </text>
    </svg>
    

#### CSS

In order to make the SVG `<text>` element wrap to multiple lines, we use the [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space#multiple_lines_in_svg_text_element)
 CSS property. We then select the first line using the `::first-line` pseudo-element.

    text {
      font-size: 20px;
      font-family: sans-serif;
    }
    

css

    text {
      white-space: break-spaces;
    }
    
    text::first-line {
      fill: blue;
      font-weight: bold;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# first-line-pseudo](https://drafts.csswg.org/css-pseudo/#first-line-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line#see_also)

-------------------------------------------------------------------------------------------------------

*   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_first-line/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_first-line (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afirst-line&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_first-line%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afirst-line%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_first-line%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7ed7b730bf88307cc6cf34b82bb1d735b9a1aa1f%0A*+Document+last+modified%3A+2026-07-28T05%3A29%3A56.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
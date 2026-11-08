*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#mdn-search)
    

`::first-letter` CSS pseudo-element
===================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::first-letter`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 applies styles to the first letter of the first line of a [block container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model#block_containers)
, but only when not preceded by other content (such as images or inline tables).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#try_it)

-----------------------------------------------------------------------------------------------------

    p::first-letter {
      font-size: 1.5rem;
      font-weight: bold;
      color: brown;
    }
    

    <p>
      Scientists exploring the depths of Monterey Bay unexpectedly encountered a
      rare and unique species of dragonfish. This species is the rarest of its
      species.
    </p>
    
    <p>
      When Robison and a team of researchers discovered this fish, they were aboard
      a week-long expedition.
    </p>
    

The first letter of an element is not always trivial to identify:

*   Punctuation that precedes or immediately follows the first letter is included in the match. Punctuation includes any Unicode character defined in the _open_ (Ps), _close_ (Pe), _initial quote_ (Pi), _final quote_ (Pf), and _other punctuation_ (Po) classes.
*   Some languages have digraphs that are always capitalized together, like the `IJ` in Dutch. In these cases, both letters of the digraph should be matched by the `::first-letter` pseudo-element.
*   A combination of the [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
     pseudo-element and the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
     property may inject some text at the beginning of the element. In that case, `::first-letter` will match the first letter of this generated content.

**Note:** CSS introduced the `::first-letter` notation (with two colons) to distinguish [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 from [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
. For backward compatibility, browsers also accept `:first-letter`, introduced earlier.

Browser support for digraphs such as `IJ` in Dutch is poor. Check the compatibility table below to see the current state of support.

[Allowable properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#allowable_properties)

---------------------------------------------------------------------------------------------------------------------------------

Only a small subset of CSS properties can be used with the `::first-letter` pseudo-element:

*   All font properties: [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    , [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    , [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    , [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    , [`font-language-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
    , [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
    , [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    , [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    , [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    , [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    , [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    , [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    , [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    , [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    , [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    , [`font-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
    , [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
     and [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   All background properties: [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    , [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    , [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
    , [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    , [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    , and [`background-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    
*   All margin properties: [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    , [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    , [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   All padding properties: [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    , [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    , [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    , [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    , [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    
*   All border properties: the shorthands [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    , [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    , [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
    , and the longhands properties
*   The [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     property
*   The [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    , [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    , [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
     (when appropriate), [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    , [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    , [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    , [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
    , [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
     (only if `float` is `none`) CSS properties

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#syntax)

-----------------------------------------------------------------------------------------------------

css

    ::first-letter {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#examples)

---------------------------------------------------------------------------------------------------------

### [Basic drop cap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#basic_drop_cap)

In this example we will use the `::first-letter` pseudo-element to create a drop cap effect on the first letter of the paragraph coming right after the `<h2>`.

#### HTML

html

    <h2>My heading</h2>
    <p>
      Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
      eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
      voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita
      kasd gubergren, no sea takimata sanctus est.
    </p>
    <p>
      Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie
      consequat.
    </p>
    

#### CSS

css

    p {
      width: 500px;
      line-height: 1.5;
    }
    
    h2 + p::first-letter {
      color: white;
      background-color: black;
      border-radius: 2px;
      box-shadow: 3px 3px 0 red;
      font-size: 250%;
      padding: 6px 3px;
      margin-right: 6px;
      float: left;
    }
    

#### Result

### [Effect on special punctuation and non-Latin characters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#effect_on_special_punctuation_and_non-latin_characters)

This example illustrates the effect of `::first-letter` on special punctuation and non-Latin characters.

#### HTML

html

    <p>
      Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie
      consequat.
    </p>
    <p>-The beginning of a special punctuation mark.</p>
    <p>_The beginning of a special punctuation mark.</p>
    <p>"The beginning of a special punctuation mark.</p>
    <p>'The beginning of a special punctuation mark.</p>
    <p>*The beginning of a special punctuation mark.</p>
    <p>#The beginning of a special punctuation mark.</p>
    <p>「特殊的汉字标点符号开头。</p>
    <p>《特殊的汉字标点符号开头。</p>
    <p>"特殊的汉字标点符号开头。</p>
    

#### CSS

css

    p::first-letter {
      color: red;
      font-size: 150%;
    }
    

#### Result

### [Styling first letter in SVG text element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#styling_first_letter_in_svg_text_element)

In this example, we use the `::first-letter` pseudo-element to style the first letter of an SVG [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 element.

**Note:** At time of writing this feature has [limited support](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#browser_compatibility)
.

#### HTML

html

    <svg viewBox="0 0 300 40">
      <text y="30">First letter in &lt;text&gt; SVG</text>
    </svg>
    

#### CSS

css

    text {
      font-family: sans-serif;
    }
    
    text::first-letter {
      font-family: serif;
      font-size: 2rem;
      font-weight: 600;
      fill: tomato;
      stroke: indigo;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# first-letter-pseudo](https://drafts.csswg.org/css-pseudo/#first-letter-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter#see_also)

---------------------------------------------------------------------------------------------------------

*   [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_first-letter/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_first-letter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afirst-letter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_first-letter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Afirst-letter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_first-letter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7ed7b730bf88307cc6cf34b82bb1d735b9a1aa1f%0A*+Document+last+modified%3A+2026-07-28T05%3A29%3A56.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
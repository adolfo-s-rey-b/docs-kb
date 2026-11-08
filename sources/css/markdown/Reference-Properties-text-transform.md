*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#mdn-search)
    

`text-transform` CSS property
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-transform`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies how to capitalize an element's text. It can be used to make text appear in all-uppercase or all-lowercase, or with each word capitalized. It also can help improve legibility for ruby.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#try_it)

------------------------------------------------------------------------------------------------------

    text-transform: capitalize;
    

    text-transform: uppercase;
    

    text-transform: lowercase;
    

    text-transform: none;
    

    text-transform: full-width;
    

    text-transform: full-size-kana;
    

    text-transform: math-auto;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        <p>
          LONDON. Michaelmas term lately over, and the Lord Chancellor sitting in
          Lincoln's Inn Hall.
        </p>
        <p lang="el">
          Σ is a Greek letter and appears in ΟΔΥΣΣΕΥΣ. Θα πάμε στο "Θεϊκό φαΐ" ή στη
          "Νεράιδα"
        </p>
        <p lang="ja">ァィゥェ ォヵㇰヶ</p>
      </div>
    </section>
    

    #example-element {
      font-size: 1.2em;
    }
    

The `text-transform` property takes into account language-specific case mapping rules such as the following:

*   In Turkic languages, like Turkish (`tr`), Azerbaijani (`az`), Crimean Tatar (`crh`), Volga Tatar (`tt`), and Bashkir (`ba`), there are two kinds of `i`, with and without the dot, and two case pairings: `i`/`İ` and `ı`/`I`.
*   In German (`de`), the `ß` becomes `SS` in uppercase.
*   In Dutch (`nl`), the `ij` digraph becomes `IJ`, even with `text-transform: capitalize`, which only puts the first letter of a word in uppercase.
*   In Greek (`el`), vowels lose their accent when the whole word is in uppercase (`ά`/`Α`), except for the disjunctive eta (`ή`/`Ή`). Also, diphthongs with an accent on the first vowel lose the accent and gain a diaeresis on the second vowel (`άι`/`ΑΪ`).
*   In Greek (`el`), the lowercase sigma character has two forms: `σ` and `ς`. `ς` is used only when sigma terminates a word. When applying `text-transform: lowercase` to an uppercase sigma (`Σ`), the browser needs to choose the right lowercase form based on context.
*   in Irish (`ga`), certain prefixed letters remain in lowercase when the base initial is capitalized, so for example `text-transform: uppercase` will change `ar aon tslí` to `AR AON tSLÍ` and not, as one might expect, `AR AON TSLÍ` (Firefox only). In some cases, a hyphen is also removed upon uppercasing: `an t-uisce` transforms to `AN tUISCE` (and the hyphen is correctly reinserted by `text-transform: lowercase`).

The language is defined by the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 HTML attribute or the [`xml:lang`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/xml:lang)
 XML attribute.

**Note:** Support for language-specific cases varies between browsers, so check the [browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#browser_compatibility)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-transform: none;
    text-transform: capitalize;
    text-transform: uppercase;
    text-transform: lowercase;
    text-transform: full-width;
    text-transform: full-size-kana;
    text-transform: math-auto;
    
    /* Global values */
    text-transform: inherit;
    text-transform: initial;
    text-transform: revert;
    text-transform: revert-layer;
    text-transform: unset;
    

[`capitalize`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#capitalize)

Is a keyword that converts the first _letter_ of each word to uppercase. Other characters remain unchanged (they retain their original case as written in the element's text). A letter is defined as a character that is part of Unicode's Letter or Number general categories; thus, any punctuation marks or symbols at the beginning of a word are ignored.

**Warning:** In many languages, it is considered incorrect to capitalize every word in a sentence, even in titles and names. If you don't know the language of the text the style will be applied to, you should avoid using `capitalize`. Furthermore, `capitalize` does not create title casing, because it does not apply language-specific rules such as skipping articles in English.

**Note:** The `capitalize` keyword was under-specified in CSS 1 and CSS 2.1. This resulted in differences between browsers in the way the first letter was calculated (Firefox considered `-` and `_` as letters, but other browsers did not. Both WebKit and Gecko incorrectly considered letter-based symbols like `ⓐ` to be real letters.) By precisely defining the correct behavior, CSS Text Level 3 cleans this mess up. The `capitalize` line in the browser compatibility table contains the version the different engines started to support this now precisely-defined behavior.

[`uppercase`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#uppercase)

Is a keyword that converts all characters to uppercase.

[`lowercase`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#lowercase)

Is a keyword that converts all characters to lowercase.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#none)

Is a keyword that prevents the case of all characters from being changed.

[`full-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#full-width)

Is a keyword that forces the writing of a character — mainly ideograms and Latin scripts — inside a square, allowing them to be aligned in the usual East Asian scripts (like Chinese or Japanese).

[`full-size-kana`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#full-size-kana)

Generally used for [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 annotation text, the keyword converts all small Kana characters to the equivalent full-size Kana, to compensate for legibility issues at the small font sizes typically used in ruby.

[`math-auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#math-auto)

Used to automatically render text in math italic where appropriate. It transforms Latin and Greek letters, and a few other math-related symbols, to [italic mathematical symbols](https://www.unicode.org/charts/PDF/U1D400.pdf "External link (opens in new tab)")
 but only if it's applied on a text node containing a single character. For example, "x" will become "𝑥" (U+1D465), but "exp" will stay as "exp". It is primarily used to specify the behavior of [`<mi>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/mi "<mi>")
 elements in MathML. You should generally use MathML markup which automatically applies the right styling.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#accessibility)

--------------------------------------------------------------------------------------------------------------------

Large sections of text set with a `text-transform` value of `uppercase` may be difficult for people with cognitive concerns such as Dyslexia to read.

*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [W3C Understanding WCAG 2.2](https://w3c.github.io/wcag/guidelines/22/#visual-presentation "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

text-transform =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 capitalize [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 uppercase [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 lowercase [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 full-width [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 full-size-kana  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  math-auto                                             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#examples)

----------------------------------------------------------------------------------------------------------

### [Example using "none"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_none)

html

    <p>
      Initial String
      <strong>Lorem ipsum dolor sit amet, consectetur adipisicing elit…</strong>
    </p>
    <p>
      text-transform: none
      <strong
        ><span
          >Lorem ipsum dolor sit amet, consectetur adipisicing elit…</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: none;
    }
    strong {
      float: right;
    }
    

This demonstrates no text transformation.

### [Example using "capitalize" (general)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_capitalize_general)

html

    <p>
      Initial String
      <strong>Lorem ipsum dolor sit amet, consectetur adipisicing elit…</strong>
    </p>
    <p>
      text-transform: capitalize
      <strong
        ><span
          >Lorem ipsum dolor sit amet, consectetur adipisicing elit…</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: capitalize;
    }
    strong {
      float: right;
    }
    

This demonstrates text capitalization.

### [Example using "capitalize" (punctuation)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_capitalize_punctuation)

html

    <p>
      Initial String
      <strong
        >(this) "is" [a] –short– -test- «for» *the* _css_ ¿capitalize?
        ?¡transform!</strong
      >
    </p>
    <p>
      text-transform: capitalize
      <strong
        ><span
          >(this) "is" [a] –short– -test- «for» *the* _css_ ¿capitalize?
          ?¡transform!</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: capitalize;
    }
    strong {
      float: right;
    }
    

This demonstrates how initial punctuations of a word are ignored. The keyword target the first letter, that is the first Unicode character part of the Letter or Number general category.

### [Example using "capitalize" (Symbols)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_capitalize_symbols)

html

    <p>
      Initial String
      <strong>ⓐⓑⓒ (ⓓⓔⓕ) —ⓖⓗⓘ— ⓙkl</strong>
    </p>
    <p>
      text-transform: capitalize
      <strong><span>ⓐⓑⓒ (ⓓⓔⓕ) —ⓖⓗⓘ— ⓙkl</span></strong>
    </p>
    

css

    span {
      text-transform: capitalize;
    }
    strong {
      float: right;
    }
    

This demonstrates how initial symbols are ignored. The keyword target the first letter, that is the first Unicode character part of the Letter or Number general category.

### [Example using "capitalize" (Dutch ij digraph)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_capitalize_dutch_ij_digraph)

html

    <p>
      Initial String
      <strong lang="nl">The Dutch word: "ijsland" starts with a digraph.</strong>
    </p>
    <p>
      text-transform: capitalize
      <strong
        ><span lang="nl"
          >The Dutch word: "ijsland" starts with a digraph.</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: capitalize;
    }
    strong {
      float: right;
    }
    

This demonstrates how the Dutch _ij_ digraph must be handled like one single letter.

### [Example using "uppercase" (general)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_uppercase_general)

html

    <p>
      Initial String
      <strong>Lorem ipsum dolor sit amet, consectetur adipisicing elit…</strong>
    </p>
    <p>
      text-transform: uppercase
      <strong
        ><span
          >Lorem ipsum dolor sit amet, consectetur adipisicing elit…</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: uppercase;
    }
    strong {
      float: right;
    }
    

This demonstrates transforming the text to uppercase.

### [Example using "uppercase" (Greek vowels)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_uppercase_greek_vowels)

html

    <p>
      Initial String
      <strong>Θα πάμε στο "Θεϊκό φαΐ" ή στη "Νεράιδα"</strong>
    </p>
    <p>
      text-transform: uppercase
      <strong
        ><span lang="el">Θα πάμε στο "Θεϊκό φαΐ" ή στη "Νεράιδα"</span></strong
      >
    </p>
    

css

    span {
      text-transform: uppercase;
    }
    strong {
      float: right;
    }
    

This demonstrates how Greek vowels except disjunctive _eta_ should have no accent, and the accent on the first vowel of a vowel pair becomes a diaeresis on the second vowel.

### [Example using "lowercase" (general)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_lowercase_general)

html

    <p>
      Initial String
      <strong>Lorem ipsum dolor sit amet, consectetur adipisicing elit…</strong>
    </p>
    <p>
      text-transform: lowercase
      <strong
        ><span
          >Lorem ipsum dolor sit amet, consectetur adipisicing elit…</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: lowercase;
    }
    strong {
      float: right;
    }
    

This demonstrates transforming the text to lowercase.

### [Example using "lowercase" (Greek Σ)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_lowercase_greek_%CF%83)

html

    <p>
      Initial String
      <strong>Σ IS A greek LETTER that appears SEVERAL TIMES IN ΟΔΥΣΣΕΥΣ.</strong>
    </p>
    <p>
      text-transform: lowercase
      <strong
        ><span
          >Σ IS A greek LETTER that appears SEVERAL TIMES IN ΟΔΥΣΣΕΥΣ.</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: lowercase;
    }
    strong {
      float: right;
    }
    

This demonstrates how the Greek character sigma (`Σ`) is transformed into the regular lowercase sigma (`σ`) or the word-final variant (`ς`), according the context.

### [Example using "lowercase" (Lithuanian)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_lowercase_lithuanian)

html

    <p>
      Initial String
      <strong>Ĩ is a Lithuanian LETTER as is J́</strong>
    </p>
    <p>
      text-transform: lowercase
      <strong><span lang="lt">Ĩ is a Lithuanian LETTER as is J́</span></strong>
    </p>
    

css

    span {
      text-transform: lowercase;
    }
    strong {
      float: right;
    }
    

This demonstrates how the Lithuanian letters `Ĩ` and `J́` retain their dot when transformed to lowercase.

### [Example using "full-width" (general)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_full-width_general)

html

    <p>
      Initial String
      <strong
        >0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;&lt;=&gt;?@{|}~</strong
      >
    </p>
    <p>
      text-transform: full-width
      <strong
        ><span
          >0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;&lt;=&gt;?@{|}~</span
        ></strong
      >
    </p>
    

css

    span {
      text-transform: full-width;
    }
    strong {
      width: 100%;
      float: right;
    }
    

Some characters exist in two formats: normal width and a full-width, with different Unicode code points. The full-width version is used to mix them smoothly with Asian ideographic characters.

### [Example using "full-width" (Japanese half-width katakana)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_full-width_japanese_half-width_katakana)

html

    <p>
      Initial String
      <strong>ｳｪﾌﾞﾌﾟﾛｸﾞﾗﾐﾝｸﾞの勉強</strong>
    </p>
    <p>
      text-transform: full-width
      <strong><span>ｳｪﾌﾞﾌﾟﾛｸﾞﾗﾐﾝｸﾞの勉強</span></strong>
    </p>
    

css

    span {
      text-transform: full-width;
    }
    strong {
      width: 100%;
      float: right;
    }
    

The Japanese half-width katakana was used to represent katakana in 8-bit character codes. Unlike regular (full-width) katakana characters, a letter with dakuten (voiced sound mark) is represented as two code points, the body of letter and dakuten. The `full-width` combines these into a single code point when converting these characters into full-width.

### [Example using "full-size-kana"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_full-size-kana)

html

    <p>ァィゥェ ォヵㇰヶ ㇱㇲッㇳ ㇴㇵㇶㇷ ㇸㇹㇺャ ュョㇻㇼ ㇽㇾㇿヮ</p>
    <p>ァィゥェ ォヵㇰヶ ㇱㇲッㇳ ㇴㇵㇶㇷ ㇸㇹㇺャ ュョㇻㇼ ㇽㇾㇿヮ</p>
    

css

    p:nth-of-type(2) {
      text-transform: full-size-kana;
    }
    

### [Example using "math-auto"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#example_using_math-auto)

In this example, we use pure HTML markup to create a math formula:

html

    <div>
      (<span class="math-id">sin</span>&#8198;<span class="math-id">x</span>)<sup
        >2</sup
      >
      + (<span class="math-id">cos</span>&#8198;<span class="math-id">x</span>)<sup
        >2</sup
      >
      = 1
    </div>
    

We give every `.math-id` element `text-transform: math-auto`. However, note how only the `x` characters become italic, while the `sin` and `cos` remain unchanged.

css

    .math-id {
      text-transform: math-auto;
    }
    

However, you are encouraged to use [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
 for mathematical formulas, as it provides a more robust and accessible way to represent mathematical content. Here's the same formula using MathML:

xml

    <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
      <semantics>
        <mrow>
          <mo stretchy="false">(</mo>
          <mo lspace="0em" rspace="0em">sin</mo>
          <mspace width="0.16666666666666666em"></mspace>
          <mi>x</mi>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mo lspace="0em" rspace="0em">cos</mo>
          <mspace width="0.16666666666666666em"></mspace>
          <mi>x</mi>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>=</mo>
          <mn>1</mn>
        </mrow>
        <annotation encoding="TeX">(\sin\,x)^2+(\cos\,x)^2=1</annotation>
      </semantics>
    </math>
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# text-transform-property](https://drafts.csswg.org/css-text-4/#text-transform-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform#see_also)

----------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-transform/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-transform (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-transform&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-transform%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-transform%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-transform%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
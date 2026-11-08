*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#mdn-search)
    

`word-break` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`word-break`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether line breaks appear wherever the text would otherwise overflow its content box.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#try_it)

--------------------------------------------------------------------------------------------------

    word-break: normal;
    

    word-break: break-all;
    

    word-break: keep-all;
    

    word-break: break-word;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        Honorificabilitudinitatibus califragilisticexpialidocious
        Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
        グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
      </div>
    </section>
    

    #example-element {
      width: 80%;
      padding: 20px;
      text-align: start;
      border: solid 1px darkgray;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    word-break: normal;
    word-break: break-all;
    word-break: keep-all;
    word-break: auto-phrase; /* experimental */
    word-break: break-word; /* deprecated */
    
    /* Global values */
    word-break: inherit;
    word-break: initial;
    word-break: revert;
    word-break: revert-layer;
    word-break: unset;
    

The `word-break` property is specified as a single keyword chosen from the list of values below.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#normal)

Use the default line break rule.

[`break-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#break-all)

To prevent overflow, word breaks should be inserted between any two characters (excluding Chinese/Japanese/Korean text).

[`keep-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#keep-all)

Word breaks should not be used for Chinese/Japanese/Korean (CJK) text. Non-CJK text behavior is the same as for `normal`.

[`auto-phrase`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#auto-phrase)

Has the same effect as `word-break: normal` except that language-specific analysis is performed to improve word breaks by not placing them in the middle of natural phrases.

[`break-word`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#break-word)

Has the same effect as `overflow-wrap: anywhere` combined with `word-break: normal`, regardless of the actual value of the [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
 property.

**Note:** In contrast to `word-break: break-word` and `overflow-wrap: break-word` (see [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
), `word-break: break-all` will create a break at the exact place where text would otherwise overflow its container (even if putting an entire word on its own line would negate the need for a break).

The specification also lists an additional value, `manual`, which is not currently supported in any browsers. When implemented, `manual` will have the same effect as `word-break: normal` except that breaks won't be automatically inserted in Southeast Asian languages. This is needed because, in such languages, user agents frequently place breaks in suboptimal positions. `manual` will allow you to insert line breaks in optimal positions manually.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#formal_syntax)

----------------------------------------------------------------------------------------------------------------

word-break =   
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  break-all    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  keep-all     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  manual       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto-phrase  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  break-word     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#examples)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#html)

html

    <p>1. <code>word-break: normal</code></p>
    <p class="normal narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    
    <p>2. <code>word-break: break-all</code></p>
    <p class="breakAll narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    
    <p>3. <code>word-break: keep-all</code></p>
    <p class="keepAll narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    
    <p>4. <code>word-break: manual</code></p>
    <p class="manual narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    
    <p>5. <code>word-break: auto-phrase</code></p>
    <p class="autoPhrase narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    
    <p>6. <code>word-break: break-word</code></p>
    <p class="breakWord narrow">
      This is a long and Honorificabilitudinitatibus califragilisticexpialidocious
      Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
      グレートブリテンおよび北アイルランド連合王国という言葉は本当に長い言葉
    </p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#css)

css

    .narrow {
      padding: 10px;
      border: 1px solid;
      width: 500px;
      margin: 0 auto;
      font-size: 20px;
      line-height: 1.5;
      letter-spacing: 1px;
    }
    
    .normal {
      word-break: normal;
    }
    
    .breakAll {
      word-break: break-all;
    }
    
    .keepAll {
      word-break: keep-all;
    }
    
    .manual {
      word-break: manual;
    }
    
    .autoPhrase {
      word-break: auto-phrase;
    }
    
    .breakWord {
      word-break: break-word;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# word-break-property](https://drafts.csswg.org/css-text/#word-break-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#see_also)

------------------------------------------------------------------------------------------------------

*   [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    
*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`line-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break)
    
*   [Guide to wrapping and breaking text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/word-break/index.md?plain=1 "Folder: en-us/web/css/reference/properties/word-break (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fword-break&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fword-break%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fword-break%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fword-break%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
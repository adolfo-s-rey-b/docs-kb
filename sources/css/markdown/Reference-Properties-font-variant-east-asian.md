*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#mdn-search)
    

`font-variant-east-asian` CSS property
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-east-asian`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the use of alternate glyphs for East Asian scripts, like Japanese and Chinese.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#try_it)

---------------------------------------------------------------------------------------------------------------

    font-variant-east-asian: normal;
    

    font-variant-east-asian: ruby;
    

    font-variant-east-asian: jis78;
    

    font-variant-east-asian: proportional-width;
    

    <section id="default-example">
      <div id="example-element">
        <p>
          JIS78とJIS83以降では、檜と桧、籠と篭など、一部の文字の入れ替えが行われている。また、「唖然」や「躯体」などの書体が変更されている。
        </p>
      </div>
    </section>
    

    section {
      font-family:
        "YuGothic Medium", "YuGothic", "Yu Gothic Medium", "Yu Gothic", sans-serif;
      margin-top: 10px;
      font-size: 1.5em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#syntax)

---------------------------------------------------------------------------------------------------------------

css

    font-variant-east-asian: normal;
    font-variant-east-asian: ruby;
    font-variant-east-asian: jis78; /* <east-asian-variant-values> */
    font-variant-east-asian: jis83; /* <east-asian-variant-values> */
    font-variant-east-asian: jis90; /* <east-asian-variant-values> */
    font-variant-east-asian: jis04; /* <east-asian-variant-values> */
    font-variant-east-asian: simplified; /* <east-asian-variant-values> */
    font-variant-east-asian: traditional; /* <east-asian-variant-values> */
    font-variant-east-asian: full-width; /* <east-asian-width-values> */
    font-variant-east-asian: proportional-width; /* <east-asian-width-values> */
    font-variant-east-asian: ruby full-width jis83;
    
    /* Global values */
    font-variant-east-asian: inherit;
    font-variant-east-asian: initial;
    font-variant-east-asian: revert;
    font-variant-east-asian: revert-layer;
    font-variant-east-asian: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#values)

This property is specified either as `normal` or `ruby` or as a space-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#normal)

This keyword leads to the deactivation of the use of such alternate glyphs.

[`ruby`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#ruby)

This keyword forces the use of special glyphs for ruby characters. As these are usually smaller, font creators often designs specific forms, usually slightly bolder to improve the contrast. This keyword corresponds to the OpenType values `ruby`.

[`<east-asian-variant-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#east-asian-variant-values)

These values specify a set of logographic glyph variants which should be used for display. Possible values are:

| Keyword | Standard defining the glyphs | OpenType equivalent |
| --- | --- | --- |
| `jis78` | [JIS X 0208:1978](https://en.wikipedia.org/wiki/JIS_X_0208#First_standard "External link (opens in new tab)") | `jp78` |
| `jis83` | [JIS X 0208:1983](https://en.wikipedia.org/wiki/JIS_X_0208#Second_standard "External link (opens in new tab)") | `jp83` |
| `jis90` | [JIS X 0208:1990](https://en.wikipedia.org/wiki/JIS_X_0208#Third_standard "External link (opens in new tab)") | `jp90` |
| `jis04` | [JIS X 0213:2004](https://en.wikipedia.org/wiki/JIS_X_0213 "External link (opens in new tab)") | `jp04` |
| `simplified` | None, use the simplified Chinese glyphs | `smpl` |
| `traditional` | None, use the traditional Chinese glyphs | `trad` |

[`<east-asian-width-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#east-asian-width-values)

These values control the sizing of figures used for East Asian characters. Two values are possible:

*   `proportional-width` activating the set of East Asian characters which vary in width. It corresponds to the OpenType values `pwid`.
*   `full-width` activating the set of East Asian characters which are all of the same, roughly square, width metric. It corresponds to the OpenType values `fwid`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

font-variant-east-asian =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <east-asian-variant-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <east-asian-width-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ruby [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<east-asian-variant-values> =   
  jis78        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis83        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis90        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis04        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  simplified   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  traditional    
  
<east-asian-width-values> =   
  full-width          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  proportional-width    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#examples)

-------------------------------------------------------------------------------------------------------------------

### [Setting East Asian glyph variants](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#setting_east_asian_glyph_variants)

This example require font "Yu Gothic" installed in your OS, other fonts may not support OpenType features.

#### HTML

html

    <table>
      <thead></thead>
      <tbody>
        <tr>
          <th>normal/jis78:</th>
          <td>麹町</td>
          <td class="jis78">麹町</td>
        </tr>
        <tr>
          <th>normal/ruby:</th>
          <td>しんかんせん</td>
          <td class="ruby">しんかんせん</td>
        </tr>
        <tr>
          <th>normal/traditional:</th>
          <td>大学</td>
          <td class="traditional">大学</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    tbody {
      border: 0;
    }
    
    td {
      font-family: "Yu Gothic", fantasy;
      font-size: 20px;
    }
    th {
      color: grey;
      padding-right: 10px;
    }
    
    .ruby {
      font-variant-east-asian: ruby;
    }
    
    .jis78 {
      font-variant-east-asian: jis78;
    }
    
    .traditional {
      font-variant-east-asian: traditional;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-east-asian-prop](https://drafts.csswg.org/css-fonts/#font-variant-east-asian-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-east-asian/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-east-asian (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-east-asian&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-east-asian%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-east-asian%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-east-asian%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
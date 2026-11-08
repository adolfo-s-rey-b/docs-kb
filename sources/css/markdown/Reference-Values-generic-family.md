*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#mdn-search)
    

`<generic-family>` CSS type
===========================

The **`<generic-family>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents the keyword values for generic font families used in the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand and [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 longhand properties. The `<generic-family>` represents one or more locally-installed fonts belonging to that category of fonts.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#syntax)

--------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#values)

The `<generic-family>` [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 type is specified using one of the values listed below:

[`serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#serif)

A serif is a small line or stroke attached to the end of a larger stroke in a letter. In serif fonts, glyphs have finishing strokes, flared or tapering ends. Examples include Lucida Bright, Lucida Fax, Palatino, Palatino Linotype, Palladio, and URW Palladio.

[`sans-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#sans-serif)

A font without serifs; glyphs have plain stroke endings, without ornamentation. Example sans-serif fonts include Open Sans, Fira Sans, Lucida Sans, Lucida Sans Unicode, Trebuchet MS, Liberation Sans, and Nimbus Sans L.

[`monospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#monospace)

All glyphs have the same fixed width. Example monospace fonts include Fira Mono, DejaVu Sans Mono, Menlo, Consolas, Liberation Mono, Monaco, and Lucida Console.

[`cursive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#cursive)

Glyphs in cursive fonts generally use a cursive script or other handwriting style, and the result looks more like handwritten pen or brush writing than printed typesetting. CSS uses the term "cursive" to apply to a font for any script, including those that do not have joining strokes. Example cursive fonts include Brush Script MT, Brush Script Std, Lucida Calligraphy, Lucida Handwriting, and Apple Chancery.

[`fantasy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#fantasy)

Fantasy fonts are primarily decorative fonts that contain playful representations of characters. Example fantasy fonts include Papyrus, Herculanum, Party LET, Curlz MT, Harrington, and Comic Sans MS.

[`system-ui`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#system-ui)

Glyphs are taken from the default user interface font on a given platform. Because typographic traditions vary widely across the world, this generic family is provided for typefaces that don't map cleanly into the others.

**Note:** As the name implies, `system-ui` is intended to make UI elements look like native apps, and not for typesetting large paragraphs of text. It may cause the displayed typeface to be undesirable for some users—for example, the default Windows CJK font may render Latin scripts poorly, and the `lang` attribute may not affect the displayed font. Some operating systems do not allow customizing `system-ui`, while browsers generally allow customizing the `sans-serif` font family. For large paragraphs, use `sans-serif` or some other non-UI font family instead.

[`ui-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#ui-serif)

The default user interface serif font. See the definition of `serif` above.

[`ui-sans-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#ui-sans-serif)

The default user interface sans-serif font. See the definition of `sans-serif` above.

[`ui-monospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#ui-monospace)

The default user interface monospace font. See the definition of `monospace` above.

[`ui-rounded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#ui-rounded)

The default user interface font that has rounded features.

[`math`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#math)

Fonts for displaying mathematical expressions, for example superscript and subscript, brackets that cross several lines, nesting expressions, and double-struck glyphs with distinct meanings.

[`fangsong`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#fangsong)

A particular style of Chinese characters that are between serif-style Song and cursive-style Kai forms. This style is often used for government documents.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#formal_syntax)

----------------------------------------------------------------------------------------------------------------

<generic-family> =   
  serif          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sans-serif     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  monospace      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  cursive        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fantasy        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  system-ui      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-serif       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-sans-serif  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-monospace   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-rounded     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  math           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fangsong         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#examples)

------------------------------------------------------------------------------------------------------

This example demos several of the `<generic-family>` enumerated values for the [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 property.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# generic-font-families](https://drafts.csswg.org/css-fonts/#generic-font-families) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family#see_also)

------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
     and [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   [CSS fonts module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/generic-family/index.md?plain=1 "Folder: en-us/web/css/reference/values/generic-family (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgeneric-family&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgeneric-family%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fgeneric-family%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fgeneric-family%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
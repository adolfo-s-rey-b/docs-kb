*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#mdn-search)
    

`<text-edge>` CSS type
======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/265)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<text-edge>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 defines keywords that specify font metrics representing specific regions on a font's block-start edge and block-end edge. Each keyword specifies a position of a font's over and/or under edge.

The `<text-edge>` values are used in the [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 property to specify an amount of space to trim from the block-start and block-end edge of a text element's block container.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#syntax)

---------------------------------------------------------------------------------------------

The `<text-edge>` data type is composed of one or two keywords representing specific regions on a font's block-start (over) edge and/or block-end (under) edge:

*   When one value is specified, the position of the font's over edge and under edge are specified using that same keyword.
*   When two values are specified, the first value specifies the position of the font's over edge, and the second value specifies the position of the font's under edge.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#values)

#### Single keyword values

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#text)

The font's over and under edges are its text-over baseline/text-under baseline: this includes the font's ascenders and descenders but excludes the [half-leading](https://developer.mozilla.org/en-US/docs/Glossary/Leading)
 set on the text.

**Note:** The amount of half-leading included on a text element can be controlled using the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 property.

**Note:** The `ideographic` and `ideographic-ink` keywords are intended to specify over and under edge positions specific to [CJK language characters](https://en.wikipedia.org/wiki/CJK_characters "External link (opens in new tab)")
. Currently their exact behavior is being debated and they are not supported by any browser.

#### Two keyword values

[`alphabetic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#alphabetic)

The font's under edge is its alphabetic baseline, which is the bottom of its short lower-case letters (for example, "m", "n", and "o") or capital letters.

[`cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#cap)

The font's over edge is its cap-height baseline, which is the top of its capital letters.

[`ex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#ex)

The font's over edge is its x-height baseline, which is the top of its short lower-case letters.

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#text_2)

The font's over edge is its text-over baseline (includes the font's ascenders but excludes the over edge half-leading), or its under edge is its text-under baseline (includes the font's descenders but excludes the under edge half-leading), depending on which edge the value is set for.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#formal_syntax)

-----------------------------------------------------------------------------------------------------------

<text-edge> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 cap [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ex [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 alphabetic [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#examples)

-------------------------------------------------------------------------------------------------

See [`text-box-edge` examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#examples)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# typedef-text-edge](https://drafts.csswg.org/css-inline-3/#typedef-text-edge) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge#see_also)

-------------------------------------------------------------------------------------------------

*   [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
    , [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    , [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
    
*   [CSS inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/text-edge/index.md?plain=1 "Folder: en-us/web/css/reference/values/text-edge (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftext-edge&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftext-edge%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftext-edge%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftext-edge%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#mdn-search)
    

`hanging-punctuation` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/302)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hanging-punctuation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether a punctuation mark should hang at the start or end of a line of text. Hanging punctuation may be placed outside the line box.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#syntax)

-----------------------------------------------------------------------------------------------------------

The `hanging-punctuation` property may be specified with one, two, or three space-separated values.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#none)

No character hangs.

[`first`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#first)

An opening bracket or quote at the start of the first formatted line of an element hangs. This applies to:

*   all characters in the Unicode categories [Ps](https://unicodeplus.com/category/Ps "External link (opens in new tab)")
    , [Pf](https://unicodeplus.com/category/Pf "External link (opens in new tab)")
    , [Pi](https://unicodeplus.com/category/Pi "External link (opens in new tab)")
    
*   the quote marks `U+0027` APOSTROPHE (`'`) and `U+0022` QUOTATION MARK (`"`).

[`last`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#last)

A closing bracket or quote at the end of the last formatted line of an element hangs. This applies to:

*   all characters in the Unicode categories [Pe](https://unicodeplus.com/category/Pe "External link (opens in new tab)")
    , [Pf](https://unicodeplus.com/category/Pf "External link (opens in new tab)")
    , [Pi](https://unicodeplus.com/category/Pi "External link (opens in new tab)")
    
*   the quote marks `U+0027` APOSTROPHE (`'`) and `U+0022` QUOTATION MARK (`"`).

[`allow-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#allow-end)

A stop or comma at the end of a line hangs if it does not otherwise fit prior to justification.

Stops and commas that are allowed to hang include:

*   `U+002C`, COMMA
*   `U+002E`, FULL STOP
*   `U+060C`, ARABIC COMMA
*   `U+06D4`, ARABIC FULL STOP
*   `U+3001`, IDEOGRAPHIC COMMA
*   `U+3002`, IDEOGRAPHIC FULL STOP
*   `U+FF0C`, FULLWIDTH COMMA
*   `U+FF0E`, FULLWIDTH FULL STOP
*   `U+FE50`, SMALL COMMA
*   `U+FE51`, SMALL IDEOGRAPHIC COMMA
*   `U+FE52`, SMALL FULL STOP
*   `U+FF61`, HALFWIDTH IDEOGRAPHIC FULL STOP
*   `U+FF64`, HALFWIDTH IDEOGRAPHIC COMMA

User agents may include additional characters.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

hanging-punctuation =   
  none                                            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 first [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 force-end [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 allow-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 last [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#examples)

---------------------------------------------------------------------------------------------------------------

### [Setting opening and closing quotes to hang](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#setting_opening_and_closing_quotes_to_hang)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# hanging-punctuation-property](https://drafts.csswg.org/css-text/#hanging-punctuation-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`text-indent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent)
    
*   [CSS Tricks: Hanging punctuation](https://css-tricks.com/almanac/properties/h/hanging-punctuation/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/hanging-punctuation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/hanging-punctuation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhanging-punctuation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhanging-punctuation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhanging-punctuation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhanging-punctuation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
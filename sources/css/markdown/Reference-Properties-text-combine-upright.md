*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#mdn-search)
    

`text-combine-upright` CSS property
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-combine-upright`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the combination of characters into the space of a single character. If the combined text is wider than 1em, the user agent must fit the contents within 1em. The resulting composition is treated as a single upright glyph for layout and decoration. This property only has an effect in vertical writing modes.

This is used to produce an effect that is known as tate-chū-yoko 縦中横 in Japanese, or as 橫向文字 in Chinese.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#try_it)

------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#syntax)

------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#none)

There is no special processing.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#all)

Attempts to typeset all consecutive characters within the box horizontally, such that they take up the space of a single character within the vertical line of the box.

**Note:** The [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
 module defines a `digits <integer>` value for the `text-combine-upright` property to display two to four consecutive [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 digits (U+0030–U+0039) such that it takes up the space of a single character within the vertical line box, however, this is not supported in any browsers.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | non-replaced inline elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | specified keyword, plus integer if 'digits' |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

text-combine-upright =   
  none                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 digits <integer \[2,4\]>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#examples)

----------------------------------------------------------------------------------------------------------------

### [Using 'all' with horizontal text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#using_all_with_horizontal_text)

The all value requires markup around every piece of horizontal text, but it is currently supported by more browsers than the digits value.

#### HTML

#### CSS

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4  <br>\# text-combine-upright](https://drafts.csswg.org/css-writing-modes/#text-combine-upright) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-combine-upright/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-combine-upright (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-combine-upright&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-combine-upright%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-combine-upright%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-combine-upright%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#mdn-search)
    

`text-emphasis-position` CSS property
=====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-emphasis-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets where emphasis marks are drawn. Similar to the text rendered by the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 HTML element, if there isn't enough room for emphasis marks, the line height is increased.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#try_it)

--------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#syntax)

--------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#values)

The property accepts one or two values:

*   If only one value is provided, it can be `auto`, `over`, or `under`. When only `over` or `under` is used, `right` is assumed as the default position.
*   If two values are provided, they must include one of `over` or `under` and one of `right` or `left`. Their order does not matter.

The values include:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#auto)

Draws marks over the text in horizontal writing mode and to the right of the text in vertical writing mode.

[`over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#over)

Draws marks over the text in horizontal writing mode.

[`under`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#under)

Draws marks under the text in horizontal writing mode.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#right)

Draws marks to the right of the text in vertical writing mode.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#left)

Draws marks to the left of the text in vertical writing mode.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#description)

------------------------------------------------------------------------------------------------------------------------

The preferred position of emphasis marks depends on the language. In Japanese for example, the preferred position is `over right`. In Chinese, on the other hand, the preferred position is `under right`. The informative table below summarizes the preferred emphasis mark positions for Chinese, Mongolian and Japanese:

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Preferred emphasis mark and ruby position
| Language | Preferred position |     | Illustration |     |
| --- | --- | --- | --- | --- |
| Horizontal | Vertical |
| --- | --- | --- | --- | --- |
| Japanese | over | right | ![Emphasis marks appear over each emphasized character in horizontal Japanese text.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position/text-emphasis-ja.png "Emphasis (shown in blue for clarity) applied above a fragment of Japanese text") | ![Emphasis marks appear on the right of each emphasized character in vertical Japanese text.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position/text-emphasis-v.gif "Emphasis applied on the right of a fragment of Japanese text") |
| Korean |
| Mongolian |
| Chinese | under | right | ![Emphasis marks appear below each emphasized character in horizontal Simplified Chinese text.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position/text-emphasis-zh.gif "Emphasis (shown in blue for clarity) applied below a fragment of Chinese text") |

**Note:** The `text-emphasis-position` cannot be set, and therefore are not reset either, using the [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
 shorthand property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

text-emphasis-position =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 over [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 under [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
   [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#examples)

------------------------------------------------------------------------------------------------------------------

### [Adding emphasis mark positions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#adding_emphasis_mark_positions)

Use the dropdown menu to change the position of the emphasis marks. This will change the class on the `<section>` element, which in turn, will update the position of the emphasis marks on the text.

#### HTML

#### CSS

#### Result

Use the "Emphasis position" dropdown to choose the location of the emphasis marks. The `preferred` option in the dropdown uses the preferred positions, as explained in the [Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#description)
 section.

### [Preferring ruby over emphasis marks](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#preferring_ruby_over_emphasis_marks)

Some editors prefer to hide emphasis marks when they conflict with ruby. In HTML, this can be done with the following style rule:

### [Preferring emphasis marks over ruby](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#preferring_emphasis_marks_over_ruby)

Some other editors prefer to hide ruby when they conflict with emphasis marks. In HTML, this can be done with the following pattern:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-emphasis-position-property](https://drafts.csswg.org/css-text-decor/#text-emphasis-position-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`text-underline-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
    
*   [`text-emphasis-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style)
    
*   [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    
*   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
     shorthand property
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 13, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-emphasis-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-emphasis-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-emphasis-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-emphasis-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-emphasis-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-emphasis-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F09a34cfd2a50cad3d6b520027cbab56f05d4d731%0A*+Document+last+modified%3A+2026-09-13T20%3A35%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
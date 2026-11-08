*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#mdn-search)
    

`font-synthesis` CSS property
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2022.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-synthesis`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property lets you specify whether or not the browser may synthesize the bold, italic, small-caps, and/or subscript and superscript typefaces when they are missing in the specified font-family.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#try_it)

------------------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [font-synthesis-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
    
*   [font-synthesis-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
    
*   [font-synthesis-small-caps](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
    
*   [font-synthesis-position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#none)

Indicates that no bold, italic, or small-caps typeface may be synthesized by the browser.

[`weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#weight)

Indicates that the missing bold typeface may be synthesized by the browser if needed.

[`style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#style)

Indicates that the italic typeface may be synthesized by the browser if needed.

[`small-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#small-caps)

Indicates that the small-caps typeface may be synthesized by the browser if needed.

[`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#position)

Indicates that the subscript and superscript typeface may be synthesized by the browser, if needed, when using [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#description)

----------------------------------------------------------------------------------------------------------------

Most standard Western fonts include italic and bold variants, and some fonts include a small-caps and subscript/superscript variants. However, many fonts do not. Fonts used for Chinese, Japanese, Korean and other logographic scripts tend not to include these variants and synthesizing them might impede the legibility or change the meaning of the text. In these cases, it may be desirable to switch off the browser's default font-synthesis.

For example, using the [:lang()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
 pseudo-class, you can disable the browser from synthesizing bold and oblique characters for a language, in this case Arabic:

The table below shows how a value of the shorthand `font-synthesis` property maps to the constituent longhand properties.

| font-synthesis value | [font-synthesis-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)<br> value | [font-synthesis-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)<br> value | [font-synthesis-small-caps](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)<br> value | [font-synthesis-position](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)<br> value |
| --- | --- | --- | --- | --- |
| `none` | `none` | `none` | `none` | `none` |
| `weight` | `auto` | `none` | `none` | `none` |
| `style` | `none` | `auto` | `none` | `none` |
| `small-caps` | `none` | `none` | `auto` | `none` |
| `position` | `none` | `none` | `none` | `auto` |
| `weight style` | `auto` | `auto` | `none` | `none` |
| `weight small-caps` | `auto` | `none` | `auto` | `none` |
| `weight position` | `auto` | `none` | `none` | `auto` |
| `style small-caps` | `none` | `auto` | `auto` | `none` |
| `style position` | `none` | `auto` | `none` | `auto` |
| `weight style small-caps` | `auto` | `auto` | `auto` | `none` |
| `weight style position` | `auto` | `auto` | `none` | `auto` |
| `weight small-caps position` | `auto` | `none` | `auto` | `auto` |
| `style small-caps position` | `none` | `auto` | `auto` | `auto` |
| `weight style small-caps position` | `auto` | `auto` | `auto` | `auto` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `weight style small-caps position` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

font-synthesis =   
  none                                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 weight [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 style [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 small-caps [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 position [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#examples)

----------------------------------------------------------------------------------------------------------

### [Disabling font synthesis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#disabling_font_synthesis)

This example shows the browser's default font-synthesis behavior and compares it with when the synthesis behavior is turned off. Notice that the example uses two imported fonts to demonstrate this behavior. You might not be able to replicate turning off of font-synthesis on fonts available on your operating system by default.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-synthesis](https://drafts.csswg.org/css-fonts/#font-synthesis) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis#see_also)

----------------------------------------------------------------------------------------------------------

*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-synthesis/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-synthesis (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-synthesis%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-synthesis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
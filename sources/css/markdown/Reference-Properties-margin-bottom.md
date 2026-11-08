*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#mdn-search)
    

`margin-bottom` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`margin-bottom`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the [margin area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#margin_area)
 on the bottom of an element. A positive value places it farther from its neighbors, while a negative value places it closer.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#try_it)

-----------------------------------------------------------------------------------------------------

![The effect of the CSS margin-bottom property on the element box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom/margin-bottom.svg)

This property has no effect on _non-[replaced](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
_ inline elements, such as [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 or [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#syntax)

-----------------------------------------------------------------------------------------------------

The `margin-bottom` property is specified as the keyword `auto`, or a `<length>`, or a `<percentage>`. Its value can be positive, zero, or negative.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the margin as a fixed value.

*   For _anchor-positioned elements_, the [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
     function resolves to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value relative to the associated _anchor element_'s width or height (see [Setting element margin based on anchor size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#setting_element_margin_based_on_anchor_size)
    ).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The size of the margin as a percentage, relative to the inline size (_width_ in a horizontal language, defined by [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
) of the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#auto)

The browser selects a suitable value to use. See [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements, except elements with table [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> types other than `table-caption`, `table` and `inline-table`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the percentage as specified or the absolute length |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

margin-bottom =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-size()>        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<anchor-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  anchor-size( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <anchor-name> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <anchor-size> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
  
[<anchor-size>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
 =   
  width        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  height       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self-inline    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#examples)

---------------------------------------------------------------------------------------------------------

### [Setting positive and negative bottom margins](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#setting_positive_and_negative_bottom_margins)

#### HTML

#### CSS

CSS for divs to set margin-bottom and height

Some definitions for container and divs so margins' effects can be seen more clearly

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Model Module Level 3  <br>\# margin-physical](https://drafts.csswg.org/css-box/#margin-physical) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom#see_also)

---------------------------------------------------------------------------------------------------------

*   [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , and [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
     shorthand
*   [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
    , [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
    , [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    , and [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    
*   [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
     and [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
     shorthands
*   [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/margin-bottom/index.md?plain=1 "Folder: en-us/web/css/reference/properties/margin-bottom (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-bottom&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-bottom%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmargin-bottom%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmargin-bottom%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
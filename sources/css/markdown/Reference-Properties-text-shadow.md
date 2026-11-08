*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#mdn-search)
    

`text-shadow` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-shadow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property adds shadows to text. It accepts a comma-separated list of shadows to be applied to the text and any of its [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
. Each shadow is described by some combination of X and Y offsets from the element, blur radius, and color.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#try_it)

---------------------------------------------------------------------------------------------------

    text-shadow: 1px 1px 2px pink;
    

    text-shadow: #ffcc00 1px 0 10px;
    

    text-shadow: 5px 5px #558abb;
    

    text-shadow: red 2px 5px;
    

    text-shadow: 5px 10px;
    

    text-shadow:
      1px 1px 2px red,
      0 0 1em blue,
      0 0 0.2em blue;
    

    <section id="default-example">
      <p id="example-element">
        Far out in the uncharted backwaters of the unfashionable end of the western
        spiral arm of the Galaxy...
      </p>
    </section>
    

    p {
      font:
        1.5em "Georgia",
        serif;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#syntax)

---------------------------------------------------------------------------------------------------

css

    /* offset-x | offset-y | blur-radius | color */
    text-shadow: 1px 1px 2px black;
    
    /* color | offset-x | offset-y | blur-radius */
    text-shadow: #ffcc00 1px 0 10px;
    
    /* offset-x | offset-y | color */
    text-shadow: 5px 5px #558abb;
    
    /* color | offset-x | offset-y */
    text-shadow: white 2px 5px;
    
    /* offset-x | offset-y
    /* Use defaults for color and blur-radius */
    text-shadow: 5px 10px;
    
    /* Global values */
    text-shadow: inherit;
    text-shadow: initial;
    text-shadow: revert;
    text-shadow: revert-layer;
    text-shadow: unset;
    

This property is specified as a comma-separated list of shadows.

Each shadow is specified as two or three `<length>` values, followed optionally by a `<color>` value. The first two `<length>` values are the `<offset-x>` and `<offset-y>` values. The third, optional, `<length>` value is the `<blur-radius>`. The `<color>` value is the shadow's color.

When more than one shadow is given, shadows are applied front-to-back, with the first-specified shadow on top.

This property applies to both [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
 and [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
 [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#values)

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

Optional. The color of the shadow. It can be specified either before or after the offset values. If unspecified, the color's value is left up to the user agent, so when consistency across browsers is desired you should define it explicitly.

[`<offset-x> <offset-y>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#offset-x_offset-y)

Required. These [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values specify the shadow's distance from the text. `<offset-x>` specifies the horizontal distance; a negative value places the shadow to the left of the text. `<offset-y>` specifies the vertical distance; a negative value places the shadow above the text. If both values are `0`, the shadow is placed directly behind the text, although it may be partly visible due to the effect of `<blur-radius>`.

[`<blur-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#blur-radius)

Optional. This is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value. The higher the value, the bigger the blur; the shadow becomes wider and lighter. If not specified, it defaults to `0`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | a color plus three absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [shadow list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#interpolation "The color, x, y, blur and spread (if applicable) components of shadow lists are interpolated independently. If the inset value of any shadow pair differs between both lists, the whole list is uninterpolable. If one list is smaller than the other, it gets padded with transparent shadows with all their lengths set to 0 and its inset value matching the longer list.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

text-shadow =   
  none       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <shadow>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<shadow> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                                       [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  inset[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                                           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#examples)

-------------------------------------------------------------------------------------------------------

### [Basic shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#basic_shadow)

css

    .red-text-shadow {
      text-shadow: red 0 -2px;
    }
    

html

    <p class="red-text-shadow">
      Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
      doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.
    </p>
    

### [Multiple shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#multiple_shadows)

css

    .white-text-with-blue-shadow {
      text-shadow:
        1px 1px 2px black,
        0 0 1em blue,
        0 0 0.2em blue;
      color: white;
      font:
        1.5em "Georgia",
        serif;
    }
    

html

    <p class="white-text-with-blue-shadow">
      Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
      doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.
    </p>
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-shadow-property](https://drafts.csswg.org/css-text-decor/#text-shadow-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow#see_also)

-------------------------------------------------------------------------------------------------------

*   [Introduction to text shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
    
*   [CSS text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-shadow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-shadow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-shadow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-shadow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-shadow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-shadow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
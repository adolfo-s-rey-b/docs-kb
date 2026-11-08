*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#mdn-search)
    

`box-shadow` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`box-shadow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property adds shadow effects around an element's frame. You can set multiple effects separated by commas. A box shadow is described by X and Y offsets relative to the element, blur and spread radius, and color.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#try_it)

--------------------------------------------------------------------------------------------------

    box-shadow: 10px 5px 5px red;
    

    box-shadow: 60px -16px teal;
    

    box-shadow: 12px 12px 2px 1px rgb(0 0 255 / 0.2);
    

    box-shadow: inset 5em 1em gold;
    

    box-shadow:
      3px 3px red,
      -1em 0 0.4em olive;
    

    <section id="default-example">
      <div class="transition-all" id="example-element">
        <p>This is a box with a box-shadow around it.</p>
      </div>
    </section>
    

    #example-element {
      margin: 20px auto;
      padding: 0;
      border: 2px solid #333333;
      width: 80%;
      text-align: center;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    box-shadow: none;
    
    /* A color and two length values */
    box-shadow: red 60px -16px;
    
    /* Three length values and a color */
    box-shadow: 10px 5px 5px black;
    
    /* Four length values and a color */
    box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 20%);
    
    /* inset, length values, and a color */
    box-shadow: inset 5em 1em gold;
    
    /* Multiple shadows, separated by commas */
    box-shadow:
      3px 3px red inset,
      -1em 0 0.4em olive;
    
    /* Global values */
    box-shadow: inherit;
    box-shadow: initial;
    box-shadow: revert;
    box-shadow: revert-layer;
    box-shadow: unset;
    

Specify a single box-shadow using:

*   Two, three, or four [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     values.
    
    *   If only two values are given, they are interpreted as `<offset-x>` and `<offset-y>` values.
    *   If a third value is given, it is interpreted as a `<blur-radius>`.
    *   If a fourth value is given, it is interpreted as a `<spread-radius>`.
*   Optionally, the `inset` keyword.
    
*   Optionally, a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#color)
     value.
    

To specify multiple shadows, provide a comma-separated list of shadows.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#values)

[`<color>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#color)

Specifies color for the shadow. See [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values for possible keywords and notations. If not specified, the value of the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property defined in the parent element is used.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#length)

Specifies the offset length of the shadow. This parameter accepts two, three, or four values. Third and fourth values are optional. They are interpreted as follows:

*   If two values are specified, they are interpreted as `<offset-x>` (horizontal offset) and `<offset-y>` (vertical offset) values. Negative `<offset-x>` value places the shadow to the left of the element. Negative `<offset-y>` value places the shadow above the element.  
    If not specified, the value of `0` is used for the missing length. If both `<offset-x>` and `<offset-y>` are set to `0`, the shadow is placed behind the element (and may generate a blur effect if `<blur-radius>` and/or `<spread-radius>` is set).
    
*   If three values are specified, the third value is interpreted as `<blur-radius>`. The larger this value, the bigger the blur, so the shadow becomes bigger and lighter. Negative values are not allowed. If not specified, it will be set to `0` (meaning that the shadow's edge will be sharp). The specification does not include an exact algorithm for how the blur radius should be calculated; however, it does elaborate as follows:
    
    > …for a long, straight shadow edge, this should create a color transition the length of the blur distance that is perpendicular to and centered on the shadow's edge, and that ranges from the full shadow color at the radius endpoint inside the shadow to fully transparent at the endpoint outside it.
    
*   If four values are specified, the fourth value is interpreted as `<spread-radius>`. Positive values will cause the shadow to expand and grow bigger, negative values will cause the shadow to shrink. If not specified, it will be set to `0` (that is, the shadow will be the same size as the element).
    

[`inset` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#inset)

Changes the shadow from an outer box-shadow to an inner box-shadow (as if the content is pressed into the box). Inset shadows are clipped to the element's padding box and appear above the background but below the content. By default, the shadow behaves like a drop shadow, giving the appearance that the box is elevated above its content. This is the default behavior when `inset` is not specified.

### [Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#interpolation)

When animating shadows, such as when multiple shadow values on a box transition to new values on hover, the values are interpolated. [Interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 determines intermediate values of properties, such as the blur radius, spread radius, and color, as shadows transition. For each shadow in a list of shadows, the color, x, y, blur, and spread transition; the color as [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
, and the other values as [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
s.

In interpolating multiple shadows between two comma-separated lists of multiple box shadows, the shadows are paired, in order, with interpolation occurring between paired shadows. If the lists of shadows have different lengths, then the shorter list is padded at the end with shadows whose color is `transparent`, and X, Y, and blur are `0`, with the inset, or lack of inset, being set to match. If in any pair of shadows, one has `inset` set and the other does not, the entire shadow list is uninterpolated; the shadows will change to the new values without an animating effect.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#description)

------------------------------------------------------------------------------------------------------------

The `box-shadow` property enables you to cast a drop shadow from the frame of almost any element. If a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 is specified on the element with a box shadow, the box shadow takes on the same rounded corners. The z-ordering of multiple box shadows is the same as multiple [text shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
 (the first specified shadow is on top).

[Box-shadow generator](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Box-shadow_generator)
 is an interactive tool allowing you to generate a `box-shadow`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | any length made absolute; any specified color computed; otherwise as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [shadow list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#interpolation "The color, x, y, blur and spread (if applicable) components of shadow lists are interpolated independently. If the inset value of any shadow pair differs between both lists, the whole list is uninterpolable. If one list is smaller than the other, it gets padded with transparent shadows with all their lengths set to 0 and its inset value matching the longer list.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#formal_syntax)

----------------------------------------------------------------------------------------------------------------

box-shadow =   
  <spread-shadow>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<spread-shadow> =   
  <'box-shadow-color'>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                               [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <'box-shadow-blur'> <'box-shadow-spread'>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  <'box-shadow-position'>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
                              
  
<box-shadow-color> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<box-shadow-blur> =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<box-shadow-spread> =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<box-shadow-position> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 outset [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inset [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#examples)

------------------------------------------------------------------------------------------------------

### [Setting three shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#setting_three_shadows)

In this example, we include three shadows: an inset shadow, a regular drop shadow, and a 2px shadow that creates a border effect (we could have used an [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 instead for that third shadow).

#### HTML

html

    <blockquote>
      <q>
        You may shoot me with your words,<br />
        You may cut me with your eyes,<br />
        You may kill me with your hatefulness,<br />
        But still, like air, I'll rise.
      </q>
      <p>&mdash; Maya Angelou</p>
    </blockquote>
    

#### CSS

css

    blockquote {
      padding: 20px;
      box-shadow:
        inset 0 -3em 3em rgb(0 200 0 / 30%),
        0 0 0 2px white,
        0.3em 0.3em 1em rgb(200 0 0 / 60%);
    }
    

#### Result

### [Setting zero for offset and blur](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#setting_zero_for_offset_and_blur)

When the `x-offset`, `y-offset`, and `blur` are all zero, the box shadow will be a solid-colored outline of equal-size on all sides. The shadows are drawn back to front, so the first shadow sits on top of subsequent shadows. When the `border-radius` is set to 0, as is the default, the corners of the shadow will be, well, corners. Had we put in a `border-radius` of any other value, the corners would have been rounded.

We added a margin the size of the widest box-shadow to ensure the shadow doesn't overlap adjacent elements or go beyond the border of the containing box. A box-shadow does not impact [box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 dimensions.

#### HTML

html

    <div><p>Hello World</p></div>
    

#### CSS

css

    p {
      box-shadow:
        0 0 0 2em #f4aab9,
        0 0 0 4em #66ccff;
      margin: 4em;
      padding: 1em;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# propdef-box-shadow](https://drafts.csswg.org/css-backgrounds/#propdef-box-shadow) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow#see_also)

------------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
    
*   [Introduction to text shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows)
    
*   [Applying color to HTML elements using CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-shadow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-shadow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-shadow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-shadow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-shadow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-shadow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
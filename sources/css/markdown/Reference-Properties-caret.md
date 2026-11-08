*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#mdn-search)
    

`caret` CSS property
====================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#browser_compatibility)
 carefully before using this in production.

The **`caret`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the appearance and behavior of the **insertion caret** in a single declaration.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#try_it)

---------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    
*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    
*   [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#syntax)

---------------------------------------------------------------------------------------------

The `caret` property is specified as one, two, or three values from the constituent properties. Values can be specified in any order, and omitted values are set to their initial values.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#values)

[`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)

Sets the color of the caret.

[`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)

Controls whether the caret blinks.

[`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)

Sets the visual shape of the caret.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#description)

-------------------------------------------------------------------------------------------------------

The `caret` shorthand allows you to set multiple caret properties in a single declaration, making it convenient to customize the complete appearance and behavior of the insertion caret.

### [Value resolution](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#value_resolution)

When values are omitted from the shorthand, they reset to their initial values:

*   `caret-color`: `auto` (resolves to `currentColor`).
*   `caret-animation`: `auto` (caret blinks).
*   `caret-shape`: `auto` (browser-determined shape).

### [Order independence](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#order_independence)

Unlike some CSS shorthands, the `caret` property accepts values in any order. The browser determines which value applies to which property based on the value type:

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     values apply to `caret-color`.
*   `auto`/`manual` keywords apply to `caret-animation`.
*   Shape keywords (`bar`, `block`, `underscore`) apply to `caret-shape`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)<br>    : `auto`<br>*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)<br>    : `auto`<br>*   [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)<br>    : `auto` |
| Applies to | Text or elements that accept text input |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)<br>    : `auto` is computed as specified and `<color>` values are computed as defined for the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)<br>     property.<br>*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)<br>    : as specified<br>*   [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.")<br>    <br>*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)<br>    : discrete<br>*   [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#formal_syntax)

-----------------------------------------------------------------------------------------------------------

caret =   
  [<'caret-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
      [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'caret-animation'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'caret-shape'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
        
  
[<caret-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 =   
  auto                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<caret-animation>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
 =   
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  manual    
  
[<caret-shape>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
 =   
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bar         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  underscore    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#examples)

-------------------------------------------------------------------------------------------------

### [Retro terminal with animated caret](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#retro_terminal_with_animated_caret)

This example creates a vintage terminal interface using the `caret` shorthand to combine multiple caret properties, demonstrating how it replaces older border-based techniques.

The main advantage of the `caret` shorthand is combining multiple properties in one declaration. Here we set the shape to `block`, disable default blinking, and set the color to `green`, all in a single line.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-caret-shape](https://drafts.csswg.org/css-ui/#propdef-caret-shape) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-shape-underscore](https://drafts.csswg.org/css-ui/#valdef-caret-shape-underscore) |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-caret-animation](https://drafts.csswg.org/css-ui/#propdef-caret-animation) |
| [CSS Basic User Interface Module Level 4  <br>\# caret-color](https://drafts.csswg.org/css-ui/#caret-color) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-shape-auto](https://drafts.csswg.org/css-ui/#valdef-caret-shape-auto) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-animation-manual](https://drafts.csswg.org/css-ui/#valdef-caret-animation-manual) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-shape-block](https://drafts.csswg.org/css-ui/#valdef-caret-shape-block) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-shape-bar](https://drafts.csswg.org/css-ui/#valdef-caret-shape-bar) |
| [CSS Basic User Interface Module Level 4  <br>\# valdef-caret-animation-auto](https://drafts.csswg.org/css-ui/#valdef-caret-animation-auto) |
| [CSS Color Module Level 4  <br>\# valdef-color-currentcolor](https://drafts.csswg.org/css-color-4/#valdef-color-currentcolor) |
| [CSS Color Module Level 4  <br>\# valdef-color-transparent](https://drafts.csswg.org/css-color-4/#valdef-color-transparent) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret#see_also)

-------------------------------------------------------------------------------------------------

*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    , [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/caret/index.md?plain=1 "Folder: en-us/web/css/reference/properties/caret (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
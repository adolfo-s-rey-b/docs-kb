*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#mdn-search)
    

`outline` CSS property
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`outline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the style, color, and width of an element's outline.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#try_it)

-----------------------------------------------------------------------------------------------

    outline: solid;
    

    outline: dashed red;
    

    outline: 1rem solid;
    

    outline: thick double #32a1ce;
    

    outline: 8px ridge rgb(170 50 220 / 0.6);
    border-radius: 2rem;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with an outline around it.
      </div>
    </section>
    

    #example-element {
      padding: 0.75rem;
      width: 80%;
      height: 100px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#syntax)

-----------------------------------------------------------------------------------------------

css

    /* style */
    outline: solid;
    
    /* style | color */
    outline: dashed #ff6666;
    
    /* width | style */
    outline: thick inset;
    
    /* width | style | color*/
    outline: 3px solid green;
    
    /* Global values */
    outline: inherit;
    outline: initial;
    outline: revert;
    outline: revert-layer;
    outline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#values)

This property is specified as one, two, or three values from the following list:

[`<'outline-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#outline-width)

A [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 value setting the thickness of the outline. Defaults to `medium` if absent. See [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
.

[`<'outline-style'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#outline-style)

Sets the style of the outline. Defaults to `none` if absent. See [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
.

[`<'outline-color'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#outline-color)

Sets the color of the outline. Defaults to `invert` for browsers supporting it, `currentColor` for the others. See [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#description)

---------------------------------------------------------------------------------------------------------

The `outline` shorthand property sets the style, color, and width of an element's outline. It can be specified using one, two, or three values. The order of the values does not matter. Any omitted sub-values are set to their [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
.

The outline will be invisible for many elements if its style is not defined. This is because the style defaults to `none`. A notable exception is `input` elements, which are given default styling by browsers.

Outline is a line outside of the element's [border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
. Unlike other areas of the box, outlines don't take up space, so they don't affect the layout of the document in any way.

There are a few properties that affect an outline's appearance. It is possible to change the style, color, and width using the `outline` property, the distance from the border using the [`outline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
 property, and corner angles using the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 property.

An outline is not required to be rectangular: While dealing with multiline text, some browsers will draw an outline for each line box separately, while others will wrap the whole text with a single outline.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#accessibility)

-------------------------------------------------------------------------------------------------------------

Assigning `outline` a value of `0` or `none` will remove the browser's default focus style. If an element can be interacted with it must have a visible focus indicator. Provide obvious focus styling if the default focus style is removed.

*   [How to Design Useful and Usable Focus Indicators](https://www.deque.com/blog/give-site-focus-tips-designing-usable-focus-indicators/ "External link (opens in new tab)")
    
*   WCAG 2.1: [Understanding Success Criterion 2.4.7: Focus Visible](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)<br>    : `medium`<br>*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)<br>    : `none`<br>*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)<br>    : `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)<br>    : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>    , snapped as a line width<br>*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)<br>    : as specified<br>*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)<br>    : For the keyword `auto`, the computed value is `currentcolor`. For the color value, if the value is translucent, the computed value will be the `rgba()` corresponding one. If it isn't, it will be the `rgb()` corresponding one. The `transparent` keyword maps to `rgba(0,0,0,0)`. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)<br>    : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>    <br>*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)<br>    : by computed value type<br>*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)<br>    : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#formal_syntax)

-------------------------------------------------------------------------------------------------------------

outline =   
  [<'outline-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'outline-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'outline-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
  
[<outline-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
 =   
  <line-width>    
  
[<outline-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
 =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <outline-line-style>    
  
[<outline-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
 =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'border-top-color'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             
  
<outline-line-style> =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    
  
[<border-top-color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
 =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-1D>    
  
<image-1D> =   
  <stripes()>    
  
<stripes()> =   
  stripes( <color-stripe>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<color-stripe> =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
                            [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<flex>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#examples)

---------------------------------------------------------------------------------------------------

### [Using outline to set a focus style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#using_outline_to_set_a_focus_style)

#### HTML

html

    <a href="#">This link has a special focus style.</a>
    

#### CSS

css

    a {
      border: 1px solid;
      border-radius: 3px;
      display: inline-block;
      margin: 10px;
      padding: 5px;
    }
    
    a:focus {
      outline: 4px dotted #ee7733;
      outline-offset: 4px;
      background: #ffffaa;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# outline](https://drafts.csswg.org/css-ui/#outline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline#see_also)

---------------------------------------------------------------------------------------------------

*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/outline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/outline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1cf7346516383565b51a125c064ae3d5d893526%0A*+Document+last+modified%3A+2026-09-14T09%3A37%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
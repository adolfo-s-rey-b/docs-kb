*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#mdn-search)
    

`border` CSS property
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets an element's border. It sets the values of [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
, [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
, and [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#try_it)

----------------------------------------------------------------------------------------------

    border: solid;
    

    border: dashed red;
    

    border: 1rem solid;
    

    border: thick double #32a1ce;
    

    border: 4mm ridge rgb(211 220 50 / 0.6);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with a border around it.
      </div>
    </section>
    

    #example-element {
      background-color: #eeeeee;
      color: darkmagenta;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    
*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    

### [Reset-only sub-properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#reset-only_sub-properties)

This property resets the following CSS properties to their initial values:

*   [`border-image-outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
    
*   [`border-image-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
    
*   [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
    
*   [`border-image-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
    
*   [`border-image-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#syntax)

----------------------------------------------------------------------------------------------

css

    /* style */
    border: solid;
    
    /* width | style */
    border: 2px dotted;
    
    /* style | color */
    border: outset #ff3333;
    
    /* width | style | color */
    border: medium dashed green;
    
    /* Global values */
    border: inherit;
    border: initial;
    border: revert;
    border: revert-layer;
    border: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#values)

This property is specified as a space-separated list of one to three of the following values:

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#line-width)

Sets the thickness of the border. Defaults to `medium` if absent. See [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
.

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)

Sets the style of the border. Defaults to `none` if absent. See [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

Sets the color of the border. Defaults to `currentColor` if absent. See [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#description)

--------------------------------------------------------------------------------------------------------

The `border` shorthand property sets the width, style, and color of all four sides of an element's border. It is specified using one, two, or all three of the component property values, in any order.

Any omitted sub-values are set to their [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
. For a border to be displayed, the `<line-style>` component must be set because the style defaults to `none`.

Importantly, `border` cannot be used to specify a custom value for [`border-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
, but instead sets it to its initial value, i.e., `none`.

The `border` shorthand is especially useful when you want all four borders to be the same. To make them different from each other, however, you can use the longhand [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
, [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
, and [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 properties, which accept different values for each side. Alternatively, you can target one border at a time with the physical (e.g., [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
 ) and logical (e.g., [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
) border properties.

### [Borders vs. outlines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#borders_vs._outlines)

Borders and [outlines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 are very similar. However, outlines differ from borders in the following ways:

*   Outlines never take up space, as they are drawn outside of an element's content.
*   According to the spec, outlines don't have to be rectangular, although they usually are.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#formal_definition)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)<br>        : `medium`<br>    *   [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)<br>        : `medium`<br>    *   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>        : `medium`<br>    *   [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)<br>        : `medium`<br>*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)<br>        : `none`<br>    *   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)<br>        : `none`<br>    *   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>        : `none`<br>    *   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)<br>        : `none`<br>*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)<br>        : `currentcolor`<br>    *   [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)<br>        : `currentcolor`<br>    *   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>        : `currentcolor`<br>    *   [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)<br>        : `currentcolor` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>    *   [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>    *   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>    *   [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)<br>        : the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>        , snapped as a line width<br>*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)<br>        : as specified<br>    *   [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)<br>        : as specified<br>    *   [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)<br>        : as specified<br>    *   [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)<br>        : as specified<br>*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)<br>        : computed color<br>    *   [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)<br>        : computed color<br>    *   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>        : computed color<br>    *   [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)<br>        : computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)<br>        : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>        <br>    *   [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)<br>        : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>        <br>    *   [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)<br>        : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>        <br>    *   [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)<br>        : a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>        <br>*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)<br>    : discrete<br>*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)<br>    : as each of the properties of the shorthand:  <br>    *   [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)<br>        : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.")<br>        <br>    *   [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)<br>        : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.")<br>        <br>    *   [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)<br>        : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.")<br>        <br>    *   [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)<br>        : a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#formal_syntax)

------------------------------------------------------------------------------------------------------------

border =   
  <line-width>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <line-style>  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
         
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#examples)

--------------------------------------------------------------------------------------------------

### [Setting a pink outset border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#setting_a_pink_outset_border)

#### HTML

html

    <div>I have a border, an outline, and a box shadow! Amazing, isn't it?</div>
    

#### CSS

css

    div {
      border: 0.5rem outset pink;
      outline: 0.5rem solid khaki;
      box-shadow: 0 0 0 2rem skyblue;
      border-radius: 12px;
      font: bold 1rem sans-serif;
      margin: 2rem;
      padding: 1rem;
      outline-offset: 0.5rem;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# propdef-border](https://drafts.csswg.org/css-backgrounds/#propdef-border) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#see_also)

--------------------------------------------------------------------------------------------------

*   [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    
*   [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
    
*   [Learn CSS: Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3f221b9845703eb21db70cdc321f843d5c1c072b%0A*+Document+last+modified%3A+2026-09-17T10%3A50%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
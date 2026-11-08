*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#mdn-search)
    

`perspective` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`perspective`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property determines the distance between the z=0 plane and the user in order to give a 3D-positioned element some perspective.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#try_it)

---------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#none)

Indicates that no perspective transform is to be applied.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#length)

A [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 giving the distance from the user to the z=0 plane. It is used to apply a perspective transform to the children of the element. Negative values are syntax errors. If the value is smaller than `1px`, it is clamped to `1px`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#description)

-------------------------------------------------------------------------------------------------------------

Each 3D element with z>0 becomes larger; each 3D-element with z<0 becomes smaller. The strength of the effect is determined by the value of this property. Large values of `perspective` cause a small transformation; small values of `perspective` cause a large transformation.

The parts of the 3D elements that are behind the user — i.e., their z-axis coordinates are greater than the value of the `perspective` CSS property — are not drawn.

The _vanishing point_ is by default placed at the center of the element, but its position can be changed using the [`perspective-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective-origin)
 property.

Using this property with a value other than `none` creates a new [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
. Also, in that case, the object will act as a containing block for `position: fixed` elements that it contains.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the absolute length or `none` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

perspective =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#examples)

-------------------------------------------------------------------------------------------------------

### [Setting perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#setting_perspective)

An example showing how a cube varies if the `perspective` is set at different positions is given in [Using CSS transforms > Setting perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#setting_perspective)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# perspective-property](https://drafts.csswg.org/css-transforms-2/#perspective-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective#see_also)

-------------------------------------------------------------------------------------------------------

*   [Using CSS Transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/perspective/index.md?plain=1 "Folder: en-us/web/css/reference/properties/perspective (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fperspective&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fperspective%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fperspective%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fperspective%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
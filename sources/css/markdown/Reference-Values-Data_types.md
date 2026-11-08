*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#mdn-search)
    

CSS data types
==============

**CSS data types** define typical values (including keywords and units) accepted by CSS properties and functions. They are a special kind of [component value type](https://drafts.csswg.org/css-values/#component-types "External link (opens in new tab)")
.

The most commonly-used types are defined in the [CSS Values and Units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
 module. This module also defines [functional notations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
, which allow for more complex types or processing. Other types are defined in the specifications to which they apply.

Below you will find a reference to the types that you are most likely to come across, however it is not a comprehensive reference for all types defined in every CSS specification.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#syntax)

----------------------------------------------------------------------------------------------

In formal CSS syntax, data types are denoted by a keyword placed between the angle brackets `<` and `>`. They don't correspond to any tangible CSS code entity.

[Textual data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#textual_data_types)

----------------------------------------------------------------------------------------------------------------------

These types include keywords and identifiers as well as strings, and URLs.

[Pre-defined keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#pre-defined_keywords)

Keywords with a pre-defined meaning, for example, the value of `collapse` for the [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 property.

[CSS-wide keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)

All properties, including custom properties, accept the CSS-wide keywords:

[`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)

The value specified as the property's initial value.

[`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)

The computed value of the property on the element's parent.

[`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)

Rolls back the cascade to the value of the earlier origin.

[`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)

Rolls back the cascade to the value of the earlier [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
.

[`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)

Rolls back the cascade to the value of an earlier matching style rule.

[`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)

Acts as `inherit` or `initial` depending on whether the property is inherited or not.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

A user-defined identifier, for example the name assigned using the [`grid-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
 property.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

A `<custom-ident>` with the additional restriction that it must start with two dashes, for example, with [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

A quoted string, such as used for a value of the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property.

[`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)

A pointer to a resource, for example as the value of [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
.

[Numeric data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#numeric_data_types)

----------------------------------------------------------------------------------------------------------------------

These data types are used to indicate quantities, indexes, and positions. The majority of these are defined in the CSS values and units module, however additional types are described in other modules where they are specific to that specification alone — for example the `fr` unit in the [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 module.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

One or more decimal units 0 through 9, optionally preceded by `-` or `+`.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

Real numbers which may also have a fractional component, for example `1` or `1.34`.

[`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)

A number with a unit attached to it, for example `90deg`, `50ms`, or `15em`. This type includes distances ([`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
), durations ([`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
), frequencies ([`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
), resolutions ([`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
), and other quantities.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

A number with a percentage sign attached to it, for example `10%`.

[`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)

A ratio, written with the syntax `<number> / <number>`.

[`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)

A flexible length introduced for [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
, written as a `<number>` with the `fr` unit attached and used for grid track sizing.

[Quantities](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#quantities)

------------------------------------------------------------------------------------------------------

These [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
 types are used to specify distance and other quantities.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Lengths are a `<dimension>` and refer to distances.

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

Angles are used in properties such as [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 and are a `<dimension>` with one of `deg`, `grad`, `rad`, or `turn` units attached.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

Duration units are a `<dimension>` with an `s` or `ms` unit.

[`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)

Frequencies are a `<dimension>` with a `Hz` or `kHz` unit attached.

[`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)

Is a `<dimension>` with a unit identifier of `dpi`, `dpcm`, `dppx`, or `x`.

[Combinations of types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#combinations_of_types)

----------------------------------------------------------------------------------------------------------------------------

Some CSS properties can take a [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value. In this case the percentage value will be resolved to a quantity that matches the allowable dimension. Properties which can accept a percentage in addition to a dimension will use one of the types listed below.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

A type that can accept a length or a percentage as a value.

[`<frequency-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage)

A type that can accept a frequency or a percentage as a value.

[`<angle-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle-percentage)

A type that can accept an angle or a percentage as a value.

[`<time-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage)

A type that can accept a time or a percentage as a value.

[Color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#color)

--------------------------------------------------------------------------------------------

The [CSS color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
 module defines the [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 data type, and other types which relate to color in CSS.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

Specified as a keyword or a numerical color value.

[`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)

Specifies the transparency of a color. May be a `<number>`, in which case 0 is fully transparent and 1 is fully opaque, or a `<percentage>`, in which case 0% is fully transparent and 100% fully opaque.

[`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)

Specifies the `<angle>`, with a unit identifier of `deg`, `grad`, `rad`, or `turn`, or unitless `<number>` interpreted as `deg`, of the [color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
 specific to the `<absolute-color-functions>` of which it is a component.

[Images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#images)

----------------------------------------------------------------------------------------------

The [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
 module defines the data types which deal with images, including gradients.

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)

A URL reference to an image or a color gradient.

[`<color-stop-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#color-stop-list)

A list of two or more color stops with optional transition information using a color hint.

[`<linear-color-stop>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#linear-color-stop)

A `<color>` and a `<length-percentage>` to indicate the color stop for this part of the gradient.

[`<linear-color-hint>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#linear-color-hint)

A `<length-percentage>` to indicate how the color interpolates.

[`<ending-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#ending-shape)

Used for radial gradients; can have a keyword value of `circle` or `ellipse`.

[`<size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#size)

Determines the size of the radial gradient's ending shape. This accepts a value of a keyword or a `<length>` but not a percentage.

[2D positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#2d_positioning)

--------------------------------------------------------------------------------------------------------------

The [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 data type is interpreted as defined for the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 property.

[`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)

Defines the position of an object area. Accepts a keyword value such as `top` or `left`, or a `<length-percentage>`.

[Calculation data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#calculation_data_types)

------------------------------------------------------------------------------------------------------------------------------

These data types are used in [CSS math function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
 calculations.

[`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)

A calculation which is a sequence of calculation values interspersed with addition (`+`) and subtraction (`-`) operators. This data type requires both values to have units.

`<calc-product>`

A calculation which is a sequence of calculation values interspersed with multiplication (`*`) and division (`/`) operators. When multiplying, one value must be unitless. When dividing, the second value must be unitless.

`<calc-value>`

Defines accepted values for calculations, values such as [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, [`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 or nested [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 calculations.

[`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)

Defines a number of CSS keywords representing numeric constants such as `e` and `π`, that can be used in CSS math functions.

[Shape data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#shape_data_types)

------------------------------------------------------------------------------------------------------------------

The [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
 and [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
 modules define shape data types:

[`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)

Describes shape functions used in the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
, [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
, and [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 properties.

[`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)

Describes the shape of a container corner. It is used by the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 shorthand property and its [constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#constituent_properties)
 to specify the shape applied to affected container corners.

[Alphabetical index of data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#alphabetical_index_of_data_types)

--------------------------------------------------------------------------------------------------------------------------------------------------

*   [`<absolute-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
    
*   [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
    
*   [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    
*   [`<angle-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle-percentage)
    
*   [`<axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
    
*   [`<baseline-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    
*   [`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
    
*   [`<box-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge)
    
*   [`<calc-keyword>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
    
*   [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<color-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
    
*   [`<content-distribution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    
*   [`<content-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    
*   [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
    
*   [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
*   [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
    
*   [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
*   [`<dimension>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
    
*   [`<display-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
    
*   [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
    
*   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
    
*   [`<display-legacy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
    
*   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
    
*   [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
    
*   [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
    
*   [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    
*   [`<flex>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
    
*   [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    
*   [`<frequency-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage)
    
*   [`<generic-family>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
    
*   [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
    
*   [`<hue-interpolation-method>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
    
*   [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
    
*   [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    
*   [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    
*   [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
    
*   [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
    
*   [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
    
*   [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    
*   [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
    
*   [`<overflow-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
    
*   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
*   [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
    
*   [`<position-area>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
    
*   [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
    
*   [`<relative-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size)
    
*   [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    
*   [`<self-position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
    
*   [`<shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape)
    
*   [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
*   [`<system-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
    
*   [`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    
*   [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
    
*   [`<time-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4](https://drafts.csswg.org/css-values/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#see_also)

--------------------------------------------------------------------------------------------------

*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [Learn: Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    
*   [CSS functional notation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/data_types/index.md?plain=1 "Folder: en-us/web/css/reference/values/data_types (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2FData_types&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdata_types%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2FData_types%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdata_types%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9c03ba87f9ff4123150d8f7dc457bd546bdab83%0A*+Document+last+modified%3A+2026-07-24T10%3A23%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
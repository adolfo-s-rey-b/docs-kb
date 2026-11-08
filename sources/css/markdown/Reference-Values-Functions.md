*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#mdn-search)
    

CSS value functions
===================

**CSS value functions** are statements that invoke special data processing or calculations to return a [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
 for a CSS property. CSS value functions represent more complex [data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 and they may take some input arguments to calculate the return value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#syntax)

---------------------------------------------------------------------------------------------

selector {
  property: function(\[argument\]? \[, argument\]!);
}

The value syntax starts with the **name of the function**, followed by a left parenthesis `(`. Next up are the argument(s), and the function is finished off with a closing parenthesis `)`.

Functions can take multiple arguments, which are formatted similarly to CSS property values. Whitespace is allowed, but they are optional inside the parentheses. In some functional notations multiple arguments are separated by commas, while others use spaces.

**Note:** The CSS value functions are used as property values and should not be confused with pseudo-classes. The [functional pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#functional_pseudo-classes)
, [linguistic pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#linguistic_pseudo-classes)
, and several [tree-structural pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#tree-structural_pseudo-classes)
 require parameter values, but they're not value functions. The conditional at-rules are also not value functions; the parentheses are used for groupings.

[Transform functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#transform_functions)

-----------------------------------------------------------------------------------------------------------------------

The [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represent appearance transformation. It is used as a value of [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 property.

### [Translate functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#translate_functions)

[`translateX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX)

Translates an element horizontally.

[`translateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)

Translates an element vertically.

[`translateZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ)

Translates an element along the z-axis.

[`translate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)

Translates an element on the 2D plane.

[`translate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)

Translates an element in 3D space.

### [Rotation functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#rotation_functions)

[`rotateX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)

Rotates an element around the horizontal axis.

[`rotateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)

Rotates an element around the vertical axis.

[`rotateZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)

Rotates an element around the z-axis.

[`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)

Rotates an element around a fixed point on the 2D plane.

[`rotate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)

Rotates an element around a fixed axis in 3D space.

### [Scaling functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#scaling_functions)

[`scaleX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)

Scales an element up or down horizontally.

[`scaleY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)

Scales an element up or down vertically.

[`scaleZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)

Scales an element up or down along the z-axis.

[`scale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale)

Scales an element up or down on the 2D plane.

[`scale3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)

Scales an element up or down in 3D space.

### [Skew functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#skew_functions)

[`skewX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)

Skews an element in the horizontal direction.

[`skewY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)

Skews an element in the vertical direction.

[`skew()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew)

Skews an element on the 2D plane.

### [Matrix functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#matrix_functions)

[`matrix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix)

Describes a homogeneous 2D transformation matrix.

[`matrix3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)

Describes a 3D transformation as a 4×4 homogeneous matrix.

### [Perspective functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#perspective_functions)

[`perspective()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)

Sets the distance between the user and the z=0 plane.

[Math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)

-------------------------------------------------------------------------------------------------------------

The math functions allow CSS numeric values to be written as mathematical expressions.

Each of the pages below contains detailed information about a math function's syntax, browser compatibility data, examples, and more. For a holistic introduction to CSS math functions, see [Using CSS math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions)
.

### [Basic arithmetic](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#basic_arithmetic)

[`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)

Performs basic arithmetic calculations on numerical values.

[`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)

Perform calculations on intrinsic size values such as `auto`, `fit-content`, and `max-content`, which are not supported by the `calc()` function.

### [Comparison functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#comparison_functions)

[`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)

Calculates the smallest of a list of values.

[`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)

Calculates the largest of a list of values.

[`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)

Calculates the central of a minimum, central, and maximum values.

### [Stepped value functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#stepped_value_functions)

[`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)

Calculates a rounded number based on a rounding strategy.

[`mod()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)

Calculates a modulus (with the same sign as the divisor) when dividing one number by another.

[`progress()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/progress)

Calculates the position of a value between two other values — a start value and an end value. The result represents the progress between the start and end values, where 0 is the start, and 1 is the end.

[`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)

Calculates a remainder (with the same sign as the dividend) when dividing one number by another.

### [Trigonometric functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#trigonometric_functions)

[`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)

Calculates the trigonometric sine of a number.

[`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)

Calculates the trigonometric cosine of a number.

[`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)

Calculates the trigonometric tangent of a number.

[`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)

Calculates the trigonometric inverse sine of a number.

[`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)

Calculates the trigonometric inverse cosine of a number.

[`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)

Calculates the trigonometric inverse tangent of a number.

[`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)

Calculates the trigonometric inverse tangent of two-numbers in a plane.

### [Exponential functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#exponential_functions)

[`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)

Calculates the base raised to the power of a number.

[`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)

Calculates the square root of a number.

[`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)

Calculates the square root of the sum of the squares of its arguments.

[`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)

Calculates the logarithm of a number.

[`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)

Calculates `e` raised to the power of a number.

### [Random value functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#random_value_functions)

[`random()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random)

Generates a random value between a minimum and maximum value.

### [Sign-related functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#sign-related_functions)

[`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)

Calculates the absolute value of a number.

[`sign()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sign)

Calculates the sign (positive or negative) of the number.

[Filter functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#filter_functions)

-----------------------------------------------------------------------------------------------------------------

The [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a graphical effect that can change the appearance of an input image. It is used in the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)

Increases the image gaussian blur.

[`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)

Brightens or darkens an image.

[`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)

Increases or decreases the image contrast.

[`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)

Applies a drop shadow behind an image.

[`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)

Converts an image to grayscale.

[`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)

Changes the overall hue of an image.

[`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)

Inverts the colors of an image.

[`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)

Adds transparency to an image.

[`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)

Changes the overall saturation of an image.

[`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)

Increases the sepia of an image.

[Color functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#color_functions)

---------------------------------------------------------------------------------------------------------------

The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 specifies different color representations.

[`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)

Defines a given color according to its red, green, blue and alpha (transparency) components.

[`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)

Defines a given color according to its hue, saturation, lightness and alpha (transparency) components.

[`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)

Defines a given color according to its hue, whiteness and blackness components.

[`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)

Defines a given color according to its lightness, chroma and hue components.

[`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)

Defines a given color according to its lightness, chroma, hue and alpha (transparency) components.

[`lab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lab)

Defines a given color according to its lightness, a-axis distance and b-axis distance in the Lab colorspace.

[`oklab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklab)

Defines a given color according to its lightness, a-axis distance, b-axis distance in the Lab colorspace and alpha (transparency).

[`color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)

Specifies a particular, specified colorspace rather than the implicit sRGB colorspace.

[`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)

Mixes two color values in a given colorspace by a given amount.

[`contrast-color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)

Returns a color with maximum color contrast for a given color.

[`device-cmyk()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/device-cmyk)

Defines CMYK colors in a device-dependent way.

[`alpha()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha)

Returns a color with a modified alpha (transparency) channel.

[`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)

Returns one of two provided colors based on the current color scheme.

[`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)

Creates a custom maximum luminance limit that is a mix of different [`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
 keywords in specified percentages.

[Image functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#image_functions)

---------------------------------------------------------------------------------------------------------------

The [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 provides graphical representation of images or gradients.

### [Gradient functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#gradient_functions)

[`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)

Linear gradients transition colors progressively along an imaginary line.

[`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)

Radial gradients transition colors progressively from a center point (origin).

[`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)

Conic gradients transition colors progressively around a circle.

[`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)

Is similar to `linear-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container.

[`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)

Is similar to `radial-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container.

[`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)

Is similar to `conic-gradient()` and takes the same arguments, but it repeats the color stops infinitely in all directions so as to cover its entire container.

### [Image functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#image_functions_2)

[`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)

Defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 in a similar fashion to the [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 type, but with added functionality including specifying the image's directionality and fallback images for when the preferred image is not supported.

[`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)

Picks the most appropriate CSS image from a given set, primarily for high pixel density screens.

[`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)

Blends two or more images at a defined transparency.

[`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)

Defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value generated from an arbitrary HTML element.

[`paint()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint)

Defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value generated with a PaintWorklet.

[Counter functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#counter_functions)

-------------------------------------------------------------------------------------------------------------------

CSS counter functions are generally used with the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property, although in theory, they may be used wherever a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 is supported.

[`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)

Returns a string representing the current value of the named counter if there is one.

[`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)

Enables nested counters, returning a concatenated string representing the current values of the named counters, if there are any.

[`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)

Defines the counter styles inline, directly as the value of a property.

[Shape functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#shape_functions)

---------------------------------------------------------------------------------------------------------------

### [Basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#basic_shapes)

The [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a graphical shape. It is used in the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
, [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
, and [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 properties.

[`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)

Defines a circle shape.

[`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)

Defines an ellipse shape.

[`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)

Defines an inset rectangle shape.

[`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)

Defines a rectangle shape using the distances from the top and left edges of the reference box.

[`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)

Defines a rectangle shape using the specified distances from the top and left edges of the reference box and the rectangle width and height.

[`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)

Defines a polygon shape.

[`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)

Accepts an SVG path string to enable a shape to be drawn.

[`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)

Accepts a comma-separated list of commands defining the shape to be drawn.

### [Other shape functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#other_shape_functions)

[`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray)

Valid with [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
; defines the line segment an animated element can follow.

[`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)

Defines the curvature of an ellipse; can be used to specify a [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
, which is used with [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 and its [constituent](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#constituent_properties)
 and [related](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#properties_that_follow_corner-shape)
 properties.

[Reference functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#reference_functions)

-----------------------------------------------------------------------------------------------------------------------

The following functions are used as a value of properties to reference a value defined elsewhere:

[`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)

Uses the attributes defined on HTML element.

[`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)

Uses the user-agent defined as environment variable.

[`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)

Conditionally sets a property value depending on the result of a [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
, [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, or [feature query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
.

[`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)

Uses a file from the specified URL.

[`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)

Uses the custom property value instead of any part of a value of another property.

[Grid functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#grid_functions)

-------------------------------------------------------------------------------------------------------------

The following functions are used to define a [CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
:

[`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)

Clamps a given size to an available size according to the formula `min(maximum size, max(minimum size, argument))`.

[`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)

Defines a size range greater-than or equal-to _min_ and less-than or equal-to _max_.

[`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)

Represents a repeated fragment of the track list, allowing a large number of columns or rows that exhibit a recurring pattern.

[Font functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#font_functions)

-------------------------------------------------------------------------------------------------------------

CSS font functions are used with the [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
 property to control the use of alternate glyphs.

[`stylistic()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#stylistic)

Enables stylistic alternates for individual characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `salt`, like `salt 2`.

[`styleset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#styleset)

Enables stylistic alternatives for sets of characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ssXY`, such as `ss02`.

[`character-variant()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#character-variant)

Enables specific stylistic alternatives for characters. It is similar to `styleset()`, but doesn't create coherent glyphs for a set of characters; individual characters will have independent and not necessarily coherent styles. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `cvXY`, such as `cv02`.

[`swash()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#swash)

Enables [swash](https://en.wikipedia.org/wiki/Swash_%28typography%29 "External link (opens in new tab)")
 glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType values `swsh` and `cswh`, such as `swsh 2` and `cswh 2`.

[`ornaments()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#ornaments)

Enables ornaments such as [fleurons](https://en.wikipedia.org/wiki/Fleuron_%28typography%29 "External link (opens in new tab)")
 and other dingbat glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ornm`, such as `ornm 2`.

[`annotation()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#annotation)

Enables annotations such as circled digits or inverted characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `nalt`, such as `nalt 2`.

[Easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#easing_functions)

-----------------------------------------------------------------------------------------------------------------

The [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 CSS [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a mathematical function. It is used in transition and animation properties:

[`linear()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)

Easing function that interpolates linearly between its points.

[`cubic-bezier()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)

Easing function that defines a cubic Bézier curve.

[`steps()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)

Iteration along a specified number of stops along the transition, displaying each stop for equal lengths of time.

[Animation functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#animation_functions)

-----------------------------------------------------------------------------------------------------------------------

The following functions are used as a value of different [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 properties:

[`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)

Sets the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 of an element to an _anonymous scroll progress timeline_.

[`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)

Sets the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 of an element to an _anonymous view progress timeline_.

[Anchor positioning functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#anchor_positioning_functions)

-----------------------------------------------------------------------------------------------------------------------------------------

The anchor positioning functions are used when positioning and sizing anchor-positioned elements relative to the location and size of their associated anchor elements.

[`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)

Returns a length relative to the position of the edges of an anchor-positioned element's associated anchor element.

[`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)

Returns a length relative to the size of the associated anchor element.

[Tree counting functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#tree_counting_functions)

-------------------------------------------------------------------------------------------------------------------------------

The following functions return an integer value based on the DOM tree, rather than the flat tree like most CSS values do:

[`sibling-index()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)

Returns an integer reflecting the position of the selected element among its siblings.

[`sibling-count()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count)

Returns an integer reflecting the total number of siblings, including the selected element.

[Alphabetical index of functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#alphabetical_index_of_functions)

-----------------------------------------------------------------------------------------------------------------------------------------------

*   [`-moz-image-rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect)
    
*   [`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`alpha()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha)
    
*   [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
    
*   [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    
*   [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
    
*   [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
    
*   [`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
    
*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
    
*   [`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
    
*   [`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)
    
*   [`color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
    
*   [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
    
*   [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    
*   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
    
*   [`contrast-color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)
    
*   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    
*   [`counters()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
    
*   [`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    
*   [`cubic-bezier()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
    
*   [`device-cmyk()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/device-cmyk)
    
*   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
    
*   [`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
    
*   [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
    
*   [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
    
*   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    
*   [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
    
*   [`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
    
*   [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
    
*   [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
    
*   [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
    
*   [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
    
*   [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
    
*   [`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
    
*   [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
    
*   [`lab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lab)
    
*   [`layer()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import/layer_function)
    
*   [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
    
*   [`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
    
*   [`linear()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
    
*   [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    
*   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    
*   [`matrix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix)
    
*   [`matrix3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)
    
*   [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    
*   [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
    
*   [`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
    
*   [`mod()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)
    
*   [`oklab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklab)
    
*   [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
    
*   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
    
*   [`paint()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint)
    
*   [`palette-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)
    
*   [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
    
*   [`perspective()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)
    
*   [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
    
*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`progress()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/progress)
    
*   [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    
*   [`random()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random)
    
*   [`ray()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray)
    
*   [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
    
*   [`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
    
*   [`repeat()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
    
*   [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    
*   [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
    
*   [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    
*   [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
    
*   [`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
    
*   [`rotate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
    
*   [`rotateX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)
    
*   [`rotateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)
    
*   [`rotateZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)
    
*   [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    
*   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
    
*   [`scale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale)
    
*   [`scale3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
    
*   [`scaleX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
    
*   [`scaleY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)
    
*   [`scaleZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
    
*   [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
    
*   [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
    
*   [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
    
*   [`sibling-count()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count)
    
*   [`sibling-index()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)
    
*   [`sign()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sign)
    
*   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`skew()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew)
    
*   [`skewx()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)
    
*   [`skewy()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)
    
*   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`steps()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
    
*   [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`translate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
    
*   [`translate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)
    
*   [`translateX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX)
    
*   [`translateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)
    
*   [`translateZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ)
    
*   [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
    
*   [`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
    
*   [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    
*   [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    
*   [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#see_also)

-------------------------------------------------------------------------------------------------

*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [Learn: Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/functions/index.md?plain=1 "Folder: en-us/web/css/reference/values/functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2FFunctions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffunctions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2FFunctions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffunctions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F08a5a4313166a8f36f8c0c1320ac970423239b9a%0A*+Document+last+modified%3A+2026-09-21T14%3A32%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
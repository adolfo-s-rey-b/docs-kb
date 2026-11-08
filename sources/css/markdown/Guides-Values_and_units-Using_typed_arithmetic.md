*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#mdn-search)
    

Using CSS typed arithmetic
==========================

**CSS typed arithmetic** refers to permitted calculations performed with typed CSS values via functions such as [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
, and specifically, to the behavior defined in the [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
 module. CSS typed arithmetic enables dividing a value with one unit by a value with a different unit of the same data type, resulting in unitless quotients.

These quotients can then be used as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 in the values of unitless properties, or converted into any numeric data type (such as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
) by multiplying them by a numeric typed value.

This typed arithmetic behavior enables relationships to be created between different values on a page. This article explores typed arithmetic and presents several examples that make use of it.

**Note:** Originally, the [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
 module limited the arguments multiplication and division operations could take to make dividing by zero detectable at parse time and avoid issues such as squared units. Typed arithmetic relaxes some of those restrictions in [supporting browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#browser_compatibility)
.

[CSS typed arithmetic rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#css_typed_arithmetic_rules)

---------------------------------------------------------------------------------------------------------------------------------------------------------

When performing calculations on values in CSS, there are some rules around compatibility of values with different data types.

### [Addition and subtraction](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#addition_and_subtraction)

When adding or subtracting values, all the values must be within the same overall data type. The following examples all produce valid results:

However, the following are invalid. The results of such mixed-type calculations would be meaningless:

[Multiplication](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#multiplication)

---------------------------------------------------------------------------------------------------------------------------------

When multiplying values in CSS, only one of the values can have a unit. All other values must be unitless [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values. This is because you want a product that is a greater or lesser amount of the same unit, and do not want to create squared units, which no CSS properties accept.

If you try to multiply two values with units — even the same units — normal mathematical rules dictate that the units should be multiplied as well. For example:

In this case, the function is invalid as `800px2` is meaningless in CSS.

[Division](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#division)

---------------------------------------------------------------------------------------------------------------------

When dividing values in CSS, you can divide a value with a unit by a unitless value:

However, you can't divide a unitless value by a value with a unit as that doesn't make sense:

When a value of any numeric data type is divided by a value of the same type, the units cancel each other out, and you are left with a unitless value. Behind the scenes, the two values are computed before being divided by one another.

As a result, the same calculation can have very different results depending on the context it is used in and the units of the divisor.

Take the following example:

The `100vw` is equal to `100%` of the width of the viewport. If the viewport is currently `1000px` wide, the calculation will return the unitless value `1000`. However, if the viewport is `500px` wide, the calculation will return the unitless value `500`.

If we replace the `1px` divisor by `1em`, we get very different results:

If the viewport is `1000px` wide, and `1em` is equal to the browser default of `16px` at the point of calculation, the previous calculation will return `1000px / 16px` = `62.5`.

It used to be the case that you couldn't divide one typed value by another, even if the two values have units of the same type. However, the specification was updated to permit this; check for [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc#browser_compatibility)
.

[Why is the behavioral update useful?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#why_is_the_behavioral_update_useful)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Being able to divide one typed value by another of the same type may not sound very significant at first, but it enables useful associations between different values that can be used to create responsive UI features.

The key to all of this is being able to represent values in a unitless form via divisions like this one:

The result is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the viewport width in pixels as a unitless value. This can be used anywhere a number is valid, including other `calc()` functions. You can dynamically vary other property values based on this value, regardless of what units they have.

For example, the unitless value can be immediately transferred to [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
:

You can multiply it by a value such as `1deg` to create an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 value:

You can multiply it by a value such as `1rem` to create a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value:

Let's walk through some examples to show how CSS typed arithmetic can be useful.

[Basic example: responsive background opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#basic_example_responsive_background_opacity)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [responsive background opacity](https://mdn.github.io/dom-examples/css-typed-arithmetic/responsive-background-opacity/ "External link (opens in new tab)")
 example ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/responsive-background-opacity "External link (opens in new tab)")
) shows how to vary the opacity of a background image as the viewport width is changed. Having the background image fade out as the screen gets narrower means the image is less likely to affect the readability of the text content as they start to overlap.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#html)

The HTML contains some basic text content wrapped in a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#css)

We start by defining a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 called `--width-percentage` on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 element, which contains the result of the calculation `100vw / 2000px`. This value represents the viewport width as a percentage of `2000px` that we will later use as an alpha channel value. When the viewport is `2000px` wide, the calculation will return `1`, which is equivalent to `100%` alpha. Anything less than a `2000px` viewport width will result in a smaller value.

**Note:** Any alpha value greater than `1` is treated as `1`, therefore we don't need to clamp the maximum value.

We then set a fixed [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and some [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 on the wrapper `<div>`, and center it horizontally using [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
.

Finally, we set multiple backgrounds on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element. We'll go through these in reverse order:

1.  The last and therefore bottom-most [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     value is a non-repeating background image located near the top-right corner.
2.  The top background is a white semi-transparent overlay created using a [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
     function with both color stops set to the same color. The color's alpha channel value is calculated as `1` minus the `--width-percentage` custom property we set earlier: As the viewport width gets narrower, `--width-percentage` will get smaller, therefore the white gradient will become more opaque, reducing the opacity of the background image.

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#result)

To see the result, [view our responsive background opacity example live](https://mdn.github.io/dom-examples/css-typed-arithmetic/responsive-background-opacity/ "External link (opens in new tab)")
 ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/responsive-background-opacity "External link (opens in new tab)")
). Try altering the viewport width to see how the background opacity varies as a result.

[Varying values of different types based on a single value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#varying_values_of_different_types_based_on_a_single_value)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [different type variations](https://mdn.github.io/dom-examples/css-typed-arithmetic/different-type-variations/ "External link (opens in new tab)")
 example ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/different-type-variations "External link (opens in new tab)")
) works in a very similar way to the previous example, except that in this case, we demonstrate the use of a single variable value in the definition of multiple other values with different data types.

Specifically, we set a paragraph's background color _and_ font size based on the viewport width.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#html_2)

The markup for this example contains a paragraph of text:

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#css_2)

We start off our CSS in a similar way to the previous demo, creating a unitless value based on the viewport width. This time, we calculate it by dividing `100vw` by `1px` and store the resulting number in a custom property called `--viewport-in-pixels`. The value represents the current viewport width in pixels, without any units.

Now on to the styling of the paragraph itself. We first give it some basic styles (a [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 and [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 of `center`), then set two values based on the `--viewport-in-pixels` property created earlier:

1.  We set the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
     of the paragraph to a value equal to `--viewport-in-pixels` divided by `200`, multiplied by `1em` to convert the numeric quotient into `em`s.
2.  We set the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
     of the paragraph to an [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
     color value. The lightness and chroma components are constant values (`75%` and `50%`, respectively), whereas the hue component is set to `--viewport-in-pixels` divided by `10`, plus `100`. We then multiply the result of that by `1deg` to ensure the value is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    .
    
    **Note:** This last step is not strictly necessary, as `lch()` also accepts unitless hue values. However, a degree value may be more intuitive, and we wanted to show another example of how the unitless value can be converted into a different data type.
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#result_2)

To see the result, [view our different type variations example live](https://mdn.github.io/dom-examples/css-typed-arithmetic/different-type-variations/ "External link (opens in new tab)")
 ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/different-type-variations "External link (opens in new tab)")
). Try altering the viewport width to see how the paragraph font size and background color both vary as a result.

[An animated story circle](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#an_animated_story_circle)

-----------------------------------------------------------------------------------------------------------------------------------------------------

The [animated story circle](https://mdn.github.io/dom-examples/css-typed-arithmetic/animated-story-circle/ "External link (opens in new tab)")
 example ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/animated-story-circle "External link (opens in new tab)")
) demonstrates a more complex effect created by leveraging CSS typed arithmetic rules. In this case, the different paragraphs of a body of text are laid out in a circle emanating from a center point. What's more, the circle of paragraphs closes up into a fan shape when the viewport is made narrower, and opens up again when it is made wider.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#html_3)

The HTML is fairly basic — a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 containing multiple [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements. The text of the first paragraph is wrapped in a [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 element to provide an indicator of where to start reading.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#css_3)

We start the CSS by setting a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 of `100%` on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 element.

Next, we set several properties on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element:

*   We start by setting a `height` of `inherit`, meaning the `<body>` will inherit the `:root` element's `100%` height and therefore span the full height of the viewport.
*   Next, we horizontally center the `<body>` using [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    , and give it a [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    . As you'll see later on, this upper bound is important for controlling the maximum rotation of the fan/circle shape.
*   We center the `<div>` with `class="story-circle"` horizontally and vertically inside the `<body>` using [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
    .
*   We use the [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
     property to declare the `<body>` as an inline [size query container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries)
    . This is important because we want to vary the shape rotation based on the `<body>` width, and not the viewport width as we did in previous examples. Setting it as a size query container allows us to reference its size in calculations.

We now come to styling the `story-circle` `<div>`. We set its `width` and `height` to `1px`: it will act as a reference point with its child paragraphs positioned in a circle around it. (We don't even need to set positioning on it, as it is fine for the paragraphs to be positioned relative to the `<body>`).

We then create a custom property called `--width-percentage` that contains the result of `100cqw` (100% of the width of the element's parent query container, which is the `<body>` element) divided by `1200px`, minus `0.33333`. This is the key value that will control the amount the circle rotates by as the viewport width is changed.

We are using the container query width rather than the viewport width to control the rotation because we want to set a maximum bound for the container, which is controlled by the `<body>` `max-width`. If the rotation value becomes greater than a full circle, the last paragraph will start to overlap the first one, which spoils the effect.

Since the `max-width` is `1600px`, you might have expected the calculation to be `100cqw / 1600px)`. This would work, but we've instead gone for `(100cqw / 1200px) - 0.33333` (the `0.33333` comes from `1600px/1200px - 1`). Both would cause the maximum rotation to occur at a `<body>` width of `1600px`, but the fan now has a smaller minimum rotation, which gives a better effect at narrow viewport widths.

The final style rule selects the paragraphs themselves. Most of this styling is rudimentary. It is worth pointing out that we have set [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 to `absolute` to cause all of the paragraphs to sit on top of one another, and we've set a [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 value of `center left` to cause paragraphs to rotate around the center of their left edge, so they will all fan out from a center point over their containing `<div>`.

Now onto the interesting bit — we define a custom property called `--angle` that contains the unitless rotation angle of the paragraph, before setting the [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
 property to the resulting value. We multiply the resulting number by `1deg` to convert it to a degree value. The `--angle` custom property is the product of three values:

1.  The paragraph's [`sibling-index()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)
     minus `1`, which causes the first paragraph to have a rotation angle of `0`, as we want it to be horizontal.
2.  `360` divided by the paragraph's [`sibling-count()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count)
    , which causes all the paragraphs to be equally spaced around the circle, meaning the design will still work if the number of paragraphs changes.
3.  our `--width-percentage` custom property, which causes the rotation of the paragraphs around the circle to vary as the viewport width changes. Remember that this property has a maximum value of `1`, which will be achieved when the `<body>` element hits its `max-width` of `1600px`.

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#result_3)

To see the result, [view our animated story circle example live](https://mdn.github.io/dom-examples/css-typed-arithmetic/animated-story-circle/ "External link (opens in new tab)")
 ([see source code](https://github.com/mdn/dom-examples/tree/main/css-typed-arithmetic/animated-story-circle "External link (opens in new tab)")
). Try increasing and decreasing the viewport width to see how the paragraph fan shape unfolds into a circle and back again.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    , [`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [CSS Typed Arithmetic](https://css-tricks.com/css-typed-arithmetic/ "External link (opens in new tab)")
     on css-tricks.com (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_typed_arithmetic/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/values_and_units/using_typed_arithmetic/index.md?plain=1 "Folder: en-us/web/css/guides/values_and_units/using_typed_arithmetic (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FUsing_typed_arithmetic&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fusing_typed_arithmetic%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FUsing_typed_arithmetic%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fusing_typed_arithmetic%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff49f1d49a7ea045dd1365834d8931721894c1aaf%0A*+Document+last+modified%3A+2026-08-07T04%3A56%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
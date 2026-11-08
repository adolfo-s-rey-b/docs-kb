*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#mdn-search)
    

Using CSS custom functions
==========================

CSS custom functions enable you to create reusable blocks of CSS code that can accept arguments, contain complex logic (defined using features such as CSS [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
 functions and [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules), and return values based on that logic. They work similarly to [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
, but provide more flexibility.

In this article, we'll show you how to use them and present some real-world examples.

[Function basics](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#function_basics)

----------------------------------------------------------------------------------------------------------------------------------------------

A basic CSS custom function definition looks like this:

After the `@function` syntax, we define a name for the function: `--half-opacity`. This must be a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 type — it must start with a double-dash, and is case-sensitive. The function name is immediately followed by a set of parentheses (`()`) and a set of curly braces (`{}`).

**Note:** If multiple CSS functions are given the same name, the function in the stronger cascade [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
 wins. If all of them are in the same layer, the function defined last in the source order wins.

Inside the curly braces is the function **body**, which is where the function logic is defined. This can contain multiple declarations, including custom properties (which will be locally scoped to the function body), at-rules such as [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
, and the [`result`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#result_2)
 descriptor. The value of the `result` descriptor is evaluated to determine the value returned by the function.

Here, we are setting `result` to the value `0.5`: the `--half-opacity()` function will always return `0.5`.

### [Why "result" and not "return"?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#why_result_and_not_return)

The `result` descriptor sounds similar in functionality to the JavaScript function [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
 statement. However, `return` is not used in CSS functions. This is because, unlike JavaScript `return` statements, CSS functions do not return a value as soon as a `result` declaration is reached.

The body of a CSS function is evaluated from start to finish. If there are multiple `result` declarations included in the body, the last one in the source order overrides the earlier ones.

### [Calling a CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#calling_a_css_function)

A CSS function can be called in place of any suitable property value using the [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
 syntax, which consists of the function name followed by parentheses containing the arguments to pass to the function, if any. For example, we can call our `--half-opacity()` function like this:

Since this function always returns the value `0.5`, the previous declaration is the equivalent of `opacity: 0.5`. This isn't very useful. You might as well just use a custom property, or the literal value `0.5`.

Let's move on to look at how we can use CSS functions.

[Feature detecting CSS functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#feature_detecting_css_functions)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

One practical use of CSS functions with no parameters is in feature detection. In all of [the examples we'll be looking at](https://github.com/mdn/dom-examples/tree/main/css-custom-functions "External link (opens in new tab)")
 in this article, we define a `--supports()` function that looks like this:

You can then define a "feature not supported" banner, and set its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `--supports()`:

In browsers that support custom functions, `display` will be set to `none`, and the support banner will be hidden. In non-supporting browsers, the `display: --supports()` declaration will be invalid and therefore ignored; therefore, the banner will be displayed.

[Specifying function parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#specifying_function_parameters)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS function parameters are specified as comma-separated custom properties inside the parentheses following the function name. For example:

This function has a name of `--transparent` and takes two custom properties as parameters, `--color` and `--alpha`, which can be used locally inside the function body. The body contains a `result` descriptor, which uses [CSS relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
 to convert the input `--color` value into an [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
 color with an alpha channel value as specified in the input `--alpha` value.

You can then call this function anywhere you want to produce a semi-transparent version of an existing color.

For example:

[Specifying data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#specifying_data_types)

----------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to specify permitted data types for the function parameters and return value. When you don't specify these, the function will accept any type for these values.

Let's modify our previous function to provide data types:

The data type of each parameter is specified after the parameter name, and the data type of the `result` is specified just before the opening curly brace, preceded by the `returns` keyword. The [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
 function is used to specify a data type.

Note that, in cases where you are only specifying a single data type, you can omit the `type()` syntax and just write the type as a shorthand:

Now the function will only produce a valid value if the input arguments are a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 and a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
, respectively, and the `result` is a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
. If not, for example:

then the value will become invalid at computed-value time (since `50%` is not a `<number>` but a `<percentage>`) and the `background-color` will end up being set to `transparent`.

### [Specifying multiple permitted types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#specifying_multiple_permitted_types)

You can specify multiple accepted data types using the `|` symbol as a separator, for example:

In such cases, the full `type()` syntax must be used.

With this adjustment, the `--transparent(var(--base-color), 50%)` function call is now valid.

[Specifying default values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#specifying_default_values)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also specify default values for parameters, after a colon at the end of their definition. For example:

The `--alpha` parameter's default value is now `0.8`. If you want to use this value, you can omit the second argument when calling the function:

**Note:** If an invalid value is passed in as a function argument and a default value is specified in that parameter definition, the invalid value will be ignored, and the default value will be used instead.

### [Color adjust functions example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#color_adjust_functions_example)

You can see the `--transparent()` function in action in our [color-adjust-functions](https://mdn.github.io/dom-examples/css-custom-functions/color-adjust-functions/ "External link (opens in new tab)")
 example (see the [source code](https://github.com/mdn/dom-examples/tree/main/css-custom-functions/color-adjust-functions "External link (opens in new tab)")
).

This example also includes functions called `--lighter()` and `--darker()` that work similarly to `--transparent()`, but return lighter and darker variants of a color, respectively:

A library of functions like these can become very useful for defining color schemes based on a single color:

[Including complex logic](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#including_complex_logic)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

You can include more complex logic in functions using constructs such as [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules and [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
 functions.

Our [responsive-narrow-wide](https://mdn.github.io/dom-examples/css-custom-functions/responsive-narrow-wide/ "External link (opens in new tab)")
 example (see the [source code](https://github.com/mdn/dom-examples/tree/main/css-custom-functions/responsive-narrow-wide "External link (opens in new tab)")
) features a function called `--narrow-wide()`, which can be used to provide two value options for any property. One will be set if the viewport is below a specific breakpoint, and the other will be set if it is above.

The `--narrow-wide()` function accepts two parameters, `--narrow` and `--wide`. The returned `result` is the `--wide` property, unless the viewport is less than `700px` wide, in which case `--narrow` is returned.

This function can be used to provide responsive value options in multiple contexts:

### [Using an `if()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#using_an_if_function)

We could rewrite the `--narrow-wide()` function to use an `if()` function instead:

[Writing complex syntax once, then reusing it](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#writing_complex_syntax_once_then_reusing_it)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A key use case for CSS functions is to define a complex section of syntax once, and be able to reuse it multiple times with a much simpler function call.

Our [gradient-function](https://mdn.github.io/dom-examples/css-custom-functions/gradient-function/ "External link (opens in new tab)")
 example (see the [source code](https://github.com/mdn/dom-examples/tree/main/css-custom-functions/gradient-function "External link (opens in new tab)")
) provides an example of this. It features a function called `--shippo-pattern()` that accepts length and color arguments, and returns a complex [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 value featuring multiple [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
 backgrounds:

With this function defined, we can now create variants of this background value with different color tints and circle sizes:

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions#see_also)

--------------------------------------------------------------------------------------------------------------------------------

*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    
*   [CSS custom functions and mixins](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins)
     module
*   [Custom CSS Functions in the Browser](https://www.oddbird.net/2025/04/11/custom-functions/ "External link (opens in new tab)")
     by Miriam Suzanne (2025)
*   [CSS @function + CSS if()](https://www.bram.us/2025/02/18/css-at-function-and-css-if/ "External link (opens in new tab)")
     by Bramus (2025)
*   [5 Useful CSS functions using the new @function rule](https://una.im/5-css-functions/ "External link (opens in new tab)")
     by Una Kravets (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/custom_functions_and_mixins/using_custom_functions/index.md?plain=1 "Folder: en-us/web/css/guides/custom_functions_and_mixins/using_custom_functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_functions_and_mixins%2FUsing_custom_functions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcustom_functions_and_mixins%2Fusing_custom_functions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_functions_and_mixins%2FUsing_custom_functions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcustom_functions_and_mixins%2Fusing_custom_functions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
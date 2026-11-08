*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#mdn-search)
    

Using CSS math functions
========================

**CSS math functions** allow a property value - such as the `height`, `animation-duration`, or `font-size` of an element - to be written as a mathematical expression.

Without using any math, the built-in [CSS units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
 like `rem`, `vw`, and `%` are often flexible enough to style HTML elements to achieve a particular user experience.

However, there are cases where we might feel limited by expressing an element's style using a single value and unit. Consider the following examples:

1.  We want to set the height of a content area to be "the height of the viewport minus the height of a navbar."
2.  We want to add the width of two elements together to define the width of a third element.
3.  We want to prevent a variable `font-size` of some text from growing beyond a certain size.

In all of these cases, we need to rely on math to achieve the desired outcomes. One solution could be to rely on mathematical functions defined by JavaScript, and dynamically set element styles based on results calculated by our scripts.

In many instances, including in the examples above, **we can instead utilize math functions built directly into CSS**. This solution is often simpler to implement and faster for the browser to execute than using JavaScript.

In total, developers can use a combination of [nearly two dozen CSS math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
 in their stylesheets. In this guide, we'll exemplify four of the more commonly-used, and introduce those more advanced.

[`calc()`: Basic math operations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#calc_basic_math_operations)

------------------------------------------------------------------------------------------------------------------------------------------------------------

In the first two of our three examples above, we want to set the style of an element according to the result of an addition or subtraction operation. This is exactly one of the use cases for [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
.

The **`calc()`** function lets you specify CSS property values using **addition, subtraction, multiplication, and division**. It is often used to combine two CSS values that have different units, such as `%` and `px`.

The `calc()` math function takes a mathematical expression as a parameter and returns the result of that expression, e.g.:

css

    property: calc(expression);
    

### [`calc()` Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#calc_example)

Click on the play icon below to see the `calc()` example in the code playground and try it for yourself.

    <div class="calc1">
      <code>width: calc(10px + 100px);</code>
    </div>
    <div class="calc2">
      <code>width: calc(2em * 5);</code>
    </div>
    <div class="calc3">
      <code>width: calc(100% - 32px);</code>
    </div>
    <div class="calc4">
      <code>width: calc(var(--predefined-width) - calc(16px * 2));</code>
    </div>
    

css

    div {
      background-color: black;
      margin: 4px 0;
      width: 100%;
    }
    
    div > code {
      display: block;
      background-color: red;
      color: white;
      height: 48px;
    }
    
    .calc1 > code {
      /* Output width: `110px` */
      width: calc(10px + 100px);
    }
    
    .calc2 > code {
      /* Output width: `10em` */
      width: calc(2em * 5);
    }
    
    .calc3 > code {
      /* Output width: Depends on the container's width */
      width: calc(100% - 32px);
    }
    
    .calc4 > code {
      --predefined-width: 100%;
      /* Output width: Depends on the container's width */
      width: calc(var(--predefined-width) - calc(16px * 2));
    }
    

[`min()`: Finding the minimum value in a set](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#min_finding_the_minimum_value_in_a_set)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are cases where we don't want the value of a CSS property to exceed a certain number. Say, for example, we want the width of our content container to be the smaller of "the full width of our screen" and "500 pixels." In those cases, we can use the CSS math function [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
.

The `min()` math function takes a set of comma-separated values as arguments and returns the smallest of those values, e.g.:

css

    width: min(32px, 50%, 2rem);
    

This function is often used to compare two CSS values that have different units, such as `%` and `px`.

### [`min()` Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#min_example)

Click on the play icon below to see the `min()` example in the code playground and try it for yourself.

    <div class="min1">
      <code>width: min(9999px, 50%);</code>
    </div>
    <div class="min2">
      <code>width: min(9999px, 100%);</code>
    </div>
    <div class="min3">
      <code>width: min(120px, 150px, 90%);</code>
    </div>
    <div class="min4">
      <code>width: min(80px, 90%);</code>
    </div>
    

css

    div {
      background-color: black;
      margin: 4px 0;
      width: 100%;
    }
    
    div > code {
      display: block;
      background-color: darkblue;
      color: white;
      height: 48px;
    }
    
    .min1 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `50%` of the container's width */
      width: min(9999px, 50%);
    }
    
    .min2 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `100%` of the container's width */
      width: min(9999px, 100%);
    }
    
    .min3 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `120px` of the container's width */
      width: min(120px, 150px, 90%);
    }
    
    .min4 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `80px` of the container's width */
      width: min(80px, 90%);
    }
    

[`max()`: Finding the maximum value in a set](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#max_finding_the_maximum_value_in_a_set)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to `min()`, sometimes we don't want the value of a CSS property to go below a certain number. For example, we might want the width of our content container to be the _larger_ of "the full width of our screen" and "500 pixels." In those cases, we can use the CSS math function [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
.

The `max()` math function takes a set of comma-separated values as arguments and returns the largest of those values, e.g.:

css

    width: max(32px, 50%, 2rem);
    

This function is often used to compare two CSS values that have different units, such as `%` and `px`.

Notice the similarities and differences between the examples for `min()` and `max()`.

### [`max()` Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#max_example)

Click on the play icon below to see the `max()` example in the code playground and try it for yourself.

    <div class="max1">
      <code>width: max(50px, 50%);</code>
    </div>
    <div class="max2">
      <code>width: max(50px, 100%);</code>
    </div>
    <div class="max3">
      <code>width: max(20px, 50px, 90%);</code>
    </div>
    <div class="max4">
      <code>width: max(80px, 80%);</code>
    </div>
    

css

    div {
      background-color: black;
      margin: 4px 0;
      width: 100%;
      height: 48px;
    }
    
    div > code {
      display: block;
      background-color: darkmagenta;
      color: white;
      height: 48px;
    }
    
    .max1 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `50%` of the container's width */
      width: max(50px, 50%);
    }
    
    .max2 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `100%` of the container's width */
      width: max(50px, 100%);
    }
    
    .max3 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `90%` of the container's width */
      width: max(20px, 50px, 90%);
    }
    
    .max4 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `80%` of the container's width */
      width: max(80px, 80%);
    }
    

[`clamp()`: Constraining a value between two values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#clamp_constraining_a_value_between_two_values)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can combine the functions of `min()` and `max()` by using [`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)
. The `clamp()` math function takes a minimum value, the value to be clamped, and the maximum value as arguments, e.g.:

css

    /* clamped value: 50%, minimum: 100px, maximum: 300px */
    width: clamp(100px, 50%, 300px);
    

*   If the value to be clamped is less than the passed minimum value, the function will return the minimum value.
*   If the value to be clamped is greater than the passed maximum value, the function will return the maximum value.
*   If the value to be clamped is between the passed minimum and maximum values, the function will return the original value to be clamped.

This function is often used to compare two CSS values that have different units, such as `%` and `px`.

### [`clamp()` Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#clamp_example)

Click on the play icon below to see the `clamp()` example in the code playground and try it for yourself.

    <div class="clamp1">
      <code>width: clamp(10%, 1px, 90%);</code>
    </div>
    <div class="clamp2">
      <code>width: clamp(10%, 9999px, 90%);</code>
    </div>
    <div class="clamp3">
      <code>width: clamp(125px, 1px, 250px);</code>
    </div>
    <div class="clamp4">
      <code>width: clamp(25px, 9999px, 150px);</code>
    </div>
    

css

    div {
      background-color: black;
      margin: 4px 0;
      width: 100%;
      height: 48px;
    }
    
    div > code {
      display: block;
      background-color: darkgreen;
      color: white;
      height: 48px;
    }
    
    .clamp1 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `20%` of the container's width */
      width: clamp(20%, 1px, 80%);
    }
    
    .clamp2 > code {
      /* Output width: Depends on the container's width; */
      /* on this page, likely to be `90%` of the container's width */
      width: clamp(10%, 9999px, 90%);
    }
    
    .clamp3 > code {
      /* Output width: `125px` */
      width: clamp(125px, 1px, 250px);
    }
    
    .clamp4 > code {
      /* Output width: `150px` */
      width: clamp(25px, 9999px, 150px);
    }
    

[Advanced CSS Math Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#advanced_css_math_functions)

---------------------------------------------------------------------------------------------------------------------------------------------------------

When laying out and styling DOM elements, the four basic math functions [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
, [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
, [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
, and [`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)
 are often sufficient. However, for advanced uses like mathematics learning materials, 3D visualizations, or CSS animations, you may consider using:

*   [Stepped value functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#stepped_value_functions)
    *   [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
        : calculates a **value given a rounding strategy**
    *   [`mod()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)
        : calculates the **remainder** of a division operation with the **same sign as the divisor**
    *   [`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
        : calculates the **remainder** of a division operation with the **same sign as the dividend**
*   [Trigonometric functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#trigonometric_functions)
    *   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
        : calculates the **trigonometric sine** of a number
    *   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
        : calculates the **trigonometric cosine** of a number
    *   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
        : calculates the **trigonometric tangent** of a number
    *   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
        : calculates the **trigonometric inverse** sine of a number
    *   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
        : calculates the **trigonometric inverse** cosine of a number
    *   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
        : calculates the **trigonometric inverse** tangent of a number
    *   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
        : calculates the **trigonometric inverse** tangent given two numbers
*   [Exponential functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#exponential_functions)
    *   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
        : calculates a number **raised to the power** of another number
    *   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
        : calculates the **square root** of a number
    *   [`hypot()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
        : calculates the **square root of the sum of the squares** of the given numbers
    *   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
        : calculates the **logarithm** of a number (with `e` as the default base)
    *   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
        : calculates **`e` raised to the power** of another number
*   [Sign functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#sign-related_functions)
    *   [`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
        : calculates the **absolute value** of a number
    *   [`sign()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sign)
        : calculates the **sign (positive, negative, or zero)** of a number

[Final thoughts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions#final_thoughts)

-------------------------------------------------------------------------------------------------------------------------------

*   You can use CSS math functions to create responsive user interfaces without writing any JavaScript code.
*   CSS math functions can sometimes be used instead of [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
     to define layout breakpoints.
*   In 2023, members of the Interop Project [selected "CSS Math Functions" as a focus area of improvement](https://github.com/web-platform-tests/interop/blob/main/2023/README.md#css-math-functions "External link (opens in new tab)")
    . This means that browser vendors are working together to ensure that CSS math functions perform the same across browsers and devices.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Using_math_functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/values_and_units/using_math_functions/index.md?plain=1 "Folder: en-us/web/css/guides/values_and_units/using_math_functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FUsing_math_functions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fusing_math_functions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FValues_and_units%2FUsing_math_functions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fvalues_and_units%2Fusing_math_functions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
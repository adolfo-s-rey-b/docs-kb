*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#mdn-search)
    

`<calc-keyword>` CSS type
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<calc-keyword>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents well-defined constants such as `e` and `pi`. Rather than require authors to manually type out several digits of these mathematical constants or calculate them, a few of them are provided directly by CSS for convenience.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#syntax)

------------------------------------------------------------------------------------------------

The `<calc-keyword>` type defines numeric constants that can be used in [CSS math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#values)

[`e`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#e)

The base of the natural logarithm, approximately equal to `2.7182818284590452354`.

[`pi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#pi)

The ratio of a circle's circumference to its diameter, approximately equal to `3.1415926535897932`.

[`infinity` & `-infinity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#infinity)

An infinite value, used to indicate the largest/smallest possible value.

[`NaN`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#nan)

A value representing "Not a Number" canonical casing.

### [Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#notes)

Serializing the arguments inside [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 follows the IEEE-754 standard for floating point math which means there's a few cases to be aware of regarding constants like `infinity` and `NaN`:

*   Dividing by zero will return positive or negative `infinity` depending on the sign of the numerator.
    
*   Adding, subtracting or multiplying `infinity` to anything will return `infinity` unless it produces `NaN` (see below).
    
*   Any operation with at least one `NaN` argument will return `NaN`. This means `0 / 0`, `infinity / infinity`, `0 * infinity`, `infinity + (-infinity)`, and `infinity - infinity` will all return `NaN`.
    
*   Positive and negative zero are possible values (`0⁺` and `0⁻`). This has the following effects:
    
    *   Multiplication or division that produces zero with exactly one negative argument (`-5 * 0` or `1 / (-infinity)`) or negative result from combinations in the other math functions will return `0⁻`.
    *   `0⁻ + 0⁻` or `0⁻ - 0` will return `0⁻`. All other additions or subtractions that would produce a zero will return `0⁺`.
    *   Multiplying or dividing `0⁻` with a positive number (including `0⁺`) will return a negative result (either `0⁻` or `-infinity`), while multiplying or dividing `0⁻` with a negative number will return a positive result.

Examples of how these rules apply are shown in the [Infinity, NaN, and division by zero](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#infinity_nan_and_division_by_zero)
 section.

**Note:** It's rare to need to use `infinity` as an argument in `calc()`, but it can be used to avoid hardcoded "magic numbers" or making sure a certain value is always larger than another value. It may be useful if you need to make it obvious that a property has "the largest possible value" for that data type.

### [Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#formal_syntax)

<calc-keyword> =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#description)

----------------------------------------------------------------------------------------------------------

Mathematical constants can only be used inside [CSS math functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#math_functions)
 for calculations. Math constants are not CSS keywords, but if they are used outside of a calculation, they're treated like any other keyword. For example:

*   `animation-name: pi;` refers to an animation named "pi", not the `pi` numeric constant.
*   `line-height: e;` is invalid, but `line-height: calc(e);` is valid.
*   `rotate(1rad * pi);` won't work because [`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
     is not a math function. Use `rotate(calc(1rad * pi));`

In math functions, `<calc-keyword>` values are evaluated as [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values, therefore `e` and `pi` act as numeric constants.

Both `infinity` and `NaN` are slightly different, they are considered as degenerate numeric constants. While not technically numbers, they act as [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 values, so to get an infinite [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, for example, requires an expression like `calc(infinity * 1px)`.

The `infinity` and `NaN` values are included mostly to make serialization simpler and more obvious, but can be used to indicate a "largest possible value", since an infinite value is clamped to the allowed range. It's rare for this to be reasonable, but when using infinity it's much simpler than just putting an enormous number in a stylesheet or hardcoding magic numbers.

All constants are case-insensitive except for `NaN`, which makes `calc(Pi)`, `calc(E)` and `calc(InFiNiTy)` valid:

e
-e
E
pi
-pi
Pi
infinity
-infinity
InFiNiTy
NaN

The following are all invalid:

nan
Nan
NAN

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#examples)

----------------------------------------------------------------------------------------------------

### [Using e and pi in `calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#using_e_and_pi_in_calc)

The following example shows how to use `e` inside `calc()` to rotate an element with an exponentially-increasing angle. The second box shows how to use `pi` inside a [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
 function.

    #wrapper {
      display: flex;
      flex-direction: row;
      justify-content: space-evenly;
    }
    
    .container {
      display: flex;
      flex-direction: column;
      align-items: start;
      width: 200px;
    }
    .container > div {
      width: 100px;
      height: 100px;
      margin: 10px;
    }
    
    span {
      font-family: monospace;
      font-size: 0.8em;
    }
    
    #e {
      background-color: blue;
    }
    
    #pi {
      background-color: blue;
    }
    

html

    <div id="wrapper">
      <div class="container">
        <div id="e"></div>
        <input type="range" min="0" max="7" step="0.01" value="0" id="e-slider" />
        <label for="e-slider">e:</label>
        <span id="e-value"></span>
      </div>
      <div class="container">
        <div id="pi"></div>
        <input type="range" min="0" max="1" step="0.01" value="0" id="pi-slider" />
        <label for="pi-slider">pi:</label>
        <span id="pi-value"></span>
      </div>
    </div>
    

js

    // sliders
    const eInput = document.querySelector("#e-slider");
    const piInput = document.querySelector("#pi-slider");
    // spans for displaying values
    const eValue = document.querySelector("#e-value");
    const piValue = document.querySelector("#pi-value");
    
    eInput.addEventListener("input", function () {
      e.style.transform = `rotate(calc(1deg * pow(${this.value}, e)))`;
      eValue.textContent = e.style.transform;
    });
    
    piInput.addEventListener("input", function () {
      pi.style.rotate = `calc(sin(${this.value} * pi) * 100deg)`;
      piValue.textContent = pi.style.rotate;
    });
    

### [Infinity, NaN, and division by zero](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#infinity_nan_and_division_by_zero)

The following example shows the computed value of the `width` property when dividing by zero, followed by how serialization with different `calc()` constants look when viewed in the console:

html

    <div></div>
    

css

    div {
      height: 50px;
      background-color: red;
      width: calc(1px / 0);
    }
    

js

    const div = document.querySelector("div");
    console.log(div.offsetWidth); // 17895698 (infinity clamped to largest value for width)
    
    function logSerializedWidth(value) {
      div.style.width = value;
      console.log(div.style.width);
    }
    
    logSerializedWidth("calc(1px / 0)"); // calc(infinity * 1px)
    logSerializedWidth("calc(1px / -0)"); // calc(-infinity * 1px)
    
    logSerializedWidth("calc(1px * -infinity * -infinity)"); // calc(infinity * 1px)
    logSerializedWidth("calc(1px * -infinity * infinity)"); // calc(-infinity * 1px)
    
    logSerializedWidth("calc(1px * (NaN + 1))"); // calc(NaN * 1px)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# typedef-calc-keyword](https://drafts.csswg.org/css-values/#typedef-calc-keyword) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword#see_also)

----------------------------------------------------------------------------------------------------

*   [`<calc-sum>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
    
*   `<calc-product>`
*   `<calc-value>`

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/calc-keyword/index.md?plain=1 "Folder: en-us/web/css/reference/values/calc-keyword (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-keyword&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-keyword%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcalc-keyword%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcalc-keyword%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
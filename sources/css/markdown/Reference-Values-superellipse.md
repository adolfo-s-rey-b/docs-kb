*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#mdn-search)
    

`superellipse()` CSS function
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/398)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#browser_compatibility)
 carefully before using this in production.

The **`superellipse()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines the curvature of an ellipse, and is used to specify [corner shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 either directly, or via [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 keywords.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#syntax)

------------------------------------------------------------------------------------------------

css

    superellipse(infinity)
    superellipse(4)
    superellipse(1.7)
    superellipse(0)
    superellipse(-2.8)
    superellipse(-3)
    superellipse(-infinity)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#parameters)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A number in the range of `-infinity` to `infinity`, inclusive.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#return_value)

A superellipse shape.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#description)

----------------------------------------------------------------------------------------------------------

The `superellipse()` function returns a superellipse shape, which is used to specify [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 values. A superellipse is a closed curve symmetric shape between a rectangle and an ellipse. It resembles an ellipse that retains the geometric features of its two axes.

The superellipse shape is calculated using a modified version of an ellipse. The following equation defines an ellipse centered at the origin:

x 2 a 2 + y 2 b 2 \= 1

The `a` and `b` variables refer to the radii of the ellipse, while the `x` and `y` coordinates are points on the ellipse's circumference.

A circle is an ellipse where the radii, the `a` and `b` in the previous equation, are the same length. With `a` and `b` both equal to `r`, the equation for a circle can be written as:

x 2 + y 2 \= r 2

In this equation, the `x` and `y` are coordinates of points on the circle's circumference, and the `r` is the radius of the circle, with the center of the circle being `(0, 0)`. The ellipse is produced by scaling a circle shape along the `x` and/or `y` axis.

A superellipse shape is created by replacing the `2` exponent in each case with 2K, `K` being the argument passed to the `superellipse()` function, which modifies the curvature of the ellipse:

x 2 K + y 2 K \= 1

The following diagram illustrates different `superellipse()` values for the top right corner of a container: `infinity`, `1`, `0`, `-1`, and `-infinity`:

![Line diagram illustrating the ellipses created using different K values, as described subsequently](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse/superellipse-param.svg)

*   A `K` value of `0` creates a straight line. This value can be used to create beveled corners and corresponds to the [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
     `bevel` keyword.
*   A `K` value of `1` creates an ordinary ellipse, corresponding to the `round` keyword.
*   A `K` value of `>1` makes the ellipse shape more square; `2` corresponds to the `squircle` keyword.
*   A `K` value of `infinity` creates a perfect square (corresponding to the `square` keyword), although `K` values of `10` or more are virtually indistinguishable from a square.
*   Negative `K` values result in a concave curve, resulting in corner shapes that are curved inward, or "scooped out". A `K` value of `-1` corresponds to the `scoop` keyword and `-infinity` corresponds to the `notch` keyword.

A negative or positive superellipse would appear symmetrical to a superellipse with its inverse value.

**Note:** For any `K` parameter value passed, the `superellipse()` function's return value will always be the same for that `K` value. When that value is applied to two elements, the appearance of the corner shape may differ if the box size or [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 values differ.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#formal_syntax)

--------------------------------------------------------------------------------------------------------------

<superellipse()> =   
  superellipse( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity )               

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#examples)

----------------------------------------------------------------------------------------------------

### [`superellipse()` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#superellipse_value_comparison)

In this example, two [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 sliders allow you to cycle through many different `corner-shape` `superellipse()` values and [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 values enabling you to compare the effects of each on a container. The code is hidden for brevity, but the full explanation of the [superellipse value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#superellipse_value_comparison)
 is provided on the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 reference page.

    <form>
      <div>
        <label for="superellipse-slider">Choose a superellipse() value:</label>
        <input
          type="range"
          id="superellipse-slider"
          min="-5"
          value="0"
          max="5"
          step="0.1" />
      </div>
      <div>
        <label for="radius-slider">Choose a border-radius value:</label>
        <input type="range" id="radius-slider" min="0" value="45" max="90" />
      </div>
    </form>
    <section></section>
    

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    body {
      width: fit-content;
      margin: 20px auto;
    }
    
    section {
      display: flex;
      justify-content: center;
      align-items: center;
      flex: 100%;
      margin-top: 20px;
    }
    
    form div {
      margin-top: 5px;
      display: flex;
    }
    
    section {
      width: 100%;
      height: 180px;
      background-color: orange;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
    }
    
    section {
      box-shadow: 1px 1px 3px gray;
    }
    

    const rectangle = document.querySelector("section");
    const superEllipseRange = document.getElementById("superellipse-slider");
    const borderRadiusRange = document.getElementById("radius-slider");
    
    function setCorners() {
      const seValue = `superellipse(${superEllipseRange.value})`;
      rectangle.style.cornerShape = seValue;
      const brValue = `${borderRadiusRange.value}px`;
      rectangle.style.borderRadius = brValue;
      rectangle.innerHTML = `<div><code>corner-shape: ${seValue};</code><br><code>border-radius: ${brValue};</code></div>`;
    }
    
    superEllipseRange.addEventListener("input", setCorners);
    borderRadiusRange.addEventListener("input", setCorners);
    setCorners();
    

**Note:** See also the [`<corner-shape-value>` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#corner-shape-value_value_comparison)
 example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Borders and Box Decorations Module Level 4  <br>\# funcdef-superellipse](https://drafts.csswg.org/css-borders-4/#funcdef-superellipse) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#see_also)

----------------------------------------------------------------------------------------------------

*   [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
    
*   [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/superellipse/index.md?plain=1 "Folder: en-us/web/css/reference/values/superellipse (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsuperellipse&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsuperellipse%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsuperellipse%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsuperellipse%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd19dec85109590176f946fcceef48c787d578b1e%0A*+Document+last+modified%3A+2026-08-27T15%3A03%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
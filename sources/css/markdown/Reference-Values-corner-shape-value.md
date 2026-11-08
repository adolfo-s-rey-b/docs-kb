*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#mdn-search)
    

`<corner-shape-value>` CSS type
===============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/398)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#browser_compatibility)
 carefully before using this in production.

The **`<corner-shape-value>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 describes the shape of a container corner. It is used by the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 shorthand property and its [constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#constituent_properties)
 to specify the shape to apply to affected container corners.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#syntax)

------------------------------------------------------------------------------------------------------

The `<corner-shape-value>` data type can take a [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 function that defines a custom shape, or one of six keyword values that describe common `superellipse()` values.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#values)

[`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)

Defines a custom corner superellipse shape. A negative parameter creates an inward, or concave, curve while a positive parameter creates an outward, or convex, curve.

[Keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#keywords)

The available keyword values are as follows:

[`bevel`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#bevel)

Defines a straight, diagonal corner, which is neither convex nor concave. The `bevel` keyword is equivalent to `superellipse(0)`.

[`notch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#notch)

Defines a 90-degree concave square corner. The `notch` keyword is equivalent to `superellipse(-infinity)`.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#round)

Defines a convex ordinary ellipse, which is the standard rounded corner created by [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 without a `corner-shape` applied. The `round` keyword is equivalent to `superellipse(1)`. This is the default (initial) value for all `corner-shape` properties.

[`scoop`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#scoop)

Defines a concave ordinary ellipse. The `scoop` keyword is equivalent to `superellipse(-1)`.

[`square`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#square)

Defines a 90-degree convex square corner, which is the default corner shape when no `border-radius` (or `border-radius: 0`) is applied. The `square` keyword is equivalent to `superellipse(infinity)`.

[`squircle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#squircle)

Defines a "squircle", which is a convex curve in between `round` and `square`. The `squircle` keyword is equivalent to `superellipse(2)`.

**Note:** You can smoothly animate between different `superellipse()` values, and between different corner shape keywords, as the animation interpolates between their `superellipse()` equivalents.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

<corner-shape-value> =   
  round             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scoop             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bevel             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  notch             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  square            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  squircle          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <superellipse()>    
  
[<superellipse()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 =   
  superellipse( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity )               

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#examples)

----------------------------------------------------------------------------------------------------------

### [`<corner-shape-value>` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#corner-shape-value_value_comparison)

In this example, we provide a drop-down menu allowing you to select different `<corner-shape-value>` values and a slider that updates the container's [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
. This enables visualizing the effect of the different keywords and `superellipse()` parameter values.

The `corner-shape` property defines the shape of the box's corners while the region the shape is applied to is specified by the `border-radius` property. The code is hidden for brevity, but you can find a [full explanation of `corner-shape` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#comparing_corner-shape_values)
 along with other related examples on the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 reference page.

    <form>
      <div>
        <label for="corner-shape-choice">Choose a corner-shape value:</label>
        <select id="corner-shape-choice">
          <optgroup label="Keywords">
            <option value="square">square | superellipse(infinity)</option>
            <option selected value="squircle">squircle | superellipse(2)</option>
            <option value="round">round | superellipse(1)</option>
            <option value="bevel">bevel | superellipse(0)</option>
            <option value="scoop">scoop | superellipse(-1)</option>
            <option value="notch">notch | superellipse(-infinity)</option>
          </optgroup>
          <optgroup label="Functions">
            <option>superellipse(3)</option>
            <option>superellipse(1.5)</option>
            <option>superellipse(0.5)</option>
            <option>superellipse(-0.5)</option>
            <option>superellipse(-1.5)</option>
            <option>superellipse(-3)</option>
          </optgroup>
        </select>
      </div>
      <div>
        <label for="radius-slider">Choose a border-radius value:</label>
        <input
          type="range"
          id="radius-slider"
          min="0"
          value="45"
          max="90"
          step="1" />
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
      margin-top: 20px;
    }
    
    select {
      padding: 3px 5px;
    }
    
    form div:nth-of-type(2) {
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
    const select = document.querySelector("select");
    const range = document.getElementById("radius-slider");
    
    function setCorners() {
      rectangle.style.cornerShape = select.value;
      const brValue = `${range.value}px`;
      rectangle.style.borderRadius = brValue;
      rectangle.innerHTML = `<div><code>corner-shape: ${select.value};</code><br><code>border-radius: ${brValue};</code></div>`;
    }
    
    select.addEventListener("change", setCorners);
    range.addEventListener("input", setCorners);
    setCorners();
    

**Note:** See also the [`superellipse()` function value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse#superellipse_value_comparison)
 example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Borders and Box Decorations Module Level 4  <br>\# typedef-corner-shape-value](https://drafts.csswg.org/css-borders-4/#typedef-corner-shape-value) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value#see_also)

----------------------------------------------------------------------------------------------------------

*   [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    
*   [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/corner-shape-value/index.md?plain=1 "Folder: en-us/web/css/reference/values/corner-shape-value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcorner-shape-value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcorner-shape-value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcorner-shape-value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcorner-shape-value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
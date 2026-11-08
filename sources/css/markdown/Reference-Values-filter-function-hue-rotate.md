*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#mdn-search)
    

`hue-rotate()` CSS function
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hue-rotate()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 rotates the [hue](https://en.wikipedia.org/wiki/Hue "External link (opens in new tab)")
 of an element and its contents. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

**Note:** `hue-rotate()` is specified as a matrix operation on the RGB color. It does not actually convert the color to the HSL model, which is a non-linear operation. Therefore, it may not preserve the saturation or lightness of the original color, especially for saturated colors.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#try_it)

--------------------------------------------------------------------------------------------------------------

    filter: hue-rotate(0);
    

    filter: hue-rotate(90deg);
    

    filter: hue-rotate(-0.25turn);
    

    filter: hue-rotate(3.142rad);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* No rotation */
    hue-rotate()
    hue-rotate(0deg)
    
    /* Half-turn rotation */
    hue-rotate(-180deg)
    hue-rotate(540deg)
    hue-rotate(200grad)
    hue-rotate(3.14159rad)
    hue-rotate(0.5turn)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#parameters)

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 Optional

Specifies the relative change in hue of the input sample. A value of `0deg` leaves the input unchanged. A positive hue rotation increases the hue value, while a negative rotation decreases the hue value. The initial value for [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 is `0`. There is no minimum or maximum value. Given `hue-rotate(Ndeg)`, the effect evaluates to `N` modulo 360. The default value is `0deg`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

<hue-rotate()> =   
  hue-rotate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#examples)

------------------------------------------------------------------------------------------------------------------

### [With the backdrop-filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#with_the_backdrop-filter_property)

This example applies a `hue-rotate()` filter via the `backdrop-filter` CSS property to the paragraph, color shifting to the area behind the `<p>`.

css

    .container {
      background: url("/shared-assets/images/examples/listen_to_black_women.jpg")
        no-repeat left / contain #011296;
    }
    p {
      backdrop-filter: hue-rotate(240deg);
      text-shadow: 2px 2px #011296;
    }
    

    .container {
      padding: 3rem;
      width: 30rem;
    }
    p {
      padding: 0.5rem;
      color: white;
      font-size: 2rem;
      font-family: sans-serif;
    }
    

    <div class="container">
      <p>
        Text on images can be illegible and inaccessible even with a drop shadow.
      </p>
    </div>
    

### [With the filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#with_the_filter_property)

This example applies a `hue-rotate()` filter via the `filter` CSS property adding the color shift to the entire element, including content, border, and background image.

css

    p {
      filter: hue-rotate(-60deg);
      text-shadow: 2px 2px blue;
      background-color: magenta;
      color: goldenrod;
      border: 1em solid rebeccapurple;
      box-shadow:
        inset -5px -5px red,
        5px 5px yellow;
    }
    

    p {
      padding: 0.5rem;
      font-size: 2rem;
      font-family: sans-serif;
      width: 85vw;
    }
    

    <p>The person who wrote this example is not a designer, fortunately.</p>
    

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#using_the_svg_filter)

This example shows three images for comparison: an image with a `hue-rotate()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feColorMatrix>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feColorMatrix)
 filter element can also be used to rotate the hue of content. We set the `type` to `hueRotate` and the `values` to the angle in degrees, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="hue-rotate90" color-interpolation-filters="sRGB">
        <feColorMatrix type="hueRotate" values="90" />
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: hue-rotate(90deg);
    filter: url("#hue-rotate90"); /* with embedded SVG */
    filter: url("fileName.svg#hue-rotate90"); /* external SVG */
    

#### CSS

We include CSS that will rotate the hue of elements based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: hue-rotate(90deg);
    }
    
    .svg-filter {
      filter: url("#hue-rotate90");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>hue-rotate()</code> filter</th>
          <th>SVG filter equivalent</th>
          <th>Original image</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <img
              class="css-filter"
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              class="svg-filter"
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
          <td>
            <img
              src="https://mdn.github.io/shared-assets/images/examples/progress-pride-flag.jpg"
              alt="Pride flag" />
          </td>
        </tr>
      </tbody>
    </table>
    

### [hue-rotate() does not preserve saturation or lightness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#hue-rotate_does_not_preserve_saturation_or_lightness)

The diagram below compares two color gradients starting with red: the first is generated using `hue-rotate()`, and the second uses actual HSL color values. Note how the `hue-rotate()` gradient shows obvious differences in saturation and lightness in the middle.

html

    <div>
      <p>Using <code>hue-rotate()</code></p>
      <div id="hue-rotate"></div>
    </div>
    <div>
      <p>Using <code>hsl()</code></p>
      <div id="hsl"></div>
    </div>
    

    #hue-rotate,
    #hsl {
      display: flex;
      margin: 1em 0;
    }
    
    #hue-rotate div,
    #hsl div {
      width: 2px;
      height: 100px;
    }
    

js

    const hueRotate = document.getElementById("hue-rotate");
    const hsl = document.getElementById("hsl");
    
    for (let i = 0; i < 360; i++) {
      const div1 = document.createElement("div");
      div1.style.backgroundColor = `hsl(${i}, 100%, 50%)`;
      hsl.appendChild(div1);
    
      const div2 = document.createElement("div");
      div2.style.backgroundColor = "red";
      div2.style.filter = `hue-rotate(${i}deg)`;
      hueRotate.appendChild(div2);
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-hue-rotate](https://drafts.csswg.org/filter-effects/#funcdef-filter-hue-rotate) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate#see_also)

------------------------------------------------------------------------------------------------------------------

*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
     module
*   The other [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
     functions available to be used in values of the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
     properties include:
    *   [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
        
    *   [`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
        
    *   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
        
    *   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
        
    *   [`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
        
    *   [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
        
    *   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
        
    *   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
        
    *   [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/hue-rotate/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/hue-rotate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fhue-rotate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fhue-rotate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fhue-rotate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fhue-rotate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#mdn-search)
    

`brightness()` CSS function
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`brightness()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 applies a linear multiplier value on an element or an input image, making the image appear brighter or darker. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#try_it)

--------------------------------------------------------------------------------------------------------------

    filter: brightness(1);
    

    filter: brightness(1.75);
    

    filter: brightness(50%);
    

    filter: brightness(0);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* Completely black */
    brightness(0)
    
    /* No change */
    brightness()
    brightness(1)
    brightness(100%)
    
    /* 60% brightness */
    brightness(.6)
    brightness(60%)
    
    /* Double brightness */
    brightness(2)
    brightness(200%)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#parameters)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

Specifies the amount of the conversion. A value less than `100%` darkens the input image or element, while a value over `100%` brightens it. A value of `0%` creates a completely black image or element, while a value of `100%` leaves the input unchanged. Values between `0%` and `100%` are linear multipliers on the effect. Values greater than `100%` are allowed, providing brighter results. The initial value for [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 is `1`. Negative values are not allowed. The default value is `1`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

<brightness()> =   
  brightness( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#examples)

------------------------------------------------------------------------------------------------------------------

### [Applying brightness using the backdrop-filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#applying_brightness_using_the_backdrop-filter_property)

This example shows how to apply the `brightness()` filter to a paragraph via the [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 CSS property.

#### CSS

css

    .container {
      background: url("be_fierce.jpg") no-repeat right / contain #d4d5b2;
    }
    p {
      backdrop-filter: brightness(150%);
      text-shadow: 2px 2px white;
    }
    

    .container {
      padding: 5rem 3rem 1rem;
      width: 30rem;
    }
    p {
      padding: 0.5rem;
      color: black;
      font-size: 2rem;
      font-family: sans-serif;
    }
    

    <div class="container">
      <p>
        Text on images can be illegible and inaccessible even with a drop shadow.
      </p>
    </div>
    

#### Result

In this example, the colors in the area behind the `<p>` element shift linearly. If the `backdrop-filter` property was set to `brightness(0%)`, the `<div>` area with the `<p>` element would have been black and hidden the image behind. At `brightness(100%)`, the `<div>` area color would be the same as the input `#d4d5b2`, and the image behind would be completely transparent. With the brightness set to `150%` as in this example, the colors in the image behind are getting hidden by the brightness of the `<div>` element.

### [Applying brightness using the filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#applying_brightness_using_the_filter_property)

In this example, a `brightness()` filter is applied to the entire element, including content, border, and background image via the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 CSS property. The result shows three variations of different brightness values.

css

    p:first-of-type {
      filter: brightness(50%);
    }
    p:last-of-type {
      filter: brightness(200%);
    }
    

    p {
      text-shadow: 2px 2px blue;
      background-color: magenta;
      color: palegoldenrod;
      border: 1em solid rebeccapurple;
      box-shadow:
        inset -5px -5px red,
        5px 5px yellow;
      padding: 0.25rem;
      font-size: 1.25rem;
      font-family: sans-serif;
      width: 85vw;
    }
    

    <p>This paragraph has reduced brightness.</p>
    <p>This paragraph has normal brightness.</p>
    <p>This paragraph has increased brightness.</p>
    

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#using_the_svg_filter)

This example shows three images for comparison: an image with a `brightness()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feComponentTransfer>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feComponentTransfer)
 filter element can also be used to adjust the brightness of content by creating equivalent brightness adjustments on nested [`<feFuncR>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncR)
, [`<feFuncG>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncG)
, and [`<feFuncB>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncB)
 linear elements. We set the same `slope` for the red, green, and blue filter primitives, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="brightness75" color-interpolation-filters="sRGB">
        <feComponentTransfer>
          <feFuncR type="linear" slope="0.75" />
          <feFuncG type="linear" slope="0.75" />
          <feFuncB type="linear" slope="0.75" />
        </feComponentTransfer>
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: brightness(0.75);
    filter: brightness(75%);
    filter: url("#brightness75"); /* with embedded SVG */
    filter: url("fileName.svg#brightness75"); /* external SVG */
    

#### CSS

We include CSS that will adjust the brightness of elements based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: brightness(0.75);
    }
    
    .svg-filter {
      filter: url("#brightness75");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>brightness()</code> filter</th>
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-brightness](https://drafts.csswg.org/filter-effects/#funcdef-filter-brightness) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness#see_also)

------------------------------------------------------------------------------------------------------------------

*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
     module
*   The other [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
     functions available to be used in values of the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
     properties include:
    *   [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
        
    *   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
        
    *   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
        
    *   [`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
        
    *   [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
        
    *   [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
        
    *   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
        
    *   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
        
    *   [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/brightness/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/brightness (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fbrightness&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fbrightness%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fbrightness%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fbrightness%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
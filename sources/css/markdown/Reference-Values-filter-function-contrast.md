*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#mdn-search)
    

`contrast()` CSS function
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contrast()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 adjusts the contrast of the input image. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#try_it)

------------------------------------------------------------------------------------------------------------

    filter: contrast(1);
    

    filter: contrast(1.75);
    

    filter: contrast(50%);
    

    filter: contrast(0);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Completely gray */
    contrast(0)
    
    /* No change */
    contrast()
    contrast(1)
    contrast(100%)
    
    /* 60% contrast */
    contrast(.6)
    contrast(60%)
    
    /* Double contrast */
    contrast(2)
    contrast(200%)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#parameters)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

Specifies the amount of the conversion. A value under `100%` decreases the contrast, while a value over `100%` increases it. A value of `0` or `0%` will create an image that is completely gray, while a value of `1` or `100%` leaves the input unchanged. Negative values are not allowed. The initial value for [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 is `1`. The default value is `1`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

<contrast()> =   
  contrast( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#examples)

----------------------------------------------------------------------------------------------------------------

### [With the backdrop-filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#with_the_backdrop-filter_property)

This example applies a `contrast()` filter via the [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 CSS property to the paragraph, shifting the color of the area behind the `<p>`.

css

    .container {
      background: url("unity_for_the_people.jpg") no-repeat center / contain #333399;
    }
    p {
      backdrop-filter: contrast(0.2);
    }
    

    .container {
      padding: 3rem;
      width: 30rem;
    }
    p {
      padding: 0.5rem;
      color: white;
      font-family: sans-serif;
    }
    

    <div class="container">
      <p>
        Always ensure there is enough contrast between text and all background
        colors. If you think your text may land on top of a background image,
        include a <code>backdrop-filter</code>. Reducing the contrast of background
        colors with the <code>contrast()</code> filter may improve legibility but
        does not guarantee accessibility.
      </p>
    </div>
    

### [With the filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#with_the_filter_property)

This example applies a `contrast()` filter via the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 CSS property, changing contrast by shifting colors of the entire element, including content, border, background, and shadows.

css

    p:first-of-type {
      filter: contrast(30%);
    }
    p:last-of-type {
      filter: contrast(300%);
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
    

    <p>This paragraph has reduced contrast.</p>
    <p>This paragraph has normal contrast.</p>
    <p>This paragraph has increased contrast.</p>
    

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#using_the_svg_filter)

This example shows three images for comparison: an image with a `contrast()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feComponentTransfer>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feComponentTransfer)
 filter element can also be used to adjust the contrast of content by creating equivalent contrast adjustments on nested [`<feFuncR>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncR)
, [`<feFuncG>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncG)
, and [`<feFuncB>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncB)
 linear elements. We set the same `slope` and `intercept` for the red, green, and blue filter primitives, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="contrast200" color-interpolation-filters="sRGB">
        <feComponentTransfer>
          <feFuncR type="linear" slope="2" intercept="-0.5" />
          <feFuncG type="linear" slope="2" intercept="-0.5" />
          <feFuncB type="linear" slope="2" intercept="-0.5" />
        </feComponentTransfer>
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: contrast(2);
    filter: contrast(200%);
    filter: url("#contrast200"); /* with embedded SVG */
    filter: url("fileName.svg#contrast200"); /* external SVG */
    

#### CSS

We include CSS that will adjust the contrast of elements based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: contrast(2);
    }
    
    .svg-filter {
      filter: url("#contrast200");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>contrast()</code> filter</th>
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-contrast](https://drafts.csswg.org/filter-effects/#funcdef-filter-contrast) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast#see_also)

----------------------------------------------------------------------------------------------------------------

*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
     module
*   The other [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
     functions available to be used in values of the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
     properties include:
    *   [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
        
    *   [`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
        
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

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/contrast/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/contrast (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fcontrast&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fcontrast%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fcontrast%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fcontrast%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
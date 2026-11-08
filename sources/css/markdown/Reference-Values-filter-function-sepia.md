*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#mdn-search)
    

`sepia()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sepia()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 converts the input image to sepia, giving it a warmer, more yellow/brown appearance. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#try_it)

---------------------------------------------------------------------------------------------------------

    filter: sepia(0);
    

    filter: sepia(0.2);
    

    filter: sepia(60%);
    

    filter: sepia(1);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* No sepia conversion */
    sepia(0)
    
    /* Complete sepia conversion */
    sepia()
    sepia(1)
    sepia(100%)
    
    /* 60% sepia conversion */
    sepia(.6)
    sepia(60%)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#parameters)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

Specifies the amount of the conversion. A value of `100%` applies a complete sepia conversion, while a value of `0%` leaves the input unchanged. Values between `0%` and `100%` are linear multipliers on the effect. Values above `100%` are allowed, but the effect is clamped to `100%`. Negative values are not allowed. The initial value for [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 is `0`. The default value is `1`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

<sepia()> =   
  sepia( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#examples)

-------------------------------------------------------------------------------------------------------------

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#using_the_svg_filter)

This example shows three images for comparison: an image with a `sepia()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feColorMatrix>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feColorMatrix)
 filter element can also be used to convert content to sepia. We set the `values` for the color matrix, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="sepia70" color-interpolation-filters="sRGB">
        <feColorMatrix
          type="matrix"
          values="0.5751 0.5383 0.1323 0 0
                  0.2443 0.7802 0.1176 0 0
                  0.1904 0.3738 0.3917 0 0
                  0 0 0 1 0" />
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: sepia(0.7);
    filter: sepia(70%);
    filter: url("#sepia70"); /* with embedded SVG */
    filter: url("fileName.svg#sepia70"); /* external SVG */
    

#### CSS

We include CSS that will convert elements to sepia based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: sepia(0.7);
    }
    
    .svg-filter {
      filter: url("#sepia70");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>sepia()</code> filter</th>
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-sepia](https://drafts.csswg.org/filter-effects/#funcdef-filter-sepia) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia#see_also)

-------------------------------------------------------------------------------------------------------------

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
        
    *   [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
        
    *   [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
        
    *   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
        
    *   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/sepia/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/sepia (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fsepia&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fsepia%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fsepia%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fsepia%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#mdn-search)
    

`invert()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`invert()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 inverts the color samples in the input image. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#try_it)

----------------------------------------------------------------------------------------------------------

    filter: invert(0);
    

    filter: invert(0.3);
    

    filter: invert(50%);
    

    filter: invert(70%);
    

    filter: invert(1);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* No inversion */
    invert(0)
    
    /* Complete inversion */
    invert()
    invert(1)
    invert(100%)
    
    /* 60% inversion */
    invert(.6)
    invert(60%)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#parameters)

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 Optional

Specifies the amount of the conversion. A value of `100%` applies a complete inversion, while a value of `0%` leaves the input unchanged. Values between `0%` and `100%` are linear multipliers on the effect. Values above `100%` are allowed, but the effect is clamped to `100%`. Negative values are not allowed. The initial value for [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 is `0`. The default value is `1`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

<invert()> =   
  invert( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#examples)

--------------------------------------------------------------------------------------------------------------

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#using_the_svg_filter)

This example shows three images for comparison: an image with an `invert()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feComponentTransfer>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feComponentTransfer)
 filter element can also be used to invert content by creating equivalent inversion on nested [`<feFuncR>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncR)
, [`<feFuncG>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncG)
, and [`<feFuncB>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feFuncB)
 table elements. We set the same `tableValue` for the red, green, and blue filter primitives to the same value, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="invert70" color-interpolation-filters="sRGB">
        <feComponentTransfer>
          <feFuncR type="table" tableValues="0.7 0.3" />
          <feFuncG type="table" tableValues="0.7 0.3" />
          <feFuncB type="table" tableValues="0.7 0.3" />
        </feComponentTransfer>
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: invert(0.7);
    filter: invert(70%);
    filter: url("#invert70"); /* with embedded SVG */
    filter: url("fileName.svg#invert70"); /* external SVG */
    

#### CSS

We include CSS that will invert elements based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: invert(0.7);
    }
    
    .svg-filter {
      filter: url("#invert70");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>invert()</code> filter</th>
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-invert](https://drafts.csswg.org/filter-effects/#funcdef-filter-invert) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert#see_also)

--------------------------------------------------------------------------------------------------------------

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
        
    *   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
        
    *   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
        
    *   [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/invert/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/invert (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Finvert&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Finvert%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Finvert%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Finvert%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
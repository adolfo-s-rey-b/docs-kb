*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#mdn-search)
    

`drop-shadow()` CSS function
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`drop-shadow()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 applies a drop shadow effect to the input image. It is used as a value for the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
 and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
 properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#try_it)

---------------------------------------------------------------------------------------------------------------

    filter: drop-shadow(30px 10px 4px #4444dd);
    

    filter: drop-shadow(0 -6mm 4mm rgb(160 0 210));
    

    filter: drop-shadow(0 0 0.75rem crimson);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

A drop shadow is effectively a blurred, offset version of the input image's alpha mask, drawn in a specific color and composited below the image.

**Note:** This function is somewhat similar to the [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 property. The `box-shadow` property creates a rectangular shadow behind an element's _entire box_, while the `drop-shadow()` filter function creates a shadow that conforms to the shape (alpha channel) of the _image itself_.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* Two length values */
    /* drop-shadow( <length> <length> ) */
    drop-shadow(5px 5px)
    
    /* Three length values */
    /* drop-shadow( <length> <length> <length> ) */
    drop-shadow(5px 5px 15px)
    
    /* Two length values and a color */
    /* drop-shadow( <length> <length> <color> ) */
    drop-shadow(5px 5px red)
    
    /* Three length values and a color */
    /* drop-shadow( <length> <length> <length> <color> ) */
    drop-shadow(5px 5px 15px red)
    
    /* The order of color and length values can be changed */
    /* drop-shadow( <color> <length> <length> <length> ) */
    drop-shadow(#ee2233 0.5rem 0.5rem 1rem)
    
    /* Pass multiple drop-shadows to a filter to stack them */
    drop-shadow(10px 10px red) drop-shadow(-5px -5px yellow)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#parameters)

The `drop-shadow()` function accepts two or three [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values and an optional [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value, separated by spaces.

[`<color>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#color)

Specifies the color for the shadow. If not specified, the value of the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property defined on the element is used.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#length)

Specifies the offset length of the shadow. This parameter accepts two or three values. If two values are specified, they are interpreted as `<offset-x>` (horizontal offset) and `<offset-y>` (vertical offset) values. Negative `<offset-x>` value places the shadow to the left of the element. Negative `<offset-y>` value places the shadow above the element. If a third value is specified, it is interpreted as `<standard-deviation>`, which is the value of the standard deviation to the [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur "External link (opens in new tab)")
 function. A larger `<standard-deviation>` value creates a larger and more blurred shadow. Negative values for `<standard-deviation>` are not allowed.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#return_value)

A [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

<drop-shadow()> =   
  drop-shadow( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
[{2,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#examples)

-------------------------------------------------------------------------------------------------------------------

### [Setting a drop shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#setting_a_drop_shadow)

html

    <div>drop-shadow(16px 16px)</div>
    <div>drop-shadow(16px 16px red)</div>
    <div>drop-shadow(red 1rem 1rem 10px)</div>
    <div>drop-shadow(-16px -16px red)</div>
    <div>
      drop-shadow(1px 1px red) drop-shadow(1px -1px red) drop-shadow(-1px 1px red)
      drop-shadow(-1px -1px red)
    </div>
    

css

    div {
      display: inline-block;
      margin: 0 0.5rem 2rem 1rem;
      padding: 0.5rem;
      height: 100px;
      width: 190px;
      vertical-align: top;
      background-color: #222222;
    
      color: lime;
    }
    
    div:nth-child(1) {
      filter: drop-shadow(16px 16px);
    }
    
    div:nth-child(2) {
      filter: drop-shadow(16px 16px red);
    }
    
    div:nth-child(3) {
      filter: drop-shadow(red 1rem 1rem 10px);
    }
    
    div:nth-child(4) {
      filter: drop-shadow(-16px -16px red);
    }
    
    div:nth-child(5) {
      filter: drop-shadow(1px 1px red) drop-shadow(1px -1px red)
        drop-shadow(-1px 1px red) drop-shadow(-1px -1px red);
    }
    

In the absence of a `<color>` value in the `drop-shadow()` function in the first box, the shadow uses the value of the `color` property from the element (`lime`). The second and third shadows illustrate that the length and color values can be specified in any order. The third shadow shows the blurring effect when a third `<length>` value is specified. The fourth shadow uses negative offsets, which shift the shadow to the left and top. The fifth example shows how to use multiple drop-shadows on a single element.

### [Using the SVG filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#using_the_svg_filter)

This example shows three images for comparison: an image with a `drop-shadow()` filter function applied, an image with the equivalent SVG filter applied, and the original image.

#### SVG

The SVG [`<feDropShadow>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDropShadow)
 filter element can also be used to apply a drop shadow to content. We set the `dx` and `dy` offsets, the `stdDeviation`, and the `flood-color`, then we can reference the SVG effect by the ID of the [`<filter>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/filter)
:

html

    <svg height="0" role="none">
      <filter id="drop-shadow5" color-interpolation-filters="sRGB">
        <feDropShadow dx="5" dy="5" stdDeviation="3" flood-color="black" />
      </filter>
    </svg>
    

The following declarations produce the same effect:

css

    filter: drop-shadow(5px 5px 3px black);
    filter: url("#drop-shadow5"); /* with embedded SVG */
    filter: url("fileName.svg#drop-shadow5"); /* external SVG */
    

#### CSS

We include CSS that will apply a drop shadow to elements based on their `css-filter` or `svg-filter` class:

css

    .css-filter {
      filter: drop-shadow(5px 5px 3px black);
    }
    
    .svg-filter {
      filter: url("#drop-shadow5");
    }
    

    th,
    td {
      padding: 5px;
    }
    

    <table>
      <thead>
        <tr>
          <th><code>drop-shadow()</code> filter</th>
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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Filter Effects Module Level 1  <br>\# funcdef-filter-drop-shadow](https://drafts.csswg.org/filter-effects/#funcdef-filter-drop-shadow) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Filter_effects)
     module
*   The other [`<filter-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
     functions available to be used in values of the [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
     and [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
     properties include:
    *   [`blur()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
        
    *   [`brightness()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
        
    *   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
        
    *   [`grayscale()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
        
    *   [`hue-rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
        
    *   [`invert()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
        
    *   [`opacity()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
        
    *   [`saturate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
        
    *   [`sepia()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/filter-function/drop-shadow/index.md?plain=1 "Folder: en-us/web/css/reference/values/filter-function/drop-shadow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fdrop-shadow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fdrop-shadow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffilter-function%2Fdrop-shadow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffilter-function%2Fdrop-shadow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35b1d907e22f58fcd01fc5d3d22f1e73089c7f3d%0A*+Document+last+modified%3A+2026-11-03T21%3A02%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
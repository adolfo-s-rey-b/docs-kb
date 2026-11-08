*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#mdn-search)
    

`background-color` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the background color of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#try_it)

--------------------------------------------------------------------------------------------------------

    background-color: brown;
    

    background-color: #74992e;
    

    background-color: rgb(255 255 128);
    

    background-color: rgb(255 255 128 / 0.5);
    

    background-color: hsl(50 33% 25%);
    

    background-color: hsl(50 33% 25% / 0.75);
    

    <section id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #example-element {
      min-width: 100%;
      min-height: 100%;
      padding: 10%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-color: red;
    background-color: indigo;
    
    /* Hexadecimal value */
    background-color: #bbff00; /* Fully opaque */
    background-color: #bf0; /* Fully opaque shorthand */
    background-color: #11ffee00; /* Fully transparent */
    background-color: #1fe0; /* Fully transparent shorthand */
    background-color: #11ffeeff; /* Fully opaque */
    background-color: #1fef; /* Fully opaque shorthand */
    
    /* RGB value */
    background-color: rgb(255 255 128); /* Fully opaque */
    background-color: rgb(117 190 218 / 50%); /* 50% transparent */
    
    /* HSL value */
    background-color: hsl(50 33% 25%); /* Fully opaque */
    background-color: hsl(50 33% 25% / 75%); /* 75% opaque, i.e. 25% transparent */
    
    /* Special keyword values */
    background-color: currentColor;
    background-color: transparent;
    
    /* Global values */
    background-color: inherit;
    background-color: initial;
    background-color: revert;
    background-color: revert-layer;
    background-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#values)

This property is specified as one `<color>` value:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The uniform color of the background. It is rendered behind any [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 that is specified, although the color will still be visible through any transparency in the image.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#description)

------------------------------------------------------------------------------------------------------------------

The `background-color` property sets the background color of an element box. The color is drawn behind any background images. By default, the background color is painted within the [border-box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#border_area)
, meaning it's painted behind the border, ending at the outer edge of the border-box.

Clipping of the `background-color` paint area is controlled via the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 property. If multiple background images are set, the background color's clipping is determined by the value of the `background-clip` associated with the bottom-most background image.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#accessibility)

----------------------------------------------------------------------------------------------------------------------

It is important to ensure that the contrast ratio between the background color and the color of the text placed over it is high enough that people experiencing low vision conditions will be able to read the content of the page. A high contrast ratio also improves content accessibility for glossy-screened mobile device users when in a bright environment, such as sunlight.

Color contrast ratio is determined by comparing the luminance of the text and background color values. In order to meet current [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, a ratio of 4.5:1 is required for text content and 3:1 for larger text such as headings. Large text is defined as 18.66px and [bold](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 or larger, or 24px or larger.

*   [Understanding WCAG: Perceivable Guideline 1.4.3](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
    
*   [Understanding color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
    
*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [Understanding Success Criterion 1.4.3 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `transparent` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | computed color |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

background-color =   
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#examples)

------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#basic_example)

This example demonstrates applying `background-color` to HTML [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements using different CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 values.

#### HTML

html

    <p class="example-one">Lorem ipsum dolor sit amet, consectetuer</p>
    
    <p class="example-two">Lorem ipsum dolor sit amet, consectetuer</p>
    
    <p class="example-three">Lorem ipsum dolor sit amet, consectetuer</p>
    

#### CSS

Each paragraph is set to a different background color, including explicitly setting the default [`transparent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color#transparent)
, an [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 color function, and a [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
. We also set the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property to ensure enough contrast between the text and its background.

css

    .example-one {
      background-color: transparent;
    }
    
    .example-two {
      background-color: rgb(153 102 153);
      color: rgb(255 255 204);
    }
    
    .example-three {
      background-color: #777799;
      color: white;
    }
    

#### Result

### [Colorized tables](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#colorized_tables)

This example demonstrates the use of `background-color` on HTML [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 elements, including [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 rows and [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 cells. It also demonstrates how background colors are painted behind any borders.

#### HTML

html

    <table>
      <tbody>
        <tr id="r1">
          <td id="c11">11</td>
          <td id="c12">12</td>
          <td id="c13">13</td>
        </tr>
        <tr id="r2">
          <td id="c21">21</td>
          <td id="c22">22</td>
          <td id="c23">23</td>
        </tr>
        <tr id="r3">
          <td id="c31">31</td>
          <td id="c32">32</td>
          <td id="c33">33</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

We use CSS to set different [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 values. We also set a large dashed border on the table and every cell to demonstrate how the `background-color` is painted to the outer edge of the border-box.

css

    table {
      border-collapse: collapse;
      border: dashed black 5px;
      width: 250px;
      height: 150px;
    }
    td {
      border: dashed 5px black;
    }
    #r1 {
      background-color: lightblue;
    }
    #c12 {
      background-color: cyan;
    }
    #r2 {
      background-color: grey;
    }
    #r3 {
      background-color: olive;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-color](https://drafts.csswg.org/css-backgrounds/#background-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color#see_also)

------------------------------------------------------------------------------------------------------------

*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [Multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   Other color-related properties: [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
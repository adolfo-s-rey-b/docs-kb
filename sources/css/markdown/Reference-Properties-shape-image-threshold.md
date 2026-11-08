*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#mdn-search)
    

`shape-image-threshold` CSS property
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`shape-image-threshold`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the alpha channel threshold used to extract the shape using an image as the value for [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
.

Any pixels whose alpha component's value is greater than the threshold are considered to be part of the shape for the purposes of determining its boundaries. For example, a value of `0.5` means that the shape will enclose all the pixels that are more than 50% opaque.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#try_it)

-------------------------------------------------------------------------------------------------------------

    shape-outside: linear-gradient(
      50deg,
      rgb(77 26 103),
      transparent 80%,
      transparent
    );
    shape-image-threshold: 0.2;
    

    shape-outside: linear-gradient(
      50deg,
      rgb(77 26 103),
      transparent 80%,
      transparent
    );
    shape-image-threshold: 0.4;
    

    shape-outside: linear-gradient(
      50deg,
      rgb(77 26 103),
      transparent 80%,
      transparent
    );
    shape-image-threshold: 0.6;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element"></div>
        We had agreed, my companion and I, that I should call for him at his house,
        after dinner, not later than eleven o'clock. This athletic young Frenchman
        belongs to a small set of Parisian sportsmen, who have taken up "ballooning"
        as a pastime. After having exhausted all the sensations that are to be found
        in ordinary sports, even those of "automobiling" at a breakneck speed, the
        members of the "Aéro Club" now seek in the air, where they indulge in all
        kinds of daring feats, the nerve-racking excitement that they have ceased to
        find on earth.
      </div>
    </section>
    

    .example-container {
      text-align: left;
      padding: 20px;
    }
    
    #example-element {
      float: left;
      width: 150px;
      height: 150px;
      margin: 20px;
      background-image: linear-gradient(
        50deg,
        rgb(77 26 103),
        transparent 80%,
        transparent
      );
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* <number> value */
    shape-image-threshold: 0.7;
    
    /* Global values */
    shape-image-threshold: inherit;
    shape-image-threshold: initial;
    shape-image-threshold: revert;
    shape-image-threshold: revert-layer;
    shape-image-threshold: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#values)

[`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)

Sets the threshold used for extracting a shape from an image. The shape is defined by the pixels whose alpha value is greater than the threshold. Values outside the range 0.0 (fully transparent) to 1.0 (fully opaque) are clamped to this range.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0.0` |
| Applies to | floats |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The same as the specified value after clipping the [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)<br> to the range \[0.0, 1.0\]. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [number](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation "Values of the <number> CSS data type are interpolated as real, floating-point, numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

shape-image-threshold =   
  <opacity-value>    
  
<opacity-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#examples)

-----------------------------------------------------------------------------------------------------------------

### [Aligning text to a gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#aligning_text_to_a_gradient)

This example creates a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 block with a gradient background image. The gradient is established as a CSS shape using `shape-outside`, so that pixels within the gradient which are at least 20% opaque (that is, those pixels with an alpha component greater than 0.2) are considered part of the shape.

#### HTML

html

    <div id="gradient-shape"></div>
    
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel at commodi
      voluptates enim, distinctio officia. Saepe optio accusamus doloribus sint
      facilis itaque ab nulla, dolor molestiae assumenda cum sit placeat adipisci,
      libero quae nihil porro debitis laboriosam inventore animi impedit nostrum
      nesciunt quisquam expedita! Dolores consectetur iure atque a mollitia dicta
      repudiandae illum exercitationem aliquam repellendus ipsum porro modi, id nemo
      eligendi, architecto ratione quibusdam iusto nisi soluta? Totam inventore ea
      eum sed velit et eligendi suscipit accusamus iusto dolore, at provident eius
      alias maxime pariatur non deleniti ipsum sequi rem eveniet laboriosam magni
      expedita?
    </p>
    

#### CSS

css

    #gradient-shape {
      width: 150px;
      height: 150px;
      float: left;
      background-image: linear-gradient(30deg, black, transparent 80%, transparent);
      shape-outside: linear-gradient(30deg, black, transparent 80%, transparent);
      shape-image-threshold: 0.2;
    }
    

The shape is established here using [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 with a linear gradient rather than an image file. The same gradient is also used as the image from which the shape is derived for establishing the float area, using the [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property.

The 20% opacity threshold for treating gradient pixels as part of the shape is then established using `shape-image-threshold` with a value of `0.2`.

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# shape-image-threshold-property](https://drafts.csswg.org/css-shapes/#shape-image-threshold-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [CSS Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
    
*   [Overview of CSS Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    
*   [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [`shape-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/shape-image-threshold/index.md?plain=1 "Folder: en-us/web/css/reference/properties/shape-image-threshold (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-image-threshold&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-image-threshold%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-image-threshold%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-image-threshold%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
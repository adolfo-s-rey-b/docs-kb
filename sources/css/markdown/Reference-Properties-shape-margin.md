*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#mdn-search)
    

`shape-margin` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`shape-margin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets a margin for a CSS shape created using [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
.

The margin lets you adjust the distance between the edges of the shape (the **float element**) and the surrounding content.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#try_it)

----------------------------------------------------------------------------------------------------

    shape-margin: 0;
    

    shape-margin: 20px;
    

    shape-margin: 1em;
    

    shape-margin: 5%;
    

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
      margin: 20px;
      width: 180px;
      height: 180px;
      border-radius: 50%;
      background-color: rebeccapurple;
      shape-outside: circle(50%);
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#syntax)

----------------------------------------------------------------------------------------------------

css

    /* <length> values */
    shape-margin: 10px;
    shape-margin: 20mm;
    
    /* <percentage> value */
    shape-margin: 60%;
    
    /* Global values */
    shape-margin: inherit;
    shape-margin: initial;
    shape-margin: revert;
    shape-margin: revert-layer;
    shape-margin: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#length-percentage)

Sets the margin of the shape to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value or to a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 of the width of the element's containing block.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | floats |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the width of the containing block |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#formal_syntax)

------------------------------------------------------------------------------------------------------------------

shape-margin =   
  <length-percentage \[0,∞\]>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#examples)

--------------------------------------------------------------------------------------------------------

### [Adding a margin to a polygon](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#adding_a_margin_to_a_polygon)

#### HTML

html

    <section>
      <div class="shape"></div>
      We are not quite sure of any one thing in biology; our knowledge of geology is
      relatively very slight, and the economic laws of society are uncertain to
      every one except some individual who attempts to set them forth; but before
      the world was fashioned the square on the hypotenuse was equal to the sum of
      the squares on the other two sides of a right triangle, and it will be so
      after this world is dead; and the inhabitant of Mars, if one exists, probably
      knows its truth as we know it.
    </section>
    

#### CSS

css

    section {
      max-width: 400px;
    }
    
    .shape {
      float: left;
      width: 150px;
      height: 150px;
      background-color: maroon;
      clip-path: polygon(0 0, 150px 150px, 0 150px);
      shape-outside: polygon(0 0, 150px 150px, 0 150px);
      shape-margin: 20px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# shape-margin-property](https://drafts.csswg.org/css-shapes/#shape-margin-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin#see_also)

--------------------------------------------------------------------------------------------------------

*   [CSS Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
    
*   [Overview of CSS Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
    
*   [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [`shape-image-threshold`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/shape-margin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/shape-margin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-margin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-margin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-margin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-margin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#mdn-search)
    

`border-image-repeat` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-image-repeat`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines how the images for the sides and the middle part of the [border image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
 are scaled and tiled. The middle region can be displayed by using the keyword "fill" in the [`border-image-slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
 property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#try_it)

-----------------------------------------------------------------------------------------------------------

    border-image-repeat: stretch;
    

    border-image-repeat: repeat;
    

    border-image-repeat: round;
    

    border-image-repeat: space;
    

    border-image-repeat: round stretch;
    

    <section id="default-example">
      <div id="example-element">This is a box with a border around it.</div>
    </section>
    

    #example-element {
      width: 80%;
      height: 80%;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 50px;
      background: #fff3d4;
      color: black;
      border: 30px solid;
      border-image: url("/shared-assets/images/examples/border-diamonds.png") 30
        round;
      font-size: 1.2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    border-image-repeat: stretch;
    border-image-repeat: repeat;
    border-image-repeat: round;
    border-image-repeat: space;
    
    /* top and bottom | left and right */
    border-image-repeat: round stretch;
    
    /* Global values */
    border-image-repeat: inherit;
    border-image-repeat: initial;
    border-image-repeat: revert;
    border-image-repeat: revert-layer;
    border-image-repeat: unset;
    

The `border-image-repeat` property may be specified using one or two values chosen from the list of values below.

*   When **one** value is specified, it applies the same behavior on **all four sides**.
*   When **two** values are specified, the first applies to the **top, middle, and bottom**, the second to the **left and right**.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#values)

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#stretch)

The source image's edge regions are stretched to fill the gap between each border.

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#repeat)

The source image's edge regions are tiled (repeated) to fill the gap between each border. Tiles may be clipped to achieve the proper fit.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#round)

The source image's edge regions are tiled (repeated) to fill the gap between each border. Tiles may be stretched to achieve the proper fit.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#space)

The source image's edge regions are tiled (repeated) to fill the gap between each border. Extra space will be distributed in between tiles to achieve the proper fit.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `stretch` |
| Applies to | all elements, except internal table elements when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)<br> is `collapse`. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

border-image-repeat =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 stretch [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 repeat [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 round [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 space [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#examples)

---------------------------------------------------------------------------------------------------------------

### [Repeating border images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#repeating_border_images)

#### CSS

css

    #bordered {
      width: 12rem;
      margin-bottom: 1rem;
      padding: 1rem;
      border: 40px solid;
      border-image: url("border.png") 27;
      border-image-repeat: stretch; /* Can be changed in the live sample */
    }
    

    <div id="bordered">You can try out various border repetition rules on me!</div>
    
    <select id="repetition">
      <option value="stretch">stretch</option>
      <option value="repeat">repeat</option>
      <option value="round">round</option>
      <option value="space">space</option>
      <option value="stretch repeat">stretch repeat</option>
      <option value="space round">space round</option>
    </select>
    

    const repetition = document.getElementById("repetition");
    repetition.addEventListener("change", (evt) => {
      document.getElementById("bordered").style.borderImageRepeat =
        evt.target.value;
    });
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# border-image-repeat](https://drafts.csswg.org/css-backgrounds/#border-image-repeat) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
    
*   [Learn CSS: Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
    
*   [Border images in CSS: A key focus area for Interop 2023](https://developer.mozilla.org/en-US/blog/border-images-interop-2023/)
     on MDN blog (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-image-repeat/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-image-repeat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-repeat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-repeat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-image-repeat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-image-repeat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
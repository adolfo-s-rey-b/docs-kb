*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#mdn-search)
    

`link-parameters` CSS property
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/923)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#browser_compatibility)
 carefully before using this in production.

The **`link-parameters`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets values of external resources, such as SVGs, whose attributes have been set with the [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
 CSS function

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* single value */
    link-parameters: param(--color, red);
    
    /* multiple values */
    link-parameters:
      param(--color1, red),
      param(--color2, blue),
      param(--color3, green);
    

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#values)

-------------------------------------------------------------------------------------------------------

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#none)

No link parameters are specified.

[`param()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param)

A list of one or more link parameters.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#example)

---------------------------------------------------------------------------------------------------------

### [Updating the colors of an external SVG file](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#updating_the_colors_of_an_external_svg_file)

In this example the original SVG, on the left, is a square with `stroke` attribute set with `env(--color1, chartreuse)` and `fill` attribute set with `env(--color2, darkgreen)`. The `link-parameters` property is used to update both of these attributes on the updated square, on the right, with multiple [`param()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param)
 CSS functions.

html

    <div class="squares">
      <img
        class="original"
        src="square.svg"
        alt="A square with a chartreuse border and a dark green fill." />
      <img
        class="updated"
        src="square.svg"
        alt="A square with a red border and a tomato fill." />
    </div>
    

    .squares {
      height: 200px;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    img {
      height: 100%;
    }
    

css

    .updated {
      link-parameters:
        param(--color1, red),
        param(--color2, tomato);
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Linked Parameters Module Level 1  <br>\# propdef-link-parameters](https://drafts.csswg.org/css-link-params/#propdef-link-parameters) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`param()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param)
    
*   [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/link-parameters/index.md?plain=1 "Folder: en-us/web/css/reference/properties/link-parameters (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flink-parameters&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flink-parameters%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flink-parameters%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flink-parameters%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa9dc3374034d357cbfea717fd5d641605359e3c7%0A*+Document+last+modified%3A+2026-07-25T06%3A18%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
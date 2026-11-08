*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#mdn-search)
    

`line-height-step` CSS property
===============================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#browser_compatibility)
 carefully before using this in production.

The **`line-height-step`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the step unit for line box heights. When the property is set, line box heights are rounded up to the closest multiple of the unit.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Point values */
    line-height-step: 18pt;
    
    /* Global values */
    line-height-step: inherit;
    line-height-step: initial;
    line-height-step: revert;
    line-height-step: revert-layer;
    line-height-step: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#values)

This property is specified as the following value:

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#length)

The specified [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 is used in the calculation of the line box height step.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length) |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

line-height-step =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#examples)

------------------------------------------------------------------------------------------------------------

### [Setting step unit for line box height](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#setting_step_unit_for_line_box_height)

In the following example, the height of line box in each paragraph is rounded up to the step unit. The line box in `<h1>` does not fit into one step unit and thus occupies two, but it is still centered within the two step unit.

css

    :root {
      font-size: 12pt;
      --my-grid: 18pt;
      line-height-step: var(--my-grid);
    }
    h1 {
      font-size: 20pt;
      margin-top: calc(2 * var(--my-grid));
    }
    

The result of these rules is shown below in the following screenshot:

![How the line-height-step property affects the appearance of text.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step/line-grid-center.png)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#specifications)

------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step#see_also)

------------------------------------------------------------------------------------------------------------

*   [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    
*   [CSS Rhythmic Sizing](https://drafts.csswg.org/css-rhythm/ "External link (opens in new tab)")
     specification

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/line-height-step/index.md?plain=1 "Folder: en-us/web/css/reference/properties/line-height-step (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-height-step&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-height-step%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-height-step%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-height-step%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
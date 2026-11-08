*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#mdn-search)
    

`forced-color-adjust` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`forced-color-adjust`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows authors to opt certain elements out of forced colors mode. This then restores the control of those values to CSS.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#syntax)

-----------------------------------------------------------------------------------------------------------

css

    forced-color-adjust: auto;
    forced-color-adjust: none;
    forced-color-adjust: preserve-parent-color;
    
    /* Global values */
    forced-color-adjust: inherit;
    forced-color-adjust: initial;
    forced-color-adjust: revert;
    forced-color-adjust: revert-layer;
    forced-color-adjust: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#auto)

The element's colors are adjusted by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 in forced colors mode. This is the default value.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#none)

The element's colors are not automatically adjusted by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 in forced colors mode.

[`preserve-parent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#preserve-parent-color)

In forced colors mode, if the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property inherits from its parent (i.e., there is no [cascaded value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 or the cascaded value is `currentColor`, [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
, or another keyword that inherits from the parent), then it computes to the [used color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of its parent's `color` property. In all other cases, it behaves the same as `none`.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#usage_notes)

---------------------------------------------------------------------------------------------------------------------

This property should only be used to makes changes that will support a user's color and contrast requirements. For example, if you become aware that the color optimizations made by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 result in a poor experience when in a high contrast or dark mode. Using this property would enable tweaking of the result in that mode to provide a better experience. **It should not be used to prevent user choices being respected**.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements and text |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

forced-color-adjust =   
  auto                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-parent-color    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#examples)

---------------------------------------------------------------------------------------------------------------

### [Preserving colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#preserving_colors)

In the example below the first box will use the color scheme that the user has set. For example in Windows High Contrast mode black scheme it will have a black background and white text. The second box will preserve the site colors set on the `.box` class.

By using the [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
 media feature, you could add any other optimizations for forced color mode alongside the `forced-color-adjust` property.

#### CSS

css

    .box {
      border: 5px solid grey;
      background-color: #cccccc;
      width: 300px;
      margin: 20px;
      padding: 10px;
    }
    
    @media (forced-colors: active) {
      .forced {
        forced-color-adjust: none;
      }
    }
    

#### HTML

html

    <div class="box">
      <p>This is a box which should use your color preferences.</p>
    </div>
    
    <div class="box forced">
      <p>This is a box which should stay the colors set by the site.</p>
    </div>
    

#### Result

The following screenshot shows the image above in Windows High Contrast Mode:

![The example above in high contrast mode shows the first box with a black background the second with the gray background of the CSS.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust/windows-high-contrast.jpg)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Adjustment Module Level 1  <br>\# forced-color-adjust-prop](https://drafts.csswg.org/css-color-adjust/#forced-color-adjust-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Styling for Windows high contrast with standards for forced colors.](https://blogs.windows.com/msedgedev/2020/09/17/styling-for-windows-high-contrast-with-new-standards-for-forced-colors/ "External link (opens in new tab)")
    
*   [`print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/forced-color-adjust/index.md?plain=1 "Folder: en-us/web/css/reference/properties/forced-color-adjust (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fforced-color-adjust&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fforced-color-adjust%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fforced-color-adjust%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fforced-color-adjust%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
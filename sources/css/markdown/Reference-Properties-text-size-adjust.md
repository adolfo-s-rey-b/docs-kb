*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#mdn-search)
    

`text-size-adjust` CSS property
===============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/61)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#browser_compatibility)
 carefully before using this in production.

The **`text-size-adjust`** [CSS](https://developer.mozilla.org/en-US/docs/Web/API/CSS)
 property controls the text inflation algorithm used on some smartphones and tablets. Other browsers will ignore this property.

Because many websites have not been developed with small devices in mind, mobile browsers differ from desktop browsers in the way they render web pages. Instead of laying out pages at the width of the device screen, they lay them out using a [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 that is much wider, usually 800 or 1000 pixels. To map the extra-wide layout back to the original device size, they either show only part of the whole render or scale the viewport down to fit.

Since text that has been scaled down to fit a mobile screen may be very small, many mobile browsers apply a text inflation algorithm to enlarge the text to make it more readable. When an element containing text uses 100% of the screen's width, the algorithm increases its text size, but without modifying the layout. The `text-size-adjust` property allows web authors to disable or modify this behavior, as web pages designed with small screens in mind do not need it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#syntax)

--------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#values)

This property is specified as one of the following values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#none)

Disables the browser's inflation algorithm.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#auto)

Enables the browser's inflation algorithm. This value is used to cancel a `none` value previously set with CSS.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#percentage)

Enables the browser's inflation algorithm, specifying a percentage value with which to increase the font size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` for smartphone browsers supporting inflation, `none` in other cases (and then not modifiable). |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | yes, refer to the corresponding size of the text font |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

text-size-adjust =   
  auto                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#examples)

------------------------------------------------------------------------------------------------------------

### [Basic disabling usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#basic_disabling_usage)

As hinted at above, on a properly designed responsive site the `text-size-adjust` behavior is not needed, so developers can elect to turn it off by specifying a value of none:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Mobile Text Size Adjustment Module Level 1  <br>\# adjustment-control](https://drafts.csswg.org/css-size-adjust/#adjustment-control) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust#see_also)

------------------------------------------------------------------------------------------------------------

*   [Apple's documentation](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/AdjustingtheTextSize/AdjustingtheTextSize.html#//apple_ref/doc/uid/TP40006510-SW16 "External link (opens in new tab)")
     (2016)
*   [Google Chrome behavior description](https://docs.google.com/document/d/1PPcEwAhXJJ1TQShor29KWB17KJJq7UJOM34oHwYP3Zg/edit "External link (opens in new tab)")
     (2014)
*   [Gecko's behavior description](https://dbaron.org/log/20111126-font-inflation "External link (opens in new tab)")
    , by L. David Baron (2011)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-size-adjust/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-size-adjust (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-size-adjust&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-size-adjust%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-size-adjust%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-size-adjust%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
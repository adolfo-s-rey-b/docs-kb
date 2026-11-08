*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#mdn-search)
    

`box-ordinal-group` CSS property
================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property of the original CSS flexible box layout Module draft. It has been replaced in the specification. See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The **`box-ordinal-group`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property assigns the flexbox's child elements to an ordinal group.

Ordinal groups may be used in conjunction with the [`box-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction)
 property to control the order in which the direct children of a box appear. When the computed `box-direction` is normal, a box will display its elements starting from the lowest numbered ordinal group and ensure that those elements appear to the left (for horizontal boxes) or at the top (for vertical boxes) of the container. Elements with the same ordinal group are flowed in the order they appear in the source document tree. In the reverse direction, the ordinal groups are examined in the same order, except the elements appear reversed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#syntax)

---------------------------------------------------------------------------------------------------------

The `box-ordinal-group` property is specified as any positive [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | children of box elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

box-ordinal-group =   
  <integer>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic usage example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#basic_usage_example)

In an older version of the spec, `box-ordinal-group` was included to allow you to change the display order of flex children inside a flex container:

The modern flexbox equivalent is [`order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#specifications)

-------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    
*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    
*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    
*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-ordinal-group/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-ordinal-group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-ordinal-group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-ordinal-group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-ordinal-group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-ordinal-group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
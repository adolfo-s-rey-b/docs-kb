*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#mdn-search)
    

`box-flex` CSS property
=======================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property for controlling parts of the XUL box model. It does not match either the old CSS flexible box layout Module drafts for `box-flex` (which were based on this property) or the behavior of `-webkit-box-flex` (which is based on those drafts). See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The **`-moz-box-flex`** and **`-webkit-box-flex`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 properties specify how a `-moz-box` or `-webkit-box` grows to fill the box that contains it, in the direction of the containing box's layout.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#syntax)

------------------------------------------------------------------------------------------------

The `box-flex` property is specified as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. If the value is 0, the box does not grow. If it is greater than 0, the box grows to fill a proportion of the available space.

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#notes)

----------------------------------------------------------------------------------------------

The containing box allocates the available extra space in proportion to the flex value of each of the content elements.

Content elements that have zero flex do not grow.

If only one content element has nonzero flex, then it grows to fill the available space.

Content elements that have the same flex grow by the same absolute amounts.

If the flex value is set using the element's `flex` attribute, then the style is ignored.

To make XUL elements in a containing box the same size, set the containing box's `equalsize` attribute to the value `always`. This attribute does not have a corresponding CSS property.

A trick to make all content elements in a containing box the same size, is to give them all a fixed size (e.g., `height: 0`), and the same `box-flex` value greater than zero (e.g., `-moz-box-flex: 1`).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | elements that are direct children of an element with a CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> value of `-moz-box` or `-moz-inline-box` or `-webkit-box` or `-webkit-inline-box` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#formal_syntax)

--------------------------------------------------------------------------------------------------------------

box-flex =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#examples)

----------------------------------------------------------------------------------------------------

### [Setting box-flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#setting_box-flex)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#specifications)

----------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex#see_also)

----------------------------------------------------------------------------------------------------

*   [`box-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient)
    
*   [`box-pack`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
    
*   [`box-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction)
    
*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-flex/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-flex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-flex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-flex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-flex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-flex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
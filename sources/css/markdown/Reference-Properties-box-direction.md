*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#mdn-search)
    

`box-direction` CSS property
============================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property of the original CSS flexible box layout Module draft, and has been replaced by a newer standard. The `-moz-box-direction` will only be used for XUL while the previous standard `box-direction` has been replaced by `flex-direction`. See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The **`box-direction`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether a box lays out its contents normally (from the top or left edge), or in reverse (from the bottom or right edge).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#syntax)

-----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#normal)

The box lays out its contents from the start (the left or top edge).

[`reverse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#reverse)

The box lays out its contents from the end (the right or bottom edge).

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#notes)

---------------------------------------------------------------------------------------------------

The edge of the box designated the _start_ for layout purposes depends on the box's orientation:

*   For horizontal elements, the _start_ is the top edge.
*   For vertical elements, the _start_ is the left edge.

The edge opposite to the start is designated the _end_.

If the direction is set using the element's `dir` attribute, then the style is ignored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | elements with a CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> value of `box` or `inline-box` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

box-direction =   
  normal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  reverse    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#examples)

---------------------------------------------------------------------------------------------------------

### [Setting box direction](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#setting_box_direction)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#specifications)

---------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction#see_also)

---------------------------------------------------------------------------------------------------------

*   [`box-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient)
    
*   [`box-pack`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
    
*   [`box-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align)
    
*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-direction/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-direction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-direction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-direction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-direction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-direction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
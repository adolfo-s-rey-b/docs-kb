*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#mdn-search)
    

`box-align` CSS property
========================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property of the original CSS flexible box layout Module draft, and has been replaced by a newer standard.

The **`box-align`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies how an element aligns its contents across its layout in a perpendicular direction. The effect of the property is only visible if there is extra space in the box.

See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The direction of layout depends on the element's orientation: horizontal or vertical.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#values)

This property is specified as one of the following keyword values:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#start)

The box aligns contents at the start, leaving any extra space at the end.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#center)

The box aligns contents in the center, dividing any extra space equally between the start and the end.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#end)

The box aligns contents at the end, leaving any extra space at the start.

[`baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#baseline)

The box aligns the baselines of the contents (lining up the text). This only applies if the box's orientation is horizontal.

[`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#stretch)

The box stretches the contents so that there is no extra space in the box.

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#notes)

-----------------------------------------------------------------------------------------------

The edge of the box designated the _start_ for alignment purposes depends on the box's orientation:

*   For horizontal elements, the _start_ is the top edge.
*   For vertical elements, the _start_ is the left edge.

The edge opposite to the start is designated the _end_.

If the alignment is set using the element's `align` attribute, then the style is ignored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `stretch` |
| Applies to | elements with a CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> value of `box` or `inline-box` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#formal_syntax)

---------------------------------------------------------------------------------------------------------------

box-align =   
  start     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  baseline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#examples)

-----------------------------------------------------------------------------------------------------

### [Setting box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#setting_box_alignment)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#specifications)

-----------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align#see_also)

-----------------------------------------------------------------------------------------------------

*   [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    , [`box-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient)
    , [`box-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction)
    , [`box-pack`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-align/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-align (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-align&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-align%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-align%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-align%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#mdn-search)
    

`box-lines` CSS property
========================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property of the original CSS flexible box layout Module draft. It has been replaced in the specification. See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The **`box-lines`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property determines whether the box may have a single or multiple lines (rows for horizontally oriented boxes, columns for vertically oriented boxes).

By default a horizontal box will lay out its children in a single row, and a vertical box will lay out its children in a single column. This behavior can be changed using the `box-lines` property. The default value is `single`, which means that all elements will be placed in a single row or column, and any elements that don't fit will be considered overflow.

If a value of `multiple` is specified, however, then the box is allowed to expand to multiple lines (that is, multiple rows or columns) in order to accommodate all of its children. The box must attempt to fit its children on as few lines as possible by shrinking all elements down to their minimum widths or heights if necessary.

If the children in a horizontal box still do not fit on a line after being reduced to their minimum widths, then children are moved one by one onto a new line, until the elements remaining on the previous line fit. This process can repeat to an arbitrary number of lines. If a line contains only a single element that doesn't fit, then the element should stay on that line and overflow out of the box. The later lines are placed below the earlier lines in normal direction boxes and above in reverse direction boxes. The height of a line is the height of the largest child in that line. No additional space appears between the lines apart from the margins on the largest elements in each line. For calculating the height of a line, margins with a computed value of auto should be treated as having a value of 0.

A similar process occurs for children in a vertical box. Later lines in normal direction boxes are placed to the right of earlier lines and to the left in reverse direction boxes.

Once the number of lines has been determined, elements with a computed value for [`box-flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex)
 other than `0` stretch as necessary in an attempt to fill the remaining space on the lines. Each line computes flexes independently, so only elements on that line are considered when evaluating [`box-flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex)
 and [`box-flex-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex-group)
. The packing of elements in a line, as specified by the [`box-pack`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
 property, is also computed independently for each line.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#values)

This property is specified as one of the following keyword values:

[`single`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#single)

Box elements lay out in a single row or column.

[`multiple`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#multiple)

Box elements layout in multiple rows or columns.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `single` |
| Applies to | box elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#formal_syntax)

---------------------------------------------------------------------------------------------------------------

box-lines =   
  single    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  multiple    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#examples)

-----------------------------------------------------------------------------------------------------

### [Basic usage example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#basic_usage_example)

In the original version of the spec, `box-lines` allowed you to specify that you wanted your flex container's children to wrap onto multiple lines. This was only supported in WebKit-based browsers, with a prefix.

The modern flexbox equivalent is [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#specifications)

-----------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines#see_also)

-----------------------------------------------------------------------------------------------------

*   [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    
*   [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    
*   [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    
*   [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-lines/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-lines (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-lines&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-lines%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-lines%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-lines%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
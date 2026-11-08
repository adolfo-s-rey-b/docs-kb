*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#mdn-search)
    

`flex-direction` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`flex-direction`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how flex items are placed in the flex container defining the main axis and the direction (normal or reversed).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#try_it)

------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#values)

This property is specified as one of the following keyword values:

[`row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#row)

Specifies the flex container's main-axis to be the same as the text direction. This is the default value.

[`row-reverse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#row-reverse)

Behaves the same as `row` but specifies the content direction to be inverted, with the first item placed at the inline-end edge.

[`column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#column)

Specifies the flex container's main-axis to be the same as the block-axis.

[`column-reverse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#column-reverse)

Behaves the same as `column` but specifies the content direction to be inverted, with the first item placed at the block-end edge.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#description)

----------------------------------------------------------------------------------------------------------------

The `flex-direction` property enables you to define how flex items are placed in a flex container by setting the container's main axis and the direction of the flex items. This property is relevant only on container elements that have their [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property set to `flex` or `inline-flex`. The `flex-direction` property, along with the [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
 property, should be set using the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 shorthand.

When set on a flex container, the `flex-direction` property defines whether the flex items are laid out in the same direction or perpendicular to the text direction, and whether the items are laid out normally or reversed.

The default value is `row`. By default, or when `row` is explicitly set, the flex container's main-axis is defined to be the same as the text direction. The first flex item in the DOM order is placed at the inline-start and block start edges. Additional items are placed at the previous item's inline-end edge. Additional rows, if the container is set to wrap with `flex-wrap: wrap`, are added on the block-end edge. The **main-start** and **main-end** points are the same as the content direction, with main-start being the inline-start edge and the main-end being the inline-end edge, and cross-start and cross-end being the block-start and block-end edges, respectively.

The `row-reverse` value is used to change the inline-direction, behaving like `row`, but reversed. The first item is placed at the inline-end and block-start edges, with subsequent flex items being placed at the previous item's inline-start edge, and additional rows added on the block-end edge. The main-start and main-end points are the same as the inline-end and inline-start ends of the writing-mode, respectively, and cross-start and cross-end are the block-start and block-end edges, respectively.

When `flex-direction` is set to `column`, the main axis is the block axis. As with `row`, the first item is placed at the inline-start and block-start edges, but additional items are placed at the previous item's block-end edge rather than the inline edge. If set to be able to wrap, additional columns are added on the inline-end edge. The **main-start** and **main-end** points are based on the block direction of the writing mode, with main-start being the block-start edge and the main-end being the block-end edge, and cross-start and cross-end being the inline-start and inline-end edges, respectively.

With `column-reverse`, the main axis is the block axis, but starting at the block-end edge. The first item is placed at the inline-start and block-end edges, with subsequent items placed at the previous item's block-start edge. If set to be able to wrap, additional columns are added on the inline-end edge. The **main-start** and **main-end** points are based on the block direction of the writing mode, with main-start being the block-end edge and the main-end being the block-start edge, and cross-start and cross-end being the inline-start and inline-end edges, respectively.

The values `row` and `row-reverse` are affected by the directionality of the flex container. If its [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 attribute is `ltr`, `row` represents the horizontal axis oriented from the left to the right, and `row-reverse` from the right to the left; if the `dir` attribute is `rtl`, `row` represents the axis oriented from the right to the left, and `row-reverse` from the left to the right.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#accessibility)

--------------------------------------------------------------------------------------------------------------------

Using the `flex-direction` property with values of `row-reverse` or `column-reverse` will create a disconnect between the visual presentation of content and DOM order. This will adversely affect the experience of users with low vision navigating the page with the aid of assistive technology such as a screen reader. If the visual (CSS) order is important, then screen reader users will not have access to the correct reading order.

*   [Source Order Matters](https://adrianroselli.com/2015/09/source-order-matters.html "External link (opens in new tab)")
     by Adrian Roselli (2015)
*   [Flexbox & the keyboard navigation disconnect](https://tink.uk/flexbox-the-keyboard-navigation-disconnect/ "External link (opens in new tab)")
     by Léonie Watson (2016)
*   [Understanding SC 1.3.2: Meaningful Sequence](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence "External link (opens in new tab)")
     via WCAG 2.2 (2023)

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `row` |
| Applies to | flex containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

flex-direction =   
  row             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  row-reverse     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  column-reverse    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#examples)

----------------------------------------------------------------------------------------------------------

### [Reversing flex container columns and rows](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#reversing_flex_container_columns_and_rows)

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Flexible Box Layout Module Level 1  <br>\# flex-direction-property](https://drafts.csswg.org/css-flexbox/#flex-direction-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction#see_also)

----------------------------------------------------------------------------------------------------------

*   [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
     shorthand
*   [`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Ordering flex items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Ordering_items)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/flex-direction/index.md?plain=1 "Folder: en-us/web/css/reference/properties/flex-direction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-direction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-direction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fflex-direction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fflex-direction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc965bd5938085b2dab7d19734adbe3db0914ba5d%0A*+Document+last+modified%3A+2026-08-07T18%3A41%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#mdn-search)
    

`contain-intrinsic-height` CSS property
=======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contain-intrinsic-height`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the height of an element that a browser can use for layout when the element is subject to [size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#size_containment)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#syntax)

----------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#values)

The following values may be specified for an element.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#none)

The element has no intrinsic height.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#length)

The element has the specified height ([`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
).

[`auto <length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#auto_length)

A remembered value of the "normally rendered" element height if one exists and the element is skipping its contents (for example, when it is offscreen); otherwise the specified `<length>`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#description)

--------------------------------------------------------------------------------------------------------------------------

The property is commonly applied alongside elements that can trigger size containment, such as [`contain: size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 and [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
, and may also be set using the [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
 [shorthand property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
.

Size containment allows a user agent to lay out an element as though it had a fixed size, preventing unnecessary reflows by avoiding the re-rendering of child elements to determine the actual size (thereby improving user experience). By default, size containment treats elements as though they had no contents, and may collapse the layout in the same way as if the contents had no height (or width). The `contain-intrinsic-height` property allows authors to specify an appropriate value to be used as the height for layout.

The `auto <length>` value allows the height of the element to be stored if the element is ever "normally rendered" (with its child elements), and then used instead of the specified height when the element is skipping its contents. This allows offscreen elements with [`content-visibility: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 to benefit from size containment without developers having to be as precise in their estimates of element size. The remembered value is not used if the child elements are being rendered (if size containment is enabled, the `<length>` will be used).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | elements for which size containment can apply |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, with <length>s values computed |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

contain-intrinsic-height =   
  auto[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#examples)

--------------------------------------------------------------------------------------------------------------------

In addition to the example below, the [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
 page contains a live example that demonstrates the effect of modifying the intrinsic width and height.

### [Setting the intrinsic height](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#setting_the_intrinsic_height)

The HTML below defines an element "contained\_element" that will be subject to size constraint, and which contains a child element.

The CSS below sets the [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 of `contained_element` to `auto`, so if the element is hidden it will be size constrained. The width and height that are used when it is size constrained are set at the same time using `contain-intrinsic-width` and `contain-intrinsic-height`, respectively.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# propdef-contain-intrinsic-height](https://drafts.csswg.org/css-sizing-4/#propdef-contain-intrinsic-height) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [content-visibility: the new CSS property that boosts your rendering performance](https://web.dev/articles/content-visibility "External link (opens in new tab)")
     (web.dev)
*   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
    
*   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
    
*   [`contain-intrinsic-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/contain-intrinsic-height/index.md?plain=1 "Folder: en-us/web/css/reference/properties/contain-intrinsic-height (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-height&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-height%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-height%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-height%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
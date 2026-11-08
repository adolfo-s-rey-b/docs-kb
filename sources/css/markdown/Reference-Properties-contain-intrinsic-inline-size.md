*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#mdn-search)
    

`contain-intrinsic-inline-size` CSS property
============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`contain-intrinsic-inline-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [logical property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 defines the inline-size of an element that a browser can use for layout when the element is subject to [size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#size_containment)
.

Inline-size is the size of the element in the dimension parallel to the flow of text within a line. In a horizontal [writing mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 like standard English, inline size is the horizontal dimension (width); for a vertical writing mode, inline size is the vertical dimension.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#syntax)

---------------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#values)

The following values can be specified for the intrinsic inline size of an element:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#none)

The element has no intrinsic inline-size.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#length)

The element has the specified inline-size ([`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
).

[`auto <length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#auto_length)

When the element is in size containment and skipping its contents (for example, when it is offscreen and `content-visibility: auto` is set) the inline size is remembered from the actual size of the element when it was last able to render its child elements. If the element has never rendered its child elements and hence has no remembered value for the normally rendered element size, or if it is not skipping its contents, the inline size is the specified `<length>`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#description)

-------------------------------------------------------------------------------------------------------------------------------

The property is commonly applied alongside elements that can trigger size containment, such as [`contain: size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
 and [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
.

Size containment allows a user agent to lay out an element as though it had a fixed size, preventing unnecessary reflows by avoiding the re-rendering of child elements to determine the actual size (thereby improving user experience). By default, size containment treats elements as though they had no contents, and may collapse the layout in the same way as if the contents had no width or height. The `contain-intrinsic-inline-size` property allows authors to specify an appropriate value to be used as the inline-size for layout.

The `auto <length>` value allows the inline-size of the element to be stored if the element is ever "normally rendered" (with its child elements), and then used instead of the specified value when the element is skipping its contents. This allows offscreen elements with [`content-visibility: auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 to benefit from size containment without developers having to be as precise in their estimates of element size. The remembered value is not used if the child elements are being rendered (if size containment is enabled, the `<length>` will be used).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | elements for which size containment can apply |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, with <length>s values computed |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------------

contain-intrinsic-inline-size =   
  auto[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Setting the intrinsic inline size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#setting_the_intrinsic_inline_size)

The HTML below defines an element "contained\_element" that will be subject to size constraint, and which contains a child element.

The CSS below sets the [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 of `contained_element` to `auto`, so if the element is hidden it will be size constrained. The intrinsic block size and inline size that are used when it is size constrained are set at the same time using `contain-intrinsic-block-size` and `contain-intrinsic-inline-size`, respectively.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#specifications)

-------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# propdef-contain-intrinsic-inline-size](https://drafts.csswg.org/css-sizing-4/#propdef-contain-intrinsic-inline-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [content-visibility: the new CSS property that boosts your rendering performance](https://web.dev/articles/content-visibility "External link (opens in new tab)")
     (web.dev)
*   [`contain-intrinsic-block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
    
*   [`contain-intrinsic-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`contain-intrinsic-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
    
*   [`contain-intrinsic-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/contain-intrinsic-inline-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/contain-intrinsic-inline-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-inline-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-inline-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontain-intrinsic-inline-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontain-intrinsic-inline-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#mdn-search)
    

`order` CSS property
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`order`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the order to lay out an item in a flex or grid container. Items in a container are sorted by ascending `order` value and then by their source code order. Items not given an explicit `order` value are assigned the default value of `0`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#try_it)

---------------------------------------------------------------------------------------------

In the above demo, select the options on the left-hand side to change the value of the pink box's `order` property. The light blue boxes have been given fixed `order` values.

Bear in mind the effect of source order. For example, when `order: 2;` is selected, the pink box is placed before the two blue boxes with `order: 2;`. This is because the pink box appears before the blue boxes in the source code.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#syntax)

---------------------------------------------------------------------------------------------

Since `order` is only meant to affect the _visual order_ of elements and not their logical or tab order, it must not be used on non-visual media such as [speech](https://drafts.csswg.org/css-speech/ "External link (opens in new tab)")
.

Defined in the [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
 module, this property impacts only grid and flex items. When `order` is set on an element whose parent's [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property is not creating a flex or grid container, it has no effect.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#values)

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Represents the ordinal group to be used by the item.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#accessibility)

-----------------------------------------------------------------------------------------------------------

Using the `order` property will create a disconnect between the visual presentation of content and DOM order. This will adversely affect low vision users navigating with the aid of assistive technology such as a screen reader. If the visual order differs from the DOM order, your users will have different experiences depending on how they access your content.

*   [Flexbox & the keyboard navigation disconnect](https://tink.uk/flexbox-the-keyboard-navigation-disconnect/ "External link (opens in new tab)")
     via Tink (2016)
*   [Source Order Matters](https://adrianroselli.com/2015/09/source-order-matters.html "External link (opens in new tab)")
     via Adrian Roselli (2015)
*   [Understanding WCAG, Guideline 1.3 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.3_%E2%80%94_create_content_that_can_be_presented_in_different_ways)
    
*   [Understanding Success Criterion 1.3.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/content-structure-separation-sequence.html "External link (opens in new tab)")
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | Flex items, grid items, and absolutely-positioned flex and grid container children |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | an [integer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation "Values of the <integer> CSS data type are interpolated via integer discrete steps. The calculation is done as if they were real, floating-point numbers and the discrete value is obtained using the floor function.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#formal_syntax)

-----------------------------------------------------------------------------------------------------------

order =   
  <integer>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#examples)

-------------------------------------------------------------------------------------------------

### [Ordering items in a flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#ordering_items_in_a_flex_container)

In this example, we create a classic two-sidebar layout.

#### HTML

We include a header, a footer, and a main content area. The main content includes an article and two side bars. Note their order! We'll use the CSS `order` property to change their visual order.

#### CSS

We style the main area using [flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 module features; by setting [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, the [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 element becomes a flex container. By default, this creates flex items of equal vertical size. The sidebars are both given an absolute [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, while the [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 will consume all the [positive free space](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Controlling_flex_item_ratios#positive_and_negative_free_space)
 with a [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 factor set via the [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 shorthand.

We then set different `order` property values on each of the flex container's three children; this means the CSS is defining that component's visual order rather than it appearing in the order declared in the HTML.

#### Result

The `<article>` appears first in the source order but visually rendered in the center.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# order-property](https://drafts.csswg.org/css-display/#order-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order#see_also)

-------------------------------------------------------------------------------------------------

*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Ordering flex items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Ordering_items)
    
*   [CSS grid layout and accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Accessibility)
    
*   [CSS display](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display)
     module
*   [Reading order](https://developer.mozilla.org/en-US/docs/Glossary/Reading_order)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/order/index.md?plain=1 "Folder: en-us/web/css/reference/properties/order (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Forder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Forder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Forder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Forder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
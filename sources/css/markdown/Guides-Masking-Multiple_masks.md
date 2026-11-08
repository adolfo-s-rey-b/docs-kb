*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#mdn-search)
    

Declaring multiple masks
========================

CSS masking is a technique that enables you to use images as masks to define which sections of an element are fully visible or semi-opaque. The CSS mask selectively reveals or hides parts of the element based on the alpha channel and in some cases the brightness of the colors of the applied mask images.

CSS masks are the opposite of masks worn at masquerade (masked) balls. At a masked ball, a wearer's face is hidden wherever the mask is opaque and visible wherever you can see through the mask. In CSS, the areas where the composited mask layers are fully opaque reveal the element, while transparent areas hide it.

CSS masks are made up of one or more mask layers. In this guide, we discuss the concept of mask layers and how to declare multiple mask layers using the [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
 shorthand property.

[Understanding mask layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#understanding_mask_layers)

--------------------------------------------------------------------------------------------------------------------------------------

You can apply CSS masking to all HTML elements and most SVG elements. A mask can consist of one or more composited mask layers. You define multiple layers using comma-separated values in the [`mask`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
 shorthand property or the [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property–even a value set to `none` counts as a layer.

Each mask layer can contain a [mask image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
, which is positioned relative to the mask's origin box. The image can be sized, repeated, and clipped. If you include more than one mask image, you can define the way the mask layers are composited or combined. (These features are briefly introduced in this guide. For more details and examples, see the [masking properties guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
.)

### [Syntax for multiple mask layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#syntax_for_multiple_mask_layers)

The `mask` shorthand property accepts a comma-separated list of mask layers. The syntax for each layer can include the following values:

`<image> <position> / <size> <repeat> <origin> <clip> <composite> <mode>`

All the components in a mask layer are optional. However, if you omit the `mask-image` value, it defaults to a transparent black image, which hides the element in that layer completely.

The `mask` shorthand declaration sets values for all the `mask-*` properties. Any component not declared within a layer will default to its initial value. The `mask` property also resets all the `mask-border-*` properties to their initial values. A `mask` declaration that only includes a `mask-image` value implicitly sets the following:

### [Defining mask layers with `mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#defining_mask_layers_with_mask-image)

As long as a comma-separated [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
 property declaration includes at least one value other than `none`, a mask layer is created for every value in the declaration, even for the `none` values. This behavior applies whether you're using the `mask-image` property or the `mask` shorthand. These mask images can be gradients, images, or SVG sources. You can define them using a [CSS gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
, a raster image (such as PNGs), or an SVG [`<mask>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/mask)
 element.

The [introductory guide to masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
 introduces the different types of mask images and their modes.

The `mask-image` property is analogous to the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property. Just as with the `background-image` property, to include multiple mask images, the image values are separated by commas.

Each mask image in a multiple-image declaration creates a mask layer. All the examples in this section create one mask layer, except the `multiple-gradient-mask` declaration, which creates two.

### [Mask layers and the `none` keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#mask_layers_and_the_none_keyword)

If `none` is the only value of the `mask-image` property, no mask layers are created and no masking occurs.

Similarly, when using the `mask` shorthand, if no `mask-image` value is present other than `none`, no masking occurs. If any of the following are declared, no mask layers are created and nothing is hidden:

Otherwise, as long as there is a `mask-image` declared that isn't set to `none`, a mask layer is created for every value in the comma-separated list of values, even when the `mask-image` value is omitted from a value in the comma-separated list or is explicitly set to `none`. In other words, a layer is created for each valid comma-separated value, unless the entire property resolves to `none`.

The keyword `none` within a list of mask sources creates a mask layer, albeit a transparent black image layer. Any elements with the class `masked-element` will have five mask layers:

We can also create the layers using the `mask` shorthand:

If a value in the comma-separated list of values is an empty image, fails to download, references a `<mask>` element that doesn't exist, or otherwise cannot be displayed (or is set to `none`), it still counts as a mask image layer, rendering a transparent black mask image that has no visual effect. If all of the values do this, the element will be fully hidden.

No masking occurs if the entire property resolves to `none`, which makes the element fully visible. On the other hand, if the value includes multiple layers and at least one is not `none`, the `none` layers don't reveal any part of the element (or don't make any part of the element visible). In this example, the value doesn't resolve to `none`; but because all non-`none` images are invalid, masking occurs, and the element will be fully hidden.

A computed value other than `none` creates a [CSS stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
.

### [How mask layers affect `mask-*` properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#how_mask_layers_affect_mask-_properties)

The number of mask layers matters when you're also using individual `mask-*` properties after or with more specificity than a `mask` declaration.

The `mask-*` properties include:

*   [`mask-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
    : Sets the mode of each mask layer to either `alpha` or `luminance`, or allows it to default to the source's mode by setting the value to `match-source`. The default is `match-source`.
    
*   [`mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    : Analogous to the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
     property with syntax that follows the [`background-position`'s `<position>` syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position#position)
    , it sets the initial position of the mask image relative to the mask layer's origin box, defined by the `mask-origin` property. You can specify one, two, or four [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
     values. The default `0% 0%` positions the top-left corner of the mask at the top-left corner of the mask origin box.
    
*   [`mask-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    : Analogous to the [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
     property, it specifies the _mask positioning area_, which is the mask origin box area within which a mask image is positioned. For example, if the `mask-position` is `top left`, this property defines whether that is relative to the border's outer edge, the padding's outer edge, or the content's outer edge.
    
*   [`mask-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
    : Analogous to the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
     property, it determines the area of the element affected by a mask. It defines whether the mask painting area is the border, padding, or content box, restricting the painted content of the element to this area. If the mask layer's [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
     source is an SVG `<mask>` element, the `mask-clip` property has no effect.
    
*   [`mask-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    : Analogous to the [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
     property, this is used to size the mask layer. Values can be a single keyword (`cover`, `contain`, or `auto`), a single length or percentage, or two space-separated values–each of which may be a length, percentage, or `auto`. The default is `auto`.
    
*   [`mask-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    : Analogous to the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
     property, this defines how the mask layer image is tiled after it has been sized and positioned.
    
*   [`mask-composite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
    : Defines how a mask is combined with the mask layers below it. Each mask layer is either added to, subtracted from, included with, or excluded from the previously composited mask layers below it. Similar to `mask-mode`, there is no analogous `background-*` property.
    

Each `mask-*` value in a comma-separated list of `mask` component properties applies to a separate mask layer. As stated earlier, an element can have multiple mask layers applied — the number of layers is determined by the number of comma-separated values in the `mask-image` or `mask` properties. Each `mask-*` value is matched with a mask layer, in order. If the number of values in the `mask-*` property is greater than the number of mask layers, any excess values are ignored. If the mask component property has fewer values than the number of mask layers, the `mask-*` values are repeated.

To learn more about these individual properties, see [CSS mask properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
.

[Order of shorthand component properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#order_of_shorthand_component_properties)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the most part, the order of the properties is flexible, but there are a few quirks and exceptions.

### [Ordering rules for `mask-origin` and `mask-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#ordering_rules_for_mask-origin_and_mask-clip)

The `mask-origin` value, listed in the syntax as `<origin>`, comes before the `mask-clip` values, listed in the syntax as `<clip>`.

`<image> <position> / <size> <repeat> <origin> <clip> <composite> <mode>`

Both accept [`<geometry-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#geometry-box)
 keywords. In addition, `mask-clip` also accepts `no-clip`. Because of this, the order of these two matters when you want to set `mask-clip` to any value other than `no-clip`.

*   If one `<geometry-box>` value is present along with the `no-clip` keyword, then the `<geometry-box>` sets the `mask-origin` value, and `mask-clip` is set to `no-clip`. In this case, the order doesn't matter.
    
*   If only one `<geometry-box>` value is present and there is no `no-clip` keyword, both the `mask-origin` and `mask-clip` components are set to that value. As there is only one value, again the ordering doesn't matter.
    
*   If two `<geometry-box>` values are present, the first sets the `mask-origin` component and the second sets the `mask-clip` component. In this case, the order is very important.
    

Setting the incorrect order for the `mask-origin` and `mask-clip` values may affect the appearance, but will not cause the declaration to fail.

### [Ordering rules for `mask-size` and `mask-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#ordering_rules_for_mask-size_and_mask-position)

You may have noticed a slash between `mask-position` and `mask-size`, listed in the syntax as `<position>` and `<size>`. Both properties accept similar values.

`<image> <position> / <size> <repeat> <origin> <clip> <composite> <mode>`

In this case, the order is very important. If only one or a pair of [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values are present, it will define the position of the image rather than the size. Including both a position and a size in a mask layer without including the slash between the two will invalidate the entire declaration.

If a single pair of `<length-percentage>` values is present, it sets the `mask-position` property, and the `mask-size` will be `auto`. If a layer includes both a `mask-size` and a `mask-position`, the `mask-size` property value must come after the `mask-position` property value and the values must be separated by a forward slash (`/`). The slash is required even if the `mask-size` is set to a value that is not a valid `mask-position` value.

To include a `mask-size` in a mask layer using the `mask` shorthand, you must include a `mask-position` value with a slash immediately before it.

**Warning:** If you include a size in a mask layer but forget the slash after the position, the entire declaration will become invalid.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks#see_also)

----------------------------------------------------------------------------------------------------

*   [Introduction to CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Introduction)
    
*   [CSS mask properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Mask_properties)
    
*   [Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Multiple_masks/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/masking/multiple_masks/index.md?plain=1 "Folder: en-us/web/css/guides/masking/multiple_masks (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FMultiple_masks&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fmultiple_masks%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMasking%2FMultiple_masks%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmasking%2Fmultiple_masks%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
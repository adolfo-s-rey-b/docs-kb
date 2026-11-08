*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#mdn-search)
    

Logical properties for margins, borders, and padding
====================================================

The [CSS logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module defines flow-relative mappings for the various margin, border, and padding properties and their shorthands. In this guide, we take a look at these.

If you look at the [logical properties and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
 module, you may notice the list of module properties is very long. This is mostly because there are four longhand values each for margin, border, and padding side, plus all the shorthand values.

[Mappings for margins, borders, and padding](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#mappings_for_margins_borders_and_padding)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The module details mappings for each logical value to a physical counterpart. The table below maps these values for when the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 is `horizontal-tb` — with a left to right direction. The inline direction therefore runs horizontally — left to right — and [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
 would be equivalent to [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
.

If you were using a `horizontal-tb` writing mode with a right-to-left text direction then [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
 would be the same as [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
, and in a vertical writing mode it would be the same as using [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
.

| [Logical property](https://developer.mozilla.org/en-US/docs/Glossary/Logical_properties) | [Physical property](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties) |
| --- | --- |
| [`border-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end) | [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom) |
| [`border-block-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color) | [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color) |
| [`border-block-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style) | [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style) |
| [`border-block-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-width) | [`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width) |
| [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start) | [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top) |
| [`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color) | [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color) |
| [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style) | [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style) |
| [`border-block-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width) | [`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width) |
| [`border-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end) | [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right) |
| [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color) | [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color) |
| [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style) | [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style) |
| [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width) | [`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width) |
| [`border-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start) | [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left) |
| [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color) | [`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color) |
| [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style) | [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style) |
| [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width) | [`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width) |
| [`border-start-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius) | [`border-top-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius) |
| [`border-end-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-start-radius) | [`border-bottom-left-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-left-radius) |
| [`border-start-end-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-end-radius) | [`border-top-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius) |
| [`border-end-end-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-end-radius) | [`border-bottom-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-right-radius) |
| [`margin-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end) | [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom) |
| [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start) | [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top) |
| [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end) | [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right) |
| [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start) | [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left) |
| [`padding-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-end) | [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom) |
| [`padding-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-start) | [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top) |
| [`padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end) | [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right) |
| [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start) | [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left) |

There are also some additional shorthands, made possible because we can target both block or both inline edges of the box simultaneously. These shorthands have no physical equivalent.

| Property | Purpose |
| --- | --- |
| [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block) | Sets [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)<br>, [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)<br>, and [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)<br> for both block borders. |
| [`border-block-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-color) | Sets `border-color` for both block borders. |
| [`border-block-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-style) | Sets `border-style` for both block borders. |
| [`border-block-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-width) | Sets `border-width` for both block borders. |
| [`border-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline) | Sets `border-color`, `-style`, and `-width` for both inline borders. |
| [`border-inline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color) | Sets `border-color` for both inline borders. |
| [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style) | Sets `border-style` for both inline borders. |
| [`border-inline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width) | Sets `border-width` for both inline borders. |
| [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block) | Sets all the block [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)<br>s. |
| [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline) | Sets all the inline `margin`s. |
| [`padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block) | Sets the block [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)<br>. |
| [`padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline) | Sets the inline `padding`. |

[Margin examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#margin_examples)

-------------------------------------------------------------------------------------------------------------------------------------------------

The mapped margin properties of [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
, [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
, [`margin-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
, and [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
 can be used instead of their physical counterparts.

This example has two boxes with different sized margins to each edge. An extra container with a border has been included to make the margin more apparent.

One box uses physical properties and the other logical properties. Try changing the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property to `rtl` to cause the boxes to display in a right-to-left direction; the margins on the first box will stay in the same place, while the margins on the inline dimension of the second box will switch.

Also try changing the `writing-mode` from `horizontal-tb` to `vertical-rl`. Notice how the margins stay in the same place for the first box, but switch around to follow the text direction in the second.

html

    <div class="container">
      <div class="inner">
        <div class="physical box">
          margin-top: 5px<br />
          margin-right: 0<br />
          margin-bottom: 2em<br />
          margin-left: 50px
        </div>
      </div>
      <div class="inner">
        <div class="logical box">
          margin-block-start: 5px<br />
          margin-inline-end: 0<br />
          margin-block-end: 2em<br />
          margin-inline-start: 50px
        </div>
      </div>
    </div>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .container {
      display: flex;
    }
    .inner {
      border: 2px dotted grey;
    }
    .box {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      padding: 10px;
      width: 220px;
      height: 220px;
    }
    

css

    .box {
      writing-mode: horizontal-tb;
      direction: ltr;
    }
    
    .physical {
      margin-top: 5px;
      margin-right: 0;
      margin-bottom: 2em;
      margin-left: 50px;
    }
    
    .logical {
      margin-block-start: 5px;
      margin-inline-end: 0;
      margin-block-end: 2em;
      margin-inline-start: 50px;
    }
    

### [Margin shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#margin_shorthands)

There are shorthands available to target either both the inline sides or both the block sides, [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
 and [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
 respectively. Each accepts two values. The first value will apply to the start of that dimension, the second to the end. If only one value is set, it is applied to both.

In a horizontal writing mode this CSS would apply a `5px` margin to the top of the box and a `10px` margin to the bottom.

css

    .box {
      margin-block: 5px 10px;
    }
    

[Padding examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#padding_examples)

---------------------------------------------------------------------------------------------------------------------------------------------------

The mapped padding properties of [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
, [`padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
, [`padding-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-start)
, and [`padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
 can be used instead of their physical counterparts.

In this example, there are two boxes. One has physical padding properties set and the other uses logical padding properties. With a `writing-mode` of `horizontal-tb`, both boxes should appear the same.

Try changing the `direction` property to `rtl` to cause the boxes to display in a right-to-left direction. The padding on the first box will stay in the same place, whereas the padding on the inline dimension of the second box will switch.

You can also try changing the `writing-mode` from `horizontal-tb` to `vertical-rl`. Again, notice how the padding stays in the same place for the first box, but switches around to follow the text direction in the second.

html

    <div class="container">
      <div class="physical box">
        padding-top: 5px<br />
        padding-right: 0<br />
        padding-bottom: 2em<br />
        padding-left: 50px
      </div>
    
      <div class="logical box">
        padding-block-start: 5px<br />
        padding-inline-end: 0<br />
        padding-block-end: 2em<br />
        padding-inline-start: 50px
      </div>
    </div>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      display: flex;
    }
    .box {
      border: 2px solid rgb(96 139 168);
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      margin: 10px;
      width: 220px;
      height: 220px;
    }
    

css

    .box {
      writing-mode: horizontal-tb;
      direction: ltr;
    }
    
    .physical {
      padding-top: 5px;
      padding-right: 0;
      padding-bottom: 2em;
      padding-left: 50px;
    }
    
    .logical {
      padding-block-start: 5px;
      padding-inline-end: 0;
      padding-block-end: 2em;
      padding-inline-start: 50px;
    }
    

### [Padding shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#padding_shorthands)

As with margin, there are two-value shorthands for padding — [`padding-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
 and [`padding-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block)
 — which allow you to set the padding of the two inline, and two block dimensions, respectively.

In a horizontal `writing-mode`, this CSS would apply `5px` of padding to the top of the box and `10px` of padding to the bottom:

css

    .box {
      padding-block: 5px 10px;
    }
    

[Border examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#border_examples)

-------------------------------------------------------------------------------------------------------------------------------------------------

The border properties are the main reason that this module seems to have so many properties, as it provides longhand logical properties for the color, width, and style of the border on each side of a box, along with the shorthand to set all three at once for each side. As with margin and padding, there is a mapped version of each physical property.

The demo below uses some longhands and three shorthand values. As with the other demos, try changing the `direction` property to `rtl` to cause the boxes to display in a right-to-left direction, or changing the `writing-mode` from `horizontal-tb` to `vertical-rl`.

html

    <div class="container">
      <div class="physical box">Borders using physical properties.</div>
      <div class="logical box">Borders using logical properties.</div>
    </div>
    

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    
    .container {
      display: flex;
    }
    .box {
      border-radius: 5px;
      background-color: rgb(96 139 168 / 0.2);
      margin: 10px;
      width: 220px;
      height: 220px;
    }
    

css

    .box {
      writing-mode: horizontal-tb;
      direction: ltr;
    }
    
    .physical {
      border-top: 2px solid hotpink;
      border-right-style: dotted;
      border-right-color: goldenrod;
      border-right-width: 5px;
      border-bottom: 4px double black;
      border-left: none;
    }
    
    .logical {
      border-block-start: 2px solid hotpink;
      border-inline-end-style: dotted;
      border-inline-end-color: goldenrod;
      border-inline-end-width: 5px;
      border-block-end: 4px double black;
      border-inline-start: none;
    }
    

### [Border shorthands](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#border_shorthands)

There are two-value shorthands to set the width, style, and color of the block or inline dimension, and shorthands to set all three values in the block or inline dimension. The below code, in a horizontal writing mode, would give you a `2px green solid` border on the top and bottom of the box, and a `4px dotted purple` border on the left and right.

css

    .box {
      border-block: 2px solid green;
      border-inline-width: 4px;
      border-inline-style: dotted;
      border-inline-color: rebeccapurple;
    }
    

### [Flow relative border-radius properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#flow_relative_border-radius_properties)

The module has flow-relative equivalents for the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 longhands. The below example, in a horizontal `writing-mode`, would set the top-right border radius to `1em`, the bottom-right to `0`, the bottom-left to `20px` and the top-left to `40px`.

css

    .box {
      border-end-start-radius: 1em;
      border-end-end-radius: 0;
      border-start-end-radius: 20px;
      border-start-start-radius: 40px;
    }
    

[Indicating logical values for the 4-value shorthand syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding#indicating_logical_values_for_the_4-value_shorthand_syntax)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The specification makes a suggestion for the four-value shorthands such as the `margin` property, however the final decision on how this should be indicated is as yet unresolved, and is discussed in [this issue](https://github.com/w3c/csswg-drafts/issues/1282 "External link (opens in new tab)")
.

Using any four-value shorthand such as `margin`, `padding`, or `border` will currently use the physical versions, so if following the flow of the document is important, use the longhand properties for the time being.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Margins_borders_padding/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/logical_properties_and_values/margins_borders_padding/index.md?plain=1 "Folder: en-us/web/css/guides/logical_properties_and_values/margins_borders_padding (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FMargins_borders_padding&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fmargins_borders_padding%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLogical_properties_and_values%2FMargins_borders_padding%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flogical_properties_and_values%2Fmargins_borders_padding%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
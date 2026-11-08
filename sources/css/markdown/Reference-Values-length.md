*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#mdn-search)
    

`<length>` CSS type
===================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<length>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a distance value. Lengths can be used in numerous CSS properties, such as [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, [`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
, [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, and [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
.

**Note:** Although [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values are usable in some of the same properties that accept `<length>` values, they are not themselves `<length>` values. See [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#syntax)

------------------------------------------------------------------------------------------

The `<length>` data type consists of a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by one of the units listed below. As with all CSS dimensions, there is no space between the number and the unit literal. Specifying the length unit is optional if the number is `0`.

**Note:** Some properties allow negative `<length>` values, while others do not.

### [Specified vs. computed values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#specified_vs._computed_values)

The [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
 of a length (_specified length_) is represented by its quantity and unit. The [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of a length (_computed length_) is the specified length resolved to an absolute length, and its unit is not distinguished.

For some properties, such as `border-width`, `outline-width`, `column-rule-width`, and `outline-offset`, the computed `<length>` values are rounded to an integer number of [device pixels](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel)
 to ensure reasonable visual display:

*   A non-zero value less than 1 device pixel is rounded up.
*   A value greater than 1 device pixel is rounded down to the nearest whole device pixel.

For example, on a screen with a [`devicePixelRatio`](https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio "devicePixelRatio")
 of 3, `border-width: 1.5px` computes to approximately `1.33px` (rounded down from 4.5 to 4 device pixels), and `outline-width: 0.2px` computes to approximately `0.33px` (rounded up from 0.6 to 1 device pixel).

### [Relative vs. absolute lengths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_vs._absolute_lengths)

The `<length>` units can be relative or absolute. Relative lengths represent a measurement in terms of some other distance. Depending on the unit, this distance can be the size of a specific character, the [line height](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
, or the size of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
. Style sheets that use relative length units can more easily scale from one output environment to another.

**Note:** Child elements do not inherit the relative values as specified for their parent; they inherit the computed values.

[Relative length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units)

------------------------------------------------------------------------------------------------------------------------

CSS relative length units are based on font, container, or viewport sizes.

### [Relative length units based on font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_font)

Font lengths define the `<length>` value in terms of the size of a particular character or font attribute in the font currently in effect in an element or its parent.

**Note:** These units, especially `em` and the root relative `rem`, are often used to create scalable layouts, which maintain the vertical rhythm of the page even when the user changes the font size.

[`cap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cap)

Equal to the "cap height" (nominal height of capital letters) of the element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
.

[`ch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#ch)

Represents the width or, more precisely, the [advance measure](https://developer.mozilla.org/en-US/docs/Glossary/Advance_measure)
 of the glyph `0` (zero, the Unicode character U+0030) in the element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
. In cases where determining the measure of the `0` glyph is impossible or impractical, it must be assumed to be `0.5em` wide by `1em` tall.

[`em`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#em)

Represents the calculated [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the element. If used on the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 property itself, it represents the _inherited_ font-size of the element.

[`ex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#ex)

Equal to the [x-height](https://en.wikipedia.org/wiki/X-height "External link (opens in new tab)")
 of the element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
. In fonts with the `x` letter, this is generally the height of lowercase letters in the font; `1ex ≈ 0.5em` in many fonts.

[`ic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#ic)

Represents the used [advance measure](https://developer.mozilla.org/en-US/docs/Glossary/Advance_measure)
 of the "水" glyph (CJK water ideograph, U+6C34), found in the font used to render it.

[`lh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#lh)

Equal to the computed value of the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 property of the element on which it is used, converted to an absolute length. This unit enables length calculations based on the theoretical size of an ideal empty line. However, the size of actual line boxes may differ based on their content.

### [Relative length units based on root element's font](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_root_elements_font)

Root element font relative length units define the `<length>` value in terms of the size of a particular character or font attribute of the [root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 element:

[`rcap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rcap)

Equal to the "cap height" (nominal height of capital letters) of the root element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
.

[`rch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rch)

Equal to the width or the [advance measure](https://developer.mozilla.org/en-US/docs/Glossary/Advance_measure)
 of the glyph `0` (zero, the Unicode character U+0030) in the root element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
.

[`rem`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rem)

Represents the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of the root element (typically [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
). When used within the root element [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, it represents its initial value. A common browser default is `16px`, but user-defined preferences may modify this.

[`rex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rex)

Equal to the x-height of the root element's [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
.

[`ric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#ric)

Equal to the value of [`ic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#ic)
 unit on the root element's font.

[`rlh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rlh)

Equal to the value of [`lh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#lh)
 unit on the root element's font. This unit enables length calculations based on the theoretical size of an ideal empty line. However, the size of actual line boxes may differ based on their content.

### [Relative length units based on viewport](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport)

The **viewport-percentage length units** are based on four different viewport sizes: small, large, dynamic, and default. The allowance for the different viewport sizes is in response to browser interfaces expanding and retracting dynamically and hiding and showing the content underneath.

[**Small viewport units**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#small_viewport_units)

When you want the smallest possible viewport in response to browser interfaces expanding dynamically, you should use the small viewport size. The small viewport size allows the content you design to fill the entire viewport when browser interfaces are expanded. Choosing this size might also possibly leave empty spaces when browser interfaces retract.

For example, an element that is sized using viewport-percentage units based on the small viewport size, the element will fill the screen perfectly without any of its content being obscured when all the dynamic browser interfaces are shown. When those browser interfaces are hidden, however, there might be extra space visible around the element. Therefore, the small viewport-percentage units are "safer" to use in general, but might not produce the most attractive layout after a user starts interacting with the page.

The small viewport size is represented by the `sv` prefix and results in the `sv*` viewport-percentage length units. The sizes of the small viewport-percentage units are fixed, and therefore stable, unless the viewport itself is resized.

[**Large viewport units**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#large_viewport_units)

When you want the largest possible viewport in response to browser interfaces retracting dynamically, you should use the large viewport size. The large viewport size allows the content you design to fill the entire viewport when browser interfaces are retracting. You need to be aware that the content might get hidden when browser interfaces expand.

For example, on mobile phones where screen real-estate is at a premium, browsers often hide part or all of the title and address bar after a user starts scrolling the page. When an element is sized using a viewport-percentage unit based on the large viewport size, the content of the element will fill the entire visible page when these browser interfaces are hidden. However, when these retractable browser interfaces are shown, they can hide the content that is sized or positioned using the _large_ viewport-percentage units.

The large viewport unit is represented by the `lv` prefix and results in the `lv*` viewport-percentage units. The sizes of the large viewport-percentage units are fixed and therefore stable, unless the viewport itself is resized.

[**Dynamic viewport units**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#dynamic_viewport_units)

When you want the viewport to be automatically sized in response to browser interfaces dynamically expanding or retracting, you can use the dynamic viewport size. The dynamic viewport size allows the content you design to fit exactly within the viewport, irrespective of the presence of dynamic browser interfaces.

The dynamic viewport unit is represented by the `dv` prefix and results in the `dv*` viewport-percentage units. The sizes of the dynamic viewport-percentage units are not stable, even when the viewport itself is unchanged.

**Note:** While the dynamic viewport size can give you more control and flexibility, using viewport-percentage units based on the dynamic viewport size can cause the content to resize while a user is scrolling a page. This can lead to degradation of the user interface and cause a performance hit.

[**Default viewport units**](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#default_viewport_units)

The default viewport size is defined by the browser. The behavior of the resulting viewport-percentage unit could be equivalent to the viewport-percentage unit based on the small viewport size, the large viewport size, an intermediate size between the two, or the dynamic viewport size.

**Note:** For example, a browser might implement the default viewport-percentage unit for height (`vh`) that is equivalent to the large viewport-percentage height unit (`lvh`). If so, this could obscure content on a full-page display while the browser interface is expanded. Currently, all default viewport units (`vh`, `vw`, etc.) are equivalent to their large viewport counterparts (`lvh`, `lvw`, etc.).

Viewport-percentage lengths define `<length>` values in percentage relative to the size of the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
, which in turn is based on either the size of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
 or the page area, i.e., the visible portion of the document. When the height or width of the initial containing block is changed, the elements that are sized based on them are scaled accordingly. There is a viewport-percentage length unit variant corresponding to each of the viewport sizes, as described below.

**Note:** Viewport lengths are invalid in [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 declaration blocks.

[`vh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vh)

Represents a percentage of the height of the viewport's initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
. `1vh` is 1% of the viewport height. For example, if the viewport height is `300px`, then a value of `70vh` on a property will be `210px`.

The respective viewport-percentage units for small, large, and dynamic viewport sizes are `svh`, `lvh`, and `dvh`. `vh` is equivalent to `lvh`, representing the viewport-percentage length unit based on the large viewport size.

[`vw`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vw)

Represents a percentage of the width of the viewport's initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
. `1vw` is 1% of the viewport width. For example, if the viewport width is `800px`, then a value of `50vw` on a property will be `400px`.

For small, large, and dynamic viewport sizes, the respective viewport-percentage units are `svw`, `lvw`, and `dvw`. `vw` is equivalent to `lvw`, representing the viewport-percentage length unit based on the large viewport size.

[`vmax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vmax)

Represents in percentage the largest of `vw` and `vh`.

For small, large, and dynamic viewport sizes, the respective viewport-percentage units are `svmax`, `lvmax`, and `dvmax`. `vmax` is equivalent to `lvmax`, representing the viewport-percentage length unit based on the large viewport size.

[`vmin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vmin)

Represents in percentage the smallest of `vw` and `vh`.

For small, large, and dynamic viewport sizes, the respective viewport-percentage units are `svmin`, `lvmin`, and `dvmin`. `vmin` is equivalent to `lvmin`, representing the viewport-percentage length unit based on the large viewport size.

[`vb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vb)

Represents the percentage of the size of the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
, in the direction of the root element's [block axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
.

For small, large, and dynamic viewport sizes, the respective viewport-percentage units are `svb`, `lvb`, and `dvb`, respectively. `vb` is equivalent to `lvb`, representing the viewport-percentage length unit based on the large viewport size.

[`vi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#vi)

Represents a percentage of the size of the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
, in the direction of the root element's [inline axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
.

For small, large, and dynamic viewport sizes, the respective viewport-percentage units are `svi`, `lvi`, and `dvi`. `vi` is equivalent to `lvi`, representing the viewport-percentage length unit based on the large viewport size.

### [Container query length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#container_query_length_units)

When applying styles to a container using container queries, you can use container query length units. These units specify a length relative to the dimensions of a query container. Components that use units of length relative to their container are more flexible to use in different containers without having to recalculate concrete length values.

If no eligible container is available for the query, the container query length unit defaults to the [small viewport unit](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#small_viewport_units)
 for that axis (`sv*`).

For more information, see [Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
.

[`cqw`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqw)

Represents a percentage of the width of the query container. `1cqw` is 1% of the query container's width. For example, if the query container's width is `800px`, then a value of `50cqw` on a property will be `400px`.

[`cqh`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqh)

Represents a percentage of the height of the query container. `1cqh` is 1% of the query container's height. For example, if the query container's height is `300px`, then a value of `10cqh` on a property will be `30px`.

[`cqi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqi)

Represents a percentage of the inline size of the query container. `1cqi` is 1% of the query container's inline size. For example, if the query container's inline size is `800px`, then a value of `50cqi` on a property will be `400px`.

[`cqb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqb)

Represents a percentage of the block size of the query container. `1cqb` is 1% of the query container's block size. For example, if the query container's block size is `300px`, then a value of `10cqb` on a property will be `30px`.

[`cqmin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqmin)

Represents a percentage of the smaller value of either the query container's inline size or block size. `1cqmin` is 1% of the smaller value of either the query container's inline size or block size. For example, if the query container's inline size is `800px` and its block size is `300px`, then a value of `50cqmin` on a property will be `150px`.

[`cqmax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cqmax)

Represents a percentage of the larger value of either the query container's inline size or block size. `1cqmax` is 1% of the larger value of either the query container's inline size or block size. For example, if the query container's inline size is `800px` and its block size is `300px`, then a value of `50cqmax` on a property will be `400px`.

[Absolute length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)

------------------------------------------------------------------------------------------------------------------------

**Absolute length units** represent a physical measurement when the physical properties of the output medium are known, such as for print layout. This is done by anchoring one of the units to a **physical unit** or the **visual angle unit** and then defining the others relative to it. Physical units include `cm`, `in`, `mm`, `pc`, `pt`, `px`, and `Q`.The anchoring is done differently for low-resolution devices, such as screens, versus high-resolution devices, such as printers.

For low-dpi devices, the unit `px` represents the physical _reference pixel_; other units are defined relative to it. Thus, `1in` is defined as `96px`, which equals `72pt`. The consequence of this definition is that on such devices, dimensions described in inches (`in`), centimeters (`cm`), or millimeters (`mm`) don't necessarily match the size of the physical unit with the same name.

For high-dpi devices, inches (`in`), centimeters (`cm`), and millimeters (`mm`) are the same as their physical counterparts. Therefore, the `px` unit is defined relative to them (1/96 of `1in`).

**Note:** Many users increase their [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
's default font size to make text more legible. Absolute lengths can cause accessibility problems because they are fixed and do not scale according to user settings. For this reason, prefer relative lengths (such as `em` or `rem`) when setting `font-size`.

[`px`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#px)

One pixel. For screen displays, it traditionally represents one [device pixel](https://developer.mozilla.org/en-US/docs/Glossary/Device_pixel)
 (dot). However, for _printers_ and _high-resolution screens_, one CSS pixel implies multiple device pixels. `1px` = `1in / 96`.

[`cm`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#cm)

One centimeter. `1cm` = `96px / 2.54`.

[`mm`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#mm)

One millimeter. `1mm` = `1cm / 10`.

[`Q`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#q)

One quarter of a millimeter. `1Q` = `1cm / 40`.

[`in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#in)

One inch. `1in` = `2.54cm` = `96px`.

[`pc`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#pc)

One pica. `1pc` = `12pt` = `1in / 6`.

[`pt`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#pt)

One point. `1pt` = `1in / 72`.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation)

--------------------------------------------------------------------------------------------------------

When animated, values of the `<length>` data type are interpolated as real, floating-point numbers. The [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 happens on the calculated value. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#examples)

----------------------------------------------------------------------------------------------

### [Comparing different length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#comparing_different_length_units)

The following example provides you with an input field in which you can enter a `<length>` value (e.g., `300px`, `50%`, `30vw`) to set the width of a result bar that will appear below it once you've pressed the Enter or the Return key.

This allows you to compare and contrast the effects of different length units.

#### HTML

#### CSS

#### JavaScript

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# lengths](https://drafts.csswg.org/css-values/#lengths) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#see_also)

----------------------------------------------------------------------------------------------

*   [Learn: Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    
*   [CSS values & units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [Box Model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/length/index.md?plain=1 "Folder: en-us/web/css/reference/values/length (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb25b4a98b757fbd05ce1fb74b1b78f3fcf917729%0A*+Document+last+modified%3A+2026-07-08T16%3A02%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
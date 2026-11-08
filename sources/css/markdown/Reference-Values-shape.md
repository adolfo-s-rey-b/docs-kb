*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#mdn-search)
    

`<shape>` CSS type
==================

Deprecated

Avoid using this feature in new projects. The CSS Masking specification deprecated the `clip` property. This feature may be a candidate for removal from web standards or browsers.

Consider using the following features instead: [clip-path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path "The clip-path CSS property and SVG attribute set the visible area of an element. Everything outside the area will be hidden.")
.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<shape>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 defines the specific form (shape) of a region. The region represents the part of an element to which the [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
 property applies.

**Note:** `<shape>` and `rect()` work in conjunction with [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
, which has been deprecated in favor of [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
. When possible, use `clip-path` and the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 data type instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#syntax)

-----------------------------------------------------------------------------------------

The `<shape>` data type is specified using the `rect()` function, which produces a region in the form of a rectangle.

`rect()`

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#values)

![A graph showing top, right, bottom, and left, as described below. These define the rectangle's shape. The upper left corner is defined by the top and left values. The bottom right corner is defined by the bottom and right values.](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape/rect.png)

[_top_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#top)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the offset for the top of the rectangle relative to the top border of the element's box.

[_right_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#right)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the offset for the right of the rectangle relative to the left border of the element's box.

[_bottom_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#bottom)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the offset for the bottom of the rectangle relative to the top border of the element's box.

[_left_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#left)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the offset for the left of the rectangle relative to the left border of the element's box.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#interpolation)

-------------------------------------------------------------------------------------------------------

When animated, values of the `<shape>` data type are interpolated over their `top`, `right`, `bottom`, and `left` components, each treated as a real, floating-point number. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#example)

-------------------------------------------------------------------------------------------

### [Example demonstrating correct use of the rect() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#example_demonstrating_correct_use_of_the_rect_function)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# value-def-shape](https://drafts.csswg.org/css2/#value-def-shape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#see_also)

---------------------------------------------------------------------------------------------

*   Related CSS property: [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/shape/index.md?plain=1 "Folder: en-us/web/css/reference/values/shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fshape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fshape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fshape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fshape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
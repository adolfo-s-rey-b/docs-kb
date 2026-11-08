*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#mdn-search)
    

`<alpha-value>` CSS type
========================

The **`<alpha-value>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a value that can be either a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, specifying the **[alpha channel](https://developer.mozilla.org/en-US/docs/Glossary/Alpha)
** or **transparency** of a color.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#syntax)

-----------------------------------------------------------------------------------------------

The value of an `<alpha-value>` is given as either a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

If given as a number, the useful range is 0 (fully transparent) to 1.0 (fully opaque), with decimal values in between; that is, 0.5 indicates that half of the foreground color is used and half of the background color is used. Values outside the range of 0 to 1 are permitted, but are [clamped](https://en.wikipedia.org/wiki/Clamping_(graphics) "External link (opens in new tab)")
 to lie within the range 0 to 1.

If the alpha value is given as a percentage, 0% corresponds to fully transparent while 100% indicates fully opaque.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#formal_syntax)

-------------------------------------------------------------------------------------------------------------

<alpha-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#interpolation)

-------------------------------------------------------------------------------------------------------------

When animated, values of the `<alpha-value>` CSS data type are [interpolated](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 as real, floating-point numbers. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#examples)

---------------------------------------------------------------------------------------------------

### [Setting text color opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#setting_text_color_opacity)

The [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 function accepts a fourth optional value to specify an alpha value. The following example shows how to apply a color with 60% opacity using the alpha value:

css

    /* <rgb()> */
    color: rgb(34 12 64 / 60%);
    

### [Setting shape image threshold](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#setting_shape_image_threshold)

Here an alpha value is used to determine which parts of an image are considered part of a shape:

css

    /* shape-image-threshold */
    shape-image-threshold: 70%;
    shape-image-threshold: 0.7;
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 4  <br>\# typedef-color-alpha-value](https://drafts.csswg.org/css-color/#typedef-color-alpha-value) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value#see_also)

---------------------------------------------------------------------------------------------------

*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    
*   [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   [CSS Color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/alpha-value/index.md?plain=1 "Folder: en-us/web/css/reference/values/alpha-value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Falpha-value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Falpha-value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Falpha-value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Falpha-value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
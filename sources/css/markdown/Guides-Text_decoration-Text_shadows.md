*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#mdn-search)
    

Introduction to text shadows
============================

You can apply shadows to your text by using the [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
 property. This property accepts a comma-separated list of shadow values. Each shadow requires at least two [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values but can include up to three `<length>` values and one [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 value.

css

    text-shadow: 1px 3px;
    text-shadow: 1px -2px 3px white;
    text-shadow:
      5px 5px mediumblue,
      10px 10px magenta,
      15px 15px rebeccapurple;
    

To remove any shadow from the text, use the keyword `none`.

css

    text-shadow: none;
    

In this guide, we look at the components of text shadows and how you can apply multiple text shadows to an element.

[Components of text shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#components_of_text_shadows)

----------------------------------------------------------------------------------------------------------------------------------------------

Each shadow includes a horizontal offset, a vertical offset, and an optional blur radius, in that order. You can also define the color of the shadow.

### [Horizontal offset](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#horizontal_offset)

The first [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 in the value of `text-shadow` represents the horizontal offset of the shadow relative to the original text. Positive values move the shadow to the right, while negative values move it to the left. A value of `0` is a common valid value.

In this example, the different `text-shadow` declarations differ only in their horizontal offsets. The first `<length>` value moves the shadow to the left (`-30px`) or to the right (`30px`).

css

    .negative {
      text-shadow: -30px 0 1px red;
    }
    
    .positive {
      text-shadow: 30px 0 1px red;
    }
    
    .zero {
      text-shadow: 0 0 1px red;
    }
    

    <p class="negative">Negative</p>
    <p class="positive">Positive</p>
    <p class="zero">Zero</p>
    

    p {
      border: 1px solid;
      padding: 20px;
      font-family: sans-serif;
      font-size: 1.25rem;
    }
    

You may have noticed that the `text-shadow` property has no effect on the [CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
, similar to the [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 property. Just like [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
, text shadows do not affect layout, do not trigger scrolling, and do not impact the size of the scrollable overflow area. While text shadows can make an element's text appear bigger, they have no actual impact on the width (or height) of content.

### [Vertical offset](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#vertical_offset)

The second [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 in the value of `text-shadow` represents the vertical offset of the shadow relative to the original text. This required value behaves similarly to the horizontal offset, except that it moves the shadow up or down rather than left or right.

In this example, the `text-shadow` declarations differ only in their vertical offsets. The second `<length>` value moves the shadow up (`-30px`) or down (`30px`).

css

    .negative {
      text-shadow: 0 -30px 1px red;
    }
    
    .positive {
      text-shadow: 0 30px 1px red;
    }
    
    .zero {
      text-shadow: 0 0 1px red;
    }
    

### [Blur radius](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#blur_radius)

The blur radius is defined by the third [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value and is optional. If omitted, the blur radius is `0`, creating a copy of the text positioned by the first two length values. The value must be `0` or greater; the greater the value, the more widely dispersed the shadow effect will be.

In this example, the `text-shadow` declarations differ only in their blur radii. This third `<length>` value is either invalid (`-5px`), blurs the shadow (`5px`), or creates a copy of the text (`0`).

css

    .negative {
      /* invalid */
      text-shadow: 30px 30px -5px red;
    }
    
    .positive {
      text-shadow: 30px 30px 5px red;
    }
    
    .zero {
      text-shadow: 30px 30px 0 red;
    }
    

### [Shadow color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#shadow_color)

While you can apply [multiple shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#multiple_shadows)
 to text, each shadow consists of a single base color. That color can be any valid CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 value, defaulting to [`currentcolor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
 if omitted.

The following three shadows are equivalent in terms of their shadow colors:

css

    .shadow-color {
      text-shadow:
        5px 5px mediumblue,
        10px 10px magenta,
        15px 15px rebeccapurple;
    }
    
    .shadow-color-hex {
      text-shadow:
        5px 5px #0000cd,
        10px 10px #ff00ff,
        15px 15px #663399;
    }
    
    .shadow-color-rgb {
      text-shadow:
        5px 5px rgb(0 0 205),
        10px 10px rgb(255 0 255),
        15px 15px rgb(102 51 153);
    }
    

[Multiple shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#multiple_shadows)

--------------------------------------------------------------------------------------------------------------------------

You can apply multiple shadows to the same text by including multiple shadow values separated by commas.

The shadow effects are applied front-to-back: the first shadow is on top.

In our example of `text-shadow: 5px 5px mediumblue, 10px 10px magenta, 15px 15px rebeccapurple;`, it defines three shadows, with the blue one on top of the pink, which is on top of the purple:

    p {
      text-shadow:
        5px 5px mediumblue,
        10px 10px magenta,
        15px 15px rebeccapurple;
    }
    

    <p>I have three shadows</p>
    

[Multiple shadows with transparent text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows#multiple_shadows_with_transparent_text)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Shadows are painted above any background colors or images and below any borders. While shadows overlay each other, they don't overlay the text. There is no equivalent of the [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 property's `inset` keyword in the text shadow world. Unlike a box shadow, text shadows are not clipped to the shadowed shape and may show through if the text is partially-transparent.

The following examples apply the same shadows to the text but with different [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property values. The semi-transparent examples are difficult to read but are included to demonstrate how shadows render:

css

    p {
      text-shadow:
        5px 5px 0 mediumblue,
        10px 10px 5px magenta,
        15px 15px 10px rebeccapurple;
    }
    
    .opaque {
      color: black;
    }
    
    .semitransparent {
      color: rgb(0 0 0 / 0.5);
    }
    
    .transparent {
      color: transparent;
    }
    
    .white {
      color: white;
    }
    
    .semi-white {
      color: rgb(255 255 255 / 0.75);
    }
    

    <p class="opaque">The text is opaque black</p>
    <p class="semitransparent">The text is semiopaque black</p>
    <p class="transparent">The text is transparent black</p>
    <p class="white">The text is opaque white</p>
    <p class="semi-white">The text is semiopaque white</p>
    

    p {
      border: 1px solid black;
      padding: 20px;
      font-family: sans-serif;
      font-size: 1.75rem;
      font-weight: bold;
    }
    

In the "transparent" example, the text is transparent but is fully legible because the top shadow is not blurred. Note how the shadow appears behind the text and is visible when the text is less than fully opaque. This is especially noticeable in the "semi-opaque white" example. This behavior differs from non-inset box shadows, where shadows are clipped at the border's outer edge.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/text_decoration/text_shadows/index.md?plain=1 "Folder: en-us/web/css/guides/text_decoration/text_shadows (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText_decoration%2FText_shadows&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ftext_decoration%2Ftext_shadows%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText_decoration%2FText_shadows%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ftext_decoration%2Ftext_shadows%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
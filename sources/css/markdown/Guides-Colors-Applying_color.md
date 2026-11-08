*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#mdn-search)
    

Applying color to HTML elements using CSS
=========================================

With [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
, there are lots of ways to add color to your [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 [elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)
 to create the look you want. This guide is a primer introducing how CSS can be used to apply colors to HTML elements. This guide includes [lists of the CSS properties that set color in their values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#properties_that_can_have_color)
 and how to use colors both [in stylesheets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#specifying_colors_as_values_in_stylesheets)
 and [in other ways](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#other_ways_to_use_color)
.

**Note:** It is important to [use colors wisely](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely)
. Always select appropriate colors, ensuring the contrast between text and the background is sufficient to ensure legibility, and always keep the needs of people with differing visual capabilities in mind.

To learn more about CSS colors as a data type, see the [CSS `<color>` data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 reference and the [CSS color values guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
.

[Properties that can have color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#properties_that_can_have_color)

-----------------------------------------------------------------------------------------------------------------------------------------------

At the element level, everything in HTML can have color applied to it. Let's look at the different items rendered on the page — such as text, borders, etc. We'll provide lists of the CSS properties that apply color to each.

At a fundamental level, the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property defines the foreground color of an HTML element's content and the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 property defines the element's background color. These can be used on just about any element.

### [Text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#text)

Whenever an element is rendered, these properties are used to determine the color of the text, its background, and any decorations on the text.

[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)

The color to use when drawing the text and any [text decorations](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals#font_style_font_weight_text_transform_and_text_decoration)
 (such as the addition of under- or overlines, strike-through lines, and so forth).

[`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)

The text's background color.

[`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)

Configures a shadow effect to apply to text. Among the options for the shadow is the shadow's base color (which is then blurred and blended with the background based on the other parameters). See [Text drop shadows](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals#text_drop_shadows)
 to learn more.

[`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)

The default text decorations (such as underlines, strikethroughs, etc.) color is [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
. This keyword represents the current value of the `color` property. However, you can override that value and use a different color for them with the `text-decoration-color` property.

[`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)

The color to use when rendering emphasis symbols adjacent to each character in the text. This is used primarily when drawing text for East Asian languages.

[`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)

The color to use when drawing the [caret](https://developer.mozilla.org/en-US/docs/Glossary/Caret)
 (sometimes referred to as the text input cursor) within the element. This is only useful in elements that are editable, such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 or elements whose HTML [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 attribute is set to `true`.

### [Boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#boxes)

Every element is a box with some sort of content, and has a background and a border in addition to whatever contents the box may have.

[Borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#borders_2)

See the [Borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#borders_2)
 section for a list of the CSS properties you can use to set the colors of a box's borders.

[`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)

The background color to use in areas of the element that have no foreground content.

[`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)

Configures inset shadow and drop shadow effects on the box. Among the options for each shadow is the shadow's base color (which is then blurred and blended with any background based on the other parameters).

[`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)

The color to use when drawing the line separating columns of text when using [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
.

[`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)

The color to use when drawing an outline around the outside of the element. This outline is different from the border in that it doesn't get space set aside for it in the document. Outlines do not participate in the [box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
, overlapping other content. Outlines are generally used as focus indicators, indicating which element currently has focus and will receive keyboard input events.

### [Borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#borders)

Any element can have a border drawn around it. A basic element border is a line drawn around the edges of the element's content. See [The box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
 to learn about the relationship between elements and their borders, and the article [Styling borders using CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
 to learn more about applying styles to borders.

You can use the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 shorthand property, which lets you configure everything about the border in one shot (including non-color features of borders, such as its [width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
, [style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 (solid, dashed, etc.), and so forth.

[`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
 shorthand

Specifies a single color to use for every side of the element's border.

[`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
, [`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
, [`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
, and [`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)

Lets you set the color of the corresponding side of the element's border.

[`border-block-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)
 and [`border-block-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color)

With these, you can set the color used to draw the borders which are closest to the start and end of the block the border surrounds. In a left-to-right writing mode (such as the way English is written), the block start border is the top edge and the block end is the bottom. This differs from the inline start and end, which are the left and right edges (corresponding to where each line of text in the box begins and ends).

[`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)
 and [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)

These let you color the edges of the border closest to the beginning and the end of the start of lines of text within the box. Which side this is will vary depending on the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
 properties, which are typically (but not always) used to adjust text directionality based on the language being displayed. For example, if the box's text is being rendered right-to-left, then the `border-inline-start-color` is applied to the right side of the border.

[Specifying colors as values in stylesheets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#specifying_colors_as_values_in_stylesheets)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that you know which [CSS properties let you apply color to elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#properties_that_can_have_color)
, you can start adding colors to your websites. Let's look at some examples of using color within a [style sheet](https://developer.mozilla.org/en-US/docs/Glossary/Style_sheet)
. In this example, we use several previously mentioned properties, with the concept of applying colors in CSS being the same no matter the property.

Let's look at the result first, before going on to look at the code we need to create it:

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#html)

The HTML responsible for creating the above example is shown here:

Here we have a wrapper [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 containing two child `<div>`s, each with a single child paragraph ([`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
). Each content `<div>` is given a different look and feel.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#css)

Let's look at the CSS that creates the above result a piece at a time.

**Note:** We are using multiple [different CSS color value types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
 in this example to demonstrate their use. This is not recommended for production code. When writing CSS, use the most intuitive value type for you and your team.

The `.wrapper` class is used to assign styles to the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 that encloses all of our other content. This establishes the height of the container using [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, allowing the width of this block-level element to default to 100% of its parent. Setting the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex` and adding a `10px` [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 creates a flex container to lay out the children side by side with a gap between all the container's children. We use [`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
 to let the flex children grow to fill the container; it doesn't affect the flex container itself.

Of more interest to our discussion here is the use of the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 property to establish a border around the outside edge of the element. This border is a solid line, 6 pixels wide, in the [named color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 `mediumturquoise`.

Within our wrapper, we have a left box and a right box.

The `.boxLeft` class, used to style the box on the left, sets up the color of the background and the outline:

*   The box's background color is set by changing the value of the CSS [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
     property to `rgb(245 130 130)`, using the [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
     functional notation.
*   An outline is defined for the box. Unlike the more commonly used [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
     doesn't affect layout at all; it draws over the top of whatever may happen to be outside the element's box instead of making room as `border` does. This outline is a solid, dark red line that's two pixels thick. Note the use of the `darkred` keyword when specifying the color.
*   Notice that we're not explicitly setting the text color. That means the value of [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     will be inherited from the nearest containing element that defines it. By default, that's black.

**Note:** We included the `text-decoration-*` styles separately because Safari doesn't support [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 as a shorthand property.

Finally, the `.boxRight` class sets several styles on the box that's drawn to the right. Then the following colors are established (using five different ways of declaring [color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
):

*   The `background-color` is set using [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
     functional notation — `hwb(270deg 63% 13%)`. This is a medium purple color.
*   The box's `outline` is used to specify that the box should be enclosed in a four-pixel thick dashed line whose color is a somewhat deeper purple using the six-digit [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
     `#6e1478`.
*   The foreground (text) color is specified by setting the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     property using [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
     functional notation — `hsl(0deg 95% 95%)`. This is a very light pinkish color.
*   We add a green wavy line under the text with the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     shorthand, along with the longhand component for browser compatibility. We used the 3-digit [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
     `#8f8`, which is the equivalent of `#88ff88`.
*   Finally, a bit of a shadow is added to the text using [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    . Its `color` parameter is set to `black`, a [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
     value.

We used five different color syntaxes to demonstrate what is possible. In the real world, you and your team will preferably pick a preferred color notation, with everyone working on a code base using the same color syntax.

[Other ways to use color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#other_ways_to_use_color)

---------------------------------------------------------------------------------------------------------------------------------

CSS isn't the only web technology that supports color. Other examples include:

The HTML [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)

Lets you draw 2D bitmapped graphics in a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element. See our [Canvas tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
 to learn more.

[SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 (Scalable Vector Graphics)

Lets you create images using commands that draw specific shapes, patterns, and lines. SVG commands are formatted as XML, and can be embedded directly into a web page or placed in the page using the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, just like any other type of image.

[WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)

The Web Graphics Library is an OpenGL ES-based API for drawing high-performance 2D and 3D graphics on the Web. See our [WebGL tutorial](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial)
 to find out more. Also see [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API)
, a successor to WebGL for modern GPUs.

**Note:** A few now obsolete HTML attributes accepted colors as values, such as `bgcolor` and `vlink`. These attributes only accepted [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
 and three- or six-digit [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
 values.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color#see_also)

---------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   [CSS color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
     guide
*   [Using color wisely](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely)
    
*   [CSS color module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
    
*   [Drawing graphics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Drawing_graphics)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/colors/applying_color/index.md?plain=1 "Folder: en-us/web/css/guides/colors/applying_color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors%2FApplying_color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcolors%2Fapplying_color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors%2FApplying_color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcolors%2Fapplying_color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
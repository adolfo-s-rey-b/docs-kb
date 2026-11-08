*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#mdn-search)
    

Basic shapes with shape-outside
===============================

CSS shapes can be defined using the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 type. In this guide, we discuss creating rectangles, circles, ellipses, and polygons with the [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property. These are features defined in the [CSS shapes module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
.

Before looking at shapes, it is worth understanding two pieces of information that go together to make these shapes possible:

*   The `<basic-shape>` type
*   The reference box

[The <basic-shape> type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_basic-shape_type)

----------------------------------------------------------------------------------------------------------------------------------

The [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 type is used as the value for all of our basic shapes. This type is a functional notation: the function parentheses contain arguments used to describe the shape.

The accepted arguments vary depending on the shape you are creating. We will cover these in the examples below.

[The reference box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)

--------------------------------------------------------------------------------------------------------------------------

Understanding the reference box used by CSS shapes is important when using basic shapes, as it defines each shape's coordinate system. You have already met the reference box in [the guide on creating shapes from box values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/From_box_values)
, which directly uses the reference box to create the shape.

The screenshot below shows the Firefox Shapes Inspector displaying the reference box of a circle created using `shape-outside: circle(50%)`. The element has 20 pixels of padding, border, and margin applied. The Shapes Inspector highlights these reference boxes.

![Text wrapping around a circle floated left. The left edge of the text is circular abutting the clipped shape on the outside of the margin with the margin following the shape clipping.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside/shapes-reference-box.png)

The default reference box for a basic shape is the `margin-box`. You can see in the screenshot that the shape is defined relative to that part of the Box Model.

While the default reference box is `margin-box`, this can be modified. To set a different box as the reference box, include the desired box value after your basic shape definition.

These two declarations are the same:

For your shape to use a different reference box, include a different [`<box-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge)
 value, for example, to use the border as a reference box for our circle, set:

Shapes created that extend past the margin box will have the shape clipped to the margin box. The following basic shapes demonstrate this.

[inset()](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#inset)

----------------------------------------------------------------------------------------------------

The [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
 function defines a rectangle. This may not seem very useful as floating an item, without shapes, will give you a rectangular shape around it. However, the `inset()` type enables the definition of offsets, thus pulling the wrapping text around the reduced-size rectangle, over parts of the floated element.

The `inset()` function takes up to four side offset values, plus an optional `round` keyword, followed by a [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 value. The below CSS creates a rectangular shape inset from the reference box of the floated element 20 pixels from the top and bottom and 10 pixels from the left and right, with a `border-radius` value of 10 pixels.

The offset values use the same rules as the [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 shorthand. Four space-separated values define the top, right, bottom, and left offsets — in that order. You can also set more than one offset at once:

*   If there is only one value, it applies to all sides.
*   If there are two values, the top and bottom offsets are set to the first value and the right and left offsets are set to the second.
*   If there are three values, the top is set to the first value, the left and right are set to the second, and the bottom is set to the third.

The above rules can therefore also be written as:

In the example below we have an `inset()` shape used to pull content over the floated element. Change the offset values to see how the shape changes.

You can also add a box value as an alternative reference box. In the example below, try changing the reference box from `margin-box` to `border-box`, `padding-box`, or `content-box` to see how the reference box used as the starting point changes before offsets are calculated.

    <div class="box">
      <div class="shape"></div>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .shape {
      float: left;
      width: 150px;
      height: 100px;
      shape-outside: inset(20px 50px 10px 0 round 50px) margin-box;
      background-color: rebeccapurple;
      border: 2px solid black;
      border-radius: 10px;
      margin: 20px;
      padding: 20px;
    }
    

You can also create rectangles based on distances from the top and left edges of the reference box with the [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 function, or by width and height with the [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 function; both of these also support optional rounded corners.

[circle()](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#circle)

------------------------------------------------------------------------------------------------------

The [`circle()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
 value for `shape-outside` can accept two possible arguments: a `<shape-radius>` defining the size and the `<position>` defining its location.

The `circle()` and `ellipse()` `shape-outside` values both accept [`<shape-radius>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#shape-radius)
 as an argument. This can be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, or one of the keywords `closest-side` or `farthest-side`.

The `closest-side` keyword value uses the length from the center of the shape to the closest side of the reference box to create the radius length. The `farthest-side` keyword value uses the length from the center of the shape to the farthest side of the reference box.

The second argument is a `position`, which accepts a one- or two-keyword [`<position>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
 value, to indicate the position of the center of the circle. This is specified the same way as [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
; if one or both values are omitted, the values default to `center`.

To create a circle, we include a single radius value, optionally followed by the keyword **at** followed by a position value. This example has a circle applied to an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 with a `width` and `height` of `210px` and a `margin` of `20px`. This gives a total width for the reference box of `250px`. The `50%` value for the `<shape-radius>` means the radius is `125px`. The position value is set to `30%`, which is `30%` from the left and at the default vertical `center`.

html

    <div class="box">
      <img
        alt="An orange hot air balloon as seen from below"
        src="https://mdn.github.io/shared-assets/images/examples/round-balloon.png" />
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    img {
      float: left;
      shape-outside: circle(50% at 30%);
      margin: 20px;
    }
    

Play with increasing or decreasing the size of the circle by changing the size of the radius, moving the circle around with the position value, or setting a reference box as we did for `inset()`.

The below example combines generated content with a `circle()` function that uses the keywords `top left` for position. This creates a quarter circle shape in the top left corner of the page for text to flow around.

html

    <div class="box">
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .box::before {
      content: "";
      float: left;
      width: 250px;
      height: 250px;
      shape-outside: circle(50% at top left);
    }
    

### [The shape will be clipped by the margin box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_shape_will_be_clipped_by_the_margin_box)

As noted in [reference boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)
 above, the `margin-box` will clip the shape. You can see this by moving the center of our circle towards the content by setting the position to `60%`. The center of the circle will be nearer to the content and the circle will extend past the margin-box. This means that the extension becomes clipped and squared off.

![The circle shape is clipped by the margin box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside/shapes-circle-clipped.png)

[ellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#ellipse)

--------------------------------------------------------------------------------------------------------

An ellipse is a squashed circle. As such, the [`ellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
 function acts in a very similar way to `circle()` except that we have to specify two radii, `x` and `y`, in that order.

These may then be followed by one or two `<position>` values, as with `circle()`, to define the location of the center of the ellipse. In the example below, we have an ellipse with an `x` radius of `40%`, a `y` radius of `50%` and the `<position>` set to `left`. This means that the center of the ellipse is at the center of the left edge of the reference box. This creates a half ellipse shape around which the text will wrap. You can change these values to see how the ellipse changes.

html

    <div class="box">
      <div class="shape"></div>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    .shape {
      float: left;
      shape-outside: ellipse(40% 50% at left);
      margin: 20px;
      width: 100px;
      height: 200px;
    }
    

The keyword values of `closest-side` and `farthest-side` are useful in creating a quick ellipse based on the size of the floated element reference box.

    <div class="box">
      <div class="shape"></div>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .shape {
      float: left;
      shape-outside: ellipse(closest-side farthest-side at 30%);
      margin: 20px;
      width: 100px;
      height: 140px;
    }
    

[polygon()](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#polygon)

--------------------------------------------------------------------------------------------------------

The [`polygon()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
 function is more complex, enabling the creation of multiple-sided polygon shapes. This shape accepts three or more pairs of values (a polygon must at least draw a triangle). Each space-separated pair of values is separated with a comma and represents the coordinates of a single vertex drawn relative to the reference box. Each pair of coordinates defines an edge of the polygon, with the final edge defined by the first and last set of coordinates.

The example below creates a shape for text to follow using the `polygon()` function. Try changing the coordinate values to see how the shape changes.

    <div class="box">
      <div class="shape"></div>
      <p>
        One November night in the year 1782, so the story runs, two brothers sat
        over their winter fire in the little French town of Annonay, watching the
        grey smoke-wreaths from the hearth curl up the wide chimney. Their names
        were Stephen and Joseph Montgolfier, they were papermakers by trade, and
        were noted as possessing thoughtful minds and a deep interest in all
        scientific knowledge and new discovery. Before that night—a memorable night,
        as it was to prove—hundreds of millions of people had watched the rising
        smoke-wreaths of their fires without drawing any special inspiration from
        the fact.
      </p>
    </div>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .shape {
      float: left;
      shape-outside: polygon(
        0px 0px,
        0px 189px,
        100.48% 94.71%,
        200px 120px,
        80.67% 37.17%
      );
      width: 200px;
      height: 200px;
    }
    

To create even more complex shapes, you can define the outline of any shape with the [`path()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
 or [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
 functions.

The `inset()`, `circle()`, `ellipse()`, and `polygon()` are inspectable and editable using the Firefox Developer Tools Shape Inspector. The screenshot below shows the shape highlighted in the tool.

![The polygon basic shape, highlighted with the Shapes Inspector.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside/shapes-polygon.png)

Another resource is [Clippy](https://bennettfeely.com/clippy/ "External link (opens in new tab)")
, a tool for creating shapes with examples using the CSS [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property, which uses the same basic shape functions and values as the `shape-outside` property.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/shapes/using_shape-outside/index.md?plain=1 "Folder: en-us/web/css/guides/shapes/using_shape-outside (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShapes%2FUsing_shape-outside&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fshapes%2Fusing_shape-outside%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FShapes%2FUsing_shape-outside%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fshapes%2Fusing_shape-outside%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
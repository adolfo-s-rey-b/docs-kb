*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#mdn-search)
    

`polygon()` CSS function
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`polygon()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 function is one of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 [data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
. It's used to draw a [polygon](https://en.wikipedia.org/wiki/Polygon "External link (opens in new tab)")
 by providing one or more pairs of coordinates, each of which represents a vertex of the shape.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#try_it)

-------------------------------------------------------------------------------------------------------

    clip-path: polygon(
      0% 20%,
      60% 20%,
      60% 0%,
      100% 50%,
      60% 100%,
      60% 80%,
      0% 80%
    );
    

    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #default-example {
      background: #ffee99;
    }
    
    #example-element {
      background: linear-gradient(to bottom right, #ff5522, #0055ff);
      width: 100%;
      height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Coordinate list */
    polygon(50% 2.4%, 34.5% 33.8%, 0% 38.8%, 25% 63.1%, 19.1% 97.6%)
    polygon(0px 0px, 200px 100px, 0px 200px)
    polygon(0% 0px, 100% 100px, 0px 100%)
    polygon(0 0, 50% 1rem, 100% 2vw, calc(100% - 20px) 100%, 0 100%)
    
    /* Coordinate list with fill-rule and/or round value */
    polygon(nonzero, 0% 0%, 50% 50%, 0% 100%)
    polygon(round 20px, 0% 0%, 50% 50%, 0% 100%)
    polygon(evenodd round 2em, 0% 0%, 50% 50%, 0% 100%)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#parameters)

The `polygon()` function accepts an optional first parameter containing values that modify the polygon's appearance — a [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 keyword, the `round` keyword followed by a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value, or both. The first parameter's components are separated by spaces. The other parameters are space-separated x/y coordinate pairs of [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values.

[`<fill-rule>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 Optional

A keyword equal to `nonzero` (the default) or `evenodd`, which specifies the algorithm used to fill the polygon shape.

[`round <length>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#round_length)

The `round` keyword specifies that the polygon should have rounded corners, and the accompanying [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value specifies the radius of those corners.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Each vertex, or point, of the polygon is represented by a space-separated pair of `<length-percentage>` values defining the x/y coordinates of the vertex relative to the shape's [reference box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside#the_reference_box)
.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#return_value)

A [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#description)

-----------------------------------------------------------------------------------------------------------------

You can create almost any shape with the `polygon()` function by specifying the x/y coordinates of its vertices, or points, as comma-separated pairs of [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values:

`polygon(x1 y1, x2 y2, x3 y3, x4 y4, xn yn)`

Although only a single point is required to create a valid `polygon()` function value, at least 3 points are required to create a shape (a triangle). There is no upper limit on the number of points that can be specified. The shape is drawn through the specified points in the order they appear in the function, with a final line automatically being drawn between the last and first points to close the shape.

We could define the coordinates of a triangle shape like this:

| axis | point 1 | point 2 | point 3 |
| --- | --- | --- | --- |
| x   | 0%  | 100% | 100% |
| y   | 0%  | 0%  | 100% |

We can apply those coordinates to the CSS [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property in a `polygon()` function as follows:

css

    clip-path: polygon(0% 0%, 100% 0%, 100% 100%);
    

This creates a triangle shape that covers half the area of its parent container by specifying the coordinates of three of its four corners: top-left (`0% 0%`), top-right (`100% 0%`), and bottom-right (`100% 100%`). If we assume a 200x200px container with a green background:

    <div class="box"></div>
    

    .box {
      width: 200px;
      height: 200px;
      background-color: green;
      clip-path: polygon(0% 0%, 100% 0%, 100% 100%);
    }
    

### [The effect of point order](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#the_effect_of_point_order)

The order in which you define the points can result in different shapes. For example, the following two `clip-path` declarations both use a `polygon()` function with X/Y coordinate pairs for the container's four corners, but in a different order.

css

    clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
    clip-path: polygon(0% 0%, 100% 0%, 0% 100%, 100% 100%);
    

    <div class="box"></div>
    <div class="box box2"></div>
    

    body {
      display: flex;
      gap: 20px;
    }
    
    .box {
      width: 200px;
      height: 200px;
      background-color: purple;
      clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
    }
    
    .box2 {
      clip-path: polygon(0% 0%, 100% 0%, 0% 100%, 100% 100%);
    }
    

The first function draws a square, while the second draws an hourglass shape.

### [Specifying polygon modifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#specifying_polygon_modifiers)

The `polygon()` function accepts an optional first parameter modifying the rendering of the resulting shape. The parameter value can include either or both of the following, separated by spaces:

*   A [`<fill-rule>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
     keyword equal to `nonzero` (the default) or `evenodd`, which specifies the algorithm used to fill the polygon shape. This only has an effect when the lines drawn between coordinate values overlap.
*   The `round` keyword followed by a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
     value. This specifies that the polygon should have rounded corners, with the `<length>` value specifying the radius of those corners.

For example, we could expand upon the previous triangle example and add rounded corners:

css

    clip-path: polygon(round 20px, 0% 0%, 100% 0%, 100% 100%);
    

    <div class="box"></div>
    

    .box {
      width: 200px;
      height: 200px;
      background-color: green;
      clip-path: polygon(round 20px, 0% 0%, 100% 0%, 100% 100%);
    }
    

This results in the same triangle shape, but with `20px` radius rounded corners:

**Note:** In each case, the corner radius is clamped to ensure it is never larger than half of any line segment length. The maximum corner radius is clamped to the smaller of `tan(corner-angle/2) * (segment-length / 2)` evaluated against both line segments forming the corner. [The specification](https://drafts.csswg.org/css-shapes-1/#funcdef-basic-shape-polygon "External link (opens in new tab)")
 contains further details for those interested.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

<polygon()> =   
  polygon( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<fill-rule>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#examples)

-----------------------------------------------------------------------------------------------------------

### [Create a triangle](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#create_a_triangle)

In this example, a triangle is formed by defining the coordinates of its three points.

#### HTML

html

    <div class="triangle"></div>
    

#### CSS

css

    .triangle {
      width: 400px;
      height: 400px;
      background-color: magenta;
      clip-path: polygon(100% 0%, 50% 50%, 100% 100%);
    }
    

#### Result

The coordinates for the triangle are the top-right corner (`100% 0%`), the center point (`50% 50%`), and the bottom-right corner (`100% 100%`) of the container.

### [Create a rounded star](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#create_a_rounded_star)

In this example, we create a star shape and use the `round` keyword to round its corners.

#### HTML

html

    <div class="star"></div>
    

#### CSS

css

    .star {
      width: 400px;
      height: 400px;
      background-color: hotpink;
      clip-path: polygon(
        round 20px,
        50% 5%,
        60.85% 27.48%,
        85.22% 21.99%,
        74.38% 44.44%,
        93.88% 60.01%,
        69.57% 65.56%,
        69.53% 90.55%,
        50% 75%,
        30.47% 90.55%,
        30.43% 65.56%,
        6.12% 60.01%,
        25.62% 44.44%,
        14.78% 21.99%,
        39.15% 27.48%
      );
    }
    

    @supports not (clip-path: polygon(round 20px, 0% 0%, 100% 0%, 100% 100%)) {
      body::before {
        font-family: sans-serif;
        content: "Your browser does not support the polygon() function's round keyword.";
        background-color: wheat;
        padding: 1rem 0;
        text-align: center;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

### [Setting a polygon for shape-outside](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#setting_a_polygon_for_shape-outside)

In this example a shape is created for text to follow using the [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
 property.

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

    .box {
      width: 250px;
    }
    
    .shape {
      float: left;
      shape-outside: polygon(
        0 5%,
        15% 12%,
        30% 15%,
        40% 26%,
        45% 35%,
        45% 45%,
        40% 55%,
        10% 90%,
        10% 98%,
        8% 100%,
        0 100%
      );
      width: 300px;
      height: 320px;
    }
    
    p {
      font-size: 0.9rem;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# funcdef-basic-shape-polygon](https://drafts.csswg.org/css-shapes/#funcdef-basic-shape-polygon) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon#see_also)

-----------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    , [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    , [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [Guide to Basic Shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/polygon/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/polygon (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fpolygon&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fpolygon%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fpolygon%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fpolygon%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6edb918a9e6bd17858d48dcfa5d76aa5ed5b9659%0A*+Document+last+modified%3A+2026-08-24T13%3A35%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
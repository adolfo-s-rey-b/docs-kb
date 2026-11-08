*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#mdn-search)
    

`rotate3d()` CSS function
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rotate3d()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that rotates an element around a fixed axis in 3D space, without deforming it. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#try_it)

---------------------------------------------------------------------------------------------------------------

    transform: rotate3d(0, 0, 0, 0);
    

    transform: rotate3d(1, 1, 1, 45deg);
    

    transform: rotate3d(2, -1, -1, -0.2turn);
    

    transform: rotate3d(0, 1, 0.5, 3.142rad);
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        <div class="face front">1</div>
        <div class="face back">2</div>
        <div class="face right">3</div>
        <div class="face left">4</div>
        <div class="face top">5</div>
        <div class="face bottom">6</div>
      </div>
    </section>
    

    #default-example {
      background: linear-gradient(skyblue, khaki);
      perspective: 550px;
    }
    
    #example-element {
      width: 100px;
      height: 100px;
      transform-style: preserve-3d;
    }
    
    .face {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      position: absolute;
      backface-visibility: inherit;
      font-size: 60px;
      color: white;
    }
    
    .front {
      background: rgb(90 90 90 / 0.7);
      transform: translateZ(50px);
    }
    
    .back {
      background: rgb(0 210 0 / 0.7);
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(210 0 0 / 0.7);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .left {
      background: rgb(0 0 210 / 0.7);
      transform: rotateY(-90deg) translateZ(50px);
    }
    
    .top {
      background: rgb(210 210 0 / 0.7);
      transform: rotateX(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(210 0 210 / 0.7);
      transform: rotateX(-90deg) translateZ(50px);
    }
    

In 3D space, rotations have three degrees of freedom, which together describe a single axis of rotation. The axis of rotation is defined by an \[x, y, z\] vector and pass by the origin (as defined by the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 property). If, as specified, the vector is not _normalized_ (i.e., if the sum of the square of its three coordinates is not 1), the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 will normalize it internally. A non-normalizable vector, such as the null vector, \[0, 0, 0\], will cause the rotation to be ignored, but without invalidating the whole CSS property.

**Note:** Unlike rotations in the 2D plane, the composition of 3D rotations is usually not commutative. In other words, the order in which the rotations are applied impacts the result.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#syntax)

---------------------------------------------------------------------------------------------------------------

css

    rotate3d(x, y, z, a)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#values)

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#x)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 describing the x-coordinate of the vector denoting the axis of rotation which can be a positive or negative number.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#y)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 describing the y-coordinate of the vector denoting the axis of rotation which can be a positive or negative number.

[`z`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#z)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 describing the z-coordinate of the vector denoting the axis of rotation which can be a positive or negative number.

[`a`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#a)

Is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.

|     |     |
| --- | --- |
| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | This transformation applies to the 3D space and can't be represented on the plane. |
| [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") |
| Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | (1+(1−cos(a))(x2−1)z⋅sin(a)+xy(1−cos(a))−y⋅sin(a)+xz(1−cos(a))−z⋅sin(a)+xy(1−cos(a))1+(1−cos(a))(y2−1)x⋅sin(a)+yz(1−cos(a))y⋅sin(a)+xz(1−cos(a))−x⋅sin(a)+yz(1−cos(a))1+(1−cos(a))(z2−1))\\begin{pmatrix}1 + (1 - \\cos(a))(x^2 - 1) & z\\cdot \\sin(a) + xy(1 - \\cos(a)) & -y\\cdot \\sin(a) + xz(1 - \\cos(a))\\\\-z\\cdot \\sin(a) + xy(1 - \\cos(a)) & 1 + (1 - \\cos(a))(y^2 - 1) & x\\cdot \\sin(a) + yz(1 - \\cos(a))\\\\y\\cdot \\sin(a) + xz(1 - \\cos(a)) & -x\\cdot \\sin(a) + yz(1 - \\cos(a)) & 1 + (1 - \\cos(a))(z^2 - 1)\\end{pmatrix} |
| Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") | (1+(1−cos(a))(x2−1)z⋅sin(a)+xy(1−cos(a))−y⋅sin(a)+xz(1−cos(a))0−z⋅sin(a)+xy(1−cos(a))1+(1−cos(a))(y2−1)x⋅sin(a)+yz(1−cos(a))0y⋅sin(a)+xz(1−cos(a))−x⋅sin(a)+yz(1−cos(a))1+(1−cos(a))(z2−1)00001)\\begin{pmatrix}1 + (1 - \\cos(a))(x^2 - 1) & z\\cdot \\sin(a) + xy(1 - \\cos(a)) & -y\\cdot \\sin(a) + xz(1 - \\cos(a)) & 0\\\\-z\\cdot \\sin(a) + xy(1 - \\cos(a)) & 1 + (1 - \\cos(a))(y^2 - 1) & x\\cdot \\sin(a) + yz(1 - \\cos(a)) & 0\\\\y\\cdot \\sin(a) + xz(1 - \\cos(a)) & -x\\cdot \\sin(a) + yz(1 - \\cos(a)) & 1 + (1 - \\cos(a))(z^2 - 1) & 0\\\\0 & 0 & 0 & 1\\end{pmatrix} |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

<rotate3d()> =   
  rotate3d( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#examples)

-------------------------------------------------------------------------------------------------------------------

### [Rotating on the y-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#rotating_on_the_y-axis)

#### HTML

html

    <div>Normal</div>
    <div class="rotated">Rotated</div>
    

#### CSS

css

    body {
      perspective: 800px;
    }
    
    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .rotated {
      transform: rotate3d(0, 1, 0, 60deg);
      background-color: pink;
    }
    

#### Result

### [Rotating on a custom axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#rotating_on_a_custom_axis)

#### HTML

html

    <div>Normal</div>
    <div class="rotated">Rotated</div>
    

#### CSS

css

    body {
      perspective: 800px;
    }
    
    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .rotated {
      transform: rotate3d(1, 2, -1, 192deg);
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-rotate3d](https://drafts.csswg.org/css-transforms-2/#funcdef-rotate3d) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     property
*   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
     property
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/rotate3d/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/rotate3d (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Frotate3d&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotate3d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Frotate3d%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotate3d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
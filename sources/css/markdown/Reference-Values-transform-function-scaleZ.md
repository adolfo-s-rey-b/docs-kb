*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#mdn-search)
    

`scaleZ()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scaleZ()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that resizes an element along the z-axis. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#try_it)

-------------------------------------------------------------------------------------------------------------

    transform: scaleZ(1);
    

    transform: scaleZ(1.4);
    

    transform: scaleZ(0.5);
    

    transform: scaleZ(-1.4);
    

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
      perspective: 800px;
      perspective-origin: 150% 150%;
    }
    
    #example-element {
      width: 100px;
      height: 100px;
      perspective: 550px;
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
    

This scaling transformation modifies the z-coordinate of each element point by a constant factor, except when the scale factor is 1, in which case the function is the identity transform. The scaling is not isotropic, and the angles of the element are not conserved. `scaleZ(-1)` defines an [axial symmetry](https://en.wikipedia.org/wiki/Axial_symmetry "External link (opens in new tab)")
, with the z-axis passing through the origin (as specified by the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 property).

In the above interactive examples, [`perspective: 550px;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
 (to create a 3D space) and [`transform-style: preserve-3d;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style)
 (so the children, the 6 sides of the cube, are also positioned in the 3D space), have been set on the cube.

**Note:** `scaleZ(sz)` is equivalent to `scale3d(1, 1, sz)`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#syntax)

-------------------------------------------------------------------------------------------------------------

css

    scaleZ(s)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#values)

[`s`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#s)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the scaling factor to apply on the z-coordinate of each point of the element.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | (10001000s)\\left( \\begin{array}{ccc} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & s \\end{array} \\right) | (1000010000s00001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & s & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

<scaleZ()> =   
  scaleZ( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#examples)

-----------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#html)

html

    <div>Normal</div>
    <div class="perspective">Translated</div>
    <div class="scaled-translated">Scaled</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#css)

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .perspective {
      /* Includes a perspective to create a 3D space */
      transform: perspective(400px) translateZ(-100px);
      background-color: limegreen;
    }
    
    .scaled-translated {
      /* Includes a perspective to create a 3D space */
      transform: perspective(400px) scaleZ(2) translateZ(-100px);
      background-color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-scalez](https://drafts.csswg.org/css-transforms-2/#funcdef-scalez) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`scaleX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
    
*   [`scaleY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)
    
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        
    *   Note: there is no `skew` property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/scalez/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/scalez (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FscaleZ&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscalez%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FscaleZ%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscalez%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
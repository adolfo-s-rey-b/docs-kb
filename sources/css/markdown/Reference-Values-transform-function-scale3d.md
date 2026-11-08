*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#mdn-search)
    

`scale3d()` CSS function
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scale3d()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that resizes an element in 3D space. Because the amount of scaling is defined by a vector \[sx, sy, sz\], it can resize different dimensions at different scales. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#try_it)

--------------------------------------------------------------------------------------------------------------

    transform: scale3d(1, 1, 1);
    

    transform: scale3d(1.3, 1.3, 1.3);
    

    transform: scale3d(0.5, 1, 1.7);
    

    transform: scale3d(-1.4, 0.4, 0.7);
    

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
    

This scaling transformation is characterized by a three-dimensional vector. Its coordinates define how much scaling is done in each direction. If all three coordinates are equal, the scaling is uniform (_isotropic_) and the [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of the element is preserved (this is a [homothetic transformation](https://en.wikipedia.org/wiki/Homothetic_transformation "External link (opens in new tab)")
).

When a coordinate value is outside the \[-1, 1\] range, the element grows along that dimension; when inside, it shrinks. If it is negative, the result is a [point reflection](https://en.wikipedia.org/wiki/Point_reflection "External link (opens in new tab)")
 in that dimension. A value of 1 has no effect.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#syntax)

--------------------------------------------------------------------------------------------------------------

css

    scale3d(sx, sy, sz)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#values)

[`sx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#sx)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the abscissa (horizontal, x-component) of the scaling vector.

[`sy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#sy)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the ordinate (vertical, y-component) of the scaling vector.

[`sz`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#sz)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the z-component of the scaling vector.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | (sx000sy000sz)\\left( \\begin{array}{ccc} sx & 0 & 0 \\\\ 0 & sy & 0 \\\\ 0 & 0 & sz \\end{array} \\right) | (sx0000sy0000sz00001)\\left( \\begin{array}{cccc} sx & 0 & 0 & 0 \\\\ 0 & sy & 0 & 0 \\\\ 0 & 0 & sz & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

<scale3d()> =   
  scale3d( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#examples)

------------------------------------------------------------------------------------------------------------------

### [Without changing the origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#without_changing_the_origin)

#### HTML

html

    <div>Normal</div>
    <div class="scaled">Scaled</div>
    

#### CSS

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .scaled {
      transform: perspective(500px) scale3d(2, 0.7, 0.2) translateZ(100px);
      background-color: pink;
    }
    

#### Result

### [Translating the origin of the transformation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#translating_the_origin_of_the_transformation)

#### HTML

html

    <div>Normal</div>
    <div class="scaled">Scaled</div>
    

#### CSS

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .scaled {
      transform: perspective(500px) scale3d(2, 0.7, 0.2) translateZ(100px);
      transform-origin: left;
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-scale3d](https://drafts.csswg.org/css-transforms-2/#funcdef-scale3d) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`scaleZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
    
*   [`translate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)
    
*   [`rotate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/scale3d/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/scale3d (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fscale3d&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscale3d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fscale3d%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscale3d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
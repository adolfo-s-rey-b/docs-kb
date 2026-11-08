*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#mdn-search)
    

`matrix3d()` CSS function
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`matrix3d()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a 3D transformation as a 4x4 homogeneous matrix. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#try_it)

---------------------------------------------------------------------------------------------------------------

    transform: matrix3d(
      -0.6,
      1.34788,
      0,
      0,
      -2.34788,
      -0.6,
      0,
      0,
      0,
      0,
      1,
      0,
      0,
      0,
      10,
      1
    );
    

    transform: matrix3d(
      0.5,
      0,
      -0.866025,
      0,
      0.595877,
      1.2,
      -1.03209,
      0,
      0.866025,
      0,
      0.5,
      0,
      25.9808,
      0,
      15,
      1
    );
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#syntax)

---------------------------------------------------------------------------------------------------------------

css

    matrix3d(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#values)

The `matrix3d()` function is specified with 16 values. They are described in the column-major order.

[_a1_ _b1_ _c1_ _d1_ _a2_ _b2_ _c2_ _d2_ _a3_ _b3_ _c3_ _d3_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#a1)

Are [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s describing the linear transformation.

[_a4_ _b4_ _c4 d4_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#a4)

Are [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s describing the translation to apply.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | A generic 3D [affine transformation](https://en.wikipedia.org/wiki/Affine_transformation "External link (opens in new tab)")<br> can't be represented using a Cartesian-coordinate matrix, as translations are not linear transformations. | (a1a2a3a4b1b2b3b4c1c2c3c4d1d2d3d4)\\left( \\begin{array}{cccc} a1 & a2 & a3 & a4 \\\\ b1 & b2 & b3 & b4 \\\\ c1 & c2 & c3 & c4 \\\\ d1 & d2 & d3 & d4 \\\\ \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

<matrix3d()> =   
  matrix3d( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{16}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#examples)

-------------------------------------------------------------------------------------------------------------------

### [Cube squashing example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#cube_squashing_example)

The following example shows a 3D cube created from DOM elements and transforms, which can be hovered/focused to apply a `matrix3d()` transform to it.

#### HTML

html

    <section id="example-element" tabindex="0">
      <div class="face front">1</div>
      <div class="face back">2</div>
      <div class="face right">3</div>
      <div class="face left">4</div>
      <div class="face top">5</div>
      <div class="face bottom">6</div>
    </section>
    

#### CSS

css

    #example-element {
      width: 100px;
      height: 100px;
      transform-style: preserve-3d;
      transition: transform 1.5s;
      transform: rotate3d(1, 1, 1, 30deg);
      margin: 50px auto;
    }
    
    #example-element:hover,
    #example-element:focus {
      transform: rotate3d(1, 1, 1, 30deg)
        matrix3d(1, 0, 0, 0, 0, 1, 6, 0, 0, 0, 1, 0, 50, 100, 0, 1.1);
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
      background: rgb(90 90 90 / 70%);
      transform: translateZ(50px);
    }
    
    .back {
      background: rgb(0 210 0 / 70%);
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(210 0 0 / 70%);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .left {
      background: rgb(0 0 210 / 70%);
      transform: rotateY(-90deg) translateZ(50px);
    }
    
    .top {
      background: rgb(210 210 0 / 70%);
      transform: rotateX(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(210 0 210 / 70%);
      transform: rotateX(-90deg) translateZ(50px);
    }
    

#### Result

### [Matrix translation and scale example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#matrix_translation_and_scale_example)

Another `transform3d()` example, which implements an animated combined translate and scale.

#### HTML

html

    <div class="foo">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos quaerat sit
      soluta, quisquam exercitationem delectus qui unde in facere necessitatibus aut
      quia porro dolorem nesciunt enim, at consequuntur aliquam esse?
    </div>
    

#### CSS

css

    html {
      width: 100%;
    }
    body {
      height: 100vh;
      /* Centering content */
      display: flex;
      flex-flow: row wrap;
      justify-content: center;
      align-content: center;
    }
    .foo {
      width: 50%;
      padding: 1em;
      color: white;
      background: #ff8c66;
      border: 2px dashed black;
      text-align: center;
      font-family: system-ui, sans-serif;
      font-size: 14px;
      /* Setting up animation for better demonstration */
      animation: MotionScale 2s alternate linear infinite;
    }
    
    @keyframes MotionScale {
      0% {
        /*
          Identity matrix is used as basis here.
          The matrix below describes the
          following transformations:
            Translates every X point by -50px
            Translates every Y point by -100px
            Translates every Z point by 0
            Scales down by 10%
        */
        /* prettier-ignore */
        transform: matrix3d(
          1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 1, 0,
          -50, -100, 0, 1.1
        );
      }
      50% {
        /* prettier-ignore */
        transform: matrix3d(
          1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 1, 0,
          0, 0, 0, 0.9
        );
      }
      100% {
        /* prettier-ignore */
        transform: matrix3d(
          1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 1, 0,
          50, 100, 0, 1.1
        )
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-matrix3d](https://drafts.csswg.org/css-transforms-2/#funcdef-matrix3d) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/matrix3d/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/matrix3d (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fmatrix3d&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fmatrix3d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fmatrix3d%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fmatrix3d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
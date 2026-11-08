*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#mdn-search)
    

`rotateX()` CSS function
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rotateX()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that rotates an element around the x-axis (horizontal) without deforming it. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#try_it)

--------------------------------------------------------------------------------------------------------------

    transform: rotateX(0);
    

    transform: rotateX(45deg);
    

    transform: rotateX(-0.2turn);
    

    transform: rotateX(3.142rad);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

The axis of rotation passes through an origin, defined by the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 CSS property.

**Note:** `rotateX(a)` is equivalent to `rotate3d(1, 0, 0, a)`.

**Note:** Unlike rotations in the 2D plane, the composition of 3D rotations is usually not commutative. In other words, the order in which the rotations are applied impacts the result.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#syntax)

--------------------------------------------------------------------------------------------------------------

css

    rotateX(a)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#values)

[`a`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#a)

Is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 representing the angle of the rotation. A positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | (1000cos(a)\-sin(a)0sin(a)cos(a))\\left( \\begin{array}{ccc} 1 & 0 & 0 \\\\ 0 & \\cos(a) & -\\sin(a) \\\\ 0 & \\sin(a) & \\cos(a) \\end{array} \\right) | (10000cos(a)\-sin(a)00sin(a)cos(a)00001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & 0 \\\\ 0 & \\cos(a) & -\\sin(a) & 0 \\\\ 0 & \\sin(a) & \\cos(a) & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

<rotateX()> =   
  rotateX( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#examples)

------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#html)

html

    <div>Normal</div>
    <div class="rotated">Rotated</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#css)

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .rotated {
      transform: rotateX(45deg);
      background-color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-rotatex](https://drafts.csswg.org/css-transforms-2/#funcdef-rotatex) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     property
*   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
     property
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/rotatex/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/rotatex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FrotateX&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotatex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FrotateX%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotatex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
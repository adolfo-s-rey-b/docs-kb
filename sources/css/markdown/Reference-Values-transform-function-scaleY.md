*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#mdn-search)
    

`scaleY()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scaleY()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that resizes an element along the y-axis (vertically). Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#try_it)

-------------------------------------------------------------------------------------------------------------

    transform: scaleY(1);
    

    transform: scaleY(0.7);
    

    transform: scaleY(1.3);
    

    transform: scaleY(-0.5);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

It modifies the ordinate (vertical, y-coordinate) of each element point by a constant factor, except when the scale factor is 1, in which case the function is the identity transform. The scaling is not isotropic, and the angles of the element are not conserved. `scaleY(-1)` defines an [axial symmetry](https://en.wikipedia.org/wiki/Axial_symmetry "External link (opens in new tab)")
, with a horizontal axis passing through the origin (as specified by the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 property).

**Note:** `scaleY(sy)` is equivalent to `scale(1, sy)` or `scale3d(1, sy, 1)`.

`transform: rotateX(180deg);` === `transform: scaleY(-1);`

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#syntax)

-------------------------------------------------------------------------------------------------------------

css

    scaleY(s)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#values)

[`s`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#s)

Is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 representing the scaling factor to apply on the ordinate (vertical, y-coordinate) of each point of the element.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| (100s)\\left( \\begin{array}{cc} 1 & 0 \\\\ 0 & s \\end{array} \\right) | (1000s0001)\\left( \\begin{array}{ccc} 1 & 0 & 0 \\\\ 0 & s & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (1000s0001)\\left( \\begin{array}{ccc} 1 & 0 & 0 \\\\ 0 & s & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (10000s0000100001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & 0 \\\\ 0 & s & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |
| `[1 0 0 s 0 0]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

<scaleY()> =   
  scaleY( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#examples)

-----------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#html)

html

    <div>Normal</div>
    <div class="scaled">Scaled</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#css)

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .scaled {
      transform: scaleY(0.6);
      background-color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-scaley](https://drafts.csswg.org/css-transforms/#funcdef-transform-scaley) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`scaleX()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
    
*   [`scaleZ()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
    
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

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/scaley/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/scaley (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FscaleY&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscaley%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FscaleY%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscaley%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
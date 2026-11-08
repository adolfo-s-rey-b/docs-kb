*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#mdn-search)
    

`matrix()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`matrix()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a homogeneous 2D transformation matrix. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

**Note:** The `matrix(a, b, c, d, tx, ty)` function is a shorthand for `matrix3d(a, b, 0, 0, c, d, 0, 0, 0, 0, 1, 0, tx, ty, 0, 1)`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#try_it)

-------------------------------------------------------------------------------------------------------------

    transform: matrix(1.2, 0.2, -1, 0.9, 0, 20);
    

    transform: matrix(0.4, 0, 0.5, 1.2, 60, 10);
    

    transform: matrix(0, 1, 1, 0, 0, 0);
    

    transform: matrix(0.1, 1, -0.3, 1, 0, 0);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#syntax)

-------------------------------------------------------------------------------------------------------------

css

    matrix(a, b, c, d, tx, ty)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#values)

The `matrix()` function is specified with six values. The constant values are implied and not passed as parameters; the other parameters are described in the column-major order.

[_a_ _b_ _c_ _d_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#a)

Are [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s describing the linear transformation.

[_tx_ _ty_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#tx)

Are [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
s describing the translation to apply.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| (acbd)\\begin{pmatrix} a & c \\\\ b & d \\end{pmatrix} | (actxbdty001)\\left( \\begin{array}{ccc} a & c & tx \\\\ b & d & ty \\\\ 0 & 0 & 1 \\\\ \\end{array} \\right) | (actxbdty001)\\left( \\begin{array}{ccc} a & c & tx \\\\ b & d & ty \\\\ 0 & 0 & 1 \\\\ \\end{array} \\right) | (ac0txbd0ty00100001)\\left( \\begin{array}{cccc} a & c & 0 & tx \\\\ b & d & 0 & ty \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ \\end{array} \\right) |
| `[a b c d tx ty]` |

The values represent the following functions: `matrix(scaleX(), skewY(), skewX(), scaleY(), translateX(), translateY())`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

<matrix()> =   
  matrix( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{6}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#examples)

-----------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#html)

html

    <div>Normal</div>
    <div class="changed">Changed</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#css)

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .changed {
      transform: matrix(1, 2, -1, 1, 80, 80);
      background-color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-matrix](https://drafts.csswg.org/css-transforms/#funcdef-transform-matrix) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`matrix3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/matrix/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/matrix (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fmatrix&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fmatrix%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fmatrix%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fmatrix%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
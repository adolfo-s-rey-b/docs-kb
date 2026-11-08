*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#mdn-search)
    

`rotate()` CSS function
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rotate()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that rotates an element around a fixed point on the 2D plane, without deforming it. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#try_it)

-------------------------------------------------------------------------------------------------------------

    transform: rotate(0);
    

    transform: rotate(90deg);
    

    transform: rotate(-0.25turn);
    

    transform: rotate(3.142rad);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

The fixed point that the element rotates around — mentioned above — is also known as the **transform origin**. This defaults to the center of the element, but you can set your own custom transform origin using the [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
 property.

**Note:** The SVG [`transform`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/transform)
 attribute has its own grammar, in which `rotate()` accepts two optional extra values giving the center of rotation, as in `rotate(45, 50, 50)`. That form is only valid in the attribute, not in CSS: the CSS `rotate()` function takes an angle alone, and the center is set with [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#syntax)

-------------------------------------------------------------------------------------------------------------

css

    rotate(a)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#values)

[_a_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#a)

Is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 representing the angle of the rotation. The direction of rotation depends on the writing direction. In a left-to-right context, a positive angle denotes a clockwise rotation, a negative angle a counter-clockwise one. In a right-to-left context, a positive angle denotes a counter-clockwise rotation, a negative angle a clockwise one. A rotation by 180° is called _point reflection_.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| (cos(a)\-sin(a)sin(a)cos(a))\\left( \\begin{array}{cc} \\cos(a) & -\\sin(a) \\\\ \\sin(a) & \\cos(a) \\end{array} \\right) | (cos(a)\-sin(a)0sin(a)cos(a)0001)\\left( \\begin{array}{ccc} \\cos(a) & -\\sin(a) & 0 \\\\ \\sin(a) & \\cos(a) & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (cos(a)\-sin(a)0sin(a)cos(a)0001)\\left( \\begin{array}{ccc} \\cos(a) & -\\sin(a) & 0 \\\\ \\sin(a) & \\cos(a) & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (cos(a)\-sin(a)00sin(a)cos(a)0000100001)\\left( \\begin{array}{cccc} \\cos(a) & -\\sin(a) & 0 & 0 \\\\ \\sin(a) & \\cos(a) & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ \\end{array} \\right) |
| `[cos(a) sin(a) -sin(a) cos(a) 0 0]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

<rotate()> =   
  rotate( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#basic_example)

#### HTML

html

    <div>Normal</div>
    <div class="rotated">Rotated</div>
    

#### CSS

css

    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .rotated {
      transform: rotate(45deg); /* Equal to rotateZ(45deg) */
      background-color: pink;
    }
    

#### Result

### [Combining rotation with another transformation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#combining_rotation_with_another_transformation)

If you want to apply multiple transformations to an element, be careful about the order in which you specify your transformations. For example, if you rotate before translating, the translation will be along the new axis of rotation!

#### HTML

html

    <div>Normal</div>
    <div class="rotate">Rotated</div>
    <div class="rotate-translate">Rotated + Translated</div>
    <div class="translate-rotate">Translated + Rotated</div>
    

#### CSS

css

    div {
      position: absolute;
      left: 40px;
      top: 40px;
      width: 100px;
      height: 100px;
      background-color: lightgray;
    }
    
    .rotate {
      background-color: transparent;
      outline: 2px dashed;
      transform: rotate(45deg);
    }
    
    .rotate-translate {
      background-color: pink;
      transform: rotate(45deg) translateX(180px);
    }
    
    .translate-rotate {
      background-color: gold;
      transform: translateX(180px) rotate(45deg);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-rotate](https://drafts.csswg.org/css-transforms/#funcdef-transform-rotate) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     property
*   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
     property
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`rotate3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 31, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/rotate/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/rotate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Frotate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Frotate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Frotate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F80ab11f9d757b49325122071a8a6210440ec6551%0A*+Document+last+modified%3A+2026-07-31T09%3A57%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
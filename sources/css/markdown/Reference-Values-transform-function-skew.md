*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#mdn-search)
    

`skew()` CSS function
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`skew()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that skews an element on the 2D plane. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#try_it)

-----------------------------------------------------------------------------------------------------------

    transform: skew(0);
    

    transform: skew(15deg, 15deg);
    

    transform: skew(-0.06turn, 18deg);
    

    transform: skew(0.312rad);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

This transformation is a shear mapping ([transvection](https://en.wikipedia.org/wiki/Shear_mapping "External link (opens in new tab)")
) that distorts each point within an element by a certain angle in the horizontal and vertical directions. The effect is as if you grabbed each corner of the element and pulled them along a certain angle.

The coordinates of each point are modified by a value proportionate to the specified angle and the distance to the origin. Thus, the farther from the origin a point is, the greater the value added to it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#syntax)

-----------------------------------------------------------------------------------------------------------

css

    skew(ax)
    
    skew(ax, ay)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#values)

[`ax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#ax)

Is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 representing the angle to use to distort the element along the x-axis.

[`ay` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#ay)

Is an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 representing the angle to use to distort the element along the y-axis. If not defined, its default value is `0`, resulting in a purely horizontal skewing.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| (1tan(ax)tan(ay)1)\\left( \\begin{array}{cc} 1 & \\tan(ax) \\\\ \\tan(ay) & 1 \\end{array} \\right) | (1tan(ax)0tan(ay)10001)\\left( \\begin{array}{ccc} 1 & \\tan(ax) & 0 \\\\ \\tan(ay) & 1 & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (1tan(ax)0tan(ay)10001)\\left( \\begin{array}{ccc} 1 & \\tan(ax) & 0 \\\\ \\tan(ay) & 1 & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (1tan(ax)00tan(ay)10000100001)\\left( \\begin{array}{cccc} 1 & \\tan(ax) & 0 & 0 \\\\ \\tan(ay) & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |
| `[1 tan(ay) tan(ax) 1 0 0]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

<skew()> =   
  skew( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <zero> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#examples)

---------------------------------------------------------------------------------------------------------------

### [Skewing on the x-axis only](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#skewing_on_the_x-axis_only)

#### HTML

html

    <div>Normal</div>
    <div class="skewed">Skewed</div>
    

#### CSS

css

    body {
      margin: 20px;
    }
    
    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .skewed {
      transform: skew(10deg); /* Equal to skewX(10deg) */
      background-color: pink;
    }
    

#### Result

### [Skewing on both axes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#skewing_on_both_axes)

#### HTML

html

    <div>Normal</div>
    <div class="skewed">Skewed</div>
    

#### CSS

css

    body {
      margin: 20px;
    }
    
    div {
      width: 80px;
      height: 80px;
      background-color: skyblue;
    }
    
    .skewed {
      transform: skew(10deg, 10deg);
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-skew](https://drafts.csswg.org/css-transforms/#funcdef-transform-skew) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [skewX()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)
    
*   [skewY()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)
    
*   Individual transform properties:
    *   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
        
    *   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
        
    *   [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
        
    *   Note: there is no `skew` property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/skew/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/skew (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fskew&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fskew%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fskew%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fskew%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
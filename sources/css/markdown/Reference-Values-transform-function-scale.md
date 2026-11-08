*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#mdn-search)
    

`scale()` CSS function
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scale()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines a transformation that resizes an element on the 2D plane. Because the amount of scaling is defined by a vector \[sx, sy\], it can resize the horizontal and vertical dimensions at different scales. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#try_it)

------------------------------------------------------------------------------------------------------------

    transform: scale(1);
    

    transform: scale(0.7);
    

    transform: scale(1.3, 0.4);
    

    transform: scale(-0.5, 1);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

This scaling transformation is characterized by a two-dimensional vector. Its coordinates define how much scaling is done in each direction. If both coordinates are equal, the scaling is uniform (_isotropic_) and the aspect ratio of the element is preserved (this is a [homothetic transformation](https://en.wikipedia.org/wiki/Homothetic_transformation "External link (opens in new tab)")
).

When a coordinate value is outside the \[-1, 1\] range, the element grows along that dimension; when inside, it shrinks. A negative value results in a [point reflection](https://en.wikipedia.org/wiki/Point_reflection "External link (opens in new tab)")
 in that dimension. The value `1` has no effect.

**Note:** The `scale()` function only scales in 2D. To scale in 3D, use [`scale3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
 instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#syntax)

------------------------------------------------------------------------------------------------------------

css

    scale(sx)
    
    scale(sx, sy)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#values)

[`sx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#sx)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the abscissa (horizontal, x-component) of the scaling vector.

[`sy` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#sy)

A [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the ordinate (vertical, y-component) of the scaling vector. If not defined, its default value is `sx`, resulting in a uniform scaling that preserves the element's [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| (sx00sy)\\left( \\begin{array}{cc} sx & 0 \\\\ 0 & sy \\end{array} \\right) | (sx000sy0001)\\left( \\begin{array}{ccc} sx & 0 & 0 \\\\ 0 & sy & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (sx000sy0001)\\left( \\begin{array}{ccc} sx & 0 & 0 \\\\ 0 & sy & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (sx0000sy0000100001)\\left( \\begin{array}{cccc} sx & 0 & 0 & 0 \\\\ 0 & sy & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |
| `[sx 0 0 sy 0 0]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

<scale()> =   
  scale( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#accessibility)

--------------------------------------------------------------------------------------------------------------------------

Scaling/zooming animations are problematic for accessibility, as they are a common trigger for certain types of migraine. If you need to include such animations on your website, you should provide a control to allow users to turn off animations, preferably site-wide.

Also, consider making use of the [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 media feature — use it to write a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
 that will turn off animations if the user has reduced animation specified in their system preferences.

Find out more:

*   [MDN Understanding WCAG, Guideline 2.3 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.3_%e2%80%94_seizures_and_physical_reactions_do_not_design_content_in_a_way_that_is_known_to_cause_seizures_or_physical_reactions)
    
*   [Understanding Success Criterion 2.3.3 | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#examples)

----------------------------------------------------------------------------------------------------------------

### [Scaling the X and Y dimensions together](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#scaling_the_x_and_y_dimensions_together)

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
      transform: scale(0.7); /* Equal to scaleX(0.7) scaleY(0.7) */
      background-color: pink;
    }
    

#### Result

### [Scaling X and Y dimensions separately, and translating the origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#scaling_x_and_y_dimensions_separately_and_translating_the_origin)

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
      transform: scale(2, 0.5); /* Equal to scaleX(2) scaleY(0.5) */
      transform-origin: left;
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-scale](https://drafts.csswg.org/css-transforms/#funcdef-transform-scale) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
    
*   [`zoom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/zoom)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`scale3d()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
    
*   Other individual transform properties [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
     and [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/scale/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/scale (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fscale&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscale%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Fscale%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Fscale%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#mdn-search)
    

`translate()` CSS function
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`translate()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 repositions an element in the horizontal and/or vertical directions. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#try_it)

----------------------------------------------------------------------------------------------------------------

    transform: translate(0);
    

    transform: translate(42px, 18px);
    

    transform: translate(-2.1rem, -2ex);
    

    transform: translate(3ch, 3mm);
    

    <section id="default-example">
      <img
        class="transition-all"
        id="static-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/firefox-logo.svg"
        width="200" />
    </section>
    

    #static-element {
      opacity: 0.4;
      position: absolute;
    }
    
    #example-element {
      position: absolute;
    }
    

This transformation is characterized by a two-dimensional vector \[tx, ty\]. Its coordinates define how much the element moves in each direction.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#syntax)

----------------------------------------------------------------------------------------------------------------

css

    /* Single <length-percentage> values */
    transform: translate(200px);
    transform: translate(50%);
    
    /* Double <length-percentage> values */
    transform: translate(100px, 200px);
    transform: translate(100px, 50%);
    transform: translate(30%, 200px);
    transform: translate(30%, 50%);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#values)

[Single `<length-percentage>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#single_length-percentage_values)

This value is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the abscissa (horizontal, x-component) of the translating vector \[tx, 0\]. The ordinate (vertical, y-component) of the translating vector will be set to `0`. For example, `translate(2px)` is equivalent to `translate(2px, 0)`. A percentage value refers to the width of the reference box defined by the [`transform-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
 property.

[Double `<length-percentage>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#double_length-percentage_values)

This value describes two [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values representing both the abscissa (horizontal, x-component) and the ordinate (vertical, y-component) of the translating vector \[tx, ty\]. A percentage as first value refers to the width, as second part to the height of the reference box defined by the [`transform-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
 property.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| A translation is not a linear transformation in ℝ^2 and can't be represented using a Cartesian-coordinate matrix. | (10tx01ty001)\\left( \\begin{array}{ccc} 1 & 0 & tx \\\\ 0 & 1 & ty \\\\ 0 & 0 & 1 \\end{array} \\right) | (10tx01ty001)\\left( \\begin{array}{ccc} 1 & 0 & tx \\\\ 0 & 1 & ty \\\\ 0 & 0 & 1 \\end{array} \\right) | (100tx010ty00100001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & tx \\\\ 0 & 1 & 0 & ty \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |
| `[1 0 0 1 tx ty]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#formal_syntax)

------------------------------------------------------------------------------------------------------------------------------

<translate()> =   
  translate( <length-percentage> , <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#examples)

--------------------------------------------------------------------------------------------------------------------

### [Using a single-axis translation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#using_a_single-axis_translation)

#### HTML

html

    <div>Static</div>
    <div class="moved">Moved</div>
    <div>Static</div>
    

#### CSS

css

    div {
      width: 60px;
      height: 60px;
      background-color: skyblue;
    }
    
    .moved {
      /* Equal to: translateX(10px) or translate(10px, 0) */
      transform: translate(10px);
      background-color: pink;
    }
    

#### Result

### [Combining y-axis and x-axis translation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#combining_y-axis_and_x-axis_translation)

#### HTML

html

    <div>Static</div>
    <div class="moved">Moved</div>
    <div>Static</div>
    

#### CSS

css

    div {
      width: 60px;
      height: 60px;
      background-color: skyblue;
    }
    
    .moved {
      transform: translate(10px, 10px);
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-translate](https://drafts.csswg.org/css-transforms/#funcdef-transform-translate) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/translate/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/translate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Ftranslate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Ftranslate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#mdn-search)
    

`translateX()` CSS function
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`translateX()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 repositions an element horizontally on the 2D plane. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#try_it)

-----------------------------------------------------------------------------------------------------------------

    transform: translateX(0);
    

    transform: translateX(42px);
    

    transform: translateX(-2.1rem);
    

    transform: translateX(3ch);
    

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
    

**Note:** `translateX(tx)` is equivalent to `translate(tx, 0)` or `translate3d(tx, 0, 0)`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* <length-percentage> values */
    transform: translateX(200px);
    transform: translateX(50%);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#length-percentage)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the abscissa (horizontal, x-component) of the translating vector \[tx, 0\]. In [Cartesian coordinate system](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)
 it represents shift along x-axis. A percentage value refers to the width of the reference box defined by the [`transform-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
 property.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| A translation is not a linear transformation in ℝ^2 and can't be represented using a Cartesian-coordinate matrix. | (10t010001)\\left( \\begin{array}{ccc} 1 & 0 & t \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (10t010001)\\left( \\begin{array}{ccc} 1 & 0 & t \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{array} \\right) | (100t010000100001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & t \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |
| `[1 0 0 1 t 0]` |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

<translateX()> =   
  translateX( <length-percentage> )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#examples)

---------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#html)

html

    <div>Static</div>
    <div class="moved">Moved</div>
    <div>Static</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#css)

css

    div {
      width: 60px;
      height: 60px;
      background-color: skyblue;
    }
    
    .moved {
      transform: translateX(10px); /* Equal to translate(10px) */
      background-color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# funcdef-transform-translatex](https://drafts.csswg.org/css-transforms/#funcdef-transform-translatex) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`translate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
    
*   [`translateY()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)
    
*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/translatex/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/translatex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FtranslateX&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslatex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FtranslateX%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslatex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
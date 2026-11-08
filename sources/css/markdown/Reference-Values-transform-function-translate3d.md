*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#mdn-search)
    

`translate3d()` CSS function
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`translate3d()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 repositions an element in 3D space. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#try_it)

------------------------------------------------------------------------------------------------------------------

    transform: translate3d(0, 0, 0);
    

    transform: translate3d(42px, -62px, -135px);
    

    transform: translate3d(-2.7rem, 0, 1rem);
    

    transform: translate3d(5ch, 0.4in, 5em);
    

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
    

This transformation is characterized by a three-dimensional vector \[tx, ty, tz\]. Its coordinates define how much the element moves in each direction.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#syntax)

------------------------------------------------------------------------------------------------------------------

css

    translate3d(tx, ty, tz)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#values)

[`tx`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#tx)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the abscissa (horizontal, x-component) of the translating vector \[tx, ty, tz\].

[`ty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#ty)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 representing the ordinate (vertical, y-component)of the translating vector \[tx, ty, tz\].

[`tz`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#tz)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the z-component of the translating vector. It can't be a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value; in that case the property containing the transform is considered invalid \[tx, ty, tz\].

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | A translation is not a linear transformation in ℝ^3 and can't be represented using a Cartesian-coordinate matrix. | (100tx010ty001tz0001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & tx \\\\ 0 & 1 & 0 & ty \\\\ 0 & 0 & 1 & tz \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------------

<translate3d()> =   
  translate3d( <length-percentage> , <length-percentage> , [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#examples)

----------------------------------------------------------------------------------------------------------------------

### [Using a single axis translation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#using_a_single_axis_translation)

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
      /* Equivalent to perspective(500px) translateX(10px) */
      transform: perspective(500px) translate3d(10px, 0, 0px);
      background-color: pink;
    }
    

#### Result

### [Combining z-axis and x-axis translation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#combining_z-axis_and_x-axis_translation)

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
      transform: perspective(500px) translate3d(10px, 0, 100px);
      background-color: pink;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-translate3d](https://drafts.csswg.org/css-transforms-2/#funcdef-translate3d) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/translate3d/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/translate3d (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Ftranslate3d&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslate3d%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2Ftranslate3d%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslate3d%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
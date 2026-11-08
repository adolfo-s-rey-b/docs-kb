*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#mdn-search)
    

`translateZ()` CSS function
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`translateZ()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 repositions an element along the z-axis in 3D space, i.e., closer to or farther away from the viewer. Its result is a [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 data type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#try_it)

-----------------------------------------------------------------------------------------------------------------

    transform: translateZ(0);
    

    transform: translateZ(42px);
    

    transform: translateZ(-9.7rem);
    

    transform: translateZ(-3ch);
    

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
    

This transformation is defined by a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 which specifies how far inward or outward the element or elements move.

In the above interactive examples, [`perspective: 550px;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
 (to create a 3D space) and [`transform-style: preserve-3d;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style)
 (so the children, the 6 sides of the cube, are also positioned in the 3D space), have been set on the cube.

**Note:** `translateZ(tz)` is equivalent to `translate3d(0, 0, tz)`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    translateZ(tz)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#values)

[`tz`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#tz)

A [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 representing the z-component of the translating vector \[0, 0, tz\]. In [Cartesian coordinate system](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)
 it represents shift along z-axis. A positive value moves the element towards the viewer, and a negative value farther away.

| [Cartesian coordinates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function#cartesian_coordinates)<br> on [ℝ^2](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | [Homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "External link (opens in new tab)")<br> on [ℝℙ^2](https://en.wikipedia.org/wiki/Real_projective_plane "External link (opens in new tab)") | Cartesian coordinates on [ℝ^3](https://en.wikipedia.org/wiki/Real_coordinate_space "External link (opens in new tab)") | Homogeneous coordinates on [ℝℙ^3](https://en.wikipedia.org/wiki/Real_projective_space "External link (opens in new tab)") |
| --- | --- | --- | --- |
| This transformation applies to the 3D space and can't be represented on the plane. |     | A translation is not a linear transformation in ℝ^3 and can't be represented using a Cartesian-coordinate matrix. | (10000100001t0001)\\left( \\begin{array}{cccc} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & t \\\\ 0 & 0 & 0 & 1 \\end{array} \\right) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

<translateZ()> =   
  translateZ( [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#examples)

---------------------------------------------------------------------------------------------------------------------

In this example, two boxes are created. One is positioned normally on the page, without being translated at all. The second is altered by applying perspective to create a 3D space, then moved towards the user.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#html)

html

    <div>Static</div>
    <div class="moved">Moved</div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#css)

css

    div {
      position: relative;
      width: 60px;
      height: 60px;
      left: 100px;
      background-color: skyblue;
    }
    
    .moved {
      transform: perspective(500px) translateZ(200px);
      background-color: pink;
    }
    

What really matters here is the class "moved"; let's take a look at what it does. First, the [`perspective()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)
 function positions the viewer relative to the plane that lies where z=0 (in essence, the surface of the screen). A value of `500px` means the user is 500 pixels "in front of" the imagery located at z=0.

Then, the `translateZ()` function moves the element 200 pixels "outward" from the screen, toward the user. This has the effect of making the element appear larger when viewed on a 2D display, or closer when viewed using a VR headset or other 3D display device.

Note if the `perspective()` value is less than the `translateZ()` value, such as `transform: perspective(200px) translateZ(300px);` the transformed element will not be visible as it is further than the user's viewport. The smaller the difference between the perspective and translateZ values, the closer the user is to the element and the larger the translated element will seem.

**Note:** As the composition of transforms isn't commutative, the order you write the different functions is significant. In particular, in general, you want `perspective()` to be placed before `translateZ()`.

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# funcdef-translatez](https://drafts.csswg.org/css-transforms-2/#funcdef-translatez) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/transform-function/translatez/index.md?plain=1 "Folder: en-us/web/css/reference/values/transform-function/translatez (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FtranslateZ&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslatez%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftransform-function%2FtranslateZ%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftransform-function%2Ftranslatez%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
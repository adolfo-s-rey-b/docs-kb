*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#mdn-search)
    

Using CSS transforms
====================

By modifying the coordinate space, **CSS transforms** change the shape and position of the affected content without disrupting the normal document flow. This guide provides an introduction to using transforms.

CSS transforms are implemented using a set of CSS properties that let you apply affine linear transformations to HTML elements. These transformations include rotation, skewing, scaling, and translation both in the plane and in the 3D space.

**Warning:** Only transformable elements can be `transform`ed; that is, all elements whose layout is governed by the CSS [box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model)
 except for: [non-replaced inline boxes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model#inline-level_and_block-level_boxes)
, [table-column boxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
, and [table-column-group boxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
.

[CSS transforms properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#css_transforms_properties)

--------------------------------------------------------------------------------------------------------------------------------

Two major properties are used to define CSS transforms: [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 (or the individual [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
, [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
, and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
 properties) and [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
.

[`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)

Specifies the position of the origin. By default, it is at the center of the element and can be moved. It is used by several transforms, like rotations, scaling or skewing, that need a specific point as a parameter.

[`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)

Specifies the transforms to apply to the element. It is a space-separated list of transforms, which are applied one after the other, as requested by the composition operation. Composite transforms are effectively applied in order from right to left.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#examples)

----------------------------------------------------------------------------------------------

Here is an unaltered image of the MDN logo:

![MDN Logo](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using/logo.png)

### [Rotating](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#rotating)

Here is the MDN logo rotated 90 degrees from its bottom-left corner.

html

    <img src="logo.png" alt="MDN Logo" />
    

css

    img {
      rotate: 90deg;
      transform-origin: bottom left;
    }
    

### [Skewing and translating](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#skewing_and_translating)

Here is the MDN logo, skewed by 10 degrees and translated by 150 pixels on the X-axis.

html

    <img src="logo.png" alt="MDN logo" />
    

css

    img {
      transform: skewX(10deg) translateX(150px);
      transform-origin: bottom left;
    }
    

[3D specific CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#3d_specific_css_properties)

----------------------------------------------------------------------------------------------------------------------------------

Performing CSS transformations in 3D space is a bit more complex. You have to start by configuring the 3D space by giving it a perspective, then you have to configure how your 2D elements will behave in that space.

### [Perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#perspective)

The first element to set is the [`perspective`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
. The perspective is what gives us the 3D impression. The farther from the viewer the elements are, the smaller they are.

#### Setting perspective

This example shows a cube with the perspective set at different positions. How quick the cube shrinks is defined by the [`perspective`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
 property. The smaller its value is, the deeper the perspective is.

##### HTML

The HTML below creates four copies of the same box, with the perspective set at different values.

html

    <table>
      <tbody>
        <tr>
          <th><code>perspective: 250px;</code></th>
          <th><code>perspective: 350px;</code></th>
        </tr>
        <tr>
          <td>
            <div class="container">
              <div class="cube perspective-250">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
          </td>
          <td>
            <div class="container">
              <div class="cube perspective-350">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
          </td>
        </tr>
        <tr>
          <th><code>perspective: 500px;</code></th>
          <th><code>perspective: 650px;</code></th>
        </tr>
        <tr>
          <td>
            <div class="container">
              <div class="cube perspective-500">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
          </td>
          <td>
            <div class="container">
              <div class="cube perspective-650">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    

##### CSS

The CSS establishes classes that can be used to set the perspective to different distances. It also includes classes for the container box and the cube itself, as well as each of its faces.

css

    /* Shorthand classes for different perspective values */
    .perspective-250 {
      perspective: 250px;
    }
    
    .perspective-350 {
      perspective: 350px;
    }
    
    .perspective-500 {
      perspective: 500px;
    }
    
    .perspective-650 {
      perspective: 650px;
    }
    
    /* Define the container div, the cube div, and a generic face */
    .container {
      width: 200px;
      height: 200px;
      margin: 75px 0 0 75px;
      border: none;
    }
    
    .cube {
      width: 100%;
      height: 100%;
      perspective-origin: 150% 150%;
      transform-style: preserve-3d;
    }
    
    .face {
      display: block;
      position: absolute;
      width: 100px;
      height: 100px;
      border: none;
      line-height: 100px;
      font-family: sans-serif;
      font-size: 60px;
      color: white;
      text-align: center;
      backface-visibility: visible;
    }
    
    /* Define each face based on direction */
    .front {
      background: rgb(0 0 0 / 30%);
      transform: translateZ(50px);
    }
    
    .back {
      background: lime;
      color: black;
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(196 0 0 / 70%);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .left {
      background: rgb(0 0 196 / 70%);
      transform: rotateY(-90deg) translateZ(50px);
    }
    
    .top {
      background: rgb(196 196 0 / 70%);
      transform: rotateX(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(196 0 196 / 70%);
      transform: rotateX(-90deg) translateZ(50px);
    }
    
    /* Make the table a little nicer */
    th,
    p,
    td {
      background-color: #eeeeee;
      padding: 10px;
      font-family: sans-serif;
      text-align: left;
    }
    

##### Result

The second element to configure is the position of the viewer, with the [`perspective-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective-origin)
 property. By default the perspective is centered on the viewer, which is not always adequate.

#### Changing the perspective origin

This example shows cubes with popular `perspective-origin` values.

##### HTML

html

    <section>
      <figure>
        <figcaption><code>perspective-origin: top left;</code></figcaption>
        <div class="container">
          <div class="cube po-tl">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: top;</code></figcaption>
        <div class="container">
          <div class="cube po-tm">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: top right;</code></figcaption>
        <div class="container">
          <div class="cube po-tr">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: left;</code></figcaption>
        <div class="container">
          <div class="cube po-ml">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: 50% 50%;</code></figcaption>
        <div class="container">
          <div class="cube po-mm">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: right;</code></figcaption>
        <div class="container">
          <div class="cube po-mr">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: bottom left;</code></figcaption>
        <div class="container">
          <div class="cube po-bl">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: bottom;</code></figcaption>
        <div class="container">
          <div class="cube po-bm">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: bottom right;</code></figcaption>
        <div class="container">
          <div class="cube po-br">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: -200% -200%;</code></figcaption>
        <div class="container">
          <div class="cube po-200200neg">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: 200% 200%;</code></figcaption>
        <div class="container">
          <div class="cube po-200200pos">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    
      <figure>
        <figcaption><code>perspective-origin: 200% -200%;</code></figcaption>
        <div class="container">
          <div class="cube po-200200">
            <div class="face front">1</div>
            <div class="face back">2</div>
            <div class="face right">3</div>
            <div class="face left">4</div>
            <div class="face top">5</div>
            <div class="face bottom">6</div>
          </div>
        </div>
      </figure>
    </section>
    

##### CSS

css

    /* perspective-origin values (unique per example) */
    .po-tl {
      perspective-origin: top left;
    }
    .po-tm {
      perspective-origin: top;
    }
    .po-tr {
      perspective-origin: top right;
    }
    .po-ml {
      perspective-origin: left;
    }
    .po-mm {
      perspective-origin: 50% 50%;
    }
    .po-mr {
      perspective-origin: right;
    }
    .po-bl {
      perspective-origin: bottom left;
    }
    .po-bm {
      perspective-origin: bottom;
    }
    .po-br {
      perspective-origin: bottom right;
    }
    .po-200200neg {
      perspective-origin: -200% -200%;
    }
    .po-200200pos {
      perspective-origin: 200% 200%;
    }
    .po-200200 {
      perspective-origin: 200% -200%;
    }
    
    /* Define the container div, the cube div, and a generic face */
    .container {
      width: 100px;
      height: 100px;
      margin: 24px;
      border: none;
    }
    
    .cube {
      width: 100%;
      height: 100%;
      perspective: 300px;
      transform-style: preserve-3d;
    }
    
    .face {
      display: block;
      position: absolute;
      width: 100px;
      height: 100px;
      border: none;
      line-height: 100px;
      font-family: sans-serif;
      font-size: 60px;
      color: white;
      text-align: center;
      backface-visibility: visible;
    }
    
    /* Define each face based on direction */
    .front {
      background: rgb(0 0 0 / 30%);
      transform: translateZ(50px);
    }
    .back {
      background: lime;
      color: black;
      transform: rotateY(180deg) translateZ(50px);
    }
    .right {
      background: rgb(196 0 0 / 70%);
      transform: rotateY(90deg) translateZ(50px);
    }
    .left {
      background: rgb(0 0 196 / 70%);
      transform: rotateY(-90deg) translateZ(50px);
    }
    .top {
      background: rgb(196 196 0 / 70%);
      transform: rotateX(90deg) translateZ(50px);
    }
    .bottom {
      background: rgb(196 0 196 / 70%);
      transform: rotateX(-90deg) translateZ(50px);
    }
    
    /* Make the layout a little nicer */
    section {
      background-color: #eeeeee;
      padding: 10px;
      font-family: sans-serif;
      text-align: left;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
    }
    

##### Result

Once you have done this, you can work on the element in the 3D space.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using#see_also)

----------------------------------------------------------------------------------------------

*   The [CSS `transform` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     and the [CSS `<transform-function>` data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   The individual transforms properties: [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    , [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    , and [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
     (There is no `skew` property)
*   [Using device orientation with 3D Transforms](https://developer.mozilla.org/en-US/docs/Web/API/Device_orientation_events/Using_device_orientation_with_3D_transforms)
    
*   [Intro to CSS 3D transforms](https://3dtransforms.desandro.com/ "External link (opens in new tab)")
     (Blog post by David DeSandro)
*   [CSS Transform Playground](https://css-transform.moro.es/ "External link (opens in new tab)")
     (Online tool to visualize CSS Transform functions)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/transforms/using/index.md?plain=1 "Folder: en-us/web/css/guides/transforms/using (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FTransforms%2FUsing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ftransforms%2Fusing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FTransforms%2FUsing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ftransforms%2Fusing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
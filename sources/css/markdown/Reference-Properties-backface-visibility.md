*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#mdn-search)
    

`backface-visibility` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`backface-visibility`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether the back face of an element is visible when turned towards the user.

An element's back face is a mirror image of its front face. Though invisible in 2D, the back face can become visible when a transformation causes the element to be rotated in 3D space. (This property has no effect on 2D transforms, which have no perspective.)

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#try_it)

-----------------------------------------------------------------------------------------------------------

    backface-visibility: visible;
    

    backface-visibility: hidden;
    

    <section class="default-example" id="default-example">
      <div id="example-element">
        <div class="face front">1</div>
        <div class="face back">2</div>
        <div class="face right">3</div>
        <div class="face bottom">6</div>
      </div>
    </section>
    

    #default-example {
      background: linear-gradient(skyblue, khaki);
    }
    
    #example-element {
      width: 100px;
      height: 100px;
      perspective: 550px;
      perspective-origin: 220% 220%;
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
      background: rgb(0 0 0 / 0.4);
      font-size: 60px;
      color: white;
    }
    
    .front {
      transform: translateZ(50px);
    }
    
    .back {
      background: rgb(230 0 0);
      color: white;
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(0 0 0 / 0.6);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(0 0 0 / 0.6);
      transform: rotateX(-90deg) translateZ(50px);
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    backface-visibility: visible;
    backface-visibility: hidden;
    
    /* Global values */
    backface-visibility: inherit;
    backface-visibility: initial;
    backface-visibility: revert;
    backface-visibility: revert-layer;
    backface-visibility: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#values)

This property is specified as one of the following keywords:

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#visible)

The back face is visible when turned towards the user.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#hidden)

The back face is hidden, effectively making the element invisible when turned away from the user.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

backface-visibility =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#examples)

---------------------------------------------------------------------------------------------------------------

### [Cube with transparent and opaque faces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#cube_with_transparent_and_opaque_faces)

This example shows a cube with transparent faces, and one with opaque faces.

#### HTML

html

    <table>
      <thead>
        <tr>
          <th><code>backface-visibility: visible;</code></th>
          <th><code>backface-visibility: hidden;</code></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div class="container">
              <div class="cube show-bf">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
            <p>
              Since all faces are partially transparent, the back faces (2, 4, 5)
              are visible through the front faces (1, 3, 6).
            </p>
          </td>
          <td>
            <div class="container">
              <div class="cube hide-bf">
                <div class="face front">1</div>
                <div class="face back">2</div>
                <div class="face right">3</div>
                <div class="face left">4</div>
                <div class="face top">5</div>
                <div class="face bottom">6</div>
              </div>
            </div>
            <p>The three back faces (2, 4, 5) are hidden.</p>
          </td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    /* Classes that will show or hide the
       three back faces of the "cube" */
    .show-bf div {
      backface-visibility: visible;
    }
    
    .hide-bf div {
      backface-visibility: hidden;
    }
    
    /* Define the container div, the cube div, and a generic face */
    .container {
      width: 150px;
      height: 150px;
      margin: 75px 0 0 75px;
      border: none;
    }
    
    .cube {
      width: 100%;
      height: 100%;
      perspective: 550px;
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
      margin: 0px;
      padding: 6px;
      font-family: sans-serif;
      text-align: left;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# backface-visibility-property](https://drafts.csswg.org/css-transforms-2/#backface-visibility-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/backface-visibility/index.md?plain=1 "Folder: en-us/web/css/reference/properties/backface-visibility (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackface-visibility&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackface-visibility%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackface-visibility%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackface-visibility%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
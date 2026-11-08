*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#mdn-search)
    

`transform-origin` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transform-origin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the origin for an element's transformations.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#try_it)

--------------------------------------------------------------------------------------------------------

    transform-origin: center;
    

    transform-origin: top left;
    

    transform-origin: 50px 50px;
    

    /* 3D rotation with z-axis origin */
    transform-origin: bottom right 60px;
    

    <section id="default-example">
      <div id="example-container">
        <div id="example-element">Rotate me!</div>
        <img
          alt=""
          id="crosshair"
          src="/shared-assets/images/examples/crosshair.svg"
          width="24px" />
        <div id="static-element"></div>
      </div>
    </section>
    

    @keyframes rotate {
      from {
        transform: rotate(0);
      }
    
      to {
        transform: rotate(30deg);
      }
    }
    
    @keyframes rotate3d {
      from {
        transform: rotate3d(0, 0, 0, 0);
      }
    
      to {
        transform: rotate3d(1, 2, 0, 60deg);
      }
    }
    
    #example-container {
      width: 160px;
      height: 160px;
      position: relative;
    }
    
    #example-element {
      width: 100%;
      height: 100%;
      display: flex;
      position: absolute;
      align-items: center;
      justify-content: center;
      background: #f7ebee;
      color: black;
      font-size: 1.2rem;
      text-transform: uppercase;
    }
    
    #example-element.rotate {
      animation: rotate 1s forwards;
    }
    
    #example-element.rotate3d {
      animation: rotate3d 1s forwards;
    }
    
    #crosshair {
      width: 24px;
      height: 24px;
      opacity: 0;
      position: absolute;
    }
    
    #static-element {
      width: 100%;
      height: 100%;
      position: absolute;
      border: dotted 3px #ff1100;
    }
    

    const crosshair = document.getElementById("crosshair");
    const el = document.getElementById("example-element");
    
    function update() {
      const selected = document.querySelector(".selected");
    
      /* Restart the animation
               https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Tips */
      el.className = "";
      window.requestAnimationFrame(() => {
        window.requestAnimationFrame(() => {
          el.className =
            el.style.transformOrigin.split(" ")[2] === "60px"
              ? "rotate3d"
              : "rotate";
        });
      });
    
      const transformOrigin = getComputedStyle(el).transformOrigin;
      const pos = transformOrigin.split(/\s+/);
      crosshair.style.left = `calc(${pos[0]} - 12px)`;
      crosshair.style.top = `calc(${pos[1]} - 12px)`;
    }
    
    const observer = new MutationObserver(() => {
      update();
    });
    
    observer.observe(el, {
      attributes: true,
      attributeFilter: ["style"],
    });
    
    update();
    crosshair.style.opacity = "1";
    

The transform origin is the point around which a transformation is applied. For example, the transform origin of the [`rotate()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
 function is the center of rotation.

In effect, this property wraps a pair of translations around the element's other transformations. The first translation moves the transform origin to the true origin at (0,0). Then the other transformations are applied, and because the transform origin is at (0,0), those transformations act about the transform origin. Finally, the opposite translation is applied, moving the transform origin back to its original location. Consequently, this definition

css

    transform-origin: -100% 50%;
    transform: rotate(45deg);
    

results in the same transformation as

css

    transform-origin: 0 0;
    transform: translate(-100%, 50%) rotate(45deg) translate(100%, -50%);
    

Reading from right to left, `translate(100%, -50%)` is the translation to bring the transform origin to the true origin, `rotate(45deg)` is the original transformation, and `translate(-100%, 50%)` is the translation to restore the transform origin to its original location.

By default, the origin of a transform is `center`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* One-value syntax */
    transform-origin: 2px;
    transform-origin: bottom;
    
    /* x-offset | y-offset */
    transform-origin: 3cm 2px;
    
    /* x-offset-keyword | y-offset */
    transform-origin: left 2px;
    
    /* x-offset-keyword | y-offset-keyword */
    transform-origin: right top;
    
    /* y-offset-keyword | x-offset-keyword */
    transform-origin: top right;
    
    /* x-offset | y-offset | z-offset */
    transform-origin: 2px 30% 10px;
    
    /* x-offset-keyword | y-offset | z-offset */
    transform-origin: left 5px -3px;
    
    /* x-offset-keyword | y-offset-keyword | z-offset */
    transform-origin: right bottom 2cm;
    
    /* y-offset-keyword | x-offset-keyword | z-offset */
    transform-origin: bottom right 2cm;
    
    /* Global values */
    transform-origin: inherit;
    transform-origin: initial;
    transform-origin: revert;
    transform-origin: revert-layer;
    transform-origin: unset;
    

The `transform-origin` property may be specified using one, two, or three values, where each value represents an offset. Offsets that are not explicitly defined are reset to their corresponding [initial values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
.

If a single [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value is defined, it represents the horizontal offset.

If two or more values are defined and either no value is a keyword, or the only used keyword is `center`, then the first value represents the horizontal offset and the second represents the vertical offset.

*   One-value syntax:
    
    *   The value must be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
        , a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
        , or one of the keywords `left`, `center`, `right`, `top`, and `bottom`.
*   Two-value syntax:
    
    *   One value must be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
        , a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
        , or one of the keywords `left`, `center`, and `right`.
    *   The other value must be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
        , a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
        , or one of the keywords `top`, `center`, and `bottom`.
*   Three-value syntax:
    
    *   The first two values are the same as for the two-value syntax.
    *   The third value must be a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
        . It always represents the Z offset.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#values)

[_x-offset_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#x-offset)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 describing how far from the left edge of the box the origin of the transform is set.

[_offset-keyword_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#offset-keyword)

Is one of the `left`, `right`, `top`, `bottom`, or `center` keyword describing the corresponding offset.

[_y-offset_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#y-offset)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 describing how far from the top edge of the box the origin of the transform is set.

[_x-offset-keyword_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#x-offset-keyword)

Is one of the `left`, `right`, or `center` keyword describing how far from the left edge of the box the origin of the transform is set.

[_y-offset-keyword_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#y-offset-keyword)

Is one of the `top`, `bottom`, or `center` keyword describing how far from the top edge of the box the origin of the transform is set.

[_z-offset_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#z-offset)

Is a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 (and never a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 which would make the statement invalid) describing how far from the user eye the z=0 origin is set.

The keywords are convenience shorthands and match the following [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values:

| Keyword | Value |
| --- | --- |
| `left` | `0%` |
| `center` | `50%` |
| `right` | `100%` |
| `top` | `0%` |
| `bottom` | `100%` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `50% 50% 0` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the size of bounding box |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br> the absolute value, otherwise a percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | simple list of length, percentage, or calc |

**Note:** The initial value of `transform-origin` is `0 0` for all SVG elements except for root `<svg>` elements and `<svg>` elements that are a direct child of a [foreignObject](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject)
, and whose `transform-origin` is `50% 50%`, like other CSS elements. See the [SVG transform-origin](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/transform-origin)
 attribute for more information.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

transform-origin =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 top [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 bottom [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#examples)

------------------------------------------------------------------------------------------------------------

### [A demonstration of various transform values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#a_demonstration_of_various_transform_values)

This example shows the effect of choosing different `transform-origin` values for a variety of transformation functions.

    <div class="container">
      <div class="example">
        <div class="box box1">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: none;
      </pre>
    
      <div class="example">
        <div class="box box2">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: rotate(30deg);
      </pre>
    
      <div class="example">
        <div class="box box3">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: rotate(30deg);
    transform-origin: 0 0;
      </pre>
    
      <div class="example">
        <div class="box box4">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: rotate(30deg);
    transform-origin: 100% 100%;
      </pre>
    
      <div class="example">
        <div class="box box5">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: rotate(30deg);
    transform-origin: -1em -3em;
      </pre>
    
      <div class="example">
        <div class="box box6">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: scale(1.7);
      </pre>
    
      <div class="example">
        <div class="box box7">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: scale(1.7);
    transform-origin: 0 0;
      </pre>
    
      <div class="example">
        <div class="box box8">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: scale(1.7);
    transform-origin: 100% -30%;
      </pre>
    
      <div class="example">
        <div class="box box9">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: skewX(50deg);
    transform-origin: 100% -30%;
      </pre>
    
      <div class="example">
        <div class="box box10">&nbsp;</div>
        <div class="box original">&nbsp;</div>
      </div>
    
      <pre>
    transform: skewY(50deg);
    transform-origin: 100% -30%;
      </pre>
    </div>
    

    .container {
      display: grid;
      grid-template-columns: 200px 100px;
      gap: 20px;
    }
    
    .example {
      position: relative;
      margin: 0 2em 4em 5em;
    }
    
    .box {
      display: inline-block;
      width: 3em;
      height: 3em;
      border: solid 1px;
      background-color: palegreen;
    }
    
    .original {
      position: absolute;
      left: 0;
      opacity: 20%;
    }
    
    .box1 {
      transform: none;
    }
    
    .box2 {
      transform: rotate(30deg);
    }
    
    .box3 {
      transform: rotate(30deg);
      transform-origin: 0 0;
    }
    
    .box4 {
      transform: rotate(30deg);
      transform-origin: 100% 100%;
    }
    
    .box5 {
      transform: rotate(30deg);
      transform-origin: -1em -3em;
    }
    
    .box6 {
      transform: scale(1.7);
    }
    
    .box7 {
      transform: scale(1.7);
      transform-origin: 0 0;
    }
    
    .box8 {
      transform: scale(1.7);
      transform-origin: 100% -30%;
    }
    
    .box9 {
      transform: skewX(50deg);
      transform-origin: 100% -30%;
    }
    
    .box10 {
      transform: skewY(50deg);
      transform-origin: 100% -30%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 1  <br>\# transform-origin-property](https://drafts.csswg.org/css-transforms/#transform-origin-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin#see_also)

------------------------------------------------------------------------------------------------------------

*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    
*   SVG [`transform-origin`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/transform-origin)
     attribute
*   [https://css-tricks.com/almanac/properties/t/transform-origin/](https://css-tricks.com/almanac/properties/t/transform-origin/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transform-origin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transform-origin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-origin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-origin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-origin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-origin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
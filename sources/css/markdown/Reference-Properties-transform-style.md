*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#mdn-search)
    

`transform-style` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transform-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether children of an element are positioned in the 3D space or are flattened in the plane of the element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#try_it)

-------------------------------------------------------------------------------------------------------

    transform-style: flat;
    

    transform-style: preserve-3d;
    

    <section class="default-example" id="default-example">
      <div class="transition-all layer" id="example-element">
        <p>Parent</p>
        <div class="numeral"><code>rotate3d(1, 1, 1, 45deg)</code></div>
      </div>
    </section>
    

    .layer {
      background: #623e3f;
      border-radius: 0.75rem;
      color: white;
      transform: perspective(200px) rotateY(30deg);
    }
    
    .numeral {
      background-color: #ffba08;
      border-radius: 0.2rem;
      color: black;
      margin: 1rem;
      padding: 0.2rem;
      transform: rotate3d(1, 1, 1, 45deg);
    }
    

If flattened, the element's children will not exist on their own in the 3D-space.

As this property is not inherited, it must be set for all non-leaf descendants of the element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    transform-style: flat;
    transform-style: preserve-3d;
    
    /* Global values */
    transform-style: inherit;
    transform-style: initial;
    transform-style: revert;
    transform-style: revert-layer;
    transform-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#values)

This property is specified as one of the following keyword values:

[`flat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#flat)

Indicates that the children of the element are lying in the plane of the element itself.

[`preserve-3d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#preserve-3d)

Indicates that the children of the element should be positioned in the 3D-space.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#description)

-----------------------------------------------------------------------------------------------------------------

The spec lists some [grouping property values](https://drafts.csswg.org/css-transforms-2/#grouping-property-values "External link (opens in new tab)")
, which require the user agent to create a flattened representation of the descendant elements before they can be applied, and therefore force the element to have a [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of `transform-style: flat`, even when `preserve-3d` is specified. These property values include:

*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    : any value other than `visible` or `clip`.
*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    : any value less than `1`.
*   [`filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
    : any value other than `none`.
*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    : any value other than `auto`.
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    : any value other than `none`.
*   [`isolation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation)
    : used value of `isolate`.
*   [`mask-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    : any value other than `none`.
*   [`mask-border-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
    : any value other than `none`.
*   [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    : any value other than `normal`.
*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    : `paint` and any other property/value combination that causes paint containment. This includes any property that affect the used value of the `contain` property, such as `content-visibility: hidden`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `flat` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |
| Creates [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context) | yes |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

transform-style =   
  flat         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  preserve-3d    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#examples)

-----------------------------------------------------------------------------------------------------------

### [Transform style demonstration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#transform_style_demonstration)

In this example we have a 3D cube created using transforms. The parent container of the cube faces has `transform-style: preserve-3d` set on it by default, so it is transformed in the 3D space and you can see it as intended.

We also provide a checkbox allowing you to toggle between this, and `transform-style: flat`. In this alternative state, the cube faces are all flattened onto the plane of their parent, and you might not be able to see them at all, depending on the browser you are using.

#### HTML

html

    <section id="example-element">
      <div class="face front">1</div>
      <div class="face back">2</div>
      <div class="face right">3</div>
      <div class="face left">4</div>
      <div class="face top">5</div>
      <div class="face bottom">6</div>
    </section>
    
    <div class="checkbox">
      <label for="preserve"><code>preserve-3d</code></label>
      <input type="checkbox" id="preserve" checked />
    </div>
    

#### CSS

css

    #example-element {
      margin: 50px;
      width: 100px;
      height: 100px;
      transform-style: preserve-3d;
      transform: rotate3d(1, 1, 1, 30deg);
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
      background: rgb(90 90 90 / 70%);
      transform: translateZ(50px);
    }
    
    .back {
      background: rgb(0 210 0 / 70%);
      transform: rotateY(180deg) translateZ(50px);
    }
    
    .right {
      background: rgb(210 0 0 / 70%);
      transform: rotateY(90deg) translateZ(50px);
    }
    
    .left {
      background: rgb(0 0 210 / 70%);
      transform: rotateY(-90deg) translateZ(50px);
    }
    
    .top {
      background: rgb(210 210 0 / 70%);
      transform: rotateX(90deg) translateZ(50px);
    }
    
    .bottom {
      background: rgb(210 0 210 / 70%);
      transform: rotateX(-90deg) translateZ(50px);
    }
    

#### JavaScript

js

    const cube = document.getElementById("example-element");
    const checkbox = document.getElementById("preserve");
    
    checkbox.addEventListener("change", () => {
      cube.style.transformStyle = checkbox.checked ? "preserve-3d" : "flat";
    });
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transforms Module Level 2  <br>\# transform-style-property](https://drafts.csswg.org/css-transforms-2/#transform-style-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Using CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transforms/Using)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transform-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transform-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransform-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransform-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
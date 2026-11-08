*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#mdn-search)
    

`vector-effect` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`vector-effect`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property suppresses specific [transformation effects](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/transform)
 in SVG, thus permitting effects like a road on a map staying the same width no matter how the map is zoomed, or allowing a diagram key to retain its position and size regardless of other transforms. It can only be used with SVG elements that accept the [`vector-effect`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/vector-effect)
 attribute. When used, the CSS value overrides any values of the element's `vector-effect` attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    vector-effect: none;
    vector-effect: non-scaling-stroke;
    
    /* Global values */
    vector-effect: inherit;
    vector-effect: initial;
    vector-effect: revert;
    vector-effect: revert-layer;
    vector-effect: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#none)

No vector effects are applied to the element, meaning it will be fully affected by transforms as normal.

[`non-scaling-stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#non-scaling-stroke)

The element's drawn stroke width will be physically equal in size to its defined stroke width, even if the element has been scaled up or down in size due to transforms of either itself or its coordinate system. This is the case whether the element is scaled with transforms or by physical resizing of the entire image.

**Note:** The spec defines three other values, `non-scaling-size`, `non-rotation`, and `fixed-position`, but these have no implementations and are considered at-risk.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

vector-effect =   
  none                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  non-scaling-stroke  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  non-scaling-size    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  non-rotation        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed-position        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#examples)

---------------------------------------------------------------------------------------------------------

### [Preventing SVG stroke scaling with CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#preventing_svg_stroke_scaling_with_css)

Here, we start with a 200x100 SVG image that contains two rectangles inside a group. The group is scaled up and rotated. The second of the two rectangles has a class of `thinned`.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
      <g
        transform="scale(2.3) rotate(23)"
        transform-origin="100 50"
        stroke-width="3"
        stroke="orange"
        fill="#ddeeff88">
        <rect x=" 60" y="20" width="30" height="60" />
        <rect x="110" y="20" width="30" height="60" class="thinned" />
      </g>
    </svg>
    

To this SVG image, we apply `width: 500px` to make it larger than its intrinsic size, and set the classed [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 to have non-scaled strokes.

css

    svg {
      width: 500px;
    }
    svg rect.thinned {
      vector-effect: non-scaling-stroke;
    }
    

The result is that the first of the two rectangles has an apparent (visual) stroke width of approximately 17, whereas the second rectangle still has an apparent stroke width of 3 despite having been scaled up in the same way the first rectangle has.

### [Overriding SVG stroke scaling values with CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#overriding_svg_stroke_scaling_values_with_css)

In this case, we start with a similar SVG image to the one used in the previous example. Here, the [`<g>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
 element is rotated as before, but no scaling is applied to it. The `<rect>` elements are given a common origin for their transforms, and have their `vector-effect` SVG attributes set to a value of `none`.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
      <g
        transform="rotate(23)"
        transform-origin="100 50"
        stroke-width="3"
        stroke="orange"
        fill="#ddeeff88">
        <rect
          x=" 60"
          y="20"
          width="30"
          height="60"
          transform-origin="100 50"
          vector-effect="none" />
        <rect
          x="110"
          y="20"
          width="30"
          height="60"
          transform-origin="100 50"
          vector-effect="none"
          class="thinned" />
      </g>
    </svg>
    

As before, the SVG is made larger than its intrinsic size using CSS. This time, scaling is applied to the `<rect>` elements directly, and the second rectangle is set to have its strokes non-scaled.

css

    svg {
      width: 500px;
    }
    svg rect {
      transform: scale(2.3);
    }
    svg rect.thinned {
      vector-effect: non-scaling-stroke;
    }
    

The result is visually identical to that of the previous example. What we can see is that the attribute value of `none` is overridden by the CSS value `non-scaling-stroke`, and that the vector effects are honored even though the scaling was done directly on the `<rect>` rather than on its parent `<g>` element.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# VectorEffectProperty](https://w3c.github.io/svgwg/svg2-draft/coords.html#VectorEffectProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect#see_also)

---------------------------------------------------------------------------------------------------------

*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
     data type
*   SVG [`vector-effect`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/vector-effect)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/vector-effect/index.md?plain=1 "Folder: en-us/web/css/reference/properties/vector-effect (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvector-effect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvector-effect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fvector-effect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fvector-effect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
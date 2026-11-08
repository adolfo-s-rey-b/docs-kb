*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#mdn-search)
    

`clip-rule` CSS property
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`clip-rule`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property determines, when parts of the path overlap other parts, which pixels in a mask's box are inside the clipping shape defined by a [clip path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 and which are outside.

The `clip-rule` property only applies to SVG elements that are contained within a [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 element, overriding the element's [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/clip-rule)
 attribute value if present. The `clip-rule` property basically works as the [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 property, except that it applies to `<clipPath>` definitions. It does not have any effect on CSS [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
s.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#syntax)

-------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    clip-rule: nonzero;
    clip-rule: evenodd;
    
    /* Global values */
    clip-rule: inherit;
    clip-rule: initial;
    clip-rule: revert;
    clip-rule: revert-layer;
    clip-rule: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#values)

This property is specified as one of the following keyword values:

[`nonzero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#nonzero)

For every point in the clipping mask's box, a ray is drawn in a random direction. Every time the ray intersects with any part of the clipping path, a tally is increased by one if the clipping path's part is moving from left to right across the ray, whereas it is decreased by one if the path part is moving right to left across the ray. If the final total of the tally is zero, the point is outside the path's shape. Otherwise, it's inside the path's shape.

[`even-odd`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#even-odd)

For every point in the clipping mask's box, a ray is drawn in a random direction. Every time the ray intersects with any part of the clipping path, a tally is increased by one. If the final total of the tally is even, the point is outside the path's shape; otherwise, it's inside the path's shape. Zero is taken to be even.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#formal_syntax)

---------------------------------------------------------------------------------------------------------------

clip-rule =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#examples)

-----------------------------------------------------------------------------------------------------

### [Value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#value_comparison)

In this example, we will apply different CSS `clip-rule` values to similar SVG [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 elements to demonstrate the difference between `evenodd` and `non-zero`.

#### HTML

The markup has multiple `<svg>` containers, each containing a `<clipPath>` element that defines a star shape, and a `<rect>` element to draw the star inside. The stars are created with overlapping lines. Other than the `id`, the markup of the first two SVG elements is identical. The third SVG includes just the `<path>` element, showing how the lines of the path that created the star overlap.

html

    <svg>
      <clipPath id="star1">
        <path d="M50,0 21,90 98,35 2,35 79,90z" />
      </clipPath>
      <rect clip-path="url(#star1)" width="95" height="95" />
    </svg>
    
    <svg>
      <clipPath id="star2">
        <path d="M50,0 21,90 98,35 2,35 79,90z" />
      </clipPath>
      <rect clip-path="url(#star2)" width="95" height="95" />
    </svg>
    
    <svg id="star3">
      <path d="M50,0 21,90 98,35 2,35 79,90z" />
    </svg>
    

#### CSS

The `clip-rule` for the `<path>` in the first SVG is set to `evenodd`; `nonzero` in the second SVG. For the path-only SVG, we removed the default [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
 and defined both a [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
 color and [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
 to make the overlapping path lines visible:

    body {
      display: flex;
      gap: 20px;
    }
    svg {
      width: 110px;
      height: 110px;
    }
    

css

    #star1 path {
      clip-rule: evenodd;
    }
    
    #star2 path {
      clip-rule: nonzero;
    }
    
    #star3 path {
      fill: none;
      stroke: black;
      stroke-width: 1;
    }
    

#### Results

### [Within basic shape definitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#within_basic_shape_definitions)

This example demonstrates that, while the `clip-rule` does not have any effect on CSS [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
s, it can affect a `<clipPath>` used as the source of a shape.

#### HTML

We include an SVG with two `<clipPath>` elements that define star shapes, which are identical except for their `id` attribute values. We also include two `<div>` elements that will contain our star shapes.

html

    <svg height="0" width="0">
      <defs>
        <clipPath id="star1">
          <path d="M100,0 42,180 196,70 4,70 158,180z" />
        </clipPath>
        <clipPath id="star2">
          <path d="M100,0 42,180 196,70 4,70 158,180z" />
        </clipPath>
      </defs>
    </svg>
    
    <div></div>
    <div></div>
    

#### CSS

We provide the `<div>` elements with a set [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, adding a [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
 for their [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 value:

    body {
      display: flex;
      gap: 20px;
    }
    

css

    div {
      height: 200px;
      width: 200px;
      background-image: conic-gradient(
        at center,
        rebeccapurple,
        green,
        lightblue,
        rebeccapurple
      );
    }
    

We use the [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 property to set the different `<clipPath>` elements as the clipping path for each `<div>`:

css

    div:first-of-type {
      clip-path: url("#star1");
    }
    div:last-of-type {
      clip-path: url("#star2");
    }
    

Finally, we set the different `clip-rule` values for each of the `<clipPath>` element's `<path>`s:

css

    #star1 path {
      clip-rule: evenodd;
    }
    #star2 path {
      clip-rule: nonzero;
    }
    

#### Results

### [Choosing between rules for a path with all clockwise paths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#choosing_between_rules_for_a_path_with_all_clockwise_paths)

In this SVG image, we have two rectangles that are clipped, once with each clipping rule. There are two [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
 elements, so that one can be set to use the non-zero clipping rule and the other uses the even-odd rule. Both paths are drawn in a clockwise direction for both its inner and outer parts.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50">
      <g stroke="#112233" fill="#bbccdd">
        <!-- basic rectangle and clipping path visualization follow -->
        <rect x="10" y="10" width="30" height="30" />
        <path
          d="M 65,5 l 20,20 -20,20 -20,-20 20,-20 m 0,10 l 10,10 -10,10 -10,-10 10,-10 z"
          fill="none"
          stroke-width="0.5" />
        <!-- rectangles to be clipped follow -->
        <rect x="110" y="10" width="30" height="30" clip-path="url(#clipper1)" />
        <rect x="160" y="10" width="30" height="30" clip-path="url(#clipper2)" />
      </g>
      <!-- clipping paths follow -->
      <clipPath id="clipper1" clipPathUnits="objectBoundingBox">
        <path
          d="M 0.5 -0.15 l 0.65 0.65 -0.65,0.65 -0.65,-0.65 0.65,-0.65 m 0,0.33 l 0.33,0.33 -0.33,0.33 -0.33,-0.33 0.33,-0.33 z"
          clip-rule="evenodd" />
      </clipPath>
      <clipPath id="clipper2" clipPathUnits="objectBoundingBox">
        <path
          d="M 0.5 -0.15 l 0.65 0.65 -0.65,0.65 -0.65,-0.65 0.65,-0.65 m 0,0.33 l 0.33,0.33 -0.33,0.33 -0.33,-0.33 0.33,-0.33 z"
          clip-rule="nonzero" />
      </clipPath>
    </svg>
    

To the clipping paths that are applied to the clipped rectangles, the CSS `clip-rule` property is used to set one path to use the `nonzero` rules, and the other to use the `evenodd` rule. These override the values of the `clip-path` attributes in the SVG, which have been intentionally set to the opposite values as the CSS imposes.

css

    #clipper1 {
      clip-rule: nonzero;
    }
    #clipper2 {
      clip-rule: evenodd;
    }
    

Because both the inner and outer parts of the path move in a clockwise (left-to-right) direction, the resulting clip shape will be different between the two clipping rules. For `nonzero`, any ray inside the outer part of the shape will tally to a value above zero, because it will encounter one or more left-to-right path fragments. For `even-odd`, points between the two parts of the path will have an odd-numbered tally, whereas any point either inside the inner path or outside the outer part will have an even-numbered tally.

### [Choosing between rules for a path with different winding paths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#choosing_between_rules_for_a_path_with_different_winding_paths)

This example uses the same SVG as the previous example, with the change that the interior part of the clipping path winds in a counterclockwise direction.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50">
      <g stroke="#112233" fill="#bbccdd">
        <!-- basic rectangle and clipping path visualization follow -->
        <rect x="10" y="10" width="30" height="30" />
        <path
          d="M 65,5 l 20,20 -20,20 -20,-20 20,-20 m 0,10 l 10,10 -10,10 -10,-10 10,-10 z"
          fill="none"
          stroke-width="0.5" />
        <!-- rectangles to be clipped follow -->
        <rect x="110" y="10" width="30" height="30" clip-path="url(#clipper1)" />
        <rect x="160" y="10" width="30" height="30" clip-path="url(#clipper2)" />
      </g>
      <!-- clipping paths follow -->
      <clipPath id="clipper1" clipPathUnits="objectBoundingBox">
        <path
          d="M 0.5 -0.15 l 0.65 0.65 -0.65,0.65 -0.65,-0.65 0.65,-0.65 m 0,0.33 l -0.33,0.33 0.33,0.33 0.33,-0.33 -0.33,-0.33 z" />
      </clipPath>
      <clipPath id="clipper2" clipPathUnits="objectBoundingBox">
        <path
          d="M 0.5 -0.15 l 0.65 0.65 -0.65,0.65 -0.65,-0.65 0.65,-0.65 m 0,0.33 l 0.33,0.33 -0.33,0.33 -0.33,-0.33 0.33,-0.33 z" />
      </clipPath>
    </svg>
    

We apply the same CSS as before.

css

    #clipper1 {
      clip-rule: nonzero;
    }
    #clipper2 {
      clip-rule: evenodd;
    }
    

In this case, because the outer part of the path moves in a clockwise (left-to-right) direction and the interior part of the path moves in a counterclockwise (right-to-left) direction, the resulting clip shape will be the same regardless of which clipping rule is used.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Masking Module Level 1  <br>\# the-clip-rule](https://drafts.csswg.org/css-masking/#the-clip-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule#see_also)

-----------------------------------------------------------------------------------------------------

*   [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [Introduction to CSS clipping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking/Clipping)
    
*   [CSS masking](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Masking)
     module
*   SVG [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/clip-rule)
     attribute
*   SVG [`<clipPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/clipPath)
     element
*   SVG [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/clip-rule/index.md?plain=1 "Folder: en-us/web/css/reference/properties/clip-rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip-rule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip-rule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclip-rule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclip-rule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
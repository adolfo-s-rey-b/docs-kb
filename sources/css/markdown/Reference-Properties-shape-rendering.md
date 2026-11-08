*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#mdn-search)
    

`shape-rendering` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`shape-rendering`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property provides hints to the renderer about what tradeoffs to make when rendering shapes like paths, circles, or rectangles. It only has an effect on the [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)
, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)
, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)
, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)
, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)
, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
 elements. If explicitly declared, the value of the CSS property overrides the any values of the element's [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/shape-rendering)
 attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#syntax)

-------------------------------------------------------------------------------------------------------

css

    shape-rendering: auto;
    shape-rendering: crispEdges;
    shape-rendering: geometricPrecision;
    shape-rendering: optimizeSpeed;
    
    /* Global values */
    shape-rendering: inherit;
    shape-rendering: initial;
    shape-rendering: revert;
    shape-rendering: revert-layer;
    shape-rendering: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#values)

The [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values denote the horizontal center of the circle or ellipse.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#auto)

This value directs the user agents to make tradeoffs in order to balance speed, edge crispness, and geometric precision, with geometric precision given more importance than speed and edge crispness.

[`crispEdges`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#crispedges)

This value directs the user agent to emphasize edge contrast over geometric precision or rendering speed. The final rendering is likely to skip techniques such as anti-aliasing. It may also adjust line positions and line widths in order to align edges with device pixels.

[`geometricPrecision`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#geometricprecision)

This value directs the user agent to emphasize geometric precision over speed or crisp edges. The final rendering may involve techniques such as anti-aliasing.

[`optimizeSpeed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#optimizespeed)

This value directs the user agent to emphasize rendering speed over geometric precision or edge crispness. The final rendering is likely to skip techniques such as anti-aliasing.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in an `svg` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

shape-rendering =   
  auto                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  optimizeSpeed       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  crispEdges          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  geometricPrecision    

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#example)

---------------------------------------------------------------------------------------------------------

To show the different renderings, we create a set of four ellipses of equal size and shape.

html

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120">
      <ellipse cx="50" cy="60" rx="40" ry="60" />
      <ellipse cx="150" cy="60" rx="40" ry="60" />
      <ellipse cx="250" cy="60" rx="40" ry="60" />
      <ellipse cx="350" cy="60" rx="40" ry="60" />
    </svg>
    

We then apply the four values of `shape-rendering`, one per ellipse.

css

    ellipse:nth-of-type(1) {
      shape-rendering: crispEdges;
    }
    ellipse:nth-of-type(2) {
      shape-rendering: geometricPrecision;
    }
    ellipse:nth-of-type(3) {
      shape-rendering: optimizeSpeed;
    }
    ellipse:nth-of-type(4) {
      shape-rendering: auto;
    }
    

The resulting SVG is shown here. The first and third ellipses (counting from left to right) are more likely to show jagged edges, whereas the second should have a smoother appearance. The fourth and last ellipse's appearance will be dictated by the specific tradeoffs made by the user agent you use to view the example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# ShapeRendering](https://w3c.github.io/svgwg/svg2-draft/painting.html#ShapeRendering) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering#see_also)

-----------------------------------------------------------------------------------------------------------

*   SVG [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/shape-rendering)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/shape-rendering/index.md?plain=1 "Folder: en-us/web/css/reference/properties/shape-rendering (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-rendering&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-rendering%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fshape-rendering%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fshape-rendering%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
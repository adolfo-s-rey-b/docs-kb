*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#mdn-search)
    

`marker-start` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`marker-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property points to a marker that will be drawn on the first vertex of the element's path; that is, at its starting vertex. The marker must have been defined using an SVG [`<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)
 element, and can only be referenced with a [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 value. The value of the CSS property overrides any values of the `marker-start` attribute in the SVG.

For many marker-supporting shapes, the first and last vertices are in the same place: for example, the top left corner of a [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)
. In such shapes, if both the first and last markers are defined, two markers will be drawn at that point, though they may not point in the same direction.

**Note:** The `marker-start` property will only have an effect for elements that can use SVG markers. See [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/marker-start)
 for a list.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#syntax)

----------------------------------------------------------------------------------------------------

css

    marker-start: none;
    marker-start: url("markers.svg#arrow");
    
    /* Global values */
    marker-start: inherit;
    marker-start: initial;
    marker-start: revert;
    marker-start: revert-layer;
    marker-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#none)

This means no marker will be drawn at the first vertex of the element's path.

[`<marker-ref>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#marker-ref)

A [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 that refers to a marker defined by an SVG [`<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)
 element, to be drawn at the first vertex of the element's path. If the URL reference is invalid, no marker will be drawn at the path's first vertex.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in an `svg` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)<br> values made absolute |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#formal_syntax)

------------------------------------------------------------------------------------------------------------------

marker-start =   
  none          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <marker-ref>    
  
<marker-ref> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#example)

------------------------------------------------------------------------------------------------------

    html,
    body,
    svg {
      height: 100%;
    }
    

html

    <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker
          id="triangle"
          viewBox="0 0 10 10"
          markerWidth="10"
          markerHeight="10"
          refX="1"
          refY="5"
          markerUnits="strokeWidth"
          orient="auto">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="red" />
        </marker>
      </defs>
      <polyline
        id="test"
        fill="none"
        stroke="black"
        points="20,100 40,60 70,80 100,20" />
    </svg>
    

css

    polyline#test {
      marker-start: url("#triangle");
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# MarkerStartProperty](https://w3c.github.io/svgwg/svg2-draft/painting.html#MarkerStartProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start#see_also)

--------------------------------------------------------------------------------------------------------

*   [`marker-mid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    
*   [`marker-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    
*   [`marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker)
    
*   SVG [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/marker-start)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/marker-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/marker-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmarker-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmarker-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fmarker-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fmarker-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
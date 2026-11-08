*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#mdn-search)
    

`baseline-shift` CSS property
=============================

Baseline 2026

Newly available

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`baseline-shift`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property repositions the dominant-baseline of a text element relative to the dominant-baseline of its parent text content element. The shifted element might be a sub- or superscript. If the property is present, the value overrides the element's [`baseline-shift`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/baseline-shift)
 attribute.

**Note:** The `baseline-shift` property only applies to [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
 and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 elements nested in an [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
. It doesn't apply to other SVG, HTML, or pseudo-elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#syntax)

------------------------------------------------------------------------------------------------------

css

    /* <length-percentage> values */
    baseline-shift: -0.5px;
    baseline-shift: 4%;
    
    /* keyword values */
    baseline-shift: sub;
    baseline-shift: super;
    
    /* Global values */
    baseline-shift: inherit;
    baseline-shift: initial;
    baseline-shift: revert;
    baseline-shift: revert-layer;
    baseline-shift: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#values)

[`sub`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#sub)

The dominant-baseline is shifted to the default position for subscripts.

[`super`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#super)

The dominant-baseline is shifted to the default position for superscripts.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#length-percentage)

Raises (if positive) or lowers (if negative) the dominant-baseline of the text content element by the specified length or percentage, with the percentage being relative to the dominant-baseline of the parent text content element's [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | inline-level boxes and SVG text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the used value of [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height) |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword or a computed value |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

baseline-shift =   
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sub                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  super                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom                 
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#examples)

----------------------------------------------------------------------------------------------------------

### [Using keyword values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#using_keyword_values)

This example demonstrates the basic usage of the `sub` and `super` keyword values of the `baseline-shift` property, as well as how the `baseline-shift` CSS property takes precedence over the `baseline-shift` SVG attribute.

#### HTML

We define an SVG with two SVG [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 elements, each containing a [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 element with the SVG [`baseline-shift`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/baseline-shift)
 attribute set on it.

    <p>Original SVG</p>
    

html

    <svg viewBox="0 0 500 120" xmlns="http://www.w3.org/2000/svg">
      <text x="10" y="50">
        Ceci
        <tspan baseline-shift="super">n'est pas</tspan>
        une pipe super!
      </text>
      <text x="10" y="90">
        Ceci
        <tspan baseline-shift="sub">n'est pas</tspan>
        une pipe sub!
      </text>
    </svg>
    

    <p><code>baseline-shift: sub;</code></p>
    <svg viewBox="0 0 500 120" xmlns="http://www.w3.org/2000/svg">
      <text x="10" y="50">
        Ceci
        <tspan baseline-shift="super">n'est pas</tspan>
        une pipe super!
      </text>
      <text x="10" y="90">
        Ceci
        <tspan baseline-shift="sub">n'est pas</tspan>
        une pipe sub!
      </text>
    </svg>
    <p><code>baseline-shift: super;</code></p>
    <svg viewBox="0 0 500 120" xmlns="http://www.w3.org/2000/svg">
      <text x="10" y="50">
        Ceci
        <tspan baseline-shift="super">n'est pas</tspan>
        une pipe super!
      </text>
      <text x="10" y="90">
        Ceci
        <tspan baseline-shift="sub">n'est pas</tspan>
        une pipe sub!
      </text>
    </svg>
    

The SVG is repeated three times; we've only shown one copy for the sake of brevity.

#### CSS

We make the text in all three SVG images large and cursive, adding some color to differentiate the content within the `<tspan>` elements.

We set the `baseline-shift` property value to `sub` on the second SVG's `<tspan>` element and `super` on the third SVG's `<tspan>` element. The first SVG has no additional CSS applied to it.

css

    text {
      font-family: cursive;
      font-size: 2rem;
    }
    [baseline-shift="sub"] {
      fill: deeppink;
    }
    [baseline-shift="super"] {
      fill: rebeccapurple;
    }
    
    svg:nth-of-type(2) tspan {
      baseline-shift: sub;
    }
    svg:nth-of-type(3) tspan {
      baseline-shift: super;
    }
    

    svg {
      border: 1px solid;
      width: 15em;
      margin-bottom: 10px;
    }
    @supports not (baseline-shift: sub) {
      body::before {
        content: "Your browser doesn't support the `baseline-shift` property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Results

The SVG `baseline-shift` attribute values are used in the first SVG. In the second and third SVGs, the CSS `baseline-shift` values override the attribute values.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# baseline-shift-property](https://drafts.csswg.org/css-inline/#baseline-shift-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# BaselineShiftProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#BaselineShiftProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift#see_also)

----------------------------------------------------------------------------------------------------------

*   SVG [`baseline-shift`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/baseline-shift)
     attribute
*   Presentation properties: `baseline-shift`, [`clip-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    , [`color-interpolation-filters`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    , [`fill-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    , [`fill-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    , [`fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    , [`marker-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    , [`marker-mid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    , [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start)
    , [`shape-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
    , [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
    , [`stop-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity)
    , [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    , [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    , [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    , [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    , [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    , [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    , [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    , [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    , [`text-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor)
    , and [`vector-effect`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/baseline-shift/index.md?plain=1 "Folder: en-us/web/css/reference/properties/baseline-shift (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbaseline-shift&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbaseline-shift%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbaseline-shift%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbaseline-shift%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
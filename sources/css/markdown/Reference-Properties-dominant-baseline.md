*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#mdn-search)
    

`dominant-baseline` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`dominant-baseline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the specific [baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Typography)
 used to align the box's text and inline-level contents. It also indicates the default alignment baseline of any boxes participating in baseline alignment in the box's alignment context. If present, it overrides the shape's [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/dominant-baseline)
 attribute.

Baselines are selected from the font baseline table. If there is no baseline table in the nominal font, or if the baseline table lacks an entry for the desired baseline, then the browser may use heuristics to determine the position of the desired baseline.

The `dominant-baseline` property is used to determine or re-determine a _scaled-baseline-table_. A scaled-baseline-table is a compound value with three components:

1.  a baseline-identifier for the dominant-baseline,
2.  a baseline-table, and
3.  a baseline-table font-size.

Some values of `dominant-baseline` re-determine all three values. Others only re-establish the baseline-table font-size. When the initial value, `auto`, would give an undesired result, this property can be used to explicitly set the desired scaled-baseline-table.

**Note:** The `dominant-baseline` property only has an effect on the [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 SVG elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Initial value */
    dominant-baseline: auto;
    
    /* Keyword values */
    dominant-baseline: alphabetic;
    dominant-baseline: central;
    dominant-baseline: hanging;
    dominant-baseline: ideographic;
    dominant-baseline: mathematical;
    dominant-baseline: middle;
    dominant-baseline: text-bottom;
    dominant-baseline: text-top;
    
    /* Global values */
    dominant-baseline: inherit;
    dominant-baseline: initial;
    dominant-baseline: revert;
    dominant-baseline: revert-layer;
    dominant-baseline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#auto)

If this property is applied to a [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 element, then the computed value depends on the value of the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/writing-mode)
 attribute.

If the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/writing-mode)
 is horizontal, then the value of the dominant-baseline component is `alphabetic`. Otherwise, if the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/writing-mode)
 is vertical, then the value of the dominant-baseline component is `central`.

If this property is applied to a [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
, or [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
 element, then the dominant-baseline and the baseline-table components remain the same as those of the parent text content element.

If the computed [`baseline-shift`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/baseline-shift)
 value actually shifts the baseline, then the baseline-table font-size component is set to the value of the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 attribute on the element on which the `dominant-baseline` attribute occurs, otherwise the baseline-table font-size remains the same as that of the element.

If there is no parent text content element, the scaled-baseline-table value is constructed as for [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
 elements.

[`alphabetic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#alphabetic)

The baseline-identifier for the dominant-baseline is set to be `alphabetic`, the derived baseline-table is constructed using the `alphabetic` baseline-table in the font, and the baseline-table font-size is changed to the value of the element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute or the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, if set.

[`central`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#central)

The baseline-identifier for the dominant-baseline is set to be `central`. The derived baseline-table is constructed from the defined baselines in the font's baseline-table. That font baseline-table is chosen using the following priority order of baseline-table names: `ideographic`, `alphabetic`, `hanging`, `mathematical`. The baseline-table font-size is changed to the value of the element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute or the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, if set.

[`hanging`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#hanging)

The baseline-identifier for the dominant-baseline is set to be `hanging`, the derived baseline-table is constructed using the `hanging` baseline-table in the font, and the baseline-table font-size is changed to the value of the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute of [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 CSS property on this element.

[`ideographic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#ideographic)

The baseline-identifier for the dominant-baseline is set to be `ideographic`, the derived baseline-table is constructed using the `ideographic` baseline-table in the font, and the baseline-table font-size is changed to the value of the value of the element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute or the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, if set.

[`mathematical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#mathematical)

The baseline-identifier for the dominant-baseline is set to be `mathematical`, the derived baseline-table is constructed using the `mathematical` baseline-table in the font, and the baseline-table font-size is changed to the value of the value of the element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute or the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, if set.

[`middle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#middle)

The baseline-identifier for the dominant-baseline is set to be `middle`. The derived baseline-table is constructed from the defined baselines in a baseline-table in the font. That font baseline-table is chosen using the following priority order of baseline-table names: `ideographic`, `alphabetic`, `hanging`, `mathematical`. The baseline-table font-size is changed to the value of the element's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-size)
 SVG attribute or the CSS [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, if set.

[`text-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#text-bottom)

The _line-under_ edge is used as the baseline, which is usually the bottom edge of the font's em box.

[`text-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#text-top)

The _line-over_ edge is used as the baseline, which is usually the top edge of the font's em box.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block-containers, flex containers, grid containers, inline boxes, table rows, and SVG text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

dominant-baseline =   
  auto               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <baseline-metric>    
  
<baseline-metric> =   
  text-bottom   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ideographic   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  middle        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  central       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  mathematical  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hanging       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  text-top        

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#example)

-----------------------------------------------------------------------------------------------------------

html

    <svg viewBox="0 0 450 160" width="700" height="200">
      <text x="50" y="20">alphabetic</text>
      <text x="50" y="60">central</text>
      <text x="50" y="100">hanging</text>
      <text x="50" y="140">ideographic</text>
      <text x="250" y="20">mathematical</text>
      <text x="250" y="60">middle</text>
      <text x="250" y="100">text-bottom</text>
      <text x="250" y="140">text-top</text>
      <path
        d="M   0,20 l 400,0
           m -400,40 l 400,0
           m -400,40 l 400,0
           m -400,40 l 400,0"
        stroke="grey" />
      <text x="0" y="20" fill="red">auto</text>
      <text x="0" y="60" fill="red">auto</text>
      <text x="0" y="100" fill="red">auto</text>
      <text x="0" y="140" fill="red">auto</text>
    </svg>
    

css

    text {
      font-size: 20px;
    }
    text:nth-of-type(1) {
      dominant-baseline: alphabetic;
    }
    text:nth-of-type(2) {
      dominant-baseline: central;
    }
    text:nth-of-type(3) {
      dominant-baseline: hanging;
    }
    text:nth-of-type(4) {
      dominant-baseline: ideographic;
    }
    text:nth-of-type(5) {
      dominant-baseline: mathematical;
    }
    text:nth-of-type(6) {
      dominant-baseline: middle;
    }
    text:nth-of-type(7) {
      dominant-baseline: text-bottom;
    }
    text:nth-of-type(8) {
      dominant-baseline: text-top;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# dominant-baseline-property](https://drafts.csswg.org/css-inline/#dominant-baseline-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# DominantBaselineProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#DominantBaselineProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
    
*   [`text-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor)
    
*   [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    
*   SVG [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/dominant-baseline)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/dominant-baseline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/dominant-baseline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdominant-baseline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdominant-baseline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdominant-baseline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdominant-baseline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
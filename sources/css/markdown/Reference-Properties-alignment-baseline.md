*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#mdn-search)
    

`alignment-baseline` CSS property
=================================

Baseline 2026

Newly available

\*

Since March 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/15)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`alignment-baseline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the specific [baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Typography)
 used to align the box's text and inline-level contents. **Baseline alignment** is the relationship among the baselines of multiple alignment subjects within an alignment context. When performing baseline alignment, the `alignment-baseline` property value specifies which baseline of the box is aligned to the corresponding baseline of its alignment context.

**Note:** The `alignment-baseline` property only has an effect on inline-level boxes, flex items, grid items, table cells, and the [`<text>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/text)
, [`<textPath>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/textPath)
, and [`<tspan>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/tspan)
 SVG elements. If present, it overrides the shape's [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/alignment-baseline)
 attribute.

In an inline formatting context, inline-level box fragments and glyphs share an alignment context established by their parent inline box fragment along its inline axis. In SVG text layout, these values instead specify the baseline that is aligned to the SVG current text position.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Initial value */
    alignment-baseline: baseline;
    
    /* Keyword values */
    alignment-baseline: alphabetic;
    alignment-baseline: central;
    alignment-baseline: ideographic;
    alignment-baseline: mathematical;
    alignment-baseline: middle;
    alignment-baseline: text-bottom;
    alignment-baseline: text-top;
    
    /* Mapped values */
    alignment-baseline: text-before-edge; /* text-top */
    alignment-baseline: text-after-edge; /* text-bottom */
    
    /* Deprecated values  */
    alignment-baseline: auto;
    alignment-baseline: before-edge;
    alignment-baseline: after-edge;
    alignment-baseline: hanging;
    
    /* Global values */
    alignment-baseline: inherit;
    alignment-baseline: initial;
    alignment-baseline: revert;
    alignment-baseline: revert-layer;
    alignment-baseline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#values)

This property is specified as one of the following keyword values:

[`baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#baseline)

Use the [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
 value of the parent.

[`alphabetic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#alphabetic)

Used in writing Latin, Cyrillic, Greek, and many other scripts; matches the box's alphabetic baseline to that of its parent, corresponding to the bottom of most, but not all characters.

[`central`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#central)

Matches the box's central baseline to the central baseline of its parent, corresponding to the ideographic central baseline, halfway between the ideographic-under and ideographic-over baselines.

[`ideographic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#ideographic)

Matches the box's ideographic character face under-side baseline to that of its parent, with the derived baseline-table constructed using the ideographic baseline-table in the font.

[`mathematical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#mathematical)

Matches the box's mathematical baseline to that of its parent, corresponding to the center baseline around which mathematical characters are designed.

[`middle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#middle)

Aligns the vertical midpoint of the box with the baseline of the parent box plus half the x-height of the parent. Uses the x-middle baselines; except under [`text-orientation: upright;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
 (where the alphabetic and x-height baselines are essentially meaningless), in which case it uses the `central` baseline instead.

[`text-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#text-bottom)

Matches the bottom of the box to the top of the parent's content area, using the line-under edge of an inline's content box.

[`text-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#text-top)

Matches the top of the box to the top of the parent's content area; the line-over edge of an inline's content box.

**Note:** In SVG2, the `auto`, `before-edge`, and `after-edge` were deprecated and `text-before-edge` is an alias for `text-top`, and `text-after-edge` is an alias for `text-bottom`. These keywords should not be used as part of the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 shorthand property. Browsers support `auto` as a synonym for `baseline` and `hanging`, wherein the alignment-point of the object being aligned is aligned with the "hanging" baseline of the parent text content element, but neither is part of the specification.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `baseline` |
| Applies to | inline-level boxes, flex items, grid items, table cells, and SVG text content elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

alignment-baseline =   
  baseline           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
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

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#example)

------------------------------------------------------------------------------------------------------------

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
      <text x="0" y="20" fill="red">baseline</text>
      <text x="0" y="60" fill="red">baseline</text>
      <text x="0" y="100" fill="red">baseline</text>
      <text x="0" y="140" fill="red">baseline</text>
    </svg>
    

css

    text {
      font-size: 20px;
      alignment-baseline: baseline;
    }
    text:nth-of-type(1) {
      alignment-baseline: alphabetic;
    }
    text:nth-of-type(2) {
      alignment-baseline: central;
    }
    text:nth-of-type(3) {
      alignment-baseline: hanging;
    }
    text:nth-of-type(4) {
      alignment-baseline: ideographic;
    }
    text:nth-of-type(5) {
      alignment-baseline: mathematical;
    }
    text:nth-of-type(6) {
      alignment-baseline: middle;
    }
    text:nth-of-type(7) {
      alignment-baseline: text-bottom;
    }
    text:nth-of-type(8) {
      alignment-baseline: text-top;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# alignment-baseline-property](https://drafts.csswg.org/css-inline/#alignment-baseline-property) |
| [Scalable Vector Graphics (SVG) 2  <br>\# AlignmentBaselineProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#AlignmentBaselineProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`dominant-baseline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
    
*   SVG [`alignment-baseline`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/alignment-baseline)
     attribute
*   [CSS inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
     module
*   [CSS box alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/alignment-baseline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/alignment-baseline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falignment-baseline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falignment-baseline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Falignment-baseline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Falignment-baseline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
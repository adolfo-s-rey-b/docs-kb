*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#mdn-search)
    

`paint-order` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`paint-order`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you control the order in which the fill and stroke (and painting markers) of text content and shapes are drawn.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Normal */
    paint-order: normal;
    
    /* Single values */
    paint-order: stroke; /* draw the stroke first, then fill and markers */
    paint-order: markers; /* draw the markers first, then fill and stroke */
    
    /* Multiple values */
    paint-order: stroke fill; /* draw the stroke first, then the fill, then the markers */
    paint-order: markers stroke fill; /* draw markers, then stroke, then fill */
    
    /* Global values */
    paint-order: inherit;
    paint-order: initial;
    paint-order: revert;
    paint-order: revert-layer;
    paint-order: unset;
    

If no value is specified, the default paint order is `fill`, `stroke`, `markers`.

When one value is specified, that one is painted first, followed by the other two in their default order relative to one another. When two values are specified, they will be painted in the order they are specified in, followed by the unspecified one.

**Note:** In the case of this property, markers are only appropriate when drawing SVG shapes involving the use of the `marker-*` properties (e.g., [`marker-start`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/marker-start)
) and [`<marker>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/marker)
 element. They do not apply to HTML text, so in that case, you can only determine the order of `stroke` and `fill`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#normal)

Paint the different items in normal paint order.

[`stroke`, `fill`, `markers`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#stroke)

Specify some or all of these values in the order you want them to be painted in.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | text elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

paint-order =   
  normal                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 fill [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 stroke [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 markers [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#examples)

-------------------------------------------------------------------------------------------------------

### [Reversing the paint order of stroke and fill](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#reversing_the_paint_order_of_stroke_and_fill)

#### SVG

html

    <svg xmlns="http://www.w3.org/2000/svg" width="400" height="200">
      <text x="10" y="75">stroke in front</text>
      <text x="10" y="150" class="stroke-behind">stroke behind</text>
    </svg>
    

#### CSS

css

    text {
      font-family: sans-serif;
      font-size: 50px;
      font-weight: bold;
      fill: black;
      stroke: red;
      stroke-width: 4px;
    }
    
    .stroke-behind {
      paint-order: stroke fill;
    }
    

#### Result

### [Reversing the paint order of stroke and fill using HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#reversing_the_paint_order_of_stroke_and_fill_using_html)

To control the fill and stroke order in HTML, you can use the [`-webkit-text-stroke-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
 and [`-webkit-text-stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width)
 CSS properties.

#### HTML

html

    <div>stroke in front</div>
    <div class="stroke-behind">stroke behind</div>
    

#### CSS

css

    div {
      font-family: sans-serif;
      font-size: 50px;
      font-weight: bold;
      fill: black;
      padding-top: 10px;
      padding-bottom: 10px;
      -webkit-text-stroke-color: red;
      -webkit-text-stroke-width: 4px;
    }
    
    .stroke-behind {
      paint-order: stroke fill;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# PaintOrderProperty](https://w3c.github.io/svgwg/svg2-draft/painting.html#PaintOrderProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order#see_also)

-------------------------------------------------------------------------------------------------------

*   [CSS Tricks: paint-order](https://css-tricks.com/almanac/properties/p/paint-order/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/paint-order/index.md?plain=1 "Folder: en-us/web/css/reference/properties/paint-order (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpaint-order&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpaint-order%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fpaint-order%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fpaint-order%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
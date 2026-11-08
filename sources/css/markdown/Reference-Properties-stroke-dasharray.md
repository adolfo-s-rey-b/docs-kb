*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#mdn-search)
    

`stroke-dasharray` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`stroke-dasharray`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines a pattern of dashes and gaps used in the painting of the [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 shape's stroke. If present, it overrides the element's [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dasharray)
 attribute.

This property applies to any SVG shape or text-content element (see [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dasharray)
 for a full list), but as an inherited property, it may be applied to elements such as [`<g>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/g)
 and still have the intended effect on descendant elements' strokes.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    stroke-dasharray: none;
    
    /* Numeric, length, and percentage values */
    stroke-dasharray: 2px, 5px;
    stroke-dasharray: 20%, 50%;
    stroke-dasharray: 2, 5;
    
    /* The following two rules are equivalent */
    stroke-dasharray: 2, 5, 3;
    stroke-dasharray: 2, 5, 3, 2, 5, 3;
    
    /* Global values */
    stroke-dasharray: inherit;
    stroke-dasharray: initial;
    stroke-dasharray: revert;
    stroke-dasharray: revert-layer;
    stroke-dasharray: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#values)

The value is a list of comma and/or white space separated `<number>`, `<length>`, and / or `<percentage>` values that specify the lengths of alternating dashes and gaps, or the keyword `none`. If an odd number of values are given, the entire value will be repeated in order to set an even number of values.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#none)

The stroke will be drawn without any dashes. The default value.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

A number of SVG units, the size of which are defined by the current unit space. Negative values are invalid.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

Pixel units are handled the same as SVG units (see `<number>`, above) and font-based lengths such as `em` are calculated with respect to the element's SVG value for the text size; the effects of other length units may depend on the browser. Negative values are invalid.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Percentages refer to the normalized diagonal of the current SVG viewport, which is calculated as <width>2+<height>22. Negative values are invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | [`<circle>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/circle)<br>, [`<ellipse>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/ellipse)<br>, [`<line>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/line)<br>, [`<path>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)<br>, [`<polygon>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polygon)<br>, [`<polyline>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/polyline)<br>, and [`<rect>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/rect)<br> elements in an `svg` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | refer to the normalized diagonal measure of the current SVG viewport's applied [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)<br>, or of the viewport itself if no `viewBox` is specified |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A comma separated list of absolute lengths or percentages, numbers converted to absolute lengths first, or keyword specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

stroke-dasharray =   
  none                                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#examples)

------------------------------------------------------------------------------------------------------------

### [Basic dash array](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#basic_dash_array)

This example demonstrates basic usage of the `stroke-dasharray` property using space-separated `<number>` values.

#### HTML

First, we set up a basic SVG rectangle shape. To this rectangle, a red stroke with a width of `2` is applied.

html

    <svg viewBox="0 0 100 50" width="500" height="250">
      <rect
        x="10"
        y="10"
        width="80"
        height="30"
        fill="none"
        stroke="red"
        stroke-width="2" />
    </svg>
    

#### CSS

We define a dash pattern for the stroke: ten units of dash, followed by five units of space. This means the gaps between dashes will be half the length as the dashes themselves.

css

    rect {
      stroke-dasharray: 10 5;
    }
    

#### Results

Where the stroke turns a corner, the pattern is carried along, as it were. At the top left corner, where the start and end of the stroke meet, the ten-unit-long starting dash appears to join with the part of the dash pattern seen at the end of the path, creating what looks like a longer-than-ten-units line bending around the corner.

### [Dash array repetition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#dash_array_repetition)

This example includes an odd-number of comma-separated `<number>` values to demonstrates how the value is repeated if an odd number of values is given in order to set an even number of values.

#### HTML

In this case, we define two rectangles.

html

    <svg viewBox="0 0 100 100" width="500" height="500">
      <rect
        x="10"
        y="10"
        width="80"
        height="30"
        fill="none"
        stroke="red"
        stroke-width="2" />
      <rect
        x="10"
        y="60"
        width="80"
        height="30"
        fill="none"
        stroke="red"
        stroke-width="2" />
    </svg>
    

#### CSS

To the first rectangle, we define a dasharray of `5, 5, 1`, which calls for five units of dash, five of gap, and one unit of dash. However, because this is an odd number of numbers, the entire set of numbers is repeated, thus creating a value identical to that applied to the second rectangle.

css

    rect:nth-of-type(1) {
      stroke-dasharray: 5, 5, 1;
    }
    rect:nth-of-type(2) {
      stroke-dasharray: 5, 5, 1, 5, 5, 1;
    }
    

#### Result

The reason an even count of numbers is required is so that every dash array begins with a dash and ends with a gap. Thus, the pattern defined is a five-unit dash, a five-unit gap, a one-unit dash, a five-unit gap, a five-unit dash, and a one-unit gap. In the resulting stroke, every instance of a one-unit gap between two five-unit dashes indicates a place where the dash array starts over.

### [Percentage and pixel values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#percentage_and_pixel_values)

This example demonstrates the use of `<percentage>` and `<length>` values within the `stroke-dasharray` property value.

#### HTML

As in the previous example, we define two rectangles.

html

    <svg viewBox="0 0 100 100" width="500" height="500">
      <rect
        x="10"
        y="10"
        width="80"
        height="30"
        fill="none"
        stroke="red"
        stroke-width="2" />
      <rect
        x="10"
        y="60"
        width="80"
        height="30"
        fill="none"
        stroke="red"
        stroke-width="2" />
    </svg>
    

#### CSS

This time, rather than collections of bare numbers, we use pixel units and percentages.

css

    rect:nth-of-type(1) {
      stroke-dasharray: 5px, 5px, 1px;
    }
    rect:nth-of-type(2) {
      stroke-dasharray: 5%, 5%, 1%;
    }
    

#### Results

The results are essentially indistinguishable from the results in the previous example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fill and Stroke Module Level 3  <br>\# stroke-dasharray](https://drafts.csswg.org/fill-stroke-3/#stroke-dasharray) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray#see_also)

------------------------------------------------------------------------------------------------------------

*   [`stroke-dashoffset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    
*   [`stroke-linecap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    
*   [`stroke-linejoin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    
*   [`stroke-miterlimit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    
*   [`stroke-opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    
*   [`stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    
*   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   SVG [`stroke-dasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke-dasharray)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/stroke-dasharray/index.md?plain=1 "Folder: en-us/web/css/reference/properties/stroke-dasharray (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-dasharray&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-dasharray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fstroke-dasharray%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fstroke-dasharray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
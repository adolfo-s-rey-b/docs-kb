*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#mdn-search)
    

`row-gap` CSS property
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`row-gap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the size of the gap ([gutter](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
) between an element's rows in multi-column, flexible box, and grid layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#try_it)

-----------------------------------------------------------------------------------------------

    row-gap: 0;
    

    row-gap: 1ch;
    

    row-gap: 1em;
    

    row-gap: 20px;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element">
          <div>One</div>
          <div>Two</div>
          <div>Three</div>
          <div>Four</div>
          <div>Five</div>
        </div>
      </div>
    </section>
    

    #example-element {
      border: 1px solid #c5c5c5;
      display: grid;
      grid-template-columns: 1fr 1fr;
      width: 200px;
    }
    
    #example-element > div {
      background-color: rgb(0 0 255 / 0.2);
      border: 3px solid blue;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Keyword value */
    row-gap: normal;
    
    /* <length-percentage> value */
    row-gap: 20px;
    row-gap: 1em;
    row-gap: 3vmin;
    row-gap: 0.5cm;
    row-gap: 10%;
    row-gap: calc(10% - 6px);
    
    /* <line-width> values */
    row-gap: thin;
    row-gap: medium;
    row-gap: thick;
    
    /* Global values */
    row-gap: inherit;
    row-gap: initial;
    row-gap: revert;
    row-gap: revert-layer;
    row-gap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#normal)

For multi-column layout, resolves to `1em`; otherwise `0`. This is the default value.

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)

Sets the size of the gap using the keywords `thin`, `medium`, or `thick`, or a positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Sets a non-negative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value. Percentages are relative to the block-size of the content box or `0`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#description)

---------------------------------------------------------------------------------------------------------

The `row-gap` property sets the size of the gap between an element's rows. This gap may contain a visible separator as a gap decoration. If there is a rule between rows, it will appear in the middle of the gap, but has no impact on the gap size. These decorative lines can be added to the otherwise "empty space" by using the [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
 property or [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand.

Defined in [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
, the property can be used in multi-column, flexible box, and grid layouts. The `row-gap`, along with the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 property, can also be set using the [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand property, in that order. The `row-gap` property replaced the `grid-row-gap` property, which was limited to [CSS grid layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
. Now `grid-row-gap` is an alias for `row-gap`.

The property specifies a fixed-length gutter between items in a container, separating boxes in the container's block axis. Negative values are invalid. The default value `normal` resolves to `1em` on multi-column containers, and `0` everywhere else. See [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
 for more information about gaps by layout type.

Percentages resolve against the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)
 size of the container element's block axis when this size is definite, against `0` otherwise, except in grid layout, for which cyclic percentage sizes resolve against zero for determining [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 contributions but resolve against the element's content box when laying out the contents. See [Specifying gap values as percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#specifying_gap_values_as_percentages)
 for more information.

In grid layouts, the effect of the gap is as though the grid lines between grid rows acquired the thickness of the property's value: the grid track between two rows is the space between the gutters that represent them. When it comes to track sizing, each gutter is treated as an extra, empty, fixed-size track of the specified size, which is spanned by any grid items that spans across more than one row. While treated as empty for sizing, the gap created may contain a [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | multi-column elements, flex containers, grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to corresponding dimension of the content area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, with <length>s made absolute, and normal computing to zero except on multi-column elements |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#formal_syntax)

-------------------------------------------------------------------------------------------------------------

row-gap =   
  normal                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage \[0,∞\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <line-width>                 
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#examples)

---------------------------------------------------------------------------------------------------

### [Flex layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#flex_layout)

This example demonstrates using the `row-gap` property to create horizontal space between adjacent rows of flex items. It also demonstrates how the `row-gap` size is not affected by the size of the row rule.

#### HTML

We include six items in a container element:

html

    <div id="flexbox">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

#### CSS

We set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `flex`, set the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 to `row wrap` to create a flex container with rows of flex items that flow onto new lines as needed, and limit the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 to `300px`. We also add a [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
, which will draw a 30px-wide, dashed, magenta line in the middle of the gap.

The `row-gap` value is set as `20px` on the flex container to create a `20px` gap between the adjacent flex rows.

We also set a background color on the flex items, with most being semi-opaque, to demonstrate how the rule is visible under the flex items when it is wider than the gap.

css

    #flexbox {
      display: flex;
      flex-flow: row wrap;
      width: 300px;
      row-rule: 30px dashed magenta;
    
      row-gap: 20px;
    }
    
    #flexbox > div {
      border: 1px solid green;
      background-color: #00ff0033;
      flex: 1 1 100px;
      height: 50px;
    }
    #flexbox > div:nth-of-type(3n-1) {
      background-color: lime;
    }
    

#### Result

To set vertical space between flex items, specify a non-zero value for the [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
 property, optionally setting both `row-gap` and `column-gap` by using the `gap` shorthand.

### [Grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#grid_layout)

This example demonstrates using the `row-gap` property with a `<percentage>` value in a grid layout.

#### HTML

We include five items in a container element:

html

    <div id="grid">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

#### CSS

We set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `grid`, the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 to `240px`, the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 to `350px` and [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
 to `repeat(3, 1fr)` to create a 350px-wide grid container with three columns and as many rows as needed. Each row is `100px` tall, as defined by the [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
 property.

The `row-gap` is set to `5%`. The container height is `240px`. The `5%` value creates a row gap that is `12px` tall, leaving `216px` for three rows of grid items, meaning each row is `72px` tall.

css

    #grid {
      display: grid;
      height: 240px;
      width: 350px;
      grid-template-rows: repeat(3, 1fr);
      grid-template-columns: 150px 1fr;
    
      row-gap: 5%;
    }
    

    body {
      padding: 1em;
    }
    
    #grid > div {
      outline: 1px solid green;
      background-color: lime;
    }
    @layer no-support {
      @supports not (row-gap: 5%) {
        body::before {
          content: "Your browser doesn't support percent values";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# column-row-gap](https://drafts.csswg.org/css-gaps-1/#column-row-gap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap#see_also)

---------------------------------------------------------------------------------------------------

*   [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [Basic concepts of grid layout: gutters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#gutters)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/row-gap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/row-gap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-gap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-gap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Frow-gap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Frow-gap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04dfe418f2942ae739d41592c22fafa3679fc03c%0A*+Document+last+modified%3A+2026-10-05T17%3A37%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
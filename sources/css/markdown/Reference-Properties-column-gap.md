*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#mdn-search)
    

`column-gap` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-gap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the size of the gap ([gutter](https://developer.mozilla.org/en-US/docs/Glossary/Gutters)
) between an element's columns in multi-column, flexible box, and grid layouts.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#try_it)

--------------------------------------------------------------------------------------------------

    column-gap: 0;
    

    column-gap: 10%;
    

    column-gap: 1em;
    

    column-gap: 20px;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    column-gap: normal;
    
    /* <length-percentage> value */
    column-gap: 3px;
    column-gap: 2.5em;
    column-gap: 3%;
    column-gap: calc(3% - 6px);
    
    /* <line-width> keyword value */
    column-gap: thin;
    column-gap: medium;
    column-gap: thick;
    
    /* Global values */
    column-gap: inherit;
    column-gap: initial;
    column-gap: revert;
    column-gap: revert-layer;
    column-gap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#values)

This property is specified as a single value from the following list:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#normal)

For multi-column layout, sets the gap to `1em`; otherwise `0`. This is the default value.

[`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)

Sets the size of the gap using the keywords `thin`, `medium`, or `thick`, or a positive [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Sets a non-negative [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value. Percentages are relative to the inline-size of the content box.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#description)

------------------------------------------------------------------------------------------------------------

The `column-gap` property sets the size of the gap between an element's columns. The property specifies a fixed-length gutter between items in a container, separating boxes in the container's inline axis. Negative values are invalid. Column gaps in multi-col containers are `1em` wide by default, while no gap is added between grid columns or flex items or rows. See [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
 for more information about gaps by layout type.

Percentages are calculated against the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#content_area)
 size of the container element's inline axis when this size is definite, against `0` otherwise, except in grid layout, for which cyclic percentage sizes resolve against zero for determining [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
 contributions but resolve against the element's content box when laying out the contents. See [Specifying gap values as percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps#specifying_gap_values_as_percentages)
 for more information.

The column gap may contain a visible separator as a [gap decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
. To draw a rule between the columns, use the [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 or the [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
 shorthand. The rule appears in the middle of the gap but has no effect on the size of the gap between the columns.

The `column-gap` property, along with the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 property, can also be set by using the [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 shorthand, which sets both `row-gap` and `column-gap` in one declaration, in that order.

The `column-gap` property replaced the `grid-column-gap` property, which was initially defined in [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 for creating gaps between grid columns. `grid-column-gap` is now an alias for `column-gap`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | multi-column elements, flex containers, grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to corresponding dimension of the content area |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, with <length>s made absolute, and normal computing to zero except on multi-column elements |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#formal_syntax)

----------------------------------------------------------------------------------------------------------------

column-gap =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#examples)

------------------------------------------------------------------------------------------------------

### [Flex layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#flex_layout)

This example demonstrates using the `column-gap` property to create horizontal space between adjacent flex items.

#### HTML

We include six items in a container element:

html

    <div class="flexbox">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

#### CSS

We set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `flex` and the [`flex-flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
 property to `row wrap` to create a flex container with rows of items. This allows the items to flow onto new lines if needed. The flex items are each given a flex basis of either `200px` or `300px`.

We define a column rule with the [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 property. The `column-gap` value is set to `20px` on the flex container, creating a `20px` gap between the adjacent flex items in each row. The column rule is drawn in the middle of the gap.

css

    .flexbox {
      display: flex;
      flex-flow: row wrap;
      column-rule: 1px solid magenta;
    
      column-gap: 20px;
    }
    
    .flexbox > div {
      border: 1px solid green;
      background-color: lime;
      height: 35px;
      flex: 200px;
    }
    div:nth-of-type(3n) {
      flex: 300px;
    }
    

#### Result

To set vertical space between flex rows, specify a non-zero value for the [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
 property, optionally setting both `row-gap` and `column-gap` by using the `gap` shorthand.

### [Grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#grid_layout)

This example demonstrates using the `column-gap` property with a `<percentage>` value in a grid layout. It also demonstrates how the `column-gap` size is not affected by the size of the column rule.

#### HTML

We include seven items in a container element:

html

    <div id="grid">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    

#### CSS

We set the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 to `grid`, the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 to `400px` and the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 to `repeat(3, 1fr)` to create a 400px-wide grid container with three columns and as many rows as needed. Each row is `100px` tall, as defined by the [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
 property. Every odd grid item has a `lime` background color and the even grid items are semi-opaque.

We've also set a very wide, semi-opaque `column-rule` to demonstrate how the rule is painted behind the content, with the width of the rule having no impact on the size of the gap. The `column-gap` is set to `5%`, which creates a gap that is `20px` wide.

css

    #grid {
      display: grid;
      width: 400px;
      grid-template-columns: repeat(3, 1fr);
      grid-auto-rows: 100px;
      column-rule: 30px solid #ff00ff33;
    
      column-gap: 5%;
    }
    
    #grid > div {
      outline: 1px solid green;
      background-color: lime;
    }
    #grid > div:nth-of-type(even) {
      background-color: #00ff0033;
    }
    

    @layer no-support {
      @supports not (column-gap: 5%) {
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

The column rule is wider than the column gap, and is visible only where the items drawn on top are semi-transparent.

### [Multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#multi-column_layout)

This example demonstrates using the `column-gap` property with a `<line-width>` keyword value in a multi-col layout.

#### HTML

html

    <p class="content-box">
      This is some multi-column text with a thin column gap created with the CSS
      `column-gap` property. The `normal` default value for the `column-gap`
      property in multi-col layout is 1em.
    </p>
    

#### CSS

css

    .content-box {
      column-count: 3;
      column-gap: thin;
    }
    

    @layer no-support {
      @supports not (column-gap: thick) {
        body::before {
          content: "Your browser doesn't support the <line-width> keyword values";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Gaps Module Level 1  <br>\# column-row-gap](https://drafts.csswg.org/css-gaps-1/#column-row-gap) |
| [CSS Grid Layout Module Level 2  <br>\# gutters](https://drafts.csswg.org/css-grid/#gutters) |
| [CSS Multi-column Layout Module Level 1  <br>\# column-gap](https://drafts.csswg.org/css-multicol/#column-gap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap#see_also)

------------------------------------------------------------------------------------------------------

*   [`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
    
*   [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    
*   [`rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
    
*   [Defining CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps/Defining_gaps)
    
*   [Basic concepts of grid layout: gutters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#gutters)
    
*   [Styling Columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Styling_columns)
    
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-gap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-gap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-gap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-gap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-gap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-gap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F04dfe418f2942ae739d41592c22fafa3679fc03c%0A*+Document+last+modified%3A+2026-10-05T17%3A37%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#mdn-search)
    

`border-spacing` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-spacing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the distance between the borders of adjacent cells in a [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
. This property applies only when [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 is `separate`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#try_it)

------------------------------------------------------------------------------------------------------

    border-spacing: 0;
    

    border-spacing: 5px;
    

    border-spacing: 5px 1rem;
    

    <section class="default-example" id="default-example">
      <table class="transition-all" id="example-element">
        <tbody>
          <tr>
            <td>Cell 1.1</td>
            <td>Cell 1.2</td>
          </tr>
          <tr>
            <td>Cell 2.1</td>
            <td>Cell 2.2</td>
          </tr>
          <tr>
            <td>Cell 3.1</td>
            <td>Cell 3.2</td>
          </tr>
        </tbody>
      </table>
    </section>
    

    table {
      width: 15rem;
      table-layout: fixed;
    }
    
    td {
      border: 5px solid;
      border-color: crimson dodgerblue;
      padding: 0.75rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#syntax)

------------------------------------------------------------------------------------------------------

css

    /* <length> */
    border-spacing: 2px;
    
    /* horizontal <length> | vertical <length> */
    border-spacing: 1cm 2em;
    
    /* Global values */
    border-spacing: inherit;
    border-spacing: initial;
    border-spacing: revert;
    border-spacing: revert-layer;
    border-spacing: unset;
    

The `border-spacing` property may be specified as either one or two values.

*   When **one** `<length>` value is specified, it defines both the horizontal and vertical spacings between cells.
*   When **two** `<length>` values are specified, the first value defines the horizontal spacing between cells (i.e., the space between cells in adjacent _columns_), and the second value defines the vertical spacing between cells (i.e., the space between cells in adjacent _rows_).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The size of the spacing as a fixed value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#description)

----------------------------------------------------------------------------------------------------------------

The `border-spacing` value is also used along the outside edge of the table, where the distance between the table's border and the cells in the first/last column or row is the sum of the relevant (horizontal or vertical) `border-spacing` and the relevant (top, right, bottom, or left) [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 on the table.

**Note:** The `border-spacing` property is equivalent to the deprecated `cellspacing` attribute of the `<table>` element, except that `border-spacing` has an optional second value that can be used to set different horizontal and vertical spacing.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | `table` and `inline-table` elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | two absolute lengths |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

border-spacing =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#examples)

----------------------------------------------------------------------------------------------------------

### [Spacing and padding table cells](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#spacing_and_padding_table_cells)

This example applies a spacing of `.5em` vertically and `1em` horizontally between a table's cells. Note how, along its outside edges, the table's `padding` values are added to its `border-spacing` values.

#### HTML

html

    <table>
      <tbody>
        <tr>
          <td>1</td>
          <td>2</td>
          <td>3</td>
        </tr>
        <tr>
          <td>4</td>
          <td>5</td>
          <td>6</td>
        </tr>
        <tr>
          <td>7</td>
          <td>8</td>
          <td>9</td>
        </tr>
      </tbody>
    </table>
    

#### CSS

css

    table {
      border-spacing: 1em 0.5em;
      padding: 0 2em 1em 0;
      border: 1px solid orange;
    }
    
    td {
      width: 1.5em;
      height: 1.5em;
      background: #d2d2d2;
      text-align: center;
      vertical-align: middle;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# separated-borders](https://drafts.csswg.org/css2/#separated-borders) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing#see_also)

----------------------------------------------------------------------------------------------------------

*   [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
    , [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   The `border-spacing` property alters the appearance of the [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
     HTML element.
*   [CSS table](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Table)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-spacing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-spacing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-spacing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-spacing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-spacing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-spacing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#mdn-search)
    

`column-count` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-count`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property breaks an element's content into the specified number of columns.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#try_it)

----------------------------------------------------------------------------------------------------

    column-count: 2;
    

    column-count: 3;
    

    column-count: 4;
    

    column-count: auto;
    column-width: 8rem;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

    #example-element {
      width: 100%;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    column-count: auto;
    
    /* <integer> value */
    column-count: 3;
    
    /* Global values */
    column-count: inherit;
    column-count: initial;
    column-count: revert;
    column-count: revert-layer;
    column-count: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#values)

This property is specified as a single value from the following list:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#auto)

The number of columns is determined by other CSS properties, such as [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Is a strictly positive [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 describing the ideal number of columns into which the content of the element will be flowed. If the [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 is also set to a non-`auto` value, it merely indicates the maximum allowed number of columns.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#description)

--------------------------------------------------------------------------------------------------------------

Setting the `column-count` to a value greater than `1` creates a multi-column layout. The element's content will be evenly distributed between the specified number of columns.

The `column-count` property, along with the [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 and [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 properties, can also be set by using the [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block containers except table wrapper boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | an [integer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation "Values of the <integer> CSS data type are interpolated via integer discrete steps. The calculation is done as if they were real, floating-point numbers and the discrete value is obtained using the floor function.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#formal_syntax)

------------------------------------------------------------------------------------------------------------------

column-count =   
  auto             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer \[1,∞\]>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#examples)

--------------------------------------------------------------------------------------------------------

### [Splitting a paragraph across three columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#splitting_a_paragraph_across_three_columns)

#### HTML

html

    <p class="content-box">
      This is a bunch of text split into three columns using the CSS
      <code>column-count</code>
      property. The text is equally distributed over the columns.
    </p>
    

#### CSS

css

    .content-box {
      column-count: 3;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 1  <br>\# cc](https://drafts.csswg.org/css-multicol/#cc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count#see_also)

--------------------------------------------------------------------------------------------------------

*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
    
*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
     shorthand
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    , [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    , [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    , [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
     shorthand
*   [Learn: Multiple-column Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
     (Learn Layout)
*   [Basic Concepts of Multicol](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Basic_concepts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-count/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-count (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-count&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-count%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-count%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-count%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1cf7346516383565b51a125c064ae3d5d893526%0A*+Document+last+modified%3A+2026-09-14T09%3A37%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
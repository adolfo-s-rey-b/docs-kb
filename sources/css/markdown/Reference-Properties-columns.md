*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#mdn-search)
    

`columns` CSS property
======================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`columns`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets the maximum number of columns to use when drawing an element's contents, along with the minimum width and maximum height of the element's columns.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#try_it)

-----------------------------------------------------------------------------------------------

    columns: 2;
    

    columns: 6rem auto;
    

    columns: 12em;
    

    columns: 2 / 5em;
    

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
      min-width: 21rem;
      text-align: left;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Column width */
    columns: 18em;
    
    /* Column count */
    columns: auto;
    columns: 2;
    
    /* Column width and count */
    columns: 2 auto;
    columns: auto 12em;
    columns: auto auto;
    
    /* Column width and/or count, and column height */
    columns: 18em / 10em;
    columns: 2 / 90vh;
    columns: 2 auto / 300px;
    
    /* Global values */
    columns: inherit;
    columns: initial;
    columns: revert;
    columns: revert-layer;
    columns: unset;
    

The `columns` property value may be specified as a [`<column-count>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 and/or a [`<column-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 value, in any order, optionally followed by a [`<column-height>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 value preceded by a forward slash (`/`).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#values)

[`<'column-width'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#column-width)

The ideal column width, defined as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or the keyword `auto`. The actual width may be wider or narrower to fit the available space. See [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
.

[`<'column-count'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#column-count)

The ideal number of columns into which the element's content should be flowed, defined as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or the keyword `auto`. If specified as an `<integer>`, it defines the maximum allowable number of columns. See [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
.

[`<'column-height'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#column-height)

The height of the columns defined as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or the keyword `auto`. See [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
.

**Note:** Setting a `<column-height>` value resets the [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
 property to its initial value, `auto`. When `<column-height>` is set to a `<length>`, the [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
 `auto` value resolves to `wrap`. When `<column-height>` is set to `auto`, it resolves to `nowrap`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)<br>    : `auto`<br>*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)<br>    : `auto`<br>*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)<br>    : `auto` |
| Applies to | Block containers except table wrapper boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)<br>    : `auto` if specified as `auto`, otherwise for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>     the absolute value specified<br>*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)<br>    : as specified<br>*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)<br>    : `auto` if specified as `auto`, otherwise for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>     the absolute value specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)<br>    : by computed value type<br>*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)<br>    : an [integer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation "Values of the <integer> CSS data type are interpolated via integer discrete steps. The calculation is done as if they were real, floating-point numbers and the discrete value is obtained using the floor function.")<br>    <br>*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#formal_syntax)

-------------------------------------------------------------------------------------------------------------

columns =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'column-width'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'column-count'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<'column-height'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<column-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 =   
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <box-size>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <box-size>    
  
[<column-count>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 =   
  auto             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer \[1,∞\]>    
  
[<column-height>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    
  
<box-size> =   
  <length-percentage \[0,∞\]>                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contain                                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  min-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  max-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stretch( <length-percentage \[0,∞\]> )      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fit-content( <length-percentage \[0,∞\]> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>                               
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<calc-size()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 =   
  calc-size( <calc-size-basis> , <calc-sum> )    
  
<calc-size-basis> =   
  <size-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-sum>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-size()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  any               
  
[<calc-sum>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
 =   
  <calc-product> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '+' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 '-' [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-product> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-product> =   
  <calc-value> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '\*' [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 / [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <calc-value> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    
  
<calc-value> =   
  [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dimension>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <calc-keyword>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <calc-sum> )    
  
[<calc-keyword>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
 =   
  e          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pi         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  NaN          

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#examples)

---------------------------------------------------------------------------------------------------

### [Setting three equal columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#setting_three_equal_columns)

This example shows how to split a text container into three equal columns.

#### HTML

We include a basic [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element containing text content.

html

    <p class="content-box">
      This is a bunch of text split into three columns using the CSS
      <code>columns</code>
      property. The text is equally distributed over the columns.
    </p>
    

#### CSS

We set a `columns` property value on the paragraph that includes a `<column-count>` value of `3` and a `<column-width>` value of `auto`.

    body {
      width: 60%;
      margin: 0 auto;
    }
    

css

    .content-box {
      columns: 3 auto;
    }
    

#### Result

Note how the text is split up into three columns.

### [Creating wrapping, fixed height columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#creating_wrapping_fixed_height_columns)

This example demonstrates including a `<column-height>` value with the `columns` shorthand property to split a text container into fixed-height columns that wrap onto new lines when the container inline edge is reached.

#### HTML

We include a basic [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element with some text.

html

    <p class="content-box">
      This is a bunch of text split into three columns using the CSS
      <code>columns</code> property. This includes a <code>column-count</code> value
      of <code>3</code>, a <code>column-width</code> value of <code>auto</code>, and
      a <code>column-height</code> value of <code>5em</code>. The
      <code>column-wrap</code> value is set to its initial value, <code>auto</code>;
      when a <code>column-height</code> value is included,
      <code>column-wrap: auto</code> resolves to <code>wrap</code>, which allows the
      columns to wrap onto multiple rows. The text is equally distributed over the
      columns, and placed into multiple rows.
    </p>
    

#### CSS

We set a `columns` property value on the paragraph that includes a `<column-count>` value of `3`, a `<column-width>` value of `auto`, and a `<column-height>` value of `5em`. Because the `<column-height>` is set to a `<length>`, the paragraph's [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
 value computes to `wrap`, which allows the columns to wrap onto multiple rows.

css

    .content-box {
      columns: 3 auto / 5em;
    }
    

    body {
      width: 60%;
      margin: 0 auto;
    }
    

    @supports not (columns: 3 auto / 5em) {
      body::before {
        content: "Your browser does not support the 'column-height' property.";
        background-color: wheat;
        position: fixed;
        inset: 40% 0;
        height: fit-content;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

Note how the text is split up into three columns. Each column is `5em` high. After every third column, the columns wrap onto a new line in the block direction.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 2  <br>\# propdef-columns](https://drafts.csswg.org/css-multicol-2/#propdef-columns) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns#see_also)

---------------------------------------------------------------------------------------------------

*   [`widows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
    
*   [`orphans`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    
*   [Paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
    
*   [Learn: Multiple-column Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/columns/index.md?plain=1 "Folder: en-us/web/css/reference/properties/columns (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumns&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumns%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumns%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumns%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
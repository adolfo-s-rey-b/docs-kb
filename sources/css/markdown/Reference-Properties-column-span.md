*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#mdn-search)
    

`column-span` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-span`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property makes it possible for an element to span across all columns when its value is set to `all`.

An element that spans more than one column is called a **spanning element**.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#try_it)

---------------------------------------------------------------------------------------------------

    column-span: none;
    

    column-span: all;
    

    <section id="default-example">
      <div class="multicol-element">
        <p>
          London. Michaelmas term lately over, and the Lord Chancellor sitting in
          Lincoln's Inn Hall.
        </p>
        <div id="example-element">Spanner?</div>
        <p>
          Implacable November weather. As much mud in the streets as if the waters
          had but newly retired from the face of the earth, and it would not be
          wonderful to meet a Megalosaurus, forty feet long or so, waddling like an
          elephantine lizard up Holborn Hill.
        </p>
      </div>
    </section>
    

    .multicol-element {
      width: 100%;
      text-align: left;
      column-count: 3;
    }
    
    .multicol-element p {
      margin: 0;
    }
    
    #example-element {
      background-color: rebeccapurple;
      padding: 10px;
      color: white;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-span: none;
    column-span: all;
    
    /* Global values */
    column-span: inherit;
    column-span: initial;
    column-span: revert;
    column-span: revert-layer;
    column-span: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#none)

The element does not span multiple columns.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#all)

The element spans across all columns. Content in the normal flow that appears before the element is automatically balanced across all columns before the element appears. The element establishes a new block formatting context.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | in-flow block-level elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

column-span =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <integer \[1,∞\]>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto               
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#examples)

-------------------------------------------------------------------------------------------------------

### [Making a heading span columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#making_a_heading_span_columns)

In this example, the heading is made to span across all the columns of the article.

#### HTML

html

    <article>
      <h2>Header spanning all of the columns</h2>
      <p>
        The h2 should span all the columns. The rest of the text should be
        distributed among the columns.
      </p>
      <p>
        This is a bunch of text split into three columns using the CSS `columns`
        property. The text is equally distributed over the columns.
      </p>
      <p>
        This is a bunch of text split into three columns using the CSS `columns`
        property. The text is equally distributed over the columns.
      </p>
      <p>
        This is a bunch of text split into three columns using the CSS `columns`
        property. The text is equally distributed over the columns.
      </p>
      <p>
        This is a bunch of text split into three columns using the CSS `columns`
        property. The text is equally distributed over the columns.
      </p>
    </article>
    

#### CSS

css

    article {
      columns: 3;
    }
    
    h2 {
      column-span: all;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 1  <br>\# column-span](https://drafts.csswg.org/css-multicol/#column-span) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span#see_also)

-------------------------------------------------------------------------------------------------------

*   [Spanning and balancing columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout/Spanning_balancing_columns)
    
*   [Inline-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)
    
*   [`HTMLSpanElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSpanElement)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-span/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-span (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-span&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-span%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-span%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-span%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
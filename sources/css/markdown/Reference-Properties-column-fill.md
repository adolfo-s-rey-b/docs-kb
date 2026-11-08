*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#mdn-search)
    

`column-fill` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`column-fill`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls how an element's contents are balanced when broken into columns.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#try_it)

---------------------------------------------------------------------------------------------------

    column-fill: auto;
    

    column-fill: balance;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather.
      </p>
    </section>
    

    #example-element {
      width: 100%;
      height: 90%;
      columns: 3;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-fill: auto;
    column-fill: balance;
    
    /* Global values */
    column-fill: inherit;
    column-fill: initial;
    column-fill: revert;
    column-fill: revert-layer;
    column-fill: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#auto)

Columns are filled sequentially. Content takes up only the room it needs, possibly resulting in some columns remaining empty.

[`balance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#balance)

Content is equally divided between columns. In fragmented contexts, such as [paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
, only the last fragment is balanced. Therefore in paged media, only the last page would be balanced. This is the default value.

The specification defines a `balance-all` value, in which content is equally divided between columns in fragmented contexts, such as [paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
. This value is not yet supported in any browser.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `balance` |
| Applies to | multicol elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

column-fill =   
  auto         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  balance      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  balance-all    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#examples)

-------------------------------------------------------------------------------------------------------

### [Balancing column content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#balancing_column_content)

#### HTML

html

    <p class="fill-auto">
      This paragraph fills columns one at a time. Since all of the text can fit in
      the first column, the others are empty.
    </p>
    
    <p class="fill-balance">
      This paragraph attempts to balance the amount of content in each column.
    </p>
    

#### CSS

css

    p {
      height: 7em;
      background: #ffff99;
      columns: 3;
      column-rule: 1px solid;
    }
    
    p.fill-auto {
      column-fill: auto;
    }
    
    p.fill-balance {
      column-fill: balance;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 1  <br>\# cf](https://drafts.csswg.org/css-multicol/#cf) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

**Warning:** There are some interoperability issues and bugs with `column-fill` across browsers, due to unresolved issues in the specification.

In particular, when using `column-fill: auto` to fill columns sequentially, Chrome will only consult this property if the multicol container has a size in the block dimension (e.g., height in a horizontal writing mode). Firefox will always consult this property, therefore filling the first column with all of the content in cases where there is no size.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill#see_also)

-------------------------------------------------------------------------------------------------------

*   [Learn: Multiple-column Layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Multiple-column_Layout)
    
*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-fill/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-fill (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-fill&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-fill%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-fill%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-fill%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
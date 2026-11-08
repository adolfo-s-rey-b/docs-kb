*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#mdn-search)
    

`<display-legacy>` CSS type
===========================

CSS 2 used a single-keyword syntax for the `display` property, requiring separate keywords for block-level and inline-level variants of the same layout mode. This page details those values.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#syntax)

--------------------------------------------------------------------------------------------------

Valid `<display-legacy>` values:

[`inline-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#inline-block)

The element generates a block element box that will be flowed with surrounding content as if it were a single inline box (behaving much like a replaced element would).

It is equivalent to `inline flow-root`.

[`inline-table`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#inline-table)

The `inline-table` value does not have a direct mapping in HTML. It behaves like an HTML [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 element, but as an inline box, rather than a block-level box. Inside the table box is a block-level context.

It is equivalent to `inline table`.

[`inline-flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#inline-flex)

The element behaves like an inline element and lays out its content according to the flexbox model.

It is equivalent to `inline flex`.

[`inline-grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#inline-grid)

The element behaves like an inline element and lays out its content according to the grid model.

It is equivalent to `inline grid`.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#formal_syntax)

----------------------------------------------------------------------------------------------------------------

<display-legacy> =   
  inline-block  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-table  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-flex   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-grid     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#examples)

------------------------------------------------------------------------------------------------------

In the below example, we are creating an inline flex container with the legacy keyword inline-flex.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#result)

In the new syntax the inline flex container would be created using two values, inline for the outer display type, and flex for the inner display type.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# typedef-display-legacy](https://drafts.csswg.org/css-display/#typedef-display-legacy) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [css.properties.display.inline-block](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#css.properties.display.inline-block)

### [css.properties.display.inline-table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#css.properties.display.inline-table)

### [css.properties.display.inline-flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#css.properties.display.inline-flex)

### [css.properties.display.inline-grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#css.properties.display.inline-grid)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy#see_also)

------------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    *   [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
        
    *   [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
        
    *   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
        
    *   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
        
    *   [`<display-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/display-legacy/index.md?plain=1 "Folder: en-us/web/css/reference/values/display-legacy (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-legacy&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-legacy%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-legacy%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-legacy%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
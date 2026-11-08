*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#mdn-search)
    

`<display-internal>` CSS type
=============================

Some layout models such as `table` and `ruby` have a complex internal structure, with several different roles that their children and descendants can fill. This page defines those "internal" display values, which only have meaning within that particular layout mode.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#syntax)

----------------------------------------------------------------------------------------------------

Valid `<display-internal>` values:

[`table-row-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-row-group)

These elements behave like [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody)
 HTML elements.

[`table-header-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-header-group)

These elements behave like [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead)
 HTML elements.

[`table-footer-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-footer-group)

These elements behave like [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot)
 HTML elements.

[`table-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-row)

These elements behave like [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)
 HTML elements.

[`table-cell`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-cell)

These elements behave like [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)
 HTML elements.

[`table-column-group`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-column-group)

These elements behave like [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
 HTML elements.

[`table-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-column)

These elements behave like [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 HTML elements.

[`table-caption`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#table-caption)

These elements behave like [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption)
 HTML elements.

[`ruby-base`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#ruby-base)

These elements behave like [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)
 HTML elements.

[`ruby-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#ruby-text)

These elements behave like [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
 HTML elements.

[`ruby-base-container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#ruby-base-container)

These elements are generated as anonymous boxes.

[`ruby-text-container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#ruby-text-container)

These elements behave like [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)
 HTML elements.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#formal_syntax)

------------------------------------------------------------------------------------------------------------------

<display-internal> =   
  table-row-group      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-header-group   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-footer-group   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-row            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-cell           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-column-group   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-column         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table-caption        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ruby-base            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ruby-text            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ruby-base-container  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ruby-text-container    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#examples)

--------------------------------------------------------------------------------------------------------

### [CSS tables example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css_tables_example)

The following example demonstrates laying out a form using CSS table layout.

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 4  <br>\# valdef-display-table-row-group](https://drafts.csswg.org/css-display-4/#valdef-display-table-row-group) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-header-group](https://drafts.csswg.org/css-display-4/#valdef-display-table-header-group) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-footer-group](https://drafts.csswg.org/css-display-4/#valdef-display-table-footer-group) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-row](https://drafts.csswg.org/css-display-4/#valdef-display-table-row) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-cell](https://drafts.csswg.org/css-display-4/#valdef-display-table-cell) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-column-group](https://drafts.csswg.org/css-display-4/#valdef-display-table-column-group) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-column](https://drafts.csswg.org/css-display-4/#valdef-display-table-column) |
| [CSS Display Module Level 4  <br>\# valdef-display-table-caption](https://drafts.csswg.org/css-display-4/#valdef-display-table-caption) |
| [CSS Display Module Level 4  <br>\# valdef-display-ruby-base](https://drafts.csswg.org/css-display-4/#valdef-display-ruby-base) |
| [CSS Display Module Level 4  <br>\# valdef-display-ruby-text](https://drafts.csswg.org/css-display-4/#valdef-display-ruby-text) |
| [CSS Display Module Level 4  <br>\# valdef-display-ruby-base-container](https://drafts.csswg.org/css-display-4/#valdef-display-ruby-base-container) |
| [CSS Display Module Level 4  <br>\# valdef-display-ruby-text-container](https://drafts.csswg.org/css-display-4/#valdef-display-ruby-text-container) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

### [css.properties.display.table-row-group](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-row-group)

### [css.properties.display.table-header-group](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-header-group)

### [css.properties.display.table-footer-group](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-footer-group)

### [css.properties.display.table-row](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-row)

### [css.properties.display.table-cell](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-cell)

### [css.properties.display.table-column-group](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-column-group)

### [css.properties.display.table-column](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-column)

### [css.properties.display.table-caption](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.table-caption)

### [css.properties.display.ruby-base](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.ruby-base)

### [css.properties.display.ruby-text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.ruby-text)

### [css.properties.display.ruby-base-container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.ruby-base-container)

### [css.properties.display.ruby-text-container](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#css.properties.display.ruby-text-container)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal#see_also)

--------------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    *   [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
        
    *   [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
        
    *   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
        
    *   [`<display-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
        
    *   [`<display-legacy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/display-internal/index.md?plain=1 "Folder: en-us/web/css/reference/values/display-internal (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-internal&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-internal%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-internal%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-internal%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
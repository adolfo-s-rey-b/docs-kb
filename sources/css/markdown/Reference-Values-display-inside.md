*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#mdn-search)
    

`<display-inside>` CSS type
===========================

These keywords specify the element's inner [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 type, which defines the type of formatting context that lays out its contents (assuming it is a non-replaced element). These keywords are used as values of the `display` property, and can be used for legacy purposes as a single keyword, or as defined in the Level 3 specification alongside a value from the [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
 keywords.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#syntax)

--------------------------------------------------------------------------------------------------

Valid `<display-inside>` values:

[`flow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#flow)

The element lays out its contents using flow layout (block-and-inline layout).

If its outer display type is `inline`, and it is participating in a block or inline formatting context, then it generates an inline box. Otherwise it generates a block container box.

Depending on the value of other properties (such as [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
, [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
, or [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
) and whether it is itself participating in a block or inline formatting context, it either establishes a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 (BFC) for its contents or integrates its contents into its parent formatting context.

[`flow-root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#flow-root)

The element generates a block element box that establishes a new [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
, defining where the formatting root lies.

[`table`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#table)

These elements behave like HTML [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
 elements. It defines a block-level box.

[`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#flex)

The element behaves like a block element and lays out its content according to the [flexbox model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
.

[`grid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#grid)

The element behaves like a block element and lays out its content according to the [grid model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)
.

[`ruby`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#ruby)

The element behaves like an inline element and lays out its content according to the ruby formatting model. It behaves like the corresponding HTML [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 elements.

**Note:** Browsers that support the two value syntax, on finding the inner value only, such as when `display: flex` or `display: grid` is specified, will set their outer value to `block`. This will result in expected behavior; for example if you specify an element to be `display: grid`, you would expect that the box created on the grid container would be a block level box.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#formal_syntax)

----------------------------------------------------------------------------------------------------------------

<display-inside> =   
  flow       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flow-root  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  table      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  flex       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  grid       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ruby         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#examples)

------------------------------------------------------------------------------------------------------

In this example the parent box has been given `display: flow-root` and so establishes a new BFC and contains the floated item.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# typedef-display-inside](https://drafts.csswg.org/css-display/#typedef-display-inside) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [css.properties.display.flow-root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css.properties.display.flow-root)

### [css.properties.display.table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css.properties.display.table)

### [css.properties.display.flex](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css.properties.display.flex)

### [css.properties.display.grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css.properties.display.grid)

### [css.properties.display.ruby](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#css.properties.display.ruby)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside#see_also)

------------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    *   [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
        
    *   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
        
    *   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
        
    *   [`<display-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
        
    *   [`<display-legacy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
        
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [Basic Concepts of grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/display-inside/index.md?plain=1 "Folder: en-us/web/css/reference/values/display-inside (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-inside&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-inside%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-inside%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-inside%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#mdn-search)
    

`<display-outside>` CSS type
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `<display-outside>` keywords specify the element's outer [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 type, which is essentially its role in flow layout. These keywords are used as values of the `display` property, and can be used for legacy purposes as a single keyword, or as defined in the Level 3 specification alongside a value from the [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
 keywords.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#syntax)

---------------------------------------------------------------------------------------------------

Valid `<display-outside>` values:

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#block)

The element generates a block element box, generating line breaks both before and after the element when in the normal flow.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#inline)

The element generates one or more inline element boxes that do not generate line breaks before or after themselves. In normal flow, the next element will be on the same line if there is space.

**Note:** When browsers encounter a display property with only an **outer** `display` value (e.g., `display: block` or `display: inline`), the inner value defaults to `flow` (e.g., `display: block flow` and `display: inline flow`). This is backwards-compatible with single-keyword syntax.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<display-outside> =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  run-in    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#examples)

-------------------------------------------------------------------------------------------------------

In the following example, span elements (normally displayed as inline elements) are set to `display: block` and so break onto new lines and expand to fill their container in the inline dimension.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# typedef-display-outside](https://drafts.csswg.org/css-display/#typedef-display-outside) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

### [css.properties.display.block](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#css.properties.display.block)

### [css.properties.display.inline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#css.properties.display.inline)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside#see_also)

-------------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    *   [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
        
    *   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
        
    *   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
        
    *   [`<display-box>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
        
    *   [`<display-legacy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
        
*   [Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_and_inline_layout)
    
*   [Introduction to formatting contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Formatting_contexts)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/display-outside/index.md?plain=1 "Folder: en-us/web/css/reference/values/display-outside (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-outside&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-outside%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-outside%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-outside%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
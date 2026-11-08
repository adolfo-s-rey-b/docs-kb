*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#mdn-search)
    

`size` CSS at-rule descriptor
=============================

Baseline 2024

Newly available

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 descriptor, used with the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 at-rule, defines the size and orientation of the box which is used to represent a page. Most of the time, this size corresponds to the target size of the printed page if applicable.

Size may either be defined with a "scalable" keyword (in this case the page will fill the available dimensions) or with absolute dimensions.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#syntax)

------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#auto)

The user agent decides the size of the page. In most cases, the dimensions and orientation of the target sheet are used.

[`landscape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#landscape)

The content of the page is displayed in landscape mode (i.e., the longest side of the box is horizontal).

[`portrait`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#portrait)

The content of the page is displayed in portrait mode (i.e., the longest side of the box is vertical). This is the default orientation.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#length)

Any length value (see [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
). The first value corresponds to the width of the page box and the second one corresponds to its height. If only one value is provided, it is used for both width and height.

[`<page-size>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#page-size)

A keyword which may be any of the following values:

[A5](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#a5)

This matches the standard, ISO dimensions: 148mm x 210mm.

[A4](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#a4)

This matches the standard, ISO dimensions: 210mm x 297mm. (most frequently used dimensions for personal printing.)

[A3](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#a3)

This matches the standard, ISO dimensions: 297mm x 420mm.

[B5](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#b5)

This matches the standard, ISO dimensions: 176mm x 250mm.

[B4](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#b4)

This matches the standard, ISO dimensions: 250mm x 353mm.

[JIS-B5](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#jis-b5)

This correspond to the JIS standard dimensions: 182mm x 257mm.

[JIS-B4](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#jis-b4)

This correspond to the JIS standard dimensions: 257mm x 364mm.

[letter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#letter)

This keyword is an equivalent to the dimensions of letter paper in North America i.e., 8.5in x 11in.

[legal](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#legal)

This keyword is an equivalent to the dimensions of legal papers in North America i.e., 8.5in x 14in.

[ledger](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#ledger)

This keyword is an equivalent to the dimensions of ledger pages in North America i.e., 11in x 17in.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with relative lengths converted into absolute lengths |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#formal_syntax)

--------------------------------------------------------------------------------------------------------------

size =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
                          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <page-size> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 portrait [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 landscape [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<page-size> =   
  A5      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  A4      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  A3      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  B5      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  B4      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  JIS-B5  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  JIS-B4  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  letter  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  legal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ledger    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#examples)

----------------------------------------------------------------------------------------------------

### [Specifying size and orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#specifying_size_and_orientation)

### [Specifying a custom size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#specifying_a_custom_size)

### [Nesting inside a @media rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#nesting_inside_a_media_rule)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Paged Media Module Level 3  <br>\# page-size-prop](https://drafts.csswg.org/css-page/#page-size-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@page/size/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@page/size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page%2Fsize&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%2Fsize%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40page%2Fsize%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40page%2Fsize%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
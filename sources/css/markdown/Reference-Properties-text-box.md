*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#mdn-search)
    

`text-box` CSS property
=======================

Baseline 2026

Newly available

Since August 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/265)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-box`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property corresponds to the [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 and [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 properties, which together specify the amount of space to trim from the block-start edge and block-end edge of a text element's block container.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
    
*   [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#syntax)

------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#values)

The `text-box` value can be composed of a [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 value and a [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 value separated by a space. See those pages for value descriptions.

The `text-box` property can also take a keyword of `normal`, which is equivalent to `text-box: none auto;`

If `text-box-trim` is omitted, it is set to `trim-both`. If `text-box-edge` is omitted, it is set to `auto`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | Block containers and inline boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#formal_syntax)

--------------------------------------------------------------------------------------------------------------

text-box =   
  normal                                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<'text-box-trim'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [<'text-box-edge'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    
  
[<text-box-trim>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 =   
  none        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  trim-both     
  
[<text-box-edge>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 =   
  auto         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <text-edge>    
  
[<text-edge>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 cap [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ex [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ideographic-ink [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 alphabetic [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#description)

----------------------------------------------------------------------------------------------------------

The height of text-only content is relative to the height of the font. In digital font files, the height contains all characters, including capital letters, ascenders, descenders, etc. Different fonts have different base line-heights, meaning that lines of text with the same `font-size` will produce line boxes of differing heights, affecting the appearance of spacing between lines.

The `text-box` properties enable trimming off extra spacing from the block-start edge and block-end edge of a text element's block container, which can include the [leading](https://developer.mozilla.org/en-US/docs/Glossary/Leading)
 at the text's block-start edge and block-end edges, and the spacing defined inside the font (as described above). This makes it much easier to control text spacing in the block direction.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#examples)

----------------------------------------------------------------------------------------------------

### [Basic `text-box` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#basic_text-box_usage)

In the following example, we have two `<p>` elements with classes of `one` and `two`.

We apply a `text-box` value of `trim-end cap alphabetic` to the first paragraph. The [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 value of `cap alphabetic` specifies trimming the over edge to the top of the capital letters and the under edge flush with the text baseline. Because the [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 value is set to `trim-end`, only the under edge of the paragraph is trimmed.

We apply a `text-box` value of `trim-both ex alphabetic` to the second paragraph. The [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
 value of `ex alphabetic` specifies trimming the over edge to the font's x-height (the top edge of the short lower-case letters) and the under edge flush with the text baseline. Because the [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 value is set to `trim-both`, both the over _and_ under edge of the paragraph are trimmed.

#### Result

The output is as follows. Note how we've included a top and bottom border on each paragraph, so that you can see how the space has been trimmed in each case.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# text-box-shorthand](https://drafts.csswg.org/css-inline-3/#text-box-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box#see_also)

----------------------------------------------------------------------------------------------------

*   [`text-box-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    , [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
    
*   [`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
     data type
*   [CSS inline layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout)
     module
*   [CSS text-box-edge](https://developer.chrome.com/blog/css-text-box-trim "External link (opens in new tab)")
     on developer.chrome.com (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-box/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-box (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
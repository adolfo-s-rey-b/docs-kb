*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#mdn-search)
    

`text-box-edge` CSS property
============================

Baseline 2026

Newly available

Since August 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/265)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-box-edge`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies an amount of space to trim from a text element's block container.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#syntax)

-----------------------------------------------------------------------------------------------------

### [Value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#value)

The `text-box-edge` property value is specified as `auto` or a [`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
 value:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#auto)

The default value. Equivalent to the `text-edge` value `text`.

[`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)

One or two separate keywords representing over and under edge positions to trim the text element's block container to.

*   If two values are specified, the first value specifies the trimming behavior to apply to the block-start (over) edge of the text, and the second value specifies the trimming behavior to apply to the block-end (under) edge of the text.
    *   Valid over edge trimming values: `text`, `cap`, and `ex`.
    *   Valid under edge trimming values: `text` and `alphabetic`.
*   If one value is specified, it specifies the over _and_ under edge trimming behavior. At the time of writing, the only valid single value is `text`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#description)

---------------------------------------------------------------------------------------------------------------

The `text-box-edge` property specifies an amount of space to trim from a text element's block container.

Vertical spacing differs between fonts, making consistent typesetting historically challenging on the web. The `text-box-edge` property — along with its counterpart property [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
, which specifies which edge(s) to trim space from — makes consistent typesetting easier to achieve. The `text-box-edge` property has no effect if `text-box-trim` is not set or is set to `none`.

The height of text-only content is relative to the height of the font. In digital font files, the height contains all characters, including capital letters, ascenders, descenders, etc. Different fonts have different base line-heights, meaning that lines of text with the same `font-size` will produce line boxes of differing heights, affecting the appearance of spacing between lines.

The `text-box-edge` property allows you to trim space from the start and/or end edge of the text's block container. This can include the [leading](https://developer.mozilla.org/en-US/docs/Glossary/Leading)
 at the text's block-start edge and block-end edges and the spacing defined inside the font (as described above). It does this by specifying a [`<text-edge>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
 value that indicates the over edge and under edge to trim the space to.

Which edge(s) to trim space from is specified using the [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 property. For example, you can choose to trim space from the over edge or the under edge of the text's block container, or both.

These properties make it much easier to control text spacing in the block direction.

The `text-box-edge` property, along with the [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 property, can also be set by using the [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block containers and inline boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

text-box-edge =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#examples)

---------------------------------------------------------------------------------------------------------

### [Basic `text-box-edge` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#basic_text-box-edge_usage)

The most common `text-box-edge` values you'll use for horizontal [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 languages such as English or Arabic are `cap alphabetic` and `ex alphabetic`. The `cap` value trims the over edge of the text element's block container to the top of the capital letters, whereas `ex` trims the over edge to the font's x-height (the top edge of the short lower-case letters). In each case, `alphabetic` trims the under-edge flush with the text baseline.

In this example, we demonstrate the effect of both of these common values, on two [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements. Additionally, a [`text-box-trim`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
 value of `trim-both` has been set on both of them, so that their start _and_ end edges are trimmed.

#### Result

The output is as follows. Note how we've included a top and bottom border on each paragraph, so that you can see how the space has been trimmed in each case.

### [Interactive `text-box-edge` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#interactive_text-box-edge_value_comparison)

For a complete interactive `text-box-edge` example, see the [`text-box-trim` page](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim#interactive_text-box-trim_and_text-box-edge_value_comparison)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# text-box-edge](https://drafts.csswg.org/css-inline-3/#text-box-edge) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge#see_also)

---------------------------------------------------------------------------------------------------------

*   [`text-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
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

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-box-edge/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-box-edge (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box-edge&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box-edge%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-box-edge%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-box-edge%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd1cf7346516383565b51a125c064ae3d5d893526%0A*+Document+last+modified%3A+2026-09-14T09%3A37%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
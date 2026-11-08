*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#mdn-search)
    

`text-wrap` CSS property
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2024.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-wrap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property controls how text inside an element is wrapped. The different values provide:

*   Typographic improvements, for example more balanced line lengths across broken headings
*   A way to turn text wrapping off completely.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#try_it)

-------------------------------------------------------------------------------------------------

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
    
*   [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#syntax)

-------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#values)

This property is specified as one of the following keyword values:

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#wrap)

Text is wrapped across lines at appropriate characters (for example spaces, in languages like English that use space separators) to minimize overflow. This is the default value.

[`nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#nowrap)

Text does not wrap across lines. It will overflow its containing element rather than breaking onto a new line.

[`balance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#balance)

Text is wrapped in a way that best balances the number of characters on each line, enhancing layout quality and legibility. Because counting characters and balancing them across multiple lines is computationally expensive, this value is only supported for blocks of text spanning a limited number of lines (six or less for Chromium and ten or less for Firefox).

[`pretty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#pretty)

Results in the same behavior as `wrap`, except that the user agent will use a slower algorithm that favors better layout over speed. This is intended for body copy where good typography is favored over performance (for example, when the number of [orphans](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
 should be kept to a minimum).

[`stable`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#stable)

Results in the same behavior as `wrap`, except that when the user is editing the content, the lines that come before the lines they are editing remain static rather than the whole block of text re-wrapping.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#description)

-----------------------------------------------------------------------------------------------------------

There are 2 ways that text can flow across lines within a block of content, such as a paragraph ([`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
) or headings ([<h1>–<h6>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
). These are _forced line breaks_, that are controlled by the user, and _soft line breaks_, that are controlled by the browser. The `text-wrap` property can be used to prompt the browser how to control the _soft line breaks_.

The value you choose, for `text-wrap`, depends on how many lines of text you anticipate styling, whether the text is `contenteditable`, and whether you need to prioritize appearance or performance.

When the styled content will be limited to a short number of lines, such as headings, captions, and blockquotes, `text-wrap: balance` can be added to balance the number of characters on each line, enhancing layout quality and legibility. As browsers limit the number of lines impacted by this property, this value's impact on performance is negligible.

For longer sections of text, `text-wrap: pretty` can be used. Note that `pretty` has a negative effect on performance, so it should be only used for longer blocks of text when the layout is more important than speed.

The `stable` value improves user experience when used on content that is [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
. This value ensures that, as the user is editing text, the previous lines in the area being edited remain stable.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#formal_definition)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `wrap` |
| Applies to | text and block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| Percentages | as each of the properties of the shorthand:  <br><br>*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)<br>    : no<br>*   [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)<br>    : no |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)<br>    : as specified<br>*   [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)<br>    : discrete<br>*   [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)<br>    : discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#formal_syntax)

---------------------------------------------------------------------------------------------------------------

text-wrap =   
  [<'text-wrap-mode'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<'text-wrap-style'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
    
  
[<text-wrap-mode>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 =   
  wrap    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nowrap    
  
[<text-wrap-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
 =   
  auto                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  balance                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stable                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pretty                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-short-last-line    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#examples)

-----------------------------------------------------------------------------------------------------

### [Basic text wrap value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#basic_text_wrap_value_comparison)

#### HTML

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#css)

#### Result

The text in the example is editable. Change the text, adding long words, to view how the different line and word lengths impact wrapping.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# text-wrap-shorthand](https://drafts.csswg.org/css-text-4/#text-wrap-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap#see_also)

-----------------------------------------------------------------------------------------------------

*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [`white-space-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
    
*   [CSS text module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
    
*   [CSS `text-wrap: balance`](https://developer.chrome.com/docs/css-ui/css-text-wrap-balance "External link (opens in new tab)")
     on developer.chrome.com (2023)
*   [CSS `text-wrap: pretty`](https://developer.chrome.com/blog/css-text-wrap-pretty/ "External link (opens in new tab)")
     on developer.chrome.com (2023)
*   [Balancing Japanese and Korean typography](https://ryelle.codes/2025/04/typography-troubles-balancing-in-japanese-korean/ "External link (opens in new tab)")
     by Kelly Choyce-Dwan (2025)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-wrap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-wrap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
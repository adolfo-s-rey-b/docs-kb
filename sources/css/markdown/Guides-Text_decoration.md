*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#mdn-search)
    

CSS text decoration
===================

The **CSS text decoration** module defines features relating to text decoration, such as underlines, text shadows, and emphasis marks. Text decoration features can provide visual cues for spelling errors, grammar issues, and links. These features can help improve the usability, accessibility, functionality, and aesthetics of your text.

By varying the color, style, and thickness of text decoration using pseudo-classes and pseudo-elements, you can highlight the emphasis in text in ways that don't rely on color alone.

Several features can help improve text readability:

*   [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
     can increase legibility by skipping descenders.
*   [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
     enables you to fine-tune the underline placement to better match font metrics or design aesthetics, which can be especially useful for unique [typefaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
    .
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
     colors that contrast with text [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
     can make the text visually pop when placed on a background with insufficient contrast.

These features all help improve legibility, and therefore, accessibility. Reducing visual noise and improving text clarity is especially helpful for users with [dyslexia](https://en.wikipedia.org/wiki/Dyslexia "External link (opens in new tab)")
 or low vision.

In the writing systems of some languages, [overlines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#overline)
 and [underlines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#underline)
 carry semantic meaning. CSS lets you adapt styling to cultural norms. Text decoration features are especially useful for languages that do not use Latin-based scripts and instead follow different underline placements, such as Japanese and Korean.

Text decoration features also enable you to follow editorial and localization standards that come from print media. For example, with a strikethrough (line-through), you can indicate the status of content. Use it to inform users that content has been removed or that prices have been halved. This feature lets you present both the original and the updated content. Overlines or double underlines are commonly used for academic and editorial annotations.

[Text decoration in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#text_decoration_in_action)

-------------------------------------------------------------------------------------------------------------------------------

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#reference)

-----------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#properties)

*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-decoration-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset)
    
*   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    
*   [`text-decoration-skip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip)
    
*   [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
    
*   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    
*   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    
*   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    
*   [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    
*   [`text-emphasis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
    
*   [`text-emphasis-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    
*   [`text-underline-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
    

The specification also defines the `text-decoration-skip-box`, `text-decoration-skip-self`, `text-decoration-skip-spaces`, and `text-emphasis-skip` properties, which are not yet supported by any browser.

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#guides)

-----------------------------------------------------------------------------------------

[Introduction to text shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/Text_shadows)

Overview of the components of the [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
 property and creating multiple text shadows

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#related_concepts)

-------------------------------------------------------------------------------------------------------------

*   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    
*   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    
*   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`drop-shadow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
    
*   [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
    
*   [`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
    
*   [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    
*   [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
    
*   [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    
*   [`font-kerning`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    
*   [`ruby-overhang`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang)
    
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    
*   [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
    
*   [Inline formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Inline_layout/Inline_formatting_context)
    
*   [Introduction to formatting contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Formatting_contexts#inline_formatting_contexts)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3](https://drafts.csswg.org/css-text-decor/) |
| [CSS Text Decoration Module Level 4](https://drafts.csswg.org/css-text-decor-4/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration#see_also)

---------------------------------------------------------------------------------------------

*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module
*   [CSS writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 17, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/text_decoration/index.md?plain=1 "Folder: en-us/web/css/guides/text_decoration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText_decoration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ftext_decoration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText_decoration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ftext_decoration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc5c748631460fdad4eaba40349ece8408fe24195%0A*+Document+last+modified%3A+2025-11-17T09%3A15%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
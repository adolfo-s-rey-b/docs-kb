*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#mdn-search)
    

`scrollbar-gutter` CSS property
===============================

Baseline 2024

Newly available

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scrollbar-gutter`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows authors to reserve space for the scrollbar, preventing unwanted layout changes as the content grows while also avoiding unnecessary visuals when scrolling isn't needed.

An element's _scrollbar gutter_ is the space between the inner border edge and the outer padding edge, where the browser may display a scrollbar. If no scrollbar is present, the gutter will be painted as an extension of the padding.

The browser determines whether _classic_ scrollbars or _overlay_ scrollbars are used:

*   Classic scrollbars are always placed in a gutter, consuming space when present.
*   Overlay scrollbars are placed over the content, not in a gutter, and are usually partially transparent.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#syntax)

--------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#auto)

The initial value. Classic scrollbars create a gutter when `overflow` is `scroll`, or when `overflow` is `auto` and the box is overflowing. Overlay scrollbars do not consume space.

[`stable`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#stable)

When using classic scrollbars, the gutter will be present if `overflow` is `auto`, `scroll`, or `hidden` even if the box is not overflowing. When using overlay scrollbars, the gutter will not be present.

[`both-edges`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#both-edges)

If a gutter would be present on one of the inline start/end edges of the box, another will be present on the opposite edge as well.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | scrolling boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

scrollbar-gutter =   
  auto                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stable [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 both-edges[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#examples)

------------------------------------------------------------------------------------------------------------

The examples below show how the different values for the `scrollbar-gutter` property would affect a scrollable `div` element (`.container`) with one or more paragraphs contained within.

**Note:** In the images for the examples, the user's system settings are set to classic scrollbars (always shown).

### [Example 1](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#example_1)

Prevent unneeded layout changes as the content growing or shrinking causes the scrollbar to appear/disappear, a space is reserved for it.

![A containing div element with a paragraph of text inside and a space to the right where the scrollbar is](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter/stable-no-scroll.png)

### [Example 2](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#example_2)

Add symmetric spacing to both sides of the box so the content is centered:

![A containing div element with a paragraph of text inside, a space to the right where the scrollbar is and a matching empty space to the left](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter/stable-both-edges.png)

### [Example 3](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#example_3)

Align the contents of a non-scrolling element and a scrolling one adjacent to it: This example shows two divs side by side. The one on the left has no scroll, but the one on the right does. Both have `scrollbar-gutter` applied, which also reserves space for the div on the left which doesn't have scrollable content. This is a good technique to use to keep the width of content consistent.

![Two adjacent divs containing text, both with space for a scrollbar](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter/side-by-side.png)

### [Overlay scrollbars](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#overlay_scrollbars)

For reference, this image shows the same div as above, but with the user's system settings set to overlay scrollbars. Note here the scrollbar will only show when the user is scrolling and on top of the content, so no space is reserved for it and the `scrollbar-gutter` property has no effect.

![One div with text, no visible scrollbar](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter/for-ref-no-scroll.png)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# scrollbar-gutter-property](https://drafts.csswg.org/css-overflow/#scrollbar-gutter-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter#see_also)

------------------------------------------------------------------------------------------------------------

*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scrollbars styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
    
*   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scrollbar-gutter/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scrollbar-gutter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-gutter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-gutter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-gutter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-gutter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
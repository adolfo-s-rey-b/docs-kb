*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#mdn-search)
    

`::selection` CSS pseudo-element
================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/9)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::selection`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 applies styles to the part of a document that has been highlighted by the user (such as clicking and dragging the mouse across text).

The `::selection` pseudo-element follows a special inheritance model common to all highlight pseudo-elements. For more details on how this inheritance works, see the [Highlight pseudo-elements inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements_inheritance)
 section.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#try_it)

--------------------------------------------------------------------------------------------------

    p::selection {
      color: red;
      background-color: yellow;
    }
    

    <p>
      Select a fragment of this paragraph, to see how its appearance is affected.
    </p>
    

[Allowable properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#allowable_properties)

------------------------------------------------------------------------------------------------------------------------------

Only certain CSS properties can be used with `::selection`:

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     and its associated properties
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`-webkit-text-stroke-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
    , [`-webkit-text-fill-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-fill-color)
     and [`-webkit-text-stroke-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width)
    

In particular, [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 is ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#syntax)

--------------------------------------------------------------------------------------------------

css

    ::selection {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#accessibility)

----------------------------------------------------------------------------------------------------------------

**Don't override selected text styles for purely aesthetic reasons** — users can customize them to suit their needs. For people experiencing cognitive concerns or who are less technologically literate, unexpected changes to selection styles may hurt their understanding of the functionality.

If overridden, it is important to ensure that the **contrast ratio** between the text and background colors of the selection is high enough that people experiencing low vision conditions can read it.

Color contrast ratio is found by comparing the luminosity of the selected text and the selected text background colors. To meet current [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, text content must have a contrast ratio of **4.5:1**, or 3:1 for larger text such as headings. (WCAG defines large text as between `18.66px` and `24px` and [bold](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
, or `24px` or larger.)

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.3 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#examples)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#html)

html

    This text has special styles when you highlight it.
    <p>Also try selecting text in this paragraph.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#css)

    ::-moz-selection {
      color: gold;
      background-color: red;
    }
    
    p::-moz-selection {
      color: white;
      background-color: blue;
    }
    

css

    /* Make selected text gold on a red background */
    ::selection {
      color: gold;
      background-color: red;
    }
    
    /* Make selected text in a paragraph white on a blue background */
    p::selection {
      color: white;
      background-color: blue;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# selectordef-selection](https://drafts.csswg.org/css-pseudo/#selectordef-selection) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection#see_also)

------------------------------------------------------------------------------------------------------

*   [`pointer-events`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
     - control which events are active on the element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_selection/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_selection (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aselection&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_selection%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aselection%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_selection%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
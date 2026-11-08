*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#mdn-search)
    

`rel="alternate stylesheet"` HTML attribute value
=================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/13)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`alternate stylesheet`** keyword pair, when used as a value for the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 attribute of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element, indicates that the target resource is an _alternative style sheet_. Specifying **alternative style sheets** in a web page allows users to see multiple versions of a page based on their needs or preferences.

**Note:** This feature is not well supported in browsers without an extension. To offer alternative presentations that work with a user's existing preferences, see the CSS [media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 and [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
.

Firefox lets users select alternate [stylesheets](https://developer.mozilla.org/en-US/docs/Glossary/Style_sheet)
 using the _View > Page Style_ submenu, which displays the values of the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attributes. Other browsers require an extension to enable this functionality. The web page can also provide its own user interface to let users switch styles.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#examples)

---------------------------------------------------------------------------------------------------------------------

### [Specifying alternate stylesheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#specifying_alternate_stylesheets)

Alternate stylesheets are specified using [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements with `rel="alternate stylesheet"` and `title="…"` attributes. For example:

In this example, the styles "Default Style", "Fancy", and "Basic" will be listed in the Firefox _Page Style_ submenu with "Default Style" pre-selected. When the user selects a different style, the page will immediately be re-rendered using that style sheet.

No matter what style is selected, the rules from the `reset.css` stylesheet will always be applied.

### [Try it out](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#try_it_out)

[Try a working example here](https://mdn.github.io/css-examples/alt-style-sheets/ "External link (opens in new tab)")
.

[Details](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#details)

-------------------------------------------------------------------------------------------------------------------

Any stylesheet in a document falls into one of the following categories:

*   **Persistent** (has `rel="stylesheet"`, no `title=""`): always applies to the document.
*   **Preferred** (has `rel="stylesheet"`, with `title="…"` specified): applied by default, but [disabled](https://developer.mozilla.org/en-US/docs/Web/API/StyleSheet/disabled "disabled")
     if an alternate stylesheet is selected. **There can only be one preferred stylesheet**, so providing stylesheets with different title attributes will cause some of them to be ignored.
*   **Alternate** (`rel="alternate stylesheet"`, with `title="…"` specified): disabled by default, can be selected.

In cases where a stylesheet menu exists, when style sheets are referenced with a `title` attribute on the [<link rel="stylesheet">](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 or [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 element, the title becomes one of the choices offered to the user. Style sheets linked with the same [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 are part of the same choice. Style sheets linked without a `title` attribute are always applied.

Use `rel="stylesheet"` to link to the default style, and `rel="alternate stylesheet"` to link to alternative style sheets. This tells the browser which style sheet title should be selected by default, and makes that default selection apply in browsers that do not support alternate style sheets.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# rel-alternate](https://html.spec.whatwg.org/multipage/links.html#rel-alternate) |
| [HTML  <br>\# the-link-is-an-alternative-stylesheet](https://html.spec.whatwg.org/multipage/links.html#the-link-is-an-alternative-stylesheet) |
| [HTML  <br>\# attr-style-title](https://html.spec.whatwg.org/multipage/semantics.html#attr-style-title) |
| [HTML  <br>\# attr-meta-http-equiv-default-style](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv-default-style) |
| [CSS Object Model (CSSOM)  <br>\# css-style-sheet-collections](https://drafts.csswg.org/cssom/#css-style-sheet-collections) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    
*   [Using dynamic styling information](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model/Using_dynamic_styling_information)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/alternate_stylesheet/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/alternate_stylesheet (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Falternate_stylesheet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Falternate_stylesheet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Falternate_stylesheet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Falternate_stylesheet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa516a9818e8cef06c626d436ee1d73fc6d87ec51%0A*+Document+last+modified%3A+2026-05-11T22%3A57%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
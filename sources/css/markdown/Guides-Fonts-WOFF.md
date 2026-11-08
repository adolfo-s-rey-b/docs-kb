*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#mdn-search)
    

Web Open Font Format (WOFF)
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**WOFF** (the **Web Open Font Format**) is a web font format developed by Mozilla in concert with Type Supply, LettError, and other organizations. It uses a compressed version of the same table-based `sfnt` structure used by TrueType, OpenType, and Open Font Format, but adds metadata and private-use data structures, including predefined fields allowing foundries and vendors to provide license information if desired.

There are three main benefits to using WOFF:

1.  The font data is compressed, so sites using WOFF will use less bandwidth and will load faster than if they used equivalent uncompressed TrueType or OpenType files.
2.  Many font vendors that are unwilling to license their TrueType or OpenType format fonts for use on the web will license WOFF format fonts. This improves availability of fonts to site designers.
3.  Both proprietary and free software browser vendors like the WOFF format, so it has the potential of becoming a truly universal, interoperable font format for the web, unlike other current font formats.

There are two versions of WOFF: WOFF and WOFF2. They mostly differ in regard to the compression algorithm used. In [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 they are identified by the `'woff'` and `'woff2'` format descriptor respectively.

[Using WOFF](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#using_woff)

--------------------------------------------------------------------------------------------

You can use the [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 CSS property to use WOFF fonts for text in web content. It works exactly like OpenType and TrueType format fonts do, except it will likely let your content download more efficiently due to the addition of compression.

[Tools for working with WOFF fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#tools_for_working_with_woff_fonts)

------------------------------------------------------------------------------------------------------------------------------------------

*   [Tools for working with WOFF](https://github.com/odemiral/woff2sfnt-sfnt2woff "External link (opens in new tab)")
     fonts are available. `sfnt2woff` and `woff2sfnt` convert between WOFF and OpenType.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#specifications)

----------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [WOFF File Format 1.0  <br>\# OverallStructure](https://w3c.github.io/woff/woff1/spec/Overview.html#OverallStructure) |
| [WOFF File Format 2.0  <br>\# FileStructure](https://w3c.github.io/woff/woff2/#FileStructure) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#browser_compatibility)

------------------------------------------------------------------------------------------------------------------

### [css.at-rules.font-face.WOFF](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#css.at-rules.font-face.WOFF)

### [css.at-rules.font-face.WOFF\_2](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#css.at-rules.font-face.WOFF_2)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF#see_also)

----------------------------------------------------------------------------------------

*   [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/WOFF/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/fonts/woff/index.md?plain=1 "Folder: en-us/web/css/guides/fonts/woff (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts%2FWOFF&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ffonts%2Fwoff%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts%2FWOFF%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ffonts%2Fwoff%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
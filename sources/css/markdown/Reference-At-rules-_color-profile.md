*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#mdn-search)
    

`@color-profile` CSS at-rule
============================

The **`@color-profile`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 defines and names a color profile which can later be used in the [`color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
 function to specify a color.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#syntax)

----------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#parameters)

[profile name](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#profile_name)

Either a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 or the identifier `device-cmyk`.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#descriptors)

[`src`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#src)

Specifies the URL to retrieve the color-profile information from.

[`rendering-intent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#rendering-intent)

If the color profile contains more than one rendering intent, this descriptor allows one to be selected as the one to use to define how to map the color to smaller [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
s than this profile is defined over.

If used, it must be one of the following keywords:

[`relative-colorimetric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#relative-colorimetric)

Media-relative colorimetric is required to leave source colors that fall inside the destination medium [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
 unchanged relative to the respective media white points. Source colors that are out of the destination medium gamut are mapped to colors on the gamut boundary using a variety of different methods.

[`absolute-colorimetric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#absolute-colorimetric)

ICC-absolute colorimetric is required to leave source colors that fall inside the destination medium [gamut](https://developer.mozilla.org/en-US/docs/Glossary/Gamut)
 unchanged relative to the adopted white (a perfect reflecting diffuser). Source colors that are out of the destination medium gamut are mapped to colors on the gamut boundary using a variety of different methods.

[`perceptual`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#perceptual)

This method is often the preferred choice for images, especially when there are substantial differences between the source and destination (such as a screen display image reproduced on a reflection print). It takes the colors of the source image and re-optimizes the appearance for the destination medium using proprietary methods.

[`saturation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#saturation)

This option was created to preserve the relative saturation (chroma) of the original, and to keep solid colors pure. However, it experienced interoperability problems like the perceptual intent.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#formal_syntax)

------------------------------------------------------------------------------------------------------------------

@color-profile =   
  @color-profile [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 device-cmyk [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#examples)

--------------------------------------------------------------------------------------------------------

This example demonstrates using offset printing to ISO 12647-2:2004 using the CGATS/SWOP TR005 2007 characterization data on grade 5 paper with an ink limit of 300% Total Area Coverage, and medium gray component replacement (GCR). This example is from the specification.

The `src` descriptor specifies the URL to retrieve the color-profile information from.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# at-profile](https://www.w3.org/TR/css-color-5/#at-profile) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile#see_also)

--------------------------------------------------------------------------------------------------------

*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@color-profile/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@color-profile (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40color-profile&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40color-profile%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40color-profile%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40color-profile%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
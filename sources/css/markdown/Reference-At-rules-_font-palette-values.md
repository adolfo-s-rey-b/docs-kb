*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#mdn-search)
    

`@font-palette-values` CSS at-rule
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@font-palette-values`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 allows you to customize the default values of [font-palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
 created by the font-maker.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#syntax)

----------------------------------------------------------------------------------------------------------

css

    @font-palette-values --identifier {
      font-family: "Bixa";
    }
    .my-class {
      font-palette: --identifier;
    }
    

The [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 is a user-defined identifier, that while it looks like a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
 behaves in a different way and is not wrapped in a [CSS var() function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#descriptors)

[`base-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)

Specifies the name or index of the base-palette, created by the font-maker, to use.

[`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)

Specifies the name of the font family that this palette can be applied to. A `font-family` name is required for the `@font-palette-values` rule to be valid.

[`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)

Specifies the colors in the base palette to override.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

@font-palette-values =   
  @font-palette-values [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#examples)

--------------------------------------------------------------------------------------------------------------

### [Overriding colors in an existing palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#overriding_colors_in_an_existing_palette)

This example shows how you can change some or all of the colors in a color font.

#### HTML

html

    <p>default colors</p>
    <p class="alternate">alternate colors</p>
    

#### CSS

css

    @import "https://fonts.googleapis.com/css2?family=Bungee+Spice";
    p {
      font-family: "Bungee Spice", fantasy;
      font-size: 2rem;
    }
    @font-palette-values --Alternate {
      font-family: "Bungee Spice";
      override-colors:
        0 #00ffbb,
        1 #007744;
    }
    .alternate {
      font-palette: --Alternate;
    }
    

#### Result

When overriding colors of the normal or base-palette at index 0 you do not need to declare which base-palette to use. This should only be done when overriding a different base-palette. If you are overriding all the colors then there is also no need to specify the base-palette to use.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# at-ruledef-font-palette-values](https://drafts.csswg.org/css-fonts/#at-ruledef-font-palette-values) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
     property
*   [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
     descriptor
*   [`base-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
     descriptor
*   [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
     descriptor
*   [`CSSFontPaletteValuesRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFontPaletteValuesRule)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-palette-values/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-palette-values (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-palette-values%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-palette-values%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd571e753a6e1aa3f37c775f0308690bc738cdbe6%0A*+Document+last+modified%3A+2026-09-12T19%3A13%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#mdn-search)
    

`@font-feature-values` CSS at-rule
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@font-feature-values`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 lets you use a common name in the [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
 property for features activated differently in OpenType. This can help simplify your CSS when using multiple fonts.

The `@font-feature-values` at-rule may be used either at the top level of your CSS or inside any CSS conditional-group at-rule.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#syntax)

----------------------------------------------------------------------------------------------------------

Each `@font-feature-values` block can contain a list of feature value blocks (listed below), as well as the [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display)
 descriptor.

### [Feature value blocks](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#feature_value_blocks)

[`@swash`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#swash)

Specifies a feature name that will work with the [`swash()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#swash)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. A swash feature value definition allows only one value: `ident1: 2` is valid, but `ident2: 2 4` isn't.

[`@annotation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#annotation)

Specifies a feature name that will work with the [`annotation()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#annotation)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. An annotation feature value definition allows only one value: `ident1: 2` is valid, but `ident2: 2 4` isn't.

[`@ornaments`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#ornaments)

Specifies a feature name that will work with the [`ornaments()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#ornaments)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. An ornaments feature value definition allows only one value: `ident1: 2` is valid, but `ident2: 2 4` isn't.

[`@stylistic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#stylistic)

Specifies a feature name that will work with the [`stylistic()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#stylistic)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. A stylistic feature value definition allows only one value: `ident1: 2` is valid, but `ident2: 2 4` isn't.

[`@styleset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#styleset)

Specifies a feature name that will work with the [`styleset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#styleset)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. A styleset feature value definition allows an unlimited number of values: `ident1: 2 4 12 1` maps to the OpenType values `ss02`, `ss04`, `ss12`, and `ss01`. Note that values higher than `99` are valid, but don't map to any OpenType values and are ignored.

[`@character-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#character-variant)

Specifies a feature name that will work with the [`character-variant()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#character-variant)
 functional notation of [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
. A character-variant feature value definition allows either one or two values: `ident1: 3` maps to `cv03=1`, and `ident2: 2 4` maps to `cv02=4`, but `ident2: 2 4 5` is invalid.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

@font-feature-values =   
  @font-feature-values <font-family-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 { <declaration-rule-list> }    
  
<font-family-name> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#examples)

--------------------------------------------------------------------------------------------------------------

### [Using @styleset in a @font-feature-values rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#using_styleset_in_a_font-feature-values_rule)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-feature-values](https://drafts.csswg.org/css-fonts/#font-feature-values) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values#see_also)

--------------------------------------------------------------------------------------------------------------

*   The [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
     property that uses values that this at-rule defines.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@font-feature-values/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@font-feature-values (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-feature-values&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-feature-values%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40font-feature-values%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40font-feature-values%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
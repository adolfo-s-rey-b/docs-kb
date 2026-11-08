*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#mdn-search)
    

`font-variant-alternates` CSS property
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-alternates`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls the usage of alternate glyphs. These alternate glyphs may be referenced by alternative names defined in [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
.

The [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
 at-rule can be used to associate, for a given font face, a human-readable name with a numeric index that controls a particular OpenType font feature. For features that select alternative glyphs (`stylistic`, `styleset`, `character-variant`, `swash`, `ornament` or `annotation`), the `font-variant-alternates` property can then reference the human-readable name in order to apply the associated feature.

This allows CSS rules to enable alternative glyphs without needing to know the specific index values that a particular font uses to control them.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-variant-alternates: normal;
    font-variant-alternates: historical-forms;
    
    /* Functional notation values */
    font-variant-alternates: stylistic(user-defined-ident);
    font-variant-alternates: styleset(user-defined-ident);
    font-variant-alternates: character-variant(user-defined-ident);
    font-variant-alternates: swash(user-defined-ident);
    font-variant-alternates: ornaments(user-defined-ident);
    font-variant-alternates: annotation(user-defined-ident);
    font-variant-alternates: swash(ident1) annotation(ident2);
    
    /* Global values */
    font-variant-alternates: inherit;
    font-variant-alternates: initial;
    font-variant-alternates: revert;
    font-variant-alternates: revert-layer;
    font-variant-alternates: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#values)

This property is specified as `normal` or as a space-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#normal)

This keyword deactivates alternate glyphs.

[`historical-forms`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#historical-forms)

This keyword enables historical forms — glyphs that were common in the past but not today. It corresponds to the OpenType value `hist`.

[`stylistic()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#stylistic)

This function enables stylistic alternates for individual characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `salt`, like `salt 2`.

[`styleset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#styleset)

This function enables stylistic alternatives for sets of characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ssXY`, like `ss02`.

[`character-variant()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#character-variant)

This function enables specific stylistic alternatives for characters. It is similar to `styleset()`, but doesn't create coherent glyphs for a set of characters; individual characters will have independent and not necessarily coherent styles. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `cvXY`, like `cv02`.

[`swash()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#swash)

This function enables [swash](https://en.wikipedia.org/wiki/Swash_%28typography%29 "External link (opens in new tab)")
 glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType values `swsh` and `cswh`, like `swsh 2` and `cswh 2`.

[`ornaments()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#ornaments)

This function enables ornaments, like [fleurons](https://en.wikipedia.org/wiki/Fleuron_%28typography%29 "External link (opens in new tab)")
 and other dingbat glyphs. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `ornm`, like `ornm 2`.

**Note:** In order to preserve text semantics, font designers should include ornaments that don't match Unicode dingbat characters as ornamental variants of the bullet character (U+2022). Be aware that some existing fonts don't follow this advice.

[`annotation()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#annotation)

This function enables annotations, like circled digits or inverted characters. The parameter is a font-specific name mapped to a number. It corresponds to the OpenType value `nalt`, like `nalt 2`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

font-variant-alternates =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 stylistic( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 historical-forms [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 styleset( <font-feature-value-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")\
 ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 character-variant( <font-feature-value-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")\
 ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 swash( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ornaments( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 annotation( <font-feature-value-name> ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<font-feature-value-name> =   
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#examples)

-------------------------------------------------------------------------------------------------------------------

### [Enabling swash glyphs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#enabling_swash_glyphs)

In this example, we use the `@font-feature-values` at-rule to define a name for the `swash` feature of the [MonteCarlo](https://github.com/googlefonts/monte-carlo "External link (opens in new tab)")
 font. The rule maps the name `"fancy"` to the index value `1`.

We can then use that name inside `font-variant-alternates` to switch on swashes for that font. This is the equivalent of a line like `font-feature-settings: "swsh" 1`, except that the CSS applying the feature does not need to include, or even know, the index value needed for this particular font.

#### HTML

html

    <p>A Fancy Swash</p>
    <p class="variant">A Fancy Swash</p>
    

#### CSS

css

    @font-face {
      font-family: "MonteCarlo";
      src: url("/shared-assets/fonts/monte-carlo/monte-carlo-regular.woff2");
    }
    
    @font-feature-values "MonteCarlo" {
      @swash {
        fancy: 1;
      }
    }
    
    p {
      font-family: "MonteCarlo", cursive;
      font-size: 3rem;
      margin: 0.7rem 3rem;
    }
    
    .variant {
      font-variant-alternates: swash(fancy);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-alternates-prop](https://drafts.csswg.org/css-fonts/#font-variant-alternates-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    
*   [`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
    
*   [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-alternates/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-alternates (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-alternates&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-alternates%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-alternates%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-alternates%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa5531a7b1fa30ab1de952ffff619a9830eb1c1a9%0A*+Document+last+modified%3A+2026-08-11T19%3A18%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
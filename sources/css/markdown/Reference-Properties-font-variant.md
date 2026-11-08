*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#mdn-search)
    

`font-variant` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property allows you to set all the font variants for a font.

You can also set the `<font-variant-css2>` values of `font-variant` defined in CSS Level 2.1, (that is, `normal` or `small-caps`), by using the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#try_it)

----------------------------------------------------------------------------------------------------

    font-variant: normal;
    

    font-variant: no-common-ligatures proportional-nums;
    

    font-variant: common-ligatures tabular-nums;
    

    font-variant: small-caps slashed-zero;
    

    <section id="default-example">
      <div id="example-element">
        <p>Difficult waffles</p>
        <table>
          <tbody>
            <tr>
              <td><span class="tabular">0O</span></td>
            </tr>
            <tr>
              <td><span class="tabular">3.14</span></td>
            </tr>
            <tr>
              <td><span class="tabular">2.71</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
    

    @font-face {
      font-family: "Fira Sans";
      src:
        local("FiraSans-Regular"),
        url("/shared-assets/fonts/FiraSans-Regular.woff2") format("woff2");
      font-weight: normal;
      font-style: normal;
    }
    
    section {
      font-family: "Fira Sans", sans-serif;
      margin-top: 10px;
      font-size: 1.5em;
    }
    
    #example-element table {
      margin-left: auto;
      margin-right: auto;
    }
    
    .tabular {
      border: 1px solid;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#syntax)

----------------------------------------------------------------------------------------------------

css

    font-variant: small-caps;
    font-variant: common-ligatures small-caps;
    
    /* Global values */
    font-variant: inherit;
    font-variant: initial;
    font-variant: revert;
    font-variant: revert-layer;
    font-variant: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#values)

This property is specified as a space-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#normal)

Specifies a normal font face. Each longhand property has an initial value of `normal`.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#none)

Sets the value of the [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
 as `none` and the values of the other longhand properties as `normal`, their initial value.

[`<common-lig-values>`, `<discretionary-lig-values>`, `<historical-lig-values>`, `<contextual-alt-values>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#common-lig-values)

Specifies the keywords related to the [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
 longhand property. The possible values are `common-ligatures`, `no-common-ligatures`, `discretionary-ligatures`, `no-discretionary-ligatures`, `historical-ligatures`, `no-historical-ligatures`, `contextual`, and `no-contextual`.

[`stylistic()`, `historical-forms`, `styleset()`, `character-variant()`, `swash()`, `ornaments()`, `annotation()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#stylistic)

Specifies the keywords and functions related to the [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
 longhand property.

[`small-caps`, `all-small-caps`, `petite-caps`, `all-petite-caps`, `unicase`, `titling-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#small-caps)

Specifies the keywords and functions related to the [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
 longhand property. The `small-caps` value is the only non-`normal` font variant valid within the [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 shorthand property.

[`<numeric-figure-values>`, `<numeric-spacing-values>`, `<numeric-fraction-values>`, `ordinal`, `slashed-zero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#numeric-figure-values)

Specifies the keywords related to the [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
 longhand property. The possible values are `lining-nums`, `oldstyle-nums`, `proportional-nums`, `tabular-nums`, `diagonal-fractions`, `stacked-fractions`, `ordinal`, and `slashed-zero`.

[`<east-asian-variant-values>`, `<east-asian-width-values>`, `ruby`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#east-asian-variant-values)

Specifies the keywords related to the [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
 longhand property. The possible values are `jis78`, `jis83`, `jis90`, `jis04`, `simplified`, `traditional`, `full-width`, `proportional-width`, and `ruby`.

[`sub`, `super`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#sub)

Specifies the keywords and functions related to the [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
 longhand property.

[`text`, `emoji`, `unicode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#text)

Specifies the keywords and functions related to the [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
 longhand property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#formal_syntax)

------------------------------------------------------------------------------------------------------------------

font-variant =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <common-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <discretionary-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <historical-lig-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <contextual-alt-values> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 small-caps [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 all-small-caps [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 petite-caps [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 all-petite-caps [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 unicase [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 titling-caps [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 stylistic( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 historical-forms [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 styleset( <font-feature-value-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")\
 ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 character-variant( <font-feature-value-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")\
 ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 swash( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ornaments( <font-feature-value-name> ) [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 annotation( <font-feature-value-name> ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <numeric-figure-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <numeric-spacing-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <numeric-fraction-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ordinal [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 slashed-zero [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <east-asian-variant-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <east-asian-width-values> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 ruby [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 sub [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 super [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 text [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 emoji [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 unicode [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<common-lig-values> =   
  common-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-common-ligatures    
  
<discretionary-lig-values> =   
  discretionary-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-discretionary-ligatures    
  
<historical-lig-values> =   
  historical-ligatures     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-historical-ligatures    
  
<contextual-alt-values> =   
  contextual     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-contextual    
  
<font-feature-value-name> =   
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
  
<numeric-figure-values> =   
  lining-nums    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  oldstyle-nums    
  
<numeric-spacing-values> =   
  proportional-nums  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  tabular-nums         
  
<numeric-fraction-values> =   
  diagonal-fractions  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stacked-fractions     
  
<east-asian-variant-values> =   
  jis78        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis83        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis90        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jis04        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  simplified   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  traditional    
  
<east-asian-width-values> =   
  full-width          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  proportional-width    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#examples)

--------------------------------------------------------------------------------------------------------

### [Setting the small-caps font variant](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#setting_the_small-caps_font_variant)

#### HTML

html

    <p class="normal">Firefox rocks!</p>
    <p class="small">Firefox rocks!</p>
    

#### CSS

css

    p.normal {
      font-variant: normal;
    }
    p.small {
      font-variant: small-caps;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-prop](https://drafts.csswg.org/css-fonts/#font-variant-prop) |
| [Scalable Vector Graphics (SVG) 2  <br>\# FontVariantProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#FontVariantProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant#see_also)

--------------------------------------------------------------------------------------------------------

*   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    
*   [`text-combine-upright`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    
*   [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    
*   SVG [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-variant)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
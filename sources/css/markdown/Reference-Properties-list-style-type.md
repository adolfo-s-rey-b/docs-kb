*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#mdn-search)
    

`list-style-type` CSS property
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`list-style-type`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the marker (such as a disc, character, or custom counter style) of a list item element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#try_it)

-------------------------------------------------------------------------------------------------------

    list-style-type: space-counter;
    

    list-style-type: disc;
    

    list-style-type: circle;
    

    list-style-type: "\1F44D";
    

    <section class="default-example" id="default-example">
      <div>
        <p>NASA Notable Missions</p>
        <ul class="transition-all unhighlighted" id="example-element">
          <li>Apollo</li>
          <li>Hubble</li>
          <li>Chandra</li>
          <li>Cassini-Huygens</li>
        </ul>
      </div>
      <hr />
      <div class="note">
        <p>
          <code>space-counter</code> is defined with
          <a
            href="//developer.mozilla.org/docs/Web/CSS/Reference/At-rules/@counter-style"
            target="_parent"
            ><code>@counter-style</code></a
          >
        </p>
      </div>
    </section>
    

    .default-example {
      font-size: 1.2rem;
    }
    
    #example-element {
      width: 100%;
      background: #be094b;
      color: white;
    }
    
    section {
      text-align: left;
      flex-direction: column;
    }
    
    hr {
      width: 50%;
      color: lightgray;
      margin: 0.5em;
    }
    
    .note {
      font-size: 0.8rem;
    }
    
    .note a {
      color: #009e5f;
    }
    
    @counter-style space-counter {
      symbols: "\1F680" "\1F6F8" "\1F6F0" "\1F52D";
      suffix: " ";
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Partial list of types */
    list-style-type: disc;
    list-style-type: circle;
    list-style-type: square;
    list-style-type: decimal;
    list-style-type: georgian;
    list-style-type: trad-chinese-informal;
    list-style-type: kannada;
    
    /* <string> value */
    list-style-type: "-";
    
    /* Identifier matching an @counter-style rule */
    list-style-type: custom-counter-style;
    
    /* Keyword value */
    list-style-type: none;
    
    /* Global values */
    list-style-type: inherit;
    list-style-type: initial;
    list-style-type: revert;
    list-style-type: revert-layer;
    list-style-type: unset;
    

The `list-style-type` property may be defined as any one of:

*   a `<custom-ident>` value,
*   a `symbols()` value,
*   a `<string>` value, or
*   the keyword `none`.

Note that:

*   Some types require a suitable font installed to display as expected.
*   The `cjk-ideographic` is identical to `trad-chinese-informal`; it exists for legacy reasons.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#values)

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

An identifier matching the value of a [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 or one of the predefined styles:

[`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)

Defines an anonymous style of the list.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

The specified string will be used as the item's marker.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#none)

No item marker is shown.

[`disc`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#disc)

A filled circle (default value).

[`circle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#circle)

A hollow circle.

[`square`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#square)

A filled square.

[`decimal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#decimal)

Decimal numbers, beginning with 1.

[`cjk-decimal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#cjk-decimal)

Han decimal numbers.

[`decimal-leading-zero`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#decimal-leading-zero)

Decimal numbers, padded by initial zeros.

[`lower-roman`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lower-roman)

Lowercase roman numerals.

[`upper-roman`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#upper-roman)

Uppercase roman numerals.

[`lower-greek`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lower-greek)

Lowercase classical Greek.

[`lower-alpha`, `lower-latin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lower-alpha)

Lowercase [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 letters.

[`upper-alpha`, `upper-latin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#upper-alpha)

Uppercase ASCII letters.

[`arabic-indic`, `-moz-arabic-indic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#arabic-indic)

Arabic-Indic numbers.

[`armenian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#armenian)

Traditional Armenian numbering.

[`bengali`, `-moz-bengali`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#bengali)

Bengali numbering.

[`cambodian`/`khmer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#cambodian)

Cambodian/Khmer numbering.

[`cjk-earthly-branch`, `-moz-cjk-earthly-branch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#cjk-earthly-branch)

Han "Earthly Branch" ordinals.

[`cjk-heavenly-stem`, `-moz-cjk-heavenly-stem`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#cjk-heavenly-stem)

Han "Heavenly Stem" ordinals.

[`cjk-ideographic`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#cjk-ideographic)

Identical to `trad-chinese-informal`.

[`devanagari`, `-moz-devanagari`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#devanagari)

Devanagari numbering.

[`ethiopic-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#ethiopic-numeric)

Ethiopic numbering.

[`georgian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#georgian)

Traditional Georgian numbering.

[`gujarati`, `-moz-gujarati`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#gujarati)

Gujarati numbering.

[`gurmukhi`, `-moz-gurmukhi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#gurmukhi)

Gurmukhi numbering.

[`hebrew`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#hebrew)

Traditional Hebrew numbering.

[`hiragana`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#hiragana)

Dictionary-order hiragana lettering.

[`hiragana-iroha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#hiragana-iroha)

[Iroha-order](https://en.wikipedia.org/wiki/Iroha "External link (opens in new tab)")
 hiragana lettering.

[`japanese-formal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#japanese-formal)

Japanese formal numbering to be used in legal or financial documents. The kanjis are designed so that they can't be modified to look like another correct one.

[`japanese-informal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#japanese-informal)

Japanese informal numbering.

[`kannada`, `-moz-kannada`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#kannada)

Kannada numbering.

[`katakana`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#katakana)

Dictionary-order katakana lettering.

[`katakana-iroha`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#katakana-iroha)

[Iroha-order](https://en.wikipedia.org/wiki/Iroha "External link (opens in new tab)")
 katakana lettering.

[`korean-hangul-formal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#korean-hangul-formal)

Korean hangul numbering.

[`korean-hanja-formal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#korean-hanja-formal)

Formal Korean Han numbering.

[`korean-hanja-informal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#korean-hanja-informal)

Korean hanja numbering.

[`lao`, `-moz-lao`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lao)

Laotian numbering.

[`lower-armenian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#lower-armenian)

Lowercase Armenian numbering.

[`malayalam`, `-moz-malayalam`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#malayalam)

Malayalam numbering.

[`mongolian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#mongolian)

Mongolian numbering.

[`myanmar`, `-moz-myanmar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#myanmar)

Myanmar (Burmese) numbering.

[`oriya`, `-moz-oriya`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#oriya)

Oriya numbering.

[`persian`, `-moz-persian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#persian)

Persian numbering.

[`simp-chinese-formal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#simp-chinese-formal)

Simplified Chinese formal numbering.

[`simp-chinese-informal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#simp-chinese-informal)

Simplified Chinese informal numbering.

[`tamil`, `-moz-tamil`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#tamil)

Tamil numbering.

[`telugu`, `-moz-telugu`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#telugu)

Telugu numbering.

[`thai`, `-moz-thai`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#thai)

Thai numbering.

[`tibetan`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#tibetan)

Tibetan numbering.

[`trad-chinese-formal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#trad-chinese-formal)

Traditional Chinese formal numbering.

[`trad-chinese-informal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#trad-chinese-informal)

Traditional Chinese informal numbering.

[`upper-armenian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#upper-armenian)

Traditional uppercase Armenian numbering.

[`disclosure-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#disclosure-open)

Symbol indicating that a disclosure widget such as [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 is opened.

[`disclosure-closed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#disclosure-closed)

Symbol indicating that a disclosure widget, like [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 is closed.

Refer to the [All list style types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#all_list_style_types)
 example to see the above values in action. Details of all the available counter styles used by various cultures around the world can be found in [Ready-made Counter Styles](https://w3c.github.io/predefined-counter-styles/ "External link (opens in new tab)")
.

### [Non-standard extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#non-standard_extensions)

Mozilla (Firefox) supports a few predefined types with a `-moz-` prefix.

*   `ethiopic-halehame`: `-moz-ethiopic-halehame`
*   `ethiopic-halehame-am`: `-moz-ethiopic-halehame-am`
*   `ethiopic-halehame-ti-er`: `-moz-ethiopic-halehame-ti-er`
*   `ethiopic-halehame-ti-et`: `-moz-ethiopic-halehame-ti-et`
*   `ethiopic-numeric`: `-moz-ethiopic-numeric`
*   `hangul`: `-moz-hangul`
*   `hangul-consonant`: `-moz-hangul-consonant`
*   `urdu`: `-moz-urdu`

See the [compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#browser_compatibility)
 to check which browsers support which extension.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#description)

-----------------------------------------------------------------------------------------------------------------

The `list-style-type` property sets the marker (such as a disc, character, or custom counter style) of a list item element. The marker will be [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
, the same as the computed [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 of the element it applies to.

Only a few elements ([`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 and [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary)
) have a default value of `display: list-item`. However, the `list-style-type` property may be applied to any element whose [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value is set to `list-item`.

### [List style inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#list_style_inheritance)

Because `list-style-type` is inherited, it can be set on a parent element (commonly [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 or [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
) to make it apply to its list items. However, user-agent stylesheets set `list-style-type` on `<ul>`, `<ol>`, and [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)
 elements, so nested lists use these default values instead of inheriting the ancestor list's value. To make nested lists inherit this value, set `list-style-type: inherit` on the nested list elements.

For example, in cases like this:

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>
        Three
        <ul>
          <li>Four</li>
          <li>Five</li>
          <li>Six</li>
        </ul>
      </li>
    </ul>
    

Where a custom style is set on the outer list:

css

    body > ul {
      list-style-type: square;
    }
    

The inner list won't inherit the custom style unless you set it to inherit:

css

    ul ul {
      list-style-type: inherit;
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#accessibility)

---------------------------------------------------------------------------------------------------------------------

Safari will not recognize an ordered or unordered list as a list in the accessibility tree if it has a `list-style-type` value of `none`. This can be resolved by adding `role="list"` to the list's opening tag. To learn more about this and potential workarounds, see [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style#accessibility)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `disc` |
| Applies to | list items |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

list-style-type =   
  <counter-style>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none               
  
<counter-style> =   
  <counter-style-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <symbols()>             
  
<counter-style-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
[<symbols()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
 =   
  symbols( <symbols-type>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <image> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 )    
  
<symbols-type> =   
  cyclic      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  numeric     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  alphabetic  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  symbolic    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fixed         
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#examples)

-----------------------------------------------------------------------------------------------------------

### [Setting list item markers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#setting_list_item_markers)

#### HTML

html

    List 1
    <ol class="normal">
      <li>Hello</li>
      <li>World</li>
      <li>What's up?</li>
    </ol>
    
    List 2
    <ol class="shortcut">
      <li>Looks</li>
      <li>Like</li>
      <li>The</li>
      <li>Same</li>
    </ol>
    

#### CSS

css

    ol.normal {
      list-style-type: upper-alpha;
    }
    
    /* or use the shortcut "list-style": */
    ol.shortcut {
      list-style: upper-alpha;
    }
    

#### Result

### [All list style types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#all_list_style_types)

#### HTML

html

    <ol>
      <li>Apollo</li>
      <li>Hubble</li>
      <li>Chandra</li>
      <li>Cassini-Huygens</li>
      <li>Spitzer</li>
    </ol>
    
    <h2>Choose a list style type:</h2>
    
    <div class="container">
      <label for="disc">
        <input type="radio" id="disc" name="type" value="disc" />disc
      </label>
    
      <label for="circle">
        <input type="radio" id="circle" name="type" value="circle" />circle
      </label>
    
      <label for="square">
        <input type="radio" id="square" name="type" value="square" />square
      </label>
    
      <label for="decimal">
        <input type="radio" id="decimal" name="type" value="decimal" />decimal
      </label>
    
      <label for="cjk-decimal">
        <input
          type="radio"
          id="cjk-decimal"
          name="type"
          value="cjk-decimal" />cjk-decimal
      </label>
    
      <label for="decimal-leading-zero">
        <input
          type="radio"
          id="decimal-leading-zero"
          name="type"
          value="decimal-leading-zero" />decimal-leading-zero
      </label>
    
      <label for="lower-roman">
        <input
          type="radio"
          id="lower-roman"
          name="type"
          value="lower-roman" />lower-roman
      </label>
    
      <label for="upper-roman">
        <input
          type="radio"
          id="upper-roman"
          name="type"
          value="upper-roman" />upper-roman
      </label>
    
      <label for="lower-greek">
        <input
          type="radio"
          id="lower-greek"
          name="type"
          value="lower-greek" />lower-greek
      </label>
    
      <label for="lower-alpha">
        <input
          type="radio"
          id="lower-alpha"
          name="type"
          value="lower-alpha" />lower-alpha, lower-latin
      </label>
    
      <label for="upper-alpha">
        <input
          type="radio"
          id="upper-alpha"
          name="type"
          value="upper-alpha" />upper-alpha, upper-latin
      </label>
    
      <label for="arabic-indic">
        <input
          type="radio"
          id="arabic-indic"
          name="type"
          value="arabic-indic" />arabic-indic
      </label>
    
      <label for="armenian">
        <input type="radio" id="armenian" name="type" value="armenian" />armenian
      </label>
    
      <label for="bengali">
        <input type="radio" id="bengali" name="type" value="bengali" />bengali
      </label>
    
      <label for="cambodian">
        <input type="radio" id="cambodian" name="type" value="cambodian" />cambodian
      </label>
    
      <label for="cjk-earthly-branch">
        <input
          type="radio"
          id="cjk-earthly-branch"
          name="type"
          value="cjk-earthly-branch" />cjk-earthly-branch
      </label>
    
      <label for="cjk-heavenly-stem">
        <input
          type="radio"
          id="cjk-heavenly-stem"
          name="type"
          value="cjk-heavenly-stem" />cjk-heavenly-stem
      </label>
    
      <label for="cjk-ideographic">
        <input
          type="radio"
          id="cjk-ideographic"
          name="type"
          value="cjk-ideographic" />cjk-ideographic
      </label>
    
      <label for="devanagari">
        <input
          type="radio"
          id="devanagari"
          name="type"
          value="devanagari" />devanagari
      </label>
    
      <label for="ethiopic-numeric">
        <input
          type="radio"
          id="ethiopic-numeric"
          name="type"
          value="ethiopic-numeric" />ethiopic-numeric
      </label>
    
      <label for="georgian">
        <input type="radio" id="georgian" name="type" value="georgian" />georgian
      </label>
    
      <label for="gujarati">
        <input type="radio" id="gujarati" name="type" value="gujarati" />gujarati
      </label>
    
      <label for="gurmukhi">
        <input type="radio" id="gurmukhi" name="type" value="gurmukhi" />gurmukhi
      </label>
    
      <label for="hebrew">
        <input type="radio" id="hebrew" name="type" value="hebrew" />hebrew
      </label>
    
      <label for="hiragana">
        <input type="radio" id="hiragana" name="type" value="hiragana" />hiragana
      </label>
    
      <label for="hiragana-iroha">
        <input
          type="radio"
          id="hiragana-iroha"
          name="type"
          value="hiragana-iroha" />hiragana-iroha
      </label>
    
      <label for="japanese-formal">
        <input
          type="radio"
          id="japanese-formal"
          name="type"
          value="japanese-formal" />japanese-formal
      </label>
    
      <label for="japanese-informal">
        <input
          type="radio"
          id="japanese-informal"
          name="type"
          value="japanese-informal" />japanese-informal
      </label>
    
      <label for="kannada">
        <input type="radio" id="kannada" name="type" value="kannada" />kannada
      </label>
    
      <label for="katakana">
        <input type="radio" id="katakana" name="type" value="katakana" />katakana
      </label>
    
      <label for="katakana-iroha">
        <input
          type="radio"
          id="katakana-iroha"
          name="type"
          value="katakana-iroha" />katakana-iroha
      </label>
    
      <label for="khmer">
        <input type="radio" id="khmer" name="type" value="khmer" />khmer
      </label>
    
      <label for="korean-hangul-formal">
        <input
          type="radio"
          id="korean-hangul-formal"
          name="type"
          value="korean-hangul-formal" />korean-hangul-formal
      </label>
    
      <label for="korean-hanja-formal">
        <input
          type="radio"
          id="korean-hanja-formal"
          name="type"
          value="korean-hanja-formal" />korean-hanja-formal
      </label>
    
      <label for="korean-hanja-informal">
        <input
          type="radio"
          id="korean-hanja-informal"
          name="type"
          value="korean-hanja-informal" />korean-hanja-informal
      </label>
    
      <label for="lao">
        <input type="radio" id="lao" name="type" value="lao" />lao
      </label>
    
      <label for="lower-armenian">
        <input
          type="radio"
          id="lower-armenian"
          name="type"
          value="lower-armenian" />lower-armenian
      </label>
    
      <label for="malayalam">
        <input type="radio" id="malayalam" name="type" value="malayalam" />malayalam
      </label>
    
      <label for="mongolian">
        <input type="radio" id="mongolian" name="type" value="mongolian" />mongolian
      </label>
    
      <label for="myanmar">
        <input type="radio" id="myanmar" name="type" value="myanmar" />myanmar
      </label>
    
      <label for="oriya">
        <input type="radio" id="oriya" name="type" value="oriya" />oriya
      </label>
    
      <label for="persian">
        <input type="radio" id="persian" name="type" value="persian" />persian
      </label>
    
      <label for="simp-chinese-formal">
        <input
          type="radio"
          id="simp-chinese-formal"
          name="type"
          value="simp-chinese-formal" />simp-chinese-formal
      </label>
    
      <label for="simp-chinese-informal">
        <input
          type="radio"
          id="simp-chinese-informal"
          name="type"
          value="simp-chinese-informal" />simp-chinese-informal
      </label>
    
      <label for="tamil">
        <input type="radio" id="tamil" name="type" value="tamil" />tamil
      </label>
    
      <label for="telugu">
        <input type="radio" id="telugu" name="type" value="telugu" />telugu
      </label>
    
      <label for="thai">
        <input type="radio" id="thai" name="type" value="thai" />thai
      </label>
    
      <label for="tibetan">
        <input type="radio" id="tibetan" name="type" value="tibetan" />tibetan
      </label>
    
      <label for="trad-chinese-formal">
        <input
          type="radio"
          id="trad-chinese-formal"
          name="type"
          value="trad-chinese-formal" />trad-chinese-formal
      </label>
    
      <label for="trad-chinese-informal">
        <input
          type="radio"
          id="trad-chinese-informal"
          name="type"
          value="trad-chinese-informal" />trad-chinese-informal
      </label>
    
      <label for="upper-armenian">
        <input
          type="radio"
          id="upper-armenian"
          name="type"
          value="upper-armenian" />upper-armenian
      </label>
    
      <label for="disclosure-open">
        <input
          type="radio"
          id="disclosure-open"
          name="type"
          value="disclosure-open" />disclosure-open
      </label>
    
      <label for="disclosure-closed">
        <input
          type="radio"
          id="disclosure-closed"
          name="type"
          value="disclosure-closed" />disclosure-closed
      </label>
    
      <label for="moz-ethiopic-halehame">
        <input
          type="radio"
          id="moz-ethiopic-halehame"
          name="type"
          value="-moz-ethiopic-halehame" />-moz-ethiopic-halehame
      </label>
    
      <label for="moz-ethiopic-halehame-am">
        <input
          type="radio"
          id="moz-ethiopic-halehame-am"
          name="type"
          value="-moz-ethiopic-halehame-am" />-moz-ethiopic-halehame-am
      </label>
    
      <label for="ethiopic-halehame-ti-er">
        <input
          type="radio"
          id="ethiopic-halehame-ti-er"
          name="type"
          value="ethiopic-halehame-ti-er" />ethiopic-halehame-ti-er
      </label>
    
      <label for="ethiopic-halehame-ti-et">
        <input
          type="radio"
          id="ethiopic-halehame-ti-et"
          name="type"
          value="ethiopic-halehame-ti-et" />ethiopic-halehame-ti-et
      </label>
    
      <label for="hangul">
        <input type="radio" id="hangul" name="type" value="hangul" />hangul
      </label>
    
      <label for="hangul-consonant">
        <input
          type="radio"
          id="hangul-consonant"
          name="type"
          value="hangul-consonant" />hangul-consonant
      </label>
    
      <label for="urdu">
        <input type="radio" id="urdu" name="type" value="urdu" />urdu
      </label>
    
      <label for="moz-ethiopic-halehame-ti-er">
        <input
          type="radio"
          id="moz-ethiopic-halehame-ti-er"
          name="type"
          value="-moz-ethiopic-halehame-ti-er" />-moz-ethiopic-halehame-ti-er
      </label>
    
      <label for="moz-ethiopic-halehame-ti-et">
        <input
          type="radio"
          id="moz-ethiopic-halehame-ti-et"
          name="type"
          value="-moz-ethiopic-halehame-ti-et" />-moz-ethiopic-halehame-ti-et
      </label>
    
      <label for="moz-hangul">
        <input
          type="radio"
          id="moz-hangul"
          name="type"
          value="-moz-hangul" />-moz-hangul
      </label>
    
      <label for="moz-hangul-consonant">
        <input
          type="radio"
          id="moz-hangul-consonant"
          name="type"
          value="-moz-hangul-consonant" />-moz-hangul-consonant
      </label>
    
      <label for="moz-urdu">
        <input type="radio" id="moz-urdu" name="type" value="-moz-urdu" />-moz-urdu
      </label>
    </div>
    

#### CSS

css

    ol {
      font-size: 1.2rem;
    }
    
    .container {
      column-count: 3;
    }
    
    label {
      display: block;
    }
    
    input {
      margin: 0.4rem;
    }
    

#### JavaScript

js

    const container = document.querySelector(".container");
    const list = document.querySelector("ol");
    
    container.addEventListener("change", (event) => {
      list.setAttribute("style", `list-style-type: ${event.target.value}`);
    });
    

#### Result

We're not limited to the list style types defined on this page or the specification. The [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 at-rule enables creating [counters using any alphabet](https://r12a.github.io/app-counters/ "External link (opens in new tab)")
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Lists and Counters Module Level 3  <br>\# text-markers](https://drafts.csswg.org/css-lists/#text-markers) |
| [CSS Counter Styles Level 3  <br>\# extending-css2](https://drafts.csswg.org/css-counter-styles/#extending-css2) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
     shorthand property
*   [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
     property
*   [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
     property
*   [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
     pseudo-element
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/list-style-type/index.md?plain=1 "Folder: en-us/web/css/reference/properties/list-style-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Flist-style-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Flist-style-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc2375c58cf5a6f0fd7053f3cee7cba8bd88a2bbe%0A*+Document+last+modified%3A+2026-09-10T07%3A32%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
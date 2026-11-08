*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#mdn-search)
    

`pad` CSS at-rule descriptor
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`pad`** descriptor of the [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 at-rule is used to set a minimum length for marker representations.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#syntax)

--------------------------------------------------------------------------------------------------------

css

    pad: 3 "0";
    pad: "+" 5;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#values)

The descriptor accepts the following two values, which are separated by a space and can be specified in any order:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Specifies the minimum length that all marker representations must reach. The value must be non-negative. In the case of the `pad` descriptor, this value is also known as the _pad length_.

[`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols#symbol)

Specifies the symbol to be used for padding if the minimum length defined by the `<integer>` is not reached. In the case of the `pad` descriptor, this value is also known as the _padding symbol_.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#description)

------------------------------------------------------------------------------------------------------------------

Use the `pad` descriptor when you need the marker representations to be of a minimum length. If a marker representation is shorter than the specified pad length, then the marker representation will be padded with the specified padding symbol. Marker representations longer than the pad length are displayed without any additional padding.

The `pad` descriptor takes an `<integer>` for the minimum marker length and a `<symbol>` for the padding. A common use case of the `pad` descriptor is when you need a list to start numbering from `01` and go through `02`, `03`, `04`, and so on, instead of just `1`, `2`, `3`, and `4`. By specifying the `pad` descriptor as `pad: 2 "0"` in this case, the browser ensures to make the counter at least two characters long and adds a padding with `0` to reach the minimum two-character length where needed. Counters that are already two or more characters long in this example will be displayed normally, without padding.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0 ""` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

pad =   
  <integer \[0,∞\]>  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  <symbol>           
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<symbol> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#examples)

------------------------------------------------------------------------------------------------------------

### [Padding a counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#padding_a_counter)

This example extends the `decimal` [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
 to create a counter that is at least three characters long, padding shorter counters with `0` to reach that minimum length. A [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
 descriptor has been added to make the output more legible.

#### HTML

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li value="40">Forty</li>
      <li>Forty-one</li>
      <li value="200">Two hundred</li>
      <li value="3000">Three thousand</li>
      <li>and so on</li>
    </ul>
    

#### CSS

css

    @counter-style pad-example {
      system: extends decimal;
      suffix: ": ";
      pad: 3 "0";
    }
    
    ul {
      list-style: pad-example;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3  <br>\# counter-style-pad](https://drafts.csswg.org/css-counter-styles/#counter-style-pad) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad#see_also)

------------------------------------------------------------------------------------------------------------

*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     descriptors: [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
    , [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
    , [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
    , [`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
    , [`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
    , [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
    , [`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
    , [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
    , [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
    
*   List style properties: [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
     function to create anonymous counter styles
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@counter-style/pad/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@counter-style/pad (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fpad&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fpad%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fpad%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fpad%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
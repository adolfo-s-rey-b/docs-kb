*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#mdn-search)
    

`ruby-position` CSS property
============================

Baseline 2024

Newly available

\*

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`ruby-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the position of a ruby element relative to its base element. It can be positioned over the element (`over`), under it (`under`), or to the right (`inter-character`).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#try_it)

-----------------------------------------------------------------------------------------------------

    ruby-position: over;
    

    ruby-position: under;
    

    <section id="default-example">
      <ruby id="example-element"> 明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
    </section>
    

    #example-element {
      font-size: 2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    ruby-position: over;
    ruby-position: under;
    ruby-position: alternate;
    ruby-position: alternate over;
    ruby-position: alternate under;
    ruby-position: inter-character;
    
    /* Global values */
    ruby-position: inherit;
    ruby-position: initial;
    ruby-position: revert;
    ruby-position: revert-layer;
    ruby-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#values)

This property is specified as one of the following keyword values:

[`over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#over)

![Over example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position/screen_shot_2015-03-04_at_13.02.20.png) Is a keyword indicating that the ruby has to be placed over the main text for horizontal scripts and right to it for vertical scripts.

[`under`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#under)

![Under example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position/screen_shot_2015-03-04_at_13.02.07.png) Is a keyword indicating that the ruby has to be placed under the main text for horizontal scripts and left to it for vertical scripts.

[`alternate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#alternate)

Is a keyword indicating that the ruby alternates between over and under, when there are multiple levels of annotation.

[`inter-character`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#inter-character)

Is a keyword indicating that the ruby annotation is placed to the right of the base text characters. This value is intended for bopomofo (zhuyin fuhao) ruby.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `alternate` |
| Applies to | ruby annotation containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

ruby-position =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 alternate [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 over [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 under [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inter-character                      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#examples)

---------------------------------------------------------------------------------------------------------

### [Ruby positioned over the text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#ruby_positioned_over_the_text)

#### HTML

html

    <ruby>
      <rb>超電磁砲</rb>
      <rp>（</rp><rt>レールガン</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-position: over;
    }
    

#### Result

### [Ruby positioned under the text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#ruby_positioned_under_the_text)

#### HTML

html

    <ruby>
      <rb>超電磁砲</rb>
      <rp>（</rp><rt>レールガン</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-position: under;
    }
    

#### Result

### [Ruby alternate](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#ruby_alternate)

#### HTML

html

    <ruby>
      <rb>A</rb><rb>B</rb><rb>C</rb>
      <rtc>Above</rtc>
      <rtc>Below</rtc>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-position: alternate; /* this is also the initial value */
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Ruby Annotation Layout Module Level 1  <br>\# rubypos](https://drafts.csswg.org/css-ruby/#rubypos) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position#see_also)

---------------------------------------------------------------------------------------------------------

*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    , [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    , [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    , and [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)
     HTML elements
*   [`ruby-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align)
    
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/ruby-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/ruby-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
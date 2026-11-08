*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#mdn-search)
    

`ruby-align` CSS property
=========================

Baseline 2024

Newly available

Since December 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`ruby-align`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the distribution of the different ruby elements over the base.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    ruby-align: start;
    ruby-align: center;
    ruby-align: space-between;
    ruby-align: space-around;
    
    /* Global values */
    ruby-align: inherit;
    ruby-align: initial;
    ruby-align: revert;
    ruby-align: revert-layer;
    ruby-align: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#values)

This property is specified as one of the following keyword values:

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#start)

Is a keyword indicating that the ruby will be aligned with the start of the base text.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#center)

Is a keyword indicating that the ruby will be aligned at the middle of the base text.

[`space-between`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#space-between)

Is a keyword indicating that the extra space will be distributed between the elements of the ruby.

[`space-around`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#space-around)

Is a keyword indicating that the extra space will be distributed between the elements of the ruby, and around it.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `space-around` |
| Applies to | ruby bases, ruby annotations, ruby base containers, ruby annotation containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#formal_syntax)

----------------------------------------------------------------------------------------------------------------

ruby-align =   
  start          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-between  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space-around     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#examples)

------------------------------------------------------------------------------------------------------

### [Ruby aligned at the start of the base text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#ruby_aligned_at_the_start_of_the_base_text)

#### HTML

html

    <ruby>
      <rb>This is a long text to check</rb>
      <rp>（</rp><rt>short ruby</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-align: start;
    }
    

#### Result

### [Ruby aligned at the center of the base text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#ruby_aligned_at_the_center_of_the_base_text)

#### HTML

html

    <ruby>
      <rb>This is a long text to check</rb>
      <rp>（</rp><rt>short ruby</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-align: center;
    }
    

#### Result

### [Extra space distributed between ruby elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#extra_space_distributed_between_ruby_elements)

#### HTML

html

    <ruby>
      <rb>This is a long text to check</rb>
      <rp>（</rp><rt>short ruby</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-align: space-between;
    }
    

#### Result

### [Extra space distributed between and around ruby elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#extra_space_distributed_between_and_around_ruby_elements)

#### HTML

html

    <ruby>
      <rb>This is a long text to check</rb>
      <rp>（</rp><rt>short ruby</rt><rp>）</rp>
    </ruby>
    

#### CSS

css

    ruby {
      ruby-align: space-around;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Ruby Annotation Layout Module Level 1  <br>\# ruby-align-property](https://drafts.csswg.org/css-ruby/#ruby-align-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align#see_also)

------------------------------------------------------------------------------------------------------

*   [`ruby-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position)
    
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module
*   HTML Ruby elements: [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    , [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    , [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    , and [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/ruby-align/index.md?plain=1 "Folder: en-us/web/css/reference/properties/ruby-align (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-align&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-align%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-align%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-align%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
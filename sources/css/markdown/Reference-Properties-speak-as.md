*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#mdn-search)
    

`speak-as` CSS property
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/84)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#browser_compatibility)
 carefully before using this in production.

The **`speak-as`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to define how [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 content is spoken. The one to three enumerated key terms determine the manner by which elements and text get rendered by aural technologies, such as [screen readers](https://developer.mozilla.org/en-US/docs/Glossary/Screen_reader)
 and digital assistants.

This property applies to all content, including pseudo-elements, with the exception [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 pseudo-elements constructed via a [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 with a defined [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
 descriptor, which takes precedence over any inherited `speak-as` property value.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#syntax)

------------------------------------------------------------------------------------------------

css

    /* single value syntax */
    speak-as: normal;
    speak-as: spell-out;
    speak-as: literal-punctuation;
    speak-as: digits;
    speak-as: no-punctuation;
    
    /* multiple value syntax */
    speak-as: spell-out literal-punctuation;
    speak-as: spell-out no-punctuation;
    speak-as: digits literal-punctuation;
    speak-as: digits no-punctuation;
    speak-as: spell-out digits literal-punctuation;
    speak-as: spell-out digits no-punctuation;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#normal)

Normal pronunciation rules with punctuation replaced by pauses. For example, "Hello, world!" would be pronounced as "Hello (pause) world (pause)". This is the default value.

[`spell-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#spell-out)

Content is spelled out letter by letter. For example, "role" would be pronounced as "r" "o" "l" "e".

[`literal-punctuation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#literal-punctuation)

Punctuation marks are spelled out literally. For example, "Hello, world!" would be pronounced as "Hello comma world exclamation mark."

[`digits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#digits)

Numbers are pronounced as individual digits. For example, "31" would be pronounced as "three one".

[`no-punctuation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#no-punctuation)

Content is pronounced normally without any punctuation. For example, "Hello, world!" would be pronounced as "Hello" "world".

**Note:** Support of the `speak-as` property is limited and inconsistently implemented across different assistive technologies, such as screen readers or speech synthesizers. To ensure any pronunciation-dependent critical information remains user-friendly and accessible to a wide audience, do not rely solely on this CSS property to define how this information content is presented aurally.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | specified value |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#formal_syntax)

--------------------------------------------------------------------------------------------------------------

speak-as =   
  normal                                              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  spell-out [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 digits [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 literal-punctuation [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 no-punctuation [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#examples)

----------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#html)

html

    <p class="normal">Hello, world! I'm 25.</p>
    <p class="spell-out">Hello, world! I'm 25.</p>
    <p class="literal-punctuation">Hello, world! I'm 25.</p>
    <p class="no-punctuation">Hello, world! I'm 25.</p>
    <p class="digits">Hello, world! I'm 25.</p>
    <p class="multi">Hello, world! I'm 25.</p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#css)

css

    .normal {
      speak-as: normal;
    }
    
    .spell-out {
      speak-as: spell-out;
    }
    
    .literal-punctuation {
      speak-as: literal-punctuation;
    }
    
    .no-punctuation {
      speak-as: no-punctuation;
    }
    
    .digits {
      speak-as: digits;
    }
    .multi {
      speak-as: literal-punctuation digits;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Speech Module Level 1  <br>\# speaking-props-speak-as](https://drafts.csswg.org/css-speech-1/#speaking-props-speak-as) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as#see_also)

----------------------------------------------------------------------------------------------------

*   [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     at-rule [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
     descriptor
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module
*   [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/speak-as/index.md?plain=1 "Folder: en-us/web/css/reference/properties/speak-as (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fspeak-as&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fspeak-as%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fspeak-as%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fspeak-as%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
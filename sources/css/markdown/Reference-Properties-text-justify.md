*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#mdn-search)
    

`text-justify` CSS property
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/75)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-justify`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what type of justification should be applied to text when [`text-align: justify;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 is set on an element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#syntax)

----------------------------------------------------------------------------------------------------

css

    text-justify: none;
    text-justify: auto;
    text-justify: inter-word;
    text-justify: inter-character;
    text-justify: distribute; /* Deprecated value */
    
    /* Global values */
    text-justify: inherit;
    text-justify: initial;
    text-justify: revert;
    text-justify: revert-layer;
    text-justify: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#none)

The text justification is turned off. This has the same effect as not setting [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 at all, although it is useful if you need to turn justification on and off for some reason.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#auto)

The browser chooses the best type of justification for the current situation based on a balance between performance and quality, but also on what is most appropriate for the language of the text (e.g., English, CJK languages, etc.). This is the default justification used if `text-justify` is not set at all.

[`inter-word`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#inter-word)

The text is justified by adding space between words (effectively varying [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
), which is most appropriate for languages that separate words using spaces, like English or Korean.

[`inter-character`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#inter-character)

The text is justified by adding space between characters (effectively varying [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
), which is most appropriate for languages like Japanese.

[`distribute`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#distribute)

Exhibits the same behavior as `inter-character`; this value is kept for backwards compatibility.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | inline-level and table-cell elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#formal_syntax)

------------------------------------------------------------------------------------------------------------------

text-justify =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inter-word [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inter-character [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ruby [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  no-compress                                           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#examples)

--------------------------------------------------------------------------------------------------------

### [Demonstration of the different values of text-justify](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#demonstration_of_the_different_values_of_text-justify)

    <p class="none">
      <code>text-justify: none</code> —<br />Lorem ipsum dolor sit amet, consectetur
      adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit, dictum id
      mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat
      justo id, feugiat leo. Cras eu elementum dui.
    </p>
    <p class="auto">
      <code>text-justify: auto</code> —<br />Lorem ipsum dolor sit amet, consectetur
      adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit, dictum id
      mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar, consequat
      justo id, feugiat leo. Cras eu elementum dui.
    </p>
    <p class="dist">
      <code>text-justify: distribute</code> —<br />Lorem ipsum dolor sit amet,
      consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
      dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar,
      consequat justo id, feugiat leo. Cras eu elementum dui.
    </p>
    <p class="word">
      <code>text-justify: inter-word</code> —<br />Lorem ipsum dolor sit amet,
      consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
      dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar,
      consequat justo id, feugiat leo. Cras eu elementum dui.
    </p>
    <p class="char">
      <code>text-justify: inter-character</code> —<br />Lorem ipsum dolor sit amet,
      consectetur adipiscing elit. Nunc ornare maximus vehicula. Duis nisi velit,
      dictum id mauris vitae, lobortis pretium quam. Quisque sed nisi pulvinar,
      consequat justo id, feugiat leo. Cras eu elementum dui.
    </p>
    

css

    p {
      font-size: 1.5em;
      border: 1px solid black;
      padding: 10px;
      width: 95%;
      margin: 10px auto;
      text-align: justify;
    }
    
    .none {
      text-justify: none;
    }
    
    .auto {
      text-justify: auto;
    }
    
    .dist {
      text-justify: distribute;
    }
    
    .word {
      text-justify: inter-word;
    }
    
    .char {
      text-justify: inter-character;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# text-justify-property](https://drafts.csswg.org/css-text/#text-justify-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify#see_also)

--------------------------------------------------------------------------------------------------------

*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-justify/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-justify (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-justify&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-justify%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-justify%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-justify%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
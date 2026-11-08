*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#mdn-search)
    

`initial-letter` CSS property
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/189)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`initial-letter`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the size and sink for dropped, raised, and sunken initial letters. This property applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
 pseudo-elements and inline-level first children of block containers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    initial-letter: normal;
    
    /* One value */
    initial-letter: 3; /* 3 lines tall, baseline at line 3 */
    initial-letter: 1.5; /* 1.5 lines tall, baseline at line 2 */
    
    /* Two values */
    initial-letter: 3 2; /* 3 lines tall, baseline at line 2 (raised 1 line) */
    initial-letter: 3 1; /* 3 lines tall, baseline unchanged (raised 2 lines) */
    
    /* Global values */
    initial-letter: inherit;
    initial-letter: initial;
    initial-letter: revert;
    initial-letter: revert-layer;
    initial-letter: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#values)

This property is specified as `normal` or a `<number>` optionally followed by an `<integer>`:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#normal)

No special initial-letter effect. Text behaves as normal.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#number)

Defines the size of the initial letter, in terms of how many lines it occupies. Negative values are not allowed.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#integer)

Defines the number of lines the initial letter should sink when the size of it is given. Values must be greater than zero. If omitted, it duplicates the size value, floored to the nearest positive whole number.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> pseudo-elements and inline-level first child of a block container |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

initial-letter =   
  normal                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[1,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 <integer \[1,∞\]>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[1,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 drop [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 raise [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#examples)

----------------------------------------------------------------------------------------------------------

### [Setting initial letter size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#setting_initial_letter_size)

#### HTML

html

    <p class="normal">Initial letter is normal</p>
    <p class="onefive">Initial letter occupies 1.5 lines</p>
    <p class="three">Initial letter occupies 3 lines</p>
    

#### CSS

css

    .normal::first-letter {
      -webkit-initial-letter: normal;
      initial-letter: normal;
    }
    
    .onefive::first-letter {
      -webkit-initial-letter: 1.5;
      initial-letter: 1.5;
    }
    
    .three::first-letter {
      -webkit-initial-letter: 3;
      initial-letter: 3;
    }
    
    p {
      outline: 1px dashed red;
    }
    

#### Result

### [Setting the sink value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#setting_the_sink_value)

In this example, all the initial letters are the same size, but with different sink values.

#### HTML

html

    <p class="four">Initial letter: Sink value = 4</p>
    <p class="same">Initial letter: Sink value not declared (same as size)</p>
    <p class="two">Initial letter: Sink value = 2</p>
    <p class="one">Initial letter: Sink value = 1</p>
    

#### CSS

css

    .four::first-letter {
      -webkit-initial-letter: 3 4;
      initial-letter: 3 4;
    }
    
    .same::first-letter {
      -webkit-initial-letter: 3;
      initial-letter: 3;
    }
    
    .two::first-letter {
      -webkit-initial-letter: 3 2;
      initial-letter: 3 2;
    }
    
    .one::first-letter {
      -webkit-initial-letter: 3 1;
      initial-letter: 3 1;
    }
    
    p {
      outline: 1px dashed red;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Inline Layout Module Level 3  <br>\# sizing-drop-initials](https://drafts.csswg.org/css-inline/#sizing-drop-initials) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter#see_also)

----------------------------------------------------------------------------------------------------------

*   [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`:first-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    
*   [Drop caps in CSS](https://www.oddbird.net/2017/01/03/initial-letter/ "External link (opens in new tab)")
     via Oddbird (2017)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/initial-letter/index.md?plain=1 "Folder: en-us/web/css/reference/properties/initial-letter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finitial-letter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finitial-letter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finitial-letter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finitial-letter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
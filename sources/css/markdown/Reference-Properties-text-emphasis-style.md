*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#mdn-search)
    

`text-emphasis-style` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-emphasis-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the appearance of emphasis marks. It can also be set, and reset, using the [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
 shorthand.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#try_it)

-----------------------------------------------------------------------------------------------------------

    text-emphasis-style: none;
    

    text-emphasis-style: triangle;
    

    text-emphasis-style: "x";
    

    text-emphasis-style: filled double-circle;
    

    <section id="default-example">
      <p>
        I'd far rather be
        <span class="transition-all" id="example-element">happy than right</span>
        any day.
      </p>
    </section>
    

    p {
      font: 1.5em sans-serif;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Initial value */
    text-emphasis-style: none; /* No emphasis marks */
    
    /* <string> values */
    text-emphasis-style: "x";
    text-emphasis-style: "\25B2";
    text-emphasis-style: "*";
    
    /* Keyword values */
    text-emphasis-style: filled;
    text-emphasis-style: open;
    text-emphasis-style: dot;
    text-emphasis-style: circle;
    text-emphasis-style: double-circle;
    text-emphasis-style: triangle;
    text-emphasis-style: filled sesame;
    text-emphasis-style: open sesame;
    
    /* Global values */
    text-emphasis-style: inherit;
    text-emphasis-style: initial;
    text-emphasis-style: revert;
    text-emphasis-style: revert-layer;
    text-emphasis-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#none)

No emphasis marks.

[`filled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#filled)

The shape is filled with solid color. If neither `filled` nor `open` is present, this is the default.

[`open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#open)

The shape is hollow.

[`dot`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#dot)

Display small circles as marks. The filled dot is `'•'` (`U+2022`), and the open dot is `'◦'` (`U+25E6`).

[`circle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#circle)

Display large circles as marks. The filled circle is `'●'` (`U+25CF`), and the open circle is `'○'` (`U+25CB`).

[`double-circle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#double-circle)

Display double circles as marks. The filled double-circle is `'◉'` (`U+25C9`), and the open double-circle is `'◎'` (`U+25CE`).

[`triangle`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#triangle)

Display triangles as marks. The filled triangle is `'▲'` (`U+25B2`), and the open triangle is `'△'` (`U+25B3`).

[`sesame`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#sesame)

Display sesames as marks. The filled sesame is `'﹅'` (`U+FE45`), and the open sesame is `'﹆'` (`U+FE46`).

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#string)

Display the given string as marks. Authors should not specify more than one _character_ in `<string>`. The UA may truncate or ignore strings consisting of more than one grapheme cluster.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

text-emphasis-style =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 filled [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 open [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 dot [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 circle [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 double-circle [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 triangle [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 sesame [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
                                              

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#basic_example)

css

    h2 {
      -webkit-text-emphasis-style: sesame;
      text-emphasis-style: sesame;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-emphasis-style-property](https://drafts.csswg.org/css-text-decor/#text-emphasis-style-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style#see_also)

---------------------------------------------------------------------------------------------------------------

*   The related properties [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    .
*   The [`text-emphasis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
     property allowing you to define the position of the emphasis marks.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-emphasis-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-emphasis-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-emphasis-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-emphasis-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-emphasis-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-emphasis-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F56f3d7018159127dbe92842413fb45d0aa7e8193%0A*+Document+last+modified%3A+2026-08-27T13%3A16%3A14.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
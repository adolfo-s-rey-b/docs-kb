*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#mdn-search)
    

`text-decoration-line` CSS property
===================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-decoration-line`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the kind of decoration that is used on text in an element, such as an underline or overline.

When setting multiple line-decoration properties at once, it may be more convenient to use the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand property instead.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#try_it)

------------------------------------------------------------------------------------------------------------

    text-decoration-line: none;
    

    text-decoration-line: underline;
    

    text-decoration-line: overline;
    

    text-decoration-line: line-through;
    

    text-decoration-line: grammar-error;
    

    text-decoration-line: spelling-error;
    

    text-decoration-line: underline overline;
    

    text-decoration-line: underline line-through;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Single keyword */
    text-decoration-line: none;
    text-decoration-line: underline;
    text-decoration-line: overline;
    text-decoration-line: line-through;
    text-decoration-line: blink;
    text-decoration-line: spelling-error;
    text-decoration-line: grammar-error;
    
    /* Multiple keywords */
    text-decoration-line: underline overline; /* Two decoration lines */
    text-decoration-line: overline underline line-through; /* Multiple decoration lines */
    
    /* Global values */
    text-decoration-line: inherit;
    text-decoration-line: initial;
    text-decoration-line: revert;
    text-decoration-line: revert-layer;
    text-decoration-line: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#values)

This property is specified either as `none` or a space-separated list of keyword values chosen from the list below:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#none)

Produces no text decoration.

[`underline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#underline)

Each line of text has a decorative line beneath it.

[`overline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#overline)

Each line of text has a decorative line above it.

[`line-through`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#line-through)

Each line of text has a decorative line going through its middle.

[`blink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#blink)

The text blinks (alternates between visible and invisible). Conforming user agents may not blink the text. This value is **deprecated** in favor of [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
.

[`spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#spelling-error)

Each line of text uses the user agents' method of highlighting spelling mistakes, which is a dotted red line in most browsers.

[`grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#grammar-error)

Each line of text uses the user agents' method of highlighting grammar mistakes, which is a dotted green line in most browsers.

**Note:** When using `spelling-error` and `grammar-error` values, the browser disregards the other properties in the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand (such as [`text-underline-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
, `color`, or `stroke`).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

text-decoration-line =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 underline [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 overline [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 line-through [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 blink [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  spelling-error                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  grammar-error                                         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#examples)

----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#basic_example)

html

    <p class="wavy">Here's some text with wavy red underline!</p>
    <p class="both">This text has lines both above and below it.</p>
    

css

    .wavy {
      text-decoration-line: underline;
      text-decoration-style: wavy;
      text-decoration-color: red;
    }
    
    .both {
      text-decoration-line: underline overline;
    }
    

### [Errors example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#errors_example)

In this example, the first paragraph contains a spelling mistake and uses the browser's styling for spelling errors on the misspelled word. The second paragraph uses the browser's styling for grammar errors. There is no styling change in browsers that do not support these `text-decoration-line` values.

html

    <p>This text contains a <span class="spelling">speling</span> mistake.</p>
    <p class="grammar">This text contain grammatical errors.</p>
    

css

    .spelling {
      text-decoration-line: spelling-error;
    }
    
    .grammar {
      text-decoration-line: grammar-error;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-decoration-line-property](https://drafts.csswg.org/css-text-decor/#text-decoration-line-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line#see_also)

----------------------------------------------------------------------------------------------------------------

*   When setting multiple line-decoration properties at once, it may be more convenient to use the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     shorthand property instead, which also includes:
    *   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
        
    *   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
        
    *   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
        
*   [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    
*   [`::spelling-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    
*   [`::grammar-error`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration-line/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration-line (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-line&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-line%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-line%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-line%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
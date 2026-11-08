*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#mdn-search)
    

`text-decoration-thickness` CSS property
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-decoration-thickness`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the stroke thickness of the decoration line that is used on text in an element, such as a line-through, underline, or overline.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#try_it)

-----------------------------------------------------------------------------------------------------------------

    text-decoration-line: underline;
    text-decoration-thickness: 3px;
    

    text-decoration-line: line-through;
    text-decoration-thickness: 0.4rem;
    

    text-decoration-line: underline overline;
    text-decoration-thickness: from-font;
    font-size: 2rem;
    

    <section id="default-example">
      <p id="example-element">
        Confusion kissed me on the cheek, and left a taste so bittersweet
      </p>
    </section>
    

    p {
      font: 1.5em sans-serif;
      text-decoration-color: red;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Single keyword */
    text-decoration-thickness: auto;
    text-decoration-thickness: from-font;
    
    /* length */
    text-decoration-thickness: 0.1em;
    text-decoration-thickness: 3px;
    
    /* percentage */
    text-decoration-thickness: 10%;
    
    /* Global values */
    text-decoration-thickness: inherit;
    text-decoration-thickness: initial;
    text-decoration-thickness: revert;
    text-decoration-thickness: revert-layer;
    text-decoration-thickness: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#auto)

The browser chooses an appropriate width for the text decoration line.

[`from-font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#from-font)

If the font file includes information about a preferred thickness, use that value. If the font file doesn't include this information, behave as if `auto` was set, with the browser choosing an appropriate thickness.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#length)

Specifies the thickness of the text decoration line as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, overriding the font file suggestion or the browser default.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#percentage)

Specifies the thickness of the text decoration line as a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 of **1em** in the current font. A percentage inherits as a relative value, and so therefore scales with changes in the font. The browser must use a minimum of 1 device pixel. For a given application of this property, the thickness is constant across the whole box it is applied to, even if there are child elements with a different font size.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the font size of the element itself |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

text-decoration-thickness =   
  auto                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  from-font            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <length-percentage>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <line-width>           
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<line-width>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
 =   
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hairline        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thin            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  medium          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  thick             

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#examples)

---------------------------------------------------------------------------------------------------------------------

### [Varying thickness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#varying_thickness)

#### HTML

html

    <p class="thin">Here's some text with a 1px red underline.</p>
    <p class="thick">This one has a 5px red underline.</p>
    <p class="shorthand">This uses the equivalent shorthand.</p>
    

#### CSS

css

    .thin {
      text-decoration-line: underline;
      text-decoration-style: solid;
      text-decoration-color: red;
      text-decoration-thickness: 1px;
    }
    
    .thick {
      text-decoration-line: underline;
      text-decoration-style: solid;
      text-decoration-color: red;
      text-decoration-thickness: 5px;
    }
    
    .shorthand {
      text-decoration: underline solid red 5px;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 4  <br>\# text-decoration-thickness-property](https://drafts.csswg.org/css-text-decor-4/#text-decoration-thickness-property) |

**Note:** The property used to be called `text-decoration-width`, but was updated in 2019 to `text-decoration-thickness`.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration-thickness/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration-thickness (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-thickness&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-thickness%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-thickness%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-thickness%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
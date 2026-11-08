*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#mdn-search)
    

`<length-percentage>` CSS type
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<length-percentage>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a value that can be either a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#syntax)

-----------------------------------------------------------------------------------------------------

Refer to the documentation for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 for details of the individual syntaxes allowed by this type.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

<length-percentage> =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#examples)

---------------------------------------------------------------------------------------------------------

### [length-percentage examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#length-percentage_examples)

This example demonstrates several properties that use `<length-percentage>` values.

#### HTML

html

    <p>You can use percentages and lengths in so many places.</p>
    

#### CSS

css

    p {
      /* length-percentage examples */
      width: 75%;
      height: 200px;
      margin: 3rem;
      padding: 1%;
      border-radius: 10px 10%;
      font-size: 250%;
      line-height: 1.5em;
    
      /* length examples */
      text-shadow: 1px 1px 1px red;
      border: 5px solid red;
      letter-spacing: 3px;
    
      /* percentage example */
      text-size-adjust: 20%;
    }
    

#### Result

### [Use in calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#use_in_calc)

Where a `<length-percentage>` is specified as an allowable type, this means that the percentage resolves to a length and therefore can be used in a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression. Therefore, all of the following values are acceptable for [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
:

css

    width: 200px;
    width: 20%;
    width: calc(100% - 200px);
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# mixed-percentages](https://drafts.csswg.org/css-values/#mixed-percentages) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage#see_also)

---------------------------------------------------------------------------------------------------------

*   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
*   [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/length-percentage/index.md?plain=1 "Folder: en-us/web/css/reference/values/length-percentage (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flength-percentage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flength-percentage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Flength-percentage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Flength-percentage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
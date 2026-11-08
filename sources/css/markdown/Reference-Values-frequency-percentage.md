*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#mdn-search)
    

`<frequency-percentage>` CSS type
=================================

The **`<frequency-percentage>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a value that can be either a [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
. Frequency values, e.g., the pitch of a speaking voice, are not currently used in any CSS properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#syntax)

--------------------------------------------------------------------------------------------------------

The value of a `<frequency-percentage>` is either a [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
; see their individual reference pages for details about their syntaxes.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#description)

------------------------------------------------------------------------------------------------------------------

### [Use in calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#use_in_calc)

Where a `<frequency-percentage>` is specified as an allowable type, this means that the percentage resolves to a frequency and therefore can be used in a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

<frequency-percentage> =   
  [<frequency>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#examples)

------------------------------------------------------------------------------------------------------------

### [Valid percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#valid_percentage_values)

90% Positive percentage
+90% Positive percentage with leading +
-90% Negative percentage — not valid for all properties that use percentages

### [Invalid percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#invalid_percentage_values)

90 % No space is allowed between the number and the unit

### [Valid frequency values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#valid_frequency_values)

12Hz     Positive integer
4.3Hz    Non-integer
14KhZ    The unit is case-insensitive, though non-SI capitalization is not recommended.
+0Hz     Zero, with a leading + and a unit
-0kHz    Zero, with a leading - and a unit

### [Invalid frequency values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#invalid_frequency_values)

12.0     This is a <number>, not an <frequency>, because it is missing a unit.
7 Hz     No space is allowed between the number and the unit.
0        Although unitless zero is an allowable <length>, it's an invalid <frequency>.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# typedef-frequency-percentage](https://drafts.csswg.org/css-values/#typedef-frequency-percentage) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage#see_also)

------------------------------------------------------------------------------------------------------------

*   [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   Related CSS data types:
    *   [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
        
    *   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/frequency-percentage/index.md?plain=1 "Folder: en-us/web/css/reference/values/frequency-percentage (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffrequency-percentage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffrequency-percentage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffrequency-percentage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffrequency-percentage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
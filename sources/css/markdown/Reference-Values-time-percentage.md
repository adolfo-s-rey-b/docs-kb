*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#mdn-search)
    

`<time-percentage>` CSS type
============================

The **`<time-percentage>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a value that can be either a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 or a [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#syntax)

---------------------------------------------------------------------------------------------------

Refer to the documentation for [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 for details of the individual syntaxes allowed by this type.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<time-percentage> =   
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#examples)

-------------------------------------------------------------------------------------------------------

### [Use in calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#use_in_calc)

Where a `<time-percentage>` is specified as an allowable type, this means that the percentage resolves to a time and therefore can be used in a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression.

### [Valid percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#valid_percentages)

50%
+50%        Optional plus sign
-50%        Negative percentages are not valid for all properties that accept percentages

### [Invalid percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#invalid_percentages)

50 %        Space not allowed between the number and the percentage sign

### [Valid times](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#valid_times)

12s         Positive integer
-456ms      Negative integer
4.3ms       Non-integer
14mS        The unit is case-insensitive, although capital letters are not recommended.
+0s         Zero with a leading + and a unit
-0ms        Zero with a leading - and a unit

### [Invalid times](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#invalid_times)

0           Although unitless zero is allowed for <length>s, it's invalid for <time>s.
12.0        This is a <number>, not a <time>, because it's missing a unit.
7 ms        No space is allowed between the number and the unit.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# typedef-time-percentage](https://drafts.csswg.org/css-values/#typedef-time-percentage) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage#see_also)

-------------------------------------------------------------------------------------------------------

*   [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
*   [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/time-percentage/index.md?plain=1 "Folder: en-us/web/css/reference/values/time-percentage (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftime-percentage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftime-percentage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftime-percentage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftime-percentage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
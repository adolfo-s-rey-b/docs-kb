*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#mdn-search)
    

`<frequency>` CSS type
======================

The **`<frequency>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a frequency dimension, such as the pitch of a speaking voice. It is not currently used in any CSS properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#syntax)

---------------------------------------------------------------------------------------------

The `<frequency>` data type consists of a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by one of the units listed below. As with all CSS dimensions, there is no space between the unit literal and the number.

### [Units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#units)

[`Hz`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#hz)

Represents a frequency in hertz. Examples: `0Hz`, `1500Hz`, `10000Hz`.

[`kHz`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#khz)

Represents a frequency in kilohertz. Examples: `0kHz`, `1.5kHz`, `10kHz`.

**Note:** Although the number `0` is always the same regardless of unit, the unit may not be omitted. In other words, `0` is invalid and does not represent `0Hz` or `0kHz`. Though the units are case-insensitive, it is good practice to use a capital "H" for `Hz` and `kHz`, as specified in the [SI](https://en.wikipedia.org/wiki/International_System_of_Units "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#examples)

-------------------------------------------------------------------------------------------------

Valid frequency values:

12Hz     Positive integer
4.3Hz    Non-integer
14KhZ    The unit is case-insensitive, though non-SI capitalization is not recommended.
+0Hz     Zero, with a leading + and a unit
-0kHz    Zero, with a leading - and a unit

Invalid frequency values:

12.0     This is a <number>, not an <frequency>, because it is missing a unit.
7 Hz     No space is allowed between the number and the unit.
0        Although unitless zero is an allowable <length>, it's an invalid <frequency>.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# frequency-value](https://drafts.csswg.org/css-values/#frequency-value) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

Currently, no browsers support this feature.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency#see_also)

-------------------------------------------------------------------------------------------------

*   [`<frequency-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/frequency/index.md?plain=1 "Folder: en-us/web/css/reference/values/frequency (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffrequency&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffrequency%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffrequency%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffrequency%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
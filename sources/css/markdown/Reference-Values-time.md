*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#mdn-search)
    

`<time>` CSS type
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<time>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a time value expressed in seconds or milliseconds. It is used in [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
, [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
, and related properties.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#syntax)

----------------------------------------------------------------------------------------

The `<time>` data type consists of a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by one of the units listed below. Optionally, it may be preceded by a single `+` or `-` sign. As with all dimensions, there is no space between the unit literal and the number.

**Note:** Although the number `0` is always the same regardless of unit, the unit may not be omitted. In other words, `0` is invalid and does not represent `0s` or `0ms`.

### [Units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#units)

[`s`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#s)

Represents a time in seconds. Examples: `0s`, `1.5s`, `-60s`.

[`ms`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#ms)

Represents a time in milliseconds. Examples: `0ms`, `150.25ms`, `-60000ms`.

**Note:** Conversion between `s` and `ms` follows the logical `1s` = `1000ms`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#examples)

--------------------------------------------------------------------------------------------

### [Valid times](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#valid_times)

12s         Positive integer
-456ms      Negative integer
4.3ms       Non-integer
14mS        The unit is case-insensitive, although capital letters are not recommended.
+0s         Zero with a leading + and a unit
-0ms        Zero with a leading - and a unit

### [Invalid times](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#invalid_times)

0           Although unitless zero is allowed for <length>s, it's invalid for <time>s.
12.0        This is a <number>, not a <time>, because it's missing a unit.
7 ms        No space is allowed between the number and the unit.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# time](https://drafts.csswg.org/css-values/#time) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time#see_also)

--------------------------------------------------------------------------------------------

*   [`<time-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/time/index.md?plain=1 "Folder: en-us/web/css/reference/values/time (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftime&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftime%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ftime%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ftime%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
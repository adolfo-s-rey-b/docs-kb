*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#mdn-search)
    

`<number>` CSS type
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<number>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a number, being either an integer, a number with a fractional component, or a base-ten exponent in scientific notation.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#syntax)

------------------------------------------------------------------------------------------

The syntax of `<number>` extends the syntax of [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
. A fractional value is represented by a `.` followed by one or more decimal digits, and may be appended to an integer. A `<number>` can also end with the letter `e` or `E` followed by an integer, which indicates a base-ten exponent in scientific notation. There is no unit associated with numbers.

As with integers, the first character of the number can be immediately preceded by - or + to indicate the number's sign: whether the number is positive or negative.

[Interpolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#interpolation)

--------------------------------------------------------------------------------------------------------

When animated, values of the `<number>` CSS data type are interpolated as real, floating-point numbers. The speed of the interpolation is determined by the [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 associated with the animation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#examples)

----------------------------------------------------------------------------------------------

### [Valid numbers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#valid_numbers)

12          A raw <integer> is also a <number>.
4.01        Positive fraction
-456.8      Negative fraction
0.0         Zero
+0.0        Zero, with a leading +
-0.0        Zero, with a leading -
.60         Fractional number without a leading zero
10e3        Scientific notation
-3.4e-2     Complicated scientific notation

### [Invalid numbers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#invalid_numbers)

12\.         Decimal points must be followed by at least one digit.
+-12.2      Only one leading +/- is allowed.
12.1.1      Only one decimal point is allowed.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# numbers](https://drafts.csswg.org/css-values/#numbers) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number#see_also)

----------------------------------------------------------------------------------------------

*   [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
    
*   [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/number/index.md?plain=1 "Folder: en-us/web/css/reference/values/number (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fnumber&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fnumber%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fnumber%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fnumber%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
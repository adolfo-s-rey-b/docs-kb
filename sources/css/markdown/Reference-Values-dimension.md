*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#mdn-search)
    

`<dimension>` CSS type
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<dimension>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 with a unit attached to it, for example `10px`.

CSS uses dimensions to specify distances ([`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
), durations ([`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
), frequencies ([`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
), resolutions ([`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
), and other quantities.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#syntax)

---------------------------------------------------------------------------------------------

The syntax of `<dimension>` is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 immediately followed by a unit which is an identifier. Unit identifiers are case insensitive.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#examples)

-------------------------------------------------------------------------------------------------

### [Valid dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#valid_dimensions)

12px      12 pixels
1rem      1 rem
1.2pt     1.2 points
2200ms    2200 milliseconds
5s        5 seconds
200hz     200 Hertz
200Hz     200 Hertz (values are case insensitive)

### [Invalid dimensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#invalid_dimensions)

12 px       The unit must come immediately after the number.
12"px"      Units are identifiers and therefore unquoted.
3sec        The seconds unit is abbreviated "s" not "sec".

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# dimensions](https://drafts.csswg.org/css-values/#dimensions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension#see_also)

-------------------------------------------------------------------------------------------------

*   [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   [Learn to style HTML using CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)
    
*   CSS distances ([`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    ), durations ([`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    ), frequencies ([`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    ), and resolutions ([`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    )

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/dimension/index.md?plain=1 "Folder: en-us/web/css/reference/values/dimension (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdimension&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdimension%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdimension%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdimension%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
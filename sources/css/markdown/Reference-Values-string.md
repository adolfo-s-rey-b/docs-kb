*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#mdn-search)
    

`<string>` CSS type
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<string>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a sequence of characters. Strings are used in numerous CSS properties, such as [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
, [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
, and [`quotes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#syntax)

------------------------------------------------------------------------------------------

The `<string>` data type is composed of any number of [Unicode](https://en.wikipedia.org/wiki/Unicode "External link (opens in new tab)")
 characters surrounded by either double (`"`) or single (`'`) quotes.

Most characters can be represented literally. All characters can also be represented with their respective [Unicode code points](https://en.wikipedia.org/wiki/Unicode#Code_point_planes_and_blocks "External link (opens in new tab)")
 in hexadecimal, in which case they are preceded by a backslash (`\`). For example, `\22` represents a double quote, `\27` a single quote (`'`), and `\A9` the copyright symbol (`©`).

Importantly, certain characters which would otherwise be invalid can be escaped with a backslash. These include double quotes when used inside a double-quoted string, single quotes when used inside a single-quoted string, and the backslash itself. For example, `\\` will create a single backslash.

To output new lines, you must escape them with a line feed character such as `\A` or `\00000A`. In your code, however, strings can span multiple lines, in which case each new line must be escaped with a `\` as the last character of the line.

However, to get new lines, you must also set the [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 property to appropriate value.

**Note:** [Character references](https://developer.mozilla.org/en-US/docs/Glossary/Character_reference)
 (such as `&nbsp;` or `&#8212;`) cannot be used in a CSS `<string>`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#examples)

----------------------------------------------------------------------------------------------

### [Examples of valid strings](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#examples_of_valid_strings)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# strings](https://drafts.csswg.org/css-values/#strings) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string#see_also)

----------------------------------------------------------------------------------------------

*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module
*   [CSS basic data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
    
*   [Introduction to CSS: Values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/string/index.md?plain=1 "Folder: en-us/web/css/reference/values/string (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fstring&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fstring%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fstring%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fstring%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
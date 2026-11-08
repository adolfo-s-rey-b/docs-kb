*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#mdn-search)
    

`<ident>` CSS type
==================

The **`<ident>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 denotes an arbitrary unquoted string of characters used as an [identifier](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#syntax)

-----------------------------------------------------------------------------------------

A CSS identifier consists of one or more characters, which can be any of the following:

*   any [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
     character in the ranges `A-Z` and `a-z`
*   any decimal digit (`0` to `9`)
*   a hyphen (`-`)
*   an underscore (`_`)
*   any other [Unicode](https://developer.mozilla.org/en-US/docs/Glossary/Unicode)
     character `U+00A0` and higher (that is, any other non-ASCII Unicode character)
*   an [escaped character](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#escaping_characters)
    

Additionally, an identifier must not start with an unescaped digit, and must not start with an unescaped hyphen followed by an unescaped digit.

Note that `id1`, `Id1`, `iD1` and `ID1` are all different identifiers because they are [case-sensitive](https://en.wikipedia.org/wiki/Case_sensitivity "External link (opens in new tab)")
. On the other hand, since there are several ways to escape a character, `toto\?` and `toto\3F` are the same identifiers.

### [Escaping characters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#escaping_characters)

[Escaping a character](https://developer.mozilla.org/en-US/docs/Glossary/Escape_character)
 means representing it in a way that changes how it is interpreted by a software system. In CSS, you can escape a character by adding a backslash (`\`) in front of the character. Any character, except the hexadecimal digits `0-9`, `a-f`, and `A-F`, can be escaped in this way. For example, `&` can be escaped as `\&`.

You can also escape any character with a backslash followed by the character's [Unicode](https://developer.mozilla.org/en-US/docs/Glossary/Unicode)
 [code point](https://developer.mozilla.org/en-US/docs/Glossary/Code_point)
 represented by one to six hexadecimal digits. For example, `&` can be escaped as `\26`. In this usage, if the escaped character is followed by a hexadecimal digit, do one of the following:

*   Place a space or other whitespace character after the Unicode code point.
*   Provide the full six-digit Unicode code point of the character being escaped.

For example, the string `&123` can be escaped as `\26 123` (with a whitespace) or `\000026123` (with the six-digit Unicode code point for `&`) to ensure that `123` is not considered as part of the escape pattern.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#examples)

---------------------------------------------------------------------------------------------

### [Valid identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#valid_identifiers)

nono79        /\* A mix of alphanumeric characters and numbers \*/
ground-level  /\* A mix of alphanumeric characters and a dash \*/
-test         /\* A hyphen followed by alphanumeric characters \*/
--toto        /\* A custom-property like identifier \*/
\_internal     /\* An underscore followed by alphanumeric characters \*/
\\22 toto      /\* An escaped character followed by alphanumeric characters \*/
\\000022toto   /\* Same as the previous example \*/
scooby\\.doo   /\* A correctly escaped period \*/
🔥123         /\* A non-ASCII character followed by numbers \*/

### [Invalid identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#invalid_identifiers)

34rem     /\* Must not start with a decimal digit \*/
-12rad    /\* Must not start with a dash followed by a decimal digit \*/
scooby.doo  /\* ASCII characters apart from alphanumerics must be escaped \*/
'scoobyDoo' /\* Treated as a string \*/
"scoobyDoo" /\* Treated as a string \*/

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# typedef-ident](https://drafts.csswg.org/css-values/#typedef-ident) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

_As this type is not a real type but a convenience type used to simplify the definition of other CSS syntax, there is no browser compatibility information as such._

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#see_also)

---------------------------------------------------------------------------------------------

*   [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
*   [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 25, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/ident/index.md?plain=1 "Folder: en-us/web/css/reference/values/ident (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fident&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fident%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fident%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fident%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcad9096502d2a74b34a67377bbb0ac88fcfa58c2%0A*+Document+last+modified%3A+2026-05-25T02%3A16%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
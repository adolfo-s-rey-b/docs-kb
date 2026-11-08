*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#mdn-search)
    

`@charset` CSS at-rule
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@charset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 rule specifies the character encoding used in the style sheet. This syntax is useful when using non-[ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 characters in some CSS properties, like [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
. Although the first character in `@charset` is the `@` symbol, it is not an [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
. It is a specific byte sequence that can only be placed at the very beginning of a stylesheet. No other characters, except the Unicode byte-order mark, are allowed before it. It also does not follow normal CSS syntax rules such as use of quotes or whitespace.

If a `@charset` is not recognized as the charset declaration, it is parsed as a normal at-rule. The [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
 module deprecates this fallback behavior, defining it as an unrecognized legacy rule to be dropped when a stylesheet is grammar-checked.

As there are several ways to define the character encoding of a style sheet, the browser will try the following methods in the following order (and stop as soon as one yields a result):

1.  The value of the [Unicode byte-order](https://en.wikipedia.org/wiki/Byte_order_mark "External link (opens in new tab)")
     character placed at the beginning of the file.
2.  The value given by the `charset` attribute of the `Content-Type:` HTTP header or the equivalent in the protocol used to serve the style sheet.
3.  The `@charset` CSS declaration.
4.  Use the character encoding defined by the referring document: the `charset` attribute of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
     element. This method is obsolete and should not be used.
5.  Assume that the document is UTF-8.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#syntax)

----------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#parameters)

[_charset_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#charset)

A [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 denoting the character encoding to be used. It must be the name of a web-safe character encoding defined in the [IANA-registry](https://www.iana.org/assignments/character-sets "External link (opens in new tab)")
, and must be double-quoted, following exactly one space character (U+0020), and immediately terminated with a semicolon. If several names are associated with an encoding, only the one marked with _preferred_ must be used.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#formal_syntax)

------------------------------------------------------------------------------------------------------------

Note that the `@charset` rule is not parsed via syntax, but via a specific byte sequence of the following form:

@charset "<charset>";

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#examples)

--------------------------------------------------------------------------------------------------

### [Valid and invalid charset declarations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#valid_and_invalid_charset_declarations)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Syntax Module Level 3  <br>\# at-ruledef-charset](https://drafts.csswg.org/css-syntax/#at-ruledef-charset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset#see_also)

--------------------------------------------------------------------------------------------------

*   [Character set](https://developer.mozilla.org/en-US/docs/Glossary/Character_set)
     glossary entry
*   [Unicode](https://developer.mozilla.org/en-US/docs/Glossary/Unicode)
     glossary entry

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@charset/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@charset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40charset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40charset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40charset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40charset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa4c63d2855b2f557e7d1ee821dee65011d569a41%0A*+Document+last+modified%3A+2026-09-17T10%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
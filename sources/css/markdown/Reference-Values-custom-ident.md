*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#mdn-search)
    

`<custom-ident>` CSS type
=========================

The **`<custom-ident>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 denotes an arbitrary user-defined string used as an [identifier](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
. It is case-sensitive, and certain values are forbidden in various contexts to prevent ambiguity.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#syntax)

------------------------------------------------------------------------------------------------

The syntax of `<custom-ident>` is similar to CSS identifiers (such as property names), except that it is [case-sensitive](https://en.wikipedia.org/wiki/Case_sensitivity "External link (opens in new tab)")
. It consists of one or more characters, where characters can be any of the following:

*   any alphabetical character (`A` to `Z`, or `a` to `z`),
*   any decimal digit (`0` to `9`),
*   a hyphen (`-`),
*   an underscore (`_`),
*   an [escaped character](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#escaping_characters)
     (preceded by a backslash, `\`),
*   a [Unicode](https://en.wikipedia.org/wiki/Unicode "External link (opens in new tab)")
     character (in the format of a backslash, `\`, followed by one to six hexadecimal digits, representing its Unicode code point)

Note that `id1`, `Id1`, `iD1`, and `ID1` are all different identifiers as they are [case-sensitive](https://en.wikipedia.org/wiki/Case_sensitivity "External link (opens in new tab)")
.

### [Escaping characters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#escaping_characters)

Any Unicode code point can be included as part of a `<custom-ident>` or quoted [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 by escaping it.

In CSS, there are several ways to escape a character. Escape sequences start with a backslash (`\`), and continue with:

*   One to six hex (`ABCDEF0123456789`) digits. The hex digits can optionally be followed by white space. The hex escape sequence gets replaced by the Unicode code point whose value is given by those digits. The whitespace allows the sequences to be followed by actual hex digits (versus replaced ones).
*   Any Unicode code point that is not a hex digit or a newline character.

Examples:

*   "&B" can be written as `\26 B` or `\000026B`.
*   "hi.there" can be written as `hi\.there` or `hi\002Ethere`.
*   "toto?" can be written as `toto\?`, `toto\3F`, or `toto\00003F`.

To include actual white space after an escape sequence, include two white spaces in the escape sequence.

### [Forbidden values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#forbidden_values)

A `<custom-ident>` must not be placed between single or double quotes as this would be identical to a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
. Moreover, the first character must not be a decimal digit, nor a hyphen (`-`) followed by a decimal digit.

To prevent ambiguity, each property that uses `<custom-ident>` forbids the use of specific values:

[`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)

Forbids the global CSS values (`unset`, `initial`, and `inherit`), as well as `none`.

[`counter-reset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
, [`counter-increment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)

Forbids the global CSS values (`unset`, `initial`, and `inherit`), as well as `none`.

[`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
, [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)

Forbids the global CSS values (`unset`, `initial`, and `inherit`), as well as the values:

*   `none`
*   `inline`
*   `outside`

Also, quite a few predefined values are implemented by the different browsers:

*   `disc`
*   `circle`
*   `square`
*   `decimal`
*   `cjk-decimal`
*   `decimal-leading-zero`
*   `lower-roman`
*   `upper-roman`
*   `lower-greek`
*   `lower-alpha`
*   `lower-latin`
*   `upper-alpha`
*   `upper-latin`
*   `arabic-indic`
*   `armenian`
*   `bengali`
*   `cambodian`
*   `cjk-earthly-branch`
*   `cjk-heavenly-stem`
*   `cjk-ideographic`
*   `devanagari`
*   `ethiopic-numeric`
*   `georgian`
*   `gujarati`
*   `gurmukhi`
*   `hebrew`
*   `hiragana`
*   `hiragana-iroha`
*   `japanese-formal`
*   `japanese-informal`
*   `kannada`
*   `katakana`
*   `katakana-iroha`
*   `khmer`
*   `korean-hangul-formal`
*   `korean-hanja-formal`
*   `korean-hanja-informal`
*   `lao`
*   `lower-armenian`
*   `malayalam`
*   `mongolian`
*   `myanmar`
*   `oriya`
*   `persian`
*   `simp-chinese-formal`
*   `simp-chinese-informal`
*   `tamil`
*   `telugu`
*   `thai`
*   `tibetan`
*   `trad-chinese-formal`
*   `trad-chinese-informal`
*   `upper-armenian`
*   `disclosure-open`
*   `disclosure-close`

[`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
, [`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
, [`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
, [`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
, [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
, [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)

Forbids the `span` and `auto` values.

[`view-transition-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)

Forbids the global CSS values (`unset`, `initial`, and `inherit`), as well as `none`.

[`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)

Forbids the global CSS values (`unset`, `initial`, and `inherit`), as well as the values `will-change`, `auto`, `scroll-position`, and `contents`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#examples)

----------------------------------------------------------------------------------------------------

### [Valid identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#valid_identifiers)

nono79            A mix of alphanumeric characters and numbers
ground-level      A mix of alphanumeric characters and a dash
-test             A dash followed by alphanumeric characters
\_internal         An underscore followed by alphanumeric characters
\\22 toto          A Unicode character followed by a sequence of alphanumeric characters
scooby\\.doo       A correctly escaped period

### [Invalid identifiers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#invalid_identifiers)

34rem             It must not start with a decimal digit.
-12rad            It must not start with a dash followed by a decimal digit.
scooby.doo        Only alphanumeric characters, \_, and - needn't be escaped.
'scoobyDoo'       This would be a <string>.
"scoobyDoo"       This would be a <string>.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# custom-idents](https://drafts.csswg.org/css-values/#custom-idents) |
| [CSS Will Change Module Level 1  <br>\# valdef-will-change-custom-ident](https://drafts.csswg.org/css-will-change/#valdef-will-change-custom-ident) |
| [CSS Counter Styles Level 3  <br>\# typedef-counter-style-name](https://drafts.csswg.org/css-counter-styles/#typedef-counter-style-name) |
| [CSS Lists and Counters Module Level 3  <br>\# counter-properties](https://drafts.csswg.org/css-lists/#counter-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

_As this type is not a real type but a convenience type used to simplify the description of allowed values, there is no browser compatibility information as such._

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident#see_also)

----------------------------------------------------------------------------------------------------

*   [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
*   [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/custom-ident/index.md?plain=1 "Folder: en-us/web/css/reference/values/custom-ident (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcustom-ident&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcustom-ident%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcustom-ident%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcustom-ident%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
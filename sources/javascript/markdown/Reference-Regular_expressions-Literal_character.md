*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#mdn-search)
    

Literal character: a, b
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **literal character** specifies exactly itself to be matched in the input text.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#syntax)

-------------------------------------------------------------------------------------------------------------------------

regex

    c
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#parameters)

[`c`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#c)

A single character that is not one of the syntax characters described below.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#description)

-----------------------------------------------------------------------------------------------------------------------------------

In regular expressions, most characters can appear literally. They are usually the most basic building blocks of patterns. For example, here is a pattern from the [Removing HTML tags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#removing_html_tags)
 example:

js

    const pattern = /<.+?>/g;
    

In this example, `.`, `+`, and `?` are called _syntax characters_. They have special meanings in regular expressions. The rest of the characters in the pattern (`<` and `>`) are literal characters. They match themselves in the input text: the left and right angle brackets.

The following characters are syntax characters in regular expressions, and they cannot appear as literal characters:

*   [`^`, `$`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
    
*   [`\`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    
*   [`.`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)
    
*   [`*`, `+`, `?`, `{`, `}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
    
*   [`(`, `)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
    
*   [`[`, `]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    
*   [`|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
    

Within character classes, more characters can appear literally. For more information, see the [Character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
 page. For example `\.` and `[.]` both match a literal `.`. In [`v`\-mode character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)
, however, there is a different set of characters reserved as syntax characters. To be most comprehensive, below is a table of ASCII characters and whether they may appear escaped or unescaped in different contexts, where "✅" means the character represents itself, "❌" means it throws a syntax error, and "⚠️" means the character is valid but means something other than itself.

| Characters | Outside character classes in `u` or `v` mode |     | In `u`\-mode character classes |     | In `v`\-mode character classes |     |
| --- | --- | --- | --- | --- | --- | --- |
| Unescaped | Escaped | Unescaped | Escaped | Unescaped | Escaped |
| --- | --- | --- | --- | --- | --- | --- |
| `123456789 "'   CEFGHIJKLMN   OPQRTUVXY_   aceghijklmop   quxy` | ✅   | ❌   | ✅   | ❌   | ✅   | ❌   |
| ``!#%&,:;<=>@`~`` | ✅   | ❌   | ✅   | ❌   | ✅   | ✅   |
| `]` | ❌   | ✅   | ❌   | ✅   | ❌   | ✅   |
| `()[{}` | ❌   | ✅   | ✅   | ✅   | ❌   | ✅   |\
| `*+?` | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   |\
| `/` | ✅   | ✅   | ✅   | ✅   | ❌   | ✅   |\
| `0DSWbdfnrstvw` | ✅   | ⚠️  | ✅   | ⚠️  | ✅   | ⚠️  |\
| `ABZz` | ✅   | ⚠️  | ✅   | ❌   | ✅   | ❌   |\
| `$.` | ⚠️  | ✅   | ✅   | ✅   | ✅   | ✅   |\
| `\|` | ⚠️  | ✅   | ✅   | ✅   | ❌   | ✅   |\
| `-` | ✅   | ❌   | ✅⚠️ | ✅   | ❌⚠️ | ✅   |\
| `^` | ⚠️  | ✅   | ✅⚠️ | ✅   | ✅⚠️ | ✅   |\
| `\` | ❌⚠️ | ✅   | ❌⚠️ | ✅   | ❌⚠️ | ✅   |\
\
**Note:** The characters that can both be escaped and unescaped in `v`\-mode character classes are exactly those forbidden as "double punctuators". See [`v`\-mode character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)\
 for more information.\
\
Whenever you want to match a syntax character literally, you need to [escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)\
 it with a backslash (`\`). For example, to match a literal `*` in a pattern, you need to write `\*` in the pattern. Using syntax characters as literal characters either leads to unexpected results or causes syntax errors — for example, `/*/` is not a valid regular expression because the quantifier is not preceded by a pattern. In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)\
, `]`, `{`, and `}` may appear literally if it's not possible to parse them as the end of a character class or quantifier delimiters. This is a [deprecated syntax for web compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
, and you should not rely on it.

Regular expression literals cannot be specified with certain non-syntax literal characters. `/` cannot appear as a literal character outside character classes in a regular expression literal, because `/` is used as the delimiter of the literal itself. You need to escape it as `\/` there if you want to match a literal `/`. Inside a character class, `/` can appear unescaped, as in `/[/]/` (unless the `v` flag is set). Line terminators cannot appear as literal characters in a regular expression literal either, because a literal cannot span multiple lines. You need to use a [character escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
 like `\n` instead. These delimiter and line-terminator restrictions do not apply when using the [`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
 constructor, although string literals have their own escaping rules (for example, `"\\"` actually denotes a single backslash character, so `new RegExp("\\*")` and `/\*/` are equivalent).

In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, the pattern is interpreted as a sequence of [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
. This means surrogate pairs actually represent two literal characters. This causes unexpected behaviors when paired with other features:

js

    /^[😄]$/.test("😄"); // false, because the pattern is interpreted as /^[\ud83d\ude04]$/
    /^😄+$/.test("😄😄"); // false, because the pattern is interpreted as /^\ud83d\ude04+$/
    

In Unicode-aware mode, the pattern is interpreted as a sequence of Unicode code points, and surrogate pairs do not get split. Therefore, you should always prefer to use the `u` flag.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#examples)

-----------------------------------------------------------------------------------------------------------------------------

### [Using literal characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#using_literal_characters)

The following example is copied from [Character escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#using_character_escapes)
. The `a` and `b` characters are literal characters in the pattern, and `\n` is an escaped character because it cannot appear literally in a regular expression literal.

js

    const pattern = /a\nb/;
    const string = `a
    b`;
    console.log(pattern.test(string)); // true
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-PatternCharacter](https://tc39.es/ecma262/multipage/text-processing.html#prod-PatternCharacter) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Character escape: `\n`, `\u{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/literal_character/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/literal_character (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FLiteral_character&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fliteral_character%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FLiteral_character%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fliteral_character%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
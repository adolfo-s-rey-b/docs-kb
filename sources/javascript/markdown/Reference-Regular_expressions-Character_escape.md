*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#mdn-search)
    

Character escape: \\n, \\u{...}
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **character escape** represents a character that may not be able to be conveniently represented in its literal form.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#syntax)

------------------------------------------------------------------------------------------------------------------------

regex

    \f, \n, \r, \t, \v
    \cA, \cB, …, \cz
    \0
    \^, \$, \\, \., \*, \+, \?, \(, \), \[, \], \{, \}, \|, \/
    
    \xHH
    \uHHHH
    \u{H…H}
    

**Note:** `,` is not part of the syntax.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#parameters)

[`H…H`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#h%E2%80%A6h)

A hexadecimal number representing the Unicode code point of the character. The `\xHH` form must have two hexadecimal digits; the `\uHHHH` form must have four; the `\u{H…H}` form must have one or more hexadecimal digits representing a value no greater than `0x10FFFF`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#description)

----------------------------------------------------------------------------------------------------------------------------------

The following character escapes are recognized in regular expressions:

[`\f`, `\n`, `\r`, `\t`, `\v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#f)

Same as those in [string literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#escape_sequences)
, except `\b`, which represents a [word boundary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
 in regexes unless in a [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
.

[`\c` followed by a letter from `A` to `Z` or `a` to `z`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#c)

Represents the control character with value equal to the letter's character value modulo 32. For example, `\cJ` represents line break (`\n`), because the code point of `J` is 74, and 74 modulo 32 is 10, which is the code point of line break. Because an uppercase letter and its lowercase form differ by 32, `\cJ` and `\cj` are equivalent. You can represent control characters from 1 to 26 in this form.

[`\0`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#0)

Represents the U+0000 NUL character. Cannot be followed by a digit (which makes it a [legacy octal escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#escape_sequences)
 sequence).

[`\^`, `\$`, `\\`, `\.`, `\*`, `\+`, `\?`, `\(`, `\)`, `\[`, `\]`, `\{`, `\}`, `\|`, `\/`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#sect)

Represents the character itself. For example, `\\` represents a backslash, and `\(` represents a left parenthesis. These are [syntax characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
 in regexes (`/` is the delimiter of a regex literal), so they require escaping unless in a [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
.

[`\xHH`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#xhh)

Represents the character with the given hexadecimal Unicode code point. The hexadecimal number must be exactly two digits long.

[`\uHHHH`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#uhhhh)

Represents the character with the given hexadecimal Unicode code point. The hexadecimal number must be exactly four digits long. Two such escape sequences can be used to represent a surrogate pair in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
. (In Unicode-unaware mode, they are always two separate characters.)

[`\u{H…H}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#uh%E2%80%A6h)

([Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
 only) Represents the character with the given hexadecimal Unicode code point. The hexadecimal number must have one or more digits and a value no greater than `0x10FFFF`. Leading zeros are allowed, so the number can be arbitrarily long.

In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, escape sequences that are not one of the above become _identity escapes_: they represent the character that follows the backslash. For example, `\a` represents the character `a`. This behavior limits the ability to introduce new escape sequences without causing backward compatibility issues, and is therefore forbidden in Unicode-aware mode.

In Unicode-unaware mode, `]`, `{`, and `}` may appear [literally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
 if it's not possible to parse them as the end of a character class or quantifier delimiters. This is a [deprecated syntax for web compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
, and you should not rely on it.

In Unicode-unaware mode, escape sequences within [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
 of the form `\cX` where `X` is a number or `_` are decoded in the same way as those with [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 letters: `\c0` is the same as `\cP` when taken modulo 32. In addition, if the form `\cX` is encountered anywhere where `X` is not one of the recognized characters, then the backslash is treated as a literal character. These syntaxes are also deprecated.

js

    /[\c0]/.test("\x10"); // true
    /[\c_]/.test("\x1f"); // true
    /[\c*]/.test("\\"); // true
    /\c/.test("\\c"); // true
    /\c0/.test("\\c0"); // true (the \c0 syntax is only supported in character classes)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#examples)

----------------------------------------------------------------------------------------------------------------------------

### [Using character escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#using_character_escapes)

Character escapes are useful when you want to match a character that is not easily represented in its literal form. For example, you cannot use a line break literally in a regex literal, so you must use a character escape:

js

    const pattern = /a\nb/;
    const string = `a
    b`;
    console.log(pattern.test(string)); // true
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#specifications)

----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-CharacterEscape](https://tc39.es/ecma262/multipage/text-processing.html#prod-CharacterEscape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape#see_also)

----------------------------------------------------------------------------------------------------------------------------

*   [Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Character class: `[...]`, `[^...]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    
*   [Character class escape: `\d`, `\D`, `\w`, `\W`, `\s`, `\S`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
    
*   [Literal character: `a`, `b`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
    
*   [Unicode character class escape: `\p{...}`, `\P{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
    
*   [Backreference: `\1`, `\2`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
    
*   [Named backreference: `\k<name>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_backreference)
    
*   [Word boundary assertion: `\b`, `\B`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/character_escape/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/character_escape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCharacter_escape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcharacter_escape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCharacter_escape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcharacter_escape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
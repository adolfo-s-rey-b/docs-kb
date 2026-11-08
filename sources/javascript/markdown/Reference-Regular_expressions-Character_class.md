*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#mdn-search)
    

Character class: \[...\], \[^...\]
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **character class** matches any character in or not in a custom set of characters. When the [`v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)
 flag is enabled, it can also be used to match finite-length strings.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#syntax)

-----------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#parameters)

[`operand1`, `operand2`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#operand1)

Can be a single character, another square-bracket-enclosed character class, a [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
, a [Unicode character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
, or a string using the `\q` syntax.

[`substring`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#substring)

A literal string.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#description)

---------------------------------------------------------------------------------------------------------------------------------

A character class specifies a list of characters between square brackets and matches any character in the list. The [`v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)
 flag drastically changes how character classes are parsed and interpreted. The following syntaxes are available in both `v` mode and non-`v` mode:

*   A single character: matches the character itself.
*   A range of characters: matches any character in the inclusive range. The range is specified by two characters separated by a dash (`-`). The first character must not be larger in character value than the second character. The _character value_ is the Unicode code point of the character. Because Unicode code points are usually assigned to alphabets in order, `[a-z]` specifies all lowercase Latin characters, while `[α-ω]` specifies all lowercase Greek characters. In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
    , regexes are interpreted as a sequence of [BMP](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#utf-16_characters_unicode_code_points_and_grapheme_clusters)
     characters. Therefore, surrogate pairs in character classes represent two characters instead of one; see below for details.
*   Escape sequences: `\b`, `\-`, [character class escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
    , [Unicode character class escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
    , and other [character escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    .

These syntaxes can occur any number of times, and the character sets they represent are unioned. For example, `/[a-zA-Z0-9]/` matches any letter or digit.

The `^` prefix in a character class creates a _complement class_. For example, `[^abc]` matches any character except `a`, `b`, or `c`. The `^` character is a literal character when it appears in the middle of a character class — for example, `[a^b]` matches the characters `a`, `^`, and `b`.

The [lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#regular_expression_literals)
 does a very rough parse of regex literals, so that it does not end the regex literal at a `/` character which appears within a character class. This means `/[/]/` is valid without needing to escape the `/`.

The boundaries of a character range must not specify more than one character, which happens if you use a [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
. For example:

In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, character ranges where one boundary is a character class make the `-` become a literal character. This is a [deprecated syntax for web compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
, and you should not rely on it.

In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, regexes are interpreted as a sequence of BMP characters. Therefore, surrogate pairs in character classes represent two characters instead of one.

Even if the pattern [ignores case](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)
, the case of the two ends of a range is significant in determining which characters belong to the range. For example, the pattern `/[E-F]/i` only matches `E`, `F`, `e`, and `f`, while the pattern `/[E-f]/i` matches all uppercase and lowercase [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 letters (because it spans over `E–Z` and `a–f`), as well as `[`, `\`, `]`, `^`, `_`, and `` ` ``.

### [Non-v-mode character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#non-v-mode_character_class)

Non-`v`\-mode character classes interpret most characters [literally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
 and have fewer restrictions about the characters they can contain. For example, `.` is the literal dot character, not the [wildcard](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)
. The only characters that cannot appear literally are `\`, `]`, and `-`.

*   In character classes, most escape sequences are supported, except `\b`, `\B`, and [backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
    . `\b` indicates a backspace character instead of a [word boundary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
    , while the other two cause syntax errors in Unicode-aware mode.
    
    In Unicode-unaware mode, `\B` is an identity escape for `B`, and numeric escapes are interpreted as legacy octal escapes or identity escapes instead of backreferences. For example, `\1` matches U+0001 and `\8` matches `8`. To use `\` literally, escape it as `\\`.
    
*   The `]` character indicates the end of the character class. To use it literally, escape it as `\]`.
    
*   The dash (`-`) character, when used between two characters, indicates a range. When it appears at the start or end of a character class, it is a literal character. It's also a literal character when it's used in the boundary of a range. For example, `[a-]` matches the characters `a` and `-`, `[!--]` matches the characters `!` to `-`, and `[--9]` matches the characters `-` to `9`. You can also escape it as `\-` if you want to use it literally anywhere.
    

### [v-mode character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)

The basic idea of character classes in `v` mode remains the same: you can still use most characters literally, use `-` to denote character ranges, and use escape sequences. One of the most important features of the `v` flag is _set notation_ within character classes. As previously mentioned, normal character classes can express unions by concatenating two ranges, such as using `[A-Z0-9]` to mean "the union of the set `[A-Z]` and the set `[0-9]`". However, there's no easy way to represent other operations with character sets, such as intersection and difference.

With the `v` flag, intersection is expressed with `&&`, and subtraction with `--`. The absence of both implies union. The two operands of `&&` or `--` can be a character, character escape, character class escape, or even another character class. For example, to express "a word character that's not an underscore", you can use `[\w--_]`. You cannot mix operators on the same level. For example, `[\w&&[A-z]--_]` is a syntax error. However, because you can nest character classes, you can be explicit by writing `[\w&&[[A-z]--_]]` or `[[\w&&[A-z]]--_]` (which both mean `[A-Za-z]`). Similarly, `[AB--C]` is invalid and you need to write `[A[B--C]]` (which just means `[AB]`).

In `v` mode, the [Unicode character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
 `\p` can match finite-length strings, such as emojis. For symmetry, regular character classes can also match more than one character. To write a "string literal" in a character class, you wrap the string in `\q{...}`. The only regex syntax supported here is [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
 — apart from this, `\q` must completely enclose literals (including escaped characters). This ensures that character classes can only match finite-length strings with finitely many possibilities.

Unlike regular disjunction, the order of alternatives within `\q` does not matter, neither does the order of the `\q` escape with the rest of the operands being unioned. During matching, all alternatives specified in a character class are always attempted in descending order of length, so the match is greedy. For example, `[\q{a|ab}]`, `[\q{ab|a}]`, `[\q{ab}a]`, and `[a\q{ab}]` applied to `"ab"` will all match `"ab"`.

Complement character classes `[^...]` cannot possibly be able to match strings longer than one character. For example, `[\q{ab|c}]` is valid and matches the string `"ab"`, but `[^\q{ab|c}]` is invalid because it's unclear how many characters should be consumed. The check is done by checking if all `\q` contain single characters and all `\p` specify character properties — for unions, all operands must be purely characters; for intersections, at least one operand must be purely characters; for subtraction, the leftmost operand must be purely characters. The check is syntactic without looking at the actual character set being specified, which means although `/[^\q{ab|c}--\q{ab}]/v` is equivalent to `/[^c]/v`, it's still rejected.

Because the character class syntax is now more sophisticated, more characters are reserved and forbidden from appearing literally.

*   In addition to `]` and `\`, the following characters must be escaped in character classes if they represent literal characters: `(`, `)`, `[`, `{`, `}`, `/`, `-`, `|`. This list is somewhat similar to the list of [syntax characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)\
    , except that `^`, `$`, `*`, `+`, and `?` are not reserved inside character classes, while `/` and `-` are not reserved outside character classes (although `/` may delimit a regex literal and therefore still needs to be escaped). All these characters may also be optionally escaped in `u`\-mode character classes.\
*   The following "double punctuator" sequences must be escaped as well (but they don't make much sense without the `v` flag anyway): `&&`, `!!`, `##`, `$$`, `%%`, `**`, `++`, `,,`, `..`, `::`, `;;`, `<<`, `==`, `>>`, `??`, `@@`, `^^`, ` `` `, `~~`. In `u` mode, some of these characters can only appear literally within character classes and cause a syntax error when escaped. In `v` mode, they must be escaped when appearing in pairs, but can be optionally escaped when appearing alone. For example, `/[\!]/u` is invalid because it's an [identity escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)\
    , but both `/[\!]/v` and `/[!]/v` are valid, while `/[!!]/v` is invalid. The [literal character](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)\
     reference has a detailed table of which characters can appear escaped or unescaped.\
\
### [Complement classes and case-insensitive matching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#complement_classes_and_case-insensitive_matching)\
\
[Case-insensitive](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)\
 matching works by case-folding both the expected character set and the matched string. When specifying complement classes, the order in which JavaScript performs case-folding and complementing is important. In brief, `[^...]` in `u` mode matches `allCharacters - caseFold(original)`, while in `v` mode matches `caseFold(allCharacters) - caseFold(original)`. This ensures that all complement class syntaxes, including `[^...]`, `\P`, `\W`, etc., cancel each other out.\
\
Consider the following two regexes (to simplify things, let's assume that Unicode characters are one of three kinds: lowercase, uppercase, and caseless, and each uppercase letter has a unique lowercase counterpart, and vice versa):\
\
The `r2` is a double negation and seems to be equivalent with `r1`. But in fact, `r1` matches all lower- and uppercase ASCII letters, while `r2` matches none. Here's a step-by-step explanation:\
\
*   In `r1`, `\p{Lowercase_Letter}` constructs a set of all lowercase characters. Characters in this set are then case-folded to their lowercase form, so they stay the same. The input string is also case-folded to lowercase. Therefore, `"A"` and `"a"` are both folded to `"a"` and matched by `r1`.\
*   In `r2`, `\P{Lowercase_Letter}` first constructs a set of all non-lowercase characters, i.e., uppercase letters and caseless characters. Characters in this set are then case-folded to their lowercase form, so the character set becomes all lowercase letters and caseless characters. `[^...]` negates the match, causing it to match anything that's _not_ in this set, i.e., an uppercase letter. However, the input is still case-folded to lowercase, so `"A"` is folded to `"a"` and not matched by `r2`.\
\
The main observation here is that after `[^...]` negates the match, the expected character set may not be a subset of the set of case-folded Unicode characters, causing the case-folded input to not be in the expected character set. In `v` mode, the set of all characters is also case-folded. The `\P` character class itself also works slightly differently in `v` mode (see [Unicode character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)\
). All of these ensure that `[^\P{Lowercase_Letter}]` and `\p{Lowercase_Letter}` are strictly equivalent.\
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#examples)\
\
---------------------------------------------------------------------------------------------------------------------------\
\
### [Matching hexadecimal digits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#matching_hexadecimal_digits)\
\
The following function determines whether a string contains a valid hexadecimal number:\
\
### [Using intersection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#using_intersection)\
\
The following function matches Greek letters.\
\
### [Using subtraction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#using_subtraction)\
\
The following function matches all non-ASCII numbers.\
\
### [Matching strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#matching_strings)\
\
The following function matches all line terminator sequences, including the [line terminator characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)\
 and the sequence `\r\n` (CRLF). The order in which the alternatives are specified does not matter, because the longest alternative, `\r\n`, is always preferred.\
\
This regular expression is exactly equivalent to `/(?:\r\n|\r|\n|\u2028|\u2029)/gu` or `/(?:\r\n|[\r\n\u2028\u2029])/gu`. However, in regular disjunction, the order of alternatives matters, so `\r\n` must be specified first in order for it to be preferred. Using a character class not only is shorter but also avoids this pitfall.\
\
The most useful case of `\q{}` is when doing subtraction and intersection. Previously, this was possible with [multiple lookaheads](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion#pattern_subtraction_and_intersection)\
. The following function matches flags that are not one of the American, Chinese, Russian, British, and French flags.\
\
This example is mostly equivalent to `/^(?!🇺🇸|🇨🇳|🇷🇺|🇬🇧|🇫🇷)\p{RGI_Emoji_Flag_Sequence}$/v`, except perhaps more performant.\
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#specifications)\
\
---------------------------------------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [ECMAScript® 2027 Language Specification  <br>\# prod-CharacterClass](https://tc39.es/ecma262/multipage/text-processing.html#prod-CharacterClass) |\
\
[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#browser_compatibility)\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#see_also)\
\
---------------------------------------------------------------------------------------------------------------------------\
\
*   [Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)\
     guide\
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)\
    \
*   [Character class escape: `\d`, `\D`, `\w`, `\W`, `\s`, `\S`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)\
    \
*   [Unicode character class escape: `\p{...}`, `\P{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)\
    \
*   [Literal character: `a`, `b`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)\
    \
*   [Character escape: `\n`, `\u{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)\
    \
*   [Disjunction: `|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)\
    \
*   [RegExp v flag with set notation and properties of strings](https://v8.dev/features/regexp-v-flag "External link (opens in new tab)")\
     on v8.dev (2022)\
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/character_class/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/character_class (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCharacter_class&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcharacter_class%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCharacter_class%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcharacter_class%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
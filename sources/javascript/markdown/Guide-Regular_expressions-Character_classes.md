*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#mdn-search)
    

Character classes
=================

Character classes distinguish kinds of characters such as, for example, distinguishing between letters and digits.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#try_it)

---------------------------------------------------------------------------------------------------------------------

[Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#types)

-------------------------------------------------------------------------------------------------------------------

| Characters | Meaning |
| --- | --- |
| `[xyz]   [a-c]` | [**Character class:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)<br> Matches any one of the enclosed characters. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first or last character enclosed in the square brackets, it is taken as a literal hyphen to be included in the character class as a normal character.<br><br>For example, `[abcd]` is the same as `[a-d]`. They match the "b" in "brisket", and the "c" in "chop".<br><br>For example, `[abcd-]` and `[-abcd]` match the "b" in "brisket", the "c" in "chop", and the "-" (hyphen) in "non-profit".<br><br>For example, `[\w-]` is the same as `[A-Za-z0-9_-]`. They both match the "b" in "brisket", the "c" in "chop", and the "n" in "non-profit".<br><br>When the [`unicodeSets`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)<br> (`v`) flag is enabled, the character class has some additional features. See the [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)<br> reference for more information. |
| `[^xyz]   [^a-c]` | [**Negated character class:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)<br> Matches anything that is not enclosed in the square brackets. You can specify a range of characters by using a hyphen, but if the hyphen appears as the first character after the `^` or the last character enclosed in the square brackets, it is taken as a literal hyphen to be included in the character class as a normal character. For example, `[^abc]` is the same as `[^a-c]`. They initially match "o" in "bacon" and "h" in "chop".<br><br>**Note:** The ^ character may also indicate the [beginning of input](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)<br>. |
| `.` | [**Wildcard:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)<br> Matches any single character _except_ line terminators: `\n`, `\r`, `\u2028` or `\u2029`. For example, `/.y/` matches "my" and "ay", but not "yes", in "yes make my day", as there is no character before "y" in "yes". If the [`dotAll`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/dotAll)<br> (s) flag is enabled, also matches line terminators. Inside a character class, the dot loses its special meaning and matches a literal dot. |
| `\d` | [**Digit character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches any digit (Arabic numeral). Equivalent to `[0-9]`. For example, `/\d/` or `/[0-9]/` matches "2" in "B2 is the suite number". |
| `\D` | [**Non-digit character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches any character that is not a digit (Arabic numeral). Equivalent to `[^0-9]`. For example, `/\D/` or `/[^0-9]/` matches "B" in "B2 is the suite number". |
| `\w` | [**Word character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches any alphanumeric character from the basic Latin alphabet, including the underscore. Equivalent to `[A-Za-z0-9_]`. For example, `/\w/` matches "a" in "apple", "5" in "$5.28", "3" in "3D" and "m" in "Émanuel". |
| `\W` | [**Non-word character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches any character that is not a word character from the basic Latin alphabet. Equivalent to `[^A-Za-z0-9_]`. For example, `/\W/` or `/[^A-Za-z0-9_]/` matches "%" in "50%" and "É" in "Émanuel". |
| `\s` | [**White space character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches a single white space character, including space, tab, form feed, line feed, and other Unicode spaces. Equivalent to `[\f\n\r\t\v\u0020\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]`. For example, `/\s\w*/` matches " bar" in "foo bar". |
| `\S` | [**Non-white space character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)<br> Matches a single character other than white space. Equivalent to `[^\f\n\r\t\v\u0020\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]`. For example, `/\S\w*/` matches "foo" in "foo bar". |
| `\t` | Matches a horizontal tab. |
| `\r` | Matches a carriage return. |
| `\n` | Matches a linefeed. |
| `\v` | Matches a vertical tab. |
| `\f` | Matches a form-feed. |
| `[\b]` | Matches a backspace. If you're looking for the word-boundary assertion (`\b`), see [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)<br>. |
| `\0` | Matches a NUL character. Do not follow this with another digit. |
| `\c_X_` | Matches a control character using [caret notation](https://en.wikipedia.org/wiki/Caret_notation "External link (opens in new tab)")<br>, where "X" is a letter from A–Z or a–z (corresponding to code points `U+0001`_–_`U+001A`). For example, `/\cM\cJ/` matches "\\r\\n". |
| `\x_hh_` | [**Hex escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)<br> Matches the character with the code `_hh_` (two hexadecimal digits). |
| `\u_HHHH_` | [**Unicode escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)<br> Matches a UTF-16 code-unit with the value `_HHHH_` (four hexadecimal digits). |
| `\u{_H…H_}` | [**Unicode code point escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)<br> Matches the character with the Unicode value `U+_H…H_` (1 to 6 hexadecimal digits). Only valid in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)<br>. |
| `\p{_UnicodeProperty_}`, `\P{_UnicodeProperty_}` | [**Unicode character class escape:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)<br> Matches a character based on its Unicode character properties: for example, emoji characters, or Japanese _katakana_ characters, or Chinese/Japanese Han/Kanji characters, etc.). Only valid in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)<br>. |
| `\` | Indicates that the following character should be treated specially, or "escaped". It behaves one of two ways.<br><br>*   For characters that are usually treated literally, indicates that the next character is special and not to be interpreted literally. For example, `/b/` matches the character "b". By placing a backslash in front of "b", that is by using `/\b/`, the character becomes special to mean match a word boundary.<br>*   For characters that are usually treated specially, indicates that the next character is not special and should be interpreted literally. For example, "\*" is a special character that means 0 or more occurrences of the preceding character should be matched; for example, `/a*/` means match 0 or more "a"s. To match `*` literally, precede it with a backslash; for example, `/a\*/` matches "a\*".<br><br>**Note:** To match this character literally, escape it with itself. In other words to search for `\` use `/\\/`. |
| `_x_\|_y_` | [**Disjunction:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)<br> Matches either "x" or "y". Each component, separated by a pipe (`\|`), is called an _alternative_. For example, `/green\|red/` matches "green" in "green apple" and "red" in "red apple".<br><br>**Note:** A disjunction is another way to specify "a set of choices", but it's not a character class. Disjunctions are not atoms — you need to use a [group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)<br> to make it part of a bigger pattern. `[abc]` is functionally equivalent to `(?:a\|b\|c)`. |

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#examples)

-------------------------------------------------------------------------------------------------------------------------

### [Looking for a series of digits](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#looking_for_a_series_of_digits)

In this example, we match a sequence of 4 digits with `\d{4}`. `\b` indicates a [word boundary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)
 (i.e., do not start or end matching in the middle of a number sequence).

See more examples in the [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
 reference.

### [Looking for a word (from the latin alphabet) starting with A](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#looking_for_a_word_from_the_latin_alphabet_starting_with_a)

In this example, we match a word starting with the letter A. `\b` indicates a [word boundary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)
 (i.e., do not start matching in the middle of a word). `[aA]` indicates the letter "a" or "A". `\w+` indicates any character _from the Latin alphabet_, multiple times (`+` is a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)
). Note that because we already match until there are no more word characters, an end `\b` boundary is not necessary.

See more examples in the [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
 reference.

### [Looking for a word (from Unicode characters)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#looking_for_a_word_from_unicode_characters)

Instead of the Latin alphabet, we can use a range of Unicode characters to identify a word (thus being able to deal with text in other languages like Russian or Arabic). The "Basic Multilingual Plane" of Unicode contains most of the characters used around the world and we can use character classes and ranges to match words written with those characters.

See more examples in the [Unicode character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
 reference.

### [Counting vowels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#counting_vowels)

In this example, we count the number of vowels (A, E, I, O, U, Y) in a text. The `g` flag is used to match all occurrences of the pattern in the text. The `i` flag is used to make the pattern case-insensitive, so it matches both uppercase and lowercase vowels.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#see_also)

-------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     guide
*   [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)
     guide
*   [Quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)
     guide
*   [Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
     guide
*   [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
    
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     reference
*   [Character class: `[...]`, `[^...]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    
*   [Character class escape: `\d`, `\D`, `\w`, `\W`, `\s`, `\S`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
    
*   [Character escape: `\n`, `\u{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    
*   [Disjunction: `|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
    
*   [Unicode character class escape: `\p{...}`, `\P{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
    
*   [Wildcard: `.`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/regular_expressions/character_classes/index.md?plain=1 "Folder: en-us/web/javascript/guide/regular_expressions/character_classes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRegular_expressions%2FCharacter_classes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fregular_expressions%2Fcharacter_classes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRegular_expressions%2FCharacter_classes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fregular_expressions%2Fcharacter_classes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8f53af45fae665627a95ac50e177b15d0228b920%0A*+Document+last+modified%3A+2026-08-27T23%3A56%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
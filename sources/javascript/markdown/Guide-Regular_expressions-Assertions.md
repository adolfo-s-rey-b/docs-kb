*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#mdn-search)
    

Assertions
==========

Assertions include boundaries, which indicate the beginnings and endings of lines and words, and other patterns indicating in some way that a match is possible (including look-ahead, look-behind, and conditional expressions).

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#try_it)

--------------------------------------------------------------------------------------------------------------

[Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#types)

------------------------------------------------------------------------------------------------------------

### [Boundary-type assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#boundary-type_assertions)

| Characters | Meaning |
| --- | --- |
| `^` | [**Input boundary beginning assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)<br> Matches the beginning of input. If the [`multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)<br> (m) flag is enabled, also matches immediately after a line break character. For example, `/^A/` does not match the "A" in "an A", but does match the first "A" in "An A".<br><br>**Note:** This character has a different meaning when it appears at the start of a [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)<br>. |
| `$` | [**Input boundary end assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)<br> Matches the end of input. If the [`multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)<br> (m) flag is enabled, also matches immediately before a line break character. For example, `/t$/` does not match the "t" in "eater", but does match it in "eat". |
| `\A` | [**Buffer boundary start assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion)<br> Matches the start of the entire string regardless of the presence of the `m` flag. Only valid in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)<br>. |
| `\z` | [**Buffer boundary end assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion)<br> Matches the end of the entire string regardless of the presence of the `m` flag. Only valid in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)<br>. |
| `\Z` | [**Buffer boundary end assertion with optional newline:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion)<br> Matches the end of the entire string, but allows an optional trailing newline character sequence (either a [line terminator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)<br> or a `\r\n` sequence). Only valid in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)<br>. |
| `\b` | [**Word boundary assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)<br> Matches a word boundary. This is the position where a word character is not followed or preceded by another word-character, such as between a letter and a space. Note that a matched word boundary is not included in the match. In other words, the length of a matched word boundary is zero.<br><br>Examples:<br><br>*   `/\bm/` matches the "m" in "moon".<br>*   `/oo\b/` does not match the "oo" in "moon", because "oo" is followed by "n" which is a word character.<br>*   `/oon\b/` matches the "oon" in "moon", because "oon" is the end of the string, thus not followed by a word character.<br>*   `/\w\b\w/` will never match anything, because a word character can never be followed by both a non-word and a word character.<br><br>To match a backspace character (`[\b]`), see [Character Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)<br>. |
| `\B` | [**Non-word-boundary assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)<br> Matches a non-word boundary. This is a position where the previous and next character are of the same type: Either both must be words, or both must be non-words, for example between two letters or between two spaces. The beginning and end of a string are considered non-words. Same as the matched word boundary, the matched non-word boundary is also not included in the match. For example, `/\Bon/` matches "on" in "at noon", and `/ye\B/` matches "ye" in "possibly yesterday". |

### [Other assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#other_assertions)

**Note:** The `?` character may also be used as a quantifier.

| Characters | Meaning |
| --- | --- |
| `x(?=y)` | [**Lookahead assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)<br> Matches "x" only if "x" is followed by "y". For example, `/Jack(?=Sprat)/` matches "Jack" only if it is followed by "Sprat".  <br>`/Jack(?=Sprat\|Frost)/` matches "Jack" only if it is followed by "Sprat" or "Frost". However, neither "Sprat" nor "Frost" is part of the match results. |
| `x(?!y)` | [**Negative lookahead assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)<br> Matches "x" only if "x" is not followed by "y". For example, `/\d+(?!\.)/` matches a number only if it is not followed by a decimal point. `/\d+(?!\.)/.exec('3.141')` matches "141" but not "3". |
| `(?<=y)x` | [**Lookbehind assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)<br> Matches "x" only if "x" is preceded by "y". For example, `/(?<=Jack)Sprat/` matches "Sprat" only if it is preceded by "Jack". `/(?<=Jack\|Tom)Sprat/` matches "Sprat" only if it is preceded by "Jack" or "Tom". However, neither "Jack" nor "Tom" is part of the match results. |
| `(?<!y)x` | [**Negative lookbehind assertion:**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)<br> Matches "x" only if "x" is not preceded by "y". For example, `/(?<!-)\d+/` matches a number only if it is not preceded by a minus sign. `/(?<!-)\d+/.exec('3')` matches "3". `/(?<!-)\d+/.exec('-3')` match is not found because the number is preceded by the minus sign. |

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#examples)

------------------------------------------------------------------------------------------------------------------

### [General boundary-type overview example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#general_boundary-type_overview_example)

### [Matching the beginning of input using a ^ control character](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#matching_the_beginning_of_input_using_a_control_character)

Use `^` for matching at the beginning of input. In this example, we can get the fruits that start with 'A' by a `/^A/` regex. For selecting appropriate fruits we can use the [`filter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
 method with an [arrow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
 function.

In the second example `^` is used both for matching at the beginning of input and for creating negated or complemented character class when used within [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
.

See more examples in the [input boundary assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
 reference.

### [Matching a word boundary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#matching_a_word_boundary)

In this example, we match fruit names containing a word that ends in "en" or "ed".

See more examples in the [word boundary assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
 reference.

### [Lookahead assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#lookahead_assertion)

In this example, we match the word "First" only if it is followed by the word "test", but we do not include "test" in the match results.

See more examples in the [lookahead assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
 reference.

### [Basic negative lookahead assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#basic_negative_lookahead_assertion)

For example, `/\d+(?!\.)/` matches a number only if it is not followed by a decimal point. `/\d+(?!\.)/.exec('3.141')` matches "141" but not "3".

See more examples in the [lookahead assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
 reference.

### [Different meaning of '?!' combination usage in assertions and character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#different_meaning_of_!_combination_usage_in_assertions_and_character_classes)

The `?!` combination has different meanings in assertions like `/x(?!y)/` and [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
 like `[^?!]`.

### [Lookbehind assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#lookbehind_assertion)

In this example, we replace the word "orange" with "apple" only if it is preceded by the word "ripe".

See more examples in the [lookbehind assertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)
 reference.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     guide
*   [Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
     guide
*   [Quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)
     guide
*   [Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
     guide
*   [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
    
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     reference
*   [Input boundary assertion: `^`, `$`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
    
*   [Lookahead assertion: `(?=...)`, `(?!...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
    
*   [Lookbehind assertion: `(?<=...)`, `(?<!...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)
    
*   [Word boundary assertion: `\b`, `\B`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/regular_expressions/assertions/index.md?plain=1 "Folder: en-us/web/javascript/guide/regular_expressions/assertions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRegular_expressions%2FAssertions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fregular_expressions%2Fassertions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FRegular_expressions%2FAssertions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fregular_expressions%2Fassertions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff4174abd45aefde55b6d45144c57ec3c2dc037a1%0A*+Document+last+modified%3A+2026-10-08T11%3A37%3A24.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
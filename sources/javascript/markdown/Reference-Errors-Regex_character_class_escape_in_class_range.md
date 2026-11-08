*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#mdn-search)
    

SyntaxError: character class escape cannot be used in class range in regular expression
=======================================================================================

The JavaScript exception "character class escape cannot be used in class range in regular expression" occurs when a [Unicode-aware](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
 regular expression pattern contains a [character class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
 where a boundary of a character range is another character class, such as a [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#message)

----------------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid regular expression: /\[\\s-1\]/u: Invalid character class (V8-based)
SyntaxError: character class escape cannot be used in class range in regular expression (Firefox)
SyntaxError: Invalid regular expression: invalid range in character class for Unicode pattern (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#error_type)

----------------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------------------------------

A character class can specify a range of characters by using a hyphen (`-`) between two characters. For example, `[a-z]` matches any lowercase letter from `a` to `z`. The two bounds of the range must represent single characters in order for the range to make sense. If one of the bounds actually represents multiple characters, an error is generated. In [non-`v`\-mode character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#non-v-mode_character_class)
, only character class escapes are allowed inside character classes; in [`v`\-mode character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)
, this can also happen if one the bounds is another `[...]` character class.

In Unicode-unaware mode, this syntax causes the `-` to become a literal character instead of generating an error, but this is a [deprecated syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
 and you should not rely on it.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#examples)

------------------------------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#invalid_cases)

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#valid_cases)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range#see_also)

------------------------------------------------------------------------------------------------------------------------------------------

*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Character class: `[...]`, `[^...]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Regex_character_class_escape_in_class_range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/regex_character_class_escape_in_class_range/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/regex_character_class_escape_in_class_range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_character_class_escape_in_class_range&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_character_class_escape_in_class_range%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRegex_character_class_escape_in_class_range%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fregex_character_class_escape_in_class_range%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa055fad7a07ef41ec3c8f90a3f1d2ad65f22826c%0A*+Document+last+modified%3A+2026-09-01T17%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
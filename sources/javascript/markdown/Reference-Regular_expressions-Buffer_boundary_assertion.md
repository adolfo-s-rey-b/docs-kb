*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#mdn-search)
    

Buffer boundary assertion: \\A, \\z, \\Z
========================================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#browser_compatibility)
 carefully before using this in production.

A **buffer boundary assertion** checks if the current position in the string is strictly at the start or end of the entire string (`\Z` also allows a trailing newline), regardless of the presence of the [`m`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)
 flag (which changes the meanings of the `^` and `$` [input boundary assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
). It's only supported in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#syntax)

---------------------------------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#description)

-------------------------------------------------------------------------------------------------------------------------------------------

`\A` asserts that the current position is the start of the entire string. `\z` asserts that the current position is the end of the entire string. `\Z` is like `\z`, but also matches before a [line terminator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
 or `\r\n` (CRLF) sequence at the end of the string. All of them are _assertions_, so they don't consume any characters.

More precisely, `\A` asserts that the character to the left is out of bounds of the string; `\z` asserts that the character to the right is out of bounds of the string; `\Z` is equivalent to `(?=(?:\r?\n?|[\u{2028}\u{2029}]?)\z)`.

These assertions only make sense when no characters are expected to the left or right of them. For example, `f\Ao` never matches because it's not possible for `\A` to both be at the start of the string and have a character to its left.

The `\A` and `\z` assertions are only useful when the `m` flag is used. Without `m`, they behave just like `^` and `$`. If your pattern only needs to match the start or end of the entire string or a line (and never a mix of both), the recommended approach is to still use the `^` and `$` assertions, and set the `m` flag as needed, because they are more widely supported than the buffer boundary assertions. If you need to match both types of boundaries in the same pattern, you can technically use [modifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier)
 to enable or disable the `m` flag in different parts of the pattern, but using these escape sequences makes the code much more readable.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#examples)

-------------------------------------------------------------------------------------------------------------------------------------

### [Mixing buffer and input boundary assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#mixing_buffer_and_input_boundary_assertions)

Suppose you have a pattern that needs to match either at the start of the whole string or the start of one line. You can turn on `m` so that you can use `^` to refer to the latter, and then use `\A` to refer to the former (you also need to turn on `u` so you can use `\A`).

This example matches line comments on their own lines, which can be a [hashbang](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#hashbang_comments)
 at start of a file or a line comment on any line. It does not match line comments at the end of a line containing code.

Another major use case of buffer boundary assertions is when you cannot modify the flags, such as regular expression search in text editors. These cases usually enable `m` by default, so you need to use `\A` and `\z` to "opt out".

### [Matching the end-of-file but allowing an optional trailing newline](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#matching_the_end-of-file_but_allowing_an_optional_trailing_newline)

File formats often allow an optional newline at the end of the file. If you want to match an end-of-file pattern that allows the trailing newline, you can use `\Z`. This feature is useful with or without the `m` flag.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Regular Expression Buffer Boundaries for ECMAScript  <br>\# sec-patterns](https://tc39.es/proposal-regexp-buffer-boundaries/#sec-patterns) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion#see_also)

-------------------------------------------------------------------------------------------------------------------------------------

*   [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Assertions)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Input boundary assertion: `^`, `$`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
    
*   [Word boundary assertion: `\b`, `\B`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Word_boundary_assertion)
    
*   [Lookahead assertion: `(?=...)`, `(?!...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
    
*   [Lookbehind assertion: `(?<=...)`, `(?<!...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Buffer_boundary_assertion/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/buffer_boundary_assertion/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/buffer_boundary_assertion (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FBuffer_boundary_assertion&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fbuffer_boundary_assertion%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FBuffer_boundary_assertion%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fbuffer_boundary_assertion%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
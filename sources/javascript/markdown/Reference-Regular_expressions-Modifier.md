*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#mdn-search)
    

Modifier: (?ims-ims:...)
========================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **modifier** overrides [flag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#regex_flags)
 settings in a specific part of a regular expression. It can be used to enable or disable flags that change the meanings of certain regex syntax elements. These flags are [`i`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)
, [`m`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)
, and [`s`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/dotAll)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#syntax)

----------------------------------------------------------------------------------------------------------------

**Note:** JavaScript only has the "bounded" modifier form, where the pattern is placed inside the modifier group. Most other languages that support modifiers have an "unbounded" form, where the modifier is applied until the end of the closest containing group.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#parameters)

[`flags1` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#flags1)

A string of flags to enable. Can contain any combination of `i`, `m`, and `s`.

[`flags2` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#flags2)

A string of flags to disable. Can contain any combination of `i`, `m`, and `s`, but must not contain any flags included in `flags1`.

[`pattern`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#pattern)

A pattern consisting of anything you may use in a regex literal, including a [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#description)

--------------------------------------------------------------------------------------------------------------------------

Some flags change the meanings of regex syntax elements:

*   The [`i`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)
     flag makes the regex case-insensitive by normalizing the case of [literal characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
     and [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    .
*   The [`m`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)
     flag changes the behavior of [input boundary assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Input_boundary_assertion)
     `^` and `$` to match the start and end of each line, in addition to the start and end of the input string.
*   The [`s`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/dotAll)
     flag changes the behavior of the [wildcard](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Wildcard)
     `.` character to match any character, including line terminators.

Sometimes you may want these changes to only take effect in a specific part of a regex pattern. You can do so by wrapping that part in a modifier. For example:

In this regex, the `i` flag is only enabled for the `Hello` part of the pattern. The `world` part is case-sensitive. Therefore, it matches `Hello world`, `hello world`, and `HELLO world`, but not `HELLO WORLD`. The following is equivalent, by enabling the `i` flag globally, and then disabling it for the `world` part:

The `flags1` and `flags2` parameters can contain any combination of `i`, `m`, and `s`. However, the flags must all be unique between `flags1` and `flags2`—you cannot enable or disable a flag twice, or enable a flag and then immediately disable it.

The `flags1` and `flags2` parameters are optional, but at least one must be non-empty. `(?flags1-:pattern)` is a modifier that only enables flags (equivalent to `(?flags1:pattern)`). `(?-flags2:pattern)` is a modifier that only disables flags. `(?:pattern)` is just a [non-capturing group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
, and `(?-:pattern)` is a syntax error.

Other flags don't make sense in a modifier and are thus syntax errors if included:

*   The [`g`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
     and [`y`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/sticky)
     flags determine how multiple calls to [`exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
     behave and affect matching behavior of the whole regex.
*   The [`d`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/hasIndices)
     flag enables additional information in the [`exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
     result and affects matching behavior of the whole regex.
*   The [`u`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode)
     and [`v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)
     flags change the behavior of the regex engine in a way that's too complex to be locally modified. They also have global effects on the regex, such as how the [`lastIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex)
     is advanced.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#examples)

--------------------------------------------------------------------------------------------------------------------

### [Matching a multiline format only at the start of the string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#matching_a_multiline_format_only_at_the_start_of_the_string)

The following regex defines a format for a multiline string. The first `^` represents the start of the whole input string, by being inside a `(?-m:)` modifier, while all other `^` characters represent the start of a line:

### [Matching certain words case-insensitively](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#matching_certain_words_case-insensitively)

Imagine you are finding all variable declarations called `foo` or `bar` (because they are bad names). The word may appear in any case, but you know the keyword is always lowercase, so you can do this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#specifications)

--------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-RegularExpressionModifiers](https://tc39.es/ecma262/multipage/text-processing.html#prod-RegularExpressionModifiers) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier#see_also)

--------------------------------------------------------------------------------------------------------------------

*   [Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Non-capturing group: `(?:...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Modifier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/modifier/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/modifier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FModifier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fmodifier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FModifier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fmodifier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
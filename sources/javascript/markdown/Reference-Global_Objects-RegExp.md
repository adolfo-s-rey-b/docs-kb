*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#mdn-search)
    

RegExp
======

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`RegExp`** object is used for matching text with a pattern.

For an introduction to regular expressions, read the [Regular expressions chapter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
 in the JavaScript guide. For detailed information of regular expression syntax, read the [regular expression reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#description)

-------------------------------------------------------------------------------------------------------------------

### [Literal notation and constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#literal_notation_and_constructor)

There are two ways to create a `RegExp` object: a _literal notation_ and a _constructor_.

*   The _literal notation_ takes a pattern between two slashes, followed by optional [flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)
    , after the second slash.
*   The _constructor function_ takes either a string or a `RegExp` object as its first parameter and a string of optional [flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)
     as its second parameter.

The following three expressions create the same regular expression object:

Before regular expressions can be used, they have to be compiled. This process allows them to perform matches more efficiently. More about the process can be found in [dotnet docs](https://learn.microsoft.com/en-us/dotnet/standard/base-types/compilation-and-reuse-in-regular-expressions "External link (opens in new tab)")
.

The literal notation results in compilation of the regular expression when the expression is evaluated. On the other hand, the constructor of the `RegExp` object, `new RegExp('ab+c')`, results in runtime compilation of the regular expression.

Use a string as the first argument to the `RegExp()` constructor when you want to [build the regular expression from dynamic input](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#building_a_regular_expression_from_dynamic_inputs)
.

### [Flags in constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#flags_in_constructor)

The expression `new RegExp(/ab+c/, flags)` will create a new `RegExp` using the source of the first parameter and the [flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)
 provided by the second.

When using the constructor function, the normal string escape rules (preceding special characters with `\` when included in a string) are necessary.

For example, the following are equivalent:

### [Special handling for regexes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#special_handling_for_regexes)

**Note:** Whether something is a "regex" can be [duck-typed](https://en.wikipedia.org/wiki/Duck_typing "External link (opens in new tab)")
. It doesn't have to be a `RegExp`!

Some built-in methods would treat regexes specially. They decide whether `x` is a regex through [multiple steps](https://tc39.es/ecma262/multipage/abstract-operations.html#sec-isregexp "External link (opens in new tab)")
:

1.  `x` must be an object (not a primitive).
2.  If [`x[Symbol.match]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/match)
     is not `undefined`, check if it's [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
    .
3.  Otherwise, if `x[Symbol.match]` is `undefined`, check if `x` had been created with the `RegExp` constructor. (This step should rarely happen, since if `x` is a `RegExp` object that have not been tampered with, it should have a `Symbol.match` property.)

Note that in most cases, it would go through the `Symbol.match` check, which means:

*   An actual `RegExp` object whose `Symbol.match` property's value is [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
     but not `undefined` (even with everything else intact, like [`exec`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
     and [`[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.replace)
    ) can be used as if it's not a regex.
*   A non-`RegExp` object with a `Symbol.match` property will be treated as if it's a regex.

This choice was made because `[Symbol.match]()` is the most indicative property that something is intended to be used for matching. (`exec` could also be used, but because it's not a symbol property, there would be too many false positives.) The places that treat regexes specially include:

*   [`String.prototype.endsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)
    , [`startsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith)
    , and [`includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)
     throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
     if the first argument is a regex.
*   [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
     and [`replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
     check whether the [global](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
     flag is set if the first argument is a regex before invoking its [`[Symbol.matchAll]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/matchAll)
     or [`[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/replace)
     method.
*   The [`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
     constructor directly returns the `pattern` argument only if `pattern` is a regex (among a few other conditions). If `pattern` is a regex, it would also interrogate `pattern`'s `source` and `flags` properties instead of coercing `pattern` to a string.

For example, [`String.prototype.endsWith()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)
 would coerce all inputs to strings, but it would throw if the argument is a regex, because it's only designed to match strings, and using a regex is likely a developer mistake.

You can get around the check by setting `[Symbol.match]` to a [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
 value that's not `undefined`. This would mean that the regex cannot be used for `String.prototype.match()` (since without `[Symbol.match]`, `match()` would construct a new `RegExp` object with the two enclosing slashes added by [`re.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/toString)
), but it can be used for virtually everything else.

### [Perl-like RegExp properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#perl-like_regexp_properties)

Note that several of the `RegExp` properties have both long and short (Perl-like) names. Both names always refer to the same value. (Perl is the programming language from which JavaScript modeled its regular expressions.) See also [deprecated `RegExp` properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#constructor)

-------------------------------------------------------------------------------------------------------------------

[`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)

Creates a new `RegExp` object.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#static_properties)

-------------------------------------------------------------------------------------------------------------------------------

[`RegExp.$1`, …, `RegExp.$9`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/n)

Static read-only properties that contain parenthesized substring matches.

[`RegExp.input` (`$_`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/input)

A static property that contains the last string against which a regular expression was successfully matched.

[`RegExp.lastMatch` (`$&`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastMatch)

A static read-only property that contains the last matched substring.

[`RegExp.lastParen` (`$+`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastParen)

A static read-only property that contains the last parenthesized substring match.

[`RegExp.leftContext` (`` $` ``)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/leftContext)

A static read-only property that contains the substring preceding the most recent match.

[`RegExp.rightContext` (`$'`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/rightContext)

A static read-only property that contains the substring following the most recent match.

[`RegExp[Symbol.species]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.species)

The constructor function that is used to create derived objects.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#static_methods)

-------------------------------------------------------------------------------------------------------------------------

[`RegExp.escape()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/escape)

[Escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#escape_sequences)
 any potential regex syntax characters in a string, and returns a new string that can be safely used as a [literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
 pattern for the [`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
 constructor.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#instance_properties)

-----------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `RegExp.prototype` and shared by all `RegExp` instances.

[`RegExp.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `RegExp` instances, the initial value is the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
 constructor.

[`RegExp.prototype.dotAll`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/dotAll)

Whether `.` matches newlines or not.

[`RegExp.prototype.flags`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/flags)

A string that contains the flags of the `RegExp` object.

[`RegExp.prototype.global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)

Whether to test the regular expression against all possible matches in a string, or only against the first.

[`RegExp.prototype.hasIndices`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/hasIndices)

Whether the regular expression result exposes the start and end indices of captured substrings.

[`RegExp.prototype.ignoreCase`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)

Whether to ignore case while attempting a match in a string.

[`RegExp.prototype.multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)

Whether or not to search in strings across multiple lines.

[`RegExp.prototype.source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/source)

The text of the pattern.

[`RegExp.prototype.sticky`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/sticky)

Whether or not the search is sticky.

[`RegExp.prototype.unicode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode)

Whether or not Unicode features are enabled.

[`RegExp.prototype.unicodeSets`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)

Whether or not the `v` flag, an upgrade to the `u` mode, is enabled.

These properties are own properties of each `RegExp` instance.

[`lastIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex)

The index at which to start the next match.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#instance_methods)

-----------------------------------------------------------------------------------------------------------------------------

[`RegExp.prototype.compile()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/compile)

(Re-)compiles a regular expression during execution of a script.

[`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)

Executes a search for a match in its string parameter.

[`RegExp.prototype.test()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)

Tests for a match in its string parameter.

[`RegExp.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/toString)

Returns a string representing the specified object. Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`RegExp.prototype[Symbol.match]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.match)

Performs match to given string and returns match result.

[`RegExp.prototype[Symbol.matchAll]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.matchAll)

Returns all matches of the regular expression against a string.

[`RegExp.prototype[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.replace)

Replaces matches in given string with new substring.

[`RegExp.prototype[Symbol.search]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.search)

Searches the match in given string and returns the index the pattern found in the string.

[`RegExp.prototype[Symbol.split]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.split)

Splits given string into an array by separating the string into substrings.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#examples)

-------------------------------------------------------------------------------------------------------------

### [Using a regular expression to change data format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#using_a_regular_expression_to_change_data_format)

The following script uses the [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
 method to match a name in the format _first last_ and output it in the format _last, first_.

In the replacement text, the script uses `$1` and `$2` to indicate the results of the corresponding matching parentheses in the regular expression pattern.

This displays `"Cruz, Maria"`.

### [Using regular expression to split lines with different line endings/ends of line/line breaks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#using_regular_expression_to_split_lines_with_different_line_endingsends_of_lineline_breaks)

The default line ending varies depending on the platform (Unix, Windows, etc.). The line splitting provided in this example works on all platforms.

Note that the order of the patterns in the regular expression matters.

### [Using regular expression on multiple lines](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#using_regular_expression_on_multiple_lines)

By default, the `.` character does not match newlines. To make it match newlines, use the `s` flag (`dotAll` mode).

### [Using a regular expression with the sticky flag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#using_a_regular_expression_with_the_sticky_flag)

The [`sticky`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/sticky)
 flag indicates that the regular expression performs sticky matching in the target string by attempting to match starting at [`RegExp.prototype.lastIndex`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex)
.

### [The difference between the sticky flag and the global flag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#the_difference_between_the_sticky_flag_and_the_global_flag)

With the sticky flag `y`, the next match has to happen at the `lastIndex` position, while with the global flag `g`, the match can happen at the `lastIndex` position or later:

With the global flag `g`, all 6 digits would be matched, not just 3.

### [Regular expression and Unicode characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#regular_expression_and_unicode_characters)

`\w` and `\W` only matches ASCII based characters; for example, `a` to `z`, `A` to `Z`, `0` to `9`, and `_`.

To match characters from other languages such as Cyrillic or Hebrew, use `\uHHHH`, where `HHHH` is the character's Unicode value in hexadecimal.

This example demonstrates how one can separate out Unicode characters from a word.

The [Unicode property escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape)
 feature provides a simpler way to target particular Unicode ranges, by allowing for statements like `\p{scx=Cyrl}` (to match any Cyrillic letter), or `\p{L}/u` (to match a letter from any language).

### [Extracting subdomain name from URL](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#extracting_subdomain_name_from_url)

**Note:** Instead of using regular expressions for parsing URLs, it is usually better to use the browsers built-in URL parser by using the [URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL_API)
.

### [Building a regular expression from dynamic inputs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#building_a_regular_expression_from_dynamic_inputs)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-regexp-regular-expression-objects](https://tc39.es/ecma262/multipage/text-processing.html#sec-regexp-regular-expression-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

### [Firefox-specific notes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#firefox-specific_notes)

Starting with Firefox 34, in the case of a capturing group with quantifiers preventing its exercise, the matched text for a capturing group is now `undefined` instead of an empty string:

Note that due to web compatibility, `RegExp.$N` will still return an empty string instead of `undefined` ([bug 1053944](https://bugzil.la/1053944 "External link (opens in new tab)")
).

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Polyfill of many modern `RegExp` features (`dotAll`, `sticky` flags, named capture groups, etc.) in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
    
*   [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
    
*   [`String.prototype.split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/regexp/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/regexp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
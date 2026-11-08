*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#mdn-search)
    

Named capturing group: (?<name>...)
===================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **named capturing group** is a particular kind of [capturing group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
 that allows you to give a name to the group. The group's matching result can later be identified by this name instead of by its index in the pattern.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#syntax)

-----------------------------------------------------------------------------------------------------------------------------

regex

    (?<name>pattern)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#parameters)

[`pattern`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#pattern)

A pattern consisting of anything you may use in a regex literal, including a [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#name)

The name of the group. Must be a valid [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#description)

---------------------------------------------------------------------------------------------------------------------------------------

Named capturing groups can be used just like capturing groups — they also have their match index in the result array, and they can be referenced through `\1`, `\2`, etc. The only difference is that they can be _additionally_ referenced by their name. The information of the capturing group's match can be accessed through:

*   The `groups` property of the return value of [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
    , or [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
     when the regex does not have the `g` flag
*   The `groups` property of each match array yielded by the iterator returned by [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
    
*   The `groups` parameter of the [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
     and [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
     methods' `replacement` callback function
*   [Named backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_backreference)
     within the same pattern

All names must be unique within the same pattern. Multiple named capturing groups with the same name result in a syntax error.

js

    /(?<name>)(?<name>)/; // SyntaxError: Invalid regular expression: Duplicate capture group name
    

This restriction is relaxed if the duplicate named capturing groups are not in the same [disjunction alternative](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
, so for any string input, only one named capturing group can actually be matched. This is a much newer feature, so check [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#browser_compatibility)
 before using it.

js

    /(?<year>\d{4})-\d{2}|\d{2}-(?<year>\d{4})/;
    // Works; "year" can either come before or after the hyphen
    

Named capturing groups will all be present in the result. If a named capturing group is not matched (for example, it belongs to an unmatched alternative in a [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
), the corresponding property on the `groups` object has value `undefined`.

js

    /(?<ab>ab)|(?<cd>cd)/.exec("cd").groups; // [Object: null prototype] { ab: undefined, cd: 'cd' }
    

You can get the start and end indices of each named capturing group in the input string by using the [`d`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/hasIndices)
 flag. In addition to accessing them on the `indices` property on the array returned by `exec()`, you can also access them by their names on `indices.groups`.

Compared to unnamed capturing groups, named capturing groups have the following advantages:

*   They allow you to provide a descriptive name for each submatch result.
*   They allow you to access submatch results without having to remember the order in which they appear in the pattern.
*   When refactoring code, you can change the order of capturing groups without worrying about breaking other references.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#examples)

---------------------------------------------------------------------------------------------------------------------------------

### [Using named capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#using_named_capturing_groups)

The following example parses a timestamp and an author name from a Git log entry (output with `git log --format=%ct,%an -- filename`):

js

    function parseLog(entry) {
      const { author, timestamp } = /^(?<timestamp>\d+),(?<author>.+)$/.exec(
        entry,
      ).groups;
      return `${author} committed on ${new Date(
        parseInt(timestamp, 10) * 1000,
      ).toLocaleString()}`;
    }
    
    parseLog("1560979912,Caroline"); // "Caroline committed on 6/19/2019, 5:31:52 PM"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#specifications)

---------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-Atom](https://tc39.es/ecma262/multipage/text-processing.html#prod-Atom) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group#see_also)

---------------------------------------------------------------------------------------------------------------------------------

*   [Polyfill of named capturing groups in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Capturing group: `(...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
    
*   [Non-capturing group: `(?:...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
    
*   [Named backreference: `\k<name>`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_backreference)
    
*   [ESLint rule: `prefer-named-capture-group`](https://eslint.org/docs/latest/rules/prefer-named-capture-group "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/named_capturing_group/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/named_capturing_group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FNamed_capturing_group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fnamed_capturing_group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FNamed_capturing_group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fnamed_capturing_group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
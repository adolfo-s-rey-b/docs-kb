*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#mdn-search)
    

Capturing group: (...)
======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **capturing group** groups a subpattern, allowing you to apply a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
 to the entire group or use [disjunctions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
 within it. It memorizes information about the subpattern match, so that you can refer back to it later with a [backreference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
, or access the information through the [match results](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec#return_value)
.

If you don't need the result of the subpattern match, use a [non-capturing group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
 instead, which improves performance and avoids refactoring hazards.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#syntax)

-----------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#parameters)

[`pattern`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#pattern)

A pattern consisting of anything you may use in a regex literal, including a [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#description)

---------------------------------------------------------------------------------------------------------------------------------

A capturing group acts like the [grouping operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping)
 in JavaScript expressions, allowing you to use a subpattern as a single [atom](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms)
.

Capturing groups are numbered by the order of their opening parentheses. The first capturing group is numbered `1`, the second `2`, and so on. [Named capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
 are also capturing groups and are numbered together with other (unnamed) capturing groups. The information of the capturing group's match can be accessed through:

*   The return value (which is an array) of [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
    , or [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
     when the regex does not have the `g` flag
*   Each match array yielded by the iterator returned by [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
    
*   The `pN` parameters of the [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
     and [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
     methods' `replacement` callback function
*   [Backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
     within the same pattern

**Note:** Even in `exec()`'s result array, capturing groups are accessed by numbers `1`, `2`, etc., because the `0` element is the entire match. `\0` is not a backreference, but a [character escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
 for the NUL character.

Capturing groups in the regex source code correspond to their results one-to-one. If a capturing group is not matched (for example, it belongs to an unmatched alternative in a [disjunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
), the corresponding result is `undefined`.

Capturing groups can be [quantified](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
. In this case, the match information corresponding to this group is the last match of the group.

Capturing groups can be used in [lookahead](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
 and [lookbehind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookbehind_assertion)
 assertions. Because lookbehind assertions match their atoms backwards, the final match corresponding to this group is the one that appears to the _left_ end of the string. However, the indices of the match groups still correspond to their relative locations in the regex source.

Capturing groups can be nested, in which case the outer group is numbered first, then the inner group, because they are ordered by their opening parentheses. If a nested group is repeated by a quantifier, then each time the group matches, the subgroups' results are all overwritten, sometimes with `undefined`.

In the example above, the outer group is matched three times:

1.  Matches `"aac"`, with subgroups `"aa"`, `undefined`, and `"c"`.
2.  Matches `"bbbc"`, with subgroups `undefined`, `"bbb"`, and `"c"`.
3.  Matches `"ac"`, with subgroups `"a"`, `undefined`, and `"c"`.

The `"bbb"` result from the second match is not preserved, because the third match overwrites it with `undefined`.

You can get the start and end indices of each capturing group in the input string by using the [`d`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/hasIndices)
 flag. This creates an extra `indices` property on the array returned by `exec()`.

You can optionally specify a name to a capturing group, which helps avoid pitfalls related to group positions and indexing. See [Named capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
 for more information.

Parentheses have other purposes in different regex syntaxes. For example, they also enclose lookahead and lookbehind assertions. Because these syntaxes all start with `?`, and `?` is a [quantifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier)
 which normally cannot occur directly after `(`, this does not lead to ambiguities.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#examples)

---------------------------------------------------------------------------------------------------------------------------

### [Matching date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#matching_date)

The following example matches a date in the format `YYYY-MM-DD`:

### [Pairing quotes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#pairing_quotes)

The following function matches the `title='xxx'` and `title="xxx"` patterns in a string. To ensure the quotes match, we use a backreference to refer to the first quote. Accessing the second capturing group (`[2]`) returns the string between the matching quote characters:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#specifications)

---------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-Atom](https://tc39.es/ecma262/multipage/text-processing.html#prod-Atom) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group#see_also)

---------------------------------------------------------------------------------------------------------------------------

*   [Groups and backreferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Non-capturing group: `(?:...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
    
*   [Named capturing group: `(?<name>...)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Named_capturing_group)
    
*   [Backreference: `\1`, `\2`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Backreference)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/capturing_group/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/capturing_group (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCapturing_group&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcapturing_group%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FCapturing_group%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fcapturing_group%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
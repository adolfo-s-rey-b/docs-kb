*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#mdn-search)
    

Quantifier: \*, +, ?, {n}, {n,}, {n,m}
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **quantifier** repeats an [atom](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms)
 a certain number of times. The quantifier is placed after the atom it applies to.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#syntax)

------------------------------------------------------------------------------------------------------------------

**Note:** Adding `?` after `{count}` is syntactically valid but practically useless. Since `{count}` always matches exactly `count` times, `atom{count}?` behaves the same as `atom{count}`.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#parameters)

[`atom`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#atom)

A single [atom](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms)
.

[`count`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#count)

A non-negative integer. The number of times the atom should be repeated.

[`min`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#min)

A non-negative integer. The minimum number of times the atom can be repeated.

[`max` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#max)

A non-negative integer. The maximum number of times the atom can be repeated. If omitted, the atom can be repeated as many times as needed.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#description)

----------------------------------------------------------------------------------------------------------------------------

A quantifier is placed after an [atom](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#atoms)
 to repeat it a certain number of times. It cannot appear on its own. Each quantifier is able to specify a minimum and maximum number that a pattern must be repeated for.

| Quantifier | Minimum | Maximum |
| --- | --- | --- |
| `?` | 0   | 1   |
| `*` | 0   | Infinity |
| `+` | 1   | Infinity |
| `{count}` | `count` | `count` |
| `{min,}` | `min` | Infinity |
| `{min,max}` | `min` | `max` |

For the `{count}`, `{min,}`, and `{min,max}` syntaxes, there cannot be white spaces around the numbers — otherwise, it becomes a [literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Literal_character)
 pattern.

This behavior is fixed in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, where braces cannot appear literally without [escaping](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
. The ability to use `{` and `}` literally without escaping is a [deprecated syntax for web compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
, and you should not rely on it.

It is a syntax error if the minimum is greater than the maximum.

Quantifiers can cause [capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group)
 to match multiple times. See the capturing groups page for more information on the behavior in this case.

Each repeated match doesn't have to be the same string.

Quantifiers are _greedy_ by default, which means they try to match as many times as possible until the maximum is reached, or until it's not possible to match further. You can make a quantifier _non-greedy_ by adding a `?` after it. In this case, the quantifier will try to match as few times as possible, only matching more times if it's impossible to match the rest of the pattern with this many repetitions.

However, as soon as the regex successfully matches the string at some index, it will not try subsequent indices, although that may result in fewer characters being consumed.

Greedy quantifiers may try fewer repetitions if it's otherwise impossible to match the rest of the pattern.

In this example, `[ab]+` first greedily matches `"abb"`, but `[abc]c` is not able to match the rest of the pattern (`"c"`), so the quantifier is reduced to match only `"ab"`.

Greedy quantifiers avoid matching infinitely many empty strings. If the minimum number of matches is reached and no more characters are being consumed by the atom at this position, the quantifier stops matching. This is why `/(a*)*/.exec("b")` does not result in an infinite loop.

Greedy quantifiers try to match as many _times_ as possible; they do not maximize the _length_ of the match. For example, `/(aa|aabaac|ba)*/.exec("aabaac")` matches `"aa"` and then `"ba"` instead of `"aabaac"`.

Quantifiers apply to a single atom. If you want to quantify a longer pattern or a disjunction, you must [group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Non-capturing_group)
 it. Quantifiers cannot be applied to [assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions#assertions)
.

In [Unicode-unaware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, [lookahead assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion)
 can be quantified. This is a [deprecated syntax for web compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#regexp)
, and you should not rely on it.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#examples)

----------------------------------------------------------------------------------------------------------------------

### [Removing HTML tags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#removing_html_tags)

The following example removes HTML tags enclosed in angle brackets. Note the use of `?` to avoid consuming too many characters at once.

The same effect can be achieved with a greedy match, but not allowing the repeated pattern to match `>`.

**Warning:** This is for demonstration only — it doesn't handle `>` in attribute values. Use a proper HTML sanitizer like the [HTML sanitizer API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Sanitizer_API)
 instead.

### [Locating Markdown paragraphs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#locating_markdown_paragraphs)

In Markdown, paragraphs are separated by one or more blank lines. The following example counts all paragraphs in a string by matching two or more line breaks.

**Warning:** This is for demonstration only — it doesn't handle line breaks in code blocks or other Markdown block elements like headings. Use a proper Markdown parser instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-Quantifier](https://tc39.es/ecma262/multipage/text-processing.html#prod-Quantifier) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Quantifiers)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Disjunction: `|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
    
*   [Character class: `[...]`, `[^...]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Quantifier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/quantifier/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/quantifier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FQuantifier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fquantifier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FQuantifier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Fquantifier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
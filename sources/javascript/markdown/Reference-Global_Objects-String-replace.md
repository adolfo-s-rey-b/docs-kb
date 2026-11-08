*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#mdn-search)
    

String.prototype.replace()
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`replace()`** method of [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
 values returns a new string with one, some, or all matches of a `pattern` replaced by a `replacement`. The `pattern` can be a string or a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
, and the `replacement` can be a string or a function called for each match. If `pattern` is a string, only the first occurrence will be replaced. The original string is left unchanged.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#try_it)

-----------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#syntax)

-----------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#parameters)

[`pattern`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#pattern)

Can be a string or an object with a [`Symbol.replace`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/replace)
 method — the typical example being a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
. Any value that doesn't have the `Symbol.replace` method will be coerced to a string.

[`replacement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#replacement)

Can be a string or a function.

*   If it's a string, it will replace the substring matched by `pattern`. A number of special replacement patterns are supported; see the [Specifying a string as the replacement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifying_a_string_as_the_replacement)
     section below.
*   If it's a function, it will be invoked for every match and its return value is used as the replacement text. The arguments supplied to this function are described in the [Specifying a function as the replacement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifying_a_function_as_the_replacement)
     section below.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#return_value)

A new string, with one, some, or all matches of the pattern replaced by the specified replacement.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#description)

---------------------------------------------------------------------------------------------------------------------------

This method does not mutate the string value it's called on. It returns a new string.

A string pattern will only be replaced once. To perform a global search and replace, use a regular expression with the `g` flag, or use [`replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
 instead.

If `pattern` is an object with a [`Symbol.replace`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/replace)
 method (including `RegExp` objects), that method is called with the target string and `replacement` as arguments. Its return value becomes the return value of `replace()`. In this case the behavior of `replace()` is entirely encoded by the `[Symbol.replace]()` method — for example, any mention of "capturing groups" in the description below is actually functionality provided by [`RegExp.prototype[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.replace)
.

If the `pattern` is an empty string, the replacement is prepended to the start of the string.

A regexp with the `g` flag is the only case where `replace()` replaces more than once. For more information about how regex properties (especially the [sticky](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/sticky)
 flag) interact with `replace()`, see [`RegExp.prototype[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.replace)
.

### [Specifying a string as the replacement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifying_a_string_as_the_replacement)

The replacement string can include the following special replacement patterns:

| Pattern | Inserts |
| --- | --- |
| `$$` | Inserts a `"$"`. |
| `$&` | Inserts the matched substring. |
| `` $` `` | Inserts the portion of the string that precedes the matched substring. |
| `$'` | Inserts the portion of the string that follows the matched substring. |
| `$n` | Inserts the `n`th (`1`\-indexed) capturing group where `n` is a positive integer less than 100. |
| `$<Name>` | Inserts the named capturing group where `Name` is the group name. |

`$n` and `$<Name>` are only available if the `pattern` argument is a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 object. If the `pattern` is a string, or if the corresponding capturing group isn't present in the regex, then the pattern will be replaced as a literal. If the group is present but isn't matched (because it's part of a disjunction), it will be replaced with an empty string.

### [Specifying a function as the replacement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifying_a_function_as_the_replacement)

You can specify a function as the second parameter. In this case, the function will be invoked after the match has been performed. The function's result (return value) will be used as the replacement string.

**Note:** The above-mentioned special replacement patterns do _not_ apply for strings returned from the replacer function.

The function has the following signature:

The arguments to the function are as follows:

[`match`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#match)

The matched substring. (Corresponds to `$&` above.)

[`p1`, `p2`, …, `pN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#p1)

The `n`th string found by a capture group (including named capturing groups), provided the first argument to `replace()` is a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 object. (Corresponds to `$1`, `$2`, etc. above.) For example, if the `pattern` is `/(\a+)(\b+)/`, then `p1` is the match for `\a+`, and `p2` is the match for `\b+`. If the group is part of a disjunction (e.g., `"abc".replace(/(a)|(b)/, replacer)`), the unmatched alternative will be `undefined`.

[`offset`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#offset)

The offset of the matched substring within the whole string being examined. For example, if the whole string was `'abcd'`, and the matched substring was `'bc'`, then this argument will be `1`.

[`string`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#string)

The whole string being examined.

[`groups`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#groups)

An object whose keys are the used group names, and whose values are the matched portions (`undefined` if not matched). Only present if the `pattern` contains at least one named capturing group.

The exact number of arguments depends on whether the first argument is a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 object — and, if so, how many capture groups it has.

The following example will set `newString` to `'abc - 12345 - #$*%'`:

The function will be invoked multiple times for each full match to be replaced if the regular expression in the first parameter is global.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#examples)

---------------------------------------------------------------------------------------------------------------------

### [Defining the regular expression in replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#defining_the_regular_expression_in_replace)

In the following example, the regular expression is defined in `replace()` and includes the ignore case flag.

This logs `'Twas the night before Christmas...'`.

**Note:** See [the regular expression guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
 for more explanations about regular expressions.

### [Using the global and ignoreCase flags with replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#using_the_global_and_ignorecase_flags_with_replace)

Global replace can only be done with a regular expression. In the following example, the regular expression includes the [global and ignore case flags](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags)
 which permits `replace()` to replace each occurrence of `'apples'` in the string with `'oranges'`.

This logs `'oranges are round, and oranges are juicy'`.

### [Switching words in a string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#switching_words_in_a_string)

The following script switches the words in the string. For the replacement text, the script uses [capturing groups](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences)
 and the `$1` and `$2` replacement patterns.

This logs `'Cruz, Maria'`.

### [Using an inline function that modifies the matched characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#using_an_inline_function_that_modifies_the_matched_characters)

In this example, all occurrences of capital letters in the string are converted to lower case, and a hyphen is inserted just before the match location. The important thing here is that additional operations are needed on the matched item before it is given back as a replacement.

The replacement function accepts the matched snippet as its parameter, and uses it to transform the case and concatenate the hyphen before returning.

Given `styleHyphenFormat('borderTop')`, this returns `'border-top'`.

Because we want to further transform the _result_ of the match before the final substitution is made, we must use a function. This forces the evaluation of the match prior to the [`toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
 method. If we had tried to do this using the match without a function, the [`toLowerCase()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
 would have no effect.

This is because `'$&'.toLowerCase()` would first be evaluated as a string literal (resulting in the same `'$&'`) before using the characters as a pattern.

### [Replacing a Fahrenheit degree with its Celsius equivalent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#replacing_a_fahrenheit_degree_with_its_celsius_equivalent)

The following example replaces a Fahrenheit degree with its equivalent Celsius degree. The Fahrenheit degree should be a number ending with `"F"`. The function returns the Celsius number ending with `"C"`. For example, if the input number is `"212F"`, the function returns `"100C"`. If the number is `"0F"`, the function returns `"-17.77777777777778C"`.

The regular expression `test` checks for any number that ends with `F`. The number of Fahrenheit degrees is accessible to the function through its second parameter, `p1`. The function sets the Celsius number based on the number of Fahrenheit degrees passed in a string to the `f2c()` function. `f2c()` then returns the Celsius number. This function approximates Perl's `s///e` flag.

### [Making a generic replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#making_a_generic_replacer)

Suppose we want to create a replacer that appends the offset data to every matched string. Because the replacer function already receives the `offset` parameter, it will be trivial if the regex is statically known.

However, this replacer would be hard to generalize if we want it to work with any regex pattern. The replacer is _variadic_ — the number of arguments it receives depends on the number of capturing groups present. We can use [rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
, but it would also collect `offset`, `string`, etc. into the array. The fact that `groups` may or may not be passed depending on the identity of the regex would also make it hard to generically know which argument corresponds to the `offset`.

The `addOffset` example above doesn't work when the regex contains a named group, because in this case `args.at(-2)` would be the `string` instead of the `offset`.

Instead, you need to extract the last few arguments based on type, because `groups` is an object while `string` is a string.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.prototype.replace](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.replace) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.prototype.replace` in `core-js` with fixes and implementation of modern behavior like `Symbol.replace` support](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
     guide
*   [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
    
*   [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
    
*   [`RegExp.prototype.exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
    
*   [`RegExp.prototype.test()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)
    
*   [`Symbol.replace`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/replace)
    
*   [`RegExp.prototype[Symbol.replace]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.replace)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/replace/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/replace (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Freplace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Freplace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Freplace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Freplace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
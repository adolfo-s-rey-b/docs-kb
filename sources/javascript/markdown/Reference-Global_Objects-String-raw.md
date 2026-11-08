*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#mdn-search)
    

String.raw()
============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`String.raw()`** static method is a tag function of [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
. This is similar to the `r` prefix in Python, or the `@` prefix in C# for string literals. It's used to get the raw string form of template literals — that is, substitutions (e.g., `${foo}`) are processed, but escape sequences (e.g., `\n`) are not.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#try_it)

-------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#syntax)

-------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#parameters)

[`strings`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#strings)

Well-formed template literal array object, like `{ raw: ['foo', 'bar', 'baz'] }`. Should be an object with a `raw` property whose value is an array-like object of strings.

[`sub1`, …, `subN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#sub1)

Contains substitution values.

[`templateString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#templatestring)

A [template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
, optionally with substitutions (`${...}`).

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#return_value)

The raw string form of a given template literal.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#exceptions)

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

Thrown if the first argument doesn't have a `raw` property, or the `raw` property is `undefined` or `null`.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#description)

-----------------------------------------------------------------------------------------------------------------------

In most cases, `String.raw()` is used with template literals. The first syntax mentioned above is only rarely used, because the JavaScript engine will call this with proper arguments for you, (just like with other [tag functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
).

`String.raw()` is the only built-in template literal tag. It has close semantics to an untagged literal since it concatenates all arguments and returns a string. You can even re-implement it with normal JavaScript code.

**Warning:** You should not use `String.raw` directly as an "identity" tag. See [Building an identity tag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#building_an_identity_tag)
 for how to implement this.

If `String.raw()` is called with an object whose `raw` property doesn't have a `length` property or a non-positive `length`, it returns an empty string `""`. If `substitutions.length < strings.raw.length - 1` (i.e., there are not enough substitutions to fill the placeholders — which can't happen in a well-formed tagged template literal), the rest of the placeholders are filled with empty strings.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using String.raw()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#using_string.raw)

### [Raw strings containing template literal syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#raw_strings_containing_template_literal_syntax)

`String.raw` is a function, so it cannot circumvent basic template literal syntax such as backticks as delimiters and `${` for substitutions. If you want to include these characters in the output string, you need to escape them with backslashes. However, since `String.raw` outputs raw strings, the backslashes will be preserved in the output.

To work around this, you can use a substitution to insert these characters.

This approach works for `String.raw` because it just concatenates the raw strings and the substitutions. In general, unfortunately, there's no way for a template literal tag to receive a `raw` string that contains unescaped template literal syntax.

### [Using String.raw with RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#using_string.raw_with_regexp)

Combining a `String.raw` template literal with the [`RegExp()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/RegExp)
 constructor allows you to create regular expressions with dynamic parts (which is not possible with regex literals) without double-escaping (`\\`) regular expression escape sequences (which is not possible with normal string literals). This is also valuable in strings that contain a lot of slashes, such as file paths or URLs.

### [Building an identity tag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#building_an_identity_tag)

Many tools give special treatment to literals tagged by a particular name.

One might naïvely implement the `html` tag as:

This, in fact, works for the case above. However, because `String.raw` would concatenate the _raw_ string literals instead of the "cooked" ones, escape sequences would not be processed.

This may not be what you want for a "true identity" tag, where the tag is purely for markup and doesn't change the literal's value. In this case, you can create a custom tag and pass the "cooked" (i.e., escape sequences are processed) literal array to `String.raw`, pretending they are raw strings.

Notice the first argument is an object with a `raw` property, whose value is an array-like object (with a `length` property and integer indexes) representing the separated strings in the template literal. The rest of the arguments are the substitutions. Since the `raw` value can be any array-like object, it can even be a string! For example, `'test'` is treated as `['t', 'e', 's', 't']`. The following is equivalent to `` `t${0}e${1}s${2}t` ``:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-string.raw](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.raw) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `String.raw` in `core-js`](https://core-js.io/docs/features/ecmascript/string-regexp "External link (opens in new tab)")
    
*   [es-shims polyfill of `String.raw`](https://www.npmjs.com/package/string.raw "External link (opens in new tab)")
    
*   [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
    
*   [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
    
*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/string/raw/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/string/raw (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fraw&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fraw%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString%2Fraw%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fstring%2Fraw%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
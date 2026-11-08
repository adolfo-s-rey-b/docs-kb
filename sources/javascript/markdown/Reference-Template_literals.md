*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#mdn-search)
    

Template literals (Template strings)
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Template literals** are literals delimited with backtick (`` ` ``) characters, allowing for [multi-line strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#multi-line_strings)
, [string interpolation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#string_interpolation)
 with embedded expressions, and special constructs called [tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
.

Template literals are sometimes informally called _template strings_, because they are used most commonly for [string interpolation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#string_interpolation)
 (to create strings by doing substitution of placeholders). However, a tagged template literal may not result in a string; it can be used with a custom [tag function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
 to perform whatever operations you want on the different parts of the template literal.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#syntax)

-----------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#parameters)

[`string text`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#string_text)

The string text that will become part of the template literal. Almost all characters are allowed literally, including [line breaks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
 and other [whitespace characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#white_space)
. However, invalid escape sequences will cause a syntax error, unless a [tag function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates_and_escape_sequences)
 is used.

[`expression`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#expression)

An expression to be inserted in the current position, whose value is converted to a string or passed to `tagFunction`.

[`tagFunction`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagfunction)

If specified, it will be called with the template strings array and substitution expressions, and the return value becomes the value of the template literal. See [tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#description)

---------------------------------------------------------------------------------------------------------------

Template literals are enclosed by backtick (`` ` ``) characters instead of double or single quotes.

Along with having normal strings, template literals can also contain other parts called _placeholders_, which are embedded expressions delimited by a dollar sign and curly braces: `${expression}`. The strings and placeholders get passed to a function — either a default function, or a function you supply. The default function (when you don't supply your own) just performs [string interpolation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#string_interpolation)
 to do substitution of the placeholders and then concatenate the parts into a single string.

To supply a function of your own, precede the template literal with a function name; the result is called a [**tagged template**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)
. In that case, the template literal is passed to your tag function, where you can then perform whatever operations you want on the different parts of the template literal.

To escape a backtick in a template literal, put a backslash (`\`) before the backtick.

Dollar signs can be escaped as well to prevent interpolation.

### [Multi-line strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#multi-line_strings)

Any newline characters inserted in the source are part of the template literal.

Using normal strings, you would have to use the following syntax in order to get multi-line strings:

Using template literals, you can do the same with this:

Like [normal string literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#escape_sequences)
, you can write a single-line string across multiple lines for source code readability, by escaping the newline with a backslash (`\`):

### [String interpolation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#string_interpolation)

Without template literals, when you want to combine output from expressions with strings, you'd [concatenate them](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Strings#concatenation_using)
 using the [addition operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
 `+`:

That can be hard to read – especially when you have multiple expressions.

With template literals, you can avoid the concatenation operator — and improve the readability of your code — by using placeholders of the form `${expression}` to perform substitutions for embedded expressions:

Note that there's a mild difference between the two syntaxes. Template literals [coerce their expressions directly to strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_coercion)
, while addition coerces its operands to primitives first. For more information, see the reference page for the [`+` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
.

### [Nesting templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#nesting_templates)

In certain cases, nesting a template is the easiest (and perhaps more readable) way to have configurable strings. Within a backtick-delimited template, it is simple to allow inner backticks by using them inside an `${expression}` placeholder within the template.

For example, without template literals, if you wanted to return a certain value based on a particular condition, you could do something like the following:

With a template literal but without nesting, you could do this:

With nesting of template literals, you can do this:

### [Tagged templates](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)

_Tagged_ templates are a more advanced form of template literals.

Tags allow you to parse template literals with a function. The first argument of a tag function contains an array of string values. The remaining arguments are related to the expressions.

The tag function can then perform whatever operations on these arguments you wish, and return the manipulated string. (Alternatively, it can return something completely different, as described in one of the following examples.)

The name of the function used for the tag can be whatever you want.

The tag does not have to be a plain identifier. You can use any expression with [precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence#table)
 greater than 16, which includes [property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
, function call, [new expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, or even another tagged template literal.

While technically permitted by the syntax, _untagged_ template literals are strings and will throw a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 when chained.

The only exception is optional chaining, which will throw a syntax error.

Note that these two expressions are still parsable. This means they would not be subject to [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
, which will only insert semicolons to fix code that's otherwise unparsable.

Tag functions don't even need to return a string!

The first argument received by the tag function is an array of strings. For any template literal, its length is equal to the number of substitutions (occurrences of `${…}`) plus one, and is therefore always non-empty.

For any particular tagged template literal expression, the tag function will always be called with the exact same literal array, no matter how many times the literal is evaluated.

This allows the tag to cache the result based on the identity of its first argument. To further ensure the array value's stability, the first argument and its [`raw` property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#raw_strings)
 are both [frozen](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isFrozen)
, so you can't mutate them in any way.

### [Raw strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#raw_strings)

The special `raw` property, available on the first argument to the tag function, allows you to access the raw strings as they were entered, without processing [escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#using_special_characters_in_strings)
.

**Note:** The template literal syntax is still processed in the same way, which means unescaped backticks and `${` have special syntactic meaning, but escaping these characters creates extra backslashes in the raw string. See [raw strings containing template literal syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw#raw_strings_containing_template_literal_syntax)
 for more information.

In addition, the [`String.raw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw)
 method exists to create raw strings just like the default template function and string concatenation would create.

`String.raw` functions like an "identity" tag if the literal doesn't contain any escape sequences. In case you want an actual identity tag that always works as if the literal is untagged, you can make a custom function that passes the "cooked" (i.e., escape sequences are processed) literal array to `String.raw`, pretending they are raw strings.

This is useful for many tools which give special treatment to literals tagged by a particular name.

### [Tagged templates and escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates_and_escape_sequences)

In normal template literals, [the escape sequences in string literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#escape_sequences)
 are all allowed. Any other non-well-formed escape sequence is a syntax error. This includes:

*   `\` followed by any decimal digit other than `0`, or `\0` followed by a decimal digit; for example `\9` and `\07` (which is a [deprecated syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#escape_sequences)
    )
*   `\x` followed by fewer than two hex digits (including none); for example `\xz`
*   `\u` not followed by `{` and followed by fewer than four hex digits (including none); for example `\uz`
*   `\u{}` enclosing an invalid Unicode code point — it contains a non-hex digit, or its value is greater than `10FFFF`; for example `\u{110000}` and `\u{z}`

**Note:** `\` followed by other characters, while they may be useless since nothing is escaped, are not syntax errors.

However, this is problematic for tagged templates, which, in addition to the "cooked" literal, also have access to the raw literals (escape sequences are preserved as-is).

Tagged templates enable the embedding of arbitrary string content, where escape sequences may follow a different syntax. Consider an example where we embed [LaTeX](https://en.wikipedia.org/wiki/LaTeX "External link (opens in new tab)")
 source text in JavaScript via `String.raw`. We want to still be able to use LaTeX macros that start with `u` or `x` without following JavaScript syntax restrictions. Therefore, the syntax restriction of well-formed escape sequences is removed from tagged templates. The example below uses [MathJax](https://www.mathjax.org/ "External link (opens in new tab)")
 to render LaTeX in one element:

However, illegal escape sequences must still be represented in the "cooked" representation. They will show up as an [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
 element in the "cooked" array:

Note that the escape-sequence restriction is only dropped from _tagged_ templates, but not from _untagged_ template literals:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-template-literals](https://tc39.es/ecma262/multipage/ecmascript-language-expressions.html#sec-template-literals) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#see_also)

---------------------------------------------------------------------------------------------------------

*   [Numbers and strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Numbers_and_strings)
     guide
*   [`String`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
    
*   [`String.raw()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/raw)
    
*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    
*   [ES6 in Depth: Template strings](https://hacks.mozilla.org/2015/05/es6-in-depth-template-strings-2/ "External link (opens in new tab)")
     on hacks.mozilla.org (2015)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/template_literals/index.md?plain=1 "Folder: en-us/web/javascript/reference/template_literals (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FTemplate_literals&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ftemplate_literals%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FTemplate_literals%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ftemplate_literals%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
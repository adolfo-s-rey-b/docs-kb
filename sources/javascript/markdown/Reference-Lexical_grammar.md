*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#mdn-search)
    

Lexical grammar
===============

This page describes JavaScript's lexical grammar. JavaScript source text is just a sequence of characters — in order for the interpreter to understand it, the string has to be _parsed_ to a more structured representation. The initial step of parsing is called [lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis "External link (opens in new tab)")
, in which the text gets scanned from left to right and is converted into a sequence of individual, atomic input elements. Some input elements are insignificant to the interpreter, and will be stripped after this step — they include [white space](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#white_space)
 and [comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)
. The others, including [identifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
, [keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
, [literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#literals)
, and punctuators (mostly [operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
), will be used for further syntax analysis. [Line terminators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
 and multiline comments are also syntactically insignificant, but they guide the process for [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 to make certain invalid token sequences become valid.

[Format-control characters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#format-control_characters)

-----------------------------------------------------------------------------------------------------------------------------------------

Format-control characters have no visual representation but are used to control the interpretation of the text.

| Code point | Name | Abbreviation | Description |
| --- | --- | --- | --- |
| U+200C | Zero width non-joiner | <ZWNJ> | Placed between characters to prevent being connected into ligatures in certain languages ([Wikipedia](https://en.wikipedia.org/wiki/Zero-width_non-joiner "External link (opens in new tab)")<br>). |
| U+200D | Zero width joiner | <ZWJ> | Placed between characters that would not normally be connected in order to cause the characters to be rendered using their connected form in certain languages ([Wikipedia](https://en.wikipedia.org/wiki/Zero-width_joiner "External link (opens in new tab)")<br>). |
| U+FEFF | Byte order mark | <BOM> | Used at the start of the script to mark it as Unicode and to allow detection of the text's encoding and byte order ([Wikipedia](https://en.wikipedia.org/wiki/Byte_order_mark "External link (opens in new tab)")<br>). |

In JavaScript source text, <ZWNJ> and <ZWJ> are treated as [identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
 parts, while <BOM> (also called a zero-width no-break space <ZWNBSP> when not at the start of text) is treated as [white space](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#white_space)
.

[White space](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#white_space)

-------------------------------------------------------------------------------------------------------------

[White space](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)
 characters improve the readability of source text and separate tokens from each other. These characters are usually unnecessary for the functionality of the code. [Minification tools](https://en.wikipedia.org/wiki/Minification_%28programming%29 "External link (opens in new tab)")
 are often used to remove whitespace in order to reduce the amount of data that needs to be transferred.

| Code point | Name | Abbreviation | Description | Escape sequence |
| --- | --- | --- | --- | --- |
| U+0009 | Character tabulation | <TAB> | Horizontal tabulation | \\t |
| U+000B | Line tabulation | <VT> | Vertical tabulation | \\v |
| U+000C | Form feed | <FF> | Page breaking control character ([Wikipedia](https://en.wikipedia.org/wiki/Page_break#Form_feed "External link (opens in new tab)")<br>). | \\f |
| U+0020 | Space | <SP> | Normal space |     |
| U+00A0 | No-break space | <NBSP> | Normal space, but no point at which a line may break |     |
| U+FEFF | Zero-width no-break space | <ZWNBSP> | When not at the start of a script, the BOM marker is a normal whitespace character. |     |
| Others | Other Unicode space characters | <USP> | [Characters in the "Space\_Separator" general category](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BGeneral_Category%3DSpace_Separator%7D "External link (opens in new tab)") |     |

**Note:** Of those [characters with the "White\_Space" property but are not in the "Space\_Separator" general category](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BWhite_Space%7D%26%5CP%7BGeneral_Category%3DSpace_Separator%7D "External link (opens in new tab)")
, U+0009, U+000B, and U+000C are still treated as white space in JavaScript; U+0085 NEXT LINE has no special role; others become the set of [line terminators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
.

**Note:** Changes to the Unicode standard used by the JavaScript engine may affect programs' behavior. For example, ES2016 upgraded the reference Unicode standard from 5.1 to 8.0.0, which caused U+180E MONGOLIAN VOWEL SEPARATOR to be moved from the "Space\_Separator" category to the "Format (Cf)" category, and made it a non-whitespace. Subsequently, the result of [`"\u180E".trim().length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)
 changed from `0` to `1`.

[Line terminators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)

-----------------------------------------------------------------------------------------------------------------------

In addition to [white space](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#white_space)
 characters, line terminator characters are used to improve the readability of the source text. However, in some cases, line terminators can influence the execution of JavaScript code as there are a few places where they are forbidden. Line terminators also affect the process of [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
.

Outside the context of lexical grammar, white space and line terminators are often conflated. For example, [`String.prototype.trim()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)
 removes all white space and line terminators from the beginning and end of a string. The `\s` [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
 in regular expressions matches all white space and line terminators.

Only the following Unicode code points are treated as line terminators in ECMAScript. Other line breaking characters are treated as white space (for example, Line Tabulation, VT, U+000B).

| Code point | Name | Abbreviation | Description | Escape sequence |
| --- | --- | --- | --- | --- |
| U+000A | Line Feed | <LF> | New line character in UNIX systems. | \\n |
| U+000D | Carriage Return | <CR> | New line character in Commodore and early Mac systems. | \\r |
| U+2028 | Line Separator | <LS> | [Wikipedia](https://en.wikipedia.org/wiki/Newline "External link (opens in new tab)") |     |
| U+2029 | Paragraph Separator | <PS> | [Wikipedia](https://en.wikipedia.org/wiki/Newline "External link (opens in new tab)") |     |

[Comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)

-------------------------------------------------------------------------------------------------------

Comments are used to add hints, notes, suggestions, or warnings to JavaScript code. This can make it easier to read and understand. They can also be used to disable code to prevent it from being executed; this can be a valuable debugging tool.

JavaScript has two long-standing ways to add comments to code: line comments and block comments. In addition, there's a special hashbang comment syntax.

### [Line comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_comments)

The first way is the `//` comment; this makes all text following it on the same line into a comment. For example:

### [Block comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#block_comments)

The second way is the `/* */` style, which is much more flexible.

For example, you can use it on a single line:

You can also make multiple-line comments, like this:

You can also use it in the middle of a line, if you wish, although this can make your code harder to read so it should be used with caution:

In addition, you can use it to disable code to prevent it from running, by wrapping code in a comment, like this:

In this case, the `console.log()` call is never issued, since it's inside a comment. Any number of lines of code can be disabled this way.

Block comments that contain at least one line terminator behave like [line terminators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
 in [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
.

### [Hashbang comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#hashbang_comments)

There's a special third comment syntax, the **hashbang comment**. A hashbang comment behaves exactly like a single line-only (`//`) comment, except that it begins with `#!` and **is only valid at the absolute start of a script or module**. Note also that no whitespace of any kind is permitted before the `#!`. The comment consists of all the characters after `#!` up to the end of the first line; only one such comment is permitted.

Hashbang comments in JavaScript resemble [shebangs in Unix](https://en.wikipedia.org/wiki/Shebang_(Unix) "External link (opens in new tab)")
 which provide the path to a specific JavaScript interpreter that you want to use to execute the script. Before the hashbang comment became standardized, it had already been de-facto implemented in non-browser hosts like Node.js, where it was stripped from the source text before being passed to the engine. An example is as follows:

The JavaScript interpreter will treat it as a normal comment — it only has semantic meaning to the shell if the script is directly run in a shell.

**Warning:** If you want scripts to be runnable directly in a shell environment, encode them in UTF-8 without a [BOM](https://en.wikipedia.org/wiki/Byte_order_mark "External link (opens in new tab)")
. Although a BOM will not cause any problems for code running in a browser — because it's stripped during UTF-8 decoding, before the source text is analyzed — a Unix/Linux shell will not recognize the hashbang if it's preceded by a BOM character.

You must only use the `#!` comment style to specify a JavaScript interpreter. In all other cases just use a `//` comment (or multiline comment).

[Identifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)

-------------------------------------------------------------------------------------------------------------

An _identifier_ is used to link a value with a name. Identifiers can be used in various places:

In JavaScript, identifiers are commonly made of alphanumeric characters, underscores (`_`), and dollar signs (`$`). Identifiers are not allowed to start with numbers. However, JavaScript identifiers are not only limited to [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 — many Unicode code points are allowed as well. Namely:

*   Start characters can be any character in the [ID\_Start](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BID_Start%7D "External link (opens in new tab)")
     category plus `_` and `$`.
*   After the first character, you can use any character in the [ID\_Continue](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp?a=%5Cp%7BID_Continue%7D "External link (opens in new tab)")
     category, which contains U+200C (ZWNJ) and U+200D (ZWJ).

**Note:** If, for some reason, you need to parse some JavaScript source yourself, do not assume all identifiers follow the pattern `/[A-Za-z_$][\w$]*/` (i.e., ASCII-only)! The range of identifiers can be described by the regex `/[$_\p{ID_Start}][$\p{ID_Continue}]*/u` (excluding unicode escape sequences).

In addition, JavaScript allows using [Unicode escape sequences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#unicode_escape_sequences)
 in the form of `\u0000` or `\u{000000}` in identifiers, which encode the same string value as the actual Unicode characters. For example, `你好` and `\u4f60\u597d` are the same identifiers:

Not all places accept the full range of identifiers. Certain syntaxes, such as function declarations, function expressions, and variable declarations require using identifier names that are not [reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
.

Most notably, private elements and object properties allow reserved words.

[Keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)

-------------------------------------------------------------------------------------------------------

_Keywords_ are tokens that look like identifiers but have special meanings in JavaScript. For example, the keyword [`async`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
 before a function declaration indicates that the function is asynchronous.

Some keywords are _reserved_, meaning that they cannot be used as an identifier for variable declarations, function declarations, etc. They are often called _reserved words_. [A list of these reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)
 is provided below. Not all keywords are reserved — for example, `async` can be used as an identifier anywhere. Some keywords are only _contextually reserved_ — for example, `await` is only reserved within the body of an async function, and `let` is only reserved in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 code, or `const` and `let` declarations.

Identifiers are always compared by _string value_, so escape sequences are interpreted. For example, this is still a syntax error:

### [Reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#reserved_words)

These keywords cannot be used as identifiers for variables, functions, classes, etc. anywhere in JavaScript source.

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [`case`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
    
*   [`catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    
*   [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
    
*   [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    
*   [`debugger`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger)
    
*   [`default`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
    
*   [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete)
    
*   [`do`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
    
*   [`else`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    
*   [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
    
*   [`extends`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
    
*   [`false`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#boolean_literal)
    
*   [`finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    
*   [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    
*   [`function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)
    
*   [`if`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    
*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    
*   [`in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)
    
*   [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
    
*   [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
    
*   [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
    
*   [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
    
*   [`super`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
    
*   [`switch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
    
*   [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
    
*   [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
    
*   [`true`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#boolean_literal)
    
*   [`try`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    
*   [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
    
*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    
*   [`void`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)
    
*   [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
    
*   [`with`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with)
    

The following are only reserved when they are found in strict mode code:

*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
     (also reserved in `const`, `let`, and class declarations)
*   [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
    
*   [`yield`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/yield)
     (also reserved in generator function bodies)

The following are only reserved when they are found in module code or async function bodies:

*   [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
    

### [Future reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#future_reserved_words)

The following are reserved as future keywords by the ECMAScript specification. They have no special functionality at present, but they might at some future time, so they cannot be used as identifiers.

These are always reserved:

*   `enum`

The following are only reserved when they are found in strict mode code:

*   `implements`
*   `interface`
*   `package`
*   `private`
*   `protected`
*   `public`

#### Future reserved words in older standards

The following are reserved as future keywords by older ECMAScript specifications (ECMAScript 1 till 3).

*   `abstract`
*   `boolean`
*   `byte`
*   `char`
*   `double`
*   `final`
*   `float`
*   `goto`
*   `int`
*   `long`
*   `native`
*   `short`
*   `synchronized`
*   `throws`
*   `transient`
*   `volatile`

### [Identifiers with special meanings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers_with_special_meanings)

A few identifiers have a special meaning in some contexts without being reserved words of any kind. They include:

*   [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
     (not a keyword, but cannot be declared as an identifier in strict mode)
*   `as` ([`import * as ns from "mod"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#namespace_import)
    )
*   [`async`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
    
*   [`eval`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
     (not a keyword, but cannot be declared as an identifier in strict mode)
*   `from` ([`import x from "mod"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    )
*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    
*   [`of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    

[Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#literals)

-------------------------------------------------------------------------------------------------------

**Note:** This section discusses literals that are atomic tokens. [Object literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 and [array literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Array#array_literal_notation)
 are [expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators)
 that consist of a series of tokens.

### [Null literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#null_literal)

See also [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)
 for more information.

### [Boolean literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#boolean_literal)

See also [boolean type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#boolean_type)
 for more information.

### [Numeric literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#numeric_literals)

The [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#number_type)
 and [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#bigint_type)
 types use numeric literals.

#### Decimal

Decimal literals can start with a zero (`0`) followed by another decimal digit, but if all digits after the leading `0` are smaller than 8, the number is interpreted as an octal number. This is considered a legacy syntax, and number literals prefixed with `0`, whether interpreted as octal or decimal, cause a syntax error in [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#legacy_octal_literals)
 — so, use the `0o` prefix instead.

##### Exponential

The decimal exponential literal is specified by the following format: `beN`; where `b` is a base number (integer or floating), followed by an `E` or `e` character (which serves as separator or _exponent indicator_) and `N`, which is _exponent_ or _power_ number – a signed integer.

#### Binary

Binary number syntax uses a leading zero followed by a lowercase or uppercase Latin letter "B" (`0b` or `0B`). The digits after the prefix must be `0` or `1`.

#### Octal

Octal number syntax uses a leading zero followed by a lowercase or uppercase Latin letter "O" (`0o` or `0O`). The digits after the prefix must be in the range `0`–`7`.

#### Hexadecimal

Hexadecimal number syntax uses a leading zero followed by a lowercase or uppercase Latin letter "X" (`0x` or `0X`). The digits after the prefix must be in the ranges `0`–`9`, `A`–`F`, or `a`–`f`.

#### BigInt literal

The [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#bigint_type)
 type is a numeric primitive in JavaScript that can represent integers with arbitrary precision. BigInt literals are created by appending `n` to the end of an integer.

Decimal BigInt literals cannot have leading zeros to avoid confusion with legacy octal literals.

For octal `BigInt` numbers, always use zero followed by the letter "o" (uppercase or lowercase):

For more information about `BigInt`, see also [JavaScript data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#bigint_type)
.

#### Numeric separators

To improve readability for numeric literals, underscores (`_`, `U+005F`) can be used as separators:

Note these limitations:

### [String literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#string_literals)

A [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#string_type)
 literal is zero or more Unicode code points enclosed in single or double quotes. Unicode code points may also be represented by an escape sequence. All code points may appear literally in a string literal except for these code points:

*   U+005C \\ (backslash)
*   U+000D <CR>
*   U+000A <LF>
*   The same kind of quote that begins the string literal

Any code points may appear in the form of an escape sequence. String literals evaluate to ECMAScript String values. When generating these String values Unicode code points are UTF-16 encoded.

The following subsections describe various escape sequences (`\` followed by one or more characters) available in string literals. Any escape sequence not listed below becomes an "identity escape" that becomes the code point itself. For example, `\z` is the same as `z`. There's a deprecated octal escape sequence syntax described in the [Deprecated and obsolete features](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#escape_sequences)
 page. Many of these escape sequences are also valid in regular expressions — see [Character escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
.

#### Escape sequences

Special characters can be encoded using escape sequences:

| Escape sequence | Unicode code point |
| --- | --- |
| `\0` | null character (U+0000 NULL) |
| `\'` | single quote (U+0027 APOSTROPHE) |
| `\"` | double quote (U+0022 QUOTATION MARK) |
| `\\` | backslash (U+005C REVERSE SOLIDUS) |
| `\n` | newline (U+000A LINE FEED; LF) |
| `\r` | carriage return (U+000D CARRIAGE RETURN; CR) |
| `\v` | vertical tab (U+000B LINE TABULATION) |
| `\t` | tab (U+0009 CHARACTER TABULATION) |
| `\b` | backspace (U+0008 BACKSPACE) |
| `\f` | form feed (U+000C FORM FEED) |
| `\` followed by a [line terminator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators) | empty string |

The last escape sequence, `\` followed by a line terminator, is useful for splitting a string literal across multiple lines without changing its meaning.

Make sure there is no space or any other character after the backslash (except for a line break), otherwise it will not work. If the next line is indented, the extra spaces will also be present in the string's value.

You can also use the [`+`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition)
 operator to append multiple strings together, like this:

Both of the above methods result in identical strings.

#### Hexadecimal escape sequences

Hexadecimal escape sequences consist of `\x` followed by exactly two hexadecimal digits representing a code unit or code point in the range 0x0000 to 0x00FF.

#### Unicode escape sequences

A Unicode escape sequence consists of exactly four hexadecimal digits following `\u`. It represents a code unit in the UTF-16 encoding. For code points U+0000 to U+FFFF, the code unit is equal to the code point. Code points U+10000 to U+10FFFF require two escape sequences representing the two code units (a surrogate pair) used to encode the character; the surrogate pair is distinct from the code point.

See also [`String.fromCharCode()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode)
 and [`String.prototype.charCodeAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)
.

#### Unicode code point escapes

A Unicode code point escape consists of `\u{`, followed by a code point in hexadecimal base, followed by `}`. The value of the hexadecimal digits must be in the range 0 and 0x10FFFF inclusive. Code points in the range U+10000 to U+10FFFF do not need to be represented as a surrogate pair.

See also [`String.fromCodePoint()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint)
 and [`String.prototype.codePointAt()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt)
.

### [Regular expression literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#regular_expression_literals)

Regular expression literals are enclosed by two forward slashes (`/`). The lexer consumes all characters up to the next unescaped forward slash or the end of the line, unless the forward slash appears within a character class (`[]`). Some characters (namely, those that are [identifier parts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#identifiers)
) can appear after the closing slash, denoting flags.

The lexical grammar is very lenient: not all regular expression literals that get identified as one token are valid regular expressions.

See also [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 for more information.

A regular expression literal cannot start with two forward slashes (`//`), because that would be a line comment. To specify an empty regular expression, use `/(?:)/`.

### [Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#template_literals)

One template literal consists of several tokens: `` `xxx${ `` (template head), `}xxx${` (template middle), and `` }xxx` `` (template tail) are individual tokens, while any expression may come between them.

See also [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
 for more information.

[Automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)

-------------------------------------------------------------------------------------------------------------------------------------------------

Some [JavaScript statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
' syntax definitions require semicolons (`;`) at the end. They include:

*   [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
    , [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    , [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    , [`using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/using)
    , [`await using`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/await_using)
    
*   [Expression statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Expression_statement)
    
*   [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    , [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    , [`return`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
    , [`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
    
*   [`debugger`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger)
    
*   Class field declarations ([public](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Public_class_fields)
     or [private](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    )
*   [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
    , [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)
    

However, to make the language more approachable and convenient, JavaScript is able to automatically insert semicolons when consuming the token stream, so that some invalid token sequences can be "fixed" to valid syntax. This step happens after the program text has been parsed to tokens according to the lexical grammar. There are three cases when semicolons are automatically inserted:

1\. When a token not allowed by the grammar is encountered, and it's separated from the previous token by at least one [line terminator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#line_terminators)
 (including a block comment that includes at least one line terminator), or the token is "}", then a semicolon is inserted before the token.

The ending ")" of [`do...while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)
 is taken care of as a special case by this rule as well.

However, semicolons are not inserted if the semicolon would then become the separator in the [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
 statement's head.

Semicolons are also never inserted as [empty statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/Empty)
. For example, in the code below, if a semicolon is inserted after ")", then the code would be valid, with an empty statement as the `if` body and the `const` declaration being a separate statement. However, because automatically inserted semicolons cannot become empty statements, this causes a [declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#what_are_statements_declarations_and_expressions)
 to become the body of the `if` statement, which is not valid.

2\. When the end of the input stream of tokens is reached, and the parser is unable to parse the single input stream as a complete program, a semicolon is inserted at the end.

This rule is a complement to the previous rule, specifically for the case where there's no "offending token" but the end of input stream.

3\. When the grammar forbids line terminators in some place but a line terminator is found, a semicolon is inserted. These places include:

*   `expr <here> ++`, `expr <here> --`
*   `continue <here> lbl`
*   `break <here> lbl`
*   `return <here> expr`
*   `throw <here> expr`
*   `yield <here> expr`
*   `yield <here> * expr`
*   `(param) <here> => {}`
*   `async <here> function`, `async <here> prop()`, `async <here> function*`, `async <here> *prop()`, `async <here> (param) <here> => {}`
*   `using <here> id`, `await <here> using <here> id`

Here [`++`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment)
 is not treated as a postfix operator applying to variable `b`, because a line terminator occurs between `b` and `++`.

Here, the `return` statement returns `undefined`, and the `a + b` becomes an unreachable statement.

Note that ASI would only be triggered if a line break separates tokens that would otherwise produce invalid syntax. If the next token can be parsed as part of a valid structure, semicolons would not be inserted. For example:

Because `()` can be seen as a function call, it would usually not trigger ASI. Similarly, `[]` may be a member access. The code above is equivalent to:

This happens to be valid syntax. `1[1, 2, 3]` is a [property accessor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
 with a [comma](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_operator)
\-joined expression. Therefore, you would get errors like "1 is not a function" and "Cannot read properties of undefined (reading 'forEach')" when running the code.

Within classes, class fields and generator methods can be a pitfall as well.

It is seen as:

And therefore will be a syntax error around `{`.

There are the following rules-of-thumb for dealing with ASI, if you want to enforce semicolon-less style:

*   Write postfix `++` and `--` on the same line as their operands.
    
*   The expressions after `return`, `throw`, or `yield` should be on the same line as the keyword.
    
*   Similarly, the label identifier after `break` or `continue` should be on the same line as the keyword.
    
*   The `=>` of an arrow function should be on the same line as the end of its parameters.
    
*   The `async` of async functions, methods, etc. cannot be directly followed by a line terminator.
    
*   The `using` keyword in `using` and `await using` statements should be on the same line as the first identifier it declares.
    
*   If a line starts with one of `(`, `[`, `` ` ``, `+`, `-`, `/` (as in regex literals), prefix it with a semicolon, or end the previous line with a semicolon.\
    \
*   Class fields should preferably always be ended with semicolons — in addition to the previous rule (which includes a field declaration followed by a [computed property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names)\
    , since the latter starts with `[`), semicolons are also required between a field declaration and a generator method.\
    \
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#specifications)\
\
-------------------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [ECMAScript® 2027 Language Specification](https://tc39.es/ecma262/multipage/ecmascript-language-lexical-grammar.html) |\
\
[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#browser_compatibility)\
\
---------------------------------------------------------------------------------------------------------------------------------\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#see_also)\
\
-------------------------------------------------------------------------------------------------------\
\
*   [Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)\
     guide\
*   [Micro-feature from ES6, now in Firefox Aurora and Nightly: binary and octal numbers](https://whereswalden.com/2013/08/12/micro-feature-from-es6-now-in-firefox-aurora-and-nightly-binary-and-octal-numbers/ "External link (opens in new tab)")\
     by Jeff Walden (2013)\
*   [JavaScript character escape sequences](https://mathiasbynens.be/notes/javascript-escapes "External link (opens in new tab)")\
     by Mathias Bynens (2011)\
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/lexical_grammar/index.md?plain=1 "Folder: en-us/web/javascript/reference/lexical_grammar (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FLexical_grammar&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Flexical_grammar%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FLexical_grammar%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Flexical_grammar%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
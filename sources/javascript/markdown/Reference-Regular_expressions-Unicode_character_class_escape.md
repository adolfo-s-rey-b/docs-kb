*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#mdn-search)
    

Unicode character class escape: \\p{...}, \\P{...}
==================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

A **Unicode character class escape** is a kind of [character class escape](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
 that matches a set of characters specified by a Unicode property. It's only supported in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
. When the [`v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)
 flag is enabled, it can also be used to match finite-length strings.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#try_it)

--------------------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#syntax)

--------------------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#parameters)

[`loneProperty`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#loneproperty)

A lone Unicode property name or value, following the same syntax as `value`. It specifies the value for the `General_Category` property, or a [binary property name](https://tc39.es/ecma262/multipage/text-processing.html#table-binary-unicode-properties "External link (opens in new tab)")
. In [`v`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)
 mode, it can also be a [binary Unicode property of strings](https://tc39.es/ecma262/multipage/text-processing.html#table-binary-unicode-properties-of-strings "External link (opens in new tab)")
.

**Note:** [ICU](https://unicode-org.github.io/icu/userguide/strings/unicodeset.html#property-values "External link (opens in new tab)")
 syntax allows omitting the `Script` property name as well, but JavaScript does not support this, because most of the time `Script_Extensions` is more useful than `Script`.

[`property`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#property)

A Unicode property name. Must be made of [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 letters (`A–Z`, `a–z`) and underscores (`_`), and must be one of the [non-binary property names](https://tc39.es/ecma262/multipage/text-processing.html#table-nonbinary-unicode-properties "External link (opens in new tab)")
.

[`value`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#value)

A Unicode property value. Must be made of ASCII letters (`A–Z`, `a–z`), underscores (`_`), and digits (`0–9`), and must be one of the supported values listed in [`PropertyValueAliases.txt`](https://unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt "External link (opens in new tab)")
.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#description)

------------------------------------------------------------------------------------------------------------------------------------------------

`\p` and `\P` are only supported in [Unicode-aware mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
. In Unicode-unaware mode, they are [identity escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
 for the `p` or `P` character.

Every Unicode character has a set of properties that describe it. For example, the character [`a`](https://util.unicode.org/UnicodeJsps/character.jsp?a=0061 "External link (opens in new tab)")
 has the `General_Category` property with value `Lowercase_Letter`, and the `Script` property with value `Latn`. The `\p` and `\P` escape sequences allow you to match a character based on its properties. For example, `a` can be matched by `\p{Lowercase_Letter}` (the `General_Category` property name is optional) as well as `\p{Script=Latn}`. `\P` creates a _complement class_ that consists of code points without the specified property.

When the [`i`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)
 flag is set, `\P` character classes are handled slightly differently in `u` and `v` modes. In `u` mode, case-folding happens after subtraction; in `v` mode, case-folding happens before subtraction. More concretely, in `u` mode, `\P{property}` matches `caseFold(allCharacters - charactersWithProperty)`. This means `/\P{Lowercase_Letter}/iu` still matches `"a"`, because `A` is not a `Lowercase_Letter`. In `v` mode, `\P{property}` matches `caseFold(allCharacters) - caseFold(charactersWithProperty)`. This means `/\P{Lowercase_Letter}/iv` does not match `"a"`, because `A` is not even in the set of all case-folded Unicode characters. See also [complement classes and case-insensitive matching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#complement_classes_and_case-insensitive_matching)
.

To compose multiple properties, use the [character set intersection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)
 syntax enabled with the `v` flag, or see [pattern subtraction and intersection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Lookahead_assertion#pattern_subtraction_and_intersection)
.

In `v` mode, `\p` may match a sequence of code points, defined in Unicode as "properties of strings". This is most useful for emojis, which are often composed of multiple code points. However, `\P` can only complement character properties.

**Note:** There are plans to port the properties of strings feature to `u` mode as well.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#examples)

------------------------------------------------------------------------------------------------------------------------------------------

### [General categories](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#general_categories)

General categories are used to classify Unicode characters and subcategories are available to define a more precise categorization. It is possible to use both short and long forms in Unicode property escapes.

They can be used to match letters, numbers, symbols, punctuation, spaces, etc. For a more exhaustive list of general categories, please refer to [the Unicode specification](https://unicode.org/reports/tr18/#General_Category_Property "External link (opens in new tab)")
.

### [Scripts and script extensions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#scripts_and_script_extensions)

Some languages use different scripts for their writing system. For instance, English and Spanish are written using the Latin script while Arabic and Russian are written with other scripts (respectively Arabic and Cyrillic). The `Script` and `Script_Extensions` Unicode properties allow regular expressions to match characters according to the script they are mainly used with (`Script`) or according to the set of scripts they belong to (`Script_Extensions`).

For example, `A` belongs to the `Latin` script and `ε` to the `Greek` script.

For more details, refer to [the Unicode specification](https://unicode.org/reports/tr24/#Script "External link (opens in new tab)")
, the [Scripts table in the ECMAScript specification](https://tc39.es/ecma262/multipage/text-processing.html#table-unicode-script-values "External link (opens in new tab)")
, and the [ISO 15924 list of script codes](https://unicode.org/iso15924/iso15924-codes.html "External link (opens in new tab)")
.

If a character is used in a limited set of scripts, the `Script` property will only match for the "predominant" used script. If we want to match characters based on a "non-predominant" script, we could use the `Script_Extensions` property (`scx` for short).

### [Unicode property escapes vs. character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#unicode_property_escapes_vs._character_classes)

With JavaScript regular expressions, it is also possible to use [character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
 and especially `\w` or `\d` to match letters or digits. However, such forms only match characters from the _Latin_ script (in other words, ASCII letters, numbers, and the underscore character for `\w`, and ASCII numbers for `\d`). As shown in [this example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes#looking_for_a_word_from_unicode_characters)
, character classes may be clumsy when used with non-Latin text.

Unicode property escape categories cover many more characters, and `\p{Letter}` and `\p{Number}` work for any script.

### [Matching prices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#matching_prices)

The following example matches prices in a string:

### [Matching strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#matching_strings)

With the `v` flag, `\p{…}` can match strings that are potentially longer than one character by using a property of strings:

However, you can't use `\P` to match "a string that does not have a property", because it's unclear how many characters should be consumed.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#specifications)

------------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# prod-CharacterClassEscape](https://tc39.es/ecma262/multipage/text-processing.html#prod-CharacterClassEscape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape#see_also)

------------------------------------------------------------------------------------------------------------------------------------------

*   [Character classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Character_classes)
     guide
*   [Regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions)
    
*   [Character class: `[...]`, `[^...]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class)
    
*   [Character class escape: `\d`, `\D`, `\w`, `\W`, `\s`, `\S`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class_escape)
    
*   [Character escape: `\n`, `\u{...}`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_escape)
    
*   [Disjunction: `|`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Disjunction)
    
*   [Unicode character property](https://en.wikipedia.org/wiki/Unicode_character_property "External link (opens in new tab)")
     on Wikipedia
*   [ES2018: RegExp Unicode property escapes](https://2ality.com/2017/07/regexp-unicode-property-escapes.html "External link (opens in new tab)")
     by Dr. Axel Rauschmayer (2017)
*   [Unicode regular expressions § Properties](https://unicode.org/reports/tr18/#Categories "External link (opens in new tab)")
    
*   [Unicode Utilities: UnicodeSet](https://util.unicode.org/UnicodeJsps/list-unicodeset.jsp "External link (opens in new tab)")
    
*   [RegExp v flag with set notation and properties of strings](https://v8.dev/features/regexp-v-flag "External link (opens in new tab)")
     on v8.dev (2022)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Unicode_character_class_escape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/regular_expressions/unicode_character_class_escape/index.md?plain=1 "Folder: en-us/web/javascript/reference/regular_expressions/unicode_character_class_escape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FUnicode_character_class_escape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Funicode_character_class_escape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FRegular_expressions%2FUnicode_character_class_escape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fregular_expressions%2Funicode_character_class_escape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F288e644117c29285df2acf37a2ac97f57546a146%0A*+Document+last+modified%3A+2026-11-06T23%3A18%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#mdn-search)
    

Intl.PluralRules
================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2019.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.PluralRules`** object enables plural-sensitive formatting and plural-related language rules.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#description)

-----------------------------------------------------------------------------------------------------------------------------

Languages use different patterns for expressing both plural numbers of items (cardinal numbers) and for expressing the order of items (ordinal numbers). English has two forms for expressing cardinal numbers: one for the singular "item" (1 hour, 1 dog, 1 fish) and the other for zero or any other number of "items" (0 hours, 2 lemmings, 100000.5 fish), while Chinese has only one form, and Arabic has six! Similarly, English has four forms for expressing ordinal numbers: "th", "st", "nd", "rd", giving the sequence: 0th, 1st, 2nd, 3rd, 4th, 5th, ..., 21st, 22nd, 23rd, 24th, 25th, and so on, while both Chinese and Arabic only have one form for ordinal numbers.

Given a particular language and set of formatting options, the methods [`Intl.PluralRules.prototype.select()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)
 and [`Intl.PluralRules.prototype.selectRange()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/selectRange)
 return a _tag_ that represents the plural form of a single or a range of numbers, cardinal or ordinal. Code can use the returned tags to represent numbers appropriately for the given language. The full set of tags that might be returned are: `zero`, `one`, `two`, `few`, `many`, and `other` (the "general" plural form, also used if the language only has one form).

As English only has two forms for cardinal numbers, the `select()` method returns only two tags: `"one"` for the singular case, and `"other"` for all other cardinal numbers. This allows construction of sentences that make sense in English for each case, such as: "1 dog is happy; do you want to play with it?" and "10 dogs are happy; do you want to play with them?".

Creating appropriate sentences for each form depends on the language, and even in English may not be as simple as just adding "s" to a noun to make the plural form. Using the example above, we see that the form may affect:

*   **Nouns**: 1 dog, 2 dogs (but not "fish" or "sheep", which have the same singular and plural form).
*   **Verbs**: 1 dog _is_ happy, 2 dogs _are_ happy.
*   **Pronouns** (and other referents): Do you want to play with _it_ / _them_.

Other languages have more forms, and choosing appropriate sentences can be even more complex.

`select()` can return any of four tags for ordinal numbers in English, representing each of the allowed forms: `one` for "st" numbers (1, 21, 31, ...), `two` for "nd" numbers (2, 22, 32, ...), `few` for "rd" numbers (3, 33, 43, ...), and `other` for "th" numbers (0, 4-20, etc.). Again, the returned tags allow appropriate formatting of strings describing an ordinal number.

For more information about the rules and how they are used, see [Plural Rules](https://cldr.unicode.org/index/cldr-spec/plural-rules "External link (opens in new tab)")
. For a list of the rules and how they apply for different languages, see the [LDML Language Plural Rules](https://www.unicode.org/cldr/charts/43/supplemental/language_plural_rules.html "External link (opens in new tab)")
.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#constructor)

-----------------------------------------------------------------------------------------------------------------------------

[`Intl.PluralRules()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)

Creates a new `Intl.PluralRules` object.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#static_methods)

-----------------------------------------------------------------------------------------------------------------------------------

[`Intl.PluralRules.supportedLocalesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/supportedLocalesOf)

Returns an array containing those of the provided locales that are supported without having to fall back to the runtime's default locale.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#instance_properties)

---------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Intl.PluralRules.prototype` and shared by all `Intl.PluralRules` instances.

[`Intl.PluralRules.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Intl.PluralRules` instances, the initial value is the [`Intl.PluralRules`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules)
 constructor.

[`Intl.PluralRules.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#intl.pluralrules.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Intl.PluralRules"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#instance_methods)

---------------------------------------------------------------------------------------------------------------------------------------

[`Intl.PluralRules.prototype.resolvedOptions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/resolvedOptions)

Returns a new object with properties reflecting the locale and collation options computed during initialization of the object.

[`Intl.PluralRules.prototype.select()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select)

Returns a string indicating which plural rule to use for locale-aware formatting.

[`Intl.PluralRules.prototype.selectRange()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/selectRange)

This method receives two values and returns a string indicating which plural rule to use for locale-aware formatting.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using locales](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#using_locales)

This example shows some of the variations in localized plural rules for cardinal numbers.

In order to get the format for the language used in the user interface of your application, make sure to specify that language (and possibly some fallback languages) using the [constructor `locales`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#locales)
 argument:

### [Using options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#using_options)

The plural form of the specified number may also depend on [constructor `options`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options)
, such as how the number is rounded, and whether it is cardinal or ordinal.

This example shows how you can set the type of rules to "ordinal", and how this affects the form for some numbers in US English.

### [Formatting text using the returned tag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#formatting_text_using_the_returned_tag)

The code below extends the previous example, showing how you might use the returned tag for an ordinal number to format text in English.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# pluralrules-objects](https://tc39.es/ecma402/#pluralrules-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Intl.PluralRules` in FormatJS](https://formatjs.github.io/docs/polyfills/intl-pluralrules/ "External link (opens in new tab)")
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/pluralrules/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/pluralrules (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FPluralRules&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fpluralrules%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FPluralRules%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fpluralrules%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F544b843570cb08d1474cfc5ec03ffb9f4edc0166%0A*+Document+last+modified%3A+2025-07-10T09%3A07%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
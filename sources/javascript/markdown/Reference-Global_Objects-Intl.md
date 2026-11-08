*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#mdn-search)
    

Intl
====

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl`** namespace object contains several constructors as well as functionality common to the internationalization constructors and other language sensitive functions. Collectively, they comprise the ECMAScript Internationalization API, which provides language sensitive string comparison, number formatting, date and time formatting, and more.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#description)

-----------------------------------------------------------------------------------------------------------------

Unlike most global objects, `Intl` is not a constructor. You cannot use it with the [`new` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
 or invoke the `Intl` object as a function. All properties and methods of `Intl` are static (just like the [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
 object).

The internationalization constructors as well as several language sensitive methods of other constructors (listed under [See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#see_also)
) use a common pattern for identifying locales and determining the one they will actually use: they all accept `locales` and `options` arguments, and negotiate the requested locale(s) against the locales they support using an algorithm specified in the `options.localeMatcher` property.

### [locales argument](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)

The `locales` argument is used to determine the locale used in a given operation. The JavaScript implementation examines `locales`, and then computes a locale it understands that comes closest to satisfying the expressed preference. `locales` may be:

*   `undefined` (or omitted): The implementation's default locale will be used.
*   A locale: A locale identifier or an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
     object that wraps a locale identifier.
*   A list of locales: Any other value, that will be converted into an object and then treated as an array of locales.

In the latter two cases, the actual locale used is the best-supported locale determined by [locale negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
. If a locale identifier is not a string or an object, a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
 is thrown. If a locale identifier is a string that's syntactically invalid, a [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
 is thrown. If a locale identifier is well-formed but the implementation doesn't recognize it, it is ignored and the next locale in the list is considered, eventually falling back to the system's locale. However, you shouldn't rely on a particular locale name being ignored, because the implementation may add data for any locale in the future. For example, `new Intl.DateTimeFormat("default")` uses the implementation's default locale only because `"default"` is syntactically valid but not recognized as any locale.

A locale identifier is a string that consists of:

1.  A language subtag with 2–3 or 5–8 letters
2.  A script subtag with 4 letters Optional
3.  A region subtag with either 2 letters or 3 digits Optional
4.  One or more variant subtags (all of which must be unique), each with either 5–8 alphanumerals or a digit followed by 3 alphanumerals Optional
5.  One or more [BCP 47](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
     extension sequences Optional
6.  A private-use extension sequence Optional

Each subtag and sequence are separated by hyphens. Locale identifiers are case-insensitive [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. However, it's conventional to use title case (the first letter is capitalized, successive letters are lower case) for script subtags, upper case for region subtags, and lower case for everything else. For example:

*   `"hi"`: Hindi (language)
*   `"de-AT"`: German (language) as used in Austria (region)
*   `"zh-Hans-CN"`: Chinese (language) written in simplified characters (script) as used in China (region)
*   `"en-emodeng"`: English (language) in the "Early modern English" dialect (variant)

Subtags identifying languages, scripts, regions (including countries), and (rarely used) variants are registered in the [IANA Language Subtag Registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry "External link (opens in new tab)")
. This registry is periodically updated over time, and implementations may not always be up to date, so don't rely too much on subtags being universally supported.

BCP 47 extension sequences consist of a single digit or letter (other than `"x"`) and one or more two- to eight-letter or digit subtags separated by hyphens. Only one sequence is permitted for each digit or letter: `"de-a-foo-a-foo"` is invalid. BCP 47 extension subtags are defined in the [Unicode CLDR Project](https://github.com/unicode-org/cldr/tree/main/common/bcp47 "External link (opens in new tab)")
. Currently only two extensions have defined semantics:

*   The `"u"` (Unicode) extension can be used to request additional customization of `Intl` API objects. Examples:
    
    *   `"de-DE-u-co-phonebk"`: Use the phonebook variant of the German sort order, which interprets umlauted vowels as corresponding character pairs: ä → ae, ö → oe, ü → ue.
    *   `"th-TH-u-nu-thai"`: Use Thai digits (๐, ๑, ๒, ๓, ๔, ๕, ๖, ๗, ๘, ๙) in number formatting.
    *   `"ja-JP-u-ca-japanese"`: Use the Japanese calendar in date and time formatting, so that 2013 is expressed as the year 25 of the Heisei period, or 平成 25.
    *   `"en-GB-u-ca-islamic-umalqura"`: use British English with the Umm al-Qura (Hijri) calendar, where the Gregorian date 14 October, 2017 is the Hijri date 24 Muharram, 1439.
*   The `"t"` (transformed) extension indicates transformed content: for example, text that was translated from another locale. No `Intl` functionality currently considers the `"t"` extension. However, this extension sometimes contains a nested locale (with no extensions): for example, the transformed extension in `"de-t-en"` contains the locale identifier for English. If a nested locale is present, it must be a valid locale identifier. For example, because `"en-emodeng-emodeng"` is invalid (because it contains a duplicate `emodeng` variant subtag), `"de-t-en-emodeng-emodeng"` is also invalid.
    

Finally, a private-use extension sequence using the letter `"x"` may appear, followed by one or more one- to eight-letter or digit subtags separated by hyphens. This allows applications to encode information for their own private use, that will be ignored by all `Intl` operations.

### [options argument](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#options_argument)

The `options` argument must be an object with properties that vary between constructors and functions. If the `options` argument is not provided or is undefined, default values are used for all properties.

One property is supported by all language sensitive constructors and functions: The `localeMatcher` property, whose value must be a string `"lookup"` or `"best fit"` and which selects one of the locale matching algorithms described below.

### [Locale identification and negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)

The list of locales specified by the `locales` argument, after Unicode extensions have been removed from them, is interpreted as a prioritized request from the application. The runtime compares it against the locales it has available and picks the best one available. Two matching algorithms exist: the `"lookup"` matcher follows the Lookup algorithm specified in [BCP 47](https://datatracker.ietf.org/doc/html/rfc4647#section-3.4 "External link (opens in new tab)")
; the `"best fit"` matcher lets the runtime provide a locale that's at least, but possibly more, suited for the request than the result of the Lookup algorithm. If the application doesn't provide a `locales` argument, or the runtime doesn't have a locale that matches the request, then the runtime's default locale is used. The matcher can be selected using a property of the `options` argument (see below).

If the selected locale identifier had a Unicode extension sequence, that extension is now used to customize the constructed object or the behavior of the function. Each constructor or function supports only a subset of the keys defined for the Unicode extension, and the supported values often depend on the locale identifier. For example, the `"co"` key (collation) is only supported by [`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
, and its `"phonebk"` value is only supported for German.

[Static properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#static_properties)

-----------------------------------------------------------------------------------------------------------------------------

[`Intl.Collator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)

Constructor for collators, which are objects that enable language-sensitive string comparison.

[`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)

Constructor for objects that enable language-sensitive date and time formatting.

[`Intl.DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)

Constructor for objects that enable the consistent translation of language, region and script display names.

[`Intl.DurationFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat)

Constructor for objects that enable locale-sensitive duration formatting.

[`Intl.ListFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat)

Constructor for objects that enable language-sensitive list formatting.

[`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)

Constructor for objects that represents a Unicode locale identifier.

[`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)

Constructor for objects that enable language-sensitive number formatting.

[`Intl.PluralRules`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)

Constructor for objects that enable plural-sensitive formatting and language-specific rules for plurals.

[`Intl.RelativeTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

Constructor for objects that enable language-sensitive relative time formatting.

[`Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)

Constructor for objects that enable locale-sensitive text segmentation.

[`Intl[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#intlsymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Intl"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#static_methods)

-----------------------------------------------------------------------------------------------------------------------

[`Intl.getCanonicalLocales()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/getCanonicalLocales)

Returns canonical locale names.

[`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf)

Returns a sorted array containing the supported unique calendar, collation, currency, numbering systems, or unit values supported by the implementation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#examples)

-----------------------------------------------------------------------------------------------------------

### [Formatting dates and numbers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#formatting_dates_and_numbers)

You can use `Intl` to format dates and numbers in a form that's conventional for a specific language and region:

### [Using the browser's preferred language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#using_the_browsers_preferred_language)

Instead of passing a hardcoded locale name to the `Intl` methods, you can use the user's preferred language provided by [`navigator.language`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language)
:

Alternatively, the [`navigator.languages`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/languages)
 property provides a sorted list of the user's preferred languages. This list can be passed directly to the `Intl` constructors to implement preference-based fallback selection of locales. The [locale negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
 process is used to pick the most appropriate locale available:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# intl-object](https://tc39.es/ecma402/#intl-object) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`Keyboard.getLayoutMap()`](https://developer.mozilla.org/en-US/docs/Web/API/Keyboard/getLayoutMap)
    
*   [`navigator.language`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language)
    
*   [`navigator.languages`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/languages)
    
*   [The ECMAScript Internationalization API](https://norbertlindenberg.com/2012/12/ecmascript-internationalization-api/index.html "External link (opens in new tab)")
     by Norbert Lindenberg (2012)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
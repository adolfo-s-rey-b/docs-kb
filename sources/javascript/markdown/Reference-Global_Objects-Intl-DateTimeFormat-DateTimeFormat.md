*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#mdn-search)
    

Intl.DateTimeFormat() constructor
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.DateTimeFormat()`** constructor creates [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
 objects.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#try_it)

-------------------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#syntax)

-------------------------------------------------------------------------------------------------------------------------------------

**Note:** `Intl.DateTimeFormat()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Both create a new `Intl.DateTimeFormat` instance. However, there's a special behavior when it's called without `new` and the `this` value is another `Intl.DateTimeFormat` instance; see [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#return_value)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#parameters)

[`locales` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 or an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instance, or an array of such locale identifiers. The runtime's default locale is used when `undefined` is passed or when none of the specified locale identifiers is supported. For the general form and interpretation of the `locales` argument, see [the parameter description on the `Intl` main page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)
.

The following Unicode extension keys are allowed:

[`nu`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#nu)

See [`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#numberingsystem)
.

[`ca`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#ca)

See [`calendar`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#calendar)
.

[`hc`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hc)

See [`hourCycle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hourcycle)
.

These keys can also be set with `options` (as listed below). When both are set, the `options` property takes precedence.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#options)

An object. For ease of reading, the property list is broken into sections based on their purposes, including [locale options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#locale_options)
, [date-time component options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#date-time_component_options)
, and [style shortcuts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#style_shortcuts)
.

#### Locale options

[`localeMatcher`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#localematcher)

The locale matching algorithm to use. Possible values are `"lookup"` and `"best fit"`; the default is `"best fit"`. For information about this option, see [Locale identification and negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
.

[`calendar`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#calendar)

The calendar to use, such as `"chinese"`, `"gregory"`, `"persian"`, and so on. For a list of supported calendar types, see [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
; the default is locale dependent. This option can also be set through the `ca` Unicode extension key; if both are provided, this `options` property takes precedence.

[`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#numberingsystem)

The numbering system to use for number formatting, such as `"arab"`, `"hans"`, `"mathsans"`, and so on. For a list of supported numbering system types, see [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_numbering_system_types)
; the default is locale dependent. This option can also be set through the `nu` Unicode extension key; if both are provided, this `options` property takes precedence.

[`hour12`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hour12)

Whether to use 12-hour time (as opposed to 24-hour time). Possible values are `true` and `false`; the default is locale dependent. When `true`, this option sets `hourCycle` to either `"h11"` or `"h12"`, depending on the locale. When `false`, it sets `hourCycle` to `"h23"`. `hour12` overrides both the `hc` locale extension tag and the `hourCycle` option, should either or both of those be present.

[`hourCycle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hourcycle)

The hour cycle to use. Possible values are `"h11"`, `"h12"`, `"h23"`, and `"h24"`; the default is inferred from `hour12` and locale. This option can also be set through the `hc` Unicode extension key; if both are provided, this `options` property takes precedence.

[`timeZone`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timezone)

The time zone to use. Can be any [IANA time zone name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
, including named identifiers such as `"UTC"`, `"America/New_York"`, and `"Etc/GMT+8"`, and offset identifiers such as `"+01:00"`, `"-2359"`, and `"+23"`. The default is the runtime's time zone, the same time zone used by [`Date.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
.

#### Date-time component options

[`weekday`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#weekday)

The representation of the weekday. Possible values are:

[`"long"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#long)

E.g., `Thursday`

[`"short"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#short)

E.g., `Thu`

[`"narrow"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#narrow)

E.g., `T`. Two weekdays may have the same narrow style for some locales (e.g., both `Tuesday`'s and `Thursday`'s narrow styles are `T` in the `en-US` locale).

[`era`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#era)

The representation of the era. Possible values are:

[`"long"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#long_2)

E.g., `Anno Domini`

[`"short"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#short_2)

E.g., `AD`

[`"narrow"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#narrow_2)

E.g., `A`

[`year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#year)

The representation of the year. Possible values are `"numeric"` and `"2-digit"`.

[`month`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#month)

The representation of the month. Possible values are:

[`"numeric"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#numeric)

E.g., `3`

[`"2-digit"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#2-digit)

E.g., `03`

[`"long"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#long_3)

E.g., `March`

[`"short"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#short_3)

E.g., `Mar`

[`"narrow"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#narrow_3)

E.g., `M`. Two months may have the same narrow style for some locales (e.g., both `March`'s and `May`'s narrow styles are `M` in the `en-US` locale).

[`day`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#day)

The representation of the day. Possible values are `"numeric"` and `"2-digit"`.

[`dayPeriod`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#dayperiod)

The formatting style used for day periods like "in the morning", "am", "noon", "n" etc. Possible values are `"narrow"`, `"short"`, and `"long"`.

**Note:** This option only has an effect if a 12-hour clock (`hourCycle: "h12"` or `hourCycle: "h11"`) is used. Many locales use the same string irrespective of the width specified.

[`hour`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#hour)

The representation of the hour. Possible values are `"numeric"` and `"2-digit"`.

[`minute`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#minute)

The representation of the minute. Possible values are `"numeric"` and `"2-digit"`.

[`second`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#second)

The representation of the second. Possible values are `"numeric"` and `"2-digit"`.

[`fractionalSecondDigits`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#fractionalseconddigits)

The number of digits used to represent fractions of a second (any additional digits are truncated). Possible values are from `1` to `3`.

[`timeZoneName`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timezonename)

The localized representation of the time zone name. Possible values are:

[`"long"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#long_4)

Long localized form (e.g., `Pacific Standard Time`, `Nordamerikanische Westküsten-Normalzeit`)

[`"short"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#short_4)

Short localized form (e.g.: `PST`, `GMT-8`)

[`"shortOffset"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#shortoffset)

Short localized GMT format (e.g., `GMT-8`)

[`"longOffset"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#longoffset)

Long localized GMT format (e.g., `GMT-08:00`)

[`"shortGeneric"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#shortgeneric)

Short generic non-location format (e.g.: `PT`, `Los Angeles Zeit`).

[`"longGeneric"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#longgeneric)

Long generic non-location format (e.g.: `Pacific Time`, `Nordamerikanische Westküstenzeit`)

**Note:** Timezone display may fall back to another format if a required string is unavailable. For example, the non-location formats should display the timezone without a specific country/city location like "Pacific Time", but may fall back to a timezone like "Los Angeles Time".

##### Date-time component default values

If any of the date-time component options are specified, then `dateStyle` and `timeStyle` must be `undefined`. If all date-time component options and `dateStyle`/`timeStyle` are `undefined`, some default options for date-time components are set, which depend on the object that the formatting method was called with:

*   When formatting [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
     and [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    , `year`, `month`, and `day` default to `"numeric"`.
*   When formatting [`Temporal.PlainTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime)
    , `hour`, `minute`, and `second` default to `"numeric"`.
*   When formatting [`Temporal.PlainYearMonth`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth)
    , `year` and `month` default to `"numeric"`.
*   When formatting [`Temporal.PlainMonthDay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainMonthDay)
    , `month` and `day` default to `"numeric"`.
*   When formatting [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
     and [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
    , `year`, `month`, `day`, `hour`, `minute`, and `second` default to `"numeric"`.

##### Format matching

Implementations are required to support displaying at least the following subsets of date-time components:

*   `weekday`, `year`, `month`, `day`, `hour`, `minute`, `second`
*   `weekday`, `year`, `month`, `day`
*   `year`, `month`, `day`
*   `year`, `month`
*   `month`, `day`
*   `hour`, `minute`, `second`
*   `hour`, `minute`

The date-time component styles requested might not directly correspond to a valid format supported by the locale, so the format matcher allows you to specify how to match the requested styles to the closest supported format.

[`formatMatcher`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#formatmatcher)

The format matching algorithm to use. Possible values are `"basic"` and `"best fit"`; the default is `"best fit"`. The algorithm for `"best fit"` is implementation-defined, and `"basic"` is [defined by the spec](https://tc39.es/ecma402/#sec-basicformatmatcher "External link (opens in new tab)")
. This option is only used when both `dateStyle` and `timeStyle` are `undefined` (so that each date-time component's format is individually customizable).

#### Style shortcuts

[`dateStyle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#datestyle)

The [date formatting style](https://cldr.unicode.org/translation/date-time/date-time-patterns#h.aa5zjyepm6vh "External link (opens in new tab)")
 to use. Possible values are `"full"`, `"long"`, `"medium"`, and `"short"`. It expands to styles for `weekday`, `day`, `month`, `year`, and `era`, with the exact combination of values depending on the locale. When formatting objects such as [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
, [`Temporal.PlainYearMonth`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth)
, and [`Temporal.PlainMonthDay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainMonthDay)
, `dateStyle` will resolve to only those fields relevant to the object.

[`timeStyle`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#timestyle)

The [time formatting style](https://cldr.unicode.org/translation/date-time/date-time-patterns#h.588vo3awdscu "External link (opens in new tab)")
 to use. Possible values are `"full"`, `"long"`, `"medium"`, and `"short"`. It expands to styles for `hour`, `minute`, `second`, and `timeZoneName`, with the exact combination of values depending on the locale.

**Note:** `dateStyle` and `timeStyle` can be used with each other, but not with other date-time component options (e.g., `weekday`, `hour`, `month`, etc.).

You can format different object types depending on which of the style shortcut options you include:

*   If the `dateStyle` is specified, then you can format [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
    , [`Temporal.PlainYearMonth`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainYearMonth)
    , and [`Temporal.PlainMonthDay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainMonthDay)
     objects.
*   If the `timeStyle` is specified, then you can format [`Temporal.PlainTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime)
     objects.
*   If either `dateStyle` or `timeStyle` is specified, then you can format [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
     and [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
     objects.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#return_value)

A new `Intl.DateTimeFormat` object.

**Note:** The text below describes behavior that is marked by the specification as "optional". It may not work in all environments. Check the [browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#browser_compatibility)
.

Normally, `Intl.DateTimeFormat()` can be called with or without [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
, and a new `Intl.DateTimeFormat` instance is returned in both cases. However, if the [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
 value is an object that is [`instanceof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)
 `Intl.DateTimeFormat` (doesn't necessarily mean it's created via `new Intl.DateTimeFormat`; just that it has `Intl.DateTimeFormat.prototype` in its prototype chain), then the value of `this` is returned instead, with the newly created `Intl.DateTimeFormat` object hidden in a `[Symbol(IntlLegacyConstructedSymbol)]` property (a unique symbol that's reused between instances).

Note that there's only one actual `Intl.DateTimeFormat` instance here: the one hidden in `[Symbol(IntlLegacyConstructedSymbol)]`. Calling the [`format()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format)
 and [`resolvedOptions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)
 methods on `formatter` would correctly use the options stored in that instance, but calling all other methods (e.g., [`formatRange()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange)
) would fail: "TypeError: formatRange method called on incompatible Object", because those methods don't consult the hidden instance's options.

This behavior, called `ChainDateTimeFormat`, does not happen when `Intl.DateTimeFormat()` is called without `new` but with `this` set to anything else that's not an `instanceof Intl.DateTimeFormat`. If you call it directly as `Intl.DateTimeFormat()`, the `this` value is [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
, and a new `Intl.DateTimeFormat` instance is created normally.

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `locales` or `options` contain invalid values.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#examples)

-----------------------------------------------------------------------------------------------------------------------------------------

### [Using DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#using_datetimeformat)

In basic use without specifying a locale, `DateTimeFormat` uses the default locale and default options.

### [Using timeStyle and dateStyle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#using_timestyle_and_datestyle)

`dateStyle` and `timeStyle` provide a shortcut for setting multiple date-time component options at once. For example, for `en-US`, `dateStyle: "short"` is equivalent to setting `year: "2-digit", month: "numeric", day: "numeric"`, and `timeStyle: "short"` is equivalent to setting `hour: "numeric", minute: "numeric"`.

However, the exact (locale dependent) component styles they resolve to are not included in the [resolved options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)
. This ensures the result of `resolvedOptions()` can be passed directly to the `Intl.DateTimeFormat()` constructor (because an `options` object with both `dateStyle` or `timeStyle` and individual date or time component styles is not valid).

### [Using dayPeriod](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#using_dayperiod)

Use the `dayPeriod` option to output a string for the times of day ("in the morning", "at night", "noon", etc.). Note, that this only works when formatting for a 12 hour clock (`hourCycle: 'h12'` or `hourCycle: 'h11'`) and that for many locales the strings are the same irrespective of the value passed for the `dayPeriod`.

### [Using timeZoneName](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#using_timezonename)

Use the `timeZoneName` option to output a string for the timezone ("GMT", "Pacific Time", etc.).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-intl-datetimeformat-constructor](https://tc39.es/ecma402/#sec-intl-datetimeformat-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#see_also)

-----------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
    
*   [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf)
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/datetimeformat/datetimeformat/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/datetimeformat/datetimeformat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDateTimeFormat%2FDateTimeFormat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdatetimeformat%2Fdatetimeformat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDateTimeFormat%2FDateTimeFormat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdatetimeformat%2Fdatetimeformat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5e0388c53dfc75003e83f79181797c3f66455971%0A*+Document+last+modified%3A+2026-01-21T21%3A15%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
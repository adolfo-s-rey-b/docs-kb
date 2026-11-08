*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#mdn-search)
    

Intl.DurationFormat() constructor
=================================

Baseline 2025

Newly available

Since March 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Intl.DurationFormat()`** constructor creates [`Intl.DurationFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat)
 objects.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#syntax)

-------------------------------------------------------------------------------------------------------------------------------------

**Note:** `Intl.DurationFormat()` can only be constructed with [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)
. Attempting to call it without `new` throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
.

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#parameters)

[`locales` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#locales)

A string with a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 or an [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale)
 instance, or an array of such locale identifiers. The runtime's default locale is used when `undefined` is passed or when none of the specified locale identifiers is supported. For the general form and interpretation of the `locales` argument, see [the parameter description on the `Intl` main page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument)
.

The following Unicode extension key is allowed:

[`nu`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#nu)

See [`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#numberingsystem)
.

This key can also be set with `options` (as listed below). When both are set, the `options` property takes precedence.

[`options` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#options)

An object containing the following properties, in the order they are retrieved (all of them are optional):

[`localeMatcher`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#localematcher)

The locale matching algorithm to use. Possible values are `"lookup"` and `"best fit"`; the default is `"best fit"`. For information about this option, see [Locale identification and negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
.

[`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#numberingsystem)

The numbering system to use for number formatting, such as `"arab"`, `"hans"`, `"mathsans"`, and so on. For a list of supported numbering system types, see [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_numbering_system_types)
; the default is locale dependent. This option can also be set through the `nu` Unicode extension key; if both are provided, this `options` property takes precedence.

[`style`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#style)

The style of the formatted duration. This value is used as the default for all other unit options, and also corresponds to the `style` option of [`Intl.ListFormat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat/ListFormat)
 when concatenating the list of duration units. Possible values are:

[`"long"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#long)

E.g., 1 hour and 50 minutes

[`"short"` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#short)

E.g., 1 hr, 50 min

[`"narrow"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#narrow)

E.g., 1h 50m

[`"digital"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#digital)

E.g., 1:50:00

[`years`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#years)

The style of the formatted years. Possible values are `"long"`, `"short"`, and `"narrow"`; the default is `options.style` if it's not `"digital"`, and `"short"` otherwise.

[`yearsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#yearsdisplay)

Whether to always display years, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `years` is unspecified, and `"always"` otherwise.

[`months`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#months)

The style of the formatted months. Possible values are `"long"`, `"short"`, and `"narrow"`; the default is `options.style` if it's not `"digital"`, and `"short"` otherwise.

[`monthsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#monthsdisplay)

Whether to always display months, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `months` is unspecified, and `"always"` otherwise.

[`weeks`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#weeks)

The style of the formatted weeks. Possible values are `"long"`, `"short"`, and `"narrow"`; the default is `options.style` if it's not `"digital"`, and `"short"` otherwise.

[`weeksDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#weeksdisplay)

Whether to always display weeks, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `weeks` is unspecified, and `"always"` otherwise.

[`days`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#days)

The style of the formatted days. Possible values are `"long"`, `"short"`, and `"narrow"`; the default is `options.style` if it's not `"digital"`, and `"short"` otherwise.

[`daysDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#daysdisplay)

Whether to always display days, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `days` is unspecified, and `"always"` otherwise.

[`hours`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#hours)

The style of the formatted hours. Possible values are `"long"`, `"short"`, `"narrow"`, `"numeric"`, and `"2-digit"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`hoursDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#hoursdisplay)

Whether to always display hours, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `hours` is unspecified and `options.style` is not `"digital"`, and `"always"` otherwise.

[`minutes`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#minutes)

The style of the formatted minutes.

*   If `hours` is `"numeric"` or `"2-digit"`, possible values are `"numeric"` and `"2-digit"`, and `"numeric"` is normalized to `"2-digit"`; the default is `"numeric"`.
*   Otherwise, possible values are `"long"`, `"short"`, `"narrow"`, `"numeric"`, and `"2-digit"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`minutesDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#minutesdisplay)

Whether to always display minutes, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `minutes` is unspecified and `options.style` is not `"digital"`, and `"always"` otherwise.

[`seconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#seconds)

The style of the formatted seconds.

*   If `minutes` is `"numeric"` or `"2-digit"`, possible values are `"numeric"` and `"2-digit"`, and `"numeric"` is normalized to `"2-digit"`; the default is `"numeric"`.
*   Otherwise, possible values are `"long"`, `"short"`, `"narrow"`, `"numeric"`, and `"2-digit"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`secondsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#secondsdisplay)

Whether to always display seconds, or only if nonzero. Possible values are `"always"` and `"auto"`; the default is `"auto"` if `seconds` is unspecified and `options.style` is not `"digital"`, and `"always"` otherwise.

[`milliseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#milliseconds)

The style of the formatted milliseconds.

*   If `seconds` is `"numeric"` or `"2-digit"`, the only possible value is `"numeric"`; the default is `"numeric"`.
*   Otherwise, possible values are `"long"`, `"short"`, `"narrow"`, and `"numeric"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`millisecondsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#millisecondsdisplay)

Whether to always display milliseconds, or only if nonzero.

*   If `seconds` is `"numeric"` or `"2-digit"`, the only possible value is `"auto"`; the default is only `"auto"` when `milliseconds` is unspecified.
*   Otherwise, possible values are `"always"` and `"auto"`; the default is `"auto"` if `milliseconds` is unspecified, and `"always"` otherwise.

[`microseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#microseconds)

The style of the formatted microseconds.

*   If `milliseconds` is `"numeric"`, the only possible value is `"numeric"`; the default is `"numeric"`.
*   Otherwise, possible values are `"long"`, `"short"`, `"narrow"`, and `"numeric"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`microsecondsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#microsecondsdisplay)

Whether to always display microseconds, or only if nonzero.

*   If `milliseconds` is `"numeric"`, the only possible value is `"auto"`; the default is only `"auto"` when `microseconds` is unspecified.
*   Otherwise, possible values are `"always"` and `"auto"`; the default is `"auto"` if `microseconds` is unspecified, and `"always"` otherwise.

[`nanoseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#nanoseconds)

The style of the formatted nanoseconds.

*   If `microseconds` is `"numeric"`, the only possible value is `"numeric"`; the default is `"numeric"`.
*   Otherwise, possible values are `"long"`, `"short"`, `"narrow"`, and `"numeric"`; the default is `options.style` if it's not `"digital"`, and `"numeric"` otherwise.

[`nanosecondsDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#nanosecondsdisplay)

Whether to always display nanoseconds, or only if nonzero.

*   If `microseconds` is `"numeric"`, the only possible value is `"auto"`; the default is only `"auto"` when `nanoseconds` is unspecified.
*   Otherwise, possible values are `"always"` and `"auto"`; the default is `"auto"` if `nanoseconds` is unspecified, and `"always"` otherwise.

[`fractionalDigits`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#fractionaldigits)

Number of how many fractional second digits to display in the output. Possible values are from `0` to `9`; the default is `undefined` (include as many fractional digits as necessary).

### [Exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `locales` or `options` contain invalid values.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#description)

-----------------------------------------------------------------------------------------------------------------------------------------------

For each time segment, an [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)
 object is constructed under the hood. It uses the following options (see [`Intl.NumberFormat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat)
 for details):

*   `numberingSystem`: the value of `options.numberingSystem`

When `milliseconds`, `microseconds`, or `nanoseconds` uses the `"numeric"` style, the following options are also used:

*   `minimumFractionDigits`: `0` when `options.fractionalDigits` is `undefined`, `options.fractionalDigits` otherwise
*   `maximumFractionDigits`: `9` when `options.fractionalDigits` is `undefined`, `options.fractionalDigits` otherwise
*   `roundingMode`: `"trunc"`

When the time segment uses the `"2-digit"` style, the following options are also used:

*   `minimumIntegerDigits`: `2`

When the time segment uses the `"long"`, `"short"`, or `"narrow"` style, the following options are also used:

*   `style`: `"unit"` when `"long"`, `"short"`, or `"narrow"` is specified, `undefined` otherwise
*   `unit`: the currently formatted unit (`"years"`, `"days"`, `"nanoseconds"`, etc.)
*   `unitDisplay`: the value of the time segment style (`"long"`, `"short"`, or `"narrow"`)

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#examples)

-----------------------------------------------------------------------------------------------------------------------------------------

### [Using the Intl.DurationFormat() constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#using_the_intl.durationformat_constructor)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Intl.DurationFormat  <br>\# sec-intl-durationformat-constructor](https://tc39.es/proposal-intl-duration-format/#sec-intl-durationformat-constructor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat#see_also)

-----------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DurationFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat)
    
*   [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf)
    
*   [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DurationFormat/DurationFormat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/durationformat/durationformat/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/durationformat/durationformat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDurationFormat%2FDurationFormat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdurationformat%2Fdurationformat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDurationFormat%2FDurationFormat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdurationformat%2Fdurationformat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
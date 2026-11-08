*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#mdn-search)
    

Intl.DateTimeFormat.prototype.resolvedOptions()
===============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`resolvedOptions()`** method of [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
 instances returns a new object with properties reflecting the options computed during initialization of this `DateTimeFormat` object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#try_it)

--------------------------------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#syntax)

--------------------------------------------------------------------------------------------------------------------------------------

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#return_value)

A new object with properties reflecting the options computed during the initialization of this `DateTimeFormat` object. The object has the following properties, in the order they are listed:

[`locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#locale)

The [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 for the locale actually used, determined by the [locale negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
 process. Only the `ca`, `hc`, and `nu` Unicode extension keys, if requested, may be included in the output.

[`calendar`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#calendar)

The value provided for this property in the `options` argument, or using the Unicode extension key `"ca"`, with default filled in as needed. It is a supported [calendar type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
 for this locale. The default is locale dependent.

[`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#numberingsystem)

The value provided for this property in the `options` argument, or using the Unicode extension key `"nu"`, with default filled in as needed. It is a supported [numbering system](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_numbering_system_types)
 for this locale. The default is locale dependent.

[`timeZone`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#timezone)

The value provided for this property in the `options` argument, with default filled in as needed. It is an [IANA time zone name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
. The default is the runtime's default time zone.

**Note:** The standardization of `Temporal` requires browsers to use the same identifier as originally specified, without canonicalization to a different alias. See [time zones and offsets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
 for more information.

[`hourCycle` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#hourcycle)

The value provided for this property in the `options` argument, or using the Unicode extension key `"hc"`, with default filled in as needed. If `hour12` was provided in the `options`, then that overrides other `hourCycle` settings. It is only present if the resolved options also include `hour` or `timeStyle`. It is either `"h11"`, `"h12"`, `"h23"`, or `"h24"`. The default is locale dependent, although `"h24"` is never a default.

[`hour12` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#hour12)

Calculated from `hourCycle`. It is only present if the resolved options also include `hour` or `timeStyle`. It is `true` if `hourCycle` is `"h11"` or `"h12"`, and `false` if `hourCycle` is `"h23"` or `"h24"`.

[`weekday`, `era`, `year`, `month`, `day`, `dayPeriod`, `hour`, `minute`, `second`, `fractionalSecondDigits`, `timeZoneName` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#weekday)

The values resulting from format matching between the corresponding properties in the `options` argument and the available combinations and representations for date-time formatting in the selected locale. Some of these properties may not be present, indicating that the corresponding components will not be represented in formatted output. `weekday`, `era`, and `dayPeriod` are either `"narrow"`, `"short"`, or `"long"`; `year`, `day`, `hour`, `minute`, and `second` are either `"numeric"`, `"2-digit"`, or `"narrow"`; `month` is either `"numeric"`, `"2-digit"`, `"narrow"`, `"short"`, or `"long"`; `fractionalSecondDigits` is either `1`, `2`, or `3`; `timeZoneName` is either `"short"`, `"long"`, `"shortOffset"`, `"longOffset"`, `"shortGeneric"`, or `"longGeneric"`.

If these properties were requested in `options`, the constructor prevents `dateStyle` and `timeStyle` from being specified, so the below group will never be present.

[`dateStyle`, `timeStyle` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#datestyle)

The values provided for these properties in the `options` argument. They are either `"full"`, `"long"`, `"medium"`, `"short"`, or `"none"`. Some of these properties may not be present, indicating that the corresponding components will not be represented in formatted output.

If these properties were requested in `options`, the constructor prevents individual date time component options from being specified, so the above group will never be present.

**Note:** Although `dateStyle` and `timeStyle` are shortcuts for individual date and time component styles, the exact (locale dependent) component styles they resolve to are not included in the resolved options. This ensures the result of `resolvedOptions()` can be passed directly to the `Intl.DateTimeFormat()` constructor (because an `options` object with both `dateStyle` or `timeStyle` and individual date or time component styles is not valid).

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#examples)

------------------------------------------------------------------------------------------------------------------------------------------

### [Using the resolvedOptions method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#using_the_resolvedoptions_method)

### [Getting the user's time zone and locale preferences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#getting_the_users_time_zone_and_locale_preferences)

The `Intl.DateTimeFormat` constructor without any options uses the current system settings. You can use `resolvedOptions()` to get the user's current time zone and locale's preferred calendar and numbering system:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#specifications)

------------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-intl.datetimeformat.prototype.resolvedoptions](https://tc39.es/ecma402/#sec-intl.datetimeformat.prototype.resolvedoptions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions#see_also)

------------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/datetimeformat/resolvedoptions/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/datetimeformat/resolvedoptions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDateTimeFormat%2FresolvedOptions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdatetimeformat%2Fresolvedoptions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FDateTimeFormat%2FresolvedOptions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fdatetimeformat%2Fresolvedoptions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
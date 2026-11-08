*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#mdn-search)
    

Date
====

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

JavaScript **`Date`** objects represent a single moment in time in a platform-independent format. `Date` objects encapsulate an integral number that represents milliseconds since the midnight at the beginning of January 1, 1970, UTC (the _epoch_).

**Note:** With the introduction of the [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
 API, the `Date` object is considered a legacy feature. Consider using `Temporal` for new code and migrate existing code over to it if possible (check the [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#browser_compatibility)
. We will be writing a usage guide soon!

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#description)

-----------------------------------------------------------------------------------------------------------------

### [The epoch, timestamps, and invalid date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)

A JavaScript date is fundamentally specified as the time in milliseconds that has elapsed since the [epoch](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-time-values-and-time-range "External link (opens in new tab)")
, which is defined as the midnight at the beginning of January 1, 1970, UTC (equivalent to the [UNIX epoch](https://developer.mozilla.org/en-US/docs/Glossary/Unix_time)
). This timestamp is _timezone-agnostic_ and uniquely defines an instant in history.

**Note:** While the time value at the heart of a Date object is UTC, the basic methods to fetch the date and time or its components all work in the local (i.e., host system) time zone and offset.

The maximum timestamp representable by a `Date` object is slightly smaller than the maximum safe integer ([`Number.MAX_SAFE_INTEGER`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)
, which is 9,007,199,254,740,991). A `Date` object can represent a maximum of ±8,640,000,000,000,000 milliseconds, or ±100,000,000 (one hundred million) days, relative to the epoch. This is the range from April 20, 271821 BC to September 13, 275760 AD. Any attempt to represent a time outside this range results in the `Date` object holding a timestamp value of [`NaN`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)
, which is an "Invalid Date".

There are various methods that allow you to interact with the timestamp stored in the date:

*   You can interact with the timestamp value directly using the [`getTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)
     and [`setTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime)
     methods.
*   The [`valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/valueOf)
     and [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Symbol.toPrimitive)
     (when passed `"number"`) methods — which are automatically called in [number coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_coercion)
     — return the timestamp, causing `Date` objects to behave like their timestamps when used in number contexts.
*   All static methods ([`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
    , [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
    , and [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC)
    ) return timestamps instead of `Date` objects.
*   The [`Date()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)
     constructor can be called with a timestamp as the only argument.

### [Date components and time zones](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_components_and_time_zones)

A date is represented internally as a single number, the _timestamp_. When interacting with it, the timestamp needs to be interpreted as a structured date-and-time representation. There are always two ways to interpret a timestamp: as a local time or as a Coordinated Universal Time (UTC), the global standard time defined by the World Time Standard. The local timezone is not stored in the date object, but is determined by the host environment (user's device).

**Note:** UTC should not be confused with the [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time "External link (opens in new tab)")
 (GMT), because they are not always equal — this is explained in more detail in the linked Wikipedia page.

For example, the timestamp 0 represents a unique instant in history, but it can be interpreted in two ways:

*   As a UTC time, it is midnight at the beginning of January 1, 1970, UTC,
*   As a local time in New York (UTC-5), it is 19:00:00 on December 31, 1969.

The [`getTimezoneOffset()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)
 method returns the difference between UTC and the local time in minutes. Note that the timezone offset does not only depend on the current timezone, but also on the time represented by the `Date` object, because of daylight saving time and historical changes. In essence, the timezone offset is the offset from UTC time, at the time represented by the `Date` object and at the location of the host environment.

There are two groups of `Date` methods: one group gets and sets various date components by interpreting the timestamp as a local time, while the other uses UTC.

| Component | Local |     | UTC |     |
| --- | --- | --- | --- | --- |
| Get | Set | Get | Set |
| --- | --- | --- | --- | --- |
| Year | [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear) | [`setFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear) | [`getUTCFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCFullYear) | [`setUTCFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCFullYear) |
| Month | [`getMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth) | [`setMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMonth) | [`getUTCMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMonth) | [`setUTCMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMonth) |
| Date (of month) | [`getDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate) | [`setDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setDate) | [`getUTCDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCDate) | [`setUTCDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCDate) |
| Hours | [`getHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours) | [`setHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours) | [`getUTCHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCHours) | [`setUTCHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCHours) |
| Minutes | [`getMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMinutes) | [`setMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMinutes) | [`getUTCMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMinutes) | [`setUTCMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMinutes) |
| Seconds | [`getSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getSeconds) | [`setSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setSeconds) | [`getUTCSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCSeconds) | [`setUTCSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCSeconds) |
| Milliseconds | [`getMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMilliseconds) | [`setMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMilliseconds) | [`getUTCMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMilliseconds) | [`setUTCMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMilliseconds) |
| Day (of week) | [`getDay()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay) | N/A | [`getUTCDay()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCDay) | N/A |

The [`Date()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)
 constructor can be called with two or more arguments, in which case they are interpreted as the year, month, day, hour, minute, second, and millisecond, respectively, in local time. [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC)
 works similarly, but it interprets the components as UTC time and also accepts a single argument representing the year.

**Note:** Some methods, including the `Date()` constructor, `Date.UTC()`, and the deprecated [`getYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear)
/[`setYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setYear)
 methods, interpret a two-digit year as a year in the 1900s. For example, `new Date(99, 5, 24)` is interpreted as June 24, 1999, not June 24, 99. See [Interpretation of two-digit years](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#interpretation_of_two-digit_years)
 for more information.

When a segment overflows or underflows its expected range, it usually "carries over to" or "borrows from" the higher segment. For example, if the month is set to 12 (months are zero-based, so December is 11), it becomes the January of the next year. If the day of month is set to 0, it becomes the last day of the previous month. This also applies to dates specified with the [date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
.

When attempting to set the local time to a time falling within an offset transition (usually daylight saving time), the exact time is derived using the same behavior as `Temporal`'s [`disambiguation: "compatible"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ambiguity_and_gaps_from_local_time_to_utc_time)
 option. That is, if the local time corresponds to two instants, the earlier one is chosen; if the local time does not exist (there is a gap), we go forward by the gap duration.

### [Date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)

There are many ways to format a date as a string. The JavaScript specification only specifies one format to be universally supported: the [_date time string format_](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date-time-string-format "External link (opens in new tab)")
, a simplification of the ISO 8601 calendar date extended format. The format is as follows:

YYYY-MM-DDTHH:mm:ss.sssZ

*   `YYYY` is the year, with four digits (`0000` to `9999`), or as an _expanded year_ of `+` or `-` followed by six digits. The sign is required for expanded years. `-000000` is explicitly disallowed as a valid year.
*   `MM` is the month, with two digits (`01` to `12`). Defaults to `01`.
*   `DD` is the day of the month, with two digits (`01` to `31`). Defaults to `01`.
*   `T` is a literal character, which indicates the beginning of the _time_ part of the string. The `T` is required when specifying the time part.
*   `HH` is the hour, with two digits (`00` to `23`). As a special case, `24:00:00` is allowed, and is interpreted as midnight at the beginning of the next day. Defaults to `00`.
*   `mm` is the minute, with two digits (`00` to `59`). Defaults to `00`.
*   `ss` is the second, with two digits (`00` to `59`). Defaults to `00`.
*   `sss` is the millisecond, with three digits (`000` to `999`). Defaults to `000`.
*   `Z` is the timezone offset, which can either be the literal character `Z` (indicating UTC), or `+` or `-` followed by `HH:mm`, the offset in hours and minutes from UTC.

Various components can be omitted, so the following are all valid:

*   Date-only form: `YYYY`, `YYYY-MM`, `YYYY-MM-DD`
*   Date-time form: one of the above date-only forms, followed by `T`, followed by `HH:mm`, `HH:mm:ss`, or `HH:mm:ss.sss`. Each combination can be followed by a time zone offset.

For example, `"2011-10-10"` (_date-only_ form), `"2011-10-10T14:48:00"` (_date-time_ form), or `"2011-10-10T14:48:00.000+09:00"` (_date-time_ form with milliseconds and time zone) are all valid date time strings.

When the time zone offset is absent, **date-only forms are interpreted as a UTC time and date-time forms are interpreted as a local time.** The interpretation as a UTC time is due to a historical spec error that was not consistent with ISO 8601 but could not be changed due to web compatibility. See [Broken Parser – A Web Reality Issue](https://maggiepint.com/2017/04/11/fixing-javascript-date-web-compatibility-and-reality/ "External link (opens in new tab)")
.

[`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)
 and the [`Date()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)
 constructor both accept strings in the date time string format as input. Furthermore, implementations are allowed to support other date formats when the input fails to match this format.

The [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
 method returns a string representation of the date in the date time string format, with the time zone offset always set to `Z` (UTC).

**Note:** You are encouraged to make sure your input conforms to the date time string format above for maximum compatibility, because support for other formats is not guaranteed. However, there are some formats that are supported in all major implementations — like [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822 "External link (opens in new tab)")
 format — in which case their usage can be acceptable. Always conduct [cross-browser tests](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing)
 to ensure your code works in all target browsers. A library can help if many different formats are to be accommodated.

Non-standard strings can be parsed in any way as desired by the implementation, including the time zone — most implementations use the local time zone by default. Implementations are not required to return invalid date for out-of-bounds date components, although they usually do. A string may have in-bounds date components (with the bounds defined above), but does not represent a date in reality (for example, "February 30"). Implementations behave inconsistently in this case. The [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse#examples)
 page offers more examples about these non-standard cases.

### [Other ways to format a date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#other_ways_to_format_a_date)

*   [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
     returns a string in the format `1970-01-01T00:00:00.000Z` (the date time string format introduced above, which is simplified [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601 "External link (opens in new tab)")
    ). [`toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON)
     calls `toISOString()` and returns the result.
*   [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)
     returns a string in the format `Thu Jan 01 1970 00:00:00 GMT+0000 (Coordinated Universal Time)`, while [`toDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toDateString)
     and [`toTimeString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString)
     return the date and time parts of the string, respectively. [`[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Symbol.toPrimitive)
     (when passed `"string"` or `"default"`) calls `toString()` and returns the result.
*   [`toUTCString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)
     returns a string in the format `Thu, 01 Jan 1970 00:00:00 GMT` (generalized [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231 "External link (opens in new tab)")
    ).
*   [`toLocaleDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)
    , [`toLocaleTimeString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString)
    , and [`toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)
     use locale-specific date and time formats, usually provided by the [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
     API.

See the [Formats of `toString` method return values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#formats_of_tostring_method_return_values)
 section for examples.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#constructor)

-----------------------------------------------------------------------------------------------------------------

[`Date()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)

When called as a constructor, returns a new `Date` object. When called as a function, returns a string representation of the current date and time.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#static_methods)

-----------------------------------------------------------------------------------------------------------------------

[`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)

Returns the numeric value corresponding to the current time—the number of milliseconds since January 1, 1970 00:00:00 UTC, with leap seconds ignored.

[`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)

Parses a string representation of a date and returns the number of milliseconds since January 1, 1970 00:00:00 UTC, with leap seconds ignored.

[`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC)

Accepts the same parameters as the longest form of the constructor (i.e., 2 to 7) and returns the number of milliseconds since January 1, 1970 00:00:00 UTC, with leap seconds ignored.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#instance_properties)

---------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Date.prototype` and shared by all `Date` instances.

[`Date.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Date` instances, the initial value is the [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)
 constructor.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#instance_methods)

---------------------------------------------------------------------------------------------------------------------------

[`Date.prototype.getDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate)

Returns the day of the month (`1` – `31`) for the specified date according to local time.

[`Date.prototype.getDay()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay)

Returns the day of the week (`0` – `6`) for the specified date according to local time.

[`Date.prototype.getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)

Returns the year (4 digits for 4-digit years) of the specified date according to local time.

[`Date.prototype.getHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours)

Returns the hour (`0` – `23`) in the specified date according to local time.

[`Date.prototype.getMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMilliseconds)

Returns the milliseconds (`0` – `999`) in the specified date according to local time.

[`Date.prototype.getMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMinutes)

Returns the minutes (`0` – `59`) in the specified date according to local time.

[`Date.prototype.getMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)

Returns the month (`0` – `11`) in the specified date according to local time.

[`Date.prototype.getSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getSeconds)

Returns the seconds (`0` – `59`) in the specified date according to local time.

[`Date.prototype.getTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)

Returns the numeric value of the specified date as the number of milliseconds since January 1, 1970 00:00:00 UTC. (Negative values are returned for prior times.)

[`Date.prototype.getTimezoneOffset()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)

Returns the time-zone offset in minutes for the current locale.

[`Date.prototype.getUTCDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCDate)

Returns the day (date) of the month (`1` – `31`) in the specified date according to universal time.

[`Date.prototype.getUTCDay()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCDay)

Returns the day of the week (`0` – `6`) in the specified date according to universal time.

[`Date.prototype.getUTCFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCFullYear)

Returns the year (4 digits for 4-digit years) in the specified date according to universal time.

[`Date.prototype.getUTCHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCHours)

Returns the hours (`0` – `23`) in the specified date according to universal time.

[`Date.prototype.getUTCMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMilliseconds)

Returns the milliseconds (`0` – `999`) in the specified date according to universal time.

[`Date.prototype.getUTCMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMinutes)

Returns the minutes (`0` – `59`) in the specified date according to universal time.

[`Date.prototype.getUTCMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCMonth)

Returns the month (`0` – `11`) in the specified date according to universal time.

[`Date.prototype.getUTCSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getUTCSeconds)

Returns the seconds (`0` – `59`) in the specified date according to universal time.

[`Date.prototype.getYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear)

Returns the year (usually 2–3 digits) in the specified date according to local time. Use [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
 instead.

[`Date.prototype.setDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setDate)

Sets the day of the month for a specified date according to local time.

[`Date.prototype.setFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)

Sets the full year (e.g., 4 digits for 4-digit years) for a specified date according to local time.

[`Date.prototype.setHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours)

Sets the hours for a specified date according to local time.

[`Date.prototype.setMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMilliseconds)

Sets the milliseconds for a specified date according to local time.

[`Date.prototype.setMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMinutes)

Sets the minutes for a specified date according to local time.

[`Date.prototype.setMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMonth)

Sets the month for a specified date according to local time.

[`Date.prototype.setSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setSeconds)

Sets the seconds for a specified date according to local time.

[`Date.prototype.setTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime)

Sets the `Date` object to the time represented by the number of milliseconds since January 1, 1970 00:00:00 UTC. Use negative numbers for times prior.

[`Date.prototype.setUTCDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCDate)

Sets the day of the month for a specified date according to universal time.

[`Date.prototype.setUTCFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCFullYear)

Sets the full year (e.g., 4 digits for 4-digit years) for a specified date according to universal time.

[`Date.prototype.setUTCHours()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCHours)

Sets the hour for a specified date according to universal time.

[`Date.prototype.setUTCMilliseconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMilliseconds)

Sets the milliseconds for a specified date according to universal time.

[`Date.prototype.setUTCMinutes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMinutes)

Sets the minutes for a specified date according to universal time.

[`Date.prototype.setUTCMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCMonth)

Sets the month for a specified date according to universal time.

[`Date.prototype.setUTCSeconds()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setUTCSeconds)

Sets the seconds for a specified date according to universal time.

[`Date.prototype.setYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setYear)

Sets the year (usually 2–3 digits) for a specified date according to local time. Use [`setFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)
 instead.

[`Date.prototype.toDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toDateString)

Returns the "date" portion of the `Date` as a human-readable string like `'Thu Apr 12 2018'`.

[`Date.prototype.toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)

Converts a date to a string following the ISO 8601 Extended Format.

[`Date.prototype.toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON)

Returns a string representing the `Date` using [`toISOString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
. Intended to be implicitly called by [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
.

[`Date.prototype.toLocaleDateString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)

Returns a string with a locality sensitive representation of the date portion of this date based on system settings.

[`Date.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString)

Returns a string with a locality-sensitive representation of this date. Overrides the [`Object.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toLocaleString)
 method.

[`Date.prototype.toLocaleTimeString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleTimeString)

Returns a string with a locality-sensitive representation of the time portion of this date, based on system settings.

[`Date.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)

Returns a string representing the specified `Date` object. Overrides the [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
 method.

[`Date.prototype.toTemporalInstant()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTemporalInstant)

Returns a new [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
 object with the same [`epochMilliseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant/epochMilliseconds)
 value as this date's [timestamp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#the_epoch_timestamps_and_invalid_date)
.

[`Date.prototype.toTimeString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString)

Returns the "time" portion of the `Date` as a human-readable string.

[`Date.prototype.toUTCString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)

Converts a date to a string using the UTC timezone.

[`Date.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/valueOf)

Returns the primitive value of a `Date` object. Overrides the [`Object.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
 method.

[`Date.prototype[Symbol.toPrimitive]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Symbol.toPrimitive)

Converts this `Date` object to a primitive value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#examples)

-----------------------------------------------------------------------------------------------------------

### [Several ways to create a Date object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#several_ways_to_create_a_date_object)

The following examples show several ways to create JavaScript dates:

**Note:** Creating a date from a string has a lot of behavior inconsistencies. See [date time string format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#date_time_string_format)
 for caveats on using different formats.

### [Formats of toString method return values](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#formats_of_tostring_method_return_values)

### [To get Date, Month and Year or Time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#to_get_date_month_and_year_or_time)

### [Interpretation of two-digit years](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#interpretation_of_two-digit_years)

`new Date()` exhibits legacy undesirable, inconsistent behavior with two-digit year values; specifically, when a `new Date()` call is given a two-digit year value, that year value does not get treated as a literal year and used as-is but instead gets interpreted as a relative offset — in some cases as an offset from the year `1900`, but in other cases, as an offset from the year `2000`.

So, to create and get dates between the years `0` and `99`, instead use the preferred [`setFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)
 and [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)
 methods:.

### [Calculating elapsed time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#calculating_elapsed_time)

The following examples show how to determine the elapsed time between two JavaScript dates in milliseconds.

Due to the differing lengths of days (due to daylight saving changeover), months, and years, expressing elapsed time in units greater than hours, minutes, and seconds requires addressing a number of issues, and should be thoroughly researched before being attempted.

**Note:** In browsers that support the [Performance API](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API)
's high-resolution time feature, [`Performance.now()`](https://developer.mozilla.org/en-US/docs/Web/API/Performance/now)
 can provide more reliable and precise measurements of elapsed time than [`Date.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
.

### [Get the number of seconds since the ECMAScript Epoch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#get_the_number_of_seconds_since_the_ecmascript_epoch)

In this case, it's important to return only an integer—so a simple division won't do. It's also important to only return actually elapsed seconds. (That's why this code uses [`Math.floor()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)
, and _not_ [`Math.round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)
.)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-date-objects](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`Date()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/date/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/date (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FDate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fdate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7e14795a6ef2bf5e760c315ce64800dd1cd98c29%0A*+Document+last+modified%3A+2025-12-08T17%3A29%3A19.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
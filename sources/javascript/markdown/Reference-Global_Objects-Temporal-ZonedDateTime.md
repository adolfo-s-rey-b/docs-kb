*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#mdn-search)
    

Temporal.ZonedDateTime
======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/291)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Temporal.ZonedDateTime`** object represents a date and time with a time zone. It is fundamentally represented as a combination of an [instant](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
, a time zone, and a calendar system.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#description)

-----------------------------------------------------------------------------------------------------------------------------------

A `ZonedDateTime` functions as a bridge between an exact time and a wall-clock time: it simultaneously represents an instant in history (like a [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
) and a local, wall-clock time (like a [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
). It does so by storing the instant, the time zone, and the calendar system. The time zone is used to convert between the instant and the local time, and the calendar system is used to interpret the local time.

`ZonedDateTime` is the only `Temporal` class that is time zone-aware. The addition of a time zone makes `ZonedDateTime` objects have important behavior differences from [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
 objects. Namely, you can no longer assume that "the time 1 minute afterwards" is the same every day, or that a day has 24 hours. In the worst case, an entire day may be missing from the local calendar. Below, we offer a quick overview of time zones and offsets and how they affect conversion between UTC time and local time.

### [Time zones and offsets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)

All times in JavaScript have one golden standard: the UTC time, which increments continuously and uniformly as physical time progresses. By contrast, users are more interested in their local time, which is the time they read on their calendars and clocks. The process of converting between UTC time and local time involves a time zone _offset_, which is calculated as:

local time = UTC time + offset

For example, if the UTC time is 1970-01-01T00:00:00, and the offset is "-05:00", then the local time is:

1970-01-01T00:00:00 + -05:00 = 1969-12-31T19:00:00

By suffixing this local time with the offset, thus expressing this time as "1969-12-31T19:00:00-05:00", it can now be unambiguously understood as an instant in history.

To know the offset, we need two pieces of information, the _time zone_, and the _instant_. The time zone is a region on Earth where the same offset is used at all times. Two clocks in the same time zone will always show the same time simultaneously, but the offset is not necessarily constant: that is, these clocks' times may change abruptly. This commonly happens during daylight saving time transitions, where the offset changes by an hour, which happens twice a year. Offsets can also change permanently due to political changes, e.g., a country switching time zones.

The time zones are stored in the [IANA Time Zone Database](https://www.iana.org/time-zones "External link (opens in new tab)")
. Each IANA time zone has:

*   A _primary time zone identifier_ that uniquely identifies the time zone. It usually refers to a geographic area anchored by a city (e.g., `Europe/Paris` or `Africa/Kampala`), but can also denote single-offset time zones like `UTC` (a consistent `+00:00` offset) or `Etc/GMT+5` (which for historical reasons is a negative offset `-05:00`). For historical reasons, the primary name for the UTC time zone is `UTC`, though in IANA it is `Etc/UTC`.
*   A _time zone definition_ in the form of a table that maps UTC date/time ranges (including future ranges) to specific offsets.
*   Zero or more _non-primary time zone identifiers_ that are aliases to the primary time zone identifier. These are usually historical names that are no longer in use, but are kept for compatibility reasons. See below for more information.

As input, named identifiers are matched case-insensitively. Internally, they are stored in their preferred case, and non-primary identifiers will _not_ be converted to their primary identifier.

**Note:** When setting the time zone name, you rarely want to set it to `"UTC"`. `ZonedDateTime` is intended to be displayed to users, but no human lives in the "UTC" time zone. If you don't know the time zone at construction time but know the wall-clock time, use a [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
. If you know the exact instant, use a [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
.

When a `Temporal` API accepts a _time zone identifier_, in addition to primary time zone identifiers and non-primary time zone identifiers, it also accepts an _offset time zone identifier_, which is in the same form as the offset, except subminute precision is not allowed. For example, `+05:30`, `-08`, `+0600` are all valid offsets identifiers. Internally, offset identifiers are stored in the `±HH:mm` form.

**Note:** Avoid using offset identifiers if there is a named time zone you can use instead. Even if a region has always used a single offset, it is better to use the named identifier to guard against future political changes to the offset.

If a region uses (or has used) multiple offsets, then using its named time zone is even more important. This is because `Temporal.ZonedDateTime` can use methods like `add` or `with` to create new instances at a different instant. If those derived instances correspond to an instant that uses a different offset (for example, after a Daylight Saving Time transition) then your calculations will have an incorrect local time. Using a named time zone ensures that local dates and times are always adjusted for the correct offset for that instant.

For convenience, when providing a time zone identifier to `Temporal` APIs such as `Temporal.ZonedDateTime.prototype.withTimeZone()` and the `timeZoneId` option of `Temporal.ZonedDateTime.from()`, you can provide it in a few other forms:

*   As another `ZonedDateTime` instance, whose `timeZoneId` will be used.
*   As an [RFC 9557 string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)
     with a time zone annotation, whose time zone identifier will be used.
*   As an ISO 8601 / RFC 3339 string containing an offset, whose offset will be used as an offset identifier; or, if using `Z`, then the `"UTC"` time zone is used. This usage is generally not recommended, because as discussed above, offset identifiers lack the ability to safely derive other `Temporal.ZonedDateTime` instances across an offset transition like when daylight saving time starts or ends. Instead, consider just using `Temporal.Instant` or fetching the user's actual named time zone.

The IANA time zone database changes from time to time, usually to add new time zones in response to political changes. However, on rare occasions, IANA time zone identifiers are renamed to match updated English translation of a city name or to update outdated naming conventions. For example, here are a few notable name changes:

| Current IANA primary identifier | Old, now non-primary identifier |
| --- | --- |
| `America/Argentina/Buenos_Aires` | `America/Buenos_Aires` |
| `Asia/Kolkata` | `Asia/Calcutta` |
| `Asia/Ho_Chi_Minh` | `Asia/Saigon` |
| `Europe/Kyiv` | `Europe/Kiev` |

Historically, these renames caused problems for programmers because the Unicode [CLDR database](https://github.com/unicode-org/cldr/blob/main/common/bcp47/timezone.xml "External link (opens in new tab)")
 (a library used by browsers to supply time zone identifiers and data) did not follow IANA's renaming for [stability reasons](https://unicode.org/reports/tr35/#Time_Zone_Identifiers "External link (opens in new tab)")
. As a result, some browsers like Chrome and Safari reported CLDR's outdated identifiers, while other browsers like Firefox overrode CLDR's defaults and reported the up-to-date primary identifiers.

With the introduction of Temporal, this behavior is now more standardized:

*   [CLDR data](https://github.com/unicode-org/cldr/blob/main/common/bcp47/timezone.xml "External link (opens in new tab)")
     now includes an `"_iana"` attribute that indicates the most up-to-date identifier if the older, stable identifier has been renamed. Browsers can use this new attribute to provide up-to-date identifiers to callers.
*   Time zone identifiers provided by the programmer will never be replaced with an alias. For example, if the caller provides `Asia/Calcutta` or `Asia/Kolkata` as the identifier input to [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
    , then the same identifier is returned in the resulting instance's [`timeZoneId`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/timeZoneId)
    . Note that the letter case of outputs are normalized to match IANA, so that `ASIA/calCuTTa` as input generates a [`timeZoneId`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/timeZoneId)
     of `Asia/Calcutta` as output.
*   When a time zone identifier is not provided by a caller but is instead sourced from the system itself (for example, when using [`Temporal.Now.timeZoneId()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Now/timeZoneId)
    ), modern identifiers are returned in all browsers. For city renames, there is a two-year lag before these system-provided-identifier APIs expose the new name, thereby giving other components (like a Node server) time to update their copies of the IANA database to recognize the new name.

Note that the attribution of primary identifiers preserves the country code: for example, the IANA database records `Atlantic/Reykjavik` as an alias for `Africa/Abidjan`, but because they correspond to different countries (Iceland and Côte d'Ivoire, respectively), they are treated as distinct primary identifiers.

This standardization applies outside of `Temporal` as well. For example, the `timeZone` option returned by [`Intl.DateTimeFormat.prototype.resolvedOptions()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions)
 is also never replaced with an alias, though browsers have traditionally canonicalized these identifiers prior to standardization by Temporal. On the other hand, [`Intl.Locale.prototype.getTimeZones()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getTimeZones)
 and [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf)
 (`timeZone` option) will return the most up-to-date identifier, while some browsers used to return the old, non-primary identifier.

### [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)

`ZonedDateTime` objects can be serialized and parsed using the [RFC 9557](https://datatracker.ietf.org/doc/html/rfc9557 "External link (opens in new tab)")
 format, an extension to the [ISO 8601 / RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339 "External link (opens in new tab)")
 format. The string has the following form (spaces are only for readability and should not be present in the actual string):

YYYY-MM-DD T HH:mm:ss.sssssssss Z/±HH:mm \[time\_zone\_id\] \[u-ca=calendar\_id\]

[`YYYY`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#yyyy)

Either a four-digit number, or a six-digit number with a `+` or `-` sign.

[`MM`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#mm)

A two-digit number from `01` to `12`.

[`DD`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#dd)

A two-digit number from `01` to `31`. The `YYYY`, `MM`, and `DD` components can be separated by `-` or nothing.

[`T` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#t)

The date-time separator, which can be `T`, `t`, or a space. Present if and only if `HH` is present.

[`HH` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#hh)

A two-digit number from `00` to `23`. Defaults to `00`.

[`mm` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#mm_2)

A two-digit number from `00` to `59`. Defaults to `00`.

[`ss.sssssssss` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ss.sssssssss)

A two-digit number from `00` to `59`. May optionally be followed by a `.` or `,` and one to nine digits. Defaults to `00`. The `HH`, `mm`, and `ss` components can be separated by `:` or nothing. You can omit either just `ss` or both `ss` and `mm`, so the time can be one of three forms: `HH`, `HH:mm`, or `HH:mm:ss.sssssssss`.

[`Z/±HH:mm` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#z%C2%B1hhmm)

Either the UTC designator `Z` or `z`, or an offset from UTC in the form `+` or `-` followed by the same format as the time component. Note that subminute precision (`:ss.sssssssss`) may be unsupported by other systems, and is accepted but never output. If omitted, the offset is derived from the time zone identifier. If present, then the time must be provided too. `Z` is not the same as `+00:00`: the former means that the time is given in UTC form regardless of the time zone identifier, while the latter means that the time is given in local time which happens to be UTC+0, and will be validated against the time zone identifier via the [`offset` option](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#offset_ambiguity)
.

[`[time_zone_id]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zone_id)

Replace `time_zone_id` with the time zone identifier (named or offset) as described above. May have a _critical flag_ by prefixing the identifier with `!`: e.g., `[!America/New_York]`. This flag generally tells other systems that it cannot be ignored if they don't support it. Note that it is required for `Temporal.ZonedDateTime.from()`: omitting it causes a `RangeError`. If you want to parse ISO 8601 / RFC 3339 strings without time zone identifier annotations, use [`Temporal.Instant.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant/from)
 instead.

[`[u-ca=calendar_id]` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#u-cacalendar_id)

Replace `calendar_id` with the calendar to use. See [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_calendar_types)
 for a list of commonly supported calendar types. Defaults to `[u-ca=iso8601]`. May have a _critical flag_ by prefixing the key with `!`: e.g., `[!u-ca=iso8601]`. This flag generally tells other systems that it cannot be ignored if they don't support it. The `Temporal` parser will throw an error if the annotations contain two or more calendar annotations and one of them is critical. Note that the `YYYY-MM-DD` is always interpreted as an ISO 8601 calendar date and then converted to the specified calendar.

As an input, other annotations in the `[key=value]` format are ignored, and they must not have the critical flag.

When serializing, you can configure the fractional second digits, whether to display the offset/time zone ID/calendar ID, and whether to add a critical flag for the annotations.

### [Ambiguity and gaps from local time to UTC time](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ambiguity_and_gaps_from_local_time_to_utc_time)

Given a time zone, conversion from UTC to local time is straightforward: you first get the offset using the time zone name and the instant, then add the offset to the instant. The reverse is not true: conversion from local time to UTC time, without an explicit offset, is ambiguous, because one local time can correspond to zero, one, or many UTC times. Consider the most common cause: daylight saving time transitions. Take New York as an example. Its standard offset is UTC-5, but during DST, all clocks are set forward by an hour, so the offset becomes UTC-4. In the US, transitions happen at 2:00 AM local time, so consider these two transition days:

| UTC time | New York time |
| --- | --- |
| 2024-03-10T06:58:00Z | 2024-03-10T01:58:00-05:00 |
| 2024-03-10T06:59:00Z | 2024-03-10T01:59:00-05:00 |
| 2024-03-10T07:00:00Z | 2024-03-10T03:00:00-04:00 |
| \--- | \--- |
| 2024-11-03T05:58:00Z | 2024-11-03T01:58:00-04:00 |
| 2024-11-03T05:59:00Z | 2024-11-03T01:59:00-04:00 |
| 2024-11-03T06:00:00Z | 2024-11-03T01:00:00-05:00 |

As you can see, in March, one hour disappeared from the local time, and in November, we have two hours that have the same wall-clock time. Suppose that we stored a `PlainDateTime` that says "2024-03-10T02:05:00", and we want to interpret it in the `America/New_York` time zone, there will be no time that corresponds to it, while a `PlainDateTime` that says "2024-11-03T01:05:00" can correspond to two different instants.

When constructing a `ZonedDateTime` from a local time (using [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
, [`Temporal.ZonedDateTime.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/with)
, [`Temporal.PlainDateTime.prototype.toZonedDateTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime/toZonedDateTime)
), the behavior for ambiguity and gaps is configurable via the `disambiguation` option:

[`earlier`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#earlier)

If there are two possible instants, choose the earlier one. If there is a gap, go back by the gap duration.

[`later`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#later)

If there are two possible instants, choose the later one. If there is a gap, go forward by the gap duration.

[`compatible` (default)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#compatible)

Same behavior as [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
: use `later` for gaps and `earlier` for ambiguities.

[`reject`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#reject)

Throw a `RangeError` whenever there is an ambiguity or a gap.

There are several cases where there's no ambiguity when constructing a `ZonedDateTime`:

*   If the time is specified in UTC via the `Z` offset.
*   If the offset is explicitly provided and used (see below).

### [Offset ambiguity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#offset_ambiguity)

We already demonstrated how ambiguity may arise from interpreting a local time in a time zone, without providing an explicit offset. However, if you provide an explicit offset, then another conflict arises: between the offset as specified, and the offset as calculated from the time zone and the local time. This is an unavoidable real-world issue: if you store a time in the future, with an anticipated offset, then before that time comes, the time zone definition may have changed due to political reasons. For example, suppose in 2018, we set a reminder at the time `2019-12-23T12:00:00-02:00[America/Sao_Paulo]` (which is a daylight saving time; Brazil is in the southern hemisphere, so it enters DST in October and exits in February). But before that time comes, in early 2019, Brazil decides to stop observing DST, so the real offset becomes `-03:00`. Should the reminder now still fire at noon (keeping the local time), or should it fire at 11:00 AM (keeping the exact time)?

For offset ambiguity to exist, a timestamp string must be parsed using different IANA Time Zone Database rules than the rules used when the timestamp was originally generated. This will never happen when timestamps are generated during the same execution of a JavaScript program, because the ECMAScript specification requires that IANA Time Zone Database rules must be consistent for the lifetime of a JavaScript program.

However, offset ambiguity may exist when a JavaScript program is parsing timestamps that were stored earlier, as in the `America/Sao_Paulo` example above, and the IANA Time Zone Database has been updated since the timestamp was originally generated. It can also happen when communicating timestamps between computers (or, rarely, between different software on the same computer!) that use different versions of the IANA Time Zone Database. The IANA Time Zone Database also has build options (for example, using or not using deprecated rules in `backzone`) that can cause offset ambiguity when communicating timestamps between computers using different software, even when the IANA Time Zone Database version is the same.

Offset ambiguity is rarely encountered and will almost always apply only to timestamps before 1970 or for timestamps that are months or years in the future. But when this problem happens, a `RangeError` will be thrown by default. When constructing a `ZonedDateTime` with [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
 or when updating it using the [`with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/with)
 method, you can prevent this exception by using the `offset` option to decide whether the offset or the time zone identifier "wins":

[`use`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#use)

Use the offset to calculate the exact time. This option "uses" the offset to decide the instant intended by the timestamp string, even if the offset at that instant has changed. The time zone identifier is still used to then infer the (possibly updated) offset and use that offset to convert the exact time to local time. In the `2019-12-23T12:00:00-02:00[America/Sao_Paulo]` example above, this option would cause the reminder to fire at 11:00 AM local time.

[`ignore`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ignore)

Use the time zone identifier to re-calculate the offset, ignoring the offset that's specified in the string. This option keeps the same local time as originally calculated when we stored the time, but may result in a different instant. Note that by ignoring the offset, the same [local time interpretation ambiguity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#ambiguity_and_gaps_from_local_time_to_utc_time)
 may arise, which is resolved using the `disambiguation` option. In the `2019-12-23T12:00:00-02:00[America/Sao_Paulo]` example above, this option would cause the reminder to fire at 12:00 PM local time.

[`reject`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#reject_2)

Throw a `RangeError` whenever there is a conflict between the offset and the time zone identifier. This is the default for [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
.

[`prefer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#prefer)

Use the offset if it's valid, otherwise calculate the offset from the time zone identifier. This is the default for [`Temporal.ZonedDateTime.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/with)
 (see that method for more details). This is different from `ignore` because in the case of local time ambiguity, the offset is used to resolve it rather than the `disambiguation` option.

If you know in advance how you want to handle offset ambiguity, consider using the `offset` option to avoid exceptions that are thrown by default. For example, a calendar application likely wants the time zone identifier to "win" so that recurring meetings are shown in the most up-to-date local time for that time zone, so `offset: "ignore"` is appropriate. On the other hand, a task scheduler application that executes a task exactly 3 hours from now should probably pick `offset: "use"` because changes to time zone rules shouldn't change the meaning of "3 hours from now".

In some cases, you may not know which `offset` option is the correct one without getting input from the user. In these cases, you may want to catch the `RangeError` and then ask your user which local time is the correct one, and then retry parsing using a different `offset` option corresponding to the user's choice.

Note that the `Z` offset is not equivalent to `+00:00`. The `Z` offset means "the time in UTC is known, but the offset to local time is unknown", as per [RFC 9557](https://www.rfc-editor.org/info/rfc9557/#name-update-to-rfc-3339 "External link (opens in new tab)")
. When the time string uses the `Z` offset, the `offset` option is ignored, and the offset is derived from the time zone ID. On the other hand, the `+00:00` offset is interpreted as a local time offset that happens to match UTC and is validated against the time zone ID.

**Note:** Although [`Temporal.Instant.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant/from)
 also takes an [RFC 9557](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)
 string in the same form, there is no ambiguity because it always ignores the time zone identifier and reads the offset only.

[Constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#constructor)

-----------------------------------------------------------------------------------------------------------------------------------

[`Temporal.ZonedDateTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/ZonedDateTime)

Creates a new `Temporal.ZonedDateTime` object by directly supplying the underlying data.

[Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#static_methods)

-----------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.ZonedDateTime.compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/compare)

Returns a number (-1, 0, or 1) indicating whether the first date-time comes before, is the same as, or comes after the second date-time. Equivalent to comparing the [`epochNanoseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/epochNanoseconds)
 of the two date-times.

[`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)

Creates a new `Temporal.ZonedDateTime` object from another `Temporal.ZonedDateTime` object, an object with date, time, and time zone properties, or an [RFC 9557](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)
 string.

[Instance properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#instance_properties)

---------------------------------------------------------------------------------------------------------------------------------------------------

These properties are defined on `Temporal.ZonedDateTime.prototype` and shared by all `Temporal.ZonedDateTime` instances.

[`Temporal.ZonedDateTime.prototype.calendarId`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/calendarId)

Returns a string representing the [calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
 used to interpret the internal ISO 8601 date.

[`Temporal.ZonedDateTime.prototype.constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

The constructor function that created the instance object. For `Temporal.ZonedDateTime` instances, the initial value is the [`Temporal.ZonedDateTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/ZonedDateTime)
 constructor.

[`Temporal.ZonedDateTime.prototype.day`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/day)

Returns a positive integer representing the 1-based day index in the month of this date, which is the same day number you would see on a calendar. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Generally starts at 1 and is continuous, but not always.

[`Temporal.ZonedDateTime.prototype.dayOfWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/dayOfWeek)

Returns a positive integer representing the 1-based day index in the week of this date. Days in a week are numbered sequentially from `1` to [`daysInWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/daysInWeek)
, with each number mapping to its name. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. 1 usually represents Monday in the calendar, even when locales using the calendar may consider a different day as the first day of the week (see [`Intl.Locale.prototype.getWeekInfo()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/getWeekInfo)
).

[`Temporal.ZonedDateTime.prototype.dayOfYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/dayOfYear)

Returns a positive integer representing the 1-based day index in the year of this date. The first day of this year is `1`, and the last day is the [`daysInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/daysInYear)
. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.ZonedDateTime.prototype.daysInMonth`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/daysInMonth)

Returns a positive integer representing the number of days in the month of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.ZonedDateTime.prototype.daysInWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/daysInWeek)

Returns a positive integer representing the number of days in the week of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For the ISO 8601 calendar, this is always 7, but in other calendar systems it may differ from week to week.

[`Temporal.ZonedDateTime.prototype.daysInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/daysInYear)

Returns a positive integer representing the number of days in the year of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For the ISO 8601 calendar, this is 365, or 366 in a leap year.

[`Temporal.ZonedDateTime.prototype.epochMilliseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/epochMilliseconds)

Returns an integer representing the number of milliseconds elapsed since the Unix epoch (midnight at the beginning of January 1, 1970, UTC) to this instant. Equivalent to dividing `epochNanoseconds` by `1e6` and flooring the result.

[`Temporal.ZonedDateTime.prototype.epochNanoseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/epochNanoseconds)

Returns a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 representing the number of nanoseconds elapsed since the Unix epoch (midnight at the beginning of January 1, 1970, UTC) to this instant.

[`Temporal.ZonedDateTime.prototype.era`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/era)

Returns a calendar-specific lowercase string representing the era of this date, or `undefined` if the calendar does not use eras (e.g., ISO 8601). `era` and `eraYear` together uniquely identify a year in a calendar, in the same way that `year` does. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For Gregorian, it is either `"ce"` or `"bce"`.

[`Temporal.ZonedDateTime.prototype.eraYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/eraYear)

Returns a non-negative integer representing the year of this date within the era, or `undefined` if the calendar does not use eras (e.g., ISO 8601). The year index usually starts from 1 (more common) or 0, and years in an era can decrease with time (e.g., Gregorian BCE). `era` and `eraYear` together uniquely identify a year in a calendar, in the same way that `year` does. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.ZonedDateTime.prototype.hour`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/hour)

Returns an integer from 0 to 23 representing the hour component of this time.

[`Temporal.ZonedDateTime.prototype.hoursInDay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/hoursInDay)

Returns a positive integer representing the number of hours in the day of this date in the time zone. It may be more or less than 24 in the case of offset changes such as daylight saving time.

[`Temporal.ZonedDateTime.prototype.inLeapYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/inLeapYear)

Returns a boolean indicating whether this date is in a leap year. A leap year is a year that has more days (due to a leap day or leap month) than a common year. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent.

[`Temporal.ZonedDateTime.prototype.microsecond`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/microsecond)

Returns an integer from 0 to 999 representing the microsecond (10\-6 second) component of this time.

[`Temporal.ZonedDateTime.prototype.millisecond`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/millisecond)

Returns an integer from 0 to 999 representing the millisecond (10\-3 second) component of this time.

[`Temporal.ZonedDateTime.prototype.minute`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/minute)

Returns an integer from 0 to 59 representing the minute component of this time.

[`Temporal.ZonedDateTime.prototype.month`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/month)

Returns a positive integer representing the 1-based month index in the year of this date. The first month of this year is `1`, and the last month is the [`monthsInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/monthsInYear)
. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Note that unlike [`Date.prototype.getMonth()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)
, the index is 1-based. If the calendar has leap months, then the month with the same [`monthCode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/monthCode)
 may have different `month` indexes for different years.

[`Temporal.ZonedDateTime.prototype.monthCode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/monthCode)

Returns a calendar-specific string representing the month of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Usually it is `M` plus a two-digit month number. For leap months, it is the previous month's code followed by `L`. If the leap month is the first month of the year, the code is `M00L`.

[`Temporal.ZonedDateTime.prototype.monthsInYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/monthsInYear)

Returns a positive integer representing the number of months in the year of this date. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. For the ISO 8601 calendar, this is always 12, but in other calendar systems it may differ.

[`Temporal.ZonedDateTime.prototype.nanosecond`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/nanosecond)

Returns an integer from 0 to 999 representing the nanosecond (10\-9 second) component of this time.

[`Temporal.ZonedDateTime.prototype.offset`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/offset)

Returns a string representing the [offset](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
 used to interpret the internal instant, in the form `±HH:mm` (or `±HH:mm:ss.sssssssss` with as much subminute precision as necessary).

[`Temporal.ZonedDateTime.prototype.offsetNanoseconds`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/offsetNanoseconds)

Returns an integer representing the [offset](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
 used to interpret the internal instant, as a number of nanoseconds (positive or negative).

[`Temporal.ZonedDateTime.prototype.second`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/second)

Returns an integer from 0 to 59 representing the second component of this time.

[`Temporal.ZonedDateTime.prototype.timeZoneId`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/timeZoneId)

Returns a string representing the [time zone identifier](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#time_zones_and_offsets)
 used to interpret the internal instant. It uses the same string used when constructing the `Temporal.ZonedDateTime` object, which is either an IANA time zone name or a fixed offset.

[`Temporal.ZonedDateTime.prototype.weekOfYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/weekOfYear)

Returns a positive integer representing the 1-based week index in the [`yearOfWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/yearOfWeek)
 of this date, or `undefined` if the calendar does not have a well-defined week system. The first week of the year is `1`. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Note that for ISO 8601, the first and last few days of the year may be attributed to the last week of the previous year or the first week of the next year.

[`Temporal.ZonedDateTime.prototype.year`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/year)

Returns an integer representing the number of years of this date relative to the start of a calendar-specific epoch year. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Usually year 1 is either the first year of the latest era or the ISO 8601 year `0001`. If the epoch is in the middle of the year, that year will have the same value before and after the start date of the era.

[`Temporal.ZonedDateTime.prototype.yearOfWeek`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/yearOfWeek)

Returns an integer representing the year to be paired with the [`weekOfYear`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/weekOfYear)
 of this date, or `undefined` if the calendar does not have a well-defined week system. [Calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal#calendars)
\-dependent. Usually this is the year of the date, but for ISO 8601, the first and last few days of the year may be attributed to the last week of the previous year or the first week of the next year, causing the `yearOfWeek` to differ by 1.

[`Temporal.ZonedDateTime.prototype[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#temporal.zoneddatetime.prototypesymbol.tostringtag)

The initial value of the [`[Symbol.toStringTag]`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/toStringTag)
 property is the string `"Temporal.ZonedDateTime"`. This property is used in [`Object.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
.

[Instance methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#instance_methods)

---------------------------------------------------------------------------------------------------------------------------------------------

[`Temporal.ZonedDateTime.prototype.add()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/add)

Returns a new `Temporal.ZonedDateTime` object representing this date-time moved forward by a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
).

[`Temporal.ZonedDateTime.prototype.equals()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/equals)

Returns `true` if this date-time is equivalent in value to another date-time (in a form convertible by [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
), and `false` otherwise. They are compared both by their instant values, time zones, and their calendars, so two date-times from different calendars or time zones may be considered equal by [`Temporal.ZonedDateTime.compare()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/compare)
 but not by `equals()`.

[`Temporal.ZonedDateTime.prototype.getTimeZoneTransition()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/getTimeZoneTransition)

Returns a `Temporal.ZonedDateTime` object representing the first instant after or before this instant at which the time zone's UTC offset changes, or `null` if there is no such transition. This is useful for finding out the offset rules of a time zone, such as its daylight saving time pattern.

[`Temporal.ZonedDateTime.prototype.round()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/round)

Returns a new `Temporal.ZonedDateTime` object representing this date-time rounded to the given unit.

[`Temporal.ZonedDateTime.prototype.since()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/since)

Returns a new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration from another date-time (in a form convertible by [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
) to this date-time. The duration is positive if the other date-time is before this date-time, and negative if after.

[`Temporal.ZonedDateTime.prototype.startOfDay()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/startOfDay)

Returns a `Temporal.ZonedDateTime` object representing the first instant of this date in the time zone. It usually has a time of `00:00:00`, but may be different if the midnight doesn't exist due to offset changes, in which case the first time that exists is returned.

[`Temporal.ZonedDateTime.prototype.subtract()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/subtract)

Returns a new `Temporal.ZonedDateTime` object representing this date-time moved backward by a given duration (in a form convertible by [`Temporal.Duration.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration/from)
).

[`Temporal.ZonedDateTime.prototype.toInstant()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toInstant)

Returns a new [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
 object representing the instant of this date-time.

[`Temporal.ZonedDateTime.prototype.toJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toJSON)

Returns a string representing this date-time in the same [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)
 as calling [`toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toString)
. Intended to be implicitly called by [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
.

[`Temporal.ZonedDateTime.prototype.toLocaleString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toLocaleString)

Returns a string with a language-sensitive representation of this date-time.

[`Temporal.ZonedDateTime.prototype.toPlainDate()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toPlainDate)

Returns a new [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
 object representing the date portion of this date-time.

[`Temporal.ZonedDateTime.prototype.toPlainDateTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toPlainDateTime)

Returns a new [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
 object representing the date and time portions of this date-time. Only the time zone information is removed.

[`Temporal.ZonedDateTime.prototype.toPlainTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toPlainTime)

Returns a new [`Temporal.PlainTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime)
 object representing the time portion of this date-time.

[`Temporal.ZonedDateTime.prototype.toString()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/toString)

Returns a string representing this date-time in the [RFC 9557 format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#rfc_9557_format)
.

[`Temporal.ZonedDateTime.prototype.until()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/until)

Returns a new [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
 object representing the duration from this date-time to another date-time (in a form convertible by [`Temporal.ZonedDateTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/from)
). The duration is positive if the other date-time is after this date-time, and negative if before.

[`Temporal.ZonedDateTime.prototype.valueOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/valueOf)

Throws a [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
, which prevents `Temporal.ZonedDateTime` instances from being [implicitly converted to primitives](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures#primitive_coercion)
 when used in arithmetic or comparison operations.

[`Temporal.ZonedDateTime.prototype.with()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/with)

Returns a new `Temporal.ZonedDateTime` object representing this date-time with some fields replaced by new values.

[`Temporal.ZonedDateTime.prototype.withCalendar()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/withCalendar)

Returns a new `Temporal.ZonedDateTime` object representing this date-time interpreted in the new calendar system.

[`Temporal.ZonedDateTime.prototype.withPlainTime()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/withPlainTime)

Returns a new `Temporal.ZonedDateTime` object representing this date-time with the time part entirely replaced by the new time (in a form convertible by [`Temporal.PlainTime.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime/from)
)

[`Temporal.ZonedDateTime.prototype.withTimeZone()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/withTimeZone)

Returns a new `Temporal.ZonedDateTime` object representing the same instant as this date-time but in the new time zone.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Temporal  <br>\# sec-temporal-zoneddatetime-objects](https://tc39.es/proposal-temporal/#sec-temporal-zoneddatetime-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`Temporal`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal)
    
*   [`Temporal.Duration`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Duration)
    
*   [`Temporal.Instant`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/Instant)
    
*   [`Temporal.PlainDateTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDateTime)
    
*   [`Temporal.PlainDate`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainDate)
    
*   [`Temporal.PlainTime`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/PlainTime)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal/ZonedDateTime/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/temporal/zoneddatetime/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/temporal/zoneddatetime (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FZonedDateTime&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fzoneddatetime%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTemporal%2FZonedDateTime%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Ftemporal%2Fzoneddatetime%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F76c2e04d720aa8260ba7d75788ed96776aac35c6%0A*+Document+last+modified%3A+2026-09-18T02%3A05%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
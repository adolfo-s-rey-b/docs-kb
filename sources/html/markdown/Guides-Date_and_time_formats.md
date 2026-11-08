*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#mdn-search)
    

Using date and time formats in HTML
===================================

Certain HTML elements use date and/or time values. The formats of the strings that specify these values are described in this article.

Elements that use such formats include certain forms of the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element that let the user choose or specify a date, time, or both, as well as the [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
 and [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
 elements, whose [`datetime`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins#datetime)
 attribute specifies the date or date and time at which the insertion or deletion of content occurred.

For `<input>`, the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 values of inputs whose [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 contains a string representing a date and/or time are:

*   [`date`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
    
*   [`datetime-local`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
    
*   [`month`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
    
*   [`time`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
    
*   [`week`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#examples)

----------------------------------------------------------------------------------------------------

Before getting into the intricacies of how date and time strings are written and parsed in HTML, here are some examples that should give you a good idea what the more commonly-used date and time string formats look like.

|     |     |     |
| --- | --- | --- |Example HTML date and time strings
| String | Date and/or time |     |
| --- | --- | --- |
| `2005-06-07` | June 7, 2005 | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_strings) |
| `08:45` | 8:45 AM | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#time_strings) |
| `08:45:25` | 8:45 AM and 25 seconds | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#time_strings) |
| `0033-08-04T03:40` | 3:40 AM on August 4, 33 | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings) |
| `1977-04-01T14:00:30` | 30 seconds after 2:00 PM on April 1, 1977 | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings) |
| `1901-01-01T00:00Z` | Midnight UTC on January 1, 1901 | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#global_date_and_time_strings) |
| `1901-01-01T00:00:01-04:00` | 1 second past midnight Eastern Standard Time (EST) on January 1, 1901 | [\[details\]](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#global_date_and_time_strings) |

[Basics](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#basics)

------------------------------------------------------------------------------------------------

Before looking at the various formats of date and time related strings used by HTML elements, it is helpful to understand a few fundamental facts about the way they're defined. HTML uses a variation of the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601 "External link (opens in new tab)")
 standard for its date and time strings. It's worth reviewing the descriptions of the formats you're using in order to ensure that your strings are in fact compatible with HTML, as the HTML specification includes algorithms for parsing these strings that is actually more precise than ISO 8601, so there can be subtle differences in how date and time strings are expected to look.

### [Character set](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#character_set)

Dates and times in HTML are always strings which use the [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 character set.

### [Year numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#year_numbers)

In order to simplify the basic format used for date strings in HTML, the specification requires that all years be given using the modern (or **proleptic**) [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar "External link (opens in new tab)")
. While user interfaces may allow entry of dates using other calendars, the underlying value always uses the Gregorian calendar.

While the Gregorian calendar wasn't created until the year 1582 (replacing the similar Julian calendar), for HTML's purposes, the Gregorian calendar is extended back to the year 1 C.E. Make sure any older dates account for this.

For the purposes of HTML dates, years are always at least four digits long; years prior to the year 1000 are padded with leading zeroes (`0`), so the year 72 is written as `0072`. Years prior to the year 1 C.E. are not supported, so HTML doesn't support years 1 B.C.E. (1 B.C.) or earlier.

A year is normally 365 days long, except during **[leap years](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#leap_years)
**.

#### Leap years

A **leap year** is any year which is divisible by 400 _or_ the year is divisible by 4 but not by 100. Although the calendar year is normally 365 days long, it actually takes the planet Earth approximately 365.2422 days to complete a single orbit around the sun. Leap years help to adjust the calendar to keep it synchronized with the actual position of the planet in its orbit. Adding a day to the year every four years essentially makes the average year 365.25 days long, which is close to correct.

The adjustments to the algorithm (taking a leap year when the year can be divided by 400, and skipping leap years when the year is divisible by 100) help to bring the average even closer to the correct number of days (365.2425 days). Scientists occasionally add leap seconds to the calendar (seriously) to handle the remaining three ten-thousandths of a day and to compensate for the gradual, naturally occurring slowing of Earth's rotation.

While month `02`, February, normally has 28 days, it has 29 days in leap years.

### [Months of the year](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#months_of_the_year)

There are 12 months in the year, numbered 1 through 12. They are always represented by a two-digit ASCII string whose value ranges from `01` through `12`. See the table in the section [Days of the month](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#days_of_the_month)
 for the month numbers and their corresponding names (and lengths in days).

### [Days of the month](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#days_of_the_month)

Month numbers 1, 3, 5, 7, 8, 10, and 12 are 31 days long. Months 4, 6, 9, and 11 are 30 days long. Month 2, February, is 28 days long most years, but is 29 days long in leap years. This is detailed in the following table.

|     |     |     |
| --- | --- | --- |The months of the year and their lengths in days
| Month number | Name (English) | Length in days |
| --- | --- | --- |
| 01  | January | 31  |
| 02  | February | 28 (29 in leap years) |
| 03  | March | 31  |
| 04  | April | 30  |
| 05  | May | 31  |
| 06  | June | 30  |
| 07  | July | 31  |
| 08  | August | 31  |
| 09  | September | 30  |
| 10  | October | 31  |
| 11  | November | 30  |
| 12  | December | 31  |

[Week strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#week_strings)

------------------------------------------------------------------------------------------------------------

A week string specifies a week within a particular year. A **valid week string** consists of a valid [year number](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#year_numbers)
, followed by a hyphen character (`-`, or U+002D), then the capital letter `W` (U+0057), followed by a two-digit week of the year value.

The week of the year is a two-digit string between `01` and `53`. Each week begins on Monday and ends on Sunday. That means it's possible for the first few days of January to be considered part of the previous week-year, and for the last few days of December to be considered part of the following week-year. The first week of the year is the week that contains the _first Thursday of the year_. For example, the first Thursday of 1953 was on January 1, so that week—beginning on Monday, December 29—is considered the first week of the year. Therefore, December 30, 1952 occurs during the week `1953-W01`.

A year has 53 weeks if:

*   The first day of the calendar year (January 1) is a Thursday **or**
*   The first day of the year (January 1) is a Wednesday and the year is a [leap year](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#leap_years)
    

All other years have 52 weeks.

| Week string | Week and year (Date range) |
| --- | --- |
| `2001-W37` | Week 37, 2001 (September 10-16, 2001) |
| `1953-W01` | Week 1, 1953 (December 29, 1952-January 4, 1953) |
| `1948-W53` | Week 53, 1948 (December 27, 1948-January 2, 1949) |
| `1949-W01` | Week 1, 1949 (January 3-9, 1949) |
| `0531-W16` | Week 16, 531 (April 13-19, 531) |
| `0042-W04` | Week 4, 42 (January 21-27, 42) |

Note that both the year and week numbers are padded with leading zeroes, with the year padded to four digits and the week to two.

[Month strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#month_strings)

--------------------------------------------------------------------------------------------------------------

A month string represents a specific month in time, rather than a generic month of the year. That is, rather than representing "January," an HTML month string represents a month and year paired, like "January 1972."

A **valid month string** consists of a valid [year number](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#year_numbers)
 (a string of at least four digits), followed by a hyphen character (`-`, or U+002D), followed by a two-digit numeric [month number](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#months_of_the_year)
, where `01` represents January and `12` represents December.

| Month string | Month and year |
| --- | --- |
| `17310-09` | September, 17310 |
| `2019-01` | January, 2019 |
| `1993-11` | November, 1993 |
| `0571-04` | April, 571 |
| `0001-07` | July, 1 C.E. |

Notice that all years are at least four characters long; years that are fewer than four digits long are padded with leading zeroes.

[Date strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_strings)

------------------------------------------------------------------------------------------------------------

A valid date string consists of a [month string](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#month_strings)
, followed by a hyphen character (`-`, or U+002D), followed by a two-digit [day of the month](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#days_of_the_month)
.

| Date string | Full date |
| --- | --- |
| `1993-11-01` | November 1, 1993 |
| `1066-10-14` | October 14, 1066 |
| `0571-04-22` | April 22, 571 |
| `0062-02-05` | February 5, 62 |

[Time strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#time_strings)

------------------------------------------------------------------------------------------------------------

A time string can specify a time with precision to the minute, second, or to the millisecond. Specifying only the hour or minute isn't permitted. A **valid time string** minimally consists of a two-digit hour followed by a colon (`:`, U+003A), then a two-digit minute. The minute may optionally be followed by another colon and a two-digit number of seconds. Milliseconds may be specified, optionally, by adding a decimal point character (`.`, U+002E) followed by one, two, or three digits.

There are some additional basic rules:

*   The hour is always specified using the 24-hour clock, with `00` being midnight and 11 PM being `23`. No values outside the range `00` – `23` are permitted.
*   The minute must be a two-digit number between `00` and `59`. No values outside that range are allowed.
*   If the number of seconds is omitted (to specify a time accurate only to the minute), no colon should follow the number of minutes.
*   If specified, the integer portion of the number of seconds must be between `00` and `59`. You _cannot_ specify leap seconds by using values like `60` or `61`.
*   If the number of seconds is specified and is an integer, it must not be followed by a decimal point.
*   If a fraction of a second is included, it may be from one to three digits long, indicating the number of milliseconds. It follows the decimal point placed after the seconds component of the time string.

| Time string | Time |
| --- | --- |
| `00:00:30.75` | 12:00:30.75 AM (30.75 seconds after midnight) |
| `12:15` | 12:15 PM |
| `13:44:25` | 1:44:25 PM (25 seconds after 1:44 PM) |

[Local date and time strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings)

------------------------------------------------------------------------------------------------------------------------------------------

A valid [`datetime-local`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
 string consists of a `date` string and a `time` string concatenated together with either the letter `T` or a space character separating them. No information about the time zone is included in the string; the date and time is presumed to be in the user's local time zone.

When you set the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of a `datetime-local` input, the string is **normalized** into a standard form. Normalized `datetime` strings always use the letter `T` to separate the date and the time, and the time portion of the string is as short as possible. This is done by leaving out the seconds component if its value is `:00`.

|     |     |     |
| --- | --- | --- |Examples of valid `datetime-local` strings
| Date/time string | Normalized date/time string | Actual date and time |
| --- | --- | --- |
| `1986-01-28T11:38:00.01` | `1986-01-28T11:38:00.01` | January 28, 1986 at 11:38:00.01 AM |
| `1986-01-28 11:38:00.010` | `1986-01-28T11:38:00.01`<br><br>Note that after normalization, this is the same string as the previous `datetime-local` string. The space has been replaced with the `T` character and the trailing zero in the fraction of a second has been removed to make the string as short as possible. | January 28, 1986 at 11:38:00.01 AM |
| `0170-07-31T22:00:00` | `0170-07-31T22:00`<br><br>Note that the normalized form of this date drops the `:00` indicating the number of seconds to be zero, because the seconds are optional when zero, and the normalized string minimizes the length of the string. | July 31, 170 at 10:00 PM |

[Global date and time strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#global_date_and_time_strings)

--------------------------------------------------------------------------------------------------------------------------------------------

A global date and time string specifies a date and time as well as the time zone in which it occurs. A **valid global date and time string** is the same format as a [local date and time string](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings)
, except it has a time zone string appended to the end, following the time.

### [Time zone offset string](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#time_zone_offset_string)

A time zone offset string specifies the offset in either a positive or a negative number of hours and minutes from the standard time base. There are two standard time bases, which are very close to the same, but not exactly the same:

*   For dates after the establishment of [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time "External link (opens in new tab)")
     (UTC) in the early 1960s, the time base is `Z` and the offset indicates a particular time zone's offset from the time at the prime meridian at 0º longitude (which passes through the Royal Observatory at Greenwich, England).
*   For dates prior to UTC, the time base is instead expressed in terms of [UT1](https://en.wikipedia.org/wiki/UT1 "External link (opens in new tab)")
    , which is the contemporary Earth solar time at the prime meridian.

The time zone string is appended immediately following the time in the date and time string. You can specify `Z` as the time zone offset string to indicate that the time is specified in UTC. Otherwise, the time zone string is constructed as follows:

1.  A character indicating the sign of the offset: the plus character (`+`, or U+002B) for time zones to the east of the prime meridian or the minus character (`-`, or U+002D) for time zones to the west of the prime meridian.
2.  A two-digit number of hours that the time zone is offset from the prime meridian. This value must be between `00` and `23`.
3.  An optional colon (`:`) character.
4.  A two-digit number of minutes past the hour; this value must be between `00` and `59`.

While this format allows for time zones between -23:59 and +23:59, the current range of time zone offsets is -12:00 to +14:00, and no time zones are currently offset from the hour by anything other than `00`, `30`, or `45` minutes. This may change at more or less anytime, since countries are free to tamper with their time zones at any time and in any way they wish to do so.

|     |     |     |
| --- | --- | --- |Examples of valid global date and time strings
| Global date and time string | Actual global date and time | Date and time at prime meridian |
| --- | --- | --- |
| `2005-06-07T00:00Z` | June 7, 2005 at midnight UTC | June 7, 2005 at midnight |
| `1789-08-22T12:30:00.1-04:00` | August 22, 1789 at a tenth of a second past 12:30 PM Eastern Daylight Time (EDT) | August 22, 1789 at a tenth of a second past 4:30 PM |
| `3755-01-01 00:00+10:00` | January 1, 3755 at midnight Australian Eastern Standard Time (AEST) | December 31, 3754 at 2:00 PM |

[Date issues](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_issues)

----------------------------------------------------------------------------------------------------------

Because of data storage and precision issues, you may want to be aware of a few client-side and server-side issues.

### [The Y2K38 Problem (often server-side)](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#the_y2k38_problem_often_server-side)

JavaScript uses double precision floating points to store dates, as with all numbers, meaning that JavaScript code will not suffer from the Y2K38 problem unless integer coercion/bit-hacks are used because all JavaScript bit operators use 32-bit signed 2s-complement integers.

The problem is with the server side of things: storage of dates greater than 2^31 - 1. To fix this problem, you must store all dates using either unsigned 32-bit integers, signed 64-bit integers, or double-precision floating points on the server. If your server is written in PHP, the fix may require upgrading your PHP to a more recent version, and upgrading your hardware to x86\_64 or IA64. If you are stuck with other hardware, you can try to emulate 64-bit hardware inside a 32-bit virtual machine, but most VMs don't support this kind of virtualization, since stability may suffer, and performance will definitely suffer greatly.

### [The Y10k Problem (often client-side)](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#the_y10k_problem_often_client-side)

In many servers, dates are stored as numbers instead of as strings--numbers of a fixed size and agnostic of format (aside from endianness). After the year 10,000, those numbers will just be a bit bigger than before, so many servers will not see issues with forms submitted after the year 10,000.

The problem is with the client side of things: parsing of dates with more than 4 digits in the year.

We need to prepare our code for any number of digits — not just 5. The following JavaScript function programmatically sets the value:

Why worry about the Y10K problem if it is going to happen many centuries after your death? Exactly because you will already be dead, so the companies using your software will be stuck using your software without any other coder who knows the system well enough to come in and fix it.

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#see_also)

----------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)
     and [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)
    : see the `datetime` attribute, which specifies either a date or a local date and time at which the content was inserted or deleted
*   [The ISO 8601 specification](https://www.iso.org/iso-8601-date-and-time-format.html "External link (opens in new tab)")
    
*   [Representing dates & times](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Representing_dates_times)
     in the [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
    
*   The JavaScript [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
     object
*   The [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)
     object for formatting dates and times for a given locale

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 9, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/date_and_time_formats/index.md?plain=1 "Folder: en-us/web/html/guides/date_and_time_formats (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FDate_and_time_formats&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fdate_and_time_formats%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FDate_and_time_formats%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fdate_and_time_formats%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0754cd805a8e010d2e3a2a065f634a3bcf358252%0A*+Document+last+modified%3A+2025-07-09T21%3A49%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")
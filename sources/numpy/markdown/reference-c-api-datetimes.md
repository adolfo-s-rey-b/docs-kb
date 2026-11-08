[Skip to main content](https://numpy.org/doc/stable/reference/c-api/datetimes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/datetimes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/datetimes.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/datetimes.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/datetimes.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/datetimes.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/datetimes.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/datetimes.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/datetimes.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/datetimes.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/datetimes.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/datetimes.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/datetimes.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/datetimes.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/datetimes.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/datetimes.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/datetimes.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/datetimes.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/datetimes.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/datetimes.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/datetimes.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/datetimes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Datetime API[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#datetime-api "Link to this heading")

=================================================================================================================

NumPy represents dates internally using an int64 counter and a unit metadata struct. Time differences are represented similarly using an int64 and a unit metadata struct. The functions described below are available to to facilitate converting between ISO 8601 date strings, NumPy datetimes, and Python datetime objects in C.

Data types[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#data-types "Link to this heading")

-------------------------------------------------------------------------------------------------------------

In addition to the [`npy_datetime`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_datetime "npy_datetime")
 and [`npy_timedelta`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_timedelta "npy_timedelta")
 typedefs for [`npy_int64`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
, NumPy defines two additional structs that represent time unit metadata and an “exploded” view of a datetime.

type PyArray\_DatetimeMetaData[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.PyArray_DatetimeMetaData "Link to this definition")
  

Represents datetime unit metadata.

typedef struct {
    NPY\_DATETIMEUNIT base;
    int num;
} PyArray\_DatetimeMetaData;

Copy to clipboard

[NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 base[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.PyArray_DatetimeMetaData.base "Link to this definition")
  

The unit of the datetime.

int num[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.PyArray_DatetimeMetaData.num "Link to this definition")
  

A multiplier for the unit.

type npy\_datetimestruct[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "Link to this definition")
  

An “exploded” view of a datetime value

typedef struct {
    npy\_int64 year;
    npy\_int32 month, day, hour, min, sec, us, ps, as;
} npy\_datetimestruct;

Copy to clipboard

enum NPY\_DATETIMEUNIT[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "Link to this definition")
  

Time units supported by NumPy. The “FR” in the names of the enum variants is short for frequency.

enumerator NPY\_FR\_ERROR[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_ERROR "Link to this definition")
  

Error or undetermined units.

enumerator NPY\_FR\_Y[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_Y "Link to this definition")
  

Years

enumerator NPY\_FR\_M[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_M "Link to this definition")
  

Months

enumerator NPY\_FR\_W[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_W "Link to this definition")
  

Weeks

enumerator NPY\_FR\_D[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_D "Link to this definition")
  

Days

enumerator NPY\_FR\_h[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_h "Link to this definition")
  

Hours

enumerator NPY\_FR\_m[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_m "Link to this definition")
  

Minutes

enumerator NPY\_FR\_s[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_s "Link to this definition")
  

Seconds

enumerator NPY\_FR\_ms[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_ms "Link to this definition")
  

Milliseconds

enumerator NPY\_FR\_us[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_us "Link to this definition")
  

Microseconds

enumerator NPY\_FR\_ns[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_ns "Link to this definition")
  

Nanoseconds

enumerator NPY\_FR\_ps[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_ps "Link to this definition")
  

Picoseconds

enumerator NPY\_FR\_fs[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_fs "Link to this definition")
  

Femtoseconds

enumerator NPY\_FR\_as[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_as "Link to this definition")
  

Attoseconds

enumerator NPY\_FR\_GENERIC[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT.NPY_FR_GENERIC "Link to this definition")
  

Unbound units, can convert to anything

Conversion functions[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#conversion-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

int NpyDatetime\_ConvertDatetimeStructToDatetime64([PyArray\_DatetimeMetaData](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.PyArray_DatetimeMetaData "PyArray_DatetimeMetaData")
 \*meta, const [npy\_datetimestruct](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "npy_datetimestruct")
 \*dts, [npy\_datetime](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_datetime "npy_datetime")
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_ConvertDatetimeStructToDatetime64 "Link to this definition")
  

Converts a datetime from a datetimestruct to a datetime in the units specified by the unit metadata. The date is assumed to be valid.

If the `num` member of the metadata struct is large, there may be integer overflow in this function.

Returns 0 on success and -1 on failure.

int NpyDatetime\_ConvertDatetime64ToDatetimeStruct([PyArray\_DatetimeMetaData](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.PyArray_DatetimeMetaData "PyArray_DatetimeMetaData")
 \*meta, [npy\_datetime](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_datetime "npy_datetime")
 dt, [npy\_datetimestruct](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "npy_datetimestruct")
 \*out)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_ConvertDatetime64ToDatetimeStruct "Link to this definition")
  

Converts a datetime with units specified by the unit metadata to an exploded datetime struct.

Returns 0 on success and -1 on failure.

int NpyDatetime\_ConvertPyDateTimeToDatetimeStruct([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*obj, [npy\_datetimestruct](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "npy_datetimestruct")
 \*out, [NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 \*out\_bestunit, int apply\_tzinfo)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_ConvertPyDateTimeToDatetimeStruct "Link to this definition")
  

Tests for and converts a Python `datetime.datetime` or `datetime.date` object into a NumPy `npy_datetimestruct`.

`out_bestunit` gives a suggested unit based on whether the object was a `datetime.date` or `datetime.datetime` object.

If `apply_tzinfo` is 1, this function uses the tzinfo to convert to UTC time, otherwise it returns the struct with the local time.

Returns -1 on error, 0 on success, and 1 (with no error set) if obj doesn’t have the needed date or datetime attributes.

int NpyDatetime\_ParseISO8601Datetime(char const \*str, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "(in Python v3.14)")
 len, [NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 unit, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 casting, [npy\_datetimestruct](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "npy_datetimestruct")
 \*out, [NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 \*out\_bestunit, [npy\_bool](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_bool "npy_bool")
 \*out\_special)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_ParseISO8601Datetime "Link to this definition")
  

Parses (almost) standard ISO 8601 date strings. The differences are:

*   The date “20100312” is parsed as the year 20100312, not as equivalent to “2010-03-12”. The ‘-’ in the dates are not optional.
    
*   Only seconds may have a decimal point, with up to 18 digits after it (maximum attoseconds precision).
    
*   Either a ‘T’ as in ISO 8601 or a ‘ ‘ may be used to separate the date and the time. Both are treated equivalently.
    
*   Doesn’t (yet) handle the “YYYY-DDD” or “YYYY-Www” formats.
    
*   Doesn’t handle leap seconds (seconds value has 60 in these cases).
    
*   Doesn’t handle 24:00:00 as synonym for midnight (00:00:00) tomorrow
    
*   Accepts special values “NaT” (not a time), “Today”, (current day according to local time) and “Now” (current time in UTC).
    

`str` must be a NULL-terminated string, and `len` must be its length.

`unit` should contain -1 if the unit is unknown, or the unit which will be used if it is.

`casting` controls how the detected unit from the string is allowed to be cast to the ‘unit’ parameter.

`out` gets filled with the parsed date-time.

`out_bestunit` gives a suggested unit based on the amount of resolution provided in the string, or -1 for NaT.

`out_special` gets set to 1 if the parsed time was ‘today’, ‘now’, empty string, or ‘NaT’. For ‘today’, the unit recommended is ‘D’, for ‘now’, the unit recommended is ‘s’, and for ‘NaT’ the unit recommended is ‘Y’.

Returns 0 on success, -1 on failure.

int NpyDatetime\_GetDatetimeISO8601StrLen(int local, [NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 base)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_GetDatetimeISO8601StrLen "Link to this definition")
  

Returns the string length to use for converting datetime objects with the given local time and unit settings to strings. Use this when constructing strings to supply to `NpyDatetime_MakeISO8601Datetime`.

int NpyDatetime\_MakeISO8601Datetime([npy\_datetimestruct](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.npy_datetimestruct "npy_datetimestruct")
 \*dts, char \*outstr, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 outlen, int local, int utc, [NPY\_DATETIMEUNIT](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NPY_DATETIMEUNIT "NPY_DATETIMEUNIT")
 base, int tzoffset, [NPY\_CASTING](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_CASTING "NPY_CASTING")
 casting)[#](https://numpy.org/doc/stable/reference/c-api/datetimes.html#c.NpyDatetime_MakeISO8601Datetime "Link to this definition")
  

Converts an `npy_datetimestruct` to an (almost) ISO 8601 NULL-terminated string. If the string fits in the space exactly, it leaves out the NULL terminator and returns success.

The differences from ISO 8601 are the ‘NaT’ string, and the number of year digits is >= 4 instead of strictly 4.

If `local` is non-zero, it produces a string in local time with a +-#### timezone offset. If `local` is zero and `utc` is non-zero, produce a string ending with ‘Z’ to denote UTC. By default, no time zone information is attached.

`base` restricts the output to that unit. Set `base` to -1 to auto-detect a base after which all the values are zero.

`tzoffset` is used if `local` is enabled, and `tzoffset` is set to a value other than -1. This is a manual override for the local time zone to use, as an offset in minutes.

`casting` controls whether data loss is allowed by truncating the data to a coarser unit. This interacts with `local`, slightly, in order to form a date unit string as a local time, the casting must be unsafe.

Returns 0 on success, -1 on failure (for example if the output string was too short).

On this page
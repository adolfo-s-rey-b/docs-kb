### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/interp-lifecycle.html "Interpreter initialization and finalization")
     |
*   [previous](https://docs.python.org/3/c-api/curses.html "Curses C API")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [DateTime Objects](https://docs.python.org/3/c-api/datetime.html)
    
*    
    
    |
*   Theme Auto Light Dark |

DateTime Objects[¶](https://docs.python.org/3/c-api/datetime.html#datetime-objects "Link to this heading")

===========================================================================================================

Various date and time objects are supplied by the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
 module. Before using any of these functions, the header file `datetime.h` must be included in your source (note that this is not included by `Python.h`), and the macro [`PyDateTime_IMPORT`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "PyDateTime_IMPORT")
 must be invoked, usually as part of the module initialisation function. The macro puts a pointer to a C structure into a static variable, [`PyDateTimeAPI`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTimeAPI "PyDateTimeAPI")
, that is used by the following macros.

PyDateTime\_IMPORT[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "Link to this definition")
  

Import the datetime C API.

On success, populate the [`PyDateTimeAPI`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTimeAPI "PyDateTimeAPI")
 pointer. On failure, set `PyDateTimeAPI` to `NULL` and set an exception. The caller must check if an error occurred via [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
:

PyDateTime\_IMPORT;
if (PyErr\_Occurred()) { /\* cleanup \*/ }

Warning

This is not compatible with subinterpreters.

Changed in version 3.15: This macro is now thread safe.

type PyDateTime\_CAPI[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_CAPI "Link to this definition")
  

Structure containing the fields for the datetime C API.

The fields of this structure are private and subject to change.

Do not use this directly; prefer `PyDateTime_*` APIs instead.

[PyDateTime\_CAPI](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_CAPI "PyDateTime_CAPI")
 \*PyDateTimeAPI[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTimeAPI "Link to this definition")
  

Dynamically allocated object containing the datetime C API.

This variable is only available once [`PyDateTime_IMPORT`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "PyDateTime_IMPORT")
 succeeds.

Changed in version 3.15: This variable should not be accessed directly as direct access is not thread-safe. Use [`PyDateTime_IMPORT`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "PyDateTime_IMPORT")
 instead.

type PyDateTime\_Date[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Date "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python date object.

type PyDateTime\_DateTime[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python datetime object.

type PyDateTime\_Time[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python time object.

type PyDateTime\_Delta[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Delta "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents the difference between two datetime values.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDateTime\_DateType[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateType "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python date type; it is the same object as [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDateTime\_DateTimeType[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTimeType "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python datetime type; it is the same object as [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDateTime\_TimeType[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TimeType "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python time type; it is the same object as [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDateTime\_DeltaType[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DeltaType "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python type for the difference between two datetime values; it is the same object as [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
 in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDateTime\_TZInfoType[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TZInfoType "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python time zone info type; it is the same object as [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo")
 in the Python layer.

Macro for access to the UTC singleton:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_TimeZone\_UTC[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TimeZone_UTC "Link to this definition")
  

Returns the time zone singleton representing UTC, the same object as [`datetime.timezone.utc`](https://docs.python.org/3/library/datetime.html#datetime.timezone.utc "datetime.timezone.utc")
.

Added in version 3.7.

Type-check macros:

int PyDate\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDate_Check "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DateType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateType "PyDateTime_DateType")
 or a subtype of `PyDateTime_DateType`. _ob_ must not be `NULL`. This function always succeeds.

int PyDate\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDate_CheckExact "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DateType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateType "PyDateTime_DateType")
. _ob_ must not be `NULL`. This function always succeeds.

int PyDateTime\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Check "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DateTimeType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTimeType "PyDateTime_DateTimeType")
 or a subtype of `PyDateTime_DateTimeType`. _ob_ must not be `NULL`. This function always succeeds.

int PyDateTime\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_CheckExact "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DateTimeType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTimeType "PyDateTime_DateTimeType")
. _ob_ must not be `NULL`. This function always succeeds.

int PyTime\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTime_Check "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_TimeType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TimeType "PyDateTime_TimeType")
 or a subtype of `PyDateTime_TimeType`. _ob_ must not be `NULL`. This function always succeeds.

int PyTime\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTime_CheckExact "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_TimeType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TimeType "PyDateTime_TimeType")
. _ob_ must not be `NULL`. This function always succeeds.

int PyDelta\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDelta_Check "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DeltaType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DeltaType "PyDateTime_DeltaType")
 or a subtype of `PyDateTime_DeltaType`. _ob_ must not be `NULL`. This function always succeeds.

int PyDelta\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDelta_CheckExact "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_DeltaType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DeltaType "PyDateTime_DeltaType")
. _ob_ must not be `NULL`. This function always succeeds.

int PyTZInfo\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTZInfo_Check "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_TZInfoType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TZInfoType "PyDateTime_TZInfoType")
 or a subtype of `PyDateTime_TZInfoType`. _ob_ must not be `NULL`. This function always succeeds.

int PyTZInfo\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTZInfo_CheckExact "Link to this definition")
  

Return true if _ob_ is of type [`PyDateTime_TZInfoType`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TZInfoType "PyDateTime_TZInfoType")
. _ob_ must not be `NULL`. This function always succeeds.

Macros to create objects:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDate\_FromDate(int year, int month, int day)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDate_FromDate "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 object with the specified year, month and day.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_FromDateAndTime "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 object with the specified year, month, day, hour, minute, second and microsecond.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_FromDateAndTimeAndFold "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 object with the specified year, month, day, hour, minute, second, microsecond and fold.

Added in version 3.6.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTime\_FromTime(int hour, int minute, int second, int usecond)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTime_FromTime "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
 object with the specified hour, minute, second and microsecond.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTime\_FromTimeAndFold(int hour, int minute, int second, int usecond, int fold)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTime_FromTimeAndFold "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
 object with the specified hour, minute, second, microsecond and fold.

Added in version 3.6.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDelta\_FromDSU(int days, int seconds, int useconds)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDelta_FromDSU "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
 object representing the given number of days, seconds and microseconds. Normalization is performed so that the resulting number of microseconds and seconds lie in the ranges documented for `datetime.timedelta` objects.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTimeZone\_FromOffset([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*offset)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTimeZone_FromOffset "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
 object with an unnamed fixed offset represented by the _offset_ argument.

Added in version 3.7.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyTimeZone\_FromOffsetAndName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyTimeZone_FromOffsetAndName "Link to this definition")
  

_Return value: New reference._

Return a [`datetime.timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
 object with a fixed offset represented by the _offset_ argument and with tzname _name_.

Added in version 3.7.

Macros to extract fields from date objects. The argument must be an instance of [`PyDateTime_Date`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Date "PyDateTime_Date")
, including subclasses (such as [`PyDateTime_DateTime`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
). The argument must not be `NULL`, and the type is not checked:

int PyDateTime\_GET\_YEAR([PyDateTime\_Date](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Date "PyDateTime_Date")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_GET_YEAR "Link to this definition")
  

Return the year, as a positive int.

int PyDateTime\_GET\_MONTH([PyDateTime\_Date](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Date "PyDateTime_Date")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_GET_MONTH "Link to this definition")
  

Return the month, as an int from 1 through 12.

int PyDateTime\_GET\_DAY([PyDateTime\_Date](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Date "PyDateTime_Date")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_GET_DAY "Link to this definition")
  

Return the day, as an int from 1 through 31.

Macros to extract fields from datetime objects. The argument must be an instance of [`PyDateTime_DateTime`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
, including subclasses. The argument must not be `NULL`, and the type is not checked:

int PyDateTime\_DATE\_GET\_HOUR([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_HOUR "Link to this definition")
  

Return the hour, as an int from 0 through 23.

int PyDateTime\_DATE\_GET\_MINUTE([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_MINUTE "Link to this definition")
  

Return the minute, as an int from 0 through 59.

int PyDateTime\_DATE\_GET\_SECOND([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_SECOND "Link to this definition")
  

Return the second, as an int from 0 through 59.

int PyDateTime\_DATE\_GET\_MICROSECOND([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_MICROSECOND "Link to this definition")
  

Return the microsecond, as an int from 0 through 999999.

int PyDateTime\_DATE\_GET\_FOLD([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_FOLD "Link to this definition")
  

Return the fold, as an int from 0 through 1.

Added in version 3.6.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_DATE\_GET\_TZINFO([PyDateTime\_DateTime](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DateTime "PyDateTime_DateTime")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_TZINFO "Link to this definition")
  

Return the tzinfo (which may be `None`).

Added in version 3.10.

Macros to extract fields from time objects. The argument must be an instance of [`PyDateTime_Time`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
, including subclasses. The argument must not be `NULL`, and the type is not checked:

int PyDateTime\_TIME\_GET\_HOUR([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_HOUR "Link to this definition")
  

Return the hour, as an int from 0 through 23.

int PyDateTime\_TIME\_GET\_MINUTE([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_MINUTE "Link to this definition")
  

Return the minute, as an int from 0 through 59.

int PyDateTime\_TIME\_GET\_SECOND([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_SECOND "Link to this definition")
  

Return the second, as an int from 0 through 59.

int PyDateTime\_TIME\_GET\_MICROSECOND([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_MICROSECOND "Link to this definition")
  

Return the microsecond, as an int from 0 through 999999.

int PyDateTime\_TIME\_GET\_FOLD([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_FOLD "Link to this definition")
  

Return the fold, as an int from 0 through 1.

Added in version 3.6.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_TIME\_GET\_TZINFO([PyDateTime\_Time](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Time "PyDateTime_Time")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_TZINFO "Link to this definition")
  

Return the tzinfo (which may be `None`).

Added in version 3.10.

Macros to extract fields from time delta objects. The argument must be an instance of [`PyDateTime_Delta`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Delta "PyDateTime_Delta")
, including subclasses. The argument must not be `NULL`, and the type is not checked:

int PyDateTime\_DELTA\_GET\_DAYS([PyDateTime\_Delta](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Delta "PyDateTime_Delta")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DELTA_GET_DAYS "Link to this definition")
  

Return the number of days, as an int from -999999999 to 999999999.

Added in version 3.3.

int PyDateTime\_DELTA\_GET\_SECONDS([PyDateTime\_Delta](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Delta "PyDateTime_Delta")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DELTA_GET_SECONDS "Link to this definition")
  

Return the number of seconds, as an int from 0 through 86399.

Added in version 3.3.

int PyDateTime\_DELTA\_GET\_MICROSECONDS([PyDateTime\_Delta](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_Delta "PyDateTime_Delta")
 \*o)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DELTA_GET_MICROSECONDS "Link to this definition")
  

Return the number of microseconds, as an int from 0 through 999999.

Added in version 3.3.

Macros for the convenience of modules implementing the DB API:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDateTime\_FromTimestamp([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_FromTimestamp "Link to this definition")
  

_Return value: New reference._

Create and return a new [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
 object given an argument tuple suitable for passing to [`datetime.datetime.fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "datetime.datetime.fromtimestamp")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDate\_FromTimestamp([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDate_FromTimestamp "Link to this definition")
  

_Return value: New reference._

Create and return a new [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
 object given an argument tuple suitable for passing to [`datetime.date.fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.date.fromtimestamp "datetime.date.fromtimestamp")
.

Internal data[¶](https://docs.python.org/3/c-api/datetime.html#internal-data "Link to this heading")

=====================================================================================================

The following symbols are exposed by the C API but should be considered internal-only.

PyDateTime\_CAPSULE\_NAME[¶](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_CAPSULE_NAME "Link to this definition")
  

Name of the datetime capsule to pass to [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "PyCapsule_Import")
.

Internal usage only. Use [`PyDateTime_IMPORT`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "PyDateTime_IMPORT")
 instead.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [DateTime Objects](https://docs.python.org/3/c-api/datetime.html#)
    
*   [Internal data](https://docs.python.org/3/c-api/datetime.html#internal-data)
    

#### Previous topic

[Curses C API](https://docs.python.org/3/c-api/curses.html "previous chapter")

#### Next topic

[Interpreter initialization and finalization](https://docs.python.org/3/c-api/interp-lifecycle.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=DateTime+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fdatetime.html&pagesource=c-api%2Fdatetime.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/datetime.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/interp-lifecycle.html "Interpreter initialization and finalization")
     |
*   [previous](https://docs.python.org/3/c-api/curses.html "Curses C API")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [DateTime Objects](https://docs.python.org/3/c-api/datetime.html)
    
*    
    
    |
*   Theme Auto Light Dark |
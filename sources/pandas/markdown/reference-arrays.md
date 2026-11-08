[Skip to main content](https://pandas.pydata.org/docs/reference/arrays.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/arrays.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/arrays.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/arrays.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/arrays.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/arrays.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/arrays.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/arrays.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/arrays.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/arrays.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/arrays.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/arrays.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/arrays.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/arrays.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas arrays, scalars, and data types[#](https://pandas.pydata.org/docs/reference/arrays.html#pandas-arrays-scalars-and-data-types "Link to this heading")

============================================================================================================================================================

Objects[#](https://pandas.pydata.org/docs/reference/arrays.html#objects "Link to this heading")

------------------------------------------------------------------------------------------------

For most data types, pandas uses NumPy arrays as the concrete objects contained with a [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
.

For some data types, pandas extends NumPy’s type system. String aliases for these types can be found at [dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)
.

| Kind of Data | pandas Data Type | Scalar | Array |
| --- | --- | --- | --- |
| TZ-aware datetime | [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype") | [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp") | [Datetimes](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-datetime) |
| Timedeltas | (none) | [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta") | [Timedeltas](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-timedelta) |
| Period (time spans) | [`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype") | [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period") | [Periods](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-period) |
| Intervals | [`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype") | [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval") | [Intervals](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-interval) |
| Nullable Integer | [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")<br>, … | (none) | [Nullable integer](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-integer-na) |
| Nullable Float | [`Float64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "pandas.Float64Dtype")<br>, … | (none) | [Nullable float](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-float-na) |
| Categorical | [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype") | (none) | [Categoricals](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-categorical) |
| Sparse | [`SparseDtype`](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas.SparseDtype "pandas.SparseDtype") | (none) | [Sparse](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-sparse) |
| Strings | [`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype") | [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)") | [Strings](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-string) |
| Nullable Boolean | [`BooleanDtype`](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype") | [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)") | [Nullable Boolean](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-bool) |
| PyArrow | [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype") | Python Scalars or [`NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA") | [PyArrow](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-arrow) |

pandas and third-party libraries can extend NumPy’s type system (see [Extension types](https://pandas.pydata.org/docs/development/extending.html#extending-extension-types)
). The top-level [`array()`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")
 method can be used to create a new array, which may be stored in a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, or as a column in a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
.

|     |     |
| --- | --- |
| [`array`](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "pandas.array")<br>(data\[, dtype, copy\]) | Create an array. |

### PyArrow[#](https://pandas.pydata.org/docs/reference/arrays.html#pyarrow "Link to this heading")

Warning

This feature is experimental, and the API can change in a future release without warning.

The [`arrays.ArrowExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "pandas.arrays.ArrowExtensionArray")
 is backed by a [`pyarrow.ChunkedArray`](https://arrow.apache.org/docs/python/generated/pyarrow.ChunkedArray.html#pyarrow.ChunkedArray "(in Apache Arrow v26.0.1)")
 with a [`pyarrow.DataType`](https://arrow.apache.org/docs/python/generated/pyarrow.DataType.html#pyarrow.DataType "(in Apache Arrow v26.0.1)")
 instead of a NumPy array and data type. The `.dtype` of a [`arrays.ArrowExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "pandas.arrays.ArrowExtensionArray")
 is an [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
.

[Pyarrow](https://arrow.apache.org/docs/python/index.html)
 provides similar array and [data type](https://arrow.apache.org/docs/python/api/datatypes.html)
 support as NumPy including first-class nullability support for all data types, immutability and more.

The table below shows the equivalent pyarrow-backed (`pa`), pandas extension, and numpy (`np`) types that are recognized by pandas. Pyarrow-backed types below need to be passed into [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
 to be recognized by pandas e.g. `pd.ArrowDtype(pa.bool_())`.

| PyArrow type | pandas extension type | NumPy type |
| --- | --- | --- |
| [`pyarrow.bool_()`](https://arrow.apache.org/docs/python/generated/pyarrow.bool_.html#pyarrow.bool_ "(in Apache Arrow v26.0.1)") | [`BooleanDtype`](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype") | `np.bool_` |
| [`pyarrow.int8()`](https://arrow.apache.org/docs/python/generated/pyarrow.int8.html#pyarrow.int8 "(in Apache Arrow v26.0.1)") | [`Int8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int8Dtype.html#pandas.Int8Dtype "pandas.Int8Dtype") | `np.int8` |
| [`pyarrow.int16()`](https://arrow.apache.org/docs/python/generated/pyarrow.int16.html#pyarrow.int16 "(in Apache Arrow v26.0.1)") | [`Int16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int16Dtype.html#pandas.Int16Dtype "pandas.Int16Dtype") | `np.int16` |
| [`pyarrow.int32()`](https://arrow.apache.org/docs/python/generated/pyarrow.int32.html#pyarrow.int32 "(in Apache Arrow v26.0.1)") | [`Int32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas.Int32Dtype "pandas.Int32Dtype") | `np.int32` |
| [`pyarrow.int64()`](https://arrow.apache.org/docs/python/generated/pyarrow.int64.html#pyarrow.int64 "(in Apache Arrow v26.0.1)") | [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype") | `np.int64` |
| [`pyarrow.uint8()`](https://arrow.apache.org/docs/python/generated/pyarrow.uint8.html#pyarrow.uint8 "(in Apache Arrow v26.0.1)") | [`UInt8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt8Dtype.html#pandas.UInt8Dtype "pandas.UInt8Dtype") | `np.uint8` |
| [`pyarrow.uint16()`](https://arrow.apache.org/docs/python/generated/pyarrow.uint16.html#pyarrow.uint16 "(in Apache Arrow v26.0.1)") | [`UInt16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt16Dtype.html#pandas.UInt16Dtype "pandas.UInt16Dtype") | `np.uint16` |
| [`pyarrow.uint32()`](https://arrow.apache.org/docs/python/generated/pyarrow.uint32.html#pyarrow.uint32 "(in Apache Arrow v26.0.1)") | [`UInt32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt32Dtype.html#pandas.UInt32Dtype "pandas.UInt32Dtype") | `np.uint32` |
| [`pyarrow.uint64()`](https://arrow.apache.org/docs/python/generated/pyarrow.uint64.html#pyarrow.uint64 "(in Apache Arrow v26.0.1)") | [`UInt64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html#pandas.UInt64Dtype "pandas.UInt64Dtype") | `np.uint64` |
| [`pyarrow.float32()`](https://arrow.apache.org/docs/python/generated/pyarrow.float32.html#pyarrow.float32 "(in Apache Arrow v26.0.1)") | [`Float32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float32Dtype.html#pandas.Float32Dtype "pandas.Float32Dtype") | `np.float32` |
| [`pyarrow.float64()`](https://arrow.apache.org/docs/python/generated/pyarrow.float64.html#pyarrow.float64 "(in Apache Arrow v26.0.1)") | [`Float64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "pandas.Float64Dtype") | `np.float64` |
| [`pyarrow.time32()`](https://arrow.apache.org/docs/python/generated/pyarrow.time32.html#pyarrow.time32 "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.time64()`](https://arrow.apache.org/docs/python/generated/pyarrow.time64.html#pyarrow.time64 "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.timestamp()`](https://arrow.apache.org/docs/python/generated/pyarrow.timestamp.html#pyarrow.timestamp "(in Apache Arrow v26.0.1)") | [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype") | `np.datetime64` |
| [`pyarrow.date32()`](https://arrow.apache.org/docs/python/generated/pyarrow.date32.html#pyarrow.date32 "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.date64()`](https://arrow.apache.org/docs/python/generated/pyarrow.date64.html#pyarrow.date64 "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.duration()`](https://arrow.apache.org/docs/python/generated/pyarrow.duration.html#pyarrow.duration "(in Apache Arrow v26.0.1)") | (none) | `np.timedelta64` |
| [`pyarrow.binary()`](https://arrow.apache.org/docs/python/generated/pyarrow.binary.html#pyarrow.binary "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.string()`](https://arrow.apache.org/docs/python/generated/pyarrow.string.html#pyarrow.string "(in Apache Arrow v26.0.1)") | [`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype") | `np.str_` |
| [`pyarrow.decimal128()`](https://arrow.apache.org/docs/python/generated/pyarrow.decimal128.html#pyarrow.decimal128 "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.list_()`](https://arrow.apache.org/docs/python/generated/pyarrow.list_.html#pyarrow.list_ "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.map_()`](https://arrow.apache.org/docs/python/generated/pyarrow.map_.html#pyarrow.map_ "(in Apache Arrow v26.0.1)") | (none) | (none) |
| [`pyarrow.dictionary()`](https://arrow.apache.org/docs/python/generated/pyarrow.dictionary.html#pyarrow.dictionary "(in Apache Arrow v26.0.1)") | [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype") | (none) |

Note

Pyarrow-backed string support is provided by both `pd.StringDtype("pyarrow")` and `pd.ArrowDtype(pa.string())`. `pd.StringDtype("pyarrow")` is described below in the [string section](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-string)
 and will be returned if the string alias `"string[pyarrow]"` is specified. `pd.ArrowDtype(pa.string())` generally has better interoperability with [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
 of different types.

While individual values in an [`arrays.ArrowExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "pandas.arrays.ArrowExtensionArray")
 are stored as a PyArrow objects, scalars are **returned** as Python scalars corresponding to the data type, e.g. a PyArrow int64 will be returned as Python int, or [`NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA "pandas.NA")
 for missing values.

|     |     |
| --- | --- |
| [`arrays.ArrowExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "pandas.arrays.ArrowExtensionArray")<br>(values) | Pandas ExtensionArray backed by a PyArrow ChunkedArray. |

|     |     |
| --- | --- |
| [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")<br>(pyarrow\_dtype) | An ExtensionDtype for PyArrow data types. |

For more information, please see the [PyArrow user guide](https://pandas.pydata.org/docs/user_guide/pyarrow.html#pyarrow)
.

### Datetimes[#](https://pandas.pydata.org/docs/reference/arrays.html#datetimes "Link to this heading")

NumPy cannot natively represent timezone-aware datetimes. pandas supports this with the [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")
 extension array, which can hold timezone-naive or timezone-aware values.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
, a subclass of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")
, is pandas’ scalar type for timezone-naive or timezone-aware datetime data. [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
 is the missing value for datetime data.

|     |     |
| --- | --- |
| [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")<br>(\[ts\_input, year, month, day, ...\]) | Pandas replacement for python datetime.datetime object. |

#### Properties[#](https://pandas.pydata.org/docs/reference/arrays.html#properties "Link to this heading")

|     |     |
| --- | --- |
| [`Timestamp.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas.Timestamp.asm8 "pandas.Timestamp.asm8") | Return numpy datetime64 format with same precision. |
| [`Timestamp.day`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#pandas.Timestamp.day "pandas.Timestamp.day") | Return the day of the Timestamp. |
| [`Timestamp.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dayofweek.html#pandas.Timestamp.dayofweek "pandas.Timestamp.dayofweek") | (DEPRECATED) Return day of the week. |
| [`Timestamp.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas.Timestamp.day_of_week "pandas.Timestamp.day_of_week") | Return day of the week. |
| [`Timestamp.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dayofyear.html#pandas.Timestamp.dayofyear "pandas.Timestamp.dayofyear") | (DEPRECATED) Return day of the year. |
| [`Timestamp.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas.Timestamp.day_of_year "pandas.Timestamp.day_of_year") | Return the day of the year. |
| [`Timestamp.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html#pandas.Timestamp.days_in_month "pandas.Timestamp.days_in_month") | Return the number of days in the month. |
| [`Timestamp.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.daysinmonth.html#pandas.Timestamp.daysinmonth "pandas.Timestamp.daysinmonth") | (DEPRECATED) Return the number of days in the month. |
| [`Timestamp.fold`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html#pandas.Timestamp.fold "pandas.Timestamp.fold") | Return the fold value of the Timestamp. |
| [`Timestamp.hour`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.hour.html#pandas.Timestamp.hour "pandas.Timestamp.hour") | Return the hour of the Timestamp. |
| [`Timestamp.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#pandas.Timestamp.is_leap_year "pandas.Timestamp.is_leap_year") | Return True if year is a leap year. |
| [`Timestamp.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#pandas.Timestamp.is_month_end "pandas.Timestamp.is_month_end") | Check if the date is the last day of the month. |
| [`Timestamp.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#pandas.Timestamp.is_month_start "pandas.Timestamp.is_month_start") | Check if the date is the first day of the month. |
| [`Timestamp.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#pandas.Timestamp.is_quarter_end "pandas.Timestamp.is_quarter_end") | Check if date is last day of the quarter. |
| [`Timestamp.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#pandas.Timestamp.is_quarter_start "pandas.Timestamp.is_quarter_start") | Check if the date is the first day of the quarter. |
| [`Timestamp.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_year_end.html#pandas.Timestamp.is_year_end "pandas.Timestamp.is_year_end") | Return True if date is last day of the year. |
| [`Timestamp.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_year_start.html#pandas.Timestamp.is_year_start "pandas.Timestamp.is_year_start") | Return True if date is first day of the year. |
| [`Timestamp.max`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.max.html#pandas.Timestamp.max "pandas.Timestamp.max") |     |
| [`Timestamp.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas.Timestamp.microsecond "pandas.Timestamp.microsecond") | Return the microsecond of the Timestamp. |
| [`Timestamp.min`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.min.html#pandas.Timestamp.min "pandas.Timestamp.min") |     |
| [`Timestamp.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "pandas.Timestamp.minute") | Return the minute of the Timestamp. |
| [`Timestamp.month`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#pandas.Timestamp.month "pandas.Timestamp.month") | Return the month of the Timestamp. |
| [`Timestamp.nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.nanosecond.html#pandas.Timestamp.nanosecond "pandas.Timestamp.nanosecond") | Return the nanosecond of the Timestamp. |
| [`Timestamp.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter") | Return the quarter of the year for the Timestamp. |
| [`Timestamp.resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.resolution.html#pandas.Timestamp.resolution "pandas.Timestamp.resolution") |     |
| [`Timestamp.second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second") | Return the second of the Timestamp. |
| [`Timestamp.tz`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#pandas.Timestamp.tz "pandas.Timestamp.tz") | Alias for tzinfo. |
| [`Timestamp.tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo") | Returns the timezone info of the Timestamp. |
| [`Timestamp.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.unit.html#pandas.Timestamp.unit "pandas.Timestamp.unit") | The abbreviation associated with self.\_creso. |
| [`Timestamp.value`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.value.html#pandas.Timestamp.value "pandas.Timestamp.value") | Return the value of the Timestamp. |
| [`Timestamp.week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.week.html#pandas.Timestamp.week "pandas.Timestamp.week") | Return the week number of the year. |
| [`Timestamp.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html#pandas.Timestamp.weekofyear "pandas.Timestamp.weekofyear") | Return the week number of the year. |
| [`Timestamp.year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.year.html#pandas.Timestamp.year "pandas.Timestamp.year") | Return the year of the Timestamp. |

#### Methods[#](https://pandas.pydata.org/docs/reference/arrays.html#methods "Link to this heading")

|     |     |
| --- | --- |
| [`Timestamp.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "pandas.Timestamp.as_unit")<br>(unit\[, round\_ok\]) | Convert the underlying int64 representation to the given unit. |
| [`Timestamp.astimezone`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html#pandas.Timestamp.astimezone "pandas.Timestamp.astimezone")<br>(tz) | Convert timezone-aware Timestamp to another time zone. |
| [`Timestamp.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html#pandas.Timestamp.ceil "pandas.Timestamp.ceil")<br>(freq\[, ambiguous, nonexistent\]) | Return a new Timestamp ceiled to this resolution. |
| [`Timestamp.combine`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html#pandas.Timestamp.combine "pandas.Timestamp.combine")<br>(date, time) | Combine a date and time into a single Timestamp object. |
| [`Timestamp.ctime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html#pandas.Timestamp.ctime "pandas.Timestamp.ctime")<br>() | Return a ctime() style string representing the Timestamp. |
| [`Timestamp.date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#pandas.Timestamp.date "pandas.Timestamp.date")<br>() | Returns datetime.date with the same year, month, and day. |
| [`Timestamp.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#pandas.Timestamp.day_name "pandas.Timestamp.day_name")<br>(\[locale\]) | Return the day name of the Timestamp with specified locale. |
| [`Timestamp.dst`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas.Timestamp.dst "pandas.Timestamp.dst")<br>() | Return the daylight saving time (DST) adjustment. |
| [`Timestamp.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas.Timestamp.floor "pandas.Timestamp.floor")<br>(freq\[, ambiguous, nonexistent\]) | Return a new Timestamp floored to this resolution. |
| [`Timestamp.fromisocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html#pandas.Timestamp.fromisocalendar "pandas.Timestamp.fromisocalendar")<br>(year, week, day) | Construct a Timestamp from an ISO year, week number, and weekday. |
| [`Timestamp.fromisoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html#pandas.Timestamp.fromisoformat "pandas.Timestamp.fromisoformat")<br>(date\_string) | Construct a Timestamp from a string in ISO 8601 format. |
| [`Timestamp.fromordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas.Timestamp.fromordinal "pandas.Timestamp.fromordinal")<br>(ordinal\[, tz\]) | Construct a timestamp from a proleptic Gregorian ordinal. |
| [`Timestamp.fromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas.Timestamp.fromtimestamp "pandas.Timestamp.fromtimestamp")<br>(ts\[, tz\]) | Create a Timestamp object from a POSIX timestamp. |
| [`Timestamp.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")<br>() | Return a named tuple containing ISO year, week number, and weekday. |
| [`Timestamp.isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "pandas.Timestamp.isoformat")<br>(\[sep, timespec\]) | Return the time formatted according to ISO 8601. |
| [`Timestamp.isoweekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#pandas.Timestamp.isoweekday "pandas.Timestamp.isoweekday")<br>() | Return the day of the week represented by the date. |
| [`Timestamp.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#pandas.Timestamp.month_name "pandas.Timestamp.month_name")<br>(\[locale\]) | Return the month name of the Timestamp with specified locale. |
| [`Timestamp.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html#pandas.Timestamp.normalize "pandas.Timestamp.normalize")<br>() | Normalize Timestamp to midnight, preserving tz information. |
| [`Timestamp.now`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas.Timestamp.now "pandas.Timestamp.now")<br>(\[tz\]) | Return new Timestamp object representing current time local to tz. |
| [`Timestamp.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html#pandas.Timestamp.replace "pandas.Timestamp.replace")<br>(\[year, month, day, hour, ...\]) | Implements datetime.replace, handles nanoseconds. |
| [`Timestamp.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html#pandas.Timestamp.round "pandas.Timestamp.round")<br>(freq\[, ambiguous, nonexistent\]) | Round the Timestamp to the specified resolution. |
| [`Timestamp.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")<br>(format) | Return a formatted string of the Timestamp. |
| [`Timestamp.strptime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strptime.html#pandas.Timestamp.strptime "pandas.Timestamp.strptime")<br>(date\_string, format) | Convert string argument to datetime. |
| [`Timestamp.time`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html#pandas.Timestamp.time "pandas.Timestamp.time")<br>() | Return time object with same time but with tzinfo=None. |
| [`Timestamp.timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")<br>() | Return POSIX timestamp as float. |
| [`Timestamp.timetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#pandas.Timestamp.timetuple "pandas.Timestamp.timetuple")<br>() | Return time tuple, compatible with time.localtime(). |
| [`Timestamp.timetz`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html#pandas.Timestamp.timetz "pandas.Timestamp.timetz")<br>() | Return time object with same time and tzinfo. |
| [`Timestamp.to_datetime64`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas.Timestamp.to_datetime64 "pandas.Timestamp.to_datetime64")<br>() | Return a NumPy datetime64 object with same precision. |
| [`Timestamp.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas.Timestamp.to_numpy "pandas.Timestamp.to_numpy")<br>(\[dtype, copy\]) | Convert the Timestamp to a NumPy datetime64. |
| [`Timestamp.to_julian_date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#pandas.Timestamp.to_julian_date "pandas.Timestamp.to_julian_date")<br>() | Convert Timestamp to a Julian Date. |
| [`Timestamp.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#pandas.Timestamp.to_period "pandas.Timestamp.to_period")<br>(\[freq\]) | Return a period of which this timestamp is an observation. |
| [`Timestamp.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas.Timestamp.to_pydatetime "pandas.Timestamp.to_pydatetime")<br>(\[warn\]) | Convert a Timestamp object to a native Python datetime object. |
| [`Timestamp.today`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas.Timestamp.today "pandas.Timestamp.today")<br>(\[tz\]) | Return the current time in the local timezone. |
| [`Timestamp.toordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#pandas.Timestamp.toordinal "pandas.Timestamp.toordinal")<br>() | Return proleptic Gregorian ordinal. |
| [`Timestamp.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")<br>(tz) | Convert timezone-aware Timestamp to another time zone. |
| [`Timestamp.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")<br>(tz\[, ambiguous, ...\]) | Attach or detach a time zone on a Timestamp. |
| [`Timestamp.tzname`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#pandas.Timestamp.tzname "pandas.Timestamp.tzname")<br>() | Return time zone name. |
| [`Timestamp.utcfromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html#pandas.Timestamp.utcfromtimestamp "pandas.Timestamp.utcfromtimestamp")<br>(ts) | Construct a timezone-aware UTC datetime from a POSIX timestamp. |
| [`Timestamp.utcnow`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas.Timestamp.utcnow "pandas.Timestamp.utcnow")<br>() | (DEPRECATED) Return a new Timestamp representing UTC day and time. |
| [`Timestamp.utcoffset`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html#pandas.Timestamp.utcoffset "pandas.Timestamp.utcoffset")<br>() | Return utc offset. |
| [`Timestamp.utctimetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#pandas.Timestamp.utctimetuple "pandas.Timestamp.utctimetuple")<br>() | Return UTC time tuple, compatible with time.localtime(). |
| [`Timestamp.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")<br>() | Return the day of the week represented by the date. |

A collection of timestamps may be stored in a [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")
. For timezone-aware data, the `.dtype` of a [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")
 is a [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype")
. For timezone-naive data, `np.dtype("datetime64[ns]")` is used.

If the data are timezone-aware, then every value in the array must have the same timezone.

|     |     |
| --- | --- |
| [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")<br>(data\[, dtype, freq, copy\]) | Pandas ExtensionArray for tz-naive or tz-aware datetime data. |

|     |     |
| --- | --- |
| [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype")<br>(\[unit, tz\]) | An ExtensionDtype for timezone-aware datetime data. |

### Timedeltas[#](https://pandas.pydata.org/docs/reference/arrays.html#timedeltas "Link to this heading")

NumPy can natively represent timedeltas. pandas provides [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 for symmetry with [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
. [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
 is the missing value for timedelta data.

|     |     |
| --- | --- |
| [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")<br>(\[value, unit\]) | Represents a duration, the difference between two dates or times. |

#### Properties[#](https://pandas.pydata.org/docs/reference/arrays.html#id1 "Link to this heading")

|     |     |
| --- | --- |
| [`Timedelta.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas.Timedelta.asm8 "pandas.Timedelta.asm8") | Return a numpy timedelta64 array scalar view. |
| [`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components") | Return a components namedtuple-like. |
| [`Timedelta.days`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html#pandas.Timedelta.days "pandas.Timedelta.days") | Returns the days of the timedelta. |
| [`Timedelta.max`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.max.html#pandas.Timedelta.max "pandas.Timedelta.max") |     |
| [`Timedelta.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.microseconds.html#pandas.Timedelta.microseconds "pandas.Timedelta.microseconds") | Return the number of microseconds (n), where 0 <= n < 1 millisecond. |
| [`Timedelta.min`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.min.html#pandas.Timedelta.min "pandas.Timedelta.min") |     |
| [`Timedelta.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html#pandas.Timedelta.nanoseconds "pandas.Timedelta.nanoseconds") | Return the number of nanoseconds (n), where 0 <= n < 1 microsecond. |
| [`Timedelta.resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution.html#pandas.Timedelta.resolution "pandas.Timedelta.resolution") |     |
| [`Timedelta.resolution_string`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution_string.html#pandas.Timedelta.resolution_string "pandas.Timedelta.resolution_string") | Return a string representing the lowest timedelta resolution. |
| [`Timedelta.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.seconds.html#pandas.Timedelta.seconds "pandas.Timedelta.seconds") | Return the total hours, minutes, and seconds of the timedelta as seconds. |
| [`Timedelta.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#pandas.Timedelta.unit "pandas.Timedelta.unit") | Return the unit of Timedelta object. |
| [`Timedelta.value`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#pandas.Timedelta.value "pandas.Timedelta.value") | Return the value of Timedelta object in nanoseconds. |
| [`Timedelta.view`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html#pandas.Timedelta.view "pandas.Timedelta.view")<br>(dtype) | Array view compatibility. |

#### Methods[#](https://pandas.pydata.org/docs/reference/arrays.html#id2 "Link to this heading")

|     |     |
| --- | --- |
| [`Timedelta.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas.Timedelta.as_unit "pandas.Timedelta.as_unit")<br>(unit\[, round\_ok\]) | Convert the underlying int64 representation to the given unit. |
| [`Timedelta.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas.Timedelta.ceil "pandas.Timedelta.ceil")<br>(freq) | Return a new Timedelta ceiled to this resolution. |
| [`Timedelta.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas.Timedelta.floor "pandas.Timedelta.floor")<br>(freq) | Return a new Timedelta floored to this resolution. |
| [`Timedelta.isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html#pandas.Timedelta.isoformat "pandas.Timedelta.isoformat")<br>() | Format the Timedelta as ISO 8601 Duration. |
| [`Timedelta.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas.Timedelta.round "pandas.Timedelta.round")<br>(freq) | Round the Timedelta to the specified resolution. |
| [`Timedelta.to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html#pandas.Timedelta.to_pytimedelta "pandas.Timedelta.to_pytimedelta")<br>() | Convert a pandas Timedelta object into a python `datetime.timedelta` object. |
| [`Timedelta.to_timedelta64`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#pandas.Timedelta.to_timedelta64 "pandas.Timedelta.to_timedelta64")<br>() | Return a numpy.timedelta64 object with 'ns' precision. |
| [`Timedelta.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#pandas.Timedelta.to_numpy "pandas.Timedelta.to_numpy")<br>(\[dtype, copy\]) | Convert the Timedelta to a NumPy timedelta64. |
| [`Timedelta.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")<br>() | Total seconds in the duration. |

A collection of [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 may be stored in a `TimedeltaArray`.

|     |     |
| --- | --- |
| [`arrays.TimedeltaArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas.arrays.TimedeltaArray "pandas.arrays.TimedeltaArray")<br>(data\[, dtype, freq, copy\]) | Pandas ExtensionArray for timedelta data. |

### Periods[#](https://pandas.pydata.org/docs/reference/arrays.html#periods "Link to this heading")

pandas represents spans of times as [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 objects.

### Period[#](https://pandas.pydata.org/docs/reference/arrays.html#period "Link to this heading")

|     |     |
| --- | --- |
| [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")<br>(\[value, freq, ordinal, year, month, ...\]) | Represents a period of time. |

#### Properties[#](https://pandas.pydata.org/docs/reference/arrays.html#id3 "Link to this heading")

|     |     |
| --- | --- |
| [`Period.day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day") | Get day of the month that a Period falls on. |
| [`Period.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek") | (DEPRECATED) Return day of the week. |
| [`Period.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas.Period.day_of_week "pandas.Period.day_of_week") | Day of the week the period lies in, with Monday=0 and Sunday=6. |
| [`Period.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear") | (DEPRECATED) Return day of the year. |
| [`Period.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas.Period.day_of_year "pandas.Period.day_of_year") | Return the day of the year. |
| [`Period.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas.Period.days_in_month "pandas.Period.days_in_month") | Get the total number of days in the month that this period falls on. |
| [`Period.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "pandas.Period.daysinmonth") | (DEPRECATED) Get the total number of days of the month that this period falls on. |
| [`Period.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "pandas.Period.end_time") | Get the Timestamp for the end of the period. |
| [`Period.freq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#pandas.Period.freq "pandas.Period.freq") | Return the frequency object for this Period. |
| [`Period.freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#pandas.Period.freqstr "pandas.Period.freqstr") | Return a string representation of the frequency. |
| [`Period.hour`](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html#pandas.Period.hour "pandas.Period.hour") | Get the hour of the day component of the Period. |
| [`Period.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#pandas.Period.is_leap_year "pandas.Period.is_leap_year") | Return True if the period's year is in a leap year. |
| [`Period.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Period.minute.html#pandas.Period.minute "pandas.Period.minute") | Get minute of the hour component of the Period. |
| [`Period.month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#pandas.Period.month "pandas.Period.month") | Return the month this Period falls on. |
| [`Period.ordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html#pandas.Period.ordinal "pandas.Period.ordinal") | Return the integer ordinal for this Period. |
| [`Period.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html#pandas.Period.quarter "pandas.Period.quarter") | Return the quarter this Period falls on. |
| [`Period.qyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.qyear.html#pandas.Period.qyear "pandas.Period.qyear") | Fiscal year the Period lies in according to its starting-quarter. |
| [`Period.second`](https://pandas.pydata.org/docs/reference/api/pandas.Period.second.html#pandas.Period.second "pandas.Period.second") | Get the second component of the Period. |
| [`Period.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time") | Get the Timestamp for the start of the period. |
| [`Period.week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html#pandas.Period.week "pandas.Period.week") | Get the week of the year on the given Period. |
| [`Period.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "pandas.Period.weekday") | Day of the week the period lies in, with Monday=0 and Sunday=6. |
| [`Period.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekofyear.html#pandas.Period.weekofyear "pandas.Period.weekofyear") | Get the week of the year on the given Period. |
| [`Period.year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas.Period.year "pandas.Period.year") | Return the year this Period falls on. |

#### Methods[#](https://pandas.pydata.org/docs/reference/arrays.html#id4 "Link to this heading")

|     |     |
| --- | --- |
| [`Period.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")<br>(freq\[, how\]) | Convert Period to desired frequency, at the start or end of the interval. |
| [`Period.now`](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html#pandas.Period.now "pandas.Period.now")<br>(freq) | Return the period of now's date. |
| [`Period.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")<br>(fmt) | (DEPRECATED) Returns a formatted string representation of the [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")<br>. |
| [`Period.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#pandas.Period.to_timestamp "pandas.Period.to_timestamp")<br>(\[freq, how\]) | Return the Timestamp representation of the Period. |

A collection of [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 may be stored in a [`arrays.PeriodArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "pandas.arrays.PeriodArray")
. Every period in a [`arrays.PeriodArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "pandas.arrays.PeriodArray")
 must have the same `freq`.

|     |     |
| --- | --- |
| [`arrays.PeriodArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "pandas.arrays.PeriodArray")<br>(values\[, dtype, copy\]) | Pandas ExtensionArray for storing Period data. |

|     |     |
| --- | --- |
| [`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")<br>(freq) | An ExtensionDtype for Period data. |

### Intervals[#](https://pandas.pydata.org/docs/reference/arrays.html#intervals "Link to this heading")

Arbitrary intervals can be represented as [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 objects.

|     |     |
| --- | --- |
| [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval") | Immutable object implementing an Interval, a bounded slice-like interval. |

#### Properties[#](https://pandas.pydata.org/docs/reference/arrays.html#id5 "Link to this heading")

|     |     |
| --- | --- |
| [`Interval.closed`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed.html#pandas.Interval.closed "pandas.Interval.closed") | String describing the inclusive side the intervals. |
| [`Interval.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_left.html#pandas.Interval.closed_left "pandas.Interval.closed_left") | Check if the interval is closed on the left side. |
| [`Interval.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.closed_right.html#pandas.Interval.closed_right "pandas.Interval.closed_right") | Check if the interval is closed on the right side. |
| [`Interval.is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.is_empty.html#pandas.Interval.is_empty "pandas.Interval.is_empty") | Indicates if an interval is empty, meaning it contains no points. |
| [`Interval.left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.left.html#pandas.Interval.left "pandas.Interval.left") | Left bound for the interval. |
| [`Interval.length`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.length.html#pandas.Interval.length "pandas.Interval.length") | Return the length of the Interval. |
| [`Interval.mid`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.mid.html#pandas.Interval.mid "pandas.Interval.mid") | Return the midpoint of the Interval. |
| [`Interval.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_left.html#pandas.Interval.open_left "pandas.Interval.open_left") | Check if the interval is open on the left side. |
| [`Interval.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.open_right.html#pandas.Interval.open_right "pandas.Interval.open_right") | Check if the interval is open on the right side. |
| [`Interval.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas.Interval.overlaps "pandas.Interval.overlaps")<br>(other) | Check whether two Interval objects overlap. |
| [`Interval.right`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.right.html#pandas.Interval.right "pandas.Interval.right") | Right bound for the interval. |

A collection of intervals may be stored in an [`arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")
.

|     |     |
| --- | --- |
| [`arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")<br>(data\[, closed, dtype, ...\]) | Pandas array for interval data that are closed on the same side. |

|     |     |
| --- | --- |
| [`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype")<br>(\[subtype, closed\]) | An ExtensionDtype for Interval data. |

### Nullable integer[#](https://pandas.pydata.org/docs/reference/arrays.html#nullable-integer "Link to this heading")

[`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 cannot natively represent integer-data with missing values. pandas provides this through [`arrays.IntegerArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas.arrays.IntegerArray "pandas.arrays.IntegerArray")
.

|     |     |
| --- | --- |
| [`arrays.IntegerArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas.arrays.IntegerArray "pandas.arrays.IntegerArray")<br>(values, mask\[, copy\]) | Array of integer (optional missing) values. |

|     |     |
| --- | --- |
| [`Int8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int8Dtype.html#pandas.Int8Dtype "pandas.Int8Dtype")<br>() | An ExtensionDtype for int8 integer data. |
| [`Int16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int16Dtype.html#pandas.Int16Dtype "pandas.Int16Dtype")<br>() | An ExtensionDtype for int16 integer data. |
| [`Int32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas.Int32Dtype "pandas.Int32Dtype")<br>() | An ExtensionDtype for int32 integer data. |
| [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")<br>() | An ExtensionDtype for int64 integer data. |
| [`UInt8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt8Dtype.html#pandas.UInt8Dtype "pandas.UInt8Dtype")<br>() | An ExtensionDtype for uint8 integer data. |
| [`UInt16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt16Dtype.html#pandas.UInt16Dtype "pandas.UInt16Dtype")<br>() | An ExtensionDtype for uint16 integer data. |
| [`UInt32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt32Dtype.html#pandas.UInt32Dtype "pandas.UInt32Dtype")<br>() | An ExtensionDtype for uint32 integer data. |
| [`UInt64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.UInt64Dtype.html#pandas.UInt64Dtype "pandas.UInt64Dtype")<br>() | An ExtensionDtype for uint64 integer data. |

### Nullable float[#](https://pandas.pydata.org/docs/reference/arrays.html#nullable-float "Link to this heading")

|     |     |
| --- | --- |
| [`arrays.FloatingArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#pandas.arrays.FloatingArray "pandas.arrays.FloatingArray")<br>(values, mask\[, copy\]) | Array of floating (optional missing) values. |

|     |     |
| --- | --- |
| [`Float32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float32Dtype.html#pandas.Float32Dtype "pandas.Float32Dtype")<br>() | An ExtensionDtype for float32 data. |
| [`Float64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "pandas.Float64Dtype")<br>() | An ExtensionDtype for float64 data. |

### Categoricals[#](https://pandas.pydata.org/docs/reference/arrays.html#categoricals "Link to this heading")

pandas defines a custom data type for representing data that can take only a limited, fixed set of values. The dtype of a [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 can be described by a [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
.

|     |     |
| --- | --- |
| [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")<br>(\[categories, ordered\]) | Type for categorical data with the categories and orderedness. |

|     |     |
| --- | --- |
| [`CategoricalDtype.categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.categories.html#pandas.CategoricalDtype.categories "pandas.CategoricalDtype.categories") | An `Index` containing the unique categories allowed. |
| [`CategoricalDtype.ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.ordered.html#pandas.CategoricalDtype.ordered "pandas.CategoricalDtype.ordered") | Whether the categories have an ordered relationship. |

Categorical data can be stored in a [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
:

|     |     |
| --- | --- |
| [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")<br>(values\[, categories, ordered, ...\]) | Represent a categorical variable in classic R / S-plus fashion. |

The alternative [`Categorical.from_codes()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")
 constructor can be used when you have the categories and integer codes already:

|     |     |
| --- | --- |
| [`Categorical.from_codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")<br>(codes\[, categories, ...\]) | Make a Categorical type from codes and categories or dtype. |

The dtype information is available on the [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")

|     |     |
| --- | --- |
| [`Categorical.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.dtype.html#pandas.Categorical.dtype "pandas.Categorical.dtype") | The `CategoricalDtype` for this instance. |
| [`Categorical.categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.categories.html#pandas.Categorical.categories "pandas.Categorical.categories") | The categories of this categorical. |
| [`Categorical.ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.ordered.html#pandas.Categorical.ordered "pandas.Categorical.ordered") | Whether the categories have an ordered relationship. |
| [`Categorical.codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#pandas.Categorical.codes "pandas.Categorical.codes") | The category codes of this categorical index. |

`np.asarray(categorical)` works by implementing the array interface. Be aware, that this converts the [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 back to a NumPy array, so categories and order information is not preserved!

|     |     |
| --- | --- |
| [`Categorical.__array__`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html#pandas.Categorical.__array__ "pandas.Categorical.__array__")<br>(\[dtype, copy\]) | The numpy array interface. |

A [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 can be stored in a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. To create a Series of dtype `category`, use `cat = s.astype(dtype)` or `Series(..., dtype=dtype)` where `dtype` is either

*   the string `'category'`
    
*   an instance of [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
    .
    

If the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is of dtype [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
, `Series.cat` can be used to change the categorical data. See [Categorical accessor](https://pandas.pydata.org/docs/reference/series.html#api-series-cat)
 for more.

More methods are available on [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
:

|     |     |
| --- | --- |
| [`Categorical.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_ordered.html#pandas.Categorical.as_ordered "pandas.Categorical.as_ordered")<br>() | Set the Categorical to be ordered. |
| [`Categorical.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.as_unordered.html#pandas.Categorical.as_unordered "pandas.Categorical.as_unordered")<br>() | Set the Categorical to be unordered. |
| [`Categorical.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")<br>(new\_categories\[, ...\]) | Set the categories to the specified new categories. |
| [`Categorical.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")<br>(new\_categories) | Rename categories. |
| [`Categorical.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")<br>(new\_categories) | Reorder categories as specified in new\_categories. |
| [`Categorical.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")<br>(new\_categories) | Add new categories. |
| [`Categorical.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "pandas.Categorical.remove_categories")<br>(removals) | Remove the specified categories. |
| [`Categorical.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "pandas.Categorical.remove_unused_categories")<br>() | Remove categories which are not used. |
| [`Categorical.map`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.map.html#pandas.Categorical.map "pandas.Categorical.map")<br>(mapper\[, na\_action\]) | Map categories using an input mapping or function. |

### Sparse[#](https://pandas.pydata.org/docs/reference/arrays.html#sparse "Link to this heading")

Data where a single value is repeated many times (e.g. `0` or `NaN`) may be stored efficiently as a [`arrays.SparseArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")
.

|     |     |
| --- | --- |
| [`arrays.SparseArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")<br>(data\[, sparse\_index, ...\]) | An ExtensionArray for storing sparse data. |

|     |     |
| --- | --- |
| [`SparseDtype`](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas.SparseDtype "pandas.SparseDtype")<br>(\[dtype, fill\_value\]) | Dtype for data stored in `SparseArray`. |

The `Series.sparse` accessor may be used to access sparse-specific attributes and methods if the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 contains sparse values. See [Sparse accessor](https://pandas.pydata.org/docs/reference/series.html#api-series-sparse)
 and [the user guide](https://pandas.pydata.org/docs/user_guide/sparse.html#sparse)
 for more.

### Strings[#](https://pandas.pydata.org/docs/reference/arrays.html#strings "Link to this heading")

When working with text data, where each valid element is a string or missing, we recommend using [`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")
 (with the alias `"string"`).

|     |     |
| --- | --- |
| [`arrays.StringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas.arrays.StringArray "pandas.arrays.StringArray")<br>(values, \*\[, dtype, copy\]) | Extension array for string data. |
| [`arrays.ArrowStringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html#pandas.arrays.ArrowStringArray "pandas.arrays.ArrowStringArray")<br>(values, \*\[, dtype\]) | Extension array for string data in a `pyarrow.ChunkedArray`. |

|     |     |
| --- | --- |
| [`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")<br>(\[storage, na\_value\]) | Extension dtype for string data. |

The `Series.str` accessor is available for [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 backed by a [`arrays.StringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas.arrays.StringArray "pandas.arrays.StringArray")
. See [String handling](https://pandas.pydata.org/docs/reference/series.html#api-series-str)
 for more.

### Nullable Boolean[#](https://pandas.pydata.org/docs/reference/arrays.html#nullable-boolean "Link to this heading")

The boolean dtype (with the alias `"boolean"`) provides support for storing boolean data (`True`, `False`) with missing values, which is not possible with a bool [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
.

|     |     |
| --- | --- |
| [`arrays.BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray")<br>(values, mask\[, copy\]) | Array of boolean (True/False) data with missing values. |

|     |     |
| --- | --- |
| [`BooleanDtype`](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype")<br>() | Extension dtype for boolean data. |

Utilities[#](https://pandas.pydata.org/docs/reference/arrays.html#utilities "Link to this heading")

----------------------------------------------------------------------------------------------------

### Constructors[#](https://pandas.pydata.org/docs/reference/arrays.html#constructors "Link to this heading")

|     |     |
| --- | --- |
| [`api.types.union_categoricals`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#pandas.api.types.union_categoricals "pandas.api.types.union_categoricals")<br>(to\_union\[, ...\]) | Combine list-like of Categorical-like, unioning categories. |
| [`api.types.infer_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.infer_dtype.html#pandas.api.types.infer_dtype "pandas.api.types.infer_dtype")<br>(value\[, skipna\]) | Return a string label of the type of the elements in a list-like input. |
| [`api.types.pandas_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.pandas_dtype.html#pandas.api.types.pandas_dtype "pandas.api.types.pandas_dtype")<br>(dtype) | Convert input into a pandas only dtype object or a numpy dtype object. |

#### Data type introspection[#](https://pandas.pydata.org/docs/reference/arrays.html#data-type-introspection "Link to this heading")

|     |     |
| --- | --- |
| [`api.types.is_any_real_numeric_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_any_real_numeric_dtype.html#pandas.api.types.is_any_real_numeric_dtype "pandas.api.types.is_any_real_numeric_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a real number dtype. |
| [`api.types.is_bool_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool_dtype.html#pandas.api.types.is_bool_dtype "pandas.api.types.is_bool_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a boolean dtype. |
| [`api.types.is_categorical_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_categorical_dtype.html#pandas.api.types.is_categorical_dtype "pandas.api.types.is_categorical_dtype")<br>(arr\_or\_dtype) | (DEPRECATED) Check whether an array-like or dtype is of the Categorical dtype. |
| [`api.types.is_complex_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex_dtype.html#pandas.api.types.is_complex_dtype "pandas.api.types.is_complex_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a complex dtype. |
| [`api.types.is_datetime64_any_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_any_dtype.html#pandas.api.types.is_datetime64_any_dtype "pandas.api.types.is_datetime64_any_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of the datetime64 dtype. |
| [`api.types.is_datetime64_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_dtype.html#pandas.api.types.is_datetime64_dtype "pandas.api.types.is_datetime64_dtype")<br>(arr\_or\_dtype) | Check whether an array-like or dtype is of the datetime64 dtype. |
| [`api.types.is_datetime64_ns_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64_ns_dtype.html#pandas.api.types.is_datetime64_ns_dtype "pandas.api.types.is_datetime64_ns_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of the datetime64\[ns\] dtype. |
| [`api.types.is_datetime64tz_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_datetime64tz_dtype.html#pandas.api.types.is_datetime64tz_dtype "pandas.api.types.is_datetime64tz_dtype")<br>(arr\_or\_dtype) | (DEPRECATED) Check whether an array-like or dtype is of a DatetimeTZDtype dtype. |
| [`api.types.is_dtype_equal`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dtype_equal.html#pandas.api.types.is_dtype_equal "pandas.api.types.is_dtype_equal")<br>(source, target) | Check if two dtypes are equal. |
| [`api.types.is_extension_array_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_extension_array_dtype.html#pandas.api.types.is_extension_array_dtype "pandas.api.types.is_extension_array_dtype")<br>(arr\_or\_dtype) | Check if an object is a pandas extension array type. |
| [`api.types.is_float_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float_dtype.html#pandas.api.types.is_float_dtype "pandas.api.types.is_float_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a float dtype. |
| [`api.types.is_int64_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_int64_dtype.html#pandas.api.types.is_int64_dtype "pandas.api.types.is_int64_dtype")<br>(arr\_or\_dtype) | (DEPRECATED) Check whether the provided array or dtype is of the int64 dtype. |
| [`api.types.is_integer_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer_dtype.html#pandas.api.types.is_integer_dtype "pandas.api.types.is_integer_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of an integer dtype. |
| [`api.types.is_interval_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_interval_dtype.html#pandas.api.types.is_interval_dtype "pandas.api.types.is_interval_dtype")<br>(arr\_or\_dtype) | (DEPRECATED) Check whether an array-like or dtype is of the Interval dtype. |
| [`api.types.is_numeric_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_numeric_dtype.html#pandas.api.types.is_numeric_dtype "pandas.api.types.is_numeric_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a numeric dtype. |
| [`api.types.is_object_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_object_dtype.html#pandas.api.types.is_object_dtype "pandas.api.types.is_object_dtype")<br>(arr\_or\_dtype) | Check whether an array-like or dtype is of the object dtype. |
| [`api.types.is_period_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_period_dtype.html#pandas.api.types.is_period_dtype "pandas.api.types.is_period_dtype")<br>(arr\_or\_dtype) | (DEPRECATED) Check whether an array-like or dtype is of the Period dtype. |
| [`api.types.is_signed_integer_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_signed_integer_dtype.html#pandas.api.types.is_signed_integer_dtype "pandas.api.types.is_signed_integer_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of a signed integer dtype. |
| [`api.types.is_string_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_string_dtype.html#pandas.api.types.is_string_dtype "pandas.api.types.is_string_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of the string dtype. |
| [`api.types.is_timedelta64_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_dtype.html#pandas.api.types.is_timedelta64_dtype "pandas.api.types.is_timedelta64_dtype")<br>(arr\_or\_dtype) | Check whether an array-like or dtype is of the timedelta64 dtype. |
| [`api.types.is_timedelta64_ns_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_timedelta64_ns_dtype.html#pandas.api.types.is_timedelta64_ns_dtype "pandas.api.types.is_timedelta64_ns_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of the timedelta64\[ns\] dtype. |
| [`api.types.is_unsigned_integer_dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_unsigned_integer_dtype.html#pandas.api.types.is_unsigned_integer_dtype "pandas.api.types.is_unsigned_integer_dtype")<br>(arr\_or\_dtype) | Check whether the provided array or dtype is of an unsigned integer dtype. |
| [`api.types.is_sparse`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_sparse.html#pandas.api.types.is_sparse "pandas.api.types.is_sparse")<br>(arr) | (DEPRECATED) Check whether an array-like is a 1-D pandas sparse array. |

#### Iterable introspection[#](https://pandas.pydata.org/docs/reference/arrays.html#iterable-introspection "Link to this heading")

|     |     |
| --- | --- |
| [`api.types.is_dict_like`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_dict_like.html#pandas.api.types.is_dict_like "pandas.api.types.is_dict_like")<br>(obj) | Check if the object is dict-like. |
| [`api.types.is_file_like`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_file_like.html#pandas.api.types.is_file_like "pandas.api.types.is_file_like")<br>(obj) | Check if the object is a file-like object. |
| [`api.types.is_list_like`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_list_like.html#pandas.api.types.is_list_like "pandas.api.types.is_list_like")<br>(obj\[, allow\_sets\]) | Check if the object is list-like. |
| [`api.types.is_named_tuple`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_named_tuple.html#pandas.api.types.is_named_tuple "pandas.api.types.is_named_tuple")<br>(obj) | Check if the object is a named tuple. |
| [`api.types.is_iterator`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_iterator.html#pandas.api.types.is_iterator "pandas.api.types.is_iterator")<br>(obj) | Check if the object is an iterator. |

#### Scalar introspection[#](https://pandas.pydata.org/docs/reference/arrays.html#scalar-introspection "Link to this heading")

|     |     |
| --- | --- |
| [`api.types.is_bool`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_bool.html#pandas.api.types.is_bool "pandas.api.types.is_bool")<br>(obj) | Return True if given object is boolean. |
| [`api.types.is_complex`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_complex.html#pandas.api.types.is_complex "pandas.api.types.is_complex")<br>(obj) | Return True if given object is complex. |
| [`api.types.is_float`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_float.html#pandas.api.types.is_float "pandas.api.types.is_float")<br>(obj) | Return True if given object is float. |
| [`api.types.is_hashable`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_hashable.html#pandas.api.types.is_hashable "pandas.api.types.is_hashable")<br>(obj\[, allow\_slice\]) | Return True if hash(obj) will succeed, False otherwise. |
| [`api.types.is_integer`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_integer.html#pandas.api.types.is_integer "pandas.api.types.is_integer")<br>(obj) | Return True if given object is integer. |
| [`api.types.is_number`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_number.html#pandas.api.types.is_number "pandas.api.types.is_number")<br>(obj) | Check if the object is a number. |
| [`api.types.is_re`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re.html#pandas.api.types.is_re "pandas.api.types.is_re")<br>(obj) | Check if the object is a regex pattern instance. |
| [`api.types.is_re_compilable`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_re_compilable.html#pandas.api.types.is_re_compilable "pandas.api.types.is_re_compilable")<br>(obj) | Check if the object can be compiled into a regex pattern instance. |
| [`api.types.is_scalar`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_scalar.html#pandas.api.types.is_scalar "pandas.api.types.is_scalar")<br>(val) | Return True if given object is scalar. |

On this page
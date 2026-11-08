[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.array.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.array.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.array.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.array.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.array.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.array.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.array.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.array.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.array.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.array.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.array.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.array.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.array.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.array.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.array[#](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas-array "Link to this heading")

====================================================================================================================

pandas.array(_data_, _dtype\=None_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/construction.py#L82-L450)
[#](https://pandas.pydata.org/docs/reference/api/pandas.array.html#pandas.array "Link to this definition")

Create an array.

This method constructs an array using pandas extension types when possible. If dtype is specified, it determines the type of array returned. Otherwise, pandas attempts to infer the appropriate dtype based on data.

Parameters:

**data**Sequence of objects

The scalars inside data should be instances of the scalar type for dtype. It’s expected that data represents a 1-dimensional array of data.

When data is an Index or Series, the underlying array will be extracted from data.

**dtype**str, np.dtype, or ExtensionDtype, optional

The dtype to use for the array. This may be a NumPy dtype or an extension type registered with pandas using [`pandas.api.extensions.register_extension_dtype()`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_extension_dtype.html#pandas.api.extensions.register_extension_dtype "pandas.api.extensions.register_extension_dtype")
.

If not specified, there are two possibilities:

1.  When data is a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    , [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
    , or `ExtensionArray`, the dtype will be taken from the data.
    
2.  Otherwise, pandas will attempt to infer the dtype from the data.
    

Note that when data is a NumPy array, `data.dtype` is _not_ used for inferring the array type. This is because NumPy cannot represent all the types of data that can be held in extension arrays.

Currently, pandas will infer an extension dtype for sequences of

| Scalar Type | Array Type |
| --- | --- |
| [`pandas.Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval") | [`pandas.arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray") |
| [`pandas.Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period") | [`pandas.arrays.PeriodArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "pandas.arrays.PeriodArray") |
| [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)") | [`pandas.arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray") |
| [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)") | [`pandas.arrays.TimedeltaArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas.arrays.TimedeltaArray "pandas.arrays.TimedeltaArray") |
| [`int`](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)") | [`pandas.arrays.IntegerArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas.arrays.IntegerArray "pandas.arrays.IntegerArray") |
| [`float`](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)") | [`pandas.arrays.FloatingArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#pandas.arrays.FloatingArray "pandas.arrays.FloatingArray") |
| [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)") | [`pandas.arrays.StringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas.arrays.StringArray "pandas.arrays.StringArray")<br> or [`pandas.arrays.ArrowStringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowStringArray.html#pandas.arrays.ArrowStringArray "pandas.arrays.ArrowStringArray") |
| [`bool`](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)") | [`pandas.arrays.BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray") |

The ExtensionArray created when the scalar type is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 is determined by `pd.options.mode.string_storage` if the dtype is not explicitly given.

For all other cases, NumPy’s usual inference rules will be used.

**copy**bool, default True

Whether to copy the data, even if not necessary. Depending on the type of data, creating the new array may require copying data, even if `copy=False`.

Returns:

ExtensionArray

The newly created array.

Raises:

ValueError

When data is not 1-dimensional.

See also

[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")

Construct a NumPy array.

[`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")

Construct a pandas Series.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

Construct a pandas Index.

[`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")

ExtensionArray wrapping a NumPy array.

[`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")

Extract the array stored within a Series.

Notes

Omitting the dtype argument means pandas will attempt to infer the best array type from the values in the data. As new array types are added by pandas and 3rd party libraries, the “best” array type may change. We recommend specifying dtype to ensure that

1.  the correct array type for the data is returned
    
2.  the returned array type doesn’t change as new extension types are added by pandas and third-party libraries
    

Additionally, if the underlying memory representation of the returned array matters, we recommend specifying the dtype as a concrete object rather than a string alias or allowing it to be inferred. For example, a future version of pandas or a 3rd-party library may include a dedicated ExtensionArray for string data. In this event, the following would no longer return a [`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")
 backed by a NumPy array.

\>>> pd.array(\["a", "b"\], dtype\=str)
<ArrowStringArray>
\['a', 'b'\]
Length: 2, dtype: str

Copy to clipboard

This would instead return the new ExtensionArray dedicated for string data. If you really need the new array to be backed by a NumPy array, specify that in the dtype.

\>>> pd.array(\["a", "b"\], dtype\=np.dtype("<U1"))
<NumpyExtensionArray>
\['a', 'b'\]
Length: 2, dtype: str32

Copy to clipboard

pandas converts entries of a multidimensional sequence (excluding NumPy arrays) to its string representation if the `dtype` is a string data type.

\>>> pd.array(\[\[1\], \[2\], \[3\]\], dtype\="str")
<ArrowStringArray>
\['\[1\]', '\[2\]', '\[3\]'\]
Length: 3, dtype: str

Copy to clipboard

Finally, Pandas has arrays that mostly overlap with NumPy

> *   [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")
>     
> *   [`arrays.TimedeltaArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.TimedeltaArray.html#pandas.arrays.TimedeltaArray "pandas.arrays.TimedeltaArray")
>     

When data with a `datetime64[ns]` or `timedelta64[ns]` dtype is passed, pandas will always return a `DatetimeArray` or `TimedeltaArray` rather than a `NumpyExtensionArray`. This is for symmetry with the case of timezone-aware data, which NumPy does not natively support.

\>>> pd.array(\["2015", "2016"\], dtype\="datetime64\[ns\]")
<DatetimeArray>
\['2015-01-01 00:00:00', '2016-01-01 00:00:00'\]
Length: 2, dtype: datetime64\[ns\]

Copy to clipboard

\>>> pd.array(\["1h", "2h"\], dtype\="timedelta64\[ns\]")
<TimedeltaArray>
\['0 days 01:00:00', '0 days 02:00:00'\]
Length: 2, dtype: timedelta64\[ns\]

Copy to clipboard

Examples

If a dtype is not specified, pandas will infer the best dtype from the values. See the description of dtype for the types pandas infers for.

\>>> pd.array(\[1, 2\])
<IntegerArray>
\[1, 2\]
Length: 2, dtype: Int64

Copy to clipboard

\>>> pd.array(\[1, 2, np.nan\])
<IntegerArray>
\[1, 2, <NA>\]
Length: 3, dtype: Int64

Copy to clipboard

\>>> pd.array(\[1.1, 2.2\])
<FloatingArray>
\[1.1, 2.2\]
Length: 2, dtype: Float64

Copy to clipboard

\>>> pd.array(\["a", None, "c"\])
<ArrowStringArray>
\['a', <NA>, 'c'\]
Length: 3, dtype: string

Copy to clipboard

\>>> with pd.option\_context("string\_storage", "python"):
...     arr \= pd.array(\["a", None, "c"\])
\>>> arr
<StringArray>
\['a', <NA>, 'c'\]
Length: 3, dtype: string

Copy to clipboard

\>>> pd.array(\[pd.Period("2000", freq\="D"), pd.Period("2000", freq\="D")\])
<PeriodArray>
\['2000-01-01', '2000-01-01'\]
Length: 2, dtype: period\[D\]

Copy to clipboard

You can use the string alias for dtype

\>>> pd.array(\["a", "b", "a"\], dtype\="category")
\['a', 'b', 'a'\]
Categories (2, str): \['a', 'b'\]

Copy to clipboard

Or specify the actual dtype

\>>> pd.array(
...     \["a", "b", "a"\], dtype\=pd.CategoricalDtype(\["a", "b", "c"\], ordered\=True)
... )
\['a', 'b', 'a'\]
Categories (3, str): \['a' < 'b' < 'c'\]

Copy to clipboard

If pandas does not infer a dedicated extension type a [`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")
 is returned.

\>>> pd.array(\[1 + 1j, 3 + 2j\])
<NumpyExtensionArray>
\[(1+1j), (3+2j)\]
Length: 2, dtype: complex128

Copy to clipboard

As mentioned in the “Notes” section, new extension types may be added in the future (by pandas or 3rd party libraries), causing the return value to no longer be a [`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")
. Specify the dtype as a NumPy dtype if you need to ensure there’s no future change in behavior.

\>>> pd.array(\[1, 2\], dtype\=np.dtype("int32"))
<NumpyExtensionArray>
\[1, 2\]
Length: 2, dtype: int32

Copy to clipboard

data must be 1-dimensional. A ValueError is raised when the input has the wrong dimensionality.

\>>> pd.array(1)
Traceback (most recent call last):
  ...
ValueError: Cannot pass scalar '1' to 'pandas.array'.

Copy to clipboard

On this page
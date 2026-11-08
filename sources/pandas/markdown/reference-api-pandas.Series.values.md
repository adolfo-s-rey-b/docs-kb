[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.values.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.values.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.values.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.values.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.values.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.values.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.values.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.values.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.values.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.values.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.values.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.values.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.values[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas-series-values "Link to this heading")

============================================================================================================================================

property Series.values[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L758-L861)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values "Link to this definition")

Return Series as ndarray or ndarray-like depending on the dtype.

Warning

We recommend using [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")
 or [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
, depending on whether you need a reference to the underlying data or a NumPy array. The return type of `.values` depends on the dtype: it is a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 for some dtypes (for example `int64` or `float64`) and an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 for others (for example `category`, nullable `Int64`, or string dtypes), which makes it harder to write code that works across dtypes. `.values` also converts timezone-aware datetimes to UTC and drops the timezone. [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")
 always returns the underlying array as an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
, and [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 always returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 and accepts `dtype`, `copy`, and `na_value` arguments to control the conversion.

Returns:

numpy.ndarray or ndarray-like

See also

[`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")

Reference to the underlying data.

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

A NumPy array representing the underlying data.

Examples

For a Series backed by a NumPy dtype such as `int64`, `.values` returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
:

\>>> pd.Series(\[1, 2, 3\]).values
array(\[1, 2, 3\])

Copy to clipboard

For extension dtypes such as the default string dtype or `category`, `.values` returns an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 instead, while [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 always returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
:

\>>> pd.Series(list("aabc")).values
<ArrowStringArray>
\['a', 'a', 'b', 'c'\]
Length: 4, dtype: str
\>>> pd.Series(list("aabc")).to\_numpy()
array(\['a', 'a', 'b', 'c'\], dtype=object)

Copy to clipboard

\>>> pd.Series(list("aabc")).astype("category").values
\['a', 'a', 'b', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

Timezone aware datetime data is converted to UTC and the timezone is dropped, while [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")
 preserves the timezone:

\>>> pd.Series(
...     pd.date\_range("20130101", periods\=3, tz\="US/Eastern")
... ).values
array(\['2013-01-01T05:00:00.000000',\
       '2013-01-02T05:00:00.000000',\
       '2013-01-03T05:00:00.000000'\], dtype='datetime64\[us\]')
\>>> pd.Series(pd.date\_range("20130101", periods\=3, tz\="US/Eastern")).array
<DatetimeArray>
\['2013-01-01 00:00:00-05:00', '2013-01-02 00:00:00-05:00',\
 '2013-01-03 00:00:00-05:00'\]
Length: 3, dtype: datetime64\[us, US/Eastern\]

Copy to clipboard

Deprecated since version 3.0.0: For [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype")
, [`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")
, and [`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype")
 dtypes, the behavior of `.values` returning a lossy or object-dtype result is deprecated. In a future version, `.values` will return the underlying ExtensionArray. Use [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 or [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array")
 instead.

On this page
[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DatetimeIndex.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DatetimeIndex.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DatetimeIndex.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DatetimeIndex.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DatetimeIndex.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DatetimeIndex.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DatetimeIndex.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DatetimeIndex.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DatetimeIndex.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DatetimeIndex.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DatetimeIndex.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DatetimeIndex.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.std[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html#pandas-datetimeindex-std "Link to this heading")

========================================================================================================================================================

DatetimeIndex.std(_axis\=None_, _dtype\=None_, _out\=None_, _ddof\=1_, _keepdims\=False_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L966-L1018)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html#pandas.DatetimeIndex.std "Link to this definition")

Return sample standard deviation over requested axis.

Normalized by N-1 by default. This can be changed using `ddof`.

Parameters:

**axis**int, optional

Axis for the function to be applied on.

**dtype**None

Unused; for compatibility with [`numpy.std()`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")
.

**out**None

Not supported; for compatibility with [`numpy.std()`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")
.

**ddof**int, default 1

Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

**keepdims**bool, default False

Not supported; for compatibility with [`numpy.std()`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "(in NumPy v2.5)")
.

**skipna**bool, default True

Exclude NA/null values.

Returns:

Timedelta

Standard deviation over requested axis.

See also

[`numpy.ndarray.std`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html#numpy.ndarray.std "(in NumPy v2.5)")

Returns the standard deviation of the array elements along given axis.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Return sample standard deviation over requested axis.

Examples

\>>> idx \= pd.date\_range("2001-01-01 00:00", periods\=3)
\>>> idx
DatetimeIndex(\['2001-01-01', '2001-01-02', '2001-01-03'\],
              dtype='datetime64\[us\]', freq='D')
\>>> idx.std()
Timedelta('1 days 00:00:00')

Copy to clipboard

On this page
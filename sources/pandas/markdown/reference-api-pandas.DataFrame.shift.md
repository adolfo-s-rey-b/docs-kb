[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.shift.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.shift.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.shift.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.shift.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.shift.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.shift.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.shift.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.shift.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.shift.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.shift.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.shift.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.shift.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.shift[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas-dataframe-shift "Link to this heading")

==================================================================================================================================================

DataFrame.shift(_periods\=1_, _freq\=None_, _axis\=0_, _fill\_value\=<no\_default>_, _suffix\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L7450-L7667)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift "Link to this definition")

Shift index by desired number of periods with an optional time freq.

When freq is not passed, shift the index without realigning the data. If freq is passed (in this case, the index must be date or datetime, or it will raise a NotImplementedError), the index will be increased using the periods and the freq. freq can be inferred when specified as “infer” as long as either freq or inferred\_freq attribute is set in the index.

Parameters:

**periods**int or Sequence

Number of periods to shift. Can be positive or negative. If an iterable of ints, the data will be shifted once by each int. This is equivalent to shifting by one value at a time and concatenating all resulting frames. The resulting columns will have the shift suffixed to their column names. For multiple periods, axis must not be 1.

**freq**DateOffset, tseries.offsets, timedelta, or str, optional

Offset to use from the tseries module or time rule (e.g. ‘EOM’). If freq is specified then the index values are shifted but the data is not realigned. That is, use freq if you would like to extend the index when shifting and preserve the original data. If freq is specified as “infer” then it will be inferred from the freq or inferred\_freq attributes of the index. If neither of those attributes exist, a ValueError is thrown.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Shift direction. For Series this parameter is unused and defaults to 0.

**fill\_value**object, optional

The scalar value to use for newly introduced missing values. the default depends on the dtype of self. For Boolean and numeric NumPy data types, `np.nan` is used. For datetime, timedelta, or period data, etc. [`NaT`](https://pandas.pydata.org/docs/reference/api/pandas.NaT.html#pandas.NaT "pandas.NaT")
 is used. For extension dtypes, `self.dtype.na_value` is used.

**suffix**str, optional

If str and periods is an iterable, this is added after the column name and before the shift value for each shifted column name.

Returns:

DataFrame

Copy of input object, shifted.

See also

[`Index.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#pandas.Index.shift "pandas.Index.shift")

Shift values of Index.

`DatetimeIndex.shift`

Shift values of DatetimeIndex.

`PeriodIndex.shift`

Shift values of PeriodIndex.

Examples

\>>> df \= pd.DataFrame(
...     \[\[10, 13, 17\], \[20, 23, 27\], \[15, 18, 22\], \[30, 33, 37\], \[45, 48, 52\]\],
...     columns\=\["Col1", "Col2", "Col3"\],
...     index\=pd.date\_range("2020-01-01", "2020-01-05"),
... )
\>>> df
            Col1  Col2  Col3
2020-01-01    10    13    17
2020-01-02    20    23    27
2020-01-03    15    18    22
2020-01-04    30    33    37
2020-01-05    45    48    52

Copy to clipboard

\>>> df.shift(periods\=3)
            Col1  Col2  Col3
2020-01-01   NaN   NaN   NaN
2020-01-02   NaN   NaN   NaN
2020-01-03   NaN   NaN   NaN
2020-01-04  10.0  13.0  17.0
2020-01-05  20.0  23.0  27.0

Copy to clipboard

\>>> df.shift(periods\=1, axis\="columns")
            Col1  Col2  Col3
2020-01-01   NaN    10    13
2020-01-02   NaN    20    23
2020-01-03   NaN    15    18
2020-01-04   NaN    30    33
2020-01-05   NaN    45    48

Copy to clipboard

\>>> df.shift(periods\=3, fill\_value\=0)
            Col1  Col2  Col3
2020-01-01     0     0     0
2020-01-02     0     0     0
2020-01-03     0     0     0
2020-01-04    10    13    17
2020-01-05    20    23    27

Copy to clipboard

\>>> df.shift(periods\=3, freq\="D")
            Col1  Col2  Col3
2020-01-04    10    13    17
2020-01-05    20    23    27
2020-01-06    15    18    22
2020-01-07    30    33    37
2020-01-08    45    48    52

Copy to clipboard

\>>> df.shift(periods\=3, freq\="infer")
            Col1  Col2  Col3
2020-01-04    10    13    17
2020-01-05    20    23    27
2020-01-06    15    18    22
2020-01-07    30    33    37
2020-01-08    45    48    52

Copy to clipboard

\>>> df\["Col1"\].shift(periods\=\[0, 1, 2\])
            Col1\_0  Col1\_1  Col1\_2
2020-01-01      10     NaN     NaN
2020-01-02      20    10.0     NaN
2020-01-03      15    20.0    10.0
2020-01-04      30    15.0    20.0
2020-01-05      45    30.0    15.0

Copy to clipboard

On this page
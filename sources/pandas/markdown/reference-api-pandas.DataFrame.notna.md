[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.notna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.notna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.notna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.notna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.notna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.notna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.notna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.notna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.notna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.notna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.notna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.notna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.notna[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas-dataframe-notna "Link to this heading")

==================================================================================================================================================

DataFrame.notna()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L8415-L8484)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "Link to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings `''` or `numpy.inf` are not considered NA values. NA values, such as None or `numpy.NaN`, get mapped to False values.

Returns:

Series/DataFrame

Mask of bool values for each element in Series/DataFrame that indicates whether an element is not an NA value.

See also

[`Series.notnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notnull.html#pandas.Series.notnull "pandas.Series.notnull")

Alias of notna.

[`DataFrame.notnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notnull.html#pandas.DataFrame.notnull "pandas.DataFrame.notnull")

Alias of notna.

[`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")

Boolean inverse of notna.

[`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")

Boolean inverse of notna.

[`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")

Omit axes labels with missing values.

[`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")

Omit axes labels with missing values.

[`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")

Top-level notna.

Examples

Show which entries in a DataFrame are not NA.

\>>> df \= pd.DataFrame(
...     dict(
...         age\=\[5, 6, np.nan\],
...         born\=\[\
...             pd.NaT,\
...             pd.Timestamp("1939-05-27"),\
...             pd.Timestamp("1940-04-25"),\
...         \],
...         name\=\["Alfred", "Batman", ""\],
...         toy\=\[None, "Batmobile", "Joker"\],
...     )
... )
\>>> df
   age       born    name        toy
0  5.0        NaT  Alfred        NaN
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

Copy to clipboard

\>>> df.notna()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

Copy to clipboard

Show which entries in a Series are not NA.

\>>> ser \= pd.Series(\[5, 6, np.nan\])
\>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

Copy to clipboard

\>>> ser.notna()
0     True
1     True
2    False
dtype: bool

Copy to clipboard

On this page
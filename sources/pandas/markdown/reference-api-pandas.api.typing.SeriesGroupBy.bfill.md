[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.bfill[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html#pandas-api-typing-seriesgroupby-bfill "Link to this heading")

===============================================================================================================================================================================================

SeriesGroupBy.bfill(_limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4188-L4270)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html#pandas.api.typing.SeriesGroupBy.bfill "Link to this definition")

Backward fill the values.

Fill missing values within each group by propagating the next valid observation backward.

Parameters:

**limit**int, optional

Limit of how many values to fill.

Returns:

Series or DataFrame

Object with missing values filled.

See also

`Series.bfill`

Backward fill the missing values in the dataset.

`DataFrame.bfill`

Backward fill the missing values in the dataset.

`Series.fillna`

Fill NaN values of a Series.

`DataFrame.fillna`

Fill NaN values of a DataFrame.

Examples

With Series:

\>>> index \= \["Falcon", "Falcon", "Parrot", "Parrot", "Parrot"\]
\>>> s \= pd.Series(\[None, 1, None, None, 3\], index\=index)
\>>> s
Falcon    NaN
Falcon    1.0
Parrot    NaN
Parrot    NaN
Parrot    3.0
dtype: float64
\>>> s.groupby(level\=0).bfill()
Falcon    1.0
Falcon    1.0
Parrot    3.0
Parrot    3.0
Parrot    3.0
dtype: float64
\>>> s.groupby(level\=0).bfill(limit\=1)
Falcon    1.0
Falcon    1.0
Parrot    NaN
Parrot    3.0
Parrot    3.0
dtype: float64

Copy to clipboard

With DataFrame:

\>>> df \= pd.DataFrame(
...     {"A": \[1, None, None, None, 4\], "B": \[None, None, 5, None, 7\]},
...     index\=index,
... )
\>>> df
          A         B
Falcon  1.0       NaN
Falcon  NaN       NaN
Parrot  NaN       5.0
Parrot  NaN       NaN
Parrot  4.0       7.0
\>>> df.groupby(level\=0).bfill()
          A         B
Falcon  1.0       NaN
Falcon  NaN       NaN
Parrot  4.0       5.0
Parrot  4.0       7.0
Parrot  4.0       7.0
\>>> df.groupby(level\=0).bfill(limit\=1)
          A         B
Falcon  1.0       NaN
Falcon  NaN       NaN
Parrot  NaN       5.0
Parrot  4.0       7.0
Parrot  4.0       7.0

Copy to clipboard

On this page
[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.indexers.VariableOffsetWindowIndexer[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html#pandas-api-indexers-variableoffsetwindowindexer "Link to this heading")

=============================================================================================================================================================================================================================

class pandas.api.indexers.VariableOffsetWindowIndexer(_index\_array\=None_, _window\_size\=0_, _index\=None_, _offset\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexers/objects.py#L215-L392)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html#pandas.api.indexers.VariableOffsetWindowIndexer "Link to this definition")

Calculate window boundaries based on a non-fixed offset such as a BusinessDay.

Unlike the default fixed-size window, this indexer uses a `DateOffset` to determine variable-width window boundaries based on the datetime index of the data.

Parameters:

**index\_array**np.ndarray, default 0

Array-like structure specifying the indices for data points. This parameter is currently not used.

**window\_size**int, optional, default 0

Specifies the number of data points in each window. This parameter is currently not used.

**index**DatetimeIndex, optional

`DatetimeIndex` of the labels of each observation.

**offset**BaseOffset, optional

`DateOffset` representing the size of the window.

**\*\*kwargs**

Additional keyword arguments passed to the parent class `BaseIndexer`.

See also

`api.indexers.BaseIndexer`

Base class for all indexers.

`DataFrame.rolling`

Rolling window calculations on DataFrames.

`offsets`

Module providing various time offset classes.

Examples

\>>> from pandas.api.indexers import VariableOffsetWindowIndexer
\>>> df \= pd.DataFrame(range(10), index\=pd.date\_range("2020", periods\=10))
\>>> offset \= pd.offsets.BDay(1)
\>>> indexer \= VariableOffsetWindowIndexer(index\=df.index, offset\=offset)
\>>> df
            0
2020-01-01  0
2020-01-02  1
2020-01-03  2
2020-01-04  3
2020-01-05  4
2020-01-06  5
2020-01-07  6
2020-01-08  7
2020-01-09  8
2020-01-10  9
\>>> df.rolling(indexer).sum()
               0
2020-01-01   0.0
2020-01-02   1.0
2020-01-03   2.0
2020-01-04   3.0
2020-01-05   7.0
2020-01-06  12.0
2020-01-07   6.0
2020-01-08   7.0
2020-01-09   8.0
2020-01-10   9.0

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `get_window_bounds`(\[num\_values, min\_periods, ...\]) | Computes the bounds of a window. |

On this page
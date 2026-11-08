[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.indexers.FixedForwardWindowIndexer[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html#pandas-api-indexers-fixedforwardwindowindexer "Link to this heading")

=======================================================================================================================================================================================================================

class pandas.api.indexers.FixedForwardWindowIndexer(_index\_array\=None_, _window\_size\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexers/objects.py#L433-L526)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html#pandas.api.indexers.FixedForwardWindowIndexer "Link to this definition")

Creates window boundaries for fixed-length windows that include the current row.

This indexer produces forward-looking windows, where each window starts at the current row and extends `window_size` rows ahead, unlike the default backward-looking behavior of `DataFrame.rolling()`.

Parameters:

**index\_array**np.ndarray, default None

Array-like structure representing the indices for the data points. If None, the default indices are assumed. This can be useful for handling non-uniform indices in data, such as in time series with irregular timestamps.

**window\_size**int, default 0

Size of the moving window. This is the number of observations used for calculating the statistic. The default is to consider all observations within the window.

**\*\*kwargs**

Additional keyword arguments passed to the subclass’s methods.

See also

`DataFrame.rolling`

Provides rolling window calculations.

`api.indexers.VariableWindowIndexer`

Calculate window bounds based on variable-sized windows.

Examples

\>>> df \= pd.DataFrame({"B": \[0, 1, 2, np.nan, 4\]})
\>>> df
     B
0  0.0
1  1.0
2  2.0
3  NaN
4  4.0

Copy to clipboard

\>>> indexer \= pd.api.indexers.FixedForwardWindowIndexer(window\_size\=2)
\>>> df.rolling(window\=indexer, min\_periods\=1).sum()
     B
0  1.0
1  3.0
2  2.0
3  4.0
4  4.0

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `get_window_bounds`(\[num\_values, min\_periods, ...\]) | Computes the bounds of a window. |

On this page
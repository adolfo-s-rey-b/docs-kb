[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.BaseIndexer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.indexers.BaseIndexer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.BaseIndexer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.indexers.BaseIndexer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.indexers.BaseIndexer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.indexers.BaseIndexer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.indexers.BaseIndexer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.indexers.BaseIndexer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.indexers.BaseIndexer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.indexers.BaseIndexer[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.BaseIndexer.html#pandas-api-indexers-baseindexer "Link to this heading")

=============================================================================================================================================================================

class pandas.api.indexers.BaseIndexer(_index\_array\=None_, _window\_size\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexers/objects.py#L25-L110)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.BaseIndexer.html#pandas.api.indexers.BaseIndexer "Link to this definition")

Base class for window bounds calculations.

Subclasses should implement `get_window_bounds` to define custom windowing logic for use with `DataFrame.rolling()` or `Series.rolling()`.

Parameters:

**index\_array**np.ndarray, default None

Array-like structure representing the indices for the data points. If None, the default indices are assumed. This can be useful for handling non-uniform indices in data, such as in time series with irregular timestamps.

**window\_size**int, default 0

Size of the moving window. This is the number of observations used for calculating the statistic. The default is to consider all observations within the window.

**\*\*kwargs**

Additional keyword arguments passed to the subclass’s methods.

See also

`DataFrame.rolling`

Provides rolling window calculations on dataframe.

`Series.rolling`

Provides rolling window calculations on series.

Examples

\>>> from pandas.api.indexers import BaseIndexer
\>>> class CustomIndexer(BaseIndexer):
...     def get\_window\_bounds(self, num\_values, min\_periods, center, closed, step):
...         start \= np.arange(num\_values, dtype\=np.int64)
...         end \= np.arange(num\_values, dtype\=np.int64) + self.window\_size
...         return start, end
\>>> df \= pd.DataFrame({"values": range(5)})
\>>> indexer \= CustomIndexer(window\_size\=2)
\>>> df.rolling(indexer).sum()
    values
0   1.0
1   3.0
2   5.0
3   7.0
4   4.0

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `get_window_bounds`(\[num\_values, min\_periods, ...\]) | Computes the bounds of a window. |

On this page
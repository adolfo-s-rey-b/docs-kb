[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.from_arrow.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.from_arrow.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.from_arrow.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.from_arrow.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.from_arrow.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.from_arrow.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.from_arrow.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.from_arrow.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.from_arrow.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.from_arrow.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.from_arrow.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.from_arrow.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.from\_arrow[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#pandas-series-from-arrow "Link to this heading")

=========================================================================================================================================================

classmethod Series.from\_arrow(_data_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2033-L2102)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#pandas.Series.from_arrow "Link to this definition")

Construct a Series from an array-like Arrow object.

This function accepts any Arrow-compatible array-like object implementing the [Arrow PyCapsule Protocol](https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html)
 (i.e. having an `__arrow_c_array__` or `__arrow_c_stream__` method).

This function currently relies on `pyarrow` to convert the object in Arrow format to pandas.

Added in version 3.0.

Parameters:

**data**pyarrow.Array or Arrow-compatible object

Any array-like object implementing the Arrow PyCapsule Protocol (i.e. has an `__arrow_c_array__` or `__arrow_c_stream__` method).

Returns:

Series

See also

[`DataFrame.from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#pandas.DataFrame.from_arrow "pandas.DataFrame.from_arrow")

Construct a DataFrame from an Arrow object.

Examples

\>>> import pyarrow as pa
\>>> arrow\_array \= pa.array(\[1, 2, 3\])
\>>> pd.Series.from\_arrow(arrow\_array)
0    1
1    2
2    3
dtype: int64

Copy to clipboard

On this page
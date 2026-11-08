[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.from_range.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.RangeIndex.from\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.from_range.html#pandas-rangeindex-from-range "Link to this heading")

=====================================================================================================================================================================

classmethod RangeIndex.from\_range(_data_, _name\=None_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/range.py#L199-L245)
[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.from_range.html#pandas.RangeIndex.from_range "Link to this definition")

Create [`pandas.RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 from a `range` object.

This method provides a way to create a [`pandas.RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 directly from a Python `range` object. The resulting [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 will have the same start, stop, and step values as the input `range` object. It is particularly useful for constructing indices in an efficient and memory-friendly manner.

Parameters:

**data**range

The range object to be converted into a RangeIndex.

**name**str, default None

Name to be stored in the index.

**dtype**Dtype or None

Data type for the RangeIndex. If None, the default integer type will be used.

Returns:

RangeIndex

See also

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")

Immutable Index implementing a monotonic integer range.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

Immutable sequence used for indexing and alignment.

Examples

\>>> pd.RangeIndex.from\_range(range(5))
RangeIndex(start=0, stop=5, step=1)

Copy to clipboard

\>>> pd.RangeIndex.from\_range(range(2, \-10, \-3))
RangeIndex(start=2, stop=-10, step=-3)

Copy to clipboard

On this page
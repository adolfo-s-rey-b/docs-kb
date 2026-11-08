[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.RangeIndex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.RangeIndex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.RangeIndex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.RangeIndex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.RangeIndex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.RangeIndex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.RangeIndex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.RangeIndex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.RangeIndex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.RangeIndex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.RangeIndex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.RangeIndex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.RangeIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas-rangeindex "Link to this heading")

===================================================================================================================================

class pandas.RangeIndex(_start\=None_, _stop\=None_, _step\=None_, _dtype\=None_, _copy\=False_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/range.py#L89-L1707)
[#](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "Link to this definition")

Immutable Index implementing a monotonic integer range.

RangeIndex is a memory-saving special case of an Index limited to representing monotonic ranges with a 64-bit dtype. Using RangeIndex may in some instances improve computing speed.

This is the default index type used by DataFrame and Series when no explicit index is provided by the user.

Parameters:

**start**int, range, or other RangeIndex instance, default None

If int and “stop” is not given, interpreted as “stop” instead.

**stop**int, default None

The end value of the range (exclusive).

**step**int, default None

The step size of the range.

**dtype**np.int64, default None

Unused, accepted for homogeneity with other index types.

**copy**bool, default False

Unused, accepted for homogeneity with other index types.

**name**object, optional

Name to be stored in the index.

Attributes

|     |     |
| --- | --- |
| [`start`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas.RangeIndex.start "pandas.RangeIndex.start") | The value of the start parameter (`0` if this was not supplied). |
| [`stop`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas.RangeIndex.stop "pandas.RangeIndex.stop") | The value of the stop parameter. |
| [`step`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas.RangeIndex.step "pandas.RangeIndex.step") | The value of the step parameter (`1` if this was not supplied). |

Methods

|     |     |
| --- | --- |
| [`from_range`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.from_range.html#pandas.RangeIndex.from_range "pandas.RangeIndex.from_range")<br>(data\[, name, dtype\]) | Create [`pandas.RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")<br> from a `range` object. |

See also

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

Examples

\>>> list(pd.RangeIndex(5))
\[0, 1, 2, 3, 4\]

Copy to clipboard

\>>> list(pd.RangeIndex(\-2, 4))
\[-2, -1, 0, 1, 2, 3\]

Copy to clipboard

\>>> list(pd.RangeIndex(0, 10, 2))
\[0, 2, 4, 6, 8\]

Copy to clipboard

\>>> list(pd.RangeIndex(2, \-10, \-3))
\[2, -1, -4, -7\]

Copy to clipboard

\>>> list(pd.RangeIndex(0))
\[\]

Copy to clipboard

\>>> list(pd.RangeIndex(1, 0))
\[\]

Copy to clipboard

On this page
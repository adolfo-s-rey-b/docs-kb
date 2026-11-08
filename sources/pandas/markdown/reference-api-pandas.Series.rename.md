[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.rename.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.rename.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.rename.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.rename.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.rename.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.rename.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.rename.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.rename.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.rename.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.rename.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.rename.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.rename.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.rename[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas-series-rename "Link to this heading")

============================================================================================================================================

Series.rename(_index\=None_, _\*_, _axis\=None_, _copy\=<no\_default>_, _inplace\=<no\_default>_, _level\=None_, _errors\='ignore'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5625-L5738)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "Link to this definition")

Alter Series index labels or name.

Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series will be left as-is. Extra labels listed don’t throw an error.

Alternatively, change `Series.name` with a scalar value.

See the [user guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename)
 for more.

Parameters:

**index**scalar, hashable sequence, dict-like or function optional

Functions or dict-like are transformations to apply to the index. Scalar or hashable sequence-like will alter the `Series.name` attribute.

**axis**{0 or ‘index’}

Unused. Parameter needed for compatibility with DataFrame.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**inplace**bool, default False

Whether to return a new Series. If True the value of copy is ignored.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**level**int or level name, default None

In case of MultiIndex, only rename labels in the specified level.

**errors**{‘ignore’, ‘raise’}, default ‘ignore’

If ‘raise’, raise KeyError when a dict-like mapper or index contains labels that are not present in the index being transformed. If ‘ignore’, existing keys will be renamed and extra keys will be ignored.

Returns:

Series

A shallow copy with index labels or name altered, or the same object if `inplace=True` and index is not a dict or callable else None.

See also

[`DataFrame.rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")

Corresponding DataFrame method.

[`Series.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis "pandas.Series.rename_axis")

Set the name of the axis.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s
0    1
1    2
2    3
dtype: int64
\>>> s.rename("my\_name")  \# scalar, changes Series.name
0    1
1    2
2    3
Name: my\_name, dtype: int64
\>>> s.rename(lambda x: x\*\*2)  \# function, changes labels
0    1
1    2
4    3
dtype: int64
\>>> s.rename({1: 3, 2: 5})  \# mapping, changes labels
0    1
3    2
5    3
dtype: int64

Copy to clipboard

On this page
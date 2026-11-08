[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.rename.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.rename.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.rename.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.rename.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.rename.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.rename.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.rename.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.rename.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.rename.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.rename.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.rename.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.rename.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rename[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas-dataframe-rename "Link to this heading")

=====================================================================================================================================================

DataFrame.rename(_mapper\=None_, _\*_, _index\=None_, _columns\=None_, _axis\=None_, _copy\=<no\_default>_, _inplace\=<no\_default>_, _level\=None_, _errors\='ignore'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L7026-L7175)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "Link to this definition")

Rename columns or index labels.

Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series will be left as-is. Extra labels listed don’t throw an error.

See the [user guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename)
 for more.

Parameters:

**mapper**dict-like or function

Dict-like or function transformations to apply to that axis’ values. Use either `mapper` and `axis` to specify the axis to target with `mapper`, or `index` and `columns`.

**index**dict-like or function

Alternative to specifying axis (`mapper, axis=0` is equivalent to `index=mapper`).

**columns**dict-like or function

Alternative to specifying axis (`mapper, axis=1` is equivalent to `columns=mapper`).

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Axis to target with `mapper`. Can be either the axis name (‘index’, ‘columns’) or number (0, 1). The default is ‘index’.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**inplace**bool, default False

Whether to modify the DataFrame rather than creating a new one. If True then value of copy is ignored.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**level**int or level name, default None

In case of a MultiIndex, only rename labels in the specified level.

**errors**{‘ignore’, ‘raise’}, default ‘ignore’

If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If ‘ignore’, existing keys will be renamed and extra keys will be ignored.

Returns:

DataFrame or None

DataFrame with the renamed axis labels or None if `inplace=True`.

Raises:

KeyError

If any of the labels is not found in the selected axis and “errors=’raise’”.

See also

[`DataFrame.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "pandas.DataFrame.rename_axis")

Set the name of the axis.

Examples

`DataFrame.rename` supports two calling conventions

*   `(index=index_mapper, columns=columns_mapper, ...)`
    
*   `(mapper, axis={'index', 'columns'}, ...)`
    

We _highly_ recommend using keyword arguments to clarify your intent.

Rename columns using a mapping:

\>>> df \= pd.DataFrame({"A": \[1, 2, 3\], "B": \[4, 5, 6\]})
\>>> df.rename(columns\={"A": "a", "B": "c"})
   a  c
0  1  4
1  2  5
2  3  6

Copy to clipboard

Rename index using a mapping:

\>>> df.rename(index\={0: "x", 1: "y", 2: "z"})
   A  B
x  1  4
y  2  5
z  3  6

Copy to clipboard

Cast index labels to a different type:

\>>> df.index
RangeIndex(start=0, stop=3, step=1)
\>>> df.rename(index\=str).index
Index(\['0', '1', '2'\], dtype='str')

Copy to clipboard

\>>> df.rename(columns\={"A": "a", "B": "b", "C": "c"}, errors\="raise")
Traceback (most recent call last):
KeyError: \['C'\] not found in axis

Copy to clipboard

Using axis-style parameters:

\>>> df.rename(str.lower, axis\="columns")
   a  b
0  1  4
1  2  5
2  3  6

Copy to clipboard

\>>> df.rename({1: 2, 2: 4}, axis\="index")
   A  B
0  1  4
2  2  5
4  3  6

Copy to clipboard

On this page
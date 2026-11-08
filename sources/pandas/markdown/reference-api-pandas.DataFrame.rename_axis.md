[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.rename_axis.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.rename_axis.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.rename_axis.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.rename_axis.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.rename_axis.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.rename_axis.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.rename_axis.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.rename_axis.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.rename_axis.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.rename_axis.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.rename_axis.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.rename_axis.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rename\_axis[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas-dataframe-rename-axis "Link to this heading")

=====================================================================================================================================================================

DataFrame.rename\_axis(_mapper\=<no\_default>_, _\*_, _index\=<no\_default>_, _columns\=<no\_default>_, _axis\=0_, _copy\=<no\_default>_, _inplace\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L7213-L7360)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "Link to this definition")

Set the name of the axis for the index or columns.

This method is useful for labeling the axes in a MultiIndex or for providing descriptive names to axes.

Parameters:

**mapper**scalar, list-like, optional

Value to set the axis name attribute.

Use either `mapper` and `axis` to specify the axis to target with `mapper`, or `index` and/or `columns`.

**index**scalar, list-like, dict-like or function, optional

A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.

**columns**scalar, list-like, dict-like or function, optional

A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to rename.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**inplace**bool, default False

Modifies the object directly, instead of creating a new Series or DataFrame.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

Returns:

DataFrame, or None

The same type as the caller or None if `inplace=True`.

See also

[`Series.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename")

Alter Series index labels or name.

[`DataFrame.rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")

Alter DataFrame index labels or name.

[`Index.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")

Set new names on index.

Notes

`DataFrame.rename_axis` supports two calling conventions

*   `(index=index_mapper, columns=columns_mapper, ...)`
    
*   `(mapper, axis={'index', 'columns'}, ...)`
    

The first calling convention will only modify the names of the index and/or the names of the Index object that is the columns. In this case, the parameter `copy` is ignored.

The second calling convention will modify the names of the corresponding index if mapper is a list or a scalar. However, if mapper is dict-like or a function, it will use the deprecated behavior of modifying the axis _labels_.

We _highly_ recommend using keyword arguments to clarify your intent.

Examples

**DataFrame**

\>>> df \= pd.DataFrame(
...     {"num\_legs": \[4, 4, 2\], "num\_arms": \[0, 0, 2\]}, \["dog", "cat", "monkey"\]
... )
\>>> df
        num\_legs  num\_arms
dog            4         0
cat            4         0
monkey         2         2
\>>> df \= df.rename\_axis("animal")
\>>> df
        num\_legs  num\_arms
animal
dog            4         0
cat            4         0
monkey         2         2
\>>> df \= df.rename\_axis("limbs", axis\="columns")
\>>> df
limbs   num\_legs  num\_arms
animal
dog            4         0
cat            4         0
monkey         2         2

Copy to clipboard

**MultiIndex**

\>>> df.index \= pd.MultiIndex.from\_product(
...     \[\["mammal"\], \["dog", "cat", "monkey"\]\], names\=\["type", "name"\]
... )
\>>> df
limbs          num\_legs  num\_arms
type   name
mammal dog            4         0
       cat            4         0
       monkey         2         2

Copy to clipboard

\>>> df.rename\_axis(index\={"type": "class"})
limbs          num\_legs  num\_arms
class  name
mammal dog            4         0
       cat            4         0
       monkey         2         2

Copy to clipboard

\>>> df.rename\_axis(columns\=str.upper)
LIMBS          num\_legs  num\_arms
type   name
mammal dog            4         0
       cat            4         0
       monkey         2         2

Copy to clipboard

On this page
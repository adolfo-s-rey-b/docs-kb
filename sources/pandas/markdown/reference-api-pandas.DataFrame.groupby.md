[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.groupby.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.groupby.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.groupby.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.groupby.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.groupby.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.groupby.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.groupby.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.groupby.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.groupby.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.groupby.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.groupby.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.groupby.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.groupby[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas-dataframe-groupby "Link to this heading")

========================================================================================================================================================

DataFrame.groupby(_by\=None_, _level\=None_, _\*_, _as\_index\=True_, _sort\=True_, _group\_keys\=True_, _observed\=True_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L13563-L13797)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "Link to this definition")

Group DataFrame using a mapper or by a Series of columns.

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.

Parameters:

**by**mapping, function, label, pd.Grouper or list of such

Used to determine the groups for the groupby. If `by` is a function, it’s called on each value of the object’s index. If a dict or Series is passed, the Series or dict VALUES will be used to determine the groups (the Series’ values are first aligned; see `.align()` method). If a list or ndarray of length equal to the number of rows is passed (see the [groupby user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups)
), the values are used as-is to determine the groups. A label or list of labels may be passed to group by the columns in `self`. Notice that a tuple is interpreted as a (single) key.

**level**int, level name, or sequence of such, default None

If the axis is a MultiIndex (hierarchical), group by a particular level or levels. Do not specify both `by` and `level`.

**as\_index**bool, default True

Return object with group labels as the index. Only relevant for DataFrame input. as\_index=False is effectively “SQL-style” grouped output. This argument has no effect on filtrations (see the [filtrations in the user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration)
), such as `head()`, `tail()`, `nth()` and in transformations (see the [transformations in the user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation)
).

**sort**bool, default True

Sort group keys. Get better performance by turning this off. Note this does not influence the order of observations within each group. Groupby preserves the order of rows within each group. If False, the groups will appear in the same order as they did in the original DataFrame. This argument has no effect on filtrations (see the [filtrations in the user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration)
), such as `head()`, `tail()`, `nth()` and in transformations (see the [transformations in the user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation)
).

Changed in version 2.0.0: Specifying `sort=False` with an ordered categorical grouper will no longer sort the values.

**group\_keys**bool, default True

When calling apply and the `by` argument produces a like-indexed (i.e. [a transform](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
) result, add group keys to index to identify pieces. By default group keys are not included when the result’s index (and column) labels match the inputs, and are included otherwise.

Changed in version 2.0.0: `group_keys` now defaults to `True`.

**observed**bool, default True

This only applies if any of the groupers are Categoricals. If True: only show observed values for categorical groupers. If False: show all values for categorical groupers.

Changed in version 3.0.0: The default value is now `True`.

**dropna**bool, default True

If True, and if group keys contain NA values, NA values together with row/column will be dropped. If False, NA values will also be treated as the key in groups.

Returns:

pandas.api.typing.DataFrameGroupBy

Returns a groupby object that contains information about the groups.

See also

[`resample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample "pandas.DataFrame.resample")

Convenience method for frequency conversion and resampling of time series.

Notes

See the [user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html)
 for more detailed usage and examples, including splitting an object into groups, iterating through groups, selecting a group, aggregation, and more.

The implementation of groupby is hash-based, meaning in particular that objects that compare as equal will be considered to be in the same group. An exception to this is that pandas has special handling of NA values: any NA values will be collapsed to a single group, regardless of how they compare. See the user guide linked above for more details.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "Animal": \["Falcon", "Falcon", "Parrot", "Parrot"\],
...         "Max Speed": \[380.0, 370.0, 24.0, 26.0\],
...     }
... )
\>>> df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0
\>>> df.groupby(\["Animal"\]).mean()
        Max Speed
Animal
Falcon      375.0
Parrot       25.0

Copy to clipboard

**Hierarchical Indexes**

We can groupby different levels of a hierarchical index using the level parameter:

\>>> arrays \= \[\
...     \["Falcon", "Falcon", "Parrot", "Parrot"\],\
...     \["Captive", "Wild", "Captive", "Wild"\],\
... \]
\>>> index \= pd.MultiIndex.from\_arrays(arrays, names\=("Animal", "Type"))
\>>> df \= pd.DataFrame({"Max Speed": \[390.0, 350.0, 30.0, 20.0\]}, index\=index)
\>>> df
                Max Speed
Animal Type
Falcon Captive      390.0
       Wild         350.0
Parrot Captive       30.0
       Wild          20.0
\>>> df.groupby(level\=0).mean()
        Max Speed
Animal
Falcon      370.0
Parrot       25.0
\>>> df.groupby(level\="Type").mean()
         Max Speed
Type
Captive      210.0
Wild         185.0

Copy to clipboard

We can also choose to include NA in group keys or not by setting dropna parameter, the default setting is True.

\>>> arr \= \[\[1, 2, 3\], \[1, None, 4\], \[2, 1, 3\], \[1, 2, 2\]\]
\>>> df \= pd.DataFrame(arr, columns\=\["a", "b", "c"\])

Copy to clipboard

\>>> df.groupby(by\=\["b"\]).sum()
    a   c
b
1.0 2   3
2.0 2   5

Copy to clipboard

\>>> df.groupby(by\=\["b"\], dropna\=False).sum()
    a   c
b
1.0 2   3
2.0 2   5
NaN 1   4

Copy to clipboard

\>>> arr \= \[\["a", 12, 12\], \[None, 12.3, 33.0\], \["b", 12.3, 123\], \["a", 1, 1\]\]
\>>> df \= pd.DataFrame(arr, columns\=\["a", "b", "c"\])

Copy to clipboard

\>>> df.groupby(by\="a").sum()
    b     c
a
a   13.0   13.0
b   12.3  123.0

Copy to clipboard

\>>> df.groupby(by\="a", dropna\=False).sum()
    b     c
a
a   13.0   13.0
b   12.3  123.0
NaN 12.3   33.0

Copy to clipboard

When using `.apply()`, use `group_keys` to include or exclude the group keys. The `group_keys` argument defaults to `True` (include).

\>>> df \= pd.DataFrame(
...     {
...         "Animal": \["Falcon", "Falcon", "Parrot", "Parrot"\],
...         "Max Speed": \[380.0, 370.0, 24.0, 26.0\],
...     }
... )
\>>> df.groupby("Animal", group\_keys\=True)\[\["Max Speed"\]\].apply(lambda x: x)
          Max Speed
Animal
Falcon 0      380.0
       1      370.0
Parrot 2       24.0
       3       26.0

Copy to clipboard

\>>> df.groupby("Animal", group\_keys\=False)\[\["Max Speed"\]\].apply(lambda x: x)
   Max Speed
0      380.0
1      370.0
2       24.0
3       26.0

Copy to clipboard

On this page
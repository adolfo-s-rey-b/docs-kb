[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.groupby.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.groupby.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.groupby.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.groupby.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.groupby.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.groupby.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.groupby.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.groupby.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.groupby.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.groupby.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.groupby.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.groupby.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.groupby[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas-series-groupby "Link to this heading")

===============================================================================================================================================

Series.groupby(_by\=None_, _level\=None_, _\*_, _as\_index\=True_, _sort\=True_, _group\_keys\=True_, _observed\=True_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L2119-L2352)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas.Series.groupby "Link to this definition")

Group Series using a mapper or by a Series of columns.

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.

Parameters:

**by**mapping, function, label, pd.Grouper or list of such

Used to determine the groups for the groupby. If `by` is a function, it’s called on each value of the object’s index. If a dict or Series is passed, the Series or dict VALUES will be used to determine the groups (the Series’ values are first aligned; see `.align()` method). If a list or ndarray of the same length as the Series is passed (see the [groupby user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups)
), the values are used as-is to determine the groups. An index level name may also be passed to group by a level of the Series’ index. Notice that a tuple is interpreted as a (single) key.

**level**int, level name, or sequence of such, default None

If the axis is a MultiIndex (hierarchical), group by a particular level or levels. Do not specify both `by` and `level`.

**as\_index**bool, default True

Return object with group labels as the index. This argument is retained for compatibility with [`DataFrame.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
 and has no effect on Series.

**sort**bool, default True

Sort group keys. Get better performance by turning this off. Note this does not influence the order of observations within each group. Groupby preserves the order of rows within each group. If False, the groups will appear in the same order as they did in the original Series. This argument has no effect on filtrations (see the [filtrations in the user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration)
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

pandas.api.typing.SeriesGroupBy

Returns a groupby object that contains information about the groups.

See also

[`resample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")

Convenience method for frequency conversion and resampling of time series.

Notes

See the [user guide](https://pandas.pydata.org/docs/dev/user_guide/groupby.html)
 for more detailed usage and examples, including splitting an object into groups, iterating through groups, selecting a group, aggregation, and more.

The implementation of groupby is hash-based, meaning in particular that objects that compare as equal will be considered to be in the same group. An exception to this is that pandas has special handling of NA values: any NA values will be collapsed to a single group, regardless of how they compare. See the user guide linked above for more details.

Examples

\>>> ser \= pd.Series(
...     \[390.0, 350.0, 30.0, 20.0\],
...     index\=\["Falcon", "Falcon", "Parrot", "Parrot"\],
...     name\="Max Speed",
... )
\>>> ser
Falcon    390.0
Falcon    350.0
Parrot     30.0
Parrot     20.0
Name: Max Speed, dtype: float64

Copy to clipboard

We can pass a list of values to group the Series data by custom labels:

\>>> ser.groupby(\["a", "b", "a", "b"\]).mean()
a    210.0
b    185.0
Name: Max Speed, dtype: float64

Copy to clipboard

Grouping by numeric labels yields similar results:

\>>> ser.groupby(\[0, 1, 0, 1\]).mean()
0    210.0
1    185.0
Name: Max Speed, dtype: float64

Copy to clipboard

We can group by a level of the index:

\>>> ser.groupby(level\=0).mean()
Falcon    370.0
Parrot     25.0
Name: Max Speed, dtype: float64

Copy to clipboard

We can group by a condition applied to the Series values:

\>>> ser.groupby(ser \> 100).mean()
Max Speed
False     25.0
True     370.0
Name: Max Speed, dtype: float64

Copy to clipboard

**Grouping by Indexes**

We can groupby different levels of a hierarchical index using the level parameter:

\>>> arrays \= \[\
...     \["Falcon", "Falcon", "Parrot", "Parrot"\],\
...     \["Captive", "Wild", "Captive", "Wild"\],\
... \]
\>>> index \= pd.MultiIndex.from\_arrays(arrays, names\=("Animal", "Type"))
\>>> ser \= pd.Series(\[390.0, 350.0, 30.0, 20.0\], index\=index, name\="Max Speed")
\>>> ser
Animal  Type
Falcon  Captive    390.0
        Wild       350.0
Parrot  Captive     30.0
        Wild        20.0
Name: Max Speed, dtype: float64

Copy to clipboard

\>>> ser.groupby(level\=0).mean()
Animal
Falcon    370.0
Parrot     25.0
Name: Max Speed, dtype: float64

Copy to clipboard

We can also group by the ‘Type’ level of the hierarchical index to get the mean speed for each type:

\>>> ser.groupby(level\="Type").mean()
Type
Captive    210.0
Wild       185.0
Name: Max Speed, dtype: float64

Copy to clipboard

We can also choose to include NA in group keys or not by defining dropna parameter, the default setting is True.

\>>> ser \= pd.Series(\[1, 2, 3, 3\], index\=\["a", "a", "b", np.nan\])
\>>> ser.groupby(level\=0).sum()
a    3
b    3
dtype: int64

Copy to clipboard

To include NA values in the group keys, set dropna=False:

\>>> ser.groupby(level\=0, dropna\=False).sum()
a    3
b    3
NaN  3
dtype: int64

Copy to clipboard

We can also group by a custom list with NaN values to handle missing group labels:

\>>> arrays \= \["Falcon", "Falcon", "Parrot", "Parrot"\]
\>>> ser \= pd.Series(\[390.0, 350.0, 30.0, 20.0\], index\=arrays, name\="Max Speed")
\>>> ser.groupby(\["a", "b", "a", np.nan\]).mean()
a    210.0
b    350.0
Name: Max Speed, dtype: float64

Copy to clipboard

\>>> ser.groupby(\["a", "b", "a", np.nan\], dropna\=False).mean()
a    210.0
b    350.0
NaN   20.0
Name: Max Speed, dtype: float64

Copy to clipboard

On this page
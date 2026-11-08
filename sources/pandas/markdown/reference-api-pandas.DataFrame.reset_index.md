[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.reset\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas-dataframe-reset-index "Link to this heading")

=====================================================================================================================================================================

DataFrame.reset\_index(_level\=None_, _\*_, _drop\=False_, _inplace\=<no\_default>_, _col\_level\=0_, _col\_fill\=''_, _allow\_duplicates\=False_, _names\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L8004-L8264)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "Link to this definition")

Reset the index, or a level of it.

Reset the index of the DataFrame, and use the default one instead. If the DataFrame has a MultiIndex, this method can remove one or more levels.

Parameters:

**level**int, str, tuple, or list, default None

Only remove the given levels from the index. Removes all levels by default.

**drop**bool, default False

Do not try to insert index into dataframe columns. This resets the index to the default integer index.

**inplace**bool, default False

Whether to modify the DataFrame rather than creating a new one.

Deprecated since version 3.1.0: This keyword is deprecated and will be removed in pandas 4.0. See the [whatsnew note on PDEP-8](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace)
 for more details.

**col\_level**int or str, default 0

If the columns have multiple levels, determines which level the labels are inserted into. By default it is inserted into the first level.

**col\_fill**object, default ‘’

If the columns have multiple levels, determines how the other levels are named. If None then the index name is repeated.

**allow\_duplicates**bool, default False

Allow duplicate column labels to be created.

**names**int, str or 1-dimensional list, default None

Using the given string, rename the DataFrame column which contains the index data. If the DataFrame has a MultiIndex, this has to be a list with length equal to the number of levels.

Returns:

DataFrame or None

DataFrame with the new index or None if `inplace=True`.

See also

[`DataFrame.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")

Opposite of reset\_index.

[`DataFrame.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")

Change to new indices or expand indices.

[`DataFrame.reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like")

Change to same indices as other DataFrame.

Notes

Columns do not store a `freq`, so the `freq` of a [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
 or [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")
 is lost when it is inserted as a column, and is not restored by a subsequent [`DataFrame.set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")
.

Examples

\>>> df \= pd.DataFrame(
...     \[("bird", 389.0), ("bird", 24.0), ("mammal", 80.5), ("mammal", np.nan)\],
...     index\=\["falcon", "parrot", "lion", "monkey"\],
...     columns\=("class", "max\_speed"),
... )
\>>> df
         class  max\_speed
falcon    bird      389.0
parrot    bird       24.0
lion    mammal       80.5
monkey  mammal        NaN

Copy to clipboard

When we reset the index, the old index is added as a column, and a new sequential index is used:

\>>> df.reset\_index()
    index   class  max\_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN

Copy to clipboard

We can use the drop parameter to avoid the old index being added as a column:

\>>> df.reset\_index(drop\=True)
    class  max\_speed
0    bird      389.0
1    bird       24.0
2  mammal       80.5
3  mammal        NaN

Copy to clipboard

You can also use reset\_index with MultiIndex.

\>>> index \= pd.MultiIndex.from\_tuples(
...     \[\
...         ("bird", "falcon"),\
...         ("bird", "parrot"),\
...         ("mammal", "lion"),\
...         ("mammal", "monkey"),\
...     \],
...     names\=\["class", "name"\],
... )
\>>> columns \= pd.MultiIndex.from\_tuples(\[("speed", "max"), ("species", "type")\])
\>>> df \= pd.DataFrame(
...     \[(389.0, "fly"), (24.0, "fly"), (80.5, "run"), (np.nan, "jump")\],
...     index\=index,
...     columns\=columns,
... )
\>>> df
               speed species
                 max    type
class  name
bird   falcon  389.0     fly
       parrot   24.0     fly
mammal lion     80.5     run
       monkey    NaN    jump

Copy to clipboard

Using the names parameter, choose a name for the index column:

\>>> df.reset\_index(names\=\["classes", "names"\])
  classes   names  speed species
                     max    type
0    bird  falcon  389.0     fly
1    bird  parrot   24.0     fly
2  mammal    lion   80.5     run
3  mammal  monkey    NaN    jump

Copy to clipboard

If the index has multiple levels, we can reset a subset of them:

\>>> df.reset\_index(level\="class")
         class  speed species
                  max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump

Copy to clipboard

If we are not dropping the index, by default, it is placed in the top level. We can place it in another level:

\>>> df.reset\_index(level\="class", col\_level\=1)
                speed species
         class    max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump

Copy to clipboard

When the index is inserted under another level, we can specify under which one with the parameter col\_fill:

\>>> df.reset\_index(level\="class", col\_level\=1, col\_fill\="species")
              species  speed species
                class    max    type
name
falcon           bird  389.0     fly
parrot           bird   24.0     fly
lion           mammal   80.5     run
monkey         mammal    NaN    jump

Copy to clipboard

If we specify a nonexistent level for col\_fill, it is created:

\>>> df.reset\_index(level\="class", col\_level\=1, col\_fill\="genus")
                genus  speed species
                class    max    type
name
falcon           bird  389.0     fly
parrot           bird   24.0     fly
lion           mammal   80.5     run
monkey         mammal    NaN    jump

Copy to clipboard

On this page
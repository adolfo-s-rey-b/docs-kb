[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.drop.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.drop.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.drop.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.drop.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.drop.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.drop.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.drop.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.drop.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.drop.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.drop.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.drop.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.drop.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.drop[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html#pandas-multiindex-drop "Link to this heading")

==================================================================================================================================================

MultiIndex.drop(_codes_, _level\=None_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2909-L3018)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html#pandas.MultiIndex.drop "Link to this definition")

Make a new [`pandas.MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
 with the passed list of codes deleted.

This method allows for the removal of specified labels from a MultiIndex. The labels to be removed can be provided as a list of tuples if no level is specified, or as a list of labels from a specific level if the level parameter is provided. This can be useful for refining the structure of a MultiIndex to fit specific requirements.

Parameters:

**codes**array-like

Must be a list of tuples when `level` is not specified.

**level**int or level name, default None

Level from which the labels will be dropped.

**errors**str, default ‘raise’

If ‘ignore’, suppress error and existing labels are dropped.

Returns:

MultiIndex

A new MultiIndex with the specified labels removed.

See also

[`MultiIndex.remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")

Create new MultiIndex from current that removes unused levels.

[`MultiIndex.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "pandas.MultiIndex.reorder_levels")

Rearrange levels using input order.

`MultiIndex.rename`

Rename levels in a MultiIndex.

Examples

\>>> idx \= pd.MultiIndex.from\_product(
...     \[(0, 1, 2), ("green", "purple")\], names\=\["number", "color"\]
... )
\>>> idx
MultiIndex(\[(0,  'green'),\
            (0, 'purple'),\
            (1,  'green'),\
            (1, 'purple'),\
            (2,  'green'),\
            (2, 'purple')\],
           names=\['number', 'color'\])
\>>> idx.drop(\[(1, "green"), (2, "purple")\])
MultiIndex(\[(0,  'green'),\
            (0, 'purple'),\
            (1, 'purple'),\
            (2,  'green')\],
           names=\['number', 'color'\])

Copy to clipboard

We can also drop from a specific level.

\>>> idx.drop("green", level\="color")
MultiIndex(\[(0, 'purple'),\
            (1, 'purple'),\
            (2, 'purple')\],
           names=\['number', 'color'\])

Copy to clipboard

\>>> idx.drop(\[1, 2\], level\=0)
MultiIndex(\[(0,  'green'),\
            (0, 'purple')\],
           names=\['number', 'color'\])

Copy to clipboard

On this page
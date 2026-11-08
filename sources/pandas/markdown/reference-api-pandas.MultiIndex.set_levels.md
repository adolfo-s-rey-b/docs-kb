[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.set_levels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.set_levels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.set_levels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.set_levels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.set_levels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.set_levels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.set_levels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.set_levels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.set_levels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.set_levels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.set_levels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.set_levels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.set\_levels[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas-multiindex-set-levels "Link to this heading")

=====================================================================================================================================================================

MultiIndex.set\_levels(_levels_, _\*_, _level\=None_, _verify\_integrity\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L981-L1098)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels "Link to this definition")

Set new levels on MultiIndex. Defaults to returning new index.

The set\_levels method provides a flexible way to change the levels of a MultiIndex. This is particularly useful when you need to update the index structure of your DataFrame without altering the data. The method returns a new MultiIndex unless the operation is performed in-place, ensuring that the original index remains unchanged unless explicitly modified.

The method checks the integrity of the new levels against the existing codes by default, but this can be disabled if you are confident that your levels are consistent with the underlying data. This can be useful when you want to perform optimizations or make specific adjustments to the index levels that do not strictly adhere to the original structure.

Parameters:

**levels**sequence or list of sequence

New level(s) to apply.

**level**int, level name, or sequence of int/level names (default None)

Level(s) to set (None for all levels).

**verify\_integrity**bool, default True

If True, checks that levels and codes are compatible.

Returns:

MultiIndex

A new MultiIndex with the updated levels.

See also

[`MultiIndex.set_codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas.MultiIndex.set_codes "pandas.MultiIndex.set_codes")

Set new codes on the existing MultiIndex.

[`MultiIndex.remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")

Create new MultiIndex from current that removes unused levels.

[`Index.set_names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")

Set Index or MultiIndex name.

Examples

\>>> idx \= pd.MultiIndex.from\_tuples(
...     \[\
...         (1, "one"),\
...         (1, "two"),\
...         (2, "one"),\
...         (2, "two"),\
...         (3, "one"),\
...         (3, "two"),\
...     \],
...     names\=\["foo", "bar"\],
... )
\>>> idx
MultiIndex(\[(1, 'one'),\
    (1, 'two'),\
    (2, 'one'),\
    (2, 'two'),\
    (3, 'one'),\
    (3, 'two')\],
   names=\['foo', 'bar'\])

Copy to clipboard

\>>> idx.set\_levels(\[\["a", "b", "c"\], \[1, 2\]\])
MultiIndex(\[('a', 1),\
            ('a', 2),\
            ('b', 1),\
            ('b', 2),\
            ('c', 1),\
            ('c', 2)\],
           names=\['foo', 'bar'\])
\>>> idx.set\_levels(\["a", "b", "c"\], level\=0)
MultiIndex(\[('a', 'one'),\
            ('a', 'two'),\
            ('b', 'one'),\
            ('b', 'two'),\
            ('c', 'one'),\
            ('c', 'two')\],
           names=\['foo', 'bar'\])
\>>> idx.set\_levels(\["a", "b"\], level\="bar")
MultiIndex(\[(1, 'a'),\
            (1, 'b'),\
            (2, 'a'),\
            (2, 'b'),\
            (3, 'a'),\
            (3, 'b')\],
           names=\['foo', 'bar'\])

Copy to clipboard

If any of the levels passed to `set_levels()` exceeds the existing length, all of the values from that argument will be stored in the MultiIndex levels, though the values will be truncated in the MultiIndex output.

\>>> idx.set\_levels(\[\["a", "b", "c"\], \[1, 2, 3, 4\]\], level\=\[0, 1\])
MultiIndex(\[('a', 1),\
    ('a', 2),\
    ('b', 1),\
    ('b', 2),\
    ('c', 1),\
    ('c', 2)\],
   names=\['foo', 'bar'\])
\>>> idx.set\_levels(\[\["a", "b", "c"\], \[1, 2, 3, 4\]\], level\=\[0, 1\]).levels
FrozenList(\[\['a', 'b', 'c'\], \[1, 2, 3, 4\]\])

Copy to clipboard

On this page
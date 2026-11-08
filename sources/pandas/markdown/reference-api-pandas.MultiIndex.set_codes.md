[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.set_codes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.set_codes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.set_codes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.set_codes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.set_codes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.set_codes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.set_codes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.set_codes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.set_codes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.set_codes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.set_codes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.set_codes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.set\_codes[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas-multiindex-set-codes "Link to this heading")

==================================================================================================================================================================

MultiIndex.set\_codes(_codes_, _\*_, _level\=None_, _verify\_integrity\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1226-L1298)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas.MultiIndex.set_codes "Link to this definition")

Set new codes on MultiIndex. Defaults to returning new index.

The codes map each index entry to its position in the corresponding level array. This method returns a new MultiIndex with the updated codes.

Parameters:

**codes**sequence or list of sequence

New codes to apply.

**level**int, level name, or sequence of int/level names (default None)

Level(s) to set (None for all levels).

**verify\_integrity**bool, default True

If True, checks that levels and codes are compatible.

Returns:

new index (of same type and class…etc) or None

The same type as the caller or None if `inplace=True`.

See also

[`MultiIndex.set_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels "pandas.MultiIndex.set_levels")

Set new levels on MultiIndex.

[`MultiIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes")

Get the codes of the levels in the MultiIndex.

[`MultiIndex.levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "pandas.MultiIndex.levels")

Get the levels of the MultiIndex.

Examples

\>>> idx \= pd.MultiIndex.from\_tuples(
...     \[(1, "one"), (1, "two"), (2, "one"), (2, "two")\], names\=\["foo", "bar"\]
... )
\>>> idx
MultiIndex(\[(1, 'one'),\
    (1, 'two'),\
    (2, 'one'),\
    (2, 'two')\],
   names=\['foo', 'bar'\])

Copy to clipboard

\>>> idx.set\_codes(\[\[1, 0, 1, 0\], \[0, 0, 1, 1\]\])
MultiIndex(\[(2, 'one'),\
            (1, 'one'),\
            (2, 'two'),\
            (1, 'two')\],
           names=\['foo', 'bar'\])
\>>> idx.set\_codes(\[1, 0, 1, 0\], level\=0)
MultiIndex(\[(2, 'one'),\
            (1, 'two'),\
            (2, 'one'),\
            (1, 'two')\],
           names=\['foo', 'bar'\])
\>>> idx.set\_codes(\[0, 0, 1, 1\], level\="bar")
MultiIndex(\[(1, 'one'),\
            (1, 'one'),\
            (2, 'two'),\
            (2, 'two')\],
           names=\['foo', 'bar'\])
\>>> idx.set\_codes(\[\[1, 0, 1, 0\], \[0, 0, 1, 1\]\], level\=\[0, 1\])
MultiIndex(\[(2, 'one'),\
            (1, 'one'),\
            (2, 'two'),\
            (1, 'two')\],
           names=\['foo', 'bar'\])

Copy to clipboard

On this page
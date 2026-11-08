[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.IndexSlice.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.IndexSlice.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.IndexSlice.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.IndexSlice.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.IndexSlice.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.IndexSlice.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.IndexSlice.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.IndexSlice.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.IndexSlice.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.IndexSlice.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.IndexSlice.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.IndexSlice.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.IndexSlice[#](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#pandas-indexslice "Link to this heading")

===================================================================================================================================

pandas.IndexSlice \= <pandas.core.indexing.\_IndexSlice object>[#](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#pandas.IndexSlice "Link to this definition")

Create an object to more easily perform multi-index slicing.

`IndexSlice` is a convenience object that allows the use of natural slice syntax (`start:stop`) when selecting from a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
, rather than requiring explicit `slice()` calls.

See also

[`MultiIndex.remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")

New MultiIndex with no unused levels.

Notes

See [Defined Levels](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-shown-levels)
 for further info on slicing a MultiIndex.

Examples

\>>> midx \= pd.MultiIndex.from\_product(\[\["A0", "A1"\], \["B0", "B1", "B2", "B3"\]\])
\>>> columns \= \["foo", "bar"\]
\>>> dfmi \= pd.DataFrame(
...     np.arange(16).reshape((len(midx), len(columns))),
...     index\=midx,
...     columns\=columns,
... )

Copy to clipboard

Using the default slice command:

\>>> dfmi.loc\[(slice(None), slice("B0", "B1")), :\]
           foo  bar
    A0 B0    0    1
       B1    2    3
    A1 B0    8    9
       B1   10   11

Copy to clipboard

Using the IndexSlice class for a more intuitive command:

\>>> idx \= pd.IndexSlice
\>>> dfmi.loc\[idx\[:, "B0":"B1"\], :\]
           foo  bar
    A0 B0    0    1
       B1    2    3
    A1 B0    8    9
       B1   10   11

Copy to clipboard

On this page
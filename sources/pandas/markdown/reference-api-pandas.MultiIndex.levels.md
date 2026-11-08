[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.levels.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.levels.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.levels.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.levels.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.levels.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.levels.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.levels.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.levels.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.levels.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.levels.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.levels.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.levels.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.levels[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas-multiindex-levels "Link to this heading")

========================================================================================================================================================

MultiIndex.levels[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L860-L934)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "Link to this definition")

Levels of the MultiIndex.

Levels refer to the different hierarchical levels or layers in a MultiIndex. In a MultiIndex, each level represents a distinct dimension or category of the index.

To access the levels, you can use the levels attribute of the MultiIndex, which returns a tuple of Index objects. Each Index object represents a level in the MultiIndex and contains the unique values found in that specific level.

If a MultiIndex is created with levels A, B, C, and the DataFrame using it filters out all rows of the level C, MultiIndex.levels will still return A, B, C.

When a `MultiIndex` is built by the standard constructors (e.g. [`MultiIndex.from_arrays()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")
, [`MultiIndex.from_tuples()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")
), missing values (`NaN`) are not stored in `levels`; they are represented by a code of `-1` in [`MultiIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes")
, so `levels` does not contain `NaN` even when the corresponding level of the `MultiIndex` does.

See also

[`MultiIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes")

The codes of the levels in the MultiIndex.

[`MultiIndex.get_level_values`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "pandas.MultiIndex.get_level_values")

Return vector of label values for requested level.

Examples

\>>> index \= pd.MultiIndex.from\_product(
...     \[\["mammal"\], ("goat", "human", "cat", "dog")\],
...     names\=\["Category", "Animals"\],
... )
\>>> leg\_num \= pd.DataFrame(data\=(4, 2, 4, 4), index\=index, columns\=\["Legs"\])
\>>> leg\_num
                  Legs
Category Animals
mammal   goat        4
         human       2
         cat         4
         dog         4

Copy to clipboard

\>>> leg\_num.index.levels
FrozenList(\[\['mammal'\], \['cat', 'dog', 'goat', 'human'\]\])

Copy to clipboard

MultiIndex levels will not change even if the DataFrame using the MultiIndex does not contain all them anymore. See how “human” is not in the DataFrame, but it is still in levels:

\>>> large\_leg\_num \= leg\_num\[leg\_num.Legs \> 2\]
\>>> large\_leg\_num
                  Legs
Category Animals
mammal   goat        4
         cat         4
         dog         4

Copy to clipboard

\>>> large\_leg\_num.index.levels
FrozenList(\[\['mammal'\], \['cat', 'dog', 'goat', 'human'\]\])

Copy to clipboard

On this page
[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas-multiindex "Link to this heading")

===================================================================================================================================

class pandas.MultiIndex(_levels\=None_, _codes\=None_, _sortorder\=None_, _names\=None_, _copy\=False_, _name\=None_, _verify\_integrity\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L201-L5059)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "Link to this definition")

A multi-level, or hierarchical, index object for pandas objects.

A MultiIndex allows indexing with multiple keys, effectively enabling multiple dimensions of indexing on a single axis. It can be thought of as an array of tuples where each tuple is unique.

Parameters:

**levels**sequence of arrays

The unique labels for each level. Uniqueness is determined by equality, so values that compare equal (e.g. `1`, `1.0` and `True`) cannot appear in the same level.

**codes**sequence of arrays

Integers for each level designating which label at each location.

**sortorder**optional int

Level of sortedness (must be lexicographically sorted by that level).

**names**optional sequence of objects

Names for each of the index levels. (name is accepted for compat).

**copy**bool, default False

Copy the meta-data.

**name**Label

Kept for compatibility with 1-dimensional Index. Should not be used.

**verify\_integrity**bool, default True

Check that the levels/codes are consistent and valid.

Attributes

|     |     |
| --- | --- |
| [`names`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html#pandas.MultiIndex.names "pandas.MultiIndex.names") | Names of levels in MultiIndex. |
| [`levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "pandas.MultiIndex.levels") | Levels of the MultiIndex. |
| [`codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes") | Codes of the MultiIndex. |
| [`nlevels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html#pandas.MultiIndex.nlevels "pandas.MultiIndex.nlevels") | Integer number of levels in this MultiIndex. |
| [`levshape`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html#pandas.MultiIndex.levshape "pandas.MultiIndex.levshape") | A tuple representing the length of each level in the MultiIndex. |
| [`dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html#pandas.MultiIndex.dtypes "pandas.MultiIndex.dtypes") | Return the dtypes as a Series for the underlying MultiIndex. |

Methods

|     |     |
| --- | --- |
| [`from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")<br>(arrays\[, sortorder, names\]) | Convert arrays to MultiIndex. |
| [`from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")<br>(tuples\[, sortorder, names\]) | Convert list of tuples to MultiIndex. |
| [`from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")<br>(iterables\[, sortorder, names\]) | Make a MultiIndex from the cartesian product of multiple iterables. |
| [`from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")<br>(df\[, sortorder, names\]) | Make a MultiIndex from a DataFrame. |
| [`set_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels "pandas.MultiIndex.set_levels")<br>(levels, \*\[, level, verify\_integrity\]) | Set new levels on MultiIndex. |
| [`set_codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas.MultiIndex.set_codes "pandas.MultiIndex.set_codes")<br>(codes, \*\[, level, verify\_integrity\]) | Set new codes on MultiIndex. |
| [`to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#pandas.MultiIndex.to_frame "pandas.MultiIndex.to_frame")<br>(\[index, name, allow\_duplicates\]) | Create a DataFrame with the levels of the MultiIndex as columns. |
| [`to_flat_index`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html#pandas.MultiIndex.to_flat_index "pandas.MultiIndex.to_flat_index")<br>() | Convert a MultiIndex to an Index of Tuples containing the level values. |
| [`sortlevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html#pandas.MultiIndex.sortlevel "pandas.MultiIndex.sortlevel")<br>(\[level, ascending, ...\]) | Sort MultiIndex at the requested level. |
| [`droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#pandas.MultiIndex.droplevel "pandas.MultiIndex.droplevel")<br>(\[level\]) | Return index with requested level(s) removed. |
| [`swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "pandas.MultiIndex.swaplevel")<br>(\[i, j\]) | Swap level i with level j. |
| [`reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "pandas.MultiIndex.reorder_levels")<br>(order) | Rearrange levels using input order. |
| [`remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")<br>() | Create new MultiIndex from current that removes unused levels. |
| [`get_level_values`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "pandas.MultiIndex.get_level_values")<br>(level) | Return vector of label values for requested level. |
| [`get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_indexer.html#pandas.MultiIndex.get_indexer "pandas.MultiIndex.get_indexer")<br>(target\[, method, limit, tolerance\]) | Compute indexer and mask for new index given the current index. |
| [`get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas.MultiIndex.get_loc "pandas.MultiIndex.get_loc")<br>(key) | Get location for a label or a tuple of labels. |
| [`get_locs`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "pandas.MultiIndex.get_locs")<br>(seq) | Get location for a sequence of labels. |
| [`get_loc_level`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html#pandas.MultiIndex.get_loc_level "pandas.MultiIndex.get_loc_level")<br>(key\[, level, drop\_level\]) | Get location and sliced index for requested label(s)/level(s). |
| [`drop`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html#pandas.MultiIndex.drop "pandas.MultiIndex.drop")<br>(codes\[, level, errors\]) | Make a new [`pandas.MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br> with the passed list of codes deleted. |

Raises:

ValueError

If `verify_integrity` is True and the levels are not unique or are not consistent with the codes.

See also

[`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")

Convert list of arrays to MultiIndex.

[`MultiIndex.from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")

Create a MultiIndex from the cartesian product of iterables.

[`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")

Convert list of tuples to a MultiIndex.

[`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")

Make a MultiIndex from a DataFrame.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

The base pandas Index type.

Notes

See the [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)
 for more.

Examples

A new `MultiIndex` is typically constructed using one of the helper methods [`MultiIndex.from_arrays()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")
, [`MultiIndex.from_product()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")
 and [`MultiIndex.from_tuples()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")
. For example (using `.from_arrays`):

\>>> arrays \= \[\[1, 1, 2, 2\], \["red", "blue", "red", "blue"\]\]
\>>> pd.MultiIndex.from\_arrays(arrays, names\=("number", "color"))
MultiIndex(\[(1,  'red'),\
            (1, 'blue'),\
            (2,  'red'),\
            (2, 'blue')\],
           names=\['number', 'color'\])

Copy to clipboard

See further examples for how to construct a MultiIndex in the doc strings of the mentioned helper methods.

On this page
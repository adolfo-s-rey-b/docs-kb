[Skip to main content](https://pandas.pydata.org/docs/reference/indexing.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/indexing.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/indexing.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/indexing.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/indexing.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/indexing.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/indexing.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/indexing.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/indexing.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/indexing.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/indexing.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/indexing.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/indexing.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/indexing.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Index objects[#](https://pandas.pydata.org/docs/reference/indexing.html#index-objects "Link to this heading")

==============================================================================================================

Index[#](https://pandas.pydata.org/docs/reference/indexing.html#index "Link to this heading")

----------------------------------------------------------------------------------------------

Note

For an overview, see [Index objects](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-class)
.

**Many of these methods or variants thereof are available on the objects that contain an index (Series/DataFrame) and those should most likely be used before calling these methods directly.**

|     |     |
| --- | --- |
| [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")<br>(\[data, dtype, copy, name, tupleize\_cols\]) | Immutable sequence used for indexing and alignment. |

### Properties[#](https://pandas.pydata.org/docs/reference/indexing.html#properties "Link to this heading")

|     |     |
| --- | --- |
| [`Index.values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "pandas.Index.values") | Return an array representing the data in the Index. |
| [`Index.is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas.Index.is_monotonic_increasing "pandas.Index.is_monotonic_increasing") | Return a boolean if the values are equal or increasing. |
| [`Index.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas.Index.is_monotonic_decreasing "pandas.Index.is_monotonic_decreasing") | Return a boolean if the values are equal or decreasing. |
| [`Index.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique") | Return if the index has unique values. |
| [`Index.has_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "pandas.Index.has_duplicates") | Check if the Index has duplicate values. |
| [`Index.hasnans`](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html#pandas.Index.hasnans "pandas.Index.hasnans") | Return True if there are any NaNs. |
| [`Index.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype") | Return the dtype object of the underlying data. |
| [`Index.inferred_type`](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#pandas.Index.inferred_type "pandas.Index.inferred_type") | Return a string of the type inferred from the values. |
| [`Index.shape`](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html#pandas.Index.shape "pandas.Index.shape") | Return a tuple of the shape of the underlying data. |
| [`Index.name`](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas.Index.name "pandas.Index.name") | Return Index or MultiIndex name. |
| [`Index.names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#pandas.Index.names "pandas.Index.names") | Get names on index. |
| [`Index.nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html#pandas.Index.nbytes "pandas.Index.nbytes") | Return the number of bytes in the underlying data. |
| [`Index.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#pandas.Index.ndim "pandas.Index.ndim") | Number of dimensions of the underlying data, by definition 1. |
| [`Index.size`](https://pandas.pydata.org/docs/reference/api/pandas.Index.size.html#pandas.Index.size "pandas.Index.size") | Return the number of elements in the underlying data. |
| [`Index.empty`](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html#pandas.Index.empty "pandas.Index.empty") | Indicator whether Index is empty. |
| [`Index.T`](https://pandas.pydata.org/docs/reference/api/pandas.Index.T.html#pandas.Index.T "pandas.Index.T") | Return the transpose, which is by definition self. |
| [`Index.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html#pandas.Index.memory_usage "pandas.Index.memory_usage")<br>(\[deep\]) | Memory usage of the values. |
| [`Index.array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array") | The ExtensionArray of the data backing this Index. |

### Modifying and computations[#](https://pandas.pydata.org/docs/reference/indexing.html#modifying-and-computations "Link to this heading")

|     |     |
| --- | --- |
| [`Index.all`](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#pandas.Index.all "pandas.Index.all")<br>(\*args, \*\*kwargs) | Return whether all elements are Truthy. |
| [`Index.any`](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#pandas.Index.any "pandas.Index.any")<br>(\*args, \*\*kwargs) | Return whether any element is Truthy. |
| [`Index.argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#pandas.Index.argmin "pandas.Index.argmin")<br>(\[axis, skipna\]) | Return int position of the smallest value in the Index. |
| [`Index.argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#pandas.Index.argmax "pandas.Index.argmax")<br>(\[axis, skipna\]) | Return int position of the largest value in the Index. |
| [`Index.copy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#pandas.Index.copy "pandas.Index.copy")<br>(\[name, deep\]) | Make a copy of this object. |
| [`Index.delete`](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas.Index.delete "pandas.Index.delete")<br>(loc) | Make new Index with passed location(-s) deleted. |
| [`Index.drop`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#pandas.Index.drop "pandas.Index.drop")<br>(labels\[, errors\]) | Make new Index with passed list of labels deleted. |
| [`Index.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "pandas.Index.drop_duplicates")<br>(\*\[, keep\]) | Return Index with duplicate values removed. |
| [`Index.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")<br>(\[keep\]) | Indicate duplicate index values. |
| [`Index.equals`](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas.Index.equals "pandas.Index.equals")<br>(other) | Determine if two Index object are equal. |
| [`Index.factorize`](https://pandas.pydata.org/docs/reference/api/pandas.Index.factorize.html#pandas.Index.factorize "pandas.Index.factorize")<br>(\[sort, use\_na\_sentinel\]) | Encode the object as an enumerated type or categorical variable. |
| [`Index.identical`](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas.Index.identical "pandas.Index.identical")<br>(other) | Similar to equals, but checks that object attributes and types are also equal. |
| [`Index.insert`](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas.Index.insert "pandas.Index.insert")<br>(loc, item) | Make new Index inserting new item at location. |
| [`Index.is_`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html#pandas.Index.is_ "pandas.Index.is_")<br>(other) | More flexible, faster check like `is` but that works through views. |
| [`Index.min`](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#pandas.Index.min "pandas.Index.min")<br>(\[axis, skipna\]) | Return the minimum value of the Index. |
| [`Index.max`](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#pandas.Index.max "pandas.Index.max")<br>(\[axis, skipna\]) | Return the maximum value of the Index. |
| [`Index.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html#pandas.Index.reindex "pandas.Index.reindex")<br>(target\[, method, level, ...\]) | Create index with target's values. |
| [`Index.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")<br>(name, \*\[, inplace\]) | Alter Index or MultiIndex name. |
| [`Index.repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#pandas.Index.repeat "pandas.Index.repeat")<br>(repeats\[, axis\]) | Repeat elements of an Index. |
| [`Index.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html#pandas.Index.replace "pandas.Index.replace")<br>(\[to\_replace, value, regex\]) | Replace values in the Index. |
| [`Index.where`](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#pandas.Index.where "pandas.Index.where")<br>(cond\[, other\]) | Replace values where the condition is False. |
| [`Index.take`](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html#pandas.Index.take "pandas.Index.take")<br>(indices\[, axis, allow\_fill, ...\]) | Return a new Index of the values selected by the indices. |
| [`Index.putmask`](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html#pandas.Index.putmask "pandas.Index.putmask")<br>(mask, value) | Return a new Index of the values set with the mask. |
| [`Index.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "pandas.Index.unique")<br>(\[level\]) | Return unique values in the index. |
| [`Index.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html#pandas.Index.nunique "pandas.Index.nunique")<br>(\[dropna\]) | Return number of unique elements in the object. |
| [`Index.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html#pandas.Index.value_counts "pandas.Index.value_counts")<br>(\[normalize, sort, ...\]) | Return a Series containing counts of unique values. |

### Compatibility with MultiIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#compatibility-with-multiindex "Link to this heading")

|     |     |
| --- | --- |
| [`Index.set_names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")<br>(names, \*\[, level, inplace\]) | Set Index or MultiIndex name. |
| [`Index.droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Index.droplevel.html#pandas.Index.droplevel "pandas.Index.droplevel")<br>(\[level\]) | Return index with requested level(s) removed. |

### Missing values[#](https://pandas.pydata.org/docs/reference/indexing.html#missing-values "Link to this heading")

|     |     |
| --- | --- |
| [`Index.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#pandas.Index.fillna "pandas.Index.fillna")<br>(value) | Fill NA/NaN values with the specified value. |
| [`Index.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")<br>(\[how\]) | Return Index without NA/NaN values. |
| [`Index.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "pandas.Index.isna")<br>() | Detect missing values. |
| [`Index.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas.Index.notna "pandas.Index.notna")<br>() | Detect existing (non-missing) values. |

### Conversion[#](https://pandas.pydata.org/docs/reference/indexing.html#conversion "Link to this heading")

|     |     |
| --- | --- |
| [`Index.astype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html#pandas.Index.astype "pandas.Index.astype")<br>(dtype\[, copy\]) | Create an Index with values cast to dtypes. |
| [`Index.infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html#pandas.Index.infer_objects "pandas.Index.infer_objects")<br>(\[copy\]) | If we have an object dtype, try to infer a non-object dtype. |
| [`Index.item`](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html#pandas.Index.item "pandas.Index.item")<br>() | Return the first element of the underlying data as a Python scalar. |
| [`Index.map`](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#pandas.Index.map "pandas.Index.map")<br>(mapper\[, na\_action\]) | Map values using an input mapping or function. |
| [`Index.ravel`](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html#pandas.Index.ravel "pandas.Index.ravel")<br>(\[order\]) | Return a view on self. |
| [`Index.to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html#pandas.Index.to_list "pandas.Index.to_list")<br>() | Return a list of the values. |
| [`Index.to_series`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_series.html#pandas.Index.to_series "pandas.Index.to_series")<br>(\[index, name\]) | Create a Series with both index and values equal to the index keys. |
| [`Index.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_frame.html#pandas.Index.to_frame "pandas.Index.to_frame")<br>(\[index, name\]) | Create a DataFrame with a column containing the Index. |
| [`Index.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")<br>(\[dtype, copy, na\_value\]) | A NumPy ndarray representing the values in this Series or Index. |
| [`Index.view`](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html#pandas.Index.view "pandas.Index.view")<br>(\[cls\]) | Return a view of the Index with the specified dtype or a new Index instance. |

### Sorting[#](https://pandas.pydata.org/docs/reference/indexing.html#sorting "Link to this heading")

|     |     |
| --- | --- |
| [`Index.argsort`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html#pandas.Index.argsort "pandas.Index.argsort")<br>(\*args, \*\*kwargs) | Return the integer indices that would sort the index. |
| [`Index.searchsorted`](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html#pandas.Index.searchsorted "pandas.Index.searchsorted")<br>(value\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`Index.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "pandas.Index.sort_values")<br>(\*\[, return\_indexer, ...\]) | Return a sorted copy of the index. |

### Time-specific operations[#](https://pandas.pydata.org/docs/reference/indexing.html#time-specific-operations "Link to this heading")

|     |     |
| --- | --- |
| [`Index.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#pandas.Index.shift "pandas.Index.shift")<br>(\[periods, freq\]) | Shift index by desired number of time frequency increments. |

### Combining / joining / set operations[#](https://pandas.pydata.org/docs/reference/indexing.html#combining-joining-set-operations "Link to this heading")

|     |     |
| --- | --- |
| [`Index.append`](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas.Index.append "pandas.Index.append")<br>(other) | Append a collection of Index options together. |
| [`Index.join`](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html#pandas.Index.join "pandas.Index.join")<br>(other, \*\[, how, level, ...\]) | Compute join\_index and indexers to conform data structures to the new index. |
| [`Index.intersection`](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "pandas.Index.intersection")<br>(other\[, sort\]) | Form the intersection of two Index objects. |
| [`Index.union`](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "pandas.Index.union")<br>(other\[, sort\]) | Form the union of two Index objects. |
| [`Index.difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "pandas.Index.difference")<br>(other\[, sort\]) | Return a new Index with elements of index not in other. |
| [`Index.symmetric_difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#pandas.Index.symmetric_difference "pandas.Index.symmetric_difference")<br>(other\[, ...\]) | Compute the symmetric difference of two Index objects. |

### Selecting[#](https://pandas.pydata.org/docs/reference/indexing.html#selecting "Link to this heading")

|     |     |
| --- | --- |
| [`Index.asof`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "pandas.Index.asof")<br>(label) | Return the label from the index, or, if not present, the previous one. |
| [`Index.asof_locs`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html#pandas.Index.asof_locs "pandas.Index.asof_locs")<br>(where, mask) | Return the locations (indices) of labels in the index. |
| [`Index.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "pandas.Index.get_indexer")<br>(target\[, method, limit, ...\]) | Compute indexer and mask for new index given the current index. |
| [`Index.get_indexer_for`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "pandas.Index.get_indexer_for")<br>(target) | Guaranteed return of an indexer even when non-unique. |
| [`Index.get_indexer_non_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html#pandas.Index.get_indexer_non_unique "pandas.Index.get_indexer_non_unique")<br>(target) | Compute indexer and mask for new index given the current index. |
| [`Index.get_level_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_level_values.html#pandas.Index.get_level_values "pandas.Index.get_level_values")<br>(level) | Return an Index of values for requested level. |
| [`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")<br>(key) | Get integer location, slice or boolean mask for requested label. |
| [`Index.get_slice_bound`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")<br>(label, side) | Calculate slice bound that corresponds to given label. |
| [`Index.isin`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#pandas.Index.isin "pandas.Index.isin")<br>(values\[, level\]) | Return a boolean array where the index values are in values. |
| [`Index.slice_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html#pandas.Index.slice_indexer "pandas.Index.slice_indexer")<br>(\[start, end, step\]) | Compute the slice indexer for input labels and step. |
| [`Index.slice_locs`](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#pandas.Index.slice_locs "pandas.Index.slice_locs")<br>(\[start, end, step\]) | Compute slice locations for input labels. |

Numeric Index[#](https://pandas.pydata.org/docs/reference/indexing.html#numeric-index "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")<br>(\[start, stop, step, dtype, copy, ...\]) | Immutable Index implementing a monotonic integer range. |

|     |     |
| --- | --- |
| [`RangeIndex.start`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.start.html#pandas.RangeIndex.start "pandas.RangeIndex.start") | The value of the start parameter (`0` if this was not supplied). |
| [`RangeIndex.stop`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.stop.html#pandas.RangeIndex.stop "pandas.RangeIndex.stop") | The value of the stop parameter. |
| [`RangeIndex.step`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.step.html#pandas.RangeIndex.step "pandas.RangeIndex.step") | The value of the step parameter (`1` if this was not supplied). |
| [`RangeIndex.from_range`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.from_range.html#pandas.RangeIndex.from_range "pandas.RangeIndex.from_range")<br>(data\[, name, dtype\]) | Create [`pandas.RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")<br> from a `range` object. |

CategoricalIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#categoricalindex "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")<br>(\[data, categories, ...\]) | Index based on an underlying [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")<br>. |

### Categorical components[#](https://pandas.pydata.org/docs/reference/indexing.html#categorical-components "Link to this heading")

|     |     |
| --- | --- |
| [`CategoricalIndex.append`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.append.html#pandas.CategoricalIndex.append "pandas.CategoricalIndex.append")<br>(other) | Append a collection of Index options together. |
| [`CategoricalIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.codes.html#pandas.CategoricalIndex.codes "pandas.CategoricalIndex.codes") | The category codes of this categorical index. |
| [`CategoricalIndex.categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.categories.html#pandas.CategoricalIndex.categories "pandas.CategoricalIndex.categories") | The categories of this CategoricalIndex. |
| [`CategoricalIndex.ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.ordered.html#pandas.CategoricalIndex.ordered "pandas.CategoricalIndex.ordered") | Whether the categories have an ordered relationship. |
| [`CategoricalIndex.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.rename_categories.html#pandas.CategoricalIndex.rename_categories "pandas.CategoricalIndex.rename_categories")<br>(...) | Rename categories. |
| [`CategoricalIndex.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.reorder_categories.html#pandas.CategoricalIndex.reorder_categories "pandas.CategoricalIndex.reorder_categories")<br>(...\[, ...\]) | Reorder categories as specified in new\_categories. |
| [`CategoricalIndex.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.add_categories.html#pandas.CategoricalIndex.add_categories "pandas.CategoricalIndex.add_categories")<br>(new\_categories) | Add new categories. |
| [`CategoricalIndex.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_categories.html#pandas.CategoricalIndex.remove_categories "pandas.CategoricalIndex.remove_categories")<br>(removals) | Remove the specified categories. |
| [`CategoricalIndex.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.remove_unused_categories.html#pandas.CategoricalIndex.remove_unused_categories "pandas.CategoricalIndex.remove_unused_categories")<br>() | Remove categories which are not used. |
| [`CategoricalIndex.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.set_categories.html#pandas.CategoricalIndex.set_categories "pandas.CategoricalIndex.set_categories")<br>(new\_categories) | Set the categories to the specified new categories. |
| [`CategoricalIndex.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_ordered.html#pandas.CategoricalIndex.as_ordered "pandas.CategoricalIndex.as_ordered")<br>() | Set the CategoricalIndex to be ordered. |
| [`CategoricalIndex.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.as_unordered.html#pandas.CategoricalIndex.as_unordered "pandas.CategoricalIndex.as_unordered")<br>() | Set the CategoricalIndex to be unordered. |

### Modifying and computations[#](https://pandas.pydata.org/docs/reference/indexing.html#id1 "Link to this heading")

|     |     |
| --- | --- |
| [`CategoricalIndex.map`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.map.html#pandas.CategoricalIndex.map "pandas.CategoricalIndex.map")<br>(mapper\[, na\_action\]) | Map values using input an input mapping or function. |
| [`CategoricalIndex.equals`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.equals.html#pandas.CategoricalIndex.equals "pandas.CategoricalIndex.equals")<br>(other) | Determine if two CategoricalIndex objects contain the same elements. |

IntervalIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#intervalindex "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")<br>(data\[, closed, dtype, copy, ...\]) | Immutable index of intervals that are closed on the same side. |

### IntervalIndex components[#](https://pandas.pydata.org/docs/reference/indexing.html#intervalindex-components "Link to this heading")

|     |     |
| --- | --- |
| [`IntervalIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_arrays.html#pandas.IntervalIndex.from_arrays "pandas.IntervalIndex.from_arrays")<br>(left, right\[, ...\]) | Construct from two arrays defining the left and right bounds. |
| [`IntervalIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_tuples.html#pandas.IntervalIndex.from_tuples "pandas.IntervalIndex.from_tuples")<br>(data\[, closed, ...\]) | Construct an IntervalIndex from an array-like of tuples. |
| [`IntervalIndex.from_breaks`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.from_breaks.html#pandas.IntervalIndex.from_breaks "pandas.IntervalIndex.from_breaks")<br>(breaks\[, closed, ...\]) | Construct an IntervalIndex from an array of splits. |
| [`IntervalIndex.left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.left.html#pandas.IntervalIndex.left "pandas.IntervalIndex.left") | Return left bounds of the intervals in the IntervalIndex. |
| [`IntervalIndex.right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.right.html#pandas.IntervalIndex.right "pandas.IntervalIndex.right") | Return right bounds of the intervals in the IntervalIndex. |
| [`IntervalIndex.mid`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.mid.html#pandas.IntervalIndex.mid "pandas.IntervalIndex.mid") | Return the midpoint of each interval in the IntervalIndex as an Index. |
| [`IntervalIndex.closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed.html#pandas.IntervalIndex.closed "pandas.IntervalIndex.closed") | String describing the inclusive side of the intervals. |
| [`IntervalIndex.closed_left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_left.html#pandas.IntervalIndex.closed_left "pandas.IntervalIndex.closed_left") | Check if the intervals are closed on the left side. |
| [`IntervalIndex.closed_right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.closed_right.html#pandas.IntervalIndex.closed_right "pandas.IntervalIndex.closed_right") | Check if the intervals are closed on the right side. |
| [`IntervalIndex.open_left`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_left.html#pandas.IntervalIndex.open_left "pandas.IntervalIndex.open_left") | Check if the intervals are open on the left side. |
| [`IntervalIndex.open_right`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.open_right.html#pandas.IntervalIndex.open_right "pandas.IntervalIndex.open_right") | Check if the intervals are open on the right side. |
| [`IntervalIndex.length`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.length.html#pandas.IntervalIndex.length "pandas.IntervalIndex.length") | Calculate the length of each interval in the IntervalIndex. |
| [`IntervalIndex.values`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.values.html#pandas.IntervalIndex.values "pandas.IntervalIndex.values") | Return an array representing the data in the Index. |
| [`IntervalIndex.is_empty`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_empty.html#pandas.IntervalIndex.is_empty "pandas.IntervalIndex.is_empty") | Indicates if an interval is empty, meaning it contains no points. |
| [`IntervalIndex.is_non_overlapping_monotonic`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_non_overlapping_monotonic.html#pandas.IntervalIndex.is_non_overlapping_monotonic "pandas.IntervalIndex.is_non_overlapping_monotonic") | Return True if the IntervalIndex is non-overlapping and monotonic. |
| [`IntervalIndex.is_overlapping`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.is_overlapping.html#pandas.IntervalIndex.is_overlapping "pandas.IntervalIndex.is_overlapping") | Return True if the IntervalIndex has overlapping intervals, else False. |
| [`IntervalIndex.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_loc.html#pandas.IntervalIndex.get_loc "pandas.IntervalIndex.get_loc")<br>(key) | Get integer location, slice or boolean mask for requested label. |
| [`IntervalIndex.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.get_indexer.html#pandas.IntervalIndex.get_indexer "pandas.IntervalIndex.get_indexer")<br>(target\[, method, ...\]) | Compute indexer and mask for new index given the current index. |
| [`IntervalIndex.set_closed`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.set_closed.html#pandas.IntervalIndex.set_closed "pandas.IntervalIndex.set_closed")<br>(closed) | Return an identical IntervalIndex closed on the specified side. |
| [`IntervalIndex.contains`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.contains.html#pandas.IntervalIndex.contains "pandas.IntervalIndex.contains")<br>(other) | Check elementwise if the Intervals contain the value. |
| [`IntervalIndex.overlaps`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")<br>(other) | Check elementwise if an Interval overlaps the values in the IntervalIndex. |
| [`IntervalIndex.to_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.to_tuples.html#pandas.IntervalIndex.to_tuples "pandas.IntervalIndex.to_tuples")<br>(\[na\_tuple\]) | Return an Index of tuples of the form (left, right). |

MultiIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#multiindex "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br>(\[levels, codes, sortorder, ...\]) | A multi-level, or hierarchical, index object for pandas objects. |

### MultiIndex constructors[#](https://pandas.pydata.org/docs/reference/indexing.html#multiindex-constructors "Link to this heading")

|     |     |
| --- | --- |
| [`MultiIndex.from_arrays`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")<br>(arrays\[, sortorder, ...\]) | Convert arrays to MultiIndex. |
| [`MultiIndex.from_tuples`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")<br>(tuples\[, sortorder, ...\]) | Convert list of tuples to MultiIndex. |
| [`MultiIndex.from_product`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")<br>(iterables\[, ...\]) | Make a MultiIndex from the cartesian product of multiple iterables. |
| [`MultiIndex.from_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")<br>(df\[, sortorder, names\]) | Make a MultiIndex from a DataFrame. |

### MultiIndex properties[#](https://pandas.pydata.org/docs/reference/indexing.html#multiindex-properties "Link to this heading")

|     |     |
| --- | --- |
| [`MultiIndex.names`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.names.html#pandas.MultiIndex.names "pandas.MultiIndex.names") | Names of levels in MultiIndex. |
| [`MultiIndex.levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levels.html#pandas.MultiIndex.levels "pandas.MultiIndex.levels") | Levels of the MultiIndex. |
| [`MultiIndex.codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "pandas.MultiIndex.codes") | Codes of the MultiIndex. |
| [`MultiIndex.nlevels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.nlevels.html#pandas.MultiIndex.nlevels "pandas.MultiIndex.nlevels") | Integer number of levels in this MultiIndex. |
| [`MultiIndex.levshape`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.levshape.html#pandas.MultiIndex.levshape "pandas.MultiIndex.levshape") | A tuple representing the length of each level in the MultiIndex. |
| [`MultiIndex.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.dtypes.html#pandas.MultiIndex.dtypes "pandas.MultiIndex.dtypes") | Return the dtypes as a Series for the underlying MultiIndex. |

### MultiIndex components[#](https://pandas.pydata.org/docs/reference/indexing.html#multiindex-components "Link to this heading")

|     |     |
| --- | --- |
| [`MultiIndex.set_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_levels.html#pandas.MultiIndex.set_levels "pandas.MultiIndex.set_levels")<br>(levels, \*\[, level, ...\]) | Set new levels on MultiIndex. |
| [`MultiIndex.set_codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas.MultiIndex.set_codes "pandas.MultiIndex.set_codes")<br>(codes, \*\[, level, ...\]) | Set new codes on MultiIndex. |
| [`MultiIndex.to_flat_index`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html#pandas.MultiIndex.to_flat_index "pandas.MultiIndex.to_flat_index")<br>() | Convert a MultiIndex to an Index of Tuples containing the level values. |
| [`MultiIndex.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#pandas.MultiIndex.to_frame "pandas.MultiIndex.to_frame")<br>(\[index, name, ...\]) | Create a DataFrame with the levels of the MultiIndex as columns. |
| [`MultiIndex.sortlevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.sortlevel.html#pandas.MultiIndex.sortlevel "pandas.MultiIndex.sortlevel")<br>(\[level, ascending, ...\]) | Sort MultiIndex at the requested level. |
| [`MultiIndex.droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.droplevel.html#pandas.MultiIndex.droplevel "pandas.MultiIndex.droplevel")<br>(\[level\]) | Return index with requested level(s) removed. |
| [`MultiIndex.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "pandas.MultiIndex.swaplevel")<br>(\[i, j\]) | Swap level i with level j. |
| [`MultiIndex.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "pandas.MultiIndex.reorder_levels")<br>(order) | Rearrange levels using input order. |
| [`MultiIndex.remove_unused_levels`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")<br>() | Create new MultiIndex from current that removes unused levels. |
| [`MultiIndex.drop`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.drop.html#pandas.MultiIndex.drop "pandas.MultiIndex.drop")<br>(codes\[, level, errors\]) | Make a new [`pandas.MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br> with the passed list of codes deleted. |
| [`MultiIndex.copy`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.copy.html#pandas.MultiIndex.copy "pandas.MultiIndex.copy")<br>(\[names, deep, name\]) | Make a copy of this object. |
| [`MultiIndex.append`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.append.html#pandas.MultiIndex.append "pandas.MultiIndex.append")<br>(other) | Append a collection of Index options together. |
| [`MultiIndex.truncate`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.truncate.html#pandas.MultiIndex.truncate "pandas.MultiIndex.truncate")<br>(\[before, after\]) | Slice index between two labels / tuples, return new MultiIndex. |

### MultiIndex selecting[#](https://pandas.pydata.org/docs/reference/indexing.html#multiindex-selecting "Link to this heading")

|     |     |
| --- | --- |
| [`MultiIndex.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc.html#pandas.MultiIndex.get_loc "pandas.MultiIndex.get_loc")<br>(key) | Get location for a label or a tuple of labels. |
| [`MultiIndex.get_locs`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_locs.html#pandas.MultiIndex.get_locs "pandas.MultiIndex.get_locs")<br>(seq) | Get location for a sequence of labels. |
| [`MultiIndex.get_loc_level`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_loc_level.html#pandas.MultiIndex.get_loc_level "pandas.MultiIndex.get_loc_level")<br>(key\[, level, ...\]) | Get location and sliced index for requested label(s)/level(s). |
| [`MultiIndex.get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_indexer.html#pandas.MultiIndex.get_indexer "pandas.MultiIndex.get_indexer")<br>(target\[, method, ...\]) | Compute indexer and mask for new index given the current index. |
| [`MultiIndex.get_level_values`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "pandas.MultiIndex.get_level_values")<br>(level) | Return vector of label values for requested level. |

|     |     |
| --- | --- |
| [`IndexSlice`](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#pandas.IndexSlice "pandas.IndexSlice") | Create an object to more easily perform multi-index slicing. |

DatetimeIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#datetimeindex "Link to this heading")

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")<br>(\[data, freq, tz, ambiguous, ...\]) | Immutable ndarray-like of datetime64 data. |

### Time/date components[#](https://pandas.pydata.org/docs/reference/indexing.html#time-date-components "Link to this heading")

|     |     |
| --- | --- |
| [`DatetimeIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.year.html#pandas.DatetimeIndex.year "pandas.DatetimeIndex.year") | The year of the datetime. |
| [`DatetimeIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month.html#pandas.DatetimeIndex.month "pandas.DatetimeIndex.month") | The month as January=1, December=12. |
| [`DatetimeIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day.html#pandas.DatetimeIndex.day "pandas.DatetimeIndex.day") | The day of the datetime. |
| [`DatetimeIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.hour.html#pandas.DatetimeIndex.hour "pandas.DatetimeIndex.hour") | The hours of the datetime. |
| [`DatetimeIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.minute.html#pandas.DatetimeIndex.minute "pandas.DatetimeIndex.minute") | The minutes of the datetime. |
| [`DatetimeIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.second.html#pandas.DatetimeIndex.second "pandas.DatetimeIndex.second") | The seconds of the datetime. |
| [`DatetimeIndex.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.microsecond.html#pandas.DatetimeIndex.microsecond "pandas.DatetimeIndex.microsecond") | The microseconds of the datetime. |
| [`DatetimeIndex.nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.nanosecond.html#pandas.DatetimeIndex.nanosecond "pandas.DatetimeIndex.nanosecond") | The nanoseconds of the datetime. |
| [`DatetimeIndex.date`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.date.html#pandas.DatetimeIndex.date "pandas.DatetimeIndex.date") | Returns numpy array of python [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.15)")<br> objects. |
| [`DatetimeIndex.time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.time.html#pandas.DatetimeIndex.time "pandas.DatetimeIndex.time") | Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")<br> objects. |
| [`DatetimeIndex.timetz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.timetz.html#pandas.DatetimeIndex.timetz "pandas.DatetimeIndex.timetz") | Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")<br> objects with timezones. |
| [`DatetimeIndex.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.dayofyear.html#pandas.DatetimeIndex.dayofyear "pandas.DatetimeIndex.dayofyear") | (DEPRECATED) The ordinal day of the year. |
| [`DatetimeIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_year.html#pandas.DatetimeIndex.day_of_year "pandas.DatetimeIndex.day_of_year") | The ordinal day of the year. |
| [`DatetimeIndex.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.dayofweek.html#pandas.DatetimeIndex.dayofweek "pandas.DatetimeIndex.dayofweek") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`DatetimeIndex.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_of_week.html#pandas.DatetimeIndex.day_of_week "pandas.DatetimeIndex.day_of_week") | The day of the week with Monday=0, Sunday=6. |
| [`DatetimeIndex.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.weekday.html#pandas.DatetimeIndex.weekday "pandas.DatetimeIndex.weekday") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`DatetimeIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.quarter.html#pandas.DatetimeIndex.quarter "pandas.DatetimeIndex.quarter") | The quarter of the date. |
| [`DatetimeIndex.tz`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz.html#pandas.DatetimeIndex.tz "pandas.DatetimeIndex.tz") | Return the timezone. |
| [`DatetimeIndex.freq`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#pandas.DatetimeIndex.freq "pandas.DatetimeIndex.freq") | Return the frequency object if it is set, otherwise None. |
| [`DatetimeIndex.freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freqstr.html#pandas.DatetimeIndex.freqstr "pandas.DatetimeIndex.freqstr") | Return the frequency object as a string if it's set, otherwise None. |
| [`DatetimeIndex.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_start.html#pandas.DatetimeIndex.is_month_start "pandas.DatetimeIndex.is_month_start") | Indicates whether the date is the first day of the month. |
| [`DatetimeIndex.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_month_end.html#pandas.DatetimeIndex.is_month_end "pandas.DatetimeIndex.is_month_end") | Indicates whether the date is the last day of the month. |
| [`DatetimeIndex.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_start.html#pandas.DatetimeIndex.is_quarter_start "pandas.DatetimeIndex.is_quarter_start") | Indicator for whether the date is the first day of a quarter. |
| [`DatetimeIndex.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_quarter_end.html#pandas.DatetimeIndex.is_quarter_end "pandas.DatetimeIndex.is_quarter_end") | Indicator for whether the date is the last day of a quarter. |
| [`DatetimeIndex.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_start.html#pandas.DatetimeIndex.is_year_start "pandas.DatetimeIndex.is_year_start") | Indicate whether the date is the first day of a year. |
| [`DatetimeIndex.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_year_end.html#pandas.DatetimeIndex.is_year_end "pandas.DatetimeIndex.is_year_end") | Indicate whether the date is the last day of the year. |
| [`DatetimeIndex.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.is_leap_year.html#pandas.DatetimeIndex.is_leap_year "pandas.DatetimeIndex.is_leap_year") | Boolean indicator if the date belongs to a leap year. |
| [`DatetimeIndex.inferred_freq`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.inferred_freq.html#pandas.DatetimeIndex.inferred_freq "pandas.DatetimeIndex.inferred_freq") | (DEPRECATED) Return the inferred frequency of the index. |
| [`DatetimeIndex.asi8`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.asi8.html#pandas.DatetimeIndex.asi8 "pandas.DatetimeIndex.asi8") | Return Integer representation of the values. |
| [`DatetimeIndex.unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.unit.html#pandas.DatetimeIndex.unit "pandas.DatetimeIndex.unit") | The precision unit of the datetime data. |

### Selecting[#](https://pandas.pydata.org/docs/reference/indexing.html#id2 "Link to this heading")

|     |     |
| --- | --- |
| [`DatetimeIndex.indexer_at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_at_time.html#pandas.DatetimeIndex.indexer_at_time "pandas.DatetimeIndex.indexer_at_time")<br>(time\[, asof\]) | Return index locations of values at particular time of day. |
| [`DatetimeIndex.indexer_between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.indexer_between_time.html#pandas.DatetimeIndex.indexer_between_time "pandas.DatetimeIndex.indexer_between_time")<br>(...\[, ...\]) | Return index locations of values between particular times of day. |

### Time-specific operations[#](https://pandas.pydata.org/docs/reference/indexing.html#id3 "Link to this heading")

|     |     |
| --- | --- |
| [`DatetimeIndex.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.normalize.html#pandas.DatetimeIndex.normalize "pandas.DatetimeIndex.normalize")<br>() | Convert times to midnight. |
| [`DatetimeIndex.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.strftime.html#pandas.DatetimeIndex.strftime "pandas.DatetimeIndex.strftime")<br>(date\_format) | Convert to Index using specified date\_format. |
| [`DatetimeIndex.snap`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.snap.html#pandas.DatetimeIndex.snap "pandas.DatetimeIndex.snap")<br>(\[freq\]) | Snap time stamps to nearest occurring frequency. |
| [`DatetimeIndex.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_convert.html#pandas.DatetimeIndex.tz_convert "pandas.DatetimeIndex.tz_convert")<br>(tz) | Convert tz-aware Datetime Array/Index from one time zone to another. |
| [`DatetimeIndex.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.tz_localize.html#pandas.DatetimeIndex.tz_localize "pandas.DatetimeIndex.tz_localize")<br>(tz\[, ambiguous, ...\]) | Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index. |
| [`DatetimeIndex.round`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "pandas.DatetimeIndex.round")<br>(freq\[, ambiguous, ...\]) | Perform round operation on the data to the specified freq. |
| [`DatetimeIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")<br>(freq\[, ambiguous, ...\]) | Perform floor operation on the data to the specified freq. |
| [`DatetimeIndex.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.ceil.html#pandas.DatetimeIndex.ceil "pandas.DatetimeIndex.ceil")<br>(freq\[, ambiguous, ...\]) | Perform ceil operation on the data to the specified freq. |
| [`DatetimeIndex.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.month_name.html#pandas.DatetimeIndex.month_name "pandas.DatetimeIndex.month_name")<br>(\[locale\]) | Return the month names with specified locale. |
| [`DatetimeIndex.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.day_name.html#pandas.DatetimeIndex.day_name "pandas.DatetimeIndex.day_name")<br>(\[locale\]) | Return the day names with specified locale. |

### Conversion[#](https://pandas.pydata.org/docs/reference/indexing.html#id4 "Link to this heading")

|     |     |
| --- | --- |
| [`DatetimeIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.as_unit.html#pandas.DatetimeIndex.as_unit "pandas.DatetimeIndex.as_unit")<br>(unit) | Convert to a dtype with the given unit resolution. |
| [`DatetimeIndex.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_period.html#pandas.DatetimeIndex.to_period "pandas.DatetimeIndex.to_period")<br>(\[freq\]) | Cast to PeriodArray/PeriodIndex at a particular frequency. |
| [`DatetimeIndex.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html#pandas.DatetimeIndex.to_pydatetime "pandas.DatetimeIndex.to_pydatetime")<br>() | Return an ndarray of `datetime.datetime` objects. |
| [`DatetimeIndex.to_series`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html#pandas.DatetimeIndex.to_series "pandas.DatetimeIndex.to_series")<br>(\[index, name\]) | Create a Series with both index and values equal to the index keys. |
| [`DatetimeIndex.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_frame.html#pandas.DatetimeIndex.to_frame "pandas.DatetimeIndex.to_frame")<br>(\[index, name\]) | Create a DataFrame with a column containing the Index. |
| [`DatetimeIndex.to_julian_date`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_julian_date.html#pandas.DatetimeIndex.to_julian_date "pandas.DatetimeIndex.to_julian_date")<br>() | Convert Timestamp to a Julian Date. |

### Methods[#](https://pandas.pydata.org/docs/reference/indexing.html#methods "Link to this heading")

|     |     |
| --- | --- |
| [`DatetimeIndex.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.mean.html#pandas.DatetimeIndex.mean "pandas.DatetimeIndex.mean")<br>(\*\[, skipna, axis\]) | Return the mean value of the Array. |
| [`DatetimeIndex.std`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.std.html#pandas.DatetimeIndex.std "pandas.DatetimeIndex.std")<br>(\[axis, dtype, out, ddof, ...\]) | Return sample standard deviation over requested axis. |

TimedeltaIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#timedeltaindex "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")<br>(\[data, freq, dtype, copy, name\]) | Immutable Index of timedelta64 data. |

### Components[#](https://pandas.pydata.org/docs/reference/indexing.html#components "Link to this heading")

|     |     |
| --- | --- |
| [`TimedeltaIndex.days`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.days.html#pandas.TimedeltaIndex.days "pandas.TimedeltaIndex.days") | Number of days for each element. |
| [`TimedeltaIndex.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.seconds.html#pandas.TimedeltaIndex.seconds "pandas.TimedeltaIndex.seconds") | Number of seconds (>= 0 and less than 1 day) for each element. |
| [`TimedeltaIndex.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.microseconds.html#pandas.TimedeltaIndex.microseconds "pandas.TimedeltaIndex.microseconds") | Number of microseconds (>= 0 and less than 1 second) for each element. |
| [`TimedeltaIndex.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.nanoseconds.html#pandas.TimedeltaIndex.nanoseconds "pandas.TimedeltaIndex.nanoseconds") | Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. |
| [`TimedeltaIndex.components`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.components.html#pandas.TimedeltaIndex.components "pandas.TimedeltaIndex.components") | Return a DataFrame of the individual resolution components of the Timedeltas. |
| [`TimedeltaIndex.inferred_freq`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.inferred_freq.html#pandas.TimedeltaIndex.inferred_freq "pandas.TimedeltaIndex.inferred_freq") | (DEPRECATED) Return the inferred frequency of the index. |
| [`TimedeltaIndex.asi8`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.asi8.html#pandas.TimedeltaIndex.asi8 "pandas.TimedeltaIndex.asi8") | Return Integer representation of the values. |
| [`TimedeltaIndex.unit`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.unit.html#pandas.TimedeltaIndex.unit "pandas.TimedeltaIndex.unit") | The precision unit of the datetime data. |

### Conversion[#](https://pandas.pydata.org/docs/reference/indexing.html#id5 "Link to this heading")

|     |     |
| --- | --- |
| [`TimedeltaIndex.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.as_unit.html#pandas.TimedeltaIndex.as_unit "pandas.TimedeltaIndex.as_unit")<br>(unit) | Convert to a dtype with the given unit resolution. |
| [`TimedeltaIndex.to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_pytimedelta.html#pandas.TimedeltaIndex.to_pytimedelta "pandas.TimedeltaIndex.to_pytimedelta")<br>() | Return an ndarray of datetime.timedelta objects. |
| [`TimedeltaIndex.to_series`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_series.html#pandas.TimedeltaIndex.to_series "pandas.TimedeltaIndex.to_series")<br>(\[index, name\]) | Create a Series with both index and values equal to the index keys. |
| [`TimedeltaIndex.round`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.round.html#pandas.TimedeltaIndex.round "pandas.TimedeltaIndex.round")<br>(freq\[, ambiguous, ...\]) | Perform round operation on the data to the specified freq. |
| [`TimedeltaIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.floor.html#pandas.TimedeltaIndex.floor "pandas.TimedeltaIndex.floor")<br>(freq\[, ambiguous, ...\]) | Perform floor operation on the data to the specified freq. |
| [`TimedeltaIndex.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.ceil.html#pandas.TimedeltaIndex.ceil "pandas.TimedeltaIndex.ceil")<br>(freq\[, ambiguous, ...\]) | Perform ceil operation on the data to the specified freq. |
| [`TimedeltaIndex.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.to_frame.html#pandas.TimedeltaIndex.to_frame "pandas.TimedeltaIndex.to_frame")<br>(\[index, name\]) | Create a DataFrame with a column containing the Index. |

### Methods[#](https://pandas.pydata.org/docs/reference/indexing.html#id6 "Link to this heading")

|     |     |
| --- | --- |
| [`TimedeltaIndex.mean`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.mean.html#pandas.TimedeltaIndex.mean "pandas.TimedeltaIndex.mean")<br>(\*\[, skipna, axis\]) | Return the mean value of the Array. |

PeriodIndex[#](https://pandas.pydata.org/docs/reference/indexing.html#periodindex "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")<br>(\[data, freq, dtype, copy, name\]) | Immutable ndarray holding ordinal values indicating regular periods in time. |

### Properties[#](https://pandas.pydata.org/docs/reference/indexing.html#id7 "Link to this heading")

|     |     |
| --- | --- |
| [`PeriodIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day") | The days of the period. |
| [`PeriodIndex.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.dayofweek.html#pandas.PeriodIndex.dayofweek "pandas.PeriodIndex.dayofweek") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`PeriodIndex.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_week.html#pandas.PeriodIndex.day_of_week "pandas.PeriodIndex.day_of_week") | The day of the week with Monday=0, Sunday=6. |
| [`PeriodIndex.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.dayofyear.html#pandas.PeriodIndex.dayofyear "pandas.PeriodIndex.dayofyear") | (DEPRECATED) The ordinal day of the year. |
| [`PeriodIndex.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day_of_year.html#pandas.PeriodIndex.day_of_year "pandas.PeriodIndex.day_of_year") | The ordinal day of the year. |
| [`PeriodIndex.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas.PeriodIndex.days_in_month "pandas.PeriodIndex.days_in_month") | The number of days in the month. |
| [`PeriodIndex.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.daysinmonth.html#pandas.PeriodIndex.daysinmonth "pandas.PeriodIndex.daysinmonth") | (DEPRECATED) The number of days in the month. |
| [`PeriodIndex.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.end_time.html#pandas.PeriodIndex.end_time "pandas.PeriodIndex.end_time") | Get the Timestamp for the end of the period. |
| [`PeriodIndex.freq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.freq.html#pandas.PeriodIndex.freq "pandas.PeriodIndex.freq") | Return the frequency object if it is set, otherwise None. |
| [`PeriodIndex.freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.freqstr.html#pandas.PeriodIndex.freqstr "pandas.PeriodIndex.freqstr") | Return the frequency object as a string if it's set, otherwise None. |
| [`PeriodIndex.hour`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.hour.html#pandas.PeriodIndex.hour "pandas.PeriodIndex.hour") | The hour of the period. |
| [`PeriodIndex.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.is_leap_year.html#pandas.PeriodIndex.is_leap_year "pandas.PeriodIndex.is_leap_year") | Logical indicating if the date belongs to a leap year. |
| [`PeriodIndex.minute`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.minute.html#pandas.PeriodIndex.minute "pandas.PeriodIndex.minute") | The minute of the period. |
| [`PeriodIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas.PeriodIndex.month "pandas.PeriodIndex.month") | The month as January=1, December=12. |
| [`PeriodIndex.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.quarter.html#pandas.PeriodIndex.quarter "pandas.PeriodIndex.quarter") | The quarter of the date. |
| [`PeriodIndex.qyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.qyear.html#pandas.PeriodIndex.qyear "pandas.PeriodIndex.qyear") | Fiscal year the Period lies in according to its starting-quarter. |
| [`PeriodIndex.second`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.second.html#pandas.PeriodIndex.second "pandas.PeriodIndex.second") | The second of the period. |
| [`PeriodIndex.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.start_time.html#pandas.PeriodIndex.start_time "pandas.PeriodIndex.start_time") | Get the Timestamp for the start of the period. |
| [`PeriodIndex.week`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.week.html#pandas.PeriodIndex.week "pandas.PeriodIndex.week") | The week ordinal of the year. |
| [`PeriodIndex.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekday.html#pandas.PeriodIndex.weekday "pandas.PeriodIndex.weekday") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`PeriodIndex.weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.weekofyear.html#pandas.PeriodIndex.weekofyear "pandas.PeriodIndex.weekofyear") | The week ordinal of the year. |
| [`PeriodIndex.year`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.year.html#pandas.PeriodIndex.year "pandas.PeriodIndex.year") | The year of the period. |
| [`PeriodIndex.asi8`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asi8.html#pandas.PeriodIndex.asi8 "pandas.PeriodIndex.asi8") | Return Integer representation of the values. |

### Methods[#](https://pandas.pydata.org/docs/reference/indexing.html#id8 "Link to this heading")

|     |     |
| --- | --- |
| [`PeriodIndex.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.asfreq.html#pandas.PeriodIndex.asfreq "pandas.PeriodIndex.asfreq")<br>(\[freq, how\]) | Convert the PeriodIndex to the specified frequency freq. |
| [`PeriodIndex.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.strftime.html#pandas.PeriodIndex.strftime "pandas.PeriodIndex.strftime")<br>(date\_format) | Convert to Index using specified date\_format. |
| [`PeriodIndex.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.to_timestamp.html#pandas.PeriodIndex.to_timestamp "pandas.PeriodIndex.to_timestamp")<br>(\[freq, how\]) | Cast to DatetimeIndex. |
| [`PeriodIndex.from_fields`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_fields.html#pandas.PeriodIndex.from_fields "pandas.PeriodIndex.from_fields")<br>(\*\[, year, quarter, ...\]) | Construct a PeriodIndex from fields (year, month, day, etc.). |
| [`PeriodIndex.from_ordinals`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.from_ordinals.html#pandas.PeriodIndex.from_ordinals "pandas.PeriodIndex.from_ordinals")<br>(ordinals, \*, freq) | Construct a PeriodIndex from ordinals. |

On this page
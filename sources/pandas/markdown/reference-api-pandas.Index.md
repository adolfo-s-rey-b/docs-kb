[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas-index "Link to this heading")

====================================================================================================================

class pandas.Index(_data\=None_, _dtype\=None_, _copy\=None_, _name\=None_, _tupleize\_cols\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L315-L8251)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "Link to this definition")

Immutable sequence used for indexing and alignment.

The basic object storing axis labels for all pandas objects.

Changed in version 2.0.0: Index can hold all numpy numeric dtypes (except float16). Previously only int64/uint64/float64 dtypes were accepted.

Parameters:

**data**array-like (1-dimensional)

An array-like structure containing the data for the index. This could be a Python list, a NumPy array, or a pandas Series.

**dtype**str, numpy.dtype, or ExtensionDtype, optional

Data type for the output Index. If not specified, this will be inferred from data. See the [user guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)
 for more usages.

**copy**bool, default None

Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.

**name**object

Name to be stored in the index.

**tupleize\_cols**bool (default: True)

When True, attempt to create a MultiIndex if possible.

See also

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")

Index implementing a monotonic integer range.

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")

Index of [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 s.

[`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")

A multi-level, or hierarchical Index.

[`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")

An Index of [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 s.

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

Index of datetime64 data.

[`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")

Index of timedelta64 data.

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Index of Period data.

Notes

An Index instance can **only** contain hashable objects. An Index instance _can not_ hold numpy float16 dtype.

NumPy arrays with `dtype=object` are handled like other list-like inputs: pandas may infer a more specific dtype (for example `str` for an array of Python strings) instead of preserving NumPy object dtype. Values that NumPy already stores in a dedicated dtype (such as `int64` integers) are not altered in the same way. To force object dtype, pass `dtype=object`.

Examples

\>>> pd.Index(\[1, 2, 3\])
Index(\[1, 2, 3\], dtype='int64')

Copy to clipboard

\>>> pd.Index(list("abc"))
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

\>>> pd.Index(\[1, 2, 3\], dtype\="uint8")
Index(\[1, 2, 3\], dtype='uint8')

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`T`](https://pandas.pydata.org/docs/reference/api/pandas.Index.T.html#pandas.Index.T "pandas.Index.T") | Return the transpose, which is by definition self. |
| [`array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array") | The ExtensionArray of the data backing this Index. |
| [`dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dtype.html#pandas.Index.dtype "pandas.Index.dtype") | Return the dtype object of the underlying data. |
| [`empty`](https://pandas.pydata.org/docs/reference/api/pandas.Index.empty.html#pandas.Index.empty "pandas.Index.empty") | Indicator whether Index is empty. |
| [`has_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "pandas.Index.has_duplicates") | Check if the Index has duplicate values. |
| [`hasnans`](https://pandas.pydata.org/docs/reference/api/pandas.Index.hasnans.html#pandas.Index.hasnans "pandas.Index.hasnans") | Return True if there are any NaNs. |
| [`inferred_type`](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#pandas.Index.inferred_type "pandas.Index.inferred_type") | Return a string of the type inferred from the values. |
| [`is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas.Index.is_monotonic_decreasing "pandas.Index.is_monotonic_decreasing") | Return a boolean if the values are equal or decreasing. |
| [`is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas.Index.is_monotonic_increasing "pandas.Index.is_monotonic_increasing") | Return a boolean if the values are equal or increasing. |
| [`is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique") | Return if the index has unique values. |
| [`name`](https://pandas.pydata.org/docs/reference/api/pandas.Index.name.html#pandas.Index.name "pandas.Index.name") | Return Index or MultiIndex name. |
| [`names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.names.html#pandas.Index.names "pandas.Index.names") | Get names on index. |
| [`nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.Index.nbytes.html#pandas.Index.nbytes "pandas.Index.nbytes") | Return the number of bytes in the underlying data. |
| [`ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Index.ndim.html#pandas.Index.ndim "pandas.Index.ndim") | Number of dimensions of the underlying data, by definition 1. |
| `nlevels` | Number of levels. |
| [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.Index.shape.html#pandas.Index.shape "pandas.Index.shape") | Return a tuple of the shape of the underlying data. |
| [`size`](https://pandas.pydata.org/docs/reference/api/pandas.Index.size.html#pandas.Index.size "pandas.Index.size") | Return the number of elements in the underlying data. |
| [`values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "pandas.Index.values") | Return an array representing the data in the Index. |

Methods

|     |     |
| --- | --- |
| [`all`](https://pandas.pydata.org/docs/reference/api/pandas.Index.all.html#pandas.Index.all "pandas.Index.all")<br>(\*args, \*\*kwargs) | Return whether all elements are Truthy. |
| [`any`](https://pandas.pydata.org/docs/reference/api/pandas.Index.any.html#pandas.Index.any "pandas.Index.any")<br>(\*args, \*\*kwargs) | Return whether any element is Truthy. |
| [`append`](https://pandas.pydata.org/docs/reference/api/pandas.Index.append.html#pandas.Index.append "pandas.Index.append")<br>(other) | Append a collection of Index options together. |
| [`argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmax.html#pandas.Index.argmax "pandas.Index.argmax")<br>(\[axis, skipna\]) | Return int position of the largest value in the Index. |
| [`argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argmin.html#pandas.Index.argmin "pandas.Index.argmin")<br>(\[axis, skipna\]) | Return int position of the smallest value in the Index. |
| [`argsort`](https://pandas.pydata.org/docs/reference/api/pandas.Index.argsort.html#pandas.Index.argsort "pandas.Index.argsort")<br>(\*args, \*\*kwargs) | Return the integer indices that would sort the index. |
| [`asof`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof.html#pandas.Index.asof "pandas.Index.asof")<br>(label) | Return the label from the index, or, if not present, the previous one. |
| [`asof_locs`](https://pandas.pydata.org/docs/reference/api/pandas.Index.asof_locs.html#pandas.Index.asof_locs "pandas.Index.asof_locs")<br>(where, mask) | Return the locations (indices) of labels in the index. |
| [`astype`](https://pandas.pydata.org/docs/reference/api/pandas.Index.astype.html#pandas.Index.astype "pandas.Index.astype")<br>(dtype\[, copy\]) | Create an Index with values cast to dtypes. |
| [`copy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#pandas.Index.copy "pandas.Index.copy")<br>(\[name, deep\]) | Make a copy of this object. |
| [`delete`](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas.Index.delete "pandas.Index.delete")<br>(loc) | Make new Index with passed location(-s) deleted. |
| `diff`(\[periods\]) | Computes the difference between consecutive values in the Index object. |
| [`difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.difference.html#pandas.Index.difference "pandas.Index.difference")<br>(other\[, sort\]) | Return a new Index with elements of index not in other. |
| [`drop`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#pandas.Index.drop "pandas.Index.drop")<br>(labels\[, errors\]) | Make new Index with passed list of labels deleted. |
| [`drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop_duplicates.html#pandas.Index.drop_duplicates "pandas.Index.drop_duplicates")<br>(\*\[, keep\]) | Return Index with duplicate values removed. |
| [`droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Index.droplevel.html#pandas.Index.droplevel "pandas.Index.droplevel")<br>(\[level\]) | Return index with requested level(s) removed. |
| [`dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.dropna.html#pandas.Index.dropna "pandas.Index.dropna")<br>(\[how\]) | Return Index without NA/NaN values. |
| [`duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Index.duplicated.html#pandas.Index.duplicated "pandas.Index.duplicated")<br>(\[keep\]) | Indicate duplicate index values. |
| [`equals`](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas.Index.equals "pandas.Index.equals")<br>(other) | Determine if two Index object are equal. |
| [`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.Index.factorize.html#pandas.Index.factorize "pandas.Index.factorize")<br>(\[sort, use\_na\_sentinel\]) | Encode the object as an enumerated type or categorical variable. |
| [`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.fillna.html#pandas.Index.fillna "pandas.Index.fillna")<br>(value) | Fill NA/NaN values with the specified value. |
| [`get_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer.html#pandas.Index.get_indexer "pandas.Index.get_indexer")<br>(target\[, method, limit, tolerance\]) | Compute indexer and mask for new index given the current index. |
| [`get_indexer_for`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_for.html#pandas.Index.get_indexer_for "pandas.Index.get_indexer_for")<br>(target) | Guaranteed return of an indexer even when non-unique. |
| [`get_indexer_non_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_indexer_non_unique.html#pandas.Index.get_indexer_non_unique "pandas.Index.get_indexer_non_unique")<br>(target) | Compute indexer and mask for new index given the current index. |
| [`get_level_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_level_values.html#pandas.Index.get_level_values "pandas.Index.get_level_values")<br>(level) | Return an Index of values for requested level. |
| [`get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")<br>(key) | Get integer location, slice or boolean mask for requested label. |
| [`get_slice_bound`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "pandas.Index.get_slice_bound")<br>(label, side) | Calculate slice bound that corresponds to given label. |
| `groupby`(values) | Group the index labels by a given array of values. |
| [`identical`](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas.Index.identical "pandas.Index.identical")<br>(other) | Similar to equals, but checks that object attributes and types are also equal. |
| [`infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html#pandas.Index.infer_objects "pandas.Index.infer_objects")<br>(\[copy\]) | If we have an object dtype, try to infer a non-object dtype. |
| [`insert`](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas.Index.insert "pandas.Index.insert")<br>(loc, item) | Make new Index inserting new item at location. |
| [`intersection`](https://pandas.pydata.org/docs/reference/api/pandas.Index.intersection.html#pandas.Index.intersection "pandas.Index.intersection")<br>(other\[, sort\]) | Form the intersection of two Index objects. |
| [`is_`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_.html#pandas.Index.is_ "pandas.Index.is_")<br>(other) | More flexible, faster check like `is` but that works through views. |
| [`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isin.html#pandas.Index.isin "pandas.Index.isin")<br>(values\[, level\]) | Return a boolean array where the index values are in values. |
| [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.isna.html#pandas.Index.isna "pandas.Index.isna")<br>() | Detect missing values. |
| `isnull`() | Detect missing values. |
| [`item`](https://pandas.pydata.org/docs/reference/api/pandas.Index.item.html#pandas.Index.item "pandas.Index.item")<br>() | Return the first element of the underlying data as a Python scalar. |
| [`join`](https://pandas.pydata.org/docs/reference/api/pandas.Index.join.html#pandas.Index.join "pandas.Index.join")<br>(other, \*\[, how, level, ...\]) | Compute join\_index and indexers to conform data structures to the new index. |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.Index.map.html#pandas.Index.map "pandas.Index.map")<br>(mapper\[, na\_action\]) | Map values using an input mapping or function. |
| [`max`](https://pandas.pydata.org/docs/reference/api/pandas.Index.max.html#pandas.Index.max "pandas.Index.max")<br>(\[axis, skipna\]) | Return the maximum value of the Index. |
| [`memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Index.memory_usage.html#pandas.Index.memory_usage "pandas.Index.memory_usage")<br>(\[deep\]) | Memory usage of the values. |
| [`min`](https://pandas.pydata.org/docs/reference/api/pandas.Index.min.html#pandas.Index.min "pandas.Index.min")<br>(\[axis, skipna\]) | Return the minimum value of the Index. |
| [`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Index.notna.html#pandas.Index.notna "pandas.Index.notna")<br>() | Detect existing (non-missing) values. |
| `notnull`() | Detect existing (non-missing) values. |
| [`nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.nunique.html#pandas.Index.nunique "pandas.Index.nunique")<br>(\[dropna\]) | Return number of unique elements in the object. |
| [`putmask`](https://pandas.pydata.org/docs/reference/api/pandas.Index.putmask.html#pandas.Index.putmask "pandas.Index.putmask")<br>(mask, value) | Return a new Index of the values set with the mask. |
| [`ravel`](https://pandas.pydata.org/docs/reference/api/pandas.Index.ravel.html#pandas.Index.ravel "pandas.Index.ravel")<br>(\[order\]) | Return a view on self. |
| [`reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Index.reindex.html#pandas.Index.reindex "pandas.Index.reindex")<br>(target\[, method, level, limit, ...\]) | Create index with target's values. |
| [`rename`](https://pandas.pydata.org/docs/reference/api/pandas.Index.rename.html#pandas.Index.rename "pandas.Index.rename")<br>(name, \*\[, inplace\]) | Alter Index or MultiIndex name. |
| [`repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#pandas.Index.repeat "pandas.Index.repeat")<br>(repeats\[, axis\]) | Repeat elements of an Index. |
| [`replace`](https://pandas.pydata.org/docs/reference/api/pandas.Index.replace.html#pandas.Index.replace "pandas.Index.replace")<br>(\[to\_replace, value, regex\]) | Replace values in the Index. |
| `round`(\[decimals\]) | Round each value in the Index to the given number of decimals. |
| [`searchsorted`](https://pandas.pydata.org/docs/reference/api/pandas.Index.searchsorted.html#pandas.Index.searchsorted "pandas.Index.searchsorted")<br>(value\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`set_names`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")<br>(names, \*\[, level, inplace\]) | Set Index or MultiIndex name. |
| [`shift`](https://pandas.pydata.org/docs/reference/api/pandas.Index.shift.html#pandas.Index.shift "pandas.Index.shift")<br>(\[periods, freq\]) | Shift index by desired number of time frequency increments. |
| [`slice_indexer`](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_indexer.html#pandas.Index.slice_indexer "pandas.Index.slice_indexer")<br>(\[start, end, step\]) | Compute the slice indexer for input labels and step. |
| [`slice_locs`](https://pandas.pydata.org/docs/reference/api/pandas.Index.slice_locs.html#pandas.Index.slice_locs "pandas.Index.slice_locs")<br>(\[start, end, step\]) | Compute slice locations for input labels. |
| [`sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Index.sort_values.html#pandas.Index.sort_values "pandas.Index.sort_values")<br>(\*\[, return\_indexer, ascending, ...\]) | Return a sorted copy of the index. |
| `sortlevel`(\[level, ascending, ...\]) | For internal compatibility with the Index API. |
| [`symmetric_difference`](https://pandas.pydata.org/docs/reference/api/pandas.Index.symmetric_difference.html#pandas.Index.symmetric_difference "pandas.Index.symmetric_difference")<br>(other\[, result\_name, sort\]) | Compute the symmetric difference of two Index objects. |
| [`take`](https://pandas.pydata.org/docs/reference/api/pandas.Index.take.html#pandas.Index.take "pandas.Index.take")<br>(indices\[, axis, allow\_fill, fill\_value\]) | Return a new Index of the values selected by the indices. |
| `to_flat_index`() | Identity method. |
| [`to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_frame.html#pandas.Index.to_frame "pandas.Index.to_frame")<br>(\[index, name\]) | Create a DataFrame with a column containing the Index. |
| [`to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html#pandas.Index.to_list "pandas.Index.to_list")<br>() | Return a list of the values. |
| [`to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")<br>(\[dtype, copy, na\_value\]) | A NumPy ndarray representing the values in this Series or Index. |
| [`to_series`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_series.html#pandas.Index.to_series "pandas.Index.to_series")<br>(\[index, name\]) | Create a Series with both index and values equal to the index keys. |
| `tolist`() | Return a list of the values. |
| `transpose`(\*args, \*\*kwargs) | Return the transpose, which is by definition self. |
| [`union`](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "pandas.Index.union")<br>(other\[, sort\]) | Form the union of two Index objects. |
| [`unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.unique.html#pandas.Index.unique "pandas.Index.unique")<br>(\[level\]) | Return unique values in the index. |
| [`value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html#pandas.Index.value_counts "pandas.Index.value_counts")<br>(\[normalize, sort, ascending, ...\]) | Return a Series containing counts of unique values. |
| [`view`](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html#pandas.Index.view "pandas.Index.view")<br>(\[cls\]) | Return a view of the Index with the specified dtype or a new Index instance. |
| [`where`](https://pandas.pydata.org/docs/reference/api/pandas.Index.where.html#pandas.Index.where "pandas.Index.where")<br>(cond\[, other\]) | Replace values where the condition is False. |

On this page
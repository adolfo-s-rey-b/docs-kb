[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas-api-extensions-extensionarray "Link to this heading")

============================================================================================================================================================================================

class pandas.api.extensions.ExtensionArray[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L122-L3236)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "Link to this definition")

Abstract base class for custom 1-D array types.

pandas will recognize instances of this class as proper arrays with a custom type and will not attempt to coerce them to objects. They may be stored directly inside a `DataFrame` or `Series`.

Attributes

|     |     |
| --- | --- |
| [`dtype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dtype.html#pandas.api.extensions.ExtensionArray.dtype "pandas.api.extensions.ExtensionArray.dtype") | An instance of ExtensionDtype. |
| [`nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.nbytes.html#pandas.api.extensions.ExtensionArray.nbytes "pandas.api.extensions.ExtensionArray.nbytes") | The number of bytes needed to store this object in memory. |
| [`ndim`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ndim.html#pandas.api.extensions.ExtensionArray.ndim "pandas.api.extensions.ExtensionArray.ndim") | Extension Arrays are only allowed to be 1-dimensional. |
| [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shape.html#pandas.api.extensions.ExtensionArray.shape "pandas.api.extensions.ExtensionArray.shape") | Return a tuple of the array dimensions. |

Methods

|     |     |
| --- | --- |
| [`argsort`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.argsort.html#pandas.api.extensions.ExtensionArray.argsort "pandas.api.extensions.ExtensionArray.argsort")<br>(\*\[, ascending, kind, na\_position\]) | Return the indices that would sort this array. |
| [`astype`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.astype.html#pandas.api.extensions.ExtensionArray.astype "pandas.api.extensions.ExtensionArray.astype")<br>(dtype\[, copy\]) | Cast to a NumPy array or ExtensionArray with 'dtype'. |
| [`copy`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.copy.html#pandas.api.extensions.ExtensionArray.copy "pandas.api.extensions.ExtensionArray.copy")<br>() | Return a copy of the array. |
| [`count`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.count.html#pandas.api.extensions.ExtensionArray.count "pandas.api.extensions.ExtensionArray.count")<br>() | Count the number of non-NA values in the array. |
| [`dropna`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.dropna.html#pandas.api.extensions.ExtensionArray.dropna "pandas.api.extensions.ExtensionArray.dropna")<br>() | Return ExtensionArray without NA values. |
| [`duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.duplicated.html#pandas.api.extensions.ExtensionArray.duplicated "pandas.api.extensions.ExtensionArray.duplicated")<br>(\[keep\]) | Return boolean ndarray denoting duplicate values. |
| [`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "pandas.api.extensions.ExtensionArray.factorize")<br>(\[use\_na\_sentinel\]) | Encode the extension array as an enumerated type. |
| [`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html#pandas.api.extensions.ExtensionArray.fillna "pandas.api.extensions.ExtensionArray.fillna")<br>(value\[, limit, copy\]) | Fill NA/NaN values using the specified method. |
| [`equals`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.equals.html#pandas.api.extensions.ExtensionArray.equals "pandas.api.extensions.ExtensionArray.equals")<br>(other) | Return if another array is equivalent to this array. |
| [`insert`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.insert.html#pandas.api.extensions.ExtensionArray.insert "pandas.api.extensions.ExtensionArray.insert")<br>(loc, item) | Insert an item at the given position. |
| [`interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.interpolate.html#pandas.api.extensions.ExtensionArray.interpolate "pandas.api.extensions.ExtensionArray.interpolate")<br>(\*, method, axis, index, limit, ...) | Fill NaN values using an interpolation method. |
| [`isin`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isin.html#pandas.api.extensions.ExtensionArray.isin "pandas.api.extensions.ExtensionArray.isin")<br>(values) | Pointwise comparison for set containment in the given values. |
| [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.isna.html#pandas.api.extensions.ExtensionArray.isna "pandas.api.extensions.ExtensionArray.isna")<br>() | A 1-D array indicating if each value is missing. |
| [`item`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.item.html#pandas.api.extensions.ExtensionArray.item "pandas.api.extensions.ExtensionArray.item")<br>(\[index\]) | Return the array element at the specified position as a Python scalar. |
| [`ravel`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.ravel.html#pandas.api.extensions.ExtensionArray.ravel "pandas.api.extensions.ExtensionArray.ravel")<br>(\[order\]) | Return a flattened view on this array. |
| [`repeat`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.repeat.html#pandas.api.extensions.ExtensionArray.repeat "pandas.api.extensions.ExtensionArray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an ExtensionArray. |
| [`searchsorted`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.searchsorted.html#pandas.api.extensions.ExtensionArray.searchsorted "pandas.api.extensions.ExtensionArray.searchsorted")<br>(value\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`shift`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shift.html#pandas.api.extensions.ExtensionArray.shift "pandas.api.extensions.ExtensionArray.shift")<br>(\[periods, fill\_value\]) | Shift values by desired number. |
| [`sort`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.sort.html#pandas.api.extensions.ExtensionArray.sort "pandas.api.extensions.ExtensionArray.sort")<br>(\*\[, ascending, kind, na\_position\]) | Sort the array in-place. |
| [`take`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html#pandas.api.extensions.ExtensionArray.take "pandas.api.extensions.ExtensionArray.take")<br>(indices, \*\[, allow\_fill, fill\_value\]) | Take elements from an array. |
| [`tolist`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.tolist.html#pandas.api.extensions.ExtensionArray.tolist "pandas.api.extensions.ExtensionArray.tolist")<br>() | Return a list of the values. |
| [`unique`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.unique.html#pandas.api.extensions.ExtensionArray.unique "pandas.api.extensions.ExtensionArray.unique")<br>() | Compute the ExtensionArray of unique values. |
| [`view`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.view.html#pandas.api.extensions.ExtensionArray.view "pandas.api.extensions.ExtensionArray.view")<br>(\[dtype\]) | Return a view on the array. |
| [`_accumulate`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._accumulate.html#pandas.api.extensions.ExtensionArray._accumulate "pandas.api.extensions.ExtensionArray._accumulate")<br>(name, \*\[, skipna\]) | Return an ExtensionArray performing an accumulation operation. |
| [`_concat_same_type`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._concat_same_type.html#pandas.api.extensions.ExtensionArray._concat_same_type "pandas.api.extensions.ExtensionArray._concat_same_type")<br>(to\_concat) | Concatenate multiple arrays of this dtype. |
| [`_explode`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._explode.html#pandas.api.extensions.ExtensionArray._explode "pandas.api.extensions.ExtensionArray._explode")<br>() | Transform each element of list-like to a row. |
| [`_formatter`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._formatter.html#pandas.api.extensions.ExtensionArray._formatter "pandas.api.extensions.ExtensionArray._formatter")<br>(\[boxed\]) | Formatting function for scalar values. |
| [`_from_factorized`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_factorized.html#pandas.api.extensions.ExtensionArray._from_factorized "pandas.api.extensions.ExtensionArray._from_factorized")<br>(values, original) | Reconstruct an ExtensionArray after factorization. |
| [`_from_sequence`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence.html#pandas.api.extensions.ExtensionArray._from_sequence "pandas.api.extensions.ExtensionArray._from_sequence")<br>(scalars, \*\[, dtype, copy\]) | Construct a new ExtensionArray from a sequence of scalars. |
| [`_from_sequence_of_strings`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._from_sequence_of_strings.html#pandas.api.extensions.ExtensionArray._from_sequence_of_strings "pandas.api.extensions.ExtensionArray._from_sequence_of_strings")<br>(strings, \*, dtype) | Construct a new ExtensionArray from a sequence of strings. |
| [`_hash_pandas_object`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._hash_pandas_object.html#pandas.api.extensions.ExtensionArray._hash_pandas_object "pandas.api.extensions.ExtensionArray._hash_pandas_object")<br>(\*, encoding, hash\_key, ...) | Hook for hash\_pandas\_object. |
| [`_is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_decreasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_decreasing "pandas.api.extensions.ExtensionArray._is_monotonic_decreasing") | Return True if the array values are monotonically decreasing. |
| [`_is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._is_monotonic_increasing.html#pandas.api.extensions.ExtensionArray._is_monotonic_increasing "pandas.api.extensions.ExtensionArray._is_monotonic_increasing") | Return True if the array values are monotonically increasing. |
| [`_pad_or_backfill`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._pad_or_backfill.html#pandas.api.extensions.ExtensionArray._pad_or_backfill "pandas.api.extensions.ExtensionArray._pad_or_backfill")<br>(\*, method\[, limit, ...\]) | Pad or backfill values, used by Series/DataFrame ffill and bfill. |
| [`_reduce`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html#pandas.api.extensions.ExtensionArray._reduce "pandas.api.extensions.ExtensionArray._reduce")<br>(name, \*\[, skipna, keepdims\]) | Return a scalar result of performing the reduction operation. |
| [`_values_for_argsort`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_argsort.html#pandas.api.extensions.ExtensionArray._values_for_argsort "pandas.api.extensions.ExtensionArray._values_for_argsort")<br>() | Return values for sorting. |
| [`_values_for_factorize`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._values_for_factorize.html#pandas.api.extensions.ExtensionArray._values_for_factorize "pandas.api.extensions.ExtensionArray._values_for_factorize")<br>() | Return an array and missing value suitable for factorization. |

See also

`api.extensions.ExtensionDtype`

A custom data type, to be paired with an ExtensionArray.

`api.extensions.ExtensionArray.dtype`

An instance of ExtensionDtype.

Notes

The interface includes the following abstract methods that must be implemented by subclasses:

*   \_from\_sequence
    
*   \_from\_factorized
    
*   \_\_getitem\_\_
    
*   \_\_len\_\_
    
*   \_\_eq\_\_
    
*   dtype
    
*   nbytes
    
*   isna
    
*   take
    
*   copy
    
*   \_concat\_same\_type
    
*   interpolate
    

A default repr displaying the type, (truncated) data, length, and dtype is provided. It can be customized or replaced by overriding:

*   \_\_repr\_\_ : A default repr for the ExtensionArray.
    
*   \_formatter : Print scalars inside a Series or DataFrame.
    

Some methods require casting the ExtensionArray to an ndarray of Python objects with `self.astype(object)`, which may be expensive. When performance is a concern, we highly recommend overriding the following methods:

*   fillna
    
*   \_pad\_or\_backfill
    
*   dropna
    
*   unique
    
*   factorize / \_values\_for\_factorize
    
*   argsort, argmax, argmin / \_values\_for\_argsort
    
*   searchsorted
    
*   map
    

The remaining methods implemented on this class should be performant, as they only compose abstract methods. Still, a more efficient implementation may be available, and these methods can be overridden.

One can implement methods to handle array accumulations or reductions.

*   \_accumulate
    
*   \_reduce
    

One can implement methods to handle parsing from strings that will be used in methods such as `pandas.io.parsers.read_csv`.

*   \_from\_sequence\_of\_strings
    

This class does not inherit from ‘abc.ABCMeta’ for performance reasons. Methods and properties required by the interface raise `pandas.errors.AbstractMethodError` and no `register` method is provided for registering virtual subclasses.

ExtensionArrays are limited to 1 dimension.

They may be backed by none, one, or many NumPy arrays. For example, `pandas.Categorical` is an extension array backed by two arrays, one for codes and one for categories. An array of IPv6 address may be backed by a NumPy structured array with two fields, one for the lower 64 bits and one for the upper 64 bits. Or they may be backed by some other storage type, like Python lists. Pandas makes no assumptions on how the data are stored, just that it can be converted to a NumPy array. The ExtensionArray interface does not impose any rules on how this data is stored. However, currently, the backing data cannot be stored in attributes called `.values` or `._values` to ensure full compatibility with pandas internals. But other names as `.data`, `._data`, `._items`, … can be freely used.

If implementing NumPy’s `__array_ufunc__` interface, pandas expects that

1.  You defer by returning `NotImplemented` when any Series are present in inputs. Pandas will extract the arrays and call the ufunc again.
    
2.  You define a `_HANDLED_TYPES` tuple as an attribute on the class. Pandas inspect this to determine whether the ufunc is valid for the types present.
    

See [NumPy universal functions](https://pandas.pydata.org/docs/development/extending.html#extending-extension-ufunc)
 for more.

By default, ExtensionArrays are not hashable. Immutable subclasses may override this behavior.

Examples

Please see the following:

[pandas-dev/pandas](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/extension/list/array.py)

On this page
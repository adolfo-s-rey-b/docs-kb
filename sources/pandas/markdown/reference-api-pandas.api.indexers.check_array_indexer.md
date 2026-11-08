[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.check_array_indexer.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.indexers.check_array_indexer.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.check_array_indexer.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.indexers.check_array_indexer.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.indexers.check_array_indexer.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.indexers.check_array_indexer.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.indexers.check_array_indexer.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.indexers.check_array_indexer.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.indexers.check_array_indexer.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.indexers.check\_array\_indexer[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.check_array_indexer.html#pandas-api-indexers-check-array-indexer "Link to this heading")

=======================================================================================================================================================================================================

pandas.api.indexers.check\_array\_indexer(_array_, _indexer_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexers/utils.py#L442-L585)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.check_array_indexer.html#pandas.api.indexers.check_array_indexer "Link to this definition")

Check if indexer is a valid array indexer for array.

For a boolean mask, array and indexer are checked to have the same length. The dtype is validated, and if it is an integer or boolean ExtensionArray, it is checked if there are missing values present, and it is converted to the appropriate numpy array. Other dtypes will raise an error.

Non-array indexers (integer, slice, Ellipsis, tuples, ..) are passed through as is.

Parameters:

**array**array-like

The array that is being indexed (only used for the length).

**indexer**array-like, list-like, int, slice, or other indexer

The indexer used for indexing. Array-like and list-like inputs that are not yet a numpy array or an ExtensionArray are converted to one. Non-array indexers (int, slice, Ellipsis, tuples, etc.) are passed through as is.

Returns:

numpy.ndarray

The validated indexer as a numpy array that can be used to index.

Raises:

IndexError

When the lengths don’t match.

ValueError

When indexer cannot be converted to a numpy ndarray to index (e.g. presence of missing values).

See also

`api.types.is_bool_dtype`

Check if key is of boolean dtype.

Examples

When checking a boolean mask, a boolean ndarray is returned when the arguments are all valid.

\>>> mask \= pd.array(\[True, False\])
\>>> arr \= pd.array(\[1, 2\])
\>>> pd.api.indexers.check\_array\_indexer(arr, mask)
array(\[ True, False\])

Copy to clipboard

An IndexError is raised when the lengths don’t match.

\>>> mask \= pd.array(\[True, False, True\])
\>>> pd.api.indexers.check\_array\_indexer(arr, mask)
Traceback (most recent call last):
...
IndexError: Boolean index has wrong length: 3 instead of 2.

Copy to clipboard

NA values in a boolean array are treated as False.

\>>> mask \= pd.array(\[True, pd.NA\])
\>>> pd.api.indexers.check\_array\_indexer(arr, mask)
array(\[ True, False\])

Copy to clipboard

A numpy boolean mask will get passed through (if the length is correct):

\>>> mask \= np.array(\[True, False\])
\>>> pd.api.indexers.check\_array\_indexer(arr, mask)
array(\[ True, False\])

Copy to clipboard

Integer and slice indexers are passed through as is:

\>>> pd.api.indexers.check\_array\_indexer(arr, 1)
1
\>>> pd.api.indexers.check\_array\_indexer(arr, slice(0, 1, 1))
slice(0, 1, 1)

Copy to clipboard

Similarly for integer indexers, an integer ndarray is returned when it is a valid indexer, otherwise an error is (for integer indexers, a matching length is not required):

\>>> indexer \= pd.array(\[0, 2\], dtype\="Int64")
\>>> arr \= pd.array(\[1, 2, 3\])
\>>> pd.api.indexers.check\_array\_indexer(arr, indexer)
array(\[0, 2\])

Copy to clipboard

\>>> indexer \= pd.array(\[0, pd.NA\], dtype\="Int64")
\>>> pd.api.indexers.check\_array\_indexer(arr, indexer)
Traceback (most recent call last):
...
ValueError: Cannot index with an integer indexer containing NA values

Copy to clipboard

For non-integer/boolean dtypes, an appropriate error is raised:

\>>> indexer \= np.array(\[0.0, 2.0\], dtype\="float64")
\>>> pd.api.indexers.check\_array\_indexer(arr, indexer)
Traceback (most recent call last):
...
IndexError: arrays used as indices must be of integer or boolean type

Copy to clipboard

On this page
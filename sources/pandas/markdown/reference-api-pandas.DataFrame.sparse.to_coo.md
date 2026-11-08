[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sparse.to\_coo[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html#pandas-dataframe-sparse-to-coo "Link to this heading")

===========================================================================================================================================================================

DataFrame.sparse.to\_coo()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L412-L473)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html#pandas.DataFrame.sparse.to_coo "Link to this definition")

Return the contents of the frame as a sparse SciPy COO matrix.

This method converts the DataFrame to a scipy COO (Coordinate) sparse matrix format for interoperability with scipy.sparse routines.

Returns:

scipy.sparse.spmatrix

If the caller is heterogeneous and contains booleans or objects, the result will be of dtype=object. See Notes.

Raises:

ValueError

If any column’s `fill_value` is not zero.

See also

[`DataFrame.sparse.to_dense`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html#pandas.DataFrame.sparse.to_dense "pandas.DataFrame.sparse.to_dense")

Convert a DataFrame with sparse values to dense.

Notes

The dtype will be the lowest-common-denominator type (implicit upcasting); that is to say if the dtypes (even of numeric types) are mixed, the one that accommodates all will be chosen.

e.g. If the dtypes are float16 and float32, dtype will be upcast to float32. By numpy.find\_common\_type convention, mixing int64 and and uint64 will result in a float64 dtype.

Examples

\>>> df \= pd.DataFrame({"A": pd.arrays.SparseArray(\[0, 1, 0, 1\])})
\>>> df.sparse.to\_coo()
<COOrdinate sparse matrix of dtype 'int64'
    with 2 stored elements and shape (4, 1)>

Copy to clipboard

On this page
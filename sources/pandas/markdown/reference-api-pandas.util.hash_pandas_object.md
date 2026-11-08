[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.util.hash_pandas_object.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.util.hash_pandas_object.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.util.hash_pandas_object.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.util.hash_pandas_object.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.util.hash_pandas_object.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.util.hash_pandas_object.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.util.hash_pandas_object.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.util.hash_pandas_object.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.util.hash_pandas_object.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.util.hash_pandas_object.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.util.hash_pandas_object.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.util.hash_pandas_object.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.util.hash\_pandas\_object[#](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html#pandas-util-hash-pandas-object "Link to this heading")

============================================================================================================================================================================

pandas.util.hash\_pandas\_object(_obj_, _index\=True_, _encoding\='utf8'_, _hash\_key\='0123456789123456'_, _categorize\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/util/hashing.py#L87-L227)
[#](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html#pandas.util.hash_pandas_object "Link to this definition")

Return a data hash of the Index/Series/DataFrame.

The hash is computed element-wise using the underlying data values, and optionally includes the index when hashing a Series or DataFrame.

Parameters:

**obj**Index, Series, or DataFrame

The pandas object to hash.

**index**bool, default True

Include the index in the hash (if Series/DataFrame). When True, the hash for each row depends on both the value and the index label, so the same value at a different index position will produce a different hash.

**encoding**str, default ‘utf8’

Encoding for data & key when strings.

**hash\_key**str, default \_default\_hash\_key

Hash\_key for string key to encode.

**categorize**bool, default True

Whether to first categorize object arrays before hashing. This is more efficient when the array contains duplicate values.

Returns:

Series of uint64

Same length as the object.

See also

`util.hash_array`

Return a hash of the given array.

`util.hash_tuples`

Hash a MultiIndex or listlike-of-tuples efficiently.

Examples

\>>> pd.util.hash\_pandas\_object(pd.Series(\[1, 2, 3\]))
0    14639053686158035780
1     3869563279212530728
2      393322362522515241
dtype: uint64

Copy to clipboard

By default, the hash includes the index, so the same value at a different index position will produce a different hash:

\>>> df1 \= pd.DataFrame({"a": \["a", "b", "c"\]})
\>>> df2 \= pd.DataFrame({"a": \["b", "a", "c"\]})
\>>> pd.util.hash\_pandas\_object(df1)
0     4578374827886788867
1    17338122309987883691
2     5473791562133574857
dtype: uint64
\>>> pd.util.hash\_pandas\_object(df2)
0     8168238220198793318
1    14044658390916132862
2     5473791562133574857
dtype: uint64

Copy to clipboard

Set `index=False` to hash only the values. In this case, the same value always produces the same hash regardless of its position:

\>>> pd.util.hash\_pandas\_object(df1, index\=False)
0     5694802365760992243
1     2797248057711234736
2    18202460376300699891
dtype: uint64
\>>> pd.util.hash\_pandas\_object(df2, index\=False)
0     2797248057711234736
1     5694802365760992243
2    18202460376300699891
dtype: uint64

Copy to clipboard

On this page
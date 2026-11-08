[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.util.hash_array.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.util.hash_array.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.util.hash_array.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.util.hash_array.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.util.hash_array.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.util.hash_array.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.util.hash_array.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.util.hash_array.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.util.hash_array.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.util.hash_array.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.util.hash_array.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.util.hash_array.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.util.hash\_array[#](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html#pandas-util-hash-array "Link to this heading")

===================================================================================================================================================

pandas.util.hash\_array(_vals_, _encoding\='utf8'_, _hash\_key\='0123456789123456'_, _categorize\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/util/hashing.py#L280-L336)
[#](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html#pandas.util.hash_array "Link to this definition")

Given a 1d array, return an array of deterministic integers.

This function applies a hash function to each element of the input array, producing a fixed set of uint64 values suitable for use in hashing-based algorithms.

Parameters:

**vals**ndarray or ExtensionArray

The input array to hash.

**encoding**str, default ‘utf8’

Encoding for data & key when strings.

**hash\_key**str, default \_default\_hash\_key

Hash\_key for string key to encode.

**categorize**bool, default True

Whether to first categorize object arrays before hashing. This is more efficient when the array contains duplicate values.

Returns:

ndarray\[np.uint64, ndim=1\]

Hashed values, same length as the vals.

See also

`util.hash_pandas_object`

Return a data hash of the Index/Series/DataFrame.

`util.hash_tuples`

Hash a MultiIndex / listlike-of-tuples efficiently.

Examples

\>>> pd.util.hash\_array(np.array(\[1, 2, 3\]))
array(\[ 6238072747940578789, 15839785061582574730,  2185194620014831856\],
  dtype=uint64)

Copy to clipboard

On this page
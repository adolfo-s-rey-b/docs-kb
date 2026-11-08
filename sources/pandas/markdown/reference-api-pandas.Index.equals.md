[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.equals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.equals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.equals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.equals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.equals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.equals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.equals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.equals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.equals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.equals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.equals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.equals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.equals[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas-index-equals "Link to this heading")

=========================================================================================================================================

Index.equals(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5854-L5954)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.equals.html#pandas.Index.equals "Link to this definition")

Determine if two Index object are equal.

The things that are being compared are:

*   The elements inside the Index object.
    
*   The order of the elements inside the Index object.
    

Parameters:

**other**Any

The other object to compare against.

Returns:

bool

True if “other” is an Index and it has the same elements and order as the calling index; False otherwise.

See also

[`Index.identical`](https://pandas.pydata.org/docs/reference/api/pandas.Index.identical.html#pandas.Index.identical "pandas.Index.identical")

Checks that object attributes and types are also equal.

[`Index.has_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Index.has_duplicates.html#pandas.Index.has_duplicates "pandas.Index.has_duplicates")

Check if the Index has duplicate values.

[`Index.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique")

Return if the index has unique values.

Examples

\>>> idx1 \= pd.Index(\[1, 2, 3\])
\>>> idx1
Index(\[1, 2, 3\], dtype='int64')
\>>> idx1.equals(pd.Index(\[1, 2, 3\]))
True

Copy to clipboard

The elements inside are compared

\>>> idx2 \= pd.Index(\["1", "2", "3"\])
\>>> idx2
Index(\['1', '2', '3'\], dtype='str')

Copy to clipboard

\>>> idx1.equals(idx2)
False

Copy to clipboard

The order is compared

\>>> ascending\_idx \= pd.Index(\[1, 2, 3\])
\>>> ascending\_idx
Index(\[1, 2, 3\], dtype='int64')
\>>> descending\_idx \= pd.Index(\[3, 2, 1\])
\>>> descending\_idx
Index(\[3, 2, 1\], dtype='int64')
\>>> ascending\_idx.equals(descending\_idx)
False

Copy to clipboard

The dtype is _not_ compared

\>>> int64\_idx \= pd.Index(\[1, 2, 3\], dtype\="int64")
\>>> int64\_idx
Index(\[1, 2, 3\], dtype='int64')
\>>> uint64\_idx \= pd.Index(\[1, 2, 3\], dtype\="uint64")
\>>> uint64\_idx
Index(\[1, 2, 3\], dtype='uint64')
\>>> int64\_idx.equals(uint64\_idx)
True

Copy to clipboard

On this page
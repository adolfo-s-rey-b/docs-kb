[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.get_slice_bound.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.get_slice_bound.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.get_slice_bound.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.get_slice_bound.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.get_slice_bound.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.get_slice_bound.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.get_slice_bound.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.get_slice_bound.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.get_slice_bound.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.get_slice_bound.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.get_slice_bound.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.get_slice_bound.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.get\_slice\_bound[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas-index-get-slice-bound "Link to this heading")

======================================================================================================================================================================

Index.get\_slice\_bound(_label_, _side_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7247-L7333)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_slice_bound.html#pandas.Index.get_slice_bound "Link to this definition")

Calculate slice bound that corresponds to given label.

Returns leftmost (one-past-the-rightmost if `side=='right'`) position of given label.

Parameters:

**label**object

The label for which to calculate the slice bound.

**side**{‘left’, ‘right’}

if ‘left’ return leftmost position of given label. if ‘right’ return one-past-the-rightmost position of given label.

Returns:

int

Index of label.

See also

[`Index.get_loc`](https://pandas.pydata.org/docs/reference/api/pandas.Index.get_loc.html#pandas.Index.get_loc "pandas.Index.get_loc")

Get integer location, slice or boolean mask for requested label.

Examples

\>>> idx \= pd.RangeIndex(5)
\>>> idx.get\_slice\_bound(3, "left")
3

Copy to clipboard

\>>> idx.get\_slice\_bound(3, "right")
4

Copy to clipboard

If `label` is non-unique in the index, an error will be raised.

\>>> idx\_duplicate \= pd.Index(\["a", "b", "a", "c", "d"\])
\>>> idx\_duplicate.get\_slice\_bound("a", "left")
Traceback (most recent call last):
KeyError: Cannot get left slice bound for non-unique label: 'a'

Copy to clipboard

On this page